<!-- version: v0.14+design-ST | source: bg_v05_simulation_and_patches.md | last_updated: 2026-04-02 -->
<!-- PATCHES APPLIED: P-12–P-32 (prior); ST-BG-01–10, ST-INT-01,05,06,07,08,09,10,12,13 added 2026-04-02 -->
<!-- NOTE: stage6_factions.md is STALE for BG mode. bg_v05 is canonical for all BG faction mechanics. -->
<!-- STALE CHECK: BG editorial blockers pending (BG-E-30 card-hand adoption). See canon/editorial_ledger.yaml. -->

# params_board_game.md — Board Game Mode (v0.5)

## Dice System
d10 pool. Same engine as TTRPG.
| Face | Effect |
|------|--------|
| 1 | −1 success |
| 2–6 | 0 |
| 7–9 | +1 success |
| 10 | +2 successes |

Majority-1s override (P-12): more 1s than 7-10s → Catastrophic Failure (Failure + one additional consequence: −1 Standing, −1 Stability, or stat degradation).
Ob minimum = 1 (P, Correction 2). No modifier may push Ob below 1.

## Degree Table
| Net | Degree |
|-----|--------|
| Ob + 1 or more | Overwhelming |
| = Ob | Success |
| Ob − 1 | Partial |
| 0 | Failure |
| Negative | Failure (Catastrophic if majority-1s also fires) |

## Standard Action Ob Reference (P-21)
| Action | Default Ob | Key Modifiers |
|--------|-----------|---------------|
| Muster (Legionary Inward) | 2 | −1 T2, −1 T11 |
| March (Legionary Outward) | 2 | +1 T8 (terrain) |
| Govern (Consul Inward) | 2 | −1 own capital; −1 with Architectus |
| Trade (Consul Outward) | 2 | +1 IP≥30; +1 T10 |
| Diplomacy (Senator Outward) | 2 | −1 Diplomat card; −1 own territory; +1 Standing≥3 vs target |
| Decree (Senator Inward) | 2 | +1 non-home territory; −1 capital |
| Parliamentary Manoeuvre | 2 | +1 PI≤2; −1 PI≥7 |
| Investigate (Tribune Inward) | 2 | −1 own territory; +1 Niflhel-active |
| Spy (Tribune Outward) | 2 | +1 heavily fortified |
| Thread Operation | 2 | −1 per Restoration Presence marker; see Thread procedure |
| Community Organising | 2 | — |
| Community Project start | 1 | — |
| Community Project advance | 2 | — |
| Fortify | 2 | — |
| Forgetting Check | 1 | −1 Restoration Weaver present; −1 VTM 2+ |

All Obs: floor 1.

## Faction Starting Stats
| Faction | Mandate | Influence | Wealth | Military | Intel | Stability | Notes |
|---------|---------|-----------|--------|----------|-------|-----------|-------|
| Crown | 5 | 5 | 4 | 4 | — | 4 | |
| Church | 5 | 6 | 5 | 4 | — | 5 | Starting TC: 28 (P-32) |
| Hafenmark | 4 | 4 | 5 | 3 | — | 4 | |
| Varfell | 3 | 4 | 3 | 4 | — | 4 | BG-specific (Mandate/Wealth 3, not TTRPG 4) |
| Restoration | 2 | 4 | 2 | 0 | — | 3 | 5-player only |
| Löwenritter | 3 | 2 | — | 6 | — | 4 | No Wealth; enters at coup trigger |
| Niflhel | — | 5 | 4 | — | — | 4 | |
| Schoenland | — | — | — | — | — | — | Spoiler only; not playable |

Total point comparison: Church 25, Crown 22, Hafenmark 20, Löwenritter 19, Varfell 18, Restoration 11.
Asymmetry is mechanically compensated by faction-specific mechanics.

## Clock Starting Values and Targets
| Clock | Start | Shared Loss | Win Threshold |
|-------|-------|-------------|---------------|
| TC (Theocracy) | 28 (P-32) | — | 65 = Church Holy State (P-32) |
| RS (Rendering Stability) | 72 | RS = 0 | — |
| IP (Invasion Pressure) | 20 | — | 80 = Vanguard (AER 3); 75 standard |
| PI (Parliamentary Integrity) | 5 | — | — |

