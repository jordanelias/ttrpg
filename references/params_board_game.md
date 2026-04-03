<!-- version: v0.5.5+AUD-BG-01 | source: bg_v05_simulation_and_patches.md | last_updated: 2026-04-02 -->
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

## Degree Table (PP-179 — now matches TTRPG)
| Net Successes | Degree |
|--------------|--------|
| ≥ 2× Ob | Overwhelming |
| = Ob | Success |
| 0 < net < Ob | Partial |
| ≤ 0 | Failure |

Ob 10 exception: Overwhelming unavailable. Partial requires net ≥ 5.

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
| Trade (Consul Outward) | 2 | +1 Institutional Pressure>=30; +1 T10 |
| Diplomacy (Senator Outward) | 2 | -1 Diplomat card; -1 own territory; +1 Standing>=3 vs target |
| Decree (Senator Inward) | 2 | +1 non-home territory; -1 capital |
| Parliamentary Manoeuvre | 2 | +1 Public Instability<=2; -1 Public Instability>=7 |
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
| Church | 5 | 6 | 5 | 4 | — | 5 | Starting Theocracy Counter: 28 (P-32) |
| Hafenmark | 4 | 4 | 5 | 3 | — | 4 | |
| Varfell | 3 | 4 | 3 | 4 | — | 4 | BG-specific (Mandate/Wealth 3, not TTRPG 4) |
| Restoration | 2 | 4 | 2 | 0 | — | 3 | 5-player only |
| Lowenritter | 3 | 2 | — | 6 | — | 4 | No Wealth; enters at coup trigger |
| Niflhel | — | 5 | 4 | — | — | 4 | |
| Schoenland | — | — | — | — | — | — | Spoiler only; not playable |

## Clock Starting Values and Targets
| Clock | Start | Floor | Ceiling | Win/Loss Threshold |
|-------|-------|-------|---------|--------------------|
| Theocracy Counter (Theocracy Clock) | 28 (P-32) | 0 | 100 [PROVISIONAL: ED-056 — no mechanical effect above 80 except seizure; 100 is cosmetic] | 65 = Church Holy State (P-32) |
| Rendering Stability (RS) | 72 | 0 | 100 | Rendering Stability = 0 = Rupture (all factions lose) |
| Institutional Pressure (Invasion Pressure) | 20 | 0 | 100 [PROVISIONAL: PP-114 — post-80 escalation table applies] | 75 = Vanguard (AER <=2); 80 = Vanguard (AER 3); AER 4: Institutional Pressure cap 60; AER 5: Institutional Pressure fixed 50 |
| Public Instability (Parliamentary Integrity) | 5 | 0 | 10 [PROVISIONAL: ED-055] | Public Instability 0 = Parliament dissolved + Lowenritter coup trigger [PROVISIONAL: ED-055] |

## Public Instability Thresholds (PP-115) [PROVISIONAL: ED-055 — user confirmation required]
| Public Instability | Effect |
|----|--------|
| 10 | Full Parliamentary authority. Crown Policy Instrument requires Public Instability vote to override. |
| 7-9 | Standard operation. Parliamentary Manoeuvre: -1 Ob. |
| 5-6 | Starting range. No modifier. |
| 3-4 | Degraded Parliament. Church Assert/Suppress resolution Ob -1. |
| 1-2 | Near-collapse. Lowenritter coup condition met if Military conditions also satisfied. |
| 0 | Parliament dissolved. Lowenritter coup fires immediately if coup trigger conditions otherwise met. All Diplomacy between factions +1 Ob (no institutional mediation). |

## Institutional Pressure Post-80 Escalation (PP-114) [PROVISIONAL]
| Institutional Pressure | Effect |
|----|--------|
| 80 | Altonian Vanguard deployed. Standard threshold. |
| 81-89 | Vanguard advances one territory/season automatically. |
| 90-99 | Vanguard reinforced: Altonian Military treated as +2 all engagements. |
| 100 | Altonian Conquest: campaign ends, shared defeat. |

