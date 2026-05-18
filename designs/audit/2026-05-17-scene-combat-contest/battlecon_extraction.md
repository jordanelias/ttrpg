# BattleCON Mechanic Extraction for C4

**Date:** 2026-05-17
**Companion to:** `designs/audit/2026-05-17-scene-combat-contest/decisions.md`
**Purpose:** Extract BattleCON pool-bypass mechanics; map to Valoria scene-combat C4 candidates; refine ED-864 direction.

## Direct sim reads (closing audit transitive-citation gap)

`tests/sim/phase8_smart_ai_v2_2026-05-15.md` and `phase10_str_stam_reform_2026-05-16.md` read full. Three findings refine prior audit:

1. **Pool dominance saturates at Agi 5, not Agi 6.** Phase 8 ROI table: Agi 4 → 95.6% vs Strong; Agi 5 → 99.9%; Agi 6 → 99.9%. Step function, not linear. One die of Agi advantage already produces 95%+ dominance.
2. **Phase 10 best-reform-stack lands Fast vs Titan at 70/30** (empirical, not extrapolation). C4 must beat this.
3. **Balanced builds work.** Fast (Agi 6) vs Fast-strong (Agi 5 STR 5) = 52.6%. Problem is extreme stat-distribution gaps, not pool grammar generally.

## BattleCON load-bearing mechanics

| Mechanic | Pool-bypass strength | Pattern |
|---|---|---|
| Range gate — attack misses if out of range | Strongest | Pool irrelevant when range fails |
| Priority — stun preempts | Strong | Action preemption, not just turn order |
| Style+Base simultaneous reveal | Medium-strong | Mind-game over pool; no info advantage |
| Discard cycle — used cards return 2 beats later | Medium | Best techniques cannot repeat |
| Asymmetric per character | Medium-strong (expensive) | No global combat stat |
| Soak / Stun Guard | Medium | Damage-cap independent of pool |

## Three C4 candidates

### M1 — Reach/Distance gate (primary)

Promote Distance from positional flavor to gate mechanic. Mismatched-reach attacks reduce attacker's effective pool to **1D + History** for that round (not Agi-doubled).

- Heavy weapon (reach 3) vs light blade (reach 1) at far distance: heavy attacks normally; light attacks at 1D + History.
- Closing distance: tactical action gated by Stamina + Agility. Fast can close, but spends turns; heavy gets free strikes during those turns.
- Uses existing Distance vocabulary; cleanest implementation.

### M2 — Stance × Stance counter-table (secondary)

4 stances (Pressure / Patience / Decisive / Cautious). Round-start simultaneous declare. Matchup table assigns flat pool reduction or pool-bypass effect:

- Patience vs Decisive → Decisive loses 3D this round (overcommitment)
- Cautious vs Pressure → Pressure capped at Partial Success degree max regardless of net (defense caps degree)
- Pressure vs Patience → Patience cannot Take Breath this round (drawn in)
- Decisive vs Cautious → Cautious cannot apply degree-cap (commitment beats hedging)
- Same-stance matchups → no counter; raw pool resolution

### M3 — Initiative preemption (tertiary)

Higher Init preempts opponent's action — cancel their pool roll for the round entirely. Costs preempting side 2 Stamina.

- Gives Att / Foc (Initiative attributes) a real combat lever.
- Stamina cost prevents repeated preemption.
- Rewards under-invested attributes.

## Stacking estimate (pre-sim)

- M1 alone: Fast vs Titan ~60/40
- M1 + M2: ~55/45
- M1 + M2 + M3: ~50/55

Phase 11 sim required to confirm.

## C2 not abandoned — layered with M1

Weapon-keyed primary attribute (C2) combines naturally with M1:
- Light weapons → Agility primary
- Heavy weapons → Strength primary
- Long weapons → Endurance primary (reach as resilience)
- Ranged → Cognition or Attunement primary

Combined effect: Strong-with-heavy gets pool-favorable matchup at range AND keeps reach advantage. Fast-with-light dominates closed range but must close to apply pool. Distance choice becomes the meta-game.

## Phase 11 sim plan

Implement M1 + M2 + M3 in `tests/sim/phase11_c4_v0.py`. Target matchups:

| Matchup | Current (Phase 10 best) | Phase 11 target |
|---|---|---|
| Fast (Agi 6, light) vs Titan (End 6 STR 7, heavy) | 70/30 Fast | 50–60% Fast |
| Mighty-heavy (Agi 3 STR 7, heavy) vs Fast (light) | 8% Mighty | 50–60% Mighty |
| Mighty (Agi 3 STR 7, light) vs Fast | 1.5% Mighty | 25–40% Mighty (F3-gap test) |
| Balanced Fast-strong (Agi 5 STR 5) vs Fast | 52.6/47.4 | Hold 50/50 |
| Symmetric Agi 3 vs Agi 3 | 51.2/48.8 | Hold 50/50 |

If targets land: C4 solved. If not: layer C2 (weapon-keyed pool) on top.

## Open canonical questions for design owner

1. **Reach gate severity.** 1D+History is aggressive. Alternatives: 2D+History; OR full pool at TN 8 (Desperate); OR no attack possible (binary gate). Mid-severity options preserve fluidity but may not break dominance.
2. **Stance counter-table magnitudes.** −3D for Decisive-vs-Patience is empirical guess. Sim will tune.
3. **Preemption stamina cost.** 2 Stamina is empirical guess. Higher cost (3-4) makes preemption rare; lower (1) makes it spammable.
4. **C2 layering decision.** Defer until M1+M2+M3 sim runs.

## Citation gap status

Closed for Phase 8 + Phase 10. Still open: `mc_v17.py` integration engine; prior balance audit. Neither blocks C4 sim work.

## Next actions

- T8: draft `designs/scene/combat_c4_draft_v0.md` — formal mechanic specs, sim-implementable.
- T9: implement `tests/sim/phase11_c4_v0.py`; run sim; report vs targets.
- T10: ratify or revise C4 per Phase 11 outcomes; commit to params/combat.md + combat_v30.md.
