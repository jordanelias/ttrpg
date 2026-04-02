<!-- version: v0.14+design-ST | sources: stage8_combat.md, mass_battle_v3.md | last_updated: 2026-04-02 -->
<!-- PATCHES APPLIED: PP-086-088, PP-091-092; ST-MB-01–10 applied to mass_battle_v3.md -->
<!-- mass_battle_v3.md is a design proposal. Values marked [COMPILED] are from stage8; [PROPOSAL] from v3. -->
<!-- STALE CHECK: Verify [COMPILED] values against current ruleset; verify [PROPOSAL] against compiled stage8 update. -->

# params_mass_combat.md — Mass Battle (v3)

## Core Formula
Effective Combat Pool = min(CP, current Strength)
As Strength drops: fewer dice regardless of quality. CP is ceiling; Strength determines reach.

## Unit Stats (1–7 unless noted)
| Stat | Description |
|------|-------------|
| Strength | Headcount/health pool. At 0: destroyed. |
| Combat Power (CP) | Dice pool ceiling. |
| Cohesion | Organisational integrity (1–7). |
| Morale | Rout threshold (1–7). |
| Speed | Slow / Standard / Fast |
| Weapon Type | Inherits personal combat table [COMPILED] |
| Armour Tier | Inherits personal combat DR table [COMPILED] |

## CP Tier Reference [PROPOSAL]
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
Governs: sub-unit limit (max = CR; TTRPG hard cap 3); Cohesion ceiling; Morale floor (= 1 while general present); tactic execution (CR dice vs Ob).
CR = 1: cannot restore Cohesion to any unit — all degradation permanent for that battle.

## Battle Phases (TTRPG)
1. Declaration
2. Volley (projectiles + Combat Thread ops)
3. Charge/Manoeuvre
4. Engagement (melee pool-split resolution)
5. Cascade (support Thread ops, Morale checks, Cohesion checks)
Reform Phase: between turns; unit not engaged.

## Cohesion Degradation (Deterministic) [PROPOSAL]
Fires at Phase 5 when total Strength lost this turn > Cohesion rating → Cohesion −1.
| Cohesion | CP penalty |
|----------|-----------|
| 5–7 | None |
| 3–4 | −1D |
| 1–2 | −2D |
| 0 | Formation broken; cannot attack; Reform or rout |

Restoration: Reform Phase only (not engaged), +1 Cohesion, CR ≥ current Cohesion + 1.

## Morale Degradation Triggers [PROPOSAL]
| Trigger | Change |
|---------|--------|
| Str < 50% max | −1 |
| Str < 25% max | −1 additional |
| Cohesion broken this turn | −1 |
| Allied unit routed in same zone | −1 |
| General incapacitated (Stage 1) | −1 |
| General killed (Stage 2) | −2 (not subject to phase cap) |
| Flanked and lost exchange | −1 |
| Idle 2+ consecutive turns | −1 |

Cap: −3 per Cascade Phase (Stage 2 death separate and uncapped).
Floor: 1 while general present. At 0: rout.
Rout contagion: −1 Morale to adjacent units; secondary loss cannot cascade to rout until next turn.

## DR Table — Mass Combat (adds Projectile column) [PROPOSAL]
| Armour | LC | HC | LB | HB | Projectile |
|--------|----|----|----|----|-----------|
| None | 0 | 0 | 0 | 0 | 0 |
| Light | 2 | 1 | 1 | 0 | 2 |
| Medium | 4 | 3 | 2 | 1 | 4 |
| Heavy | 6 | 5 | 3 | 1 | 6 |

Weapon Effectiveness:
| Attacker | vs None | vs Light | vs Medium | vs Heavy |
|----------|---------|----------|-----------|---------|
| LightCut | ✓ | ✗ | ✗ | ✗ |
| HeavyCut | ✓✓ | ✓✓ | ✓ | ✗ |
| LightBlunt | ✓ | ✗ | ✗ | ✗ |
| HeavyBlunt | ✓✓ | ✓✓ | ✓✓ | ✓✓ |
| Projectile | ✓ | ✗ | ✗ | ✗ |

HeavyBlunt is the only weapon class effective vs Heavy armour.

## Battle Scale [PROPOSAL]
| Scale | 1 Strength ≈ | Thread TS minimum |
|-------|-------------|-------------------|
| Skirmish | ~10 soldiers | 30+ |
| Company | ~100 soldiers | 30+ |
| Battle | ~500 soldiers | 50+ |
| Campaign | ~1,000 soldiers | 50+ |
| War | ~5,000 soldiers | 70+ |

## Thread Integration [COMPILED — stage11]
Combat Thread ops (Dissolution, offensive Pulling): Phase 2. Support ops (Weave, Mend, Lock, non-offensive Pulling): Phase 5. Both declared Phase 1.
Mass → Personal: Personal Action available at Phase 5 (Priority 8). Limit: 1 exchange/battle turn. General's Phase 5 consumed by personal combat (CR suspended).

## Key Design Axiom
Generalship dominates. CR asymmetry is intentional. CR=7 vs CR=1 general: near-certain outcome before dice rolled.

## PATCH SUMMARY (ST-MB series, applied to mass_battle_v3.md on 2026-04-02)

### ST-MB-03 — Effective CP Timing
Effective CP calculated at Phase 3 end. All Phase 4 damage simultaneous at Phase 5 Step 1.
CP does not change within Phase 4.

### ST-MB-04 — Morale Cap + General Kill Order
Apply non-general Morale changes first (cap −3), then Stage 2 general death −2 separately.
Maximum total Morale loss per Cascade Phase: −5.

### ST-MB-05 — CR=0 Uncommanded
All units at Line formation, Cohesion floor 1, no tactics. Morale floor suspended.

### ST-MB-06 — Reserve Timing
Commit at Phase 3 Turn N+1 → available for Phase 4 that same turn.

### ST-MB-07 — Shield Wall Three-Sided
Negates one declared flank. Front + opposite flank both apply normally.

### ST-MB-08 — Feigned Retreat Recognition
Roll CR dice (d10s equal to CR score) vs Ob 2 to recognise feint.

### ST-MB-09 — Mixed TS Forces in Southernmost
Reduce Strength proportionally to TS-capable fraction. Only Restoration+Varfell VTM≥2 viable.

### ST-MB-10 — Woven Unit Shifting Object
Shattered Woven unit fights at Line/Cohesion 1 for battle; Shifting Object status registers post-battle only.

### ST-INT-06 — BG Unit TS (Southernmost)
Church Templar: TS=0. Restoration with Weaver marker: TS=30. Varfell VTM≥2: TS=30.
All others: TS=0 (cannot operate in Southernmost).

### ST-INT-09 — Military Loss Timing
TTRPG: immediate. BG: queues to Accounting. Hybrid: TTRPG timing during battle.

## PENDING EDITORIALS
- ED-033: Commander bonus formula (P1)
- ED-037: Volley TN — TN 6 vs TN 7 (P1) [EDITORIAL blocking params update for Volley]
- ED-038: Coherence stat definition (P1)
- ED-039: Military seasonal cap pooling (P2)
- ED-036: Altonian unit stats BLOCKER
