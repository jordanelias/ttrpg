# SIM-MB-01 — Stress Test: Mass Battle
## Date: 2026-04-09
## Modes: A (Single Mechanic Isolation) + D (Edge Case Discovery)
## Source files: designs/mass_combat/mass_battle_v3.md (696L), references/params_mass_combat.md (500L)

---

## FETCH LOG
- references/canonical_sources.yaml: ✓ fetched (154 lines)
- designs/mass_combat/mass_battle_v3.md: ✓ fetched (696 lines)
- references/params_mass_combat.md: ✓ fetched (500 lines)
- canon/02_canon_constraints.md: ✓ fetched (25 lines)
- skills/valoria-simulator/SKILL.md: ✓ fetched (199 lines)

---

## MODE A — SINGLE MECHANIC ISOLATION

### A-1: Core Combat Pool (PP-233)
Formula: Pool = min(Size, Command) + Command

Pool values (Size × Command):
| Size\Cmd | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| 2 | 2 | 4 | 5 | 6 | 7 | 8 | 9 |
| 3 | 2 | 4 | 6 | 7 | 8 | 9 | 10 |
| 4 | 2 | 4 | 6 | 8 | 9 | 10 | 11 |
| 5 | 2 | 4 | 6 | 8 | 10 | 11 | 12 |
| 6 | 2 | 4 | 6 | 8 | 10 | 12 | 13 |
| 7 | 2 | 4 | 6 | 8 | 10 | 12 | 14 |

Key insight: when Size >= Command, pool = 2×Command. Size > Command adds zero to pool.
Size only reduces pool when Size < Command.

P(outcomes) by pool size (TN7):
| Pool | E[net] | P(>=1) | P(>=3) |
|---|---|---|---|
| 2D (Cmd=1) | 0.67 | ~46% | ~8% |
| 4D (Cmd=2) | 1.3 | ~80% | ~25% |
| 6D (Cmd=3) | 2.0 | ~92% | ~45% |
| 8D (Cmd=4) | 2.6 | ~97% | ~60% |
| 10D (Cmd=5) | 3.3 | ~99% | ~73% |
| 12D (Cmd=6) | 4.0 | ~99% | ~83% |
| 14D (Cmd=7) | 4.7 | ~99% | ~90% |

**Finding A-1-F1 [P2]:** Size > Command: casualties have zero effect on pool. Size degradation only matters when Size < Command. Large armies with mediocre generals take casualties consequence-free until below Command rating.

**Finding A-1-F2 [P1]:** Cmd=7 vs Cmd=1: 7× output differential. Expected damage (Dmg Mod +2 Heavy Infantry): 14.1 vs 2.0 per exchange. Cmd=5 general kills Size=7 army in ~1 exchange (expected 9.9 damage). This is the intended "generalship dominates" axiom but produces predetermined outcomes at extreme Command differentials. CONFIRMED INTENTIONAL per design doc axiom. Document as GM guidance note.

---

### A-2: Health Pool Formula (PP-233)
H = min(Discipline, Command) + DR
Total Health = Size × H

H values (Disc × Cmd, DR=0):
| Disc\Cmd | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 2 | 2 | 2 |
| 3 | 1 | 2 | 3 | 3 | 3 |
| 4 | 1 | 2 | 3 | 4 | 4 |
| 5 | 1 | 2 | 3 | 4 | 5 |

**Finding A-2-F1 [P2]:** Command caps H identically to pool cap. Cmd=1 general: H=1+DR regardless of Discipline. Command asymmetry compounds: affects both offensive output AND survivability simultaneously. No balancing factor.

---

### A-3: Discipline Degradation Trigger