## Institutional Pressure Advancement Formula (P-28)
Institutional Pressure has NO automatic per-season advance. Event-driven only.
| Condition | Institutional Pressure Change |
|-----------|-----------|
| Base per season | 0 |
| Theocracy Counter > 60 | +1/season |
| Altonian Trade Mission refused (Institutional Pressure 30 event) | +1 |
| Torben sent to Altonia | -3/season; +5 immediately on compliance |
| Torben refuses (Crown refuses at Institutional Pressure 40) | +3 immediately |
| Elske returns to Valoria | +5 immediately |
| Schoenland Proxy Arms Deal active (Institutional Pressure 45) | +2 this season |
| Crown Free Trade Decree | -1 |
| AER >= 4 | Institutional Pressure cannot advance above 60 |
| AER = 5 | Institutional Pressure fixed at 50 |
| Grand Diplomatic Scene milestone | -5 immediately |
| Military success vs Altonian interest | -2 |
| Altonian Vanguard repelled | -5 |

## Theocracy Counter Advancement (key sources)
| Source | Theocracy Counter Change |
|--------|-----------|
| T3 control (base) | +1/season |
| Church Assert (mandatory at Theocracy Counter > 50) | +1/season |
| Heresy Investigation confirmed | +0.5 |
| Templar deployment | varies |
| Theocracy Counter 80 Seizure success (per territory) | +2 |
| Hafenmark Baralta suppression (Mandate >= 4) | -1/season |
| Grand Debate challenging Church authority | -2 (Overwhelming) |
| Reformed Settlement (Church Resists) | +3 |
| Starting value (P-32) | 28 |

## Theocracy Counter Seasonal Cap (PP-116) [PROVISIONAL: F-43 / ED-056]
| Source category | Max change/season |
|----------------|------------------|
| Domain Actions only | +-3 |
| All sources combined | +-5 |
| Theocracy Counter 80 Seizure gains | NOT counted against cap. Seizure is an event resolution. |

## Cascade Depth Cap
Maximum 3 immediate mechanical effects per card play resolution step.
Clock changes (Rendering Stability, Theocracy Counter, Institutional Pressure, Public Instability) count against the cap (P-29).
Excess effects queue to Accounting Phase 5 Step 8.

## Faction Collapse (P-15) and Recovery (PP-117) [PROVISIONAL: ED-053]
On Stability = 0: (1) Mandate -> 0 immediately. (2) All other stats freeze. (3) Collapse state up to 2 seasons.

**Collapse exit (PP-117) [PROVISIONAL: ED-053 — user confirmation required]:**
Exit when ALL met:
1. At least 1 full season elapsed in collapse state.
2. No hostile Domain Action targeting that faction this season.
3. Allied faction (Pledge active) or own player takes Govern Ob 2 in any formerly controlled territory. Success: Stability -> 1, exit collapse.
4. Auto-exit at Season 2 end if not earlier: Stability 1, Mandate 0. Faction functional but politically hollow.

## Simultaneous Catastrophe (PP-118 rev.1) [PROVISIONAL: ED-054]
Accounting sequence context: Institutional Pressure Advancement at Step 4. Rendering Stability adjustment at Step 6. Victory checks at Step 12.
1. Institutional Pressure = 80 threshold fires at Step 4: Vanguard deploys as a board event. Campaign does not end at Step 4.
2. Rendering Stability = 0 (Rupture) fires at Step 6. Campaign ends as shared loss. Rupture takes precedence over all other unresolved win conditions.
3. Restoration pre-check at Step 5: Before Rendering Stability losses applied at Step 6, check if Restoration has 5 Presence markers in 5 non-adjacent territories held 2 consecutive seasons AND Rendering Stability >= 1 at Step 5. If both: Restoration wins immediately. Step 6 does not fire.
4. If Rendering Stability = 0 entering Step 5 (prior loss same phase): Restoration cannot win. Rupture fires Step 6.
5. Church Holy State (Theocracy Counter >= 65): declared at Step 12. If Restoration wins at Step 5 in same Accounting phase: Restoration wins; Step 12 not reached.
6. Simultaneous multi-faction Step 12 wins: [EDITORIAL: ED-054 — confirm co-victory or Game Master ruling for simultaneous Step 12 conditions.] Victory check fires before Rendering Stability loss application.

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
BG Thread op costs: Ob penalties, Thread Debt tokens, Rendering Stability changes, Co-Movement card draws only.
Hybrid: Player Character practitioners incur personal Coherence per TTRPG rules. Cascade Step 3 applies consequences.

