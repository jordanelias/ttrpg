# SIM-001 — Ranged Weapon Subtypes (LP/HP/LBl/HBl)
## Date: 2026-04-02
## Modes: A (isolation), C (full scenario), D (edge cases), J (cognitive load), L (precedent)
## Patch: PP-172

Test ID: SIM-001
Mechanics: PP-172 ranged subtypes, PP-105 ranged zone rules | Mode: TTRPG | Temporal: PRES
Tracks: Combat Pool, Wounds, Stamina | Factions: All (weapon availability) | NPCs: Generic
Archetypes: Archer (LP), Crossbowman (HP), Slinger LBl, Slinger HBl, Melee Fighter

---

## Mode A — Isolation: Expected Damage by Weapon Type and Armour Tier

Pool 6D, Ob1, no Defence roll (Far zone, no Dodge action).

| Weapon | TN | Mod | vs None | vs Light | vs Medium | vs Heavy |
|--------|----|-----|---------|----------|-----------|----------|
| LP | 6 | +2 | 3.4 | 1.4 | 0.4 | 0 |
| HP | 5 | +4 | 6.0 | 5.0 | 4.0 | 3.0 |
| LBl | 7 | +1 | 1.8 | 0.8 | 0 | 0 |
| HBl | 8 | +3 | 3.2 | 3.2 | 2.2 | 1.2 |

With Dodge (6D TN7 passive defence):

| Weapon | vs None | vs Light | vs Medium | vs Heavy |
|--------|---------|----------|-----------|----------|
| LP | 2.0 | 0 | 0 | 0 |
| HP | 4.2 | 3.2 | 2.2 | 1.2 |
| LBl | 1.0 | 0 | 0 | 0 |
| HBl | 3.0 | 3.0 | 2.0 | 1.0 |

---

## Mode C — Test Battles

### Battle 1: LP Archer (13D) vs Unarmoured Fighter (Open Ground)
- Round 1: Archer fires. E[damage] = 6.2. Fighter closes (Agility 7D TN7, E[net] = 1.1).
- Finding: LP dominant on open ground vs unarmoured. Environmental protection required for balance.

### Battle 2: HP Crossbowman (11D) vs Heavy Armour Knight
- Round 1: E[damage] = 5.5. Round 2: Reload (no attack). Round 3: E[damage] = 5.5.
- Round 4: Knight at Close zone. Crossbowman defends TN8 (11D → E[def] = 2.2).
- Knight (10D HC) E[damage through ranged defence] = 3.8.
- Finding: Crossbowman must avoid Close zone. Reload cycle creates 1-round vulnerability window.

### Battle 3: LBl Slinger (11D) vs Medium Armour
- E[damage] = 1.3. Effectively 0 useful damage.
- Finding: LBl is anti-personnel only. Matches historical record.

### Battle 4: HBl Slinger (11D) vs Heavy Armour — KEY
- E[damage vs Heavy] = 2.2. Compare LP vs Heavy = 0.4.
- HBl is 5× more effective than LP vs heavy armour.
- Finding: Meaningful weapon differentiation confirmed. HBl is the anti-armour ranged option.

### Battle 5: Environmental — LP Archer at River Crossing
- Fighter crosses (3 rounds, −2D while crossing).
- Round 1 E[damage] = 5.4. Round 2 E[damage] = 5.4. Round 3: Fighter arrives.
- Total exposure damage ≈ 10.8 expected — lethal without cover.
- Finding: River crossing under ranged fire is extremely dangerous. Terrain table is load-bearing for balance.

### Battle 6: Ranged Defence TN8
- Crossbowman 11D TN8: E[def] = 2.2 vs Knight 10D TN6: E[atk] = 4.0.
- E[damage through ranged defence] = 3.8 vs E[damage through standard melee defence] = 3.0.
- Finding: TN8 ranged defence viable but ~0.8 successes weaker than standard melee defence. Correct.

---

## Mode D — Edge Cases

- EDGE 7.1: Min pool (5D) HBl vs Heavy armour: E[damage] = 1.0. Still outperforms Heavy Cut vs heavy armour.
- EDGE 7.2: LP vs cover (trees, +2 DR): damage 5.4 → 3.4. Cover meaningful but not absolute.
- EDGE 7.3: HBl vs cover (+2 DR) + no armour: damage 4.2 → 2.2. Cover partially mitigates.
- EDGE 7.4: HBl at Close zone: existing sling rule applies. Draw knife (Light Cut). No issue.
- EDGE 7.5: HP reload under pressure: 1-round fire gap every 2 rounds. Enemy closes during reload.
- EDGE 7.6: Pool split at melee range: [EDITORIAL ED-085 raised. Provisional: Offence forbidden.]
- EDGE 7.7: HBl vs Heavy armour + cover (total DR4): E[damage] = 0.2. Near-immune. Correct.

---

## Mode J — Cognitive Load

Decisions: 3 | Lookups: 2–3 | Parallel tracks: 6 | Sequential deps: 3
Raw score: ~8/10 (PROBLEM threshold). Mitigated to ~5/10 with per-weapon reference card.
Flag: P2 — reference card required for first-time ranged users.

---

## Mode L — Precedent

- Burning Wheel Archery: separate skill vs Valoria pool. Simplification justified.
- Pendragon pierce flag: binary vs Valoria matrix. Matrix more expressive, justified.
- No precedent for HBl as distinct type. Novel — carries weight if availability differentiated.

---

## Findings

| ID | Severity | Description | Resolution |
|----|----------|-------------|------------|
| F1 | confirmed | HBl anti-armour profile validated | PP-172 applied |
| F2 | confirmed | Cover DR table balances LP/LBl dominance | PP-172 applied |
| F3 | P2 | Cognitive load: reference card required | Design note added |
| F4 | editorial | Pool split at melee range for ranged weapon | ED-085 provisional |
| F5 | editorial | HBl availability by faction | ED-086 provisional |

---

## Propagation Required (Post-Commit)
- designs/mass_combat/mass_battle_v3.md — add HBl unit type to ranged unit roster section
- references/params_mass_combat.md — add HBl DR row to mass combat ranged table
- designs/board_game/ — BG unit type keyword propagation (Anti-Armour for HBl units)
- references/canonical_sources.yaml — no change (combat still canonical)
