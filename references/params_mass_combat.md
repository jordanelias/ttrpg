<!-- version: v0.14+design | sources: stage8_combat.md, designs/mass_combat/mass_battle_v3.md | last_updated: 2026-03-30 -->
<!-- STALE CHECK: mass_battle_v3.md is a design proposal, not yet compiled. Parameters marked [PROPOSAL] are from v3 design only. -->
<!-- STALE CHECK: If compiled ruleset version ≠ v0.14, halt and flag before using [COMPILED] values. -->

# params_mass_combat.md — Mass Battle

## Unit Stat Block (all 1–7 unless noted)
| Stat | Description |
|------|-------------|
| Strength | Headcount / health pool. At 0: destroyed. |
| Combat Power (CP) | Dice pool ceiling. |
| Cohesion | Organisational integrity (1–7). |
| Morale | Rout threshold (1–7). |
| Speed | Slow / Standard / Fast |

Effective Combat Pool = min(CP, current Strength)

## CP Tier Reference [PROPOSAL — mass_battle_v3.md]
| CP | Tier |
|----|------|
| 1 | Levy |
| 2 | Militia |
| 3 | Professional |
| 4 | Veteran |
| 5 | Elite |
| 6–7 | Exceptional/Peerless |

## Faction Military → Unit Quality [PROPOSAL]
| Military | Max CP | Starting Cohesion ceiling |
|----------|--------|--------------------------|
| 1 | 1 | 2 |
| 2 | 2 | 3 |
| 3 | 3 | 4 |
| 4 | 4 | 5 |
| 5 | 5 | 6 |
| 6 | 6 | 7 |
| 7 | 7 | 7 |

## Command Rating (CR) [PROPOSAL]
CR = ⌈(Presence + Cognition) ÷ 2⌉
Governs: sub-unit limit (max = CR; TTRPG hard cap 3), Cohesion ceiling, Morale floor (=1 while general present), tactic execution.

## Cohesion Degradation (Deterministic) [PROPOSAL]
Fires at Phase 5 when total Strength lost this turn > Cohesion rating: Cohesion −1.
| Cohesion | Effective CP penalty |
|----------|---------------------|
| 5–7 | None |
| 3–4 | −1D |
| 1–2 | −2D |
| 0 | Formation broken; cannot attack; must Reform or rout |

Cohesion restoration: Reform Phase only (not engaged), +1 Cohesion, requires CR ≥ current Cohesion + 1.

## Morale Degradation Triggers [PROPOSAL]
| Trigger | Morale change |
|---------|--------------|
| Str < 50% of max | −1 |
| Str < 25% of max | −1 additional |
| Cohesion broken this turn | −1 |
| Allied unit routed in same zone | −1 |
| General incapacitated (Stage 1) | −1 |
| General killed (Stage 2) | −2 (not subject to cap) |
| Flanked and lost exchange | −1 |
| Idle 2+ consecutive turns | −1 |

Cap: −3 per Cascade Phase (Stage 2 general death is separate).
Floor: 1 while general present. At 0: unit routs.
Rout contagion: −1 Morale to adjacent units; secondary loss cannot cascade to rout until next turn.

## Weapon Effectiveness vs Armour [COMPILED — inherits personal combat]
| Attacker | vs None | vs Light | vs Medium | vs Heavy |
|----------|---------|----------|-----------|---------|
| LightCut | ✓ | ✗ | ✗ | ✗ |
| HeavyCut | ✓✓ | ✓✓ | ✓ | ✗ |
| LightBlunt | ✓ | ✗ | ✗ | ✗ |
| HeavyBlunt | ✓✓ | ✓✓ | ✓✓ | ✓✓ |
| Projectile | ✓ | ✗ | ✗ | ✗ |

(HeavyBlunt is the only weapon class effective against Heavy armour.)

## DR Table (adds Projectile column vs compiled table) [PROPOSAL]
| Armour | LC | HC | LB | HB | Projectile |
|--------|----|----|----|----|-----------|
| None | 0 | 0 | 0 | 0 | 0 |
| Light | 2 | 1 | 1 | 0 | 2 |
| Medium | 4 | 3 | 2 | 1 | 4 |
| Heavy | 6 | 5 | 3 | 1 | 6 |

## Battle Scale [PROPOSAL]
| Scale | 1 Strength ≈ | Thread TS minimum |
|-------|-------------|-------------------|
| Skirmish | ~10 soldiers | Personal (30+) |
| Company | ~100 soldiers | Object (30+) |
| Battle | ~500 soldiers | Territorial (50+) |
| Campaign | ~1,000 soldiers | Territorial (50+) |
| War | ~5,000 soldiers | Structural (70+) |

## Thread Integration [COMPILED — stage11_scale_transitions.md]
Combat Thread ops (Dissolution, offensive Pulling): Phase 2 (before Engagement), declared Phase 1.
Support Thread ops (Weave, Mend, Lock, non-offensive Pulling): Phase 5 (Cascade), declared Phase 1.
