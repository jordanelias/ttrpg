<!-- version: v0.14+design-ST | source: bg_v05_simulation_and_patches.md | last_updated: 2026-04-02 -->
<!-- PATCHES APPLIED: P-12-P-32 (prior); ST-BG-01-10, ST-INT series added 2026-04-02 -->
<!-- PATCHES APPLIED: PP-112 (remove struck Majority-1s), PP-113-PP-122 (gap fills) 2026-04-02 -->
<!-- NOTE: stage6_factions.md is STALE for BG mode. bg_v05 is canonical for all BG faction mechanics. -->
<!-- STALE CHECK: BG editorial blockers pending (BG-E-30 card-hand adoption). See canon/editorial_ledger.yaml. -->

# params_board_game.md — Board Game Mode (v0.5)

## Dice System
d10 pool. Same engine as TTRPG.
| Face | Effect |
|------|--------|
| 1 | -1 success |
| 2-6 | 0 |
| 7-9 | +1 success |
| 10 | +2 successes |

**Majority-1s override: STRUCK (PP-112).** All rolls resolve through standard degree table only. Removed 2026-04-02.
Ob minimum = 1. No modifier may push Ob below 1.

## Degree Table
| Net | Degree |
|-----|--------|
| >= Ob + 1 | Overwhelming [PROVISIONAL: ED-031 — BG uses Ob+1 surplus; TTRPG uses 2xOb. Intentional divergence; awaiting user confirmation.] |
| = Ob | Success |
| Ob - 1 | Partial |
| <= 0 | Failure |

## Stat Ceilings and Floors (PP-113)
| Stat | Floor | Ceiling | Notes |
|------|-------|---------|-------|
| Mandate | 0 | 7 | 0 = Collapse state |
| Influence | 1 | 7 | Cannot drop below 1 (faction remains extant) |
| Wealth | 0 | 7 | 0 = cannot Trade or fund Wealth-requiring actions |
| Military | 0 | 7 | 0 = cannot Muster (PP-039) |
| Stability | 0 | 7 | 0 = Collapse trigger (P-15) |
| Standing | 0 | 10 | No in-game benefit above 7; 10 is cosmetic maximum |

## Standard Action Ob Reference (P-21)
| Action | Default Ob | Key Modifiers |
|--------|-----------|---------------|
| Muster (Legionary Inward) | 2 | -1 T2, -1 T11 |
| March (Legionary Outward) | 2 | +1 T8 (terrain) |
| Govern (Consul Inward) | 2 | -1 own capital; -1 with Architectus |
| Trade (Consul Outward) | 2 | +1 IP>=30; +1 T10 |
| Diplomacy (Senator Outward) | 2 | -1 Diplomat card; -1 own territory; +1 Standing>=3 vs target |
| Decree (Senator Inward) | 2 | +1 non-home territory; -1 capital |
| Parliamentary Manoeuvre | 2 | +1 PI<=2; -1 PI>=7 |
| Investigate (Tribune Inward) | 2 | -1 own territory; +1 Niflhel-active |
| Spy (Tribune Outward) | 2 | +1 heavily fortified |
| Thread Operation | 2 | -1 per Restoration Presence marker; see Thread procedure |
| Community Organising | 2 | — |
| Community Project start | 1 | — |
| Community Project advance | 2 | — |
| Fortify | 2 | — |
| Forgetting Check | 1 | -1 Restoration Weaver present; -1 VTM 2+ |

All Obs: floor 1.

## Faction Starting Stats
| Faction | Mandate | Influence | Wealth | Military | Intel | Stability | Notes |
|---------|---------|-----------|--------|----------|-------|-----------|-------|
| Crown | 5 | 5 | 4 | 4 | — | 4 | |
| Church | 5 | 6 | 5 | 4 | — | 5 | Starting TC: 28 (P-32) |
| Hafenmark | 4 | 4 | 5 | 3 | — | 4 | |
| Varfell | 3 | 4 | 3 | 4 | — | 4 | BG-specific (Mandate/Wealth 3, not TTRPG 4) |
| Restoration | 2 | 4 | 2 | 0 | — | 3 | 5-player only |
| Lowenritter | 3 | 2 | — | 6 | — | 4 | No Wealth; enters at coup trigger |
| Niflhel | — | 5 | 4 | — | — | 4 | |
| Schoenland | — | — | — | — | — | — | Spoiler only; not playable |

