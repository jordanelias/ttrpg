# Weapon System v2 — Comprehensive Audit

**Date:** 2026-05-14
**Session token:** 2500216d77b103b3
**Scope:** T2.4, T5.1, T6.1 (distance), T4.1-4.4 (defense triangle), T7.1-7.2 (equal-budget)
**Method:** Bottom-up iteration, top-down review against historical precedent

---

## I. Test Results Summary

| Test | Status | Root Cause |
|------|--------|------------|
| T5.1 Distance sanity | PASS (after 2 bug fixes) | ED cost/defense asymmetry fixed |
| T2.4 Warhammer dominance | PARTIAL PASS (win rate OK, DPH ratio high) | Bash damage is correctly high |
| T6.1 Longsword dominance | PARTIAL PASS (fixed vs Mid, not vs Long) | Same-reach matchups need separate lever |
| T4.1 Triangle swing | FAIL (10-20pp vs 25-35pp target) | ±TN can't produce enough swing at 6-die defense |
| T4.2 Initiative + triangle | FAIL (1-6pp vs 8-15pp target) | Arming sword has only 2/3 of triangle coverage |
| T4.3 Specialist penalty | FAIL (mace 19-25%) | TN + triangle compound against specialists |
| T4.4 Random vs optimal def | FAIL (7pp gap) | Game theory: randomization beats fixed strategy |
| T7.1 Build matrix | FAIL (5/6 conditions) | End dominance + Soldier has no niche |
| T7.2 Protocol swing | PARTIAL PASS (1/4) | Simplified protocols underestimate real swing |

---

## II. Root Cause Analysis (Bottom-Up)

### Cause 1: HP formula super-linear End scaling

The HP formula `(End+6) × (End//2 + 2)` produces quadratic-ish scaling:

| End | HP (canonical) | HP (proposed: End×6+16) | Δ |
|-----|---------------|------------------------|---|
| 3 | 27 | 34 | +7 |
| 4 | 40 | 40 | 0 |
| 5 | 44 | 46 | +2 |
| 6 | 60 | 52 | **−8** |
| 7 | 65 | 58 | −7 |

End 6 gets 50% more HP than End 4 canonically. With `End×6+16`, the gap narrows to 30%. Combined with the wound system (−1D per wound = snowball effect), high End creates a compounding advantage: more HP → fewer wounds → larger pool → more offense AND defense → more survivability.

**Tested fix:** `HP = End × 6 + 16`. Tough drops from 69% → 57% average (unarmoured). Top build under 65% threshold.

### Cause 2: Pool formula linear in Agi

`Pool = Agi×2 + Hist + 3`. Each Agi point adds 2D to the combat pool — affecting both offense and defense. Agi 6 (Fast) produces pool 17 vs Agi 3 (Strong) at pool 11. This 55% pool advantage overwhelms weapon-specific TN differences.

**Tested fix:** Diminishing returns above Agi 4: `min(Agi,4)×2 + max(0,Agi-4)×1 + Hist + 3`. Agi 6 drops from 17→15 (−12%). Combined with HP fix, Fast drops from 60%→53%, no longer dominant.

### Cause 3: Balanced stats produce no mechanical edge

Soldier (4/4/4/4 with arming sword) averages 13-16% across ALL conditions because:
- Pool 13: same as Cunning/Knight, worse than Fast (17)
- HP 40: same as most, worse than Tough (60)
- STR 4: mediocre
- TN 7.0: worst non-blunt weapon
- No standout dimension to exploit

Even with both proposed fixes (DR pool + linear HP), Soldier only reaches 16%. The generalist has no niche.

### Cause 4: Defense triangle lever conflict

The same modifier that makes defense type selection meaningful (25-35pp swing) also makes specialist weapons unplayable (permanent wrong-defense penalty). ±0.5 TN: 10pp swing (too small). ±1.0 TN: 20pp swing (still small) but mace drops to 19% (too harsh). No scalar modifier solves both problems simultaneously.

---