## IP Advancement Formula (P-28)
IP has NO automatic per-season advance. Event-driven only.
| Condition | IP Change |
|-----------|-----------|
| Base per season | 0 |
| TC > 60 | +1/season |
| Altonian Trade Mission refused (IP 30 event) | +1 |
| Torben sent to Altonia | −3/season; +5 immediately on compliance |
| Torben refuses (Crown refuses at IP 40) | +3 immediately |
| Elske returns to Valoria | +5 immediately |
| Schoenland Proxy Arms Deal active (IP 45) | +2 this season |
| Crown Free Trade Decree | −1 |
| AER ≥ 4 | IP cannot advance above 60 |
| AER = 5 | IP fixed at 50 |
| Grand Diplomatic Scene milestone | −5 immediately |
| Military success vs Altonian interest | −2 |
| Altonian Vanguard repelled | −5 |

## TC Advancement (key sources)
| Source | TC Change |
|--------|-----------|
| T3 control (base) | +1/season |
| Church Assert (mandatory at TC > 50) | +1/season |
| Heresy Investigation confirmed | +0.5 |
| Templar deployment | varies |
| TC 80 Seizure success (per territory) | +2 |
| Hafenmark Baralta suppression (Mandate ≥ 4) | −1/season |
| Grand Debate challenging Church authority | −2 (Overwhelming) |
| Reformed Settlement (Church Resists) | +3 |
| Starting value (P-32) | 28 |

## Cascade Depth Cap
Maximum 3 immediate mechanical effects per card play resolution step.
Clock changes (RS, TC, IP, PI) count against the cap (P-29).
Excess effects queue to Accounting Phase 5 Step 8.
Prevents mid-Phase victory declarations and threshold crossings.

## Faction Collapse (P-15)
On Stability = 0: (1) Mandate → 0 immediately. (2) All other stats freeze. (3) Collapse state for up to 2 seasons.

## Battle Resolution (P-16)
Both sides roll simultaneously. Compare net successes.
- Attacker net > Defender net: Attacker wins. Effective surplus = (A net − D net) vs Ob.
- Defender net > Attacker net: Defender wins. Attacker Partial or Failure.
- Equal nets: Stalemate. Both Cohesion −1. No territorial change.

## Prosperity (P-22)
Territory-level track (0–5). Not a faction stat.
Govern Success: Prosperity +1 in territory. Govern Failure: −1.
At Year-End Accounting: Prosperity ≥ 3 → +1 Wealth to controlling faction. Prosperity ≥ 5 → +2 Wealth.
Prosperity 0–1: Stability check Ob 1 for controlling faction.

Starting Prosperity: T1:4 T2:3 T3:4 T4:2 T5:3 T6:5 T7:4 T8:3 T9:3 T10:2 T11:4 T12:1 T13:1 T14:3 T15:4.

## Fog of War (Hybrid, P-20)
Stats 1–3: Poor. Stats 5–7: Good. Stat = 4: roll 1d6 (NOT d10) — 1–3 Poor, 4–6 Good.

## Forgetting Check (P-26)
| Faction | Pool |
|---------|------|
| Restoration | Influence + 1D per Presence marker in T13 |
| Varfell | VTM level in dice (e.g. VTM 3 = 3d10) |
| Other factions | Wealth ÷ 2 (round up) |
Ob 1 (floor). Thread-qualified presence: may reroll one die once.
Hybrid: PC Spirit + TS÷10 (round down).

## VTM (Varfell Thread Monitoring)
Bootstrapping (P-27): Roll Influence vs Ob 1. Success/Overwhelming: VTM +1. Partial: Latent VTM token (converts on next T9 Tribune Inward within 2 seasons). Failure: no retry.
VTM cap: once per season regardless of source (P-31). Priority: PC spend → Southernmost → Tribune-in-Thread-active → Thread Debt.
Thread-active territory (P-23): territory where a Thread op occurred this season. T9 permanently Thread-active at VTM ≥ 2.

| VTM | Ability |
|-----|---------|
| 1 | Tribune range: any non-adjacent territory |
| 2 | Thread Resonance: while Tribune in thread-active territory |
| 3 | Patience Counter tracks publicly |
| 4 | 4 PC spend → Tribune Outward in any territory regardless of adjacency |
| 5 | Once/game: choose Actualized dimension outcome of one Co-Movement card draw |

