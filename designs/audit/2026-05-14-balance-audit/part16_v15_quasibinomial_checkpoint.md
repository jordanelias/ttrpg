# v15 Checkpoint — Quasibinomial Fractional Stats Architecture

## Architecture (per Jordan direction 2026-05-14)

### Stat representation
- All stats are floats 1.0–7.0 (no integers)
- Player-facing display multiplies for legibility:
  - Mandate = L × 20, Stability = Sta × 10, Wealth = W × 100, Influence = I × 15
  - Accord (territory) = a × 10, Piety (territory) = p × 10
- The float stat IS the value. Display multipliers are remapping for granular UX.
- No buffer class, no depletion checks. Events apply granular changes directly.

### Dice mechanics
- Pools can be fractional (e.g. 4.3 dice)
- Successes sampled via quasibinomial: Mean = N×p, Variance = φ×N×p×(1−p)
- Implementation: normal approximation with overdispersion parameter
- Continuous success count compared to integer Ob → degree

### Granular events
- "Territory lost" → Mandate −15 (= −0.75 L equivalent)
- "Govern Success" → Mandate +2 (= +0.1 L)
- "EA Success" → Mandate +20 (= +1.0 L — major institutional event)
- "Peaceful season" → Stability +3 (= +0.3 Sta)
- Granularity provides resilience: 5+ minor events to shift integer stat by 1

## Removed (non-canonical)
- Per-season Church Seizure as a discrete action (canon only has Mass Seizure one-shot)
- DerivedScore class with depletion checks
- Hafenmark suppression scaling with Mandate (reverted to canonical flat -1)

## Verified mechanics
- Mass Seizure auto-fires at CI ≥ 60 with cubic probability ((CI−60)/40)^3.3
- CI generation: Institutional Momentum +1 + Piety Yield + Templar count − Hafenmark suppression
- Deterministic threat response (mandatory Muster/Govern when Accord ≤ 3)
- Insurgency → Founded Organization pipeline (2+ contiguous Uncontrolled, persists 2 seasons)
- Universal Peninsular Sovereignty as the ONLY victory path (11/15 with treaties counting)

## Current results (N=100, consent=0.4 lapse=0.7)
| Faction | Win % | Avg Terr End |
|---|---|---|
| Crown | 48% | 1.1 |
| Hafenmark | 50% | 10.3 |
| Church | 2% | 2.8 |
| Varfell | 0% | 1.6 |

## What's still broken
- Crown overweight via coalition; Hafenmark overweight via DP accumulation
- Church has no per-season territorial acquisition path (Mass Seizure is one-shot)
- Varfell's Einhir Revival fires rarely (limited adjacency × PT prereqs)
- Surviving 4 factions only 27% of campaigns (target: ≥80%)

## What's right architecturally
- Quasibinomial sampling produces continuous outcomes — granularity all the way down
- Fractional stats handle small events naturally (no integer floor issues)
- Player-facing multipliers are display-only (computation never uses them)
- All v12c mechanics + canonical CI/Mass Seizure + Insurgency pipeline preserved
- Comprehensive JSONL logging maintained for NERS audit

## Files committed
- mc_v15.py: the architecture
- Logs are not committed but produced at /home/claude/v15_logs/ during runs

## Next iteration
- Lower Crown coalition strength (lower CONSENT_RATE or treaty utility)
- Provide Church a per-arc Mandate-gated territorial acquisition (canonical Cardinal slot)
- Strengthen Varfell Einhir Revival or add Expedition action toward T15
- Test if Hafenmark suppression should be -2 when Hafenmark L ≥ 5 (modest scaling)
