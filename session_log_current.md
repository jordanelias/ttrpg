# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_SOUTHERNMOST_FIX
phase: SESSION CLOSED
status: COMPLETE

## SOUTHERNMOST ACCESS CLARIFICATION (PP-205)

User confirmed: Stillhelm (T13) is a normal territory. The Southernmost access
gate applies only to T15 Askeheim.

### Changes Applied
T13 Stillhelm: Reverted PP-203 Fort 1 and "march triggers Warden Emergence" rule.
Both were wrong. T13 is a normal Crown territory with:
  - Non-Thread orders +1 Ob (difficult frontier terrain)
  - RS -1/season occupation (substrate proximity)
  - No special access restrictions
  - Warden Cooperation track inactive here (activates only in T15)

T15 Askeheim: Full Southernmost access system defined.
  - Not a normal territory. No faction control possible. Ever.
  - Access gate: Champion TS >= 30 staged in T13 for >= 1 season
  - Expedition declaration: pool = TS/10 (min 1D, max 3D) vs Ob 3
  - Forgetting Check on entry: same pool vs Ob 2
  - Failure = present but retains nothing; Success = Warden contact possible
  - Edeyja contact: Overwhelming on Forgetting Check or Success + 1 prior season
  - Edeyja TS 75-80: she will not engage TS < 30; TS 40+ = substantive contact

### Varfell Paths Correctly Stated
Path B (T4+T13): T13 is a normal territory. The deed measures political
presence at the Southernmost threshold, not T15 occupation.
Path C (T4+T13+1 other): same.
T15 never appears as a territorial deed condition.

### Vaynard is the Only Qualifying Champion at Game Start
VTM 3+ = TS 30. Marginal but valid. VTM 4+ = TS 40, Edeyja will engage.
No other faction Champion qualifies without extraordinary development.

## Gate: PASS

## Commits
61f3239d: PP-205 Southernmost access system

next_session_start:
  priority_1: "Run freshness_gate.py check first."
  priority_2: "BAL-BG-03: verify Varfell Path B is still adequately gated now that
    T13 is normal (2-season hold under Crown pressure still applies from PP-203)."
  priority_3: "Road network design (still deferred)."
  priority_4: "ED-108: confirm T10/T11 territory names."
```
