# Mass Seizure Declaration Audit — 2026-04-20

**Trigger:** B5-7 observed 9/10 runs ending before CI 100 ("early-ends via shared-loss"). ED-725 open item asked whether Seizure curve is too shallow or shared-loss mechanics are dominating.

## Investigation (20 seeds, engine_v3 post ED-721/722/723)

| End cause | N / 20 |
|-----------|--------|
| Crown victory (peninsula control) | 11 |
| Altonian Conquest (IP ≥ 100 + AER ≤ 1) | 5 |
| SHARED_LOSS (RS = 0, Rupture) | 2 |
| Hafenmark victory | 1 |
| 40-season timeout | 1 |

**Mass Seizure declared in 4/20 runs.** Theocracy Unification reached in 0/20.

End season: mean S16.6, median S15.5. CI at end: median 31 (below Mass Seizure threshold).

## Finding

**The Seizure curve is not too shallow. Crown's conquest timeline (S6–S20 resolutions) dominates.** Most campaigns end via Crown peninsula-control victory or Altonian invasion loss before Church CI reaches Mass Seizure declaration reliability (CI 80+, ~35% per season).

Crown NPC AI aggressively pursues military conquest — Legionary deployments, Royal Decrees targeting rival Mandate, submitting weaker factions. By S15, Crown has often absorbed 2–3 factions; the remaining factions lack the collective Mandate to sustain Church-opposing Parliamentary votes, but Church hasn't yet built CI to 60.

## Disposition

This is a **campaign balance observation, not a sim bug or design gap.** Church Mass Seizure is mechanically sound (B3/B4 re-run confirmed CI growth timing S7–S20 for Unification under cap headroom). The issue is that *other win conditions fire first* under current AI aggressiveness.

Three balance levers worth considering (NOT NEEDED for ED-722 validation — defer to broader balance pass):

1. **Dampen Crown conquest speed** (e.g., Military recovery penalty after absorbing a faction, or attacker-side Stability cost on conquest)
2. **Accelerate Church CI** (e.g., raise Conditional Passive to +2, or remove Hafenmark structural −1 when Baralta M < 5)
3. **Soften Altonian Conquest shared-loss** (e.g., IP ≥ 100 requires AER ≤ 0 AND additional condition; currently fires too easily when AER drifts)

None of these should be acted on without broader playtest / sim validation. **Flag for engine_v4 B-series post-migration audit.**

## Sub-finding: Mass Seizure declaration probability curve

Current: `P = ((CI − 40) / 60) ^ 2.5`, clamped [0, 1].

| CI | P |
|----|---|
| 50 | 2% |
| 60 | 8% |
| 70 | 19% |
| 80 | 35% |
| 90 | 57% |
| 100 | 100% |

The shape is intentional (models institutional restraint). At CI 80+ the curve yields reliable declaration within 2–3 seasons. **The shape is fine; the problem is that CI rarely reaches 80 before campaign ends.**

## Closed
No canonical change. Audit flagged for future balance pass.