## Reformed Settlement — Diplomatic Penalty Permanent (PP-121) [PROVISIONAL: ED-058]
+1 Ob to all Diplomacy targeting Hafenmark after Reformed Settlement (RDT >= 5) is PERMANENT. No reversal mechanic.
[EDITORIAL: ED-058 — confirm no reversal mechanic. If Treaty of Accommodation or Grand Debate win should reset, design that reversal.]

## CP Awards in Hybrid Mode (PP-122) [PROVISIONAL]
Procedure for Player Character faction leaders earning Character Points (CP) from BG Domain Actions:
1. Player Character declares which Belief the action expresses before rolling.
2. Success or Overwhelming: CP +1 (Belief Engagement).
3. Institutional Mandate Uphold/Compromise: CP +1 if Player Character articulates Conviction link regardless of outcome.
4. Worked example: Crown Player Character holds Belief "Parliament must be preserved." Crown Decree degrading Public Instability = Belief conflict. Crown Player Character Compromising Mandate to block the Decree earns CP +1.
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
Ob 1 (floor). Thread-qualified presence: may reroll one die once. Hybrid: Player Character Spirit + Thread Sensitivity/10 (round down).

## VTM (Varfell Thread Monitoring)
Bootstrapping (P-27): Roll Influence vs Ob 1. Success/Overwhelming: VTM +1. Partial: Latent VTM token. Failure: no retry.
VTM cap: once per season (P-31).

| VTM | Ability |
|-----|---------|
| 1 | Tribune range: any non-adjacent territory |
| 2 | Thread Resonance: while Tribune in thread-active territory |
| 3 | Patience Counter tracks publicly |
| 4 | 4 Player Character spend: Tribune Outward any territory |
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

## Theocracy Counter 80 Territorial Seizure
Per-territory roll: Church Mandate vs Ob 3 (contested) or Ob 2 (neutral).
Partial (P-30): Not seized; 1 Templar Staging Token placed.
Overwhelming: Immediate seizure, no Standing cost.
Success: Seizure; Theocracy Counter +2; Public Instability -1.
[EDITORIAL: ED-032 — Theocracy Counter 80 scope: declared target territories only, or all-territory sweep? Confirm.]

## Phase 4 Tiebreaking (P-18)
2-way Stability tie: simultaneous. 3+ way: player turn order. Military-vs-military ties: always simultaneous.

## Church Holy State Victory (P-32)
Theocracy Counter >= 65 (not 70). Starting Theocracy Counter 28 (not 22).

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


## Fail Forward — Board Game Mode (PP-177) [PROVISIONAL: ED-085, ED-086, ED-087]
Applies to all Domain Action rolls. Fires on Partial and Failure results.

### Complication Tiers
| Tier | Severity | Used for |
|------|----------|----------|
| Minor | Standing −1 OR Public Instability +1 (acting faction chooses) | Partial outcomes |
| Moderate | Mandatory consequence from action-type table | Failure outcomes |
| Severe | Moderate + Stability −1 | Failure on Ob ≥ 4 only |

