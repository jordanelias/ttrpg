<!-- DEPRECATED -->
> **DEPRECATED — 2026-04-11**
> Superseded by designs/cogload_moderate_target.md (Moderate ceiling target), which builds on this document and contains updated scores.
> Do not use as a canonical source.

---

# COGNITIVE LOAD REDUCTION STRATEGIES
## Target: All systems ≤ 10.0 (Moderate-Heavy ceiling)
## Constraint: Canon constraints P-01 through P-15 inviolable
## Format: Per system, tiered by texture preservation

---

## CURRENT SCORES AND TARGETS

| System | Current | Target | Gap |
|--------|---------|--------|-----|
| Personal Combat | 7.7 | ≤10 | ✓ Already met |
| BG Turn | 8.6 | ≤10 | ✓ Already met |
| Social Contest | 11.0 | ≤10 | −1.0 needed |
| Thread Operations | 12.8 | ≤10 | −2.8 needed |
| Mass Combat (3 units) | 14.5 | ≤10 | −4.5 needed |
| Thread in Mass Combat | 19.4 | ≤10 | −9.4 needed |

---

## 1. SOCIAL CONTEST (11.0 → ≤10.0)

### Load Sources
- 4 decisions/exchange: Read roll, genre selection, orientation selection, corroborate decision
- 3 lookups: bonus calculation, strain computation (margin + Charisma modifier − Focus defence), track movement
- 5 tracked variables: Composure, Concentration, Conviction Track, Rattled state, bonus dice

### Strategy SC-1: Strain Reference Card (Tier 1 — zero texture loss)
Pre-computed strain table indexed by margin (0–5) × Charisma modifier (0–2) × Focus defence (0–3). 18 cells. Eliminates per-exchange arithmetic.
- Reduction: −0.75
- Texture cost: None
- Canon impact: None

### Strategy SC-2: Read Once Per Contest (Tier 2 — minimal texture loss)
Roll Read (Attunement, TN 7, Ob 1) once at contest start. Result persists for all exchanges. Overwhelming result degrades by one tier each exchange (representing the opponent adjusting).
- Reduction: −1.0 (eliminates 1 roll + 1 decision per exchange after the first)
- Texture cost: Removes per-exchange social perception uncertainty. The opening "feel-out" moment is preserved; mid-contest adaptation is lost.
- Canon impact: None (Read is not a Thread operation; no P-01/P-11 concern)

### Recommended Package: SC-1 + SC-2 = −1.75 → **score 9.25** ✓

---

## 2. THREAD OPERATIONS (12.8 → ≤10.0)

### Load Sources
- 4 decisions: operation selection (6+ options), scale targeting, pool assembly, approach/modifier choice
- 4 lookups: TN (7 or 8), Ob by scale/recency, RS cost per degree, Coherence cost
- 6 tracked variables: Coherence, RS, Thread Sensitivity, Thread Pool Score, Contact Rounds remaining, Certainty

### Strategy TW-1: Pre-Computed Character Sheet Entries (Tier 1 — zero texture loss)
Add to character sheet:
- Thread Pool Score (TS ÷ 10, pre-calculated)
- Standard Thread Pool (Spirit + best History bonus + Thread Pool Score — one number)
- POP Pool (Spirit + best History bonus + Thread Pool Score÷2 — one number)
- Contact window size ("You get N operations" derived from Focus, printed once)
- RS cost quick-reference strip along sheet margin
- Reduction: −1.5 (eliminates 2 lookups, reduces pool assembly from computation to reading)
- Texture cost: None
- Canon impact: None

### Strategy TW-2: Contact Window as Operation Count (Tier 2 — minimal texture loss)
Replace round-by-round contact countdown with a fixed operation count. On successful Leap: "You have N operations" (N = Focus − 1). Operations resolve sequentially but the countdown is eliminated — the practitioner simply uses their operations then contact ends.
- Reduction: −1.3 (eliminates 1 tracked variable, 1 per-round decision)
- Texture cost: Removes the narrative beat of "running out of time" within the contact window. The tension of "do I have enough rounds left?" becomes "do I have enough operations?" — same constraint, less granular tracking. Focus still gates capacity.
- Canon impact: None. P-15 (three-layer being) is about Coherence at 0 and Leap vulnerability, not contact round granularity.