## Clock Starting Values and Targets
| Clock | Start | Floor | Ceiling | Win/Loss Threshold |
|-------|-------|-------|---------|--------------------|
| TC (Theocracy Clock) | 28 (P-32) | 0 | 100 [PROVISIONAL: ED-056 — no mechanical effect above 80 except seizure; 100 is cosmetic] | 65 = Church Holy State (P-32) |
| RS (Rendering Stability) | 72 | 0 | 100 | RS = 0 = Rupture (all factions lose) |
| IP (Invasion Pressure) | 20 | 0 | 100 [PROVISIONAL: PP-114 — post-80 escalation table applies] | 75 = Vanguard (AER <=2); 80 = Vanguard (AER 3); AER 4: IP cap 60; AER 5: IP fixed 50 |
| PI (Parliamentary Integrity) | 5 | 0 | 10 [PROVISIONAL: ED-055] | PI 0 = Parliament dissolved + Lowenritter coup trigger [PROVISIONAL: ED-055] |

## PI Thresholds (PP-115) [PROVISIONAL: ED-055 — user confirmation required]
| PI | Effect |
|----|--------|
| 10 | Full Parliamentary authority. Crown Policy Instrument requires PI vote to override. |
| 7-9 | Standard operation. Parliamentary Manoeuvre: -1 Ob. |
| 5-6 | Starting range. No modifier. |
| 3-4 | Degraded Parliament. Church Assert/Suppress resolution Ob -1. |
| 1-2 | Near-collapse. Lowenritter coup condition met if Military conditions also satisfied. |
| 0 | Parliament dissolved. Lowenritter coup fires immediately if coup trigger conditions otherwise met. All Diplomacy between factions +1 Ob (no institutional mediation). |

## IP Post-80 Escalation (PP-114) [PROVISIONAL]
| IP | Effect |
|----|--------|
| 80 | Altonian Vanguard deployed. Standard threshold. |
| 81-89 | Vanguard advances one territory/season automatically. |
| 90-99 | Vanguard reinforced: Altonian Military treated as +2 all engagements. |
| 100 | Altonian Conquest: campaign ends, shared defeat. |

## IP Advancement Formula (P-28)
IP has NO automatic per-season advance. Event-driven only.
| Condition | IP Change |
|-----------|-----------|
| Base per season | 0 |
| TC > 60 | +1/season |
| Altonian Trade Mission refused (IP 30 event) | +1 |
| Torben sent to Altonia | -3/season; +5 immediately on compliance |
| Torben refuses (Crown refuses at IP 40) | +3 immediately |
| Elske returns to Valoria | +5 immediately |
| Schoenland Proxy Arms Deal active (IP 45) | +2 this season |
| Crown Free Trade Decree | -1 |
| AER >= 4 | IP cannot advance above 60 |
| AER = 5 | IP fixed at 50 |
| Grand Diplomatic Scene milestone | -5 immediately |
| Military success vs Altonian interest | -2 |
| Altonian Vanguard repelled | -5 |

## TC Advancement (key sources)
| Source | TC Change |
|--------|-----------|
| T3 control (base) | +1/season |
| Church Assert (mandatory at TC > 50) | +1/season |
| Heresy Investigation confirmed | +0.5 |
| Templar deployment | varies |
| TC 80 Seizure success (per territory) | +2 |
| Hafenmark Baralta suppression (Mandate >= 4) | -1/season |
| Grand Debate challenging Church authority | -2 (Overwhelming) |
| Reformed Settlement (Church Resists) | +3 |
| Starting value (P-32) | 28 |

## TC Seasonal Cap (PP-116) [PROVISIONAL: F-43 / ED-056]
| Source category | Max change/season |
|----------------|------------------|
| Domain Actions only | +-3 |
| All sources combined | +-5 |
| TC 80 Seizure gains | NOT counted against cap. Seizure is an event resolution. |

## Cascade Depth Cap
Maximum 3 immediate mechanical effects per card play resolution step.
Clock changes (RS, TC, IP, PI) count against the cap (P-29).
Excess effects queue to Accounting Phase 5 Step 8.

## Faction Collapse (P-15) and Recovery (PP-117) [PROVISIONAL: ED-053]
On Stability = 0: (1) Mandate -> 0 immediately. (2) All other stats freeze. (3) Collapse state up to 2 seasons.

**Collapse exit (PP-117) [PROVISIONAL: ED-053 — user confirmation required]:**
Exit when ALL met:
1. At least 1 full season elapsed in collapse state.
2. No hostile Domain Action targeting that faction this season.
3. Allied faction (Pledge active) or own player takes Govern Ob 2 in any formerly controlled territory. Success: Stability -> 1, exit collapse.
4. Auto-exit at Season 2 end if not earlier: Stability 1, Mandate 0. Faction functional but politically hollow.

## Simultaneous Catastrophe (PP-118) [PROVISIONAL: ED-054]
If RS = 0 and IP >= 80 both trigger in the same Accounting phase:
1. RS = 0 (Rupture) checked at Step 6 takes precedence. Campaign ends as shared loss.
2. Exception: Restoration victory declared at Step 5 pre-empts Step 6 Rupture. Victory check fires before RS loss application.

## Battle Resolution (P-16)
Both sides roll simultaneously. Compare net successes.
- Attacker net > Defender net: Attacker wins.
- Defender net > Attacker net: Defender wins.
- Equal nets: Stalemate. Both Cohesion -1. No territorial change.