### Action-Type Complication Table
| Domain Action | Partial (Minor — player chooses 1) | Failure (Moderate — mandatory) |
|---------------|-------------------------------------|--------------------------------|
| Govern (Inward) | Standing −1 OR Public Instability +1 | Prosperity −1 in target territory |
| Trade (Outward) | Standing −1 OR Wealth −1 this season | Wealth −1 (permanent until Accounting) |
| Muster (Inward) | Unit mustered at Cohesion −1 OR Standing −1 | No unit mustered; Wealth −1 |
| Diplomacy (Outward) | Standing −1 OR target faction Standing +1 | Target faction gains Casus Belli vs acting faction (Ob 3 to dismiss) |
| Decree (Inward) | Mandate −1 for 1 season OR Public Instability +1 | Mandate −1 (permanent until Accounting) |
| Parliamentary Manoeuvre | Standing −1 OR no effect (player's choice) | Mandate −1 + opponent Standing +1 |
| Investigate (Inward) | One datum unreliable (GM marks) OR Standing −1 | No intel gained; Stability −1 |
| Spy (Outward) | Intel gained but identity exposed OR Standing −1 | No intel; target may take free Intel action vs actor next season |
| Thread Operation | Thread Debt token OR Rendering Stability −1 | Thread Debt token; Rendering Stability −2 |
| Community Organising | +1 Ob to next Community action in territory OR Standing −1 | No progress; Institutional Pressure +1 |
| Fortify | Fortification at unit Cohesion −1 OR Standing −1 | No fortification; Wealth −1 |
| Parliamentary Vote | Losing margin halved OR Public Instability −1 | Calling faction Mandate −1 + Public Instability −1 |

**Battle Resolution excluded.** FF applies to Domain Actions only. Battle has its own outcome table.
**Casus Belli from Diplomacy Failure:** Standard Casus Belli rules apply; expires 3 seasons unused; one Casus Belli per faction at a time.
**Thread Operation FF stacks with co-movement:** FF complication is in addition to mandatory co-movement effects (P-01). Not a replacement.
**Parliamentary Manoeuvre Partial update (PP-177 supersedes PP-170 Partial clause):** Partial = Minor complication fires. Player may choose "no effect" as their Minor choice — PP-170's "no effect" ruling is preserved as a menu option.

[PROVISIONAL: Confirmed as design intent by SIM-FF-01. ED-085/086/087 flagged for user review.]

<!-- patch_history: references/params_board_game_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->

## Season and Phase Structure (PP-169, extracted from compilation B4)
One game round = one season. Campaign year = 4 rounds. Standard: 12-16 rounds. Extended: 20 rounds.

| Phase | Name | Description |
|-------|------|-------------|
| 1 | Season Card | Flip top Event deck card. Modifier public. |
| 2 | Planning | All players place 5 Order tokens face-down simultaneously. Placement order: lowest Stability first. Ties: roll. |
| 3 | Intel Reveal | Niflhel (and Intel-capable factions) reveals prior season Intel results. |
| 4 | Order Resolution | Flip all orders. Resolve by priority sequence. |
| 5 | Seasonal Accounting | Clocks advance. Stability checks. Stat changes. CP awards. Victory checks. |
| 6 | Cleanup | Remove temporary effects. Advance round tracker. Draw replacement cards. |

Order tokens: 5 per faction per season. Up to 3 in one territory. 1 token = 1 Domain Action. Faction Unique Power uses designated token.

## Order Priority Table (PP-169, from compilation B4)
| Priority | Order Type | Notes |
|----------|-----------|-------|
| 1 | Thread Operations | RS change first; Co-Movement fires before all other resolution. |
| 2 | Military (March, Assault, Siege) | Battles resolve simultaneously per territory. |
| 3 | Intel and Sabotage | Outcomes apply before economic/governance. |
| 4 | Domain Actions (Govern, Trade, Muster, Diplomacy) | All standard Domain Actions. |
| 5 | Unique Powers | Faction Unique Power resolves last. |
| 6 | Decree / Parliamentary Manoeuvre | Take effect at next accounting if timing ambiguous. |

## Unit Muster Ob Table (PP-169, from compilation B6)
| Unit Type | Muster Ob | Prerequisite |
|-----------|----------|--------------|
| Light Infantry | 1 | None |
| Heavy Infantry | 2 | Territory Prosperity >= 5 + Wealth Ob 2 |
| Cavalry | 3 | Territory Prosperity >= 6 or officer History |
| Ranged | 2 | Officer with Ranged proficiency |
| Artillery | 4 | Wealth Ob 4 + 1 season construction |
| Knights Templar | Church only | Not Muster-able by standard order |

Unit starting Cohesion: Light Infantry 3, Heavy Infantry 4, Cavalry 4, Ranged 3, Artillery 3, Thread Corps 4.

## Faction Capital Territories (PP-169, from compilation B3)
| Faction | Capital Territory | Territory Number |
|---------|------------------|-----------------|
| Crown | Valorsplatz | T1 |
| Church | Himmelenger | T3 |
| Hafenmark | Hafenvalor | T6 |
| Varfell | Varfell | T9 |
| Guilds | Sigurdshelm | T10 |
| Niflhel | Sigurdshelm | T10 (contested; see Niflhel victory condition) |
| Restoration Movement | No fixed capital | — |
| Lowenritter | Arnesheld | T5 |

## Parliamentary Manoeuvre Results (PP-170 — fills spec gap PG-07)
Roll: Mandate vs Ob = opponent Influence / 2 (round up).
| Degree | Effect |
|--------|--------|
| Overwhelming | One pending Domain Action outcome delayed 1 season (cannot delay Unique Powers or Decrees) + opponent Stability -1 for 1 season. |
| Success | One pending Domain Action outcome delayed 1 season (cannot delay Unique Powers or Decrees). |
| Partial | No effect. [PP-170: explicit ruling.] |
| Failure | No effect. Hafenmark Mandate -1 for 1 season (procedural blowback). |

## Theocracy Counter Starting Value — Canonical
TC starts at 28 (P-32). Compilation B1 states 15 — STALE (pre-P-32). Use 28.

## Mandate Recovery — see PP-174 section below (Victory Condition Patches).

## Victory Condition Patches (PP-171 through PP-176)

### Church Deed 4 — PATCHED (PP-171)
~~Control Valorsplatz~~
**NEW: Crown Mandate ≤ 2 for 2 consecutive seasons.**
Rationale: Valorsplatz seizure requires TC ≥ 70 + military defeat of Crown, unreachable in standard 12–16 round game. Institutional erosion (Crown political collapse) is the canonical theocratic capture mechanism.

### Crown Deed 4 — PATCHED (PP-172)
~~Torben Loyalty Clock ≥ 5~~
**NEW: Torben Loyalty Clock ≥ 5 OR Institutional Pressure < 30 at game end.**
Rationale: If IP never crosses 30, the Loyalty Clock never activates (I-01 event not triggered). Without escape clause, Deed 4 is neither met nor checkable — undefined state.

### Intel Stat Advancement — ADDED (PP-173)
No prior mechanic defined. New rule:
Each season a faction executes at least 1 successful Intel order or Quiet Network (Intelligence mode) order: that faction advances their Intel track +0.25. When the track reaches the next integer: Intel stat increases by 1.
- Advancement cap: Intel stat max = 7.
- Max track advance per season: +0.25 (one qualifying success per season; additional successes do not stack).
- "Successful" = Success or Overwhelming result on the roll.

### Mandate Recovery — ADDED (PP-174)
No prior mechanic defined. New rule:
Govern Overwhelming in a faction's own capital territory: Mandate +1 (to a maximum of the faction's printed starting Mandate value).
- Once per season maximum.
- Does not apply to Govern in non-capital territories.
- Does not apply to Govern Success (only Overwhelming triggers recovery).
- Faction starting Mandate values (recovery caps): Crown 5, Church 5, Hafenmark 4, Varfell 4, Guilds 3, Niflhel n/a (no Mandate stat).