## Thread Debt (P-24)
Incurred when operating against temporal flow. Places token in territory.
Effect: +1 Ob to NEXT Thread operation in that territory (not current).

## Casus Belli Expiration (P-14)
| Source | Expiry |
|--------|--------|
| Treaty betrayal | Permanent until used |
| Brutal disposition against civilians | 3 seasons unused |
| Fabricated Heresy Investigation | 3 seasons unused |
| Varfell Patience Protocol | Expires on Riskbreaker exposure |

One CB per faction at a time.

## TC 80 Territorial Seizure
Per-territory roll: Church Mandate vs Ob 3 (contested) or Ob 2 (neutral).
Partial (P-30): Territory not seized; 1 Templar Staging Token placed. Controlling faction can contest at next Military card play.
Overwhelming: Immediate seizure, no Standing cost to Church.
Success: Seizure; TC +2; PI −1.

## Phase 4 Tiebreaking (P-18)
2-way Stability tie: simultaneous. 3+ way Stability tie: player turn order (recorded at game start).
Military-vs-military ties always simultaneous.

## Church Holy State Victory (P-32)
TC ≥ 65 (not 70). Starting TC 28 (not 22).

## Cognitive Load Estimates
| System | Load |
|--------|------|
| Card hand management | 2/10 |
| Degree table | 2/10 |
| Thread Operation (8 steps with card) | 3/10 |
| Co-Movement Cards | 5/10 per draw |
| Faction private tracks | 4/10 per player |
| Phase 4 priority order | 5/10 |
| Klapp Trajectory | 7/10 |
| Phase 5 Accounting (13+ steps) | 8/10 |
| Overall (with reference cards) | 6.5/10 |
| Overall hybrid (with cards) | 8.0/10 |

## PATCH SUMMARY (ST-BG series, applied 2026-04-02)

### PP-033 — Catastrophic Failure Replaces Failure Degree
Catastrophic Failure is a fifth degree that REPLACES Failure. Not additive.

### PP-034 — Drawn Battles
Equal net successes: both sides Cohesion −1, hold position, no territory change.

### PP-035 — Hollow Victory Scope
Hollow Victory applies to Deed-counting factions only (Hafenmark, Guilds).
Restoration (RS-based) and Crown/Löwenritter (mandate-based) are excluded.

### PP-036 — Policy Instrument Definition (Crown)
Crown bonus action at Mandate ≥ 4. Any standard action. Once/season. Not interruptible by Parliamentary Manoeuvre.

### PP-037 — Co-Movement VTM at Cap
VTM effects blocked by once/season cap or VTM max (7): convert to +1D on following season's Tribune action (max +2D total).

### PP-038 — BG vs TTRPG Pool Size
BG aggregates (sum of all Martial). TTRPG uses per-unit pools. Not statistically equivalent by design.

### PP-039 — Military 0 + Muster
At Military 0: Muster actions produce no units and may not be taken.

### PP-040 — BG Unit TS (Southernmost)
Default TS=0. Restoration+Weaver: TS=30. Varfell VTM≥2: TS=30. Church Templar: TS=0 (doctrine).

### PP-041 — Military Loss Timing
TTRPG: immediate. BG: queues to Accounting. Hybrid: TTRPG timing during battle.

### PP-042 — Military Victory and TC/RS
Military victory alone produces no TC or RS change. Thread operations during battle produce standard RS changes.

### PP-043 — Wound Penalties in Hybrid
Wound Ob penalties apply to PC's CR checks in TTRPG mass battle. Do NOT reduce BG commander bonus (Military÷3 calculation).

## PENDING EDITORIALS BLOCKING FULL SYNC
- ED-001: Card-Hand system (P1-BLOCKER) — prevents full stage_bg sync
- ED-031: Overwhelming threshold Ob+1 vs 2×Ob (P1)
- ED-032: TC 80 seizure scope (P1)
- ED-033: Commander bonus formula (P1)
- ED-034: Ceiral Ritual scale asymmetry (P2)
- ED-035: Muster output in BG context (P2)
- ED-036: Altonian unit stats BLOCKER
- ED-039: Military seasonal cap pooling (P2)