## BG Unit Cohesion (PP-119) [PROVISIONAL: GAP-BG-07]
Per-unit integer track (0-6).
| Unit Type | Starting Cohesion |
|-----------|------------------|
| Levy | 3 |
| Infantry | 4 |
| Elite | 5 |
| Cavalry | 4 |
| Artillery | 3 |
| Thread Corps | 4 |
At Cohesion 0: unit destroyed. Recovery: +1/season at Accounting if no battle engagement this season.

## BG Thread Operations — Coherence Absence (PP-120) [PROVISIONAL: ED-057]
BG Thread Operations produce NO Coherence cost. Coherence is TTRPG personal-scale only.
BG Thread op costs: Ob penalties, Thread Debt tokens, RS changes, Co-Movement card draws only.
Hybrid: PC practitioners incur personal Coherence per TTRPG rules. Cascade Step 3 applies consequences.

## Reformed Settlement — Diplomatic Penalty Permanent (PP-121) [PROVISIONAL: ED-058]
+1 Ob to all Diplomacy targeting Hafenmark after Reformed Settlement (RDT >= 5) is PERMANENT. No reversal mechanic.
[EDITORIAL: ED-058 — confirm no reversal mechanic. If Treaty of Accommodation or Grand Debate win should reset, design that reversal.]

## CP Awards in Hybrid Mode (PP-122) [PROVISIONAL]
Procedure for PC faction leaders earning Character Points (CP) from BG Domain Actions:
1. PC declares which Belief the action expresses before rolling.
2. Success or Overwhelming: CP +1 (Belief Engagement).
3. Institutional Mandate Uphold/Compromise: CP +1 if PC articulates Conviction link regardless of outcome.
4. Worked example: Crown PC holds Belief "Parliament must be preserved." Crown Decree degrading PI = Belief conflict. Crown PC Compromising Mandate to block the Decree earns CP +1.
5. BG-only (no PCs): CP does not apply.

## Prosperity (P-22)
Territory-level track (0-5). Not a faction stat.
Govern Success: Prosperity +1. Govern Failure: -1. Year-End: Prosperity >= 3 -> +1 Wealth. Prosperity >= 5 -> +2 Wealth.
Starting Prosperity: T1:4 T2:3 T3:4 T4:2 T5:3 T6:5 T7:4 T8:3 T9:3 T10:2 T11:4 T12:1 T13:1 T14:3 T15:4.

## Fog of War (Hybrid, P-20)
Stats 1-3: Poor. Stats 5-7: Good. Stat = 4: roll 1d6 (NOT d10) — 1-3 Poor, 4-6 Good.

## Forgetting Check (P-26)
| Faction | Pool |
|---------|------|
| Restoration | Influence + 1D per Presence marker in T13 |
| Varfell | VTM level in dice |
| Other factions | Wealth / 2 (round up) |
Ob 1 (floor). Thread-qualified presence: may reroll one die once. Hybrid: PC Spirit + TS/10 (round down).

## VTM (Varfell Thread Monitoring)
Bootstrapping (P-27): Roll Influence vs Ob 1. Success/Overwhelming: VTM +1. Partial: Latent VTM token. Failure: no retry.
VTM cap: once per season (P-31).

| VTM | Ability |
|-----|---------|
| 1 | Tribune range: any non-adjacent territory |
| 2 | Thread Resonance: while Tribune in thread-active territory |
| 3 | Patience Counter tracks publicly |
| 4 | 4 PC spend: Tribune Outward any territory |
| 5 | Once/game: choose Actualized dimension of one Co-Movement draw |

## Thread Debt (P-24)
+1 Ob to NEXT Thread operation in that territory (not current).

## Casus Belli Expiration (P-14)
| Source | Expiry |
|--------|--------|
| Treaty betrayal | Permanent until used |
| Brutal disposition vs civilians | 3 seasons unused |
| Fabricated Heresy Investigation | 3 seasons unused |
| Varfell Patience Protocol | Expires on Riskbreaker exposure |
One CB per faction at a time.

## TC 80 Territorial Seizure
Per-territory roll: Church Mandate vs Ob 3 (contested) or Ob 2 (neutral).
Partial (P-30): Not seized; 1 Templar Staging Token placed.
Overwhelming: Immediate seizure, no Standing cost.
Success: Seizure; TC +2; PI -1.
[EDITORIAL: ED-032 — TC 80 scope: declared target territories only, or all-territory sweep? Confirm.]

## Phase 4 Tiebreaking (P-18)
2-way Stability tie: simultaneous. 3+ way: player turn order. Military-vs-military ties: always simultaneous.

## Church Holy State Victory (P-32)
TC >= 65 (not 70). Starting TC 28 (not 22).

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

<!-- patch_history: references/params_board_game_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->