### Guild Favour Advancement — EXPLICIT (PP-175)
Previously implied, now stated:
Govern Success in a territory: Guild Favour +1 in that territory (Guilds only; other factions do not have a Favour track).
Govern Overwhelming in a territory: Guild Favour +2 in that territory.
Govern Failure: Guild Favour −1 in that territory.
Starting Guild Favour: 3 in all Guilds-controlled territories (T8 Eidursjo, T11 Halvardshelm). 0 in all other territories.
Ceiling: 10. No in-game effect above 7 except scoring.

### Varfell Deed 1 — PATCHED (PP-176)
~~Intel ≥ 6~~
**NEW: Intel ≥ 5.**
Rationale: Intel 6 from starting value 4 requires ~16 seasons of successful Intel orders at median — exceeds standard 12-round game. Intel 5 requires ~8 seasons, achievable mid-game. Varfell and Niflhel both target Intel 5, creating competitive parity on this deed dimension.

## Deed Token Summary — Post-Patch (PP-171 through PP-176)

### Crown
| Deed | Condition |
|------|-----------|
| 1 | Mandate ≥ 5 |
| 2 | Control Valorsplatz + Gransol + ≥ 2 other territories |
| 3 | Theocracy Counter < 60 and Institutional Pressure < 75 simultaneously |
| 4 | Torben Loyalty ≥ 5 OR Institutional Pressure < 30 at game end (PP-172) |

