# B3/B4 Re-run on Corrected engine_v3 — ED-721 + ED-722

**Date:** 2026-04-20
**Engine:** `tests/sim_framework/engine_v3.py` post ED-721 (PT_TIER non-linear lookup) + ED-722 (SW seed corrections T12 1→2, T14 2→3)
**Trigger:** ED-721/722 invalidated B3/B4 Piety-Yield-saturated-cap findings; this is the formal re-run.

---

## Setup

- **PT_TIER lookup (ED-721):** `{5: 1.0, 4: 0.5, 3: 0.25, 2: 0.10, 1: 0.0, 0: 0.0}`
- **SW seed (ED-722, params/bg/geography.md):** T9=5, T8=3, T14=3, T12=2, T1/T2/T3/T5/T7/T10/T17=2, T4/T6/T11/T13/T16=1, T15=0
- Engine TERRITORIES table corrected: T12 1→2, T14 2→3
- All other Sessions B/C canon active (graduated Löwenritter autonomy, Niflhel dissolution, Tensions Deck, etc.)

---

## Sanity check (S1, seed 42)

```
T9: SW=5, PT=5, controller=Church
T8: SW=3, PT=3, controller=Hafenmark
T14: SW=3, PT=3
T1: SW=2, PT=3 (Crown-controlled)
Total SW (engine): 31

Season 1 CI delta: +3 (was +5 saturation in B4)
Sources: Conditional Passive +1 (Church.M 5 > Hafenmark.M 4 in 2+ territories)
       + Piety Yield +1 (T9 only, 1.0 × 5/5 = 1.0 floored)
       + Templar Presence +1 (T9 templar=True)
```

Cap (+5/season) NOT saturated. Assert remains relevant.

---

## CI Growth Trajectory (10 seeds, 40 seasons each)

| Policy | Mass Seizure available (S, mean / range) | Theocracy Unification (S, mean / range) | Failed in 40s |
|--------|------------------------------------------|------------------------------------------|---------------|
| passive only (no Church Domain Action) | S7.9 / S7–S9 | S18.4 / S17–S20 | 0/10 |
| Assert each season (when available) | S6.6 / S6–S8 | S15.2 / S14–S17 | 0/10 |
| Assert + Hafenmark Suppress each season | S7.7 / S7–S9 | S18.6 / S17–S20 | 0/10 |

---

## Findings

### 1. ED-721 PT_tier correction reduces Piety Yield magnitude but not effective campaign timeline

The B4 finding "+5/season cap saturated from S1, Assert irrelevant" was an *artifact of the literal-PT formula bug* in arc_test_batch4.py:109 (`pt * sw / 5 = 25/5 = 5`). Under canonical PT_tier lookup, T9 yields 1 CI/season floored — but **other passive sources (Conditional Passive +1, Templar Presence +1, occasional Charity +0–2) still combine to ~+3/season at game start**. The +5 cap is approached but not saturated.

Net: Mass Seizure available S7–9 (was S5–7 under bugged formula); Unification S15–20 (was S15–18 under bugged formula). **Same general timeline; Assert reduces it by ~3 seasons.**

### 2. Assert is mechanically relevant but marginal

Assert each season pulls Unification forward by ~3 seasons (S18.4 → S15.2). A Church player who skips Assert still wins via passive accumulation — Assert is **utility-positive but not strategy-decisive**. This is consistent with Assert being one of several CI sources, not the dominant one.

### 3. Hafenmark Suppress at Baralta M ≥ 4 fully neutralizes Assert

Adding Suppress each season (with Baralta M ≥ 4, ~70% success) restores the timeline to passive-only (S18.6 ≈ S18.4). **Hafenmark structural suppression is the canonical counter to Church Assert**, not to Piety Yield itself. The mid-game political race is Church Assert vs Hafenmark Suppress, with Piety Yield as the steady background drift.

### 4. SW seed corrections (T12 1→2, T14 2→3) are minor

Engine TERRITORIES had T12=1 and T14=2 vs canonical geography T12=2, T14=3. Correcting these adds +1 to Σ SW (from 30 to 31) and increases T14 Piety Yield only when Church Prominent there (Church.M 5 > Crown.M 5 → Church not yet Prominent in T14 at game start). Effect on timeline: negligible at S1; matters once T14 changes hands.

### 5. ED-722 dynamic SW: not yet stress-tested

This re-run does not exercise the dynamic-SW mechanic — neither B3 nor B4 destroys Church religious infrastructure. To validate ED-722's "loss of Cathedral collapses Piety Yield" prediction, future B5 should include a Church-loses-Himmelenger scenario (e.g., Varfell conquers T9 + sacks S-023 Cathedral). Predicted effect: SW(T9) drops 5 → 2, T9 yield falls from 1 → 0 floored, Church loses ~1 CI/season permanently. Combined with loss of Templar Presence and probable PT decay in non-Church-controlled T9, total CI drift loss ≈ 2/season — a meaningful structural penalty consistent with the design intent.

---

## Disposition of B3/B4 invalidated findings

| Original finding | Status |
|------------------|--------|
| Piety Yield saturates +5 cap from S1 (B4) | **Refuted.** Yield = 1/season from T9. Combined passives ~3/season. |
| Assert is irrelevant from turn 1 (B4) | **Refuted.** Assert reduces Unification timeline by ~3 seasons. |
| Mass Seizure timing S12–14 (B3) | **Updated.** Seizure available S6–9 across policies; declared per ((CI−60)/40)^3.3 probability — actual fire S10–S20+. |
| Theocracy Unification timing S15–18 (B4) | **Confirmed range.** S15–20 across policies. |
| Hafenmark Suppress as primary counter to Church | **Confirmed.** Suppress neutralizes Assert; restores passive-only timeline. |
| Coup → Church alliance interaction (B4-3) | **Re-evaluation needed.** Original claim "PI=0 gives CI+2/season; Church reaches 100 faster" depended on cap headroom that we now have less of. Defer to dedicated B5. |

---

## Open items
- B5 should stress-test ED-722 dynamic SW under settlement loss/sack scenarios.
- engine_v3 model is per-territory, not per-settlement. Building a per-settlement model is engine_v4 scope (campaign_architecture_v1 §1.1 alignment).
- AER generation mechanic (B3 gap #9) still not specified — independent of this re-run.
