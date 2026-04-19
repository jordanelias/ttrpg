# Editorial Decisions — TC/CI/TCV/Seizure/Victory — 2026-04-18
# [EDITORIAL: ED-NEW — Jordan decisions resolving conflict register]

## Decision 1: CI runs to 100, no freeze
TC renamed CI (Church Influence). Range 0–100. No freeze at any threshold.

## Decision 2: TC → CI rename
Theocracy Counter is now Church Influence (CI).

## Decision 3: Seizure available from CI ≥ 60
Church may attempt territorial seizure when CI ≥ 60.

**UPDATE 2026-04-19 (v2):** Declaration is probabilistic, not automatic. Mass Seizure is a civil-war-grade action; Church institutional restraint models via exponential curve P(declare) = ((CI−60)/40)^3.3 per season. 1% at CI 70, 10% at CI 80, 39% at CI 90, 100% at CI 100. Exponential (not linear) shape reflects that institutional restraint dominates early CI range and only breaks down near ceiling. See victory_v30 §3.2.
**SUPERSESSION NOTE:** Commit 250715f (engine v3 fix) raised threshold to CI ≥ 75. That correction is itself superseded — threshold stays at 60, with probabilistic declaration curve handling the institutional-restraint intent.

## Decision 4: Seizure Ob = 10 − PT − infrastructure modifiers
Base Ob = 10 − PT. Infrastructure: Chapel −1, Church −2, Cathedral −3, Inquisitor −1, Templar −1.
Ob floor: 1.

## Decision 5: TCV → PV (Provincial Value). Not used in victory.
PV measures political power. Never used in victory calculations.
Cathedral City (T9): 5. National capital (T1): 5. Duchy capitals (T8, T12): 4.
Fortresses/Lowenskyst/Ehrenfeld (T3, T14): 3. Remaining: TBD.

## Decision 6: One-time seizure
Church seizure is a one-time event. One shot.

## Decision 7: Victory = control peninsula
All factions eliminated or submitted. No PV thresholds. No faction-specific paths.
CI is a tool, not a win condition. Applies equally to all factions.