### Church
| Deed | Condition |
|------|-----------|
| 1 | Theocracy Counter ≥ 40 |
| 2 | Church Mandate ≥ 5 |
| 3 | Control Himmelenger (continuously since game start or recaptured) |
| 4 | Crown Mandate ≤ 2 for 2 consecutive seasons (PP-171) |

### Hafenmark (unchanged)
| Deed | Condition |
|------|-----------|
| 1 | Mandate ≥ 4 and no active Heresy Investigation |
| 2 | Control Hafenvalor + Lowenskyst |
| 3 | Theocracy Counter < 50 |
| 4 | ≥ 1 Parliamentary ruling in Hafenmark's favour |

### Varfell
| Deed | Condition |
|------|-----------|
| 1 | Intel ≥ 5 (PP-176; was ≥ 6) |
| 2 | Thread Knowledge (TK) ≥ 3 |
| 3 | Control Varfell (T9) |
| 4 | ≥ 2 hidden faction stats revealed (accumulated) |

### Guilds (unchanged)
| Deed | Condition |
|------|-----------|
| 1 | Wealth ≥ 6 |
| 2 | Control Halvardshelm (T11) + Eidursjo (T8) |
| 3 | Guild Favour ≥ 5 in ≥ 3 territories |
| 4 | Institutional Pressure < 75 |

### Niflhel (unchanged)
| Deed | Condition |
|------|-----------|
| 1 | Intel ≥ 5 |
| 2 | Control Sigurdshelm (T10) |
| 3 | ≥ 3 pieces of hidden faction information held simultaneously |
| 4 | No Compromise token AND Stability ≥ 4 |

## Mandate Recovery (PP-174, replaces PARAMS GAP notice)
Govern Overwhelming in own capital territory: Mandate +1 (max once/season; max = faction starting Mandate).
## Parliamentary Vote (ED-053b resolved — provisional)
Faction calls a Parliamentary Vote via Parliamentary Manoeuvre Domain Action.
Resolution:
- Each participating faction rolls their Influence pool (1D per Influence point), TN 7
- Ob = highest opposing faction's Influence ÷ 2 (round up)
- Net successes: faction with highest net wins the vote; ties go to faction with higher Mandate
- Effects: winner faction gains +1 PI (Parliamentary Integrity); loser −1 PI
[PROVISIONAL — ED-053]

## Card-Hand System — Provisional (ED-001 resolved — provisional)
Pending full design. Provisional rule to unblock simulation:
- Each faction receives 6 tactic cards at season start (4 shared + 2 faction-specific)
- Draw 1 additional card at start of each Battle phase
- Play 1 card per Battle or Domain Action as appropriate
- Cards discard after use; hand refreshes to 6 at Seasonal Accounting
- Card effects are the disposition modifiers in §B.4
- [PROVISIONAL — requires full card-hand design review. ED-001 blocker unblocked for simulation only]

## Artillery Disposition (ED-040 resolved — provisional)
Artillery units are locked to Balanced disposition in all BG contexts. Rationale: siege weapons cannot execute offensive or defensive tactical manoeuvres — they fire from fixed positions. [PROVISIONAL — confirmed as intentional]

## TC Threshold Check During Zoom In (ED-056b)
TC threshold check fires at Seasonal Accounting regardless of Zoom In suspension. See state_transfer_spec.md.

## Overwhelming Degree Table — BG Now Matches TTRPG (PP-179)
Resolves ST-BG-01.

**Old BG rule:** Overwhelming = net successes ≥ Ob + 1 (surplus 1 over Ob).
**New BG rule:** Overwhelming = net successes ≥ 2 × Ob. **Same as TTRPG.**
At Ob 1: Overwhelming at net ≥ 2 (unchanged — Ob+1 = 2×Ob when Ob=1).
At Ob 2: Overwhelming at net ≥ 4 (was net ≥ 3). P(Overwhelming) drops from ~42% to ~22% at pool 5D.
At Ob 3: Overwhelming at net ≥ 6 (was net ≥ 4). P drops from ~22% to ~5% at pool 5D.

Updated Degree Table (BG):
| Net Successes | Degree |
|--------------|--------|
| ≥ 2× Ob | Overwhelming |
| = Ob | Success |
| 0 < net < Ob | Partial |
| ≤ 0 | Failure |

