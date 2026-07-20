<!-- INFILL — prose/rationale extracted from victory_v30.md -->
<!-- Skeleton: victory_v30.md -->

# VALORIA BG — Victory Architecture
## ED-306 Resolution (v3 — geography_design.md territory numbering, TC 75 canonical, PT cap clarified)
## PP-540–546 (2026-04-10): Balance patches — solo + co-victory timeline normalisation
## Date: 2026-04-06 | Status: DESIGN — pending Varfell Path B user decision (ED-311)
## Supersedes: v2 (same path), params_board_game.md §Victory Conditions, all Deed-based victory systems
## Dependencies: ED-302 (PT confirmed), ED-303 (TC freeze at 75), ED-304 (Partition Victory), ED-305 (WA=0), ED-307 (Baralta cadet branch), BALANCE-001 (equal win probability), BALANCE-004 (Askeheim purpose)
## Territory numbering: geography_design.md canonical (all T-numbers match geography_design.md)
## Core Frame
Victory = Territory Held + Faction-Specific Political Conditions, sustained for 2 consecutive Accounting steps.
## 1. Territory Consolidation Values (TCV)
Every territory has a fixed strategic weight. TCV is the universal measure of territorial dominance.
## 2. Piety Track (PT)
Starting values, movement rules, Calamity Drift, and Consecrated status per opus_design_proposal.md §1.1–1.4.
- Community Weaving is a Thread operation: follows standard Thread procedure including Co-Movement card draw. PT −1 is the primary effect; temporal/epistemic/actual auto-effects fire per P-01.
## 3. Victory Conditions — All Factions
Every victory requires holding all conditions for **2 consecutive Accounting steps**. A faction knocked out between steps resets its counter.
### 3.1 Crown — Peninsula Sovereignty
#### Alternate — Dominion
### 3.2 Church of Solmund — Solmundan Orthodoxy
[EDITORIAL: ED-355 — resolved provisionally. Option (b): Battle handles Fort, Seizure is political. Flagged for simulation.]
#### Alternate — Altonian Theocracy Path
#### Partition — Church + Hafenmark (ED-304)
**Non-winner outcome (ED-339):** Crown, Varfell, and RM score no victory under Partition — the negotiated partition forecloses all other victory paths. This is by design: Partition is bilateral and terminal.
**Outcome:** Mutual agreement ends the game. Both factions score a conditional victory. No holding requirement — fires immediately on mutual declaration.
### 3.3 Hafenmark — Parliamentary Sovereignty
#### Alternate — Dynastic Assertion (ED-307)
### 3.4 Varfell — Vaynard's Three Paths
#### Path A — Intelligence Hegemony
#### Path B — Southernmost Dominion
#### Path C — Thread Supremacy
### 3.5 Restoration Movement — Cultural Revolution (5 players only, hardest mode)
RM has no faction stats. It operates purely through Presence markers and Community Weaving. It cannot hold territory, raise armies, or act in any domain that requires a faction stat. It cannot be targeted by Royal Decree, Excommunicate, or Suppress. Its only vulnerability is PT reversal (Church Piety Spread) and Inquisitor disruption of Weaving.
#### Phase 1 — Cultural Majority (threshold to unlock Phase 2)
#### Phase 2 — Cultural Uprising of T9 Himmelenger
#### RM Territory Control — Cultural Displacement
RM "hold" is functionally different from faction territorial control: RM does not collect TCV from T9, does not gain Domain Action slots from it, and cannot use it as a staging area for military operations. RM's T9 control provides only: (a) the victory condition check, (b) blocking Church Piety Spread in T9, and (c) narrative authority over T9's institutional character.
### 3.6 Löwenritter — Military Regency (conditional faction, post-coup)
#### Primary — Regency Establishment
#### Alternate — Military Consolidation
## 4. Co-Victory Pairings
Co-victories require 2 consecutive Accounting steps except Partition (immediate on mutual agreement).
## 5. Shared Loss Conditions
## 6. Askeheim and RS (BALANCE-004)
WC and WR are distinct tracks. WC advances through any faction's Expedition engagement. WR advances only through Varfell's Expedition actions.
## 7. TC Generation and Church Seizure
## 8. RM Emergence
## 9. Hybrid Mode Integration
### 9.1 PT State Transfer
### 9.2 Victory Condition Check — Hybrid
Victory condition checks (all factions) fire at Accounting Step 12 regardless of active Zoom In. A Zoom In cannot delay or prevent a victory declaration. The 2-Accounting holding requirement is assessed across consecutive Accounting steps — a Zoom In spanning an Accounting boundary counts that Accounting.
### 9.3 Hybrid Victory and P-32
### 9.4 Domain Echo Autonomous Resolution (ED-300)
Autonomous TCV changes from uninvestigated Domain Echoes count toward or against victory conditions. The 2-Accounting holding requirement does not exempt autonomous changes.
## 10. Win Probability Assessment
[SIM-DEBT: Full faction-AI simulation needed to validate non-military acquisition paths, fortification effects, multi-faction interaction dynamics. Flag as P1.]
## 11. Open Editorial Items
## 12. Patch Register
## 5. Total Domination (ED-318 RESOLVED, 2026-04-07)
## 6. Notes on Spoiler Dynamics (SIM-SPOILER-BG-01 + SIM-SPOILER-HY-01, 2026-04-07)
- Church Prominence tracker: [EDITORIAL: ED-326 — recommend tracker on Church mat for Counter-Narrative eligibility.]
## PP-478 Override — §3.5 Restoration Movement
### RM Mode Applicability
- **Hybrid mode:** RM solo victory and co-victories are available ONLY after RM Founding (see params_board_game.md §RM Founding Mechanic).
### RM Solo Victory (Hybrid mode, post-Founding)
### §4 Co-Victory Override (PP-478)
### §8 RM Emergence Override (PP-478)
