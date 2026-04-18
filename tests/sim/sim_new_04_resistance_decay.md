# SIM-NEW-04 — BG + TTRPG: Resistance Decay in Practice + Crown/Hafenmark Co-Victory
## Mode: A (Isolation) + C (Full Scenario) + B (Interaction Chain)
## Date: 2026-04-08

---

## FETCH LOG
canonical_sources.yaml: ✓ (156 lines)
params_debate.md: ✓ (409 lines)
params_board_game.md: ✓ (1431 lines)
victory_architecture_v1.md: ✓ (412 lines)

---

## Part 1: Resistance Decay (New Mechanic — ED-330 resolved)

### Mode A: Decay Rate Mathematics

**Rule (PP-461):** Each 0-movement exchange reduces effective resistance by 0.25, cumulative, floor 0, reset per scene. Base resistance = ceil(avg Stability / 4).

**Scenario:** Baralta (Hafenmark, Arg pool 11D) vs Cardinal Klapp (Church, Arg pool 10D). Primary genre: Past. Both audiences: resistance 2 (Stability 4, ceil(4/4) = 1 per faction, averaged = 1.5 → ceil = 2).

**Exchange 1 — CLASH, Klapp Revealing, Baralta Obscuring:**
Klapp net: E(10D) ≈ 5.7. Baralta net: E(11D) ≈ 6.3. Expected margin ≈ 0.6.
Movement = ⌊(0.6 × 1.5 × 1.0) − 2⌋ = ⌊−1.1⌋ = 0. **0-movement.** Resistance decay fires: effective resistance = 2 − 0.25 = **1.75**.

**Exchange 2 — CLASH again:**
Same pools. Expected margin ≈ 0.6.
Movement = ⌊(0.6 × 1.5 × 1.0) − 1.75⌋ = ⌊−0.85⌋ = 0. **Still 0-movement.** Decay: 1.75 − 0.25 = **1.50**.

**Exchange 3:**
Movement = ⌊(0.6 × 1.5 × 1.0) − 1.50⌋ = ⌊−0.6⌋ = 0. **Still 0-movement.** Decay: **1.25**.

**Exchange 4:**
Movement = ⌊(0.6 × 1.5) − 1.25⌋ = ⌊−0.35⌋ = 0. Still 0. Decay: **1.00**.

**Exchange 5:**
Movement = ⌊(0.6 × 1.5) − 1.00⌋ = ⌊−0.10⌋ = 0. Still 0. Decay: **0.75**.

**Exchange 6:**
Movement = ⌊(0.6 × 1.5) − 0.75⌋ = ⌊0.15⌋ = **0** (still 0 — floor of positive fraction). Decay: **0.50**.

**Exchange 7:**
Movement = ⌊(0.6 × 1.5) − 0.50⌋ = ⌊0.40⌋ = 0. Still 0. Decay: **0.25**.

**Exchange 8:**
Movement = ⌊(0.6 × 1.5) − 0.25⌋ = ⌊0.65⌋ = **1.** First CT movement after 7 zero-movement exchanges.

**Finding P1 — Resistance decay correctly terminates stalemate.** At the expected margin of 0.6, stalemate breaks after 7 exchanges (approximately 7 rounds of debate at ~5 minutes each = a manageable scene). This is far better than the ~30 exchanges needed without decay.

**Sensitivity check — lower margin (pools further apart: 15D vs 8D, expected margin ~4):**
Exchange 1: Movement = ⌊(4 × 1.5) − 2⌋ = ⌊4⌋ = 4. No stalemate at all with unequal pools. Resistance decay only activates when stalemate already exists. Correctly targeted.

**Sensitivity check — equal pools (10D vs 10D, expected margin ~0):**
Without variance: both roll exactly the same every exchange. Margin = 0. A TIE fires (both take 1 strain, CT +1 toward initiative holder). The TIE rule prevents zero-margin CLASH from being a pure stalemate — a TIE still produces 1 CT movement. Resistance decay fires for the TIE exchange (no movement from the formula even though TIE rule produces movement). Slight interaction: resistance decays even during TIE exchanges.

**Finding P2 — TIE rule and resistance decay interact cleanly.** TIE produces 1 CT movement (not from the formula, from the TIE rule). The resistance decay still fires because the formula produces 0 movement. Both mechanisms coexist without conflict — in a TIE, CT moves by 1 (TIE rule) AND resistance decays by 0.25 (decay rule). This double-fires the stalemate-escape mechanism but does no harm: TIE already produces movement, decay is an additional minor acceleration.

---

## Part 2: Crown + Hafenmark Co-Victory

### Co-Victory Conditions (§4)

| Pair | Conditions |
|------|-----------|
| Crown + Hafenmark | Crown TCV ≥ 12 AND Hafenmark TCV ≥ 9 AND PI ≥ 5 AND TC < 50 |