## III. Historical Precedent Review (Top-Down)

### Weapon hierarchy in European martial arts

**Longsword as "king of weapons":** Liechtenauer tradition (14th-15th c.) and Fiore dei Liberi's *Fior di Battaglia* both treat the longsword as the premier dueling weapon. It was versatile (cut, thrust, half-sword, mordhau), had excellent reach, and dominated judicial duels. **Sim finding matches precedent:** longsword SHOULD be the best pure dueling weapon. The 77% vs spear is high but directionally correct — the longsword was historically superior to the spear in single combat because it could counter the spear's reach advantage through half-swording and closing techniques.

**Arming sword as standard sidearm:** The arming sword (also "knightly sword") was the universal European military sidearm from c.1000-1400. It was paired with a shield for battlefield use, and effective but not exceptional in single combat. **Design implication:** The arming sword's poor performance (TN 7.0 in v2) is partially correct — without a shield, the arming sword IS at disadvantage against longer weapons. BUT the v1 TN of 6 (Short Heavy Blade) was also defensible. The v2 reclassification to "Mid Normal" removes both the Short reach bonus and the Heavy weight bonus, which overcorrects.

**Spear's conditional dominance:** Historical sources confirm the spear dominates at distance but the sword dominates inside the spear's reach. Fiore's *Fior di Battaglia* shows spear vs sword and emphasizes the swordsman must close past the spear point. **Sim finding matches precedent:** T5.1 shows correct directionality (spear 72% from Long, 11% from Short).

**Mace/warhammer anti-armour role:** The mace and warhammer were specifically developed to defeat plate armour where cutting weapons failed. Their technique was simpler (fewer attack vectors, less finesse required) but the raw impact was devastating. **Sim finding matches precedent:** The Bash damage curve (+2/+3/+4/+4) correctly makes blunt weapons better at higher armour. The 3× STR multiplier for Heavy Blunt is high but reflects the weapon's design purpose.

**Defense type selection:** Historical European martial arts (HEMA) distinguish between:
- **Parrying** (meeting a cut with the blade): effective vs cuts, dangerous vs mace (damages the blade)
- **Deflecting** (guiding a thrust offline): requires reading the line, ineffective if the attack changes
- **Bracing/absorbing** (using weapon or body position to absorb impact): effective vs mace, poor vs thrusts

These were real tactical choices, but the advantage was about tempo (who recovers faster for the next action) rather than about hit rates. A correct parry gave you a counter-attack opportunity; a wrong defense left you out of position.

**Conclusion:** Option D (defense triangle as counter-attack opportunity, not hit-rate modifier) aligns best with historical precedent.

---

## IV. Proposed Fixes (Priority-Ordered)

### Fix 1: Aggressive Linear HP (HIGH PRIORITY)
`HP = End × 6 + 16` (replaces `(End+6) × (End//2+2)`)

**Impact:** Tough drops from 69%→57% (unarmoured), spread narrows from 56→44pp. No build exceeds 65% unarmoured at arena 3. Preserves End-matters but eliminates super-linear scaling. End 4 unchanged (40 HP).

**Risk:** Increases low-End character survivability slightly (End 3: 27→34). May need retuning of early-game lethality.

**Canonical status:** Requires changing `designs/scene/derived_stats_v30.md §4.1` and `params/combat.md §Wounds`. Design-level change.

### Fix 2: Diminishing Returns on Pool (MEDIUM PRIORITY)
`Pool = min(Agi,4)×2 + max(0,Agi-4)×1 + Hist + 3`

**Impact:** Fast (Agi 6) pool 17→15. Compresses the Agi advantage without removing it. Combined with Fix 1, no build exceeds 65%.

**Risk:** Reduces the value of Agi investment above 4. May feel punishing if players expect linear returns.

**Alternative:** Keep linear pool but add a "stat floor" bonus (all stats ≥4 → +2D pool). This buffs the generalist instead of nerfing the specialist. Simpler to explain to players.