### Recommended Package: TW-1 + TW-2 = −2.8 → **score 10.0** ✓

---

## 3. MASS COMBAT — NO THREAD (14.5 → ≤10.0)

### Load Sources
- 3N+3 decisions (N = unit count): per-unit formation/tactic/movement (Phase 1, 3), per-unit pool split (Phase 5), global Rally/Support choice (Phase 6)
- 3 lookups: DR table, Morale trigger checklist, Discipline degradation check
- 3N+4 tracked variables: per-unit Size/Discipline/Morale + RS/clocks + damage accumulation

### Strategy MC-1: Battle Plan Templates (Tier 2 — minimal texture loss)
Replace per-unit Phase 1 declarations with a single Battle Plan selection from a fixed menu:

| Plan | All Units Do |
|------|-------------|
| Advance | Engage nearest enemy; formation Aggressive |
| Hold | Defend position; formation Defensive |
| Pincer | Flanking split; 2 units engage, 1 flanks |
| Withdraw | Orderly retreat; rear unit covers |
| Screen | Ranged units fire; melee holds line |

Individual unit orders derived from the plan. General may override one unit per turn with a Command check (TN 7, Ob 1; failure = unit follows plan anyway).
- Reduction: −2.0 (N-1 fewer decisions in Phase 1; with 3 units, saves 2)
- Texture cost: Reduces tactical granularity — players choose strategies not per-unit orders. The override mechanic preserves the option for specific tactical plays. Generalship shifts from micro-management to strategic selection + selective intervention.
- Canon impact: None

### Strategy MC-2: Sub-Unit Automation (Tier 3 — moderate texture loss)
Units without a named character attached follow a deterministic engagement priority:
1. Engage nearest enemy unit in same zone
2. If no enemy in zone, hold position
3. Default pool split: 50/50 (round down to Offence)
4. Default to Defensive formation if damaged (Size < 50%)

Only the general's unit and one additional "focused" unit require full player input per turn. Other units report results; player does not plan for them.
- Reduction: −1.5 per automated unit (with 1 automated unit from 3 total: −1.5)
- Texture cost: Reduces direct tactical control over peripheral units. Preserves it for the general's unit and one other. Simulates the reality that a general can only directly control so many things at once — which reinforces the Command stat's thematic role.
- Canon impact: None

### Strategy MC-3: Phase Consolidation — 7 → 5 Phases (Tier 3 — moderate texture loss)

| Old Phase | New Phase | Change |
|-----------|-----------|--------|
| 1 Strategy Declaration | 1 Strategy | Unchanged |
| 2 Volley | 2 Ranged + Movement | Volley and Manoeuvre merge; ranged fires then movement resolves |
| 3 Manoeuvre | (merged into 2) | — |
| 4 Offensive Thread | 3 Thread | Unchanged |
| 5 Engagement | 4 Engagement + Cascade | Engagement and damage application merge; all damage (Volley + Thread + Engagement) resolves at end of Phase 4 |
| 6 Cascade | (merged into 4) | Discipline/Morale checks at end of Phase 4 |
| 7 Reform | 5 Reform | Unchanged |

- Reduction: −2.0 (2 fewer phase transitions, 2 fewer "what happens now?" lookups)
- Texture cost: Loses the tactical timing distinction between Volley and Manoeuvre (currently volley fires first, then movement — reversal is possible). Damage simultaneity is preserved (all sources resolve together). The main loss is the ability to use Volley results to inform Manoeuvre decisions.
- Canon impact: Phase 4 (Thread) remains distinct — P-14 satisfied. Co-movement auto-effects still fire per Thread op.