**Ob 10 exception (inherited from TTRPG params_core):** Overwhelming unavailable at Ob 10. Partial requires net ≥ 5.

## Trade Network Investment — Hafenmark Wealth Sink (PP-178)
Hafenmark-exclusive action. Consul card, Inward orientation, in any Hafenmark-controlled territory.
Resolves ED-077.

**Cost:** 2 Wealth before rolling.
**Roll:** Wealth vs Ob 2.
| Degree | Effect |
|--------|--------|
| Overwhelming | Trade Route token placed between this territory and one adjacent territory. All Trade orders in either territory this season and next: +1D. Hafenmark gains +1 Guild Favour in the non-capital territory. Token persists until territory changes control. |
| Success | Trade Route token placed. +1D Trade in this territory only, this season. Token persists. |
| Partial | Trade Route token placed. No immediate bonus. Token persists. |
| Failure | Wealth cost paid. No token. Hafenmark Stability −1 this season. |

**Trade Route tokens:** Permanent while Hafenmark controls the territory. Lost when territory changes control. Maximum 1 token per territory pair. Tokens are public (visible to all factions).
**Thematic note:** Hafenmark invests trade surplus into durable economic infrastructure. Military seizure of Hafenmark territories destroys this infrastructure — a natural deterrent to aggression against the Duchy.

## Resolved Params Gaps

### PG-09: Torben Loyalty Clock (from arcs_09_11 / arcs_20_23)
Torben Loyalty Clock activates at value 8 when Institutional Pressure crosses 30 (I-01 event).
Degrades: −1/season while Torben is in Altonian territory.
Floor: 1 (never reaches 0 — Torben retains residual Valorian identity).
Recovery: Elske's presence slows decay by −1/season (net: 0 decay per season if Elske recruited). Covert contact (Intel vs Ob 3): success = no decay this season; failure = contact exposed, Institutional Pressure +1.
Crown Deed 4 condition: Torben Loyalty ≥ 5 (meaning: Clock has not degraded below 5 — at 8 at activation, requires max 3 seasons of unmitigated decay before failing).

### PG-10: Parliamentary Ruling Mechanic (from stress test / critical review)
A Parliamentary ruling is produced by a successful Parliamentary Manoeuvre (Success or Overwhelming result).
The ruling delays one pending Domain Action outcome by 1 season.
Hafenmark Deed 4 condition: "at least 1 Parliamentary ruling in Hafenmark's favour" = at least 1 successful Parliamentary Manoeuvre result (Success or Overwhelming) recorded this game. Track with a Deed token placed immediately on first success.

### PG-12: Hidden Information Persistence (Niflhel Deed 3)
Niflhel holds revealed faction stats as intelligence. Information expires if the underlying stat changes by more than ±1 from the revealed value (the intelligence is now materially wrong). At expiry: information no longer counts toward Deed 3.
Niflhel Deed 3: "≥ 3 pieces of hidden faction information held simultaneously" = 3 pieces of valid (non-expired) intelligence held at Accounting.

## Audit Patches (PP-180 bundle)

### Accounting Phase Reference Steps (PP-180, resolves F-01 partial)
Phase 5 — Seasonal Accounting sequence (13 steps):
1. Apply all Domain Action stat changes queued this season.
2. Apply Military losses from unit destruction (BG timing — queued from Phase 4).
3. Thread Debt tokens: apply +1 Ob to next Thread operation in affected territories.
4. Institutional Pressure: check all advancement conditions; advance if triggered.
5. Restoration pre-check: can Restoration win this season? (5 Presence in 5 non-adjacent territories, held 2 consecutive seasons, RS ≥ 1)
6. Rendering Stability: apply all RS changes queued this season (Thread ops, Niflhel Harvest, substrate events).
7. Theocracy Counter: apply TC changes; check thresholds (C-01 through C-05).
8. Queued cascade overflow effects (beyond Cascade Depth Cap from Phase 4).
9. Stability checks: any faction at Stability 0 enters Collapse.
10. Prosperity: Halvardshelm Breadbasket (+1 if uncontested). Territory event effects.
11. CP awards (hybrid only): Belief engagement, Mandate Uphold/Compromise.
12. Victory checks: per-faction Deed tokens; shared survival condition; game-end triggers.
13. Cleanup: remove temporary effects, advance round tracker, draw replacement cards.

