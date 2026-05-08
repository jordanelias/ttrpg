# Scene Mechanics Canonical Audit — Combat / Contest / Fieldwork / Mass Combat
# Date: 2026-04-18
# Sources: params/combat.md, params/contest.md, params/fieldwork.md, params/mass_combat.md, params/core.md

---

## CROSS-DOCUMENT CONFLICTS

### CONFLICT A: Stamina formula
| Source | Formula | End 4 value |
|--------|---------|-------------|
| params/combat.md (PP-611) | Endurance + 1 | 5 |
| params/core.md (ED-694) | Endurance × 5 | 20 |

ED-694 is newer (2026-04-18). PP-611 is older. **params/core.md wins.** params/combat.md stale.

### CONFLICT B: Composure formula
| Source | Formula | Cha 4 value |
|--------|---------|-------------|
| params/contest.md (PP-234) | Charisma + 6 | 10 |
| params/core.md (ED-694) | Charisma × 3 | 12 |

ED-694 is newer. **params/core.md wins.** params/contest.md stale.

### CONFLICT C: Disposition ceiling
| Source | Formula | Bonds 5 value |
|--------|---------|---------------|
| params/fieldwork.md (PP-632) | floor(Bonds/2)+1 | +3 |
| params/core.md (PP-684) | = Bonds | +5 |

PP-684 explicitly revised PP-632. **params/core.md wins.** params/fieldwork.md stale.

### CONFLICT D: Mass battle Thread RS multiplier
| Source | Rule |
|--------|------|
| params/mass_combat.md PP-601 | ×3 multiplier STRUCK. Individual RS costs ×1. |
| params/mass_combat.md PP-204 | "Dissolution Failure = −24 RS via ×3 multiplier" |

PP-601 struck PP-192/PP-225. PP-204 note is stale — still references ×3. **PP-601 wins.** PP-204 note needs updating.

---

## COMBAT — Mechanical Completeness

| Mechanic | Status | Notes |
|----------|--------|-------|
| Pool formula (Agi×2)+H+3 | ✓ | PP-615 confirmed |
| Vitality = End×10 | ✓ | ED-694 |
| Stamina = End×5 | ✗ CONFLICT A | params/combat says End+1 |
| Wound Interval = End+6 | ✓ | Both docs agree |
| Weapon 3-axis matrix (Reach×Weight×Type) | ✓ | PP-232 complete |
| TN modifiers per axis | ✓ | Short -1, Light -1, Blunt +1 |
| Damage = net + STR + weapon mod vs armor | ✓ | PP-232 |
| Critical Hit (net≥3): weapon mod doubled | ✓ | PP-232 |
| Initiative (higher Att declares last) | ✓ | PP-232 |
| Fibonacci group bonus | ✓ | Table complete |
| Mass Mismatch (Light vs Heavy: def -1) | ✓ | PP-232 |
| Armor wield constraint (Stamina floor) | ✓ | PP-232 |
| Ranged combat (cover, closing, reload) | ✓ | PP-172 |
| Actions (Strike/Feint/Guard/Disarm/etc) | ✓ | Summary present |
| Rescue/Martyr (PP-406/407) | ✓ | Momentum values |
| Surrender/Disengage (PP-634) | ✓ | Complete |
| Thread integration cross-refs | ✓ | F-07 links correct |
| Ranged weapon TN integration | ✗ OPEN | ED-129 pending |

## CONTEST — Mechanical Completeness