### Recommended Package: MC-1 + MC-2 (1 automated unit) = −3.5 → **score 11.0**
Add MC-3 = −5.5 → **score 9.0** ✓

### Alternative Package (less texture loss): MC-1 + MC-3 = −4.0 → **score 10.5**
Close to target. One additional measure (pre-printed Morale trigger checklist on unit cards) = −0.5 → **score 10.0** ✓

---

## 4. THREAD IN MASS COMBAT (19.4 → ≤10.0)

This is the critical case. The load comes from simultaneously running two heavy subsystems. The strategies from sections 2 and 3 stack, but the key insight is: **the two systems should never require simultaneous cognitive engagement.**

### Strategy TM-1: Late Thread Declaration (Tier 2 — minimal texture loss)
Thread intent is declared at Phase 4 start (previously: Phase 1). Mass combat Phase 1 covers only tactical declarations. The practitioner decides whether to use Thread, which operation, and which target only when Phase 4 arrives.

Effect: The player plans mass tactics in Phase 1 without needing to simultaneously plan Thread. Then in Phase 4, they plan Thread without needing to simultaneously execute tactics (units are already committed). The two planning burdens are **temporally separated**.
- Reduction: −3.0 (eliminates simultaneous planning of Thread + tactics; converts parallel to sequential)
- Texture cost: Enemy cannot anticipate Thread usage at Phase 1 since it isn't declared. But since Phase 1 declarations are simultaneous and secret, the enemy couldn't act on this information anyway. Net gameplay impact: near zero.
- Canon impact: None. Thread still resolves at Phase 4 before Engagement (Phase 5). Co-movement fires normally.

### Strategy TM-2: Single Operation Per Battle Turn (Tier 2 — minimal texture loss)
In mass combat, a practitioner gets exactly 1 Thread operation per battle turn. No multi-round contact window. Focus determines Leap success probability (higher Focus = better Leap) but does not extend the contact window at mass battle scale.

Rationale: Mass battle turns represent longer timeframes than personal combat rounds. A single operation at mass scale already represents a sustained effort across the entire engagement phase. Multiple operations per turn at mass scale would imply the practitioner can perform several acts of world-alteration while armies clash around them — narratively implausible and mechanically excessive.
- Reduction: −3.0 (eliminates contact round tracking, sequential operation planning, and per-round decisions within the contact window)
- Texture cost: Practitioners with Focus 4+ lose the ability to chain multiple operations in a single battle turn. At mass scale, this is thematically appropriate — the chaos of battle limits sustained Thread contact regardless of Focus. Focus remains important for Leap success (and retains full value in personal-scale Thread operations).
- Canon impact: P-01 (inseparability) and P-11 (temporal disjunction universal) still satisfied — the single operation still produces all three co-movement auto-effects. P-15 (three-layer being) unaffected — Coherence still tracks and the Leap still has a vulnerability window.

### Strategy TM-3: Command Suspension During Thread (Tier 2 — minimal texture loss)
While a practitioner-general is in Thread contact, their Command bonus is suspended and their units follow automation (MC-2). This is identical to the existing Mass → Personal rule (PP-111: Command suspended during personal combat).

Effect: The player manages Thread only during Phase 4. Their mass combat units run on autopilot for Phases 5-7 of that turn. Next turn, if they choose not to use Thread, they resume full Command.
- Reduction: −2.0 (eliminates simultaneous unit management during Thread phase)
- Texture cost: None — this extends an existing rule (Command suspension during personal combat) to Thread contact. The thematic justification is identical: a general whose consciousness is suspended from rendering cannot simultaneously direct troops. This is arguably a consistency FIX, not a simplification.
- Canon impact: None. Reinforces P-15 (Leap = suspension of layer 2 self-rendering; a general in suspended rendering cannot command).

### Strategy TM-4: Pre-Printed ×3 RS Table (Tier 1 — zero texture loss)
Single reference card with RS costs already multiplied:

| Operation | Success | Partial | Failure |
|-----------|---------|---------|---------|
| Lock | −3 RS | −3 RS | −6 RS |
| Dissolution | −15 RS | −18 RS | −24 RS |
| Mend | +3 RS | +0 | −3 RS |
| Pull | −3 RS | −6 RS | −9 RS |

- Reduction: −1.0
- Texture cost: None
- Canon impact: None

### Recommended Package: TM-1 + TM-2 + TM-3 + TM-4 = −9.0

Combined with Thread reductions (TW-1 + TW-2 = −2.8) applied to the Thread component:
- Thread component: 12.8 − 2.8 (TW) − 3.0 (TM-2) − 1.0 (TM-4) = 6.0
- Mass component during Thread turn: automated (MC-2) = ~2.0
- Planning: sequential not parallel (TM-1) = no stacking penalty
- **Combined score: ~8.0** ✓

Without TM-1 + TM-3, the planning burden remains parallel, adding ~3.0 back → 11.0. These two strategies are essential.

---

## COMPLETE PACKAGE SUMMARY

| Strategy | System | Tier | Reduction | Texture Cost |
|----------|--------|------|-----------|-------------|
| SC-1 | Social Contest | 1 | −0.75 | None |
| SC-2 | Social Contest | 2 | −1.0 | Per-exchange Read uncertainty removed |
| TW-1 | Thread Ops | 1 | −1.5 | None |
| TW-2 | Thread Ops | 2 | −1.3 | Contact countdown granularity removed |
| MC-1 | Mass Combat | 2 | −2.0 | Per-unit tactical orders → battle plans |
| MC-3 | Mass Combat | 3 | −2.0 | Volley/Manoeuvre timing distinction removed |
| TM-1 | Thread+Mass | 2 | −3.0 | Thread declared at Phase 4 not Phase 1 |
| TM-2 | Thread+Mass | 2 | −3.0 | 1 operation per battle turn (mass scale only) |
| TM-3 | Thread+Mass | 2 | −2.0 | Command suspended during Thread (extends existing rule) |
| TM-4 | Thread+Mass | 1 | −1.0 | None |

### Resulting Scores

| System | Before | After | Rating |
|--------|--------|-------|--------|
| Personal Combat | 7.7 | 7.7 | Moderate |
| BG Turn | 8.6 | 8.6 | Moderate-Heavy |
| Social Contest | 11.0 | 9.25 | Moderate-Heavy |
| Thread Operations | 12.8 | 10.0 | Moderate-Heavy |
| Mass Combat (3 units) | 14.5 | 10.0 | Moderate-Heavy |
| Thread in Mass Combat | 19.4 | ~8.0 | Moderate |

### Canon Constraint Compliance

All strategies checked against P-01 through P-15:
- P-01 (inseparability): All Thread operations retain three-dimensional co-movement auto-effects. ✓
- P-11 (temporal disjunction): Every Thread op still produces temporal auto-effect. ✓
- P-14 (BG/VG modes express inseparability): BG Thread skipped (by design); Hybrid Thread retains all effects. ✓
- P-15 (three-layer being): Coherence still tracked; Leap vulnerability preserved; TM-3 reinforces the philosophy (suspended rendering = cannot command). ✓

No constraint violations.

---

## IMPLEMENTATION NOTES

### Zero-Effort (tooling only — no mechanical changes):
SC-1, TW-1, TM-4. Create reference cards and character sheet additions. Immediate implementation.

### Low-Effort (procedural changes — no formula changes):
TM-1 (late Thread declaration), TM-3 (Command suspension during Thread). These extend existing rules to new contexts. Can be added as GM guidance notes.

### Medium-Effort (mechanical simplification — requires params + doc updates):
SC-2, TW-2, MC-1, TM-2. Each requires updating the relevant params file and canonical doc. Simulations should verify that the simplified versions produce equivalent gameplay outcomes.

### High-Effort (structural change):
MC-3 (phase consolidation). Changes the turn structure. Requires updating mass_battle_v3.md, params_mass_combat.md, all simulation baselines, and the coverage matrix.