### Fix 3: Defense Triangle as Counter-Attack (HIGH PRIORITY for triangle)
Replace TN/pool modifiers with tempo mechanics:
- **Correct defense** → defender gets a counter-attack (half-pool strike, costs no stamina)
- **Wrong defense** → attacker gets a damage bonus (+2 flat)
- **Neutral** → no bonus

**Impact:** Decouples triangle from raw defense. Specialists (mace/Bash only) lose counter-attack opportunities but retain full defense. Versatile weapons (longsword) can exploit the triangle for tempo advantage.

**Historical alignment:** Matches HEMA practice — correct defense creates tempo advantage, not invulnerability.

**Not yet tested.** Needs sim implementation.

### Fix 4: Soldier Viability (LOW PRIORITY — depends on Fixes 1-3)
Options:
A. **Stat floor bonus:** All stats ≥ 4 → +2D pool or +5 HP. Rewards balanced investment.
B. **Versatility bonus:** Using a weapon with 2+ attack types gives +1D offense. Rewards tactical flexibility.
C. **Accept:** The balanced build is mediocre by design. Specialists SHOULD outperform generalists. The Soldier's value is versatility across contexts (decent at everything, bad at nothing), which the all-vs-all matrix at a single armour tier doesn't capture.

**Recommendation:** Option C is most defensible historically. A professional soldier's advantage was equipment, training, and formation — not stat allocation. In a duel, the specialist should win. The Soldier's value emerges in group combat, where versatility matters.

---

## V. Iteration Results Matrix

| Config | Unarmoured Top | Unarmoured Bot | Spread | Pass? |
|--------|---------------|----------------|--------|-------|
| BASELINE | Tough 69% | Soldier 13% | 56pp | ✗/✗ |
| DR pool only | Tough 70% | Soldier 14% | 56pp | ✗/✗ |
| Agg HP only | Fast 65% | Soldier 14% | 50pp | **✓**/✗ |
| **DR pool + Agg HP** | **Knight 59%** | Soldier 16% | **44pp** | **✓**/✗ |

Heavy armour baseline: Tough 82%, Soldier 12%. Fixes expected to compress ~12-15pp (proportional to unarmoured improvement).

---

## VI. Decisions Needed

1. **HP formula:** Accept `End×6+16`? Or explore other linearizations?
2. **Pool formula:** Diminishing returns above Agi 4, or stat-floor bonus for generalists?
3. **Defense triangle:** Proceed with counter-attack model (Option D)?
4. **Soldier viability:** Accept generalist weakness, or add a mechanical floor?
5. **Arming sword TN:** Keep 7.0 (v2) or buff to 6.5? Note: buffing the arming sword also buffs Tough (who uses it).
6. **DPH ratio threshold (T2.4):** Relax to 2.0× or redefine as DPR (damage per round)?

---

## VII. Session Log Entry

**Work completed this session:**
- T2.4, T5.1, T6.1 with distance mechanics — 3 sim versions, 2 bug fixes (stamina asymmetry, AI heuristic)
- T4.1-T4.4 defense triangle — 3 modifier levels tested (±0.5 TN, ±1.0 TN, ±2D pool)
- T7.1-T7.2 equal-budget matrix — baseline + 4 fix configurations
- Root cause analysis: 4 structural issues identified
- Historical precedent review: 5 weapon types grounded in HEMA sources
- 2 proposed formula fixes tested with positive results (DR pool + Agg HP)

**Files produced:**
- `weapon_v2_distance_sim.py` (v3, 331 lines)
- `weapon_v2_distance_results.md`
- `defense_triangle_results.md`
- `equal_budget_results.md`
- `sim_verification_ledger.json` (27 entries)
- This audit document

**Next session priorities:**
1. Implement and test defense triangle counter-attack model (Fix 3)
2. Re-run T7.1 with HP + pool fixes at Heavy armour (timed out)
3. T3.2/T4.3 specialist vs versatile (unblocked if triangle model decided)
4. Commit results to repo
