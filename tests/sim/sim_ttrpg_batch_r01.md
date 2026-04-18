# Combat Simulation — Run 1
**Parameters:** Str 3 / End 3 / Agi 3, Competent (Combat Pool 8), Health 9, 666 unordered matchups  
**Model:** Analytical (expected damage ratio → win probability). Engagement opens at Long range.

---

## Key Findings

### F-SIM-001 — Armour dominance over weapon weight (P1 BALANCE)
Heavy armour at Str 3 costs −1D Combat Pool (pool 7 vs 8) but grants DR 3. This trade is overwhelmingly positive. A Light weapon + Heavy armour fighter beats Medium weapon + no armour **100%** of the time in same-reach matchups. The damage reduction is so powerful relative to the pool penalty that armour tier effectively determines combat outcome more than weapon weight in many matchups.

**Root cause:** DR 3 neutralises most excess-success damage at this stat level. With pool 8, expected excess successes per hit ≈ 1–2, meaning a Heavy weapon (+2 dmg) still only deals ~3–4 damage before armour. DR 3 reduces this to 0–1. Meanwhile the −1D penalty (pool 7) only marginally reduces hit probability.

**Implication:** At Str 3, Heavy armour is near-mandatory. The −1D penalty is too cheap for the benefit received.

**Patch options:**
- A: Increase Heavy armour Str minimum to 4 (makes it inaccessible at Str 3 entirely)
- B: Increase Heavy armour pool penalty to −2D at Str 3 (one below minimum)
- C: Cap DR at excess successes (armour only reduces damage from margin, not base weapon bonus) — structural change

---

### F-SIM-002 — Short reach catastrophically weak at opening (expected, confirm intended)
288 of 666 matchups are LOCKED (Short weapon vs Long or Versatile at Long range = 0 offence). Short-weapon builds average 8.6–11.7% win rate across all matchups. This is structurally correct — the fight opens at Long range and Short fighters must manoeuvre before attacking. But 0% offence for the entire first round and no modelled manoeuvre success probability means Short fighters never win any cross-reach matchup in this model.

**Root cause:** Model treats LOCKED as permanent (no manoeuvre contest simulated). In actual play, a Short fighter would spend round 1 maneuvering (Reorient/Withdraw), contesting on Agility. The simulation does not model this exchange.

**Action required:** Run 2 must model manoeuvre rounds — probabilistic range-band change per round based on Agility vs Agility contest.

---

### F-SIM-003 — Long + Heavy armour dominates all same-reach matchups (P2 BALANCE)
Top builds by average win rate:
| Build | Avg Win Rate |
|---|---|
| Long-Heavy / Heavy armour | 93.8% |
| Vers-Heavy / Heavy armour | 91.6% |
| Long-Heavy / Medium armour | 78.8% |
| Vers-Heavy / Medium armour | 74.6% |
| Long-Medium / Heavy armour | 71.3% |

Bottom builds:
| Build | Avg Win Rate |
|---|---|
| Short-Heavy / None | 8.6% |
| Short-Light / None | 8.7% |
| Short-Medium / None | 10.7% |

Long + Heavy armour is dominant. Short + no armour is nonviable. The distribution is too wide.

---

### F-SIM-004 — Versatile weapon penalty insufficient vs Long (P2 BALANCE)
Versatile fighters lose to same-weight Long fighters in most matchups. The −1D Versatile penalty is working as intended (Long beats Versatile), but the margin is often extreme (Long-Heavy/Heavy vs Vers-Heavy/any = 87–100%). Versatile weapons are paying double: −1D to attack AND they fight Long weapons at Long range with no reach advantage. The cost may be too high relative to the flexibility benefit.

**Note:** This finding depends on Run 2 (manoeuvre modelling). If Short fighters can reliably close, Versatile becomes more useful as a hedge. Reserve patch decision until Run 2.

---

### F-SIM-005 — Mirror matchups correct (42.5% / 42.5% / 15%)
All identical build matchups return symmetric results. Draw fraction of 15% is a model artefact of the margin-based draw calculation, not a mechanical issue. Acceptable for this run.

---

## Run 2 Requirements
1. Model manoeuvre contest (Agility vs Agility, contested roll) per round for range-band changes
2. Track range band state across rounds (starts Long; Short fighter attempts to close each round)
3. Cap rounds at Stamina maximum before Catch Breath penalty applies
4. Re-evaluate Short weapon builds with manoeuvre probability

## Patch Proposals Generated
- PP-NEW-A: Heavy armour Str penalty rebalance (F-SIM-001) — P1
- PP-NEW-B: Versatile weapon penalty review (F-SIM-004) — P2, defer to Run 2