### Parliament Integrity (PI) Scale Clarification (PP-180, resolves B-01)
PI uses scale 0–10 (not 0–100). PI 5 = functional parliament; PI 0 = dissolved.
All other clocks (TC, RS, IP) use scale 0–100.
Reference materials must display PI with its 0–10 range explicitly to avoid confusion with 0–100 tracks.

### Intel Advancement Simplification (PP-180, resolves B-02)
Replaces fractional +0.25 rule (PP-173).
**New rule:** Each faction maintains an Intel Advancement Counter (0–3) on their faction mat.
Each season with at least 1 successful Intel or Quiet Network order: Counter +1.
When Counter reaches 4: Intel stat +1, Counter resets to 0.
Rate unchanged (~8 successful seasons to advance 1 point). No fractional tracking required.

### Church Excommunication Ob Cap (PP-180, resolves C-02)
Excommunication Ob = min(target Mandate, 4). Maximum Ob 4 regardless of target Mandate.
Previously: Ob = target Mandate (could reach 5 vs Crown at full strength).
At Ob 4, Church 5D: P(Success) ≈ 9%. Uncommon but possible. Represents: even a fully mandated Crown leader can be publicly challenged by the Church — the institutional weight of the papacy is real even against a strong king.
Church Excommunication Overwhelming at Ob 4 (needs net ≥ 8 from 5D): P ≈ 0.3%. Effectively removed under PP-179 — acceptable, Overwhelming effects are bonus.

### Drawn Battle Rule (PP-180, resolves GAP-BG-02)
When both sides achieve equal net successes in battle:
Stalemate. Both sides: Cohesion −1. No territorial change. Neither side may re-engage in the same territory this season (units hold ground; orders are spent).
If both sides are at Cohesion 0 after the stalemate: both units destroyed simultaneously. Territory becomes uncontrolled.

### Crown Policy Instrument — Defined (PP-180, resolves GAP-BG-03)
The Crown Policy Instrument is the Crown's once-per-season bonus political action (no card required, separate from card hand).
Activation: Crown Mandate ≥ 4. Cannot use the same Policy two consecutive seasons.
Available Policies: see Crown Policy Instruments table (in stage_bg_proposal_v02.md B5).
Resolution order: Policy → Hafenmark Opposition (if Parliamentary Manoeuvre) → Censor card (if in play).
This is printed on the Crown faction reference card.

### Co-Movement VTM Effects at Cap (PP-180, resolves GAP-BG-04)
When a Co-Movement card would advance VTM but VTM is already at maximum (5) or the once-per-season cap has been reached:
Convert: +1D to Varfell's next Tribune order in any territory (the Thread signature that would have advanced VTM instead sharpens Vaynard's tactical awareness).

### Restoration: Community Organizing vs Community Weaving Split (PP-180, resolves GAP-BG-06)
Two distinct action types within Restoration Presence system:
**Community Organizing (Praetor card, rendered-world):**
- Move Presence markers, build non-Thread Projects (Fortification, Diplomatic Mission), recruit.
- No Thread operation. No co-movement card drawn. Does NOT trigger Church Attention Pool.
- Roll: Influence vs Ob 2.

**Community Weaving (Pontifex card, Thread operation):**
- RS restoration, Einhir Memory Recovery.
- Requires practitioner Presence marker in territory.
- Produces full co-movement (card drawn). DOES trigger Attention Pool +2.
- Roll: Influence vs Ob = (100 − RS) ÷ 20 (round up, min Ob 1).

### Thread Debt Cross-Mode Hybrid Rule (PP-180, resolves G-01)
In hybrid mode, when a Player Character performs a Thread operation:
1. Apply TTRPG Thread Debt rules (personal: +1 Ob to next personal Thread operation in that territory).
2. Also place 1 BG Thread Debt token in that territory for board-scale effect (+1 Ob to next faction Thread order there).
These are additive and independent. The personal cost (TTRPG) and institutional cost (BG token) both apply.
Game Master applies at Cascade phase: "This practitioner's operation has left a substrate mark that other factions' Thread activity will feel."
