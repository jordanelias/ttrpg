# Simulation Report: SIM-STRESS-01
## Systems: Social Contest, Personal Combat, Mass Battle, Faction Play
## Date: 2026-04-04
## Simulator Modes: A (isolation), D (edge cases), J (precedent), L (cognitive load)
## Model: Sonnet 4.6

---

## FINDINGS

### Social Contest (social_contest_system_v2.md)

| ID | Severity | Description |
|----|----------|-------------|
| F-CS-01 | Design note | Read fail rate ~40–67% for Att 1–3; not a bug; note for compilation |
| F-CS-02 | Medium | Forfeit +1 track movement collapses 3-exchange Formal: 1 win + 1 forfeit = match over at Exchange 2 |
| F-CS-03 | Note | Obscuring/CROSS payoff requires exceeding resistance; player guidance needed |
| F-CS-04 | P2 | CROSS Tie contradiction: CROSS rule says no strain; Tie rule says +1 strain each. Provisional: no strain |
| F-CS-05 | P3 | Mutual Rattled incapacitation unresolved; proposed: stall consequence applies |
| F-CS-06 | P2 | Coalition Lead rotation eliminates Concentration depletion entirely |
| F-CS-07 | Action | params_contest.md missing note that History bonus = points+3 (includes +3 constant) |
| F-CS-08 | Action | GM reference card for 10-step exchange needed |

### Personal Combat (combat_design_v1.md)

| ID | Severity | Description |
|----|----------|-------------|
| F-CMB-01 | Design note | TN 5 dagger near-equalises pool gap vs TN 7; damage differential compensates; intended |
| F-CMB-02 | Design note | Light weapon vs armour: near-zero damage at Str 1; intended |
| F-CMB-03 | Design note | Breath timing creates real tactical decision; working |
| F-CMB-04 | P2 | Feint pool allocation unspecified: "Offence-only roll" — is full pool committed to Offence, leaving 0 Defence? |
| F-CMB-05 | Note | Rescue gamble under simultaneous declaration; intended consequence |
| F-CMB-06 | P2 | Initiative tiebreaker for equal Attunement in Exchange 1 unspecified |
| F-CMB-07 | Note | End 1 locked to Light armour by wield constraint; likely intended |
| F-CMB-08 | Action | Combat reference card needed (weapon TN matrix + damage modifier + ranged DR = 3 table lookups/exchange) |

### Mass Battle (mass_battle_v3.md)

| ID | Severity | Description |
|----|----------|-------------|
| F-MB-01 | Design note | Command double-contribution (min(Size,Command)+Command) is design intent; generalship dominates |
| F-MB-02 | **P1** | TTRPG-mode damage modifier not confirmed; §B.2 Dmg Mod values are BG/provisional only; SIM-DEBT-05 |
| F-MB-03 | Low confidence | Provisional BG Dmg Mod values collapse TTRPG battle to ~1 exchange; likely wrong for TTRPG |
| F-MB-04 | P2 | Mutual total destruction (both sides to 0 simultaneously): no winner rule. Provisional: draw |
| F-MB-05 | Note | Woven unit shatter supersedes Discipline check; redundancy only; no contradiction |
| F-MB-06 | P2 | Reform condition "Command ≥ Discipline+1" allows Command=1 to reform Discipline=0; contradicts explicit prohibition |
| F-MB-07 | Action | Full-turn resolution ~20-35 min with practitioner; reference card mandatory |

### Faction Play (stage6_factions.md)

| ID | Severity | Description |
|----|----------|-------------|
| F-FP-01 | Design note | Domain Action requires leadership bonus to reach plausible success rates; intended |
| F-FP-02 | P2 | Seasonal ±2 cap timing: at-resolution vs at-accounting unspecified. Provisional: at accounting |
| F-FP-03 | P2 | Royal Decree can target non-existent stats on partial-sheet factions; no constraint |
| F-FP-04 | P2 | PC excommunication: no faction succession rule. Provisional: faction reverts to NPC institutional tendency |
| F-FP-05 | P2 | Territorial seizure cascade at Mandate ≤ 2; no anti-cascade floor |
| F-FP-06 | P2 | Domain Action vs Social Contest escalation path undefined |

---

## NEW SIM-DEBT

| ID | Description | Blocks |
|----|-------------|--------|
| SIM-DEBT-05 | Mass battle TTRPG damage modifiers unconfirmed. F-MB-02. | TTRPG mass battle simulation |

---

## PROVISIONAL RULINGS

| # | Ruling | Rationale |
|---|--------|-----------|
| 1 | CROSS Tie: no strain; track +1 toward initiative holder | CROSS no-strain reflects neither argument attacked the other; tie doesn't change that |
| 2 | Mutual total destruction: draw; no territory change; both Stability check Ob 1 | Analogous to combat mutual destruction (Pyrrhic outcome) |
| 3 | Reform condition: add "AND Command ≥ 2" | Explicit prohibition takes precedence over formula |
| 4 | Seasonal stat cap: applied at accounting, not per-action | Institutional momentum doesn't reverse between actions within a season |
| 5 | Royal Decree partial-sheet: may only target stats on target's sheet | Non-existent stats cannot be changed |
| 6 | PC excommunication: faction reverts to NPC institutional tendency | Faction cannot operate leaderless |

---

## ACTIONS (no editorial approval required)

1. Add to params_contest.md: "History bonus = history points + 3 (per Stage 2 §4.1). Pool formula equivalent to combat pool."
2. Flag GM Tools: social contest 10-step exchange reference card needed.
3. Flag GM Tools: combat 3-table reference card needed.
4. Flag GM Tools: mass battle phase-order + simultaneous damage deferral reference card needed.
5. Log SIM-DEBT-05 in coverage_matrix.md.
