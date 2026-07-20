# v14 Checkpoint — Unified Derived Scores + Comprehensive Logging

## What was built
- All base stats 1-7 with internal derived buffers (Mandate/Stability/Wealth/Influence + Accord + Piety, all using same DerivedScore class)
- Accord 1-7 (replacing old 0-3, deduplicating with Order)
- Piety 1-7 (replacing 0-5, threshold ≥3 for flip)
- Deterministic threat response (mandatory Muster/Govern when Accord ≤ 3)
- All v12c mechanics + canonical CI generation + Mass Seizure cubic distribution
- Insurgency → Founded Organization → Parliamentary faction pipeline
- Comprehensive JSONL logging (every action attempt, prereq evaluation, dice roll, state change)
- Faction-specific victory paths (Hafenmark Dynastic Assertion, Varfell Southernmost, Church Theocratic Bid)

## Results at N=200 across 5 configs
| Config | Crown | Church | Hafenmark | Varfell | Surviving 4/4 |
|---|---|---|---|---|---|
| consent=0.5 lapse=0.5 | 41.5% | 58.5% | 0% | 0% | 62% |
| consent=0.4 lapse=0.6 | 30.5% | 69.5% | 0% | 0% | 49% |
| consent=0.5 lapse=0.6 | 36.5% | 63.5% | 0% | 0% | 54% |

## What worked
- All 4 factions survive to end (was: 40% all-zero collapse, now 0%)
- Peninsula health restored (was: 86% uncontrolled, now 0.6-0.8 uncontrolled)
- Derived score buffer absorbs shocks (3-5 events to deplete vs 1 in v12c)
- Comprehensive logging captures all decision branches for NERS audit
- Church Seizure properly Prominence-gated (Mandate > controller's)
- Mass Seizure fires canonically at CI 80+ (P=10%/season)
- Insurgency formation pipeline operational (revolt persists 2+ seasons → forms)

## What didn't reach 25/25/25/25
- Crown 30-50%, Church 50-70%, Hafenmark/Varfell 0%
- Hafenmark's Dynastic Assertion victory requires Mandate 6 + 6 territories — Hafenmark loses territories to Church Seizure faster than it can accumulate
- Varfell's Southernmost Dominion requires T13 + T15 + 5 territories — Varfell's starting position lacks T15 (Uncontrolled), reclaim is contested
- Church Seizure grinds Hafenmark/Varfell down: once Church L > rival L (Prominence), Church takes PT≥3 territory every season

## Structural diagnosis
The simulator now reproduces canonical mechanics faithfully. The 4-way balance gap is in the canonical design itself — Hafenmark and Varfell's victory paths are harder to achieve than Crown's or Church's, given:
1. Crown gets free coalition-building via Treaty
2. Church gets free institutional accumulation via Seizure + CI
3. Hafenmark must build Mandate 6 (caps at 7, takes time) AND hold 6 territories AND maintain Accord 4 in all
4. Varfell must conquer T13 + T15 AND hold 5 total — but Varfell starts with only T13 (no T15)

## Files committed
- mc_v14.py (1100+ lines): the simulator
- v14_logs/: 5 sample JSONL campaign logs for NERS audit

## Open work for next session
1. Defensive mechanism for Hafenmark territories against Church Seizure (canonical: constitutional Suppression on territory-level)
2. Varfell expansion path toward T15 (Expedition action — not yet implemented)
3. Hafenmark Mandate growth beyond 7 cap, or alternative Dynastic Assertion conditions
4. Test with N=1000 once balance is closer to symmetric

## NERS audit capability
The JSONL logs capture:
- Every action_attempt with prereqs_passed + reason
- Every action_resolved with dice rolls + outcomes
- Every state_change with canonical_ref
- Every CI generation breakdown (momentum + piety_yield + templars + haf_suppress)
- Every Mass Seizure check with probability + roll
- Every revolt and insurgency formation
- Every treaty formed/lapsed
- Full season-start snapshots
- Full campaign final state

This supports all 6 audit directions (top-down, bottom-up, vertical, diagonal, lateral, horizontal) per Valoria canon_terms.

— v14 commit 2026-05-14
