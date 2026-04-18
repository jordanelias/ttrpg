# SIM-004 — Personal Combat Full Ranged Test Suite
## Date: 2026-04-02
## Modes: A (isolation), C (full scenario), D (edge cases), J (cognitive load)
## Patches: PP-174

Test ID: SIM-004
Mechanics: PP-172 ranged subtypes + PP-165 pool/health | Mode: TTRPG | Temporal: PRES
Tracks: Combat Pool, Health, Wounds, Stamina | Factions: All | NPCs: Generic
Archetypes: Archer (LP), Crossbowman (HP), Stone Slinger (LBl), Lead Slinger (HBl), Melee Fighter (HC), Heavy Knight

---

## Mode A: Expected Damage Matrix (design-doc formula: net_hits + mod − DR, no STR)

No defence. Ob not applied (uncontested ranged fire).

| Weapon | Pool | TN | Mod | vs None | vs Light | vs Med | vs Heavy |
|--------|------|----|-----|---------|----------|--------|----------|
| LP | 13 | 6 | +2 | 7.2 | 5.2 | 4.2 | 2.2 |
| HP | 11 | 5 | +4 | 9.5 | 8.5 | 7.5 | 6.5 |
| LBl | 12 | 7 | +1 | 4.6 | 3.6 | 2.6 | 1.6 |
| HBl | 12 | 8 | +3 | 5.4 | 5.4 | 4.4 | 3.4 |

With Dodge (full pool TN7):

| Weapon | vs None | vs Light | vs Med | vs Heavy |
|--------|---------|----------|--------|----------|
| LP | 3.3 | 1.3 | 0.3 | 0 |
| HP | 6.2 | 5.2 | 4.2 | 3.2 |
| LBl | 1.0 | 0 | 0 | 0 |
| HBl | 3.0 | 3.0 | 2.0 | 1.0 |

---

## Mode C: Full Scenarios

**Scenario 1:** LP+LBl pair vs Heavy Knight. Open ground (1 round to close).
- LP vs Heavy (DR5): E[dmg] = 2.2. LBl vs Heavy (DR3): E[dmg] = 1.6. Combined = 3.8.
- Knight Health (Endurance 4) = 10. Wound in ~2.6 rounds at 3.8/round.
- LP+HBl pair: 2.2 + 3.4 = 5.6/round. Wound in ~1.8 rounds.

**Scenario 2:** LP vs Light Infantry — cover vs dodge.
- No cover: 5.2. Soft cover (+2DR): 3.2. Dodge (10D): 2.2.
- Cover and Dodge roughly equivalent; both meaningful tactical choices.

**Scenario 3:** HP Crossbowman vs Heavy Knight — reload cycle.
- Round 1: E[dmg] 6.5. Round 2: Reload (0). Round 3: E[dmg] 6.5.
- Round 4: Knight at Close zone. Knight attacks (12D TN7 vs 11D TN8 defence): E[dmg to crossbowman] = 4.4.
- Total damage dealt (2 shots): 13.0. Knight Health (Endurance 4) = 10 → wound already taken after shot 1.
- Finding: Crossbowman is extremely effective over 2 shots but MUST avoid Close zone.

**Scenario 4:** HBl Slinger vs Heavy Knight.
- E[dmg/round] = 3.4. Only 1 round before knight closes on open ground.
- Slinger draws knife: E[dmg vs Heavy armour] = 0. Must have terrain.

**Scenario 5:** LP vs LP mirror. Both at E[5.2−5.2 = 0] wait — both fire, no defence.
- LP1 (light armour DR2 vs LP): E[dmg] = 5.2. LP2 same. Mutual devastation.
- Wound per ~1.7 rounds each. Both incapacitated within 3-4 rounds. No-defence mirrors are lethal.

---

## Mode D: Edge Cases

- EDGE 1: HP vs unarmoured. E[dmg] = 9.5. Wound in <1 round. Historically correct.
- EDGE 2: HBl vs heavy armour + cover (DR4 total). E[dmg] = 1.4. Neutralised.
- EDGE 3: Min pool (5D) LP. E[dmg] vs unarmoured = 4.0. Still dangerous.
- EDGE 4: LBl vs light armour + Dodge. E[dmg] = 0. Dodge fully negates LBl.
- EDGE 5: HP vs LP mirror over 3 rounds. HP: 17.0 total. LP: 18.6 total. LP wins (fire rate).
- EDGE 6: Group ranged — Fibonacci ambiguity flagged (ED-093).

---

## Mode J: Cognitive Load
Load score: ~7/10 (PROBLEM). Mitigated to ~5/10 with weapon reference card.
Time: 2.5m novice / 1.0m experienced / 0.3m expert.
Flag: P2 — reference card required for first-time ranged users.

---

## Findings

| ID | Sev | Description | Resolution |
|----|-----|-------------|------------|
| F1 | P1 | "No personal HBl" line in params_combat contradicts PP-172 | PP-174 applied |
| F2 | P1 | STR in params damage formula not in design doc | PP-174 provisional (ED-092) |
| F3 | editorial | Fibonacci applicability to ranged group attacks | ED-093 provisional |
| F4 | P2 | Cognitive load: reference card required | Design note (existing SIM-001 note) |
| F5 | confirmed | HP reload cycle creates meaningful LP vs HP trade-off | No patch — working as intended |
| F6 | confirmed | HBl anti-armour role validated vs personal combat targets | No patch |