| Mechanic | Status | Notes |
|----------|--------|-------|
| Pool formula (Attr×2)+H | ✓ | PP-615 |
| Composure = Cha×3 | ✗ CONFLICT B | params/contest says Cha+6 |
| Concentration = Focus+Recall | ✓ | |
| Genre system (Memory/Projection) | ✓ | PP-235 |
| Argument styles (4: Precedent/Suppression/Vision/Insinuation) | ✓ | |
| Interaction types (CLASH/REINFORCE/CROSS/TIE) | ✓ | |
| Faction boosts (single axis per faction) | ✓ | Table complete |
| Piety Track 0-10 | ✓ | |
| Resonant Style targeting | ✓ | npc_behavior §6 |
| Appraise (Att+Rec vs Cha÷2) | ✓ | PP-614 |
| Corroboration (Bonds gate) | ✓ | PP-235 |
| Let It Ride | ✓ | |
| Practitioner Weaving (+floor(TS/30)D) | ✓ | |
| Post-contest Domain Echo | ✓ | |
| CLASH stalls at median | ✗ OPEN | ED-295 awaiting decision |
| AMPLIFY dominant over CLASH | ✗ OPEN | ED-297 awaiting decision |

## FIELDWORK — Mechanical Completeness

| Mechanic | Status | Notes |
|----------|--------|-------|
| Pool formula (Attr×2)+H | ✓ | PP-615 |
| Depth axis 0-5 | ✓ | Perception gates complete |
| Evidence Track (thresholds 3/5/8) | ✓ | |
| Disposition range | ✗ CONFLICT C | fieldwork says floor(Bonds/2)+1; core says =Bonds |
| Disposition shift by degree | ✓ | F/P/S/OW mapped |
| Disposition decay | ✓ | >+2 decays -1/season |
| Knot system (formation/tiers/effects) | ✓ | PP-632 |
| Knot pool = (Bonds×2)+3 | ✓ | |
| Exposure sources | ✓ | Full table |
| Church AP integration | ✓ | §6.5 |
| Cover (Cog + History) | ✓ | |
| Desperate Trail (fail forward) | ✓ | |
| Evidence Quality Tags | ✓ | 7 tags |
| Thread-Read pool | ✓ | (Att×2)+H+TPS |
| System transitions | ✓ | All 6 directions mapped |
| Sincerity Gate | ✓ | Spirit Ob 1 |
| BG Survey action | ✓ | Consul Inward, Ob=(5-PR)+1 |
| Wounds+fieldwork interaction | ✓ | Physical only for End-based |
| Non-Sensitive Dissonance | ✓ | Spirit check |

## MASS COMBAT — Mechanical Completeness

| Mechanic | Status | Notes |
|----------|--------|-------|
| Pool = min(Size,Command)+Command | ✓ | PP-233 |
| H = min(Discipline,Command)+DR | ✓ | |
| Damage = successes × (1+Power) | ✓ | Simultaneous |
| 7-phase structure | ✓ | PP-235 |
| 5-phase consolidation | ✓ | |
| Battle Plan Templates (5) | ✓ | |
| Discipline degradation (deterministic) | ✓ | PP-232/PP-251 |
| Morale triggers | ✓ | 8 triggers listed |
| DR tables (melee + projectile) | ✓ | PP-104 |
| Faction Military → Unit Quality | ✓ PROPOSAL | |
| Command suspension during Thread | ✓ | PP-235 |
| Thread RS ×1 (×3 STRUCK) | ✓ | PP-601 |
| Substrate Saturation Counter | ✓ | ≥3 = RS-1 |
| Single op per battle turn | ✓ | PP-235 |
| Volley Phase pool = Power at TN6 | ✓ PROVISIONAL | PP-503 |
| ×3 multiplier in PP-204 note | ✗ STALE | References struck ×3 |
| Dissolution campaign impact warning | ✓ | PP-201 |

---

## SUMMARY

| System | Complete mechanics | Conflicts | Open EDs |
|--------|-------------------|-----------|----------|
| Combat | 16/17 | 1 (Stamina) | 1 (ED-129 ranged) |
| Contest | 15/17 | 1 (Composure) | 2 (ED-295, ED-297) |
| Fieldwork | 17/17 | 1 (Disposition) | 0 |
| Mass Combat | 15/16 | 0 | 0 (1 stale ref) |

**All four systems are mechanically complete.** 3 cross-document conflicts need propagation (params files stale vs params/core.md ED-694/PP-684). 2 open editorial decisions in Contest (ED-295 CLASH stall, ED-297 AMPLIFY dominance). 1 stale ×3 reference in mass combat.

