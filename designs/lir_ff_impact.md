# VALORIA — BOARD GAME FAIL FORWARD SYSTEM
## Patch: PP-177
## Status: WORKING DESIGN — not yet committed
## Date: 2026-04-02
## Authority: stage1_core_engine §1.6 → this document (BG-mode operationalisation)
## Affects: params_board_game.md, params_board_game_history.md

---

## 1. DESIGN MANDATE

Fail Forward (FF) is stated in `stage1_core_engine §1.6`:
> "Failure does not halt the narrative. In both cases, the story moves forward."

Current BG gap: Failure outcomes for Domain Actions produce only a wasted action slot — no complication, no state change, no narrative advancement. Partial outcomes produce reduced effect only (not goal-with-complication).

This document defines BG-mode FF as:
- **Partial:** Goal is achieved, but a complication fires
- **Failure:** Goal is not achieved, and a complication fires

The complication must be: **immediate**, **legible without GM**, **state-changing**, and **proportionate** to the action type.

---

## 2. COMPLICATION STRUCTURE

Each BG Domain Action type has a Failure complication and a Partial complication. These fire automatically at resolution — no GM ruling required.

### 2.1 Complication Tiers

| Tier | Severity | Used for |
|------|----------|----------|
| Minor | Standing −1 OR Public Instability +1 (acting faction's choice) | Partial outcomes |
| Moderate | Mandatory consequence from action-type table below | Failure outcomes |
| Severe | Moderate consequence + Stability −1 | Failure on Ob ≥ 4 only |

Minor complication rule: the acting faction chooses which minor consequence applies. This preserves player agency within the FF structure.

---

## 3. ACTION-TYPE COMPLICATION TABLE

| Domain Action | Partial Complication (Minor — player chooses 1) | Failure Complication (Moderate — mandatory) |
|---------------|--------------------------------------------------|----------------------------------------------|
| Govern (Inward) | Standing −1 OR Public Instability +1 | Prosperity −1 in target territory |
| Trade (Outward) | Standing −1 OR Wealth −1 this season | Wealth −1 (permanent until Accounting) |
| Muster (Inward) | Unit mustered at Cohesion −1 OR Standing −1 | No unit mustered; Wealth −1 (materials wasted) |
| Diplomacy (Outward) | Standing −1 OR target faction's Standing +1 | Target faction gains Casus Belli vs acting faction (Ob 3 to dismiss) |
| Decree (Inward) | Mandate −1 for 1 season OR Public Instability +1 | Mandate −1 (permanent until Accounting) |
| Parliamentary Manoeuvre | Standing −1 OR no effect (already: Partial = no effect; Minor added) | Mandate −1 + opponent faction Standing +1 |
| Investigate (Inward) | Information gained is incomplete (GM notes one datum as unreliable) OR Standing −1 | No information gained; Stability −1 (internal leaks suspected) |
| Spy (Outward) | Intel gained but acting faction identity exposed OR Standing −1 | No intel gained; target faction may take one free Intel action vs acting faction next season |
| Thread Operation | Ob +1 to next Thread op in this territory (Thread Debt token) OR Rendering Stability −1 | Thread Debt token placed; Rendering Stability −2 |
| Community Organising | +1 Ob to next Community action in this territory OR Standing −1 | No progress; Institutional Pressure +1 |
| Fortify | Fortification begun at −1 Cohesion for resulting unit OR Standing −1 | No fortification; Wealth −1 |
| March / Military | See Battle Resolution (separate system) | See Battle Resolution |
| Parliamentary Vote | Losing margin halved (effect reduced) OR Public Instability −1 | Calling faction Mandate −1 + Public Instability −1 |

**Notes:**
- "Permanent until Accounting" means the effect persists until Phase 5 Seasonal Accounting, at which point it has already been applied.
- Casus Belli from Diplomacy Failure: uses standard Casus Belli rules; expires 3 seasons unused.
- Spy identity exposure: target faction's Intel track check next season (Ob 2; success = acting faction Intel −1).

---

## 4. INTEGRATION WITH EXISTING OUTCOMES

### 4.1 Parliamentary Manoeuvre (PP-170 update)

PP-170 stated: "Partial: No effect." Under FF this becomes:

| Degree | Effect |
|--------|--------|
| Overwhelming | One pending Domain Action delayed 1 season + opponent Stability −1 |
| Success | One pending Domain Action delayed 1 season |
| Partial | No delay effect; Minor complication fires (acting faction chooses: Standing −1 OR no effect) |
| Failure | No delay; Mandate −1 + opponent Standing +1 |

**Note:** Partial for Parliamentary Manoeuvre retains "no effect" as a valid Minor choice — the Minor is the choice between Standing −1 or accepting no effect. This preserves the original ruling while adding FF structure.

### 4.2 Battle Resolution

Battle already has a structured outcome table (stalemate, margins). No change. FF applies to Domain Actions only; Battle resolution is its own system.

### 4.3 Thread Operations

Thread operations already produce mandatory co-movement consequences (P-01). The FF complication for Thread op Failure adds Rendering Stability cost on top of co-movement — not instead of it.

---

## 5. CANON COMPLIANCE CHECK

| Canon Constraint | Status |
|---|---|
| P-07 (Consequences are meaningful and permanent) | ✓ FF produces lasting state changes, not cosmetic effects |
| P-08 (No null-outcome loops) | ✓ Failure advances the state — no static repetition possible |
| P-11 (Narrative momentum — inferred from §1.6) | ✓ Every roll changes the board |
| P-01 (Thread ops: all three dimensions fire) | ✓ Thread op FF adds to, not replaces, co-movement |
| P-12 (Player agency preserved) | ✓ Partial complication is player-choice |

---

## 6. COGNITIVE LOAD ASSESSMENT

Added complexity: one lookup per Failure/Partial on the action-type table.

| Load factor | Estimate |
|---|---|
| Table lookup (action-type) | ~15 seconds per trigger |
| Decision (Minor: choose 1 of 2) | ~10 seconds |
| Application (stat change) | Immediate |
| Net load addition | +0.5/10 overall |

This is acceptable. Reference card addition recommended (one column added to existing Domain Action reference card).

---

## 7. DESIGN NOTES

**Why player choice on Partial?** Preserves faction identity — a militarist faction may prefer Standing loss over Public Instability; a legitimacy-focused faction may prefer the reverse. Choice is a meaningful decision, not arbitrary.

**Why mandatory on Failure?** Failure represents a genuine collapse of the action. Ambiguity at that moment rewards delay and repetition — the exact behaviour FF is designed to prevent.

**Why proportionate to action type?** A failed Spy action and a failed Govern action have different fiction — the consequences should feel like they emerge from the fiction, not from a generic complication list.
