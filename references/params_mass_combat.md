<!-- version: v0.14+design-ST3 | sources: stage8_combat.md, mass_battle_v3.md | last_updated: 2026-04-02 -->
<!-- PATCHES APPLIED: PP-086-088, PP-091-092; ST-MB-01–10; ED-037/038; Altonian provisional; ED-050 Option D -->
<!-- PHASE STRUCTURE: 7 phases. Thread split: offensive Phase 4, support Phase 6. All damage simultaneous Phase 6 Step 1. -->
<!-- mass_battle_v3.md is a design proposal. Values marked [COMPILED] are from stage8; [PROPOSAL] from v3. -->
<!-- STALE CHECK: Verify [COMPILED] values against current ruleset; verify [PROPOSAL] against compiled stage8 update. -->

# params_mass_combat.md — Mass Battle (v3)


## BATTLE TURN PHASE STRUCTURE (7 phases, revised 2026-04-02)

| Phase | Name | Content |
|-------|------|---------|
| 1 | Strategy Declaration | Formations, tactics, Thread intent declared (simultaneous, secret) |
| 2 | Volley | Projectile fire. Damage recorded, not applied. TN 6 [PROVISIONAL]. |
| 3 | Manoeuvre | Movement by speed. Reserve commitments. |
| 4 | Offensive Thread | Dissolution, Pulling, Locking. Practitioner-only. Skipped if no practitioner present. BG: always skipped. |
| 5 | Engagement | Pool split, roll, damage recorded. Max 3 simultaneous (TTRPG). |
| 6 | Cascade | Step 1: ALL damage applied simultaneously (Volley+Thread+Engagement). Step 2: Cohesion checks. Step 3: Morale checks. Step 4: General action (Rally/Support Thread/Personal combat). Step 5: Support Thread Leap resolves. |
| 7 | Reform | Cohesion restore, Morale +1, sub-unit merge for non-engaged units. |

Damage simultaneity: Effective CP for Phase 5 calculated from Str as of Phase 3 end. Phase 4 Thread effects do not reduce Str before Phase 5 — all applied together at Phase 6 Step 1.

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

<!-- patch_history: references/params_mass_combat_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->