Hold 2 consecutive Accounting steps.

### Mode C: Crown/Hafenmark Co-Victory Race

**Season 8 game state (standard 4-player game):**
| Faction | TCV | Mandate | Notes |
|---------|-----|---------|-------|
| Crown | 12 | 5 | At co-victory TCV threshold |
| Hafenmark | 9 | 4 | At co-victory TCV threshold |
| Church | 4 | 5 | TC 36 |
| Varfell | 6 | 4 | VTM 2 |

PI: 6. TC: 36. RS: 70.

**All co-victory conditions at S8:**
- Crown TCV ≥ 12: ✓
- Hafenmark TCV ≥ 9: ✓
- PI ≥ 5: ✓ (PI 6)
- TC < 50: ✓ (TC 36)

**Co-victory fires at S8 Accounting.** But requires 2 consecutive Accounting steps. Must hold through S9.

**Can other factions disrupt in S9?**
- Church: plays Assert (TC +2 → TC 38). Still < 50. TC condition holds.
- Varfell: cannot disrupt TCV (no way to reduce Crown or Hafenmark TCV quickly — would need to militarily seize territories). Varfell Military 4D vs Crown Fort territories: Crown holds T3 (Lowenskyst, Fort 3). Varfell 4D vs 7D (Crown 4D + Fort 3): P(Varfell wins) ≈ 12%. Very unlikely.
- Church: can try to lower PI. PI 6 → need PI ≤ 4 to disrupt. Church Emergency Powers (Crown card, not Church's). Church has no PI-lowering action directly.

**S9 — Crown and Hafenmark hold positions.** No successful disruption. **Co-victory fires at S9 Accounting.**

### Mode B: Strategic Implications

**Crown + Hafenmark co-victory is the most achievable win condition for those two factions combined.** The conditions (TCV thresholds both factions can hit by S6–8, PI ≥ 5 which is the starting value, TC < 50 which holds for at least 11 seasons from start) create a low-difficulty joint win.

**Compared to solo wins:**
- Crown solo: TCV ≥ 16 + all rivals Mandate ≤ 2 + IP < 60 + PI ≥ 3. Harder (TCV 16 requires capturing 4 more territories beyond starting 12).
- Hafenmark solo: TCV ≥ 12 + Mandate ≥ 4 + PI ≥ 5 + Crown M ≤ 3. Requires Crown suppression.
- Co-victory: TCV 12 (Crown already starts here) + TCV 9 (Hafenmark starts at 8, needs 1 more territory) + PI ≥ 5 + TC < 50.

**Finding P1 — Crown + Hafenmark co-victory is potentially achievable from Season 2.** Hafenmark starts at TCV 8 and needs TCV 9 — one additional territory (any TCV 1 territory via uncontested March). Crown starts at TCV 12. PI starts at 7. TC starts at 28 (< 50). All conditions potentially met by S2 if Hafenmark takes one territory. The only gate is the 2-season hold requirement.

**[EDITORIAL: ED-342 — Crown/Hafenmark co-victory may be trivially achievable from S2 if Hafenmark takes 1 uncontested territory. Consider whether the conditions are too easily met, particularly since TCV starts are very close to thresholds (Crown 12/12, Hafenmark 8/9). May need TCV thresholds raised or additional conditions added. P2.]**

**Church counter-play:** Church can disrupt co-victory by raising TC ≥ 50 before the 2-season hold completes. TC starts at 28. TC 50 requires 22 seasons at +1/season or 11 at +2/season (Assert). Church cannot rush TC 50 fast enough to stop an early co-victory. Assert raises TC by 1 per season (replaces passive). From TC 28 to 50 = 22 seasons minimum. Co-victory fires at S2–S3.

**Finding P2 — Church has no counter to early Crown/Hafenmark co-victory.** At TC 28, Church cannot reach TC 50 in time to block a S2–S3 co-victory. This is structurally unbalanced: Church's primary disruptive lever (TC threshold effects at 50+) is 20+ seasons away when co-victory is available from S2.

---

## Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-RD-01 | P1 | Resistance decay breaks CLASH stalemate after ~7 exchanges at expected margins. Correctly targeted — only activates during zero-movement exchanges. |
| F-RD-02 | P2 | TIE rule and resistance decay interact cleanly (both fire; no conflict). TIE exchanges decay resistance despite producing 1 CT movement via TIE rule. |
| F-CV-01 | P1 | Crown/Hafenmark co-victory potentially achievable from S2 (Hafenmark needs only 1 territory). No Church counter-play available at that timeline. |
| F-CV-02 | P2 | Co-victory TCV thresholds may be too close to starting values — conditions feel underdone relative to solo win paths. |