THREE CONFLICTING DEFINITIONS:
1. mass_battle_v3.md §A.4: "When total Size lost this turn exceeds Discipline rating: Discipline degrades by 1." — single condition.
2. params_mass_combat.md PP-251: BOTH (Size loss > Discipline) AND (unit's loss > opposing loss by ≥1). Two conditions.
3. params_mass_combat.md PP-320/ED-140: BOTH (Size loss > Discipline) AND (Power asymmetry OR Thread/artillery). Different second condition.

**Finding A-3-F1 [P1 — BLOCKER]:** Three incompatible versions. Design doc is canonical (mass_battle_v3.md) per canonical_sources.yaml — single condition governs. PP-251 in params is a later patch not propagated to the design doc. Requires reconciliation. → ED-351 raised.

---

### A-4: Morale Cascade Cap
Cap: -3 per Cascade Phase (non-general). General death Stage 2: -2 uncapped. Max total: -5.

| Triggers | Before cap | Capped |
|---|---|---|
| Size <50% + Disc broken + Allied rout | -3 | -3 |
| All above + Flanked + lost | -4 | -3 |
| Any above + General killed | -3 cap + -2 | -5 |

**Finding A-4-F1 [P2]:** Morale floor=1 while general present. General death → floor suspended → -5 Morale max in one phase. Starting Morale=5: rout in 1 phase if all triggers fire + general dies. Intended.

**Finding A-4-F2 [P3]:** Idle army clock (-1 Morale if no engagement 2+ turns) fires for BOTH sides during mutual non-engagement. Creates passive-play blink-first dynamic: both sides risk Morale collapse from inaction.

---

### A-5: Volley Phase Pool

**Finding A-5-F1 [P1 — BLOCKER]:** "Roll Effective Power vs TN 6" — "Effective Power" undefined for Volley Phase. Two interpretations:
(a) Power stat (1–7 unit quality stat): straightforward but differs from engagement formula.
(b) Engagement pool = min(Size, Command) + Command: consistent with PP-233 but makes ranged identical to melee in pool calculation.
Design doc uses "Effective Power" and "Effective Pool" interchangeably but without specifying which applies to Volley. → ED-352 raised.

---

### A-6: Feigned Retreat
Recognition: opposing general rolls Command dice vs Ob 2.
Discipline check: pursuing unit Ob 1 (PP-256).

P(recognition) by Command (TN7, pool=Command):
| Cmd | P(≥2 net) |
|---|---|
| 1 | ~12% |
| 2 | ~34% |
| 3 | ~57% |
| 4 | ~74% |
| 5 | ~85% |
| 7 | ~96% |

P(feint succeeds) = P(not recognised) × P(fail Discipline check):
- Cmd=2 general vs Disc=1 unit: 0.66 × 0.60 = ~40% success
- Cmd=5 general vs Disc=4 unit: 0.15 × 0.13 = ~2% success

**Finding A-6-F1 [P2]:** Steep scaling — effectively useless vs high-Command opponents, powerful vs low-Command opponents. Intended.

**Finding A-6-F2 [P3]:** General dead (Cmd=0): no recognition possible. Feint success = 1 - P(Disc check). Feigned Retreat becomes reliably effective after general death. Intended consequence.

---

### A-7: Reserve Commitment Timing

**Finding A-7-F1 [P2 — AMBIGUITY]:** PP-MB-04: "commits at Phase 3 of Turn N+1 → unit may engage in Phase 4 of Turn N+1." Phase 4 is Thread Operations. Phase 5 is Engagement. PP-MB-04 references the wrong phase number. Should read "Phase 5 Engagement." → PP-499 (text fix).

---

## MODE D — EDGE CASE DISCOVERY

### BOUNDARY

**D-1: Thread-destroyed units vs simultaneous-damage rule [P2]**
Design doc: "A unit whose Size is reduced to 0 by Phase 4 Thread effects is removed at Phase 6 Step 1 and does not participate in Phase 5 Engagement."
But damage is not applied until Phase 6 Step 1 — so during Phase 5, unit's current Size is non-zero. Simultaneous-damage rule implies unit participates in Phase 5.
Contradiction: design doc excludes, simultaneous-damage rule includes. → ED-354 raised.

**D-2: Size=1, Command=7 [P3]**
Pool = min(1,7)+7 = 8D. Single survivor with brilliant general rolls 8D.
E[damage] = 2.6 × (1+DmgMod). Last soldier is as effective per die as full army.
Intentional per design axiom. GM guidance note.

**D-3: Minimum pool post-penalties (PP-273) [P2]**
Discipline=1: -2D penalty, min 1D floor → can still attack.
Discipline=0: Formation Break → cannot attack.
Transition from 1D to 0D fires on next Discipline check. If Size loss > Disc=1 and asymmetry met: one more check drops to 0. All-or-nothing last turn.

**D-4: Command=0 after general death [P2]**
All units: 1D minimum. E[damage] = 0.33 × (1+DmgMod) = ~0.67/turn (Light Infantry).
But Morale collapse from general death fires faster than combat opportunity: Morale -5 from full cascade → rout in 1-2 turns.
PP-273 fight-at-1D rule may never fire in practice — Morale collapses the army first.

### CASCADE

**D-5: Maximum Morale collapse chain [P2]**
Turn after general death (Stage 2 fires):
- Size <50%: -1, Disc broken: -1, Allied rout: -1 → capped at -3
- General kill Stage 2: -2 (uncapped)
- Total: -5 per phase
- Morale 5 → 0 in one phase → immediate rout
- Rout contagion: -1 adjacent units (cannot cascade same turn per brake)
- Next turn: adjacent units face own cascade → 2-turn army collapse sequence

### REGRESSION

**D-6: Discipline self-acceleration [P2]**
Discipline degradation lowers the trigger threshold.
Disc=3 triggers on Size loss > 3. After degrading to Disc=2: triggers on Size loss > 2.
Each degradation makes the next easier. Against Command=5 general (E[damage] = 9.9): Disc cascade 5→4→3→2→1→0 in 5 turns — certain against high-Command attackers.

### DEADLOCK

**D-7: Both generals simultaneously in personal combat [P2]**
Rule: "Mass battle pauses during personal combat." If both generals enter personal combat in Phase 5 simultaneously: no rule defines mass battle state. Does mass battle freeze entirely? Do units fight uncommanded at 1D minimum? No sequencing rule for bilateral general-combat.
→ ED-355 raised.

**D-8: Command=1 Discipline spiral [P1 — confirmed intentional]**
Command=1: no Discipline restoration (PP-241 requires Cmd ≥ 2). Any Size loss > 1 triggers Discipline degradation. Self-accelerating to Formation Break inevitable.
CONFIRMED INTENTIONAL per design doc [NEW-P2-05]. No patch. GM guidance: Command=1 generals should not be fielded in contested battles.

### CRUNCH CASCADE

**D-9: 56+ resolution steps per peak turn [P2]**
With 3 sub-units, 1 practitioner, Artillery, general in personal combat:
- Phase 1: 7 steps
- Phase 2: 3 steps
- Phase 3: 3 steps
- Phase 4: 3 steps
- Phase 5: 18 steps
- Phase 6: 12 steps
- Phase 7: 6 steps
Total: ~56 steps

Primary crunch: simultaneous damage bookkeeping across 3+ sources before any values change.
Recommendation: tracking sheet (3 damage buckets: Volley / Thread / Engagement per unit). No mechanical change needed.

### AMBIGUITY

**D-10: Shield Wall +2D Def across multi-direction engagements [P2]**
Clarification (PP-MB-07): "Front attack is fully defended (+2D Def). Right flank attack applies normally."
"Applies normally" implies the unmitigated flank does NOT get +2D Def bonus. But Shield Wall's +2D Def is a formation modifier that should apply to all defensive pools.
Question: does +2D Def apply to all engagements simultaneously or only to the front/negated-flank engagements?
→ ED-356 raised.

**D-11: Feigned Retreat re-engage-with-flank assignment [P2]**
"Re-engage next turn with flank" — flank advantage belongs to retreating unit by tactic design.
Text does not explicitly name the retreating unit as holder of flank advantage. Ambiguous.
Fix: add "retreating unit gains flank advantage on re-engagement." Minor text clarification.

### INCOHERENCE

**D-12: Mutual destruction Stability check [P2]**
PP-240: mutual destruction → both factions Stability check Ob 1 at Accounting.
§A.13: battle lost (routed) → Stability check Ob 1.
Mutual destruction = draw (no loser). Does the PP-240 Ob 1 replace the §A.13 check or add to it?
→ ED-357 raised.

### OPTIMAL PLAY

**D-13: Command distribution across sub-units [P1 — BLOCKER]**
Pool = min(Size, Command) + Command per sub-unit.
If Command applies in full to each sub-unit: splitting into 3 sub-units multiplies total dice.
Example: Size=7, Cmd=5. Single unit: pool=10D. Three sub-units (3/2/2): 8+7+7=22D total.
This makes 3-way splits always optimal — dominant strategy.

§A.8 note: "Attacker splitting Size=6 into 3+3 against undivided Size=5 defender is disadvantageous." This implies full Command applies per sub-unit (confirming splitting disadvantage vs undivided defender). But the formula doesn't explicitly state Command applies in full to each sub-unit.
→ ED-353 raised. Confirm explicit rule text: "Command applies in full to each sub-unit's pool."

### DEGENERATE

**D-15: Coherence depletion warning overstates risk [P2]**
Design doc §A.10: "Severed after 9 total operations. Full-battle Threadweaving is a practitioner self-destruction event."
At Battle scale: 7-turn battle = 7 operations = Coherence 10 → 3. Not Severed (Coherence=1 threshold).
Only battles ≥ 9 turns produce Severance from constant operation. 7-turn battle leaves Coherence=3 (Dissonant band, but functional).
The "self-destruction" framing is overstated for standard 7-turn battles. Needs correction in design doc.

---

## P1 FINDINGS

| ID | Mechanic | Finding | Action |
|---|---|---|---|
| A-3-F1 | Discipline degradation | 3 conflicting trigger definitions | ED-351 |
| A-5-F1 | Volley Phase | "Effective Power" undefined — Power stat vs engagement pool | ED-352 |
| D-13-F1 | Sub-unit command | Command distribution across sub-units undefined | ED-353 |

## P2 FINDINGS

| ID | Mechanic | Finding | Action |
|---|---|---|---|
| A-1-F1 | Pool formula | Size > Command: casualties have zero pool effect | Design note |
| A-2-F1 | Health formula | Command caps H and pool simultaneously — compound asymmetry | Design note |
| A-4-F2 | Morale | Idle army clock creates passive-play blink-first dynamic | PP candidate |
| A-7-F1 | Reserve timing | PP-MB-04 references Phase 4 (Thread) instead of Phase 5 (Engagement) | PP-499 text fix |
| D-1-F1 | Thread/simultaneous damage | Phase 4 destroyed units: design doc excludes from Phase 5, simultaneous-damage rule implies includes | ED-354 |
| D-4-F1 | Post-death combat | PP-273 1D minimum may never fire — Morale collapse outpaces combat | Design note |
| D-5-F1 | Morale cascade | 2-turn deterministic army collapse after general death + attrition | Design note (intended) |
| D-6-F1 | Discipline self-acceleration | Each degradation lowers threshold — self-accelerating cascade | Design note |
| D-7-F1 | Bilateral general combat | Both generals in personal combat simultaneously: mass battle state undefined | ED-355 |
| D-9-F1 | Crunch | 56+ resolution steps per peak turn | Tracking sheet |
| D-10-F1 | Shield Wall | +2D Def across multi-engagement directions undefined | ED-356 |
| D-11-F1 | Feigned Retreat | Flank advantage assignment ambiguous in text | PP candidate |
| D-12-F1 | Mutual destruction | Stability check: replacement of or addition to battle-lost consequences | ED-357 |
| D-15-F1 | Coherence depletion | Warning overstates risk for 7-turn battles | Design doc correction |

## P3 FINDINGS

| ID | Finding |
|---|---|
| A-4-F2 | Idle army clock — passive play incentive |
| A-6-F2 | Feigned Retreat auto-succeeds after general death |
| D-2-F1 | Single survivor + Cmd=7 = 8D (intended axiom) |

---

## NEW EDITORIALS

| ED | Description | Severity |
|---|---|---|
| ED-351 | Discipline degradation: reconcile 3 conflicting definitions (design doc §A.4 vs PP-251 vs PP-320) | P1 |
| ED-352 | Volley Phase pool: "Effective Power" — Power stat or min(Size,Cmd)+Cmd? | P1 |
| ED-353 | Command per sub-unit: confirm explicit rule text that Command applies in full to each sub-unit pool | P1 |
| ED-354 | Thread destruction in Phase 4: participation in Phase 5 — design doc contradicts simultaneous-damage rule | P2 |
| ED-355 | Both generals in personal combat simultaneously: mass battle pause rule undefined | P2 |
| ED-356 | Shield Wall +2D Def: all simultaneous engagements or only non-flanked? | P2 |
| ED-357 | Mutual destruction Stability check: addition to or replacement of battle-lost consequences | P2 |

