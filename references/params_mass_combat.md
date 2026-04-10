<!-- version: v0.14+design-ST7-R4-PP235 | sources: designs/mass_combat/mass_battle_v3.md (v4.4, PP-106) | last_updated: 2026-04-03 -->
<!-- PATCHES APPLIED: PP-086-088, PP-091-092; ST-MB-01–10; ED-037/038; Altonian provisional; ED-050 Option D; PP-191 (Lock phase); PP-192 (×3 RS multiplier); PP-222, PP-224, PP-225, PP-227, PP-229, PP-231 (SIM-X-22 provisional) -->
<!-- PP-232: Unit stats renamed (Strength→Size, Combat Power→Power, Cohesion→Discipline, Coherence Rating/Command Rating→Command); -->
<!--         Power derived from Size; damage formula references updated. -->
<!-- PP-233: Unit combat formula established. Pool = min(Size,Command)+Command. -->
<!--         Health per Size = min(Discipline,Command)+DR. Total Health = Size×H. -->
<!--         Damage per success = 1+Power. Size after = ⌊remaining Health÷H⌋. -->
<!--         Damage simultaneous. Size loss only reduces pool when Size>Command. -->
<!-- PHASE STRUCTURE: 7 phases. Thread split: offensive Phase 4, support Phase 6. All damage simultaneous Phase 6 Step 1. -->
<!-- mass_battle_v3.md is a design proposal. Values marked [COMPILED] are from stage8; [PROPOSAL] from v3. -->
<!-- STALE CHECK: Verify [COMPILED] values against current ruleset; verify [PROPOSAL] against compiled stage8 update. -->

# params_mass_combat.md — Mass Battle (v3)



## Battle Plan Templates (PP-235)
Phase 1: select one battle plan covering all units. Individual unit orders derived from plan. General may override one unit per turn with a Command check (TN 7, Ob 1; failure = unit follows plan).

| Plan | All Units Do |
|------|-------------|
| Advance | Engage nearest enemy; Aggressive formation |
| Hold | Defend position; Defensive formation |
| Pincer | 2 units engage front, 1 flanks |
| Withdraw | Orderly retreat; rear unit covers |
| Screen | Ranged units fire; melee holds line |

## BATTLE TURN PHASE STRUCTURE (7 phases, revised 2026-04-02)

| Phase | Name | Content |
|-------|------|---------|
| 1 | Strategy Declaration | Formations, tactics declared (simultaneous, secret). Thread intent declared at Phase 4 start, not Phase 1. (PP-235) |
| 2 | Volley | Projectile fire. Damage recorded, not applied. TN 6 [PROVISIONAL]. |
| 3 | Manoeuvre | Movement by speed. Reserve commitments. |
| 4 | Offensive Thread | Dissolution, Pulling, Locking. Practitioner-only. Skipped if no practitioner present. BG: always skipped. |
| 5 | Engagement | Pool split, roll, damage recorded. Max 3 simultaneous (TTRPG). |
| 6 | Cascade | Step 1: ALL damage applied simultaneously (Volley+Thread+Engagement). Step 2: Discipline checks. Step 3: Morale checks. Step 4: General action (Rally/Support Thread/Personal combat). Step 5: Support Thread Leap resolves. |
| 7 | Reform | Discipline restore, Morale +1, sub-unit merge for non-engaged units. |


## Phase Consolidation — 5-Phase Structure (PP-235)
For reduced cognitive load, the 7-phase structure may be run as 5 phases:

| Phase | Combines | Content |
|-------|----------|---------|
| 1 | Strategy Declaration | Battle plan selection + overrides |
| 2 | Ranged + Movement | Volley fires, then movement resolves (old Phases 2+3) |
| 3 | Thread | Offensive Thread operations (old Phase 4). Declared here, not Phase 1. |
| 4 | Engagement + Cascade | Pool split, roll, ALL damage applied (Volley+Thread+Engagement). Discipline/Morale checks. Rally/Support. (old Phases 5+6) |
| 5 | Reform | Discipline restore, Morale +1, sub-unit merge (old Phase 7) |

Damage simultaneity preserved: all sources resolve together at Phase 4 end. The 7-phase structure remains available as the full-detail reference.

Damage simultaneity: Effective Power for Phase 5 calculated from Size as of Phase 3 end. Phase 4 Thread effects do not reduce Size before Phase 5 — all applied together at Phase 6 Step 1.
> **Lock phase assignment in mass combat (PP-191):** [PROVISIONAL] Offensive Lock (targeting enemy formation) = Phase 4; declared at Phase 1 as "offensive." Support Lock (stabilising own formation) = Phase 6 Step 5; declared at Phase 1 as "support." If undeclared: defaults to Phase 6. A practitioner may not perform both Offensive and Support Lock in the same battle turn.


## Core Formula (PP-233)

### Definitions
| Term | Value |
|------|-------|
| Effective Size contribution to pool | min(Size, Command) |
| Effective Discipline contribution to Health | min(Discipline, Command) |
| Health per Size (H) | min(Discipline, Command) + DR |
| Total Health | Size × H |
| Pool | min(Size, Command) + Command |
| Damage per success | 1 + Power |
| Damage dealt | successes × (1 + Power) |
| Size after round | ⌊ remaining Health ÷ H ⌋ |
| Destroyed | Size = 0 |

### Key rules
- **Command caps both Size and Discipline contributions** — to pool and to Health respectively. Full Size still counts for total Health.
- **Pool = min(Size, Command) + Command.** A Size 2 Command 5 unit rolls 7D. Size loss only reduces the pool when Size > Command.
- **Damage is simultaneous.** Both sides deal and receive damage before Size is recalculated. A unit destroyed this round still delivers its outgoing damage.
- **H is fixed for the unit** (Discipline and DR don't change mid-battle). Current Size = ⌊ remaining Health ÷ H ⌋.

### Worked example
**Group 1:** Size 5, Command 5, Discipline 5, Power 3 (Heavy Infantry), DR 2
- Pool = min(5,5)+5 = 10D
- H = min(5,5)+2 = 7
- Total Health = 5×7 = 35
- Damage/success = 1+3 = 4

**Group 2:** Size 6, Command 3, Discipline 3, Power 1 (Light Infantry), DR 0
- Pool = min(6,3)+3 = 6D  ← Size capped at Command
- H = min(3,3)+0 = 3
- Total Health = 6×3 = 18  ← full Size used
- Damage/success = 1+1 = 2

**Round (4 successes G1, 5 successes G2 — simultaneous):**
| | Group 1 | Group 2 |
|---|---|---|
| Damage dealt | 4×4 = 16 | 5×2 = 10 |
| Incoming | 10 | 16 |
| Health after | 25 | 2 |
| Size after | ⌊25÷7⌋ = **3** | ⌊2÷3⌋ = **0 — destroyed** |

Group 2 is destroyed but their 10 damage resolves first (simultaneous). Group 1 drops Size 5→3.

## Unit Stats (1–7 unless noted)
| Stat | Description |
|------|-------------|
| Size | Headcount/health pool. At 0: destroyed. |
| Power | Dice pool ceiling. Derived from Size. |
| Discipline | Organisational integrity (1–7). |
| Morale | Rout threshold (1–7). |
| Speed | Slow / Standard / Fast |
| Weapon Type | Inherits personal combat table [COMPILED] |
| Armour Tier | Inherits personal combat DR table [COMPILED] |

## Power Tier Reference [PROPOSAL]
| Power | Tier |
|----|------|
| 1 | Levy |
| 2 | Militia |
| 3 | Professional |
| 4 | Veteran |
| 5 | Elite |
| 6–7 | Exceptional/Peerless |

## Faction Military → Unit Quality [PROPOSAL]
| Military | Max Power | Starting Discipline ceiling |
|----------|--------|--------------------------|
| 1 | 1 | 2 |
| 2 | 2 | 3 |
| 3 | 3 | 4 |
| 4 | 4 | 5 |
| 5 | 5 | 6 |
| 6 | 6 | 7 |
| 7 | 7 | 7 |

## Command [PROPOSAL] (PP-232)
Command = ⌈(Charisma + Cognition) ÷ 2⌉
Governs: sub-unit limit (max = Command; TTRPG hard cap 3); Discipline ceiling; Morale floor (= 1 while general present); tactic execution (Command dice vs Ob).
Command = 1: cannot restore Discipline to any unit — all degradation permanent for that battle.

## Battle Phases (TTRPG) — SUPERSEDED
See §BATTLE TURN PHASE STRUCTURE above (7 phases, ED-050 Option D). The prior 5-phase structure is obsolete.

## Discipline Degradation (Deterministic) [PROPOSAL] (PP-232, PP-251, PP-502)
Fires at Phase 6 Step 2 when BOTH: (1) total Size lost this turn > Discipline AND (2) this unit's loss > opposing unit's loss by ≥1. Symmetric losses do not trigger. [PROVISIONAL]
| Discipline | Power penalty |
|----------|-----------|
| 5–7 | None |
| 3–4 | −1D |
| 1–2 | −2D |
| 0 | Formation broken; cannot attack; Reform or rout |

Restoration: Reform Phase only (not engaged), +1 Discipline, Command ≥ current Discipline + 1.

## Morale Degradation Triggers [PROPOSAL]
| Trigger | Change |
|---------|--------|
| Size < 50% max | −1 |
| Size < 25% max | −1 additional |
| Discipline broken this turn | −1 |
| Allied unit routed in same zone | −1 |
| General incapacitated | −1 |
| General killed | −2 (not subject to phase cap) |
| Flanked and lost exchange | −1 |
| Idle 2+ consecutive turns | −1 |

Cap: −3 per Cascade Phase (general death separate and uncapped).
Floor: 1 while general present. At 0: rout.
Rout contagion: −1 Morale to adjacent units; secondary loss cannot cascade to rout until next turn.

## DR Table — Mass Combat (PP-104: Projectile split into 4 categories)

### Melee weapons
| Armour | LC | HC | LB | HB |
|--------|----|----|----|----|
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

### Projectile weapons (mass combat only — PP-104)
| Armour | LP (arrows) | HP (bolts) | LBl (sling) | HBl (siege) |
|--------|------------|------------|-------------|------------|
| None | 0 | 0 | 0 | 0 |
| Light | 1 | 1 | 2 | 0 |
| Medium | 4 | 3 | 4 | 1 |
| Heavy | 7 | 5 | 6 | 2 |

LP = Light Pierce (arrows). HP = Heavy Pierce (bolts). LBl = Light Blunt (sling). HBl = Heavy Blunt Siege.
*[PP-196 — confirmed: LP/HP vs None=0 is correct (net hits only, no DR reduction needed); LBl vs Light=2 reflects blunt trauma advantage vs light armour]*

### Weapon Effectiveness (combined)
| Attacker | vs None | vs Light | vs Medium | vs Heavy |
|----------|---------|----------|-----------|---------|
| LightCut | ✓ | ✗ | ✗ | ✗ |
| HeavyCut | ✓✓ | ✓✓ | ✓ | ✗ |
| LightBlunt | ✓ | ✗ | ✗ | ✗ |
| HeavyBlunt | ✓✓ | ✓✓ | ✓✓ | ✓✓ |
| Bow (LP) | ✓ | ✗ | ✗ | ✗ |
| HP (bolts) | ✓✓ | ✓✓ | ✓ | ✗ |
| Sling clay | ✓ | ✗ | ✗ | ✗ |
| Sling rock | ✓ | ✓ | ✗ | ✗ |
| Sling metal | ✓✓ | ✓✓ | ✓ | ✗ |
| Sling lead | ✓✓ | ✓✓ | ✓✓ | ✗ |
| HBl (siege) | ✓✓ | ✓✓ | ✓✓ | ✓✓ |

HeavyBlunt and HBl are the only classes effective vs Heavy armour.

**Artillery sight-line rule (PP-106):** HBl units require clear line of sight to target.
A unit in Line formation between Artillery and target blocks the shot (target is in the
firing unit's dead zone). Artillery must target units with unobstructed paths — typically
units in the same zone or flanking positions. This creates the primary counter to Artillery:
block sight-lines with front-line formations; flank to reach Artillery directly.

## Battle Scale [PROPOSAL]
| Scale | 1 Size ≈ | Thread Thread Sensitivity minimum |
|-------|-------------|-------------------|
| Skirmish | ~10 soldiers | 30+ |
| Company | ~100 soldiers | 30+ |
| Battle | ~500 soldiers | 50+ |
| Campaign | ~1,000 soldiers | 50+ |
| War | ~5,000 soldiers | 70+ |



## Volley Phase Pool (PP-503) [PROVISIONAL]
Volley Phase pool = Power stat (1–7) rolled at TN 6. NOT the engagement pool formula (PP-233). Ranged output is unit-quality-based, not Command-based.

## Mass Battle RS Multiplier (PP-192, PP-225) [PROVISIONAL]
All RS costs AND gains from Thread operations in mass battle ×3 (PP-225). Applied after degree table resolution. Coherence costs NOT multiplied. RS ceiling (100) and seasonal cap (±10) still apply.
| Op | Normal RS (Success) | Mass Battle RS (×3) |
|----|--------------------|-----------------------|
| Pulling (failure) | −2 | −6 |
| Locking (success) | −1 | −3 |
| Dissolution (success) | −5 | −15 |
| Dissolution (failure) | −8 | −24 |
| Mending (success) | +1 | +3 |
| Mending (overwhelming) | +2 | +6 |
| Weaving Overwhelming (Relational+) | +1 | +3 |
Source: ST-TW-03 design note + PP-225 (gains also ×3).

## Thread Integration [COMPILED — stage11]

> **Mass battle Dissolution — campaign impact warning (PP-201):** [PROVISIONAL] Dissolution at mass battle scale is a **campaign-altering decision**, not a tactical one. E[RS per Dissolution attempt] = −18.4 at TS 70 (9D Spirit+History, Ob5). Three Dissolution attempts in a single battle produce E[RS after] ≈ 6 (Critical band) from a campaign-starting RS 60. A single Dissolution Failure when RS < 24 triggers the Rupture immediately. **Before a practitioner declares offensive Dissolution in mass battle:** the GM should confirm the table understands this is a world-stakes action. Dissolution in mass battle is the Einhir scale of operation. It may win a battle while ending a campaign. Weaving and Mending are the only RS-neutral or RS-positive mass battle Thread operations on average. Lock and Pull are risky (E −3 to −6 RS per attempt). Dissolution is in a category of its own.


> **RS<24 mass battle Rupture threshold (PP-204):** [PROVISIONAL] If RS is below 24 when a mass battle Thread operation is declared, the GM must inform the declaring practitioner before the roll: a Dissolution Failure at this RS level triggers the Rupture immediately (Dissolution Failure = −24 RS via ×3 multiplier; RS floor = 0 = Rupture). This is not a mechanic restriction — the practitioner may still attempt the operation. It is mandatory table information. At RS 0–23: any mass battle Dissolution Failure ends the campaign in the Rupture. Partial and worse results on Dissolution (−18 RS and −24 RS respectively) also carry Rupture risk at RS < 18 and RS < 25 respectively. Print this threshold on the mass battle Thread tracking sheet.

Combat Thread ops (Dissolution, offensive Pulling): Phase 2. Support ops (Weave, Mend, Lock, non-offensive Pulling): Phase 5. Both declared Phase 1.
Mass → Personal: Personal Action available at Phase 5 (Priority 8). Limit: 1 exchange/battle turn. General's Phase 5 consumed by personal combat (Command suspended).


## Single Operation Per Battle Turn — Mass Scale (PP-235)
In mass combat, a practitioner gets exactly 1 Thread operation per battle turn. No multi-round contact window at mass battle scale. Focus determines Leap success probability but does not extend the contact window at mass scale.

Rationale: mass battle turns represent longer timeframes. A single operation at mass scale represents sustained effort across the engagement phase. Full contact-window mechanics apply at personal scale only.


## Command Suspension During Thread Contact (PP-235)
While a practitioner-general is in Thread contact (Phase 4), their Command bonus is suspended. Sub-units follow automation:
1. Engage nearest enemy unit in same zone
2. If no enemy in zone: hold position
3. Default pool split: 50/50 (round Offence down)
4. Defensive formation if Size < 50%

Extends PP-111 (Command suspension during personal combat). Thematic: suspended rendering = cannot command.

## Command Per Sub-Unit (PP-504) [PROVISIONAL]
Full Command applies to each commanded sub-unit's pool independently. Not divided. Sub-unit limit = Command value (TTRPG cap: 3). §A.8 splitting guidance under revision (ED-358).

## Key Design Axiom
Generalship dominates. Command asymmetry is intentional. Command=7 vs Command=1 general: near-certain outcome before dice rolled.


## RESOLVED PARAMS GAPS (PP-104, 2026-04-02)

### Pool Split — Phase 5 Engagement (PARAMS-GAP-04 resolved)
Declared in Phase 1. Any allocation valid, min 1D each side.
Default: ½ pool to Offence (round down), remainder Defence. [PROVISIONAL]

### Damage Formula — unit Strength loss (PARAMS-GAP-05 resolved)
Size loss = max(0, net hits + Dmg Mod − DR)
Dmg Mod from unit table below. *[PP-194 — confirmed]*

| Unit | Weapon | Dmg Mod |
|------|--------|---------|
| Levy | LightCut | +1 |
| Light Infantry | LightCut | +2 |
| Heavy Infantry | HeavyCut | +4 |
| Cavalry | HeavyCut | +5 |
| Piercing — Archer | Piercing/Bow | +0 |
| Piercing — Crossbow | Piercing/Crossbow | +0 base (+1 vs med+heavy post-DR) |
| Blunt — Throwing | Blunt/Throw | +1 |
| Blunt — Sling | Blunt/Sling | clay+0 / rock+1 / metal+2 / lead+3 vs med+heavy (−2D pool) |
| Artillery | HBl | +3 |
| Knights Templar | HeavyBlunt | +5 |


## Ranged DR Table (Volley Phase) — PP-188
Scaled (÷2 rounded up) from personal combat DR. Crossbow post-DR bonus applied after.
| Armour | vs Piercing | vs Blunt |
|--------|------------|---------|
| None | 0 | 0 |
| Light | 1 | 1 |
| Medium | 2 | 1 |
| Heavy | 3 | 2 |

Crossbow post-DR bonus (if net hits > 0): +1 vs Medium and Heavy. Scaled ÷2 from personal +2 (PP-189).
Sling: effective CP −2D; ammo modifier per unit table above.

HBl (Artillery/siege): uses PP-091 Bombard (flat Size damage). Not subject to Volley DR formula. Artillery is a separate unit type from HBl lead-sling infantry units.

Bow/LP (archer) unit effectiveness at CP4 (Veteran): vs None=1.6, vs Light=0, vs Med=0, vs Heavy=0. [PP-189: Dmg Mod +0; net successes only vs unarmoured. Re-sim pending.]
Crossbow/HP unit effectiveness at CP4: vs None=1.6, vs Light=0.6, vs Med=0.6, vs Heavy=0. [PP-189: post-DR +1 vs med+heavy; re-sim pending.]
HBl (lead sling) unit effectiveness at CP4: vs None=1.6, vs Light=1.6, vs Med=0.6, vs Heavy=0.6.
LBl remains anti-levy at mass scale (same DR as LP after scaling).

### BG Battle Partial outcome (PARAMS-GAP-06-MC resolved)
Margin = |attacker net − defender net|.
- Margin ≥ 2, attacker higher → Win: territory captured, Defender Military −1
- Margin ≤ 1 (either direction) → Partial: no territory change, Attacker Stability −1
- Margin ≥ 2, defender higher → Lose: no territory change, Attacker Military −1
[PROVISIONAL — ED-063: confirm Partial threshold and Stability cost]


<!-- patches: PP-173 (ranged DR split, HBl personal reference), PP-175 (mass combat DR scaled ÷2 provisional) -->


## SIM-X-22 Provisional Patches (PP-222, PP-224, PP-227, PP-229, PP-231)

### PP-222: Offensive Lock Blocks Cohesion Degradation [PROVISIONAL]
Offensive Lock (Phase 4) on a formation thread blocks Discipline degradation checks on the locked unit for the lock duration. The formation is frozen — it cannot degrade organisationally while the thread configuration holds it in place. ED-122 pending confirmation.

### PP-224: Diagnosis+Leap Collapse in Mass Battle [PROVISIONAL]
In mass battle, Diagnosis and Leap collapse to a single Phase 4 action (not 2 separate rounds). The PP-190 2-round rule (Diagnosis Round N, Leap Round N+1) applies to personal combat only. Mass battle tempo requires single-phase resolution. ED-124 pending confirmation.

### PP-227: Paradox Window — No Unit Stat Effect During Battle [PROVISIONAL]
A paradox window (P-22) has no mechanical effect on unit stats during the active battle turn. Pre-displacement values are used for all Phase 5 calculations. Displaced values apply on window auto-resolution at end of battle turn (Phase 7 Reform or later). ED-121 pending confirmation.

### PP-229: Contact Window Suspended During Zoom In [PROVISIONAL]
When a General triggers Zoom In (personal exchange during Phase 6 Step 4), any active Thread contact window is suspended — not consumed. Contact rounds do not tick during the personal exchange sub-scene. On return to mass scale, remaining contact rounds resume.

### PP-231: Cohesion Degradation = Asymmetry Mechanic [PROVISIONAL]
Discipline degradation is an asymmetry mechanic, not an attrition mechanic. It triggers only when: (a) Power asymmetry exists (stronger unit overwhelms weaker), (b) Thread-assisted Size loss creates sudden imbalance, or (c) Artillery bombardment. Symmetric engagements between equal-Power units do not trigger Discipline degradation — they produce attrition (Size loss) only. GM guidance note.

<!-- patch_history: references/params_mass_combat_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->
## LBl (Sling) — Prepared Defence Exception (ED-065 resolved — provisional)
LBl (sling) attacks ignore the Prepared Defence bonus (+0 DR from Prepared Defence when targeted by LBl). Sling stones are concussive/indirect and bypass shield-angling. LP, HP, HBl: Prepared Defence applies normally. [PROVISIONAL]

## Artillery Morale Cascade Cap (ED-066 resolved — provisional)
The −3 Morale cap per Cascade Phase applies as a total across all non-general sources. Multiple simultaneous HBl artillery impacts count together toward the −3 cap, not separately. Example: 3 Artillery units each destroy a unit → triggers 3× −1 Morale → capped at −3 total, not −3 each. [PROVISIONAL]

## Commander Bonus Formulas — Consolidated (ED-033 resolved — provisional)
| Context | Formula | Notes |
|---------|---------|-------|
| TTRPG mass combat | Command = ⌈(Charisma + Cognition) ÷ 2⌉ | Per params_mass_combat (PP-232) |
| BG battle resolution | Commander bonus = faction Military ÷ 3, round down (max +2D) | Per §B.3 |
| Hybrid Zoom In | Use TTRPG CR for TTRPG-layer actions; BG commander bonus for BG-layer accounting | No conversion between them |
[PROVISIONAL]

## Volley TN (ED-037 resolved — provisional)
Volley phase uses TN 6 (not TN 7). Rationale: ranged advantage before armour engagement; represents favourable conditions (distance, preparation). [PROVISIONAL — confirmed from prior provisional]
## Commander Bonus (PP-190)
Formula: faction Military ÷ 3, round down. Min 0, max +2D. Applies to BG mode. TTRPG uses Command = ⌈(Cha+Cog)÷2⌉ (PP-232). See consolidated table above.
## Altonian Invasion Units (PP-193, ED-036 resolved 2026-04-03)
Generated from Altonian Military ~5 (foreign professional standing army; above Crown/Church 4).
[ED-036 resolved 2026-04-03] Stats confirmed: Vanguard Str5 CP4 Coh4 Mor5 HeavyCut Medium. Elite Guard Str4 CP5 Coh5 Mor5 HeavyCut Heavy. Thread Corps Str3 CP3 Coh4 Mor4 TS40.

| Unit Type | Size | Power | Discipline | Morale | Armour | Weapon | Dmg Mod |
|-----------|----------|----|----------|--------|--------|--------|---------|
| Altonian Heavy Infantry | 4 | 3 | 5 | 5 | Heavy | HeavyCut | +4 |
| Altonian Cavalry | 3 | 4 | 4 | 6 | Medium | HeavyCut | +5 |
| Altonian Crossbow | 3 | 2 | 4 | 4 | Light | HP | +0/+2 vs med+heavy |
| Altonian Artillery | 2 | 2 | 3 | 4 | None | HBl | +3 |

Commander bonus: Military 5 → +1D (5÷3=1, round down).
Deployment trigger: Institutional Pressure ≥ 75 (CLOCK-EDIT-01).
## LBl vs LP Dominance (PP-197 — ED-065 resolved)
LBl (sling) outperforms LP (arrows) only vs Light armour (+2 vs +1). LP equals or exceeds LBl at Medium and Heavy. Distinction is intentional: slings = anti-light-infantry; bows = anti-armoured. No change needed.
## BG Thread Operations (PP-200 — ED-080)
BG mode: Thread operations (Phase 4 Offensive, Phase 6 Support) are always skipped. No Coherence cost applies in BG — Thread ops do not occur at board scale. This is intentional (P-01: Thread operates below BG abstraction layer). Resolves ED-080.
## Planning Phase Time (PP-202 — ED-083)
Finding from bg_v05 simulation: Phase 1 planning ~8 min/player with reference cards; ~12-15 min without. Recommendation: pre-assign Seasonal Priority order on faction reference cards to reduce deliberation. No mechanical change required.

## HP (Crossbow) Reload — Mass Combat Scale (ED-094 resolved 2026-04-03)
HP crossbow units fire every Volley Phase at mass combat scale.
Individual reload cycle is abstracted — units stagger reloads historically.
Individual reload applies only in personal combat.

## Faction Tactic Cards — Confirmed (ED-019 resolved 2026-04-03)
2 unique tactic cards per faction. Confirmed:

**Crown:**
- Royal Authority: all Crown units +1 Martial this battle.
- Diplomatic Shield: no Stability loss from Partial outcome this season.

**Church:**
- Templar Vanguard: Knights Templar units +2 Discipline this battle.
- Excommunication Threat: opposing faction −1D all Domain Actions next season if Church Mandate ≥ 4.

**Remaining factions (Varfell, Hafenmark, Löwenritter, Revolution):** TBD — pending editorial design.

## PP-240 — Mutual total destruction
All units both sides to 0 simultaneously: draw. No territory change. Both factions Stability check Ob 1 at Accounting.

## PP-241 — Reform condition
Reform requires: Command ≥ current Discipline + 1 AND Command ≥ 2. Command=1 generals cannot reform any unit regardless of Discipline value.

## PP-245 — TTRPG Dmg Mod (resolves SIM-DEBT-05)
TTRPG Dmg Mod = ⌈BG Dmg Mod ÷ 2⌉.
| Unit | TTRPG Dmg Mod |
|------|--------------|
| Levy | +1 |
| Light Infantry | +1 |
| Heavy Infantry | +2 |
| Cavalry | +3 |
| Archer/Crossbow | +0 (+1 vs med/heavy post-DR for crossbow) |
| Sling | by ammo (−2D) |
| Artillery | +2 |
| Knights Templar | +3 |

## PP-249 — Coherence → Command: no penalty
Dissonance impairs Thread operations only. No Coherence penalty on Command tactic rolls.

## PP-250 — Zoom In mid-Phase-5 deferral fix
Mid-phase Zoom In fires at next legal phase-lock point. Phase-5 trigger → After Phase 6 Step 1 (not end-of-Phase-5).

## PP-256 — Feigned Retreat Discipline check Ob
Pursuing-side Discipline check = Ob 1. P(hold | Discipline 4) ≈ 87%. P(hold | Discipline 1) ≈ 40%.

## ED-167 provisional — CF wound on Zoom Out
CF wound during Zoom In → +1 Ob to that commander's BG tactic rolls for remainder of current battle.

## ED-170 provisional — Coherence recovery in multi-day battle
1 Coherence/night of rest (no Thread ops). Single-day battle: no in-battle Coherence recovery.

## PP-273 — Mass battle minimum pool
1 die minimum after all penalties. Discipline 0 = Formation Break (no attack). Command=0 general death: units at 1 die minimum.

## PP-282 — STRUCK (duplicate of PP-193 Altonian block above)
> Superseded. PP-193 §Altonian Invasion Units is the canonical stat block.
> PP-282 was a duplicate created in a concurrent session. Struck 2026-04-04.

## PP-283 — Tactic cards confirmed canonical
All faction tactic cards in mass_battle_v3 §B.4 confirmed as canonical defaults.

## ED-087 Resolution (PP-300) — BG Ranged Faction Military Modifier
No BG Military modifier for ranged specialisation. Ranged capacity abstracted into unit Power and DR at unit design stage.
Consistent with mass combat abstraction principle. No patch needed.


## ED-094–098 Resolution (PP-301) — Mass Combat Ranged Consolidated [FLAGGED]
**ED-094 Crossbow reload:** HP unit fires every other Phase 5 as a unit. Binary ready/reloading marker.
**ED-095 Archers in melee:** Power −1 in Phase 5 if caught in melee (improvised, no weapon advantage). TN 7 unchanged.
**ED-096 Ranged DR scaling:** Personal DR values apply 1:1 at mass scale.
**ED-097 HP effective Power:** Power = 2 when ready; Power = 0 when reloading. Reload-cycle abstraction.
**ED-098 Cover timing:** Must declare in Phase 1. Late declaration: −1D penalty to covered unit's Phase 5 pool.
[FLAGGED: confirm reload binary marker implementation and Phase 1 declaration requirement.]


## ED-121–125 Resolution (PP-305) — Mass Battle Thread Definitions [FLAGGED]
**ED-121 Paradox window scene:** Battle-turn = scene. PP-223 confirmed.
**ED-122 Offensive Lock:** PP-222 confirmed — blocks Discipline degradation on locked unit for lock duration.
**ED-123 RS thresholds:** Check at Phase 7 Reform (end of each battle-turn). Coherence-0 leakage fires once per turn.
**ED-124 Diagnosis+Leap collapse:** PP-224 confirmed — single Phase 4 action at mass scale.
**ED-125 Hybrid Strategic Phase paradox windows:** Windows from Personal Phase persist into Strategic Phase. Strategic Phase generates no new windows.
[FLAGGED: confirm all five rulings before mass-battle Thread compilation.]


## ED-126 Resolution (PP-306) — FR in Mass Battle Failure Rate
98.3% failure rate for FR ops (Lock/Dissolution) at TS70 Relational in mass battle: confirmed design intent.
Mass battle is hostile to large-scale Thread intervention. Practitioners should use Object-scale operations.
Failure rate is correct signal. No patch needed.


## ED-140 Resolution (PP-320) — Discipline Degradation Asymmetry [FLAGGED]
Discipline degradation trigger (PP-248) now requires BOTH:
1. Total Size lost this turn > Discipline, AND
2. Power asymmetry (attacking unit Power > defending unit Power) OR Thread/artillery caused Size loss.
Symmetric engagements produce attrition (Size loss) only — no Discipline degradation.
[FLAGGED: confirm asymmetry threshold — strict Power > Power or Power difference ≥ 2?]


## ED-167–168 Resolution (PP-333) — Zoom Out CF Consequences [FLAGGED]
**ED-167 CF wound on Zoom Out:** Wound persists. BG consequence: PC's faction loses faction bonus dice (+1D per ED-075) for that season.
**ED-168 CF killed between Zoom Ins:** PC-B's Zoom In proceeds without PC-A. PC-A-dependent faction actions reassigned to NPC pool. PC death is final in TTRPG; BG reflects through permanent faction bonus loss.
[FLAGGED: confirm wound persistence and faction bonus mechanics before Hybrid compilation.]


## ED-170 Resolution (PP-334) — Coherence Recovery in Multi-Day Battle
1 Coherence per full overnight rest (min 6 hours, no Thread ops during rest).
No in-battle Coherence recovery between battle-turns within same day.

## Discipline Degradation — Asymmetry Precondition (PP-251)
UPDATED TRIGGER (supersedes prior formula):
Discipline check fires when BOTH conditions met:
  (1) Unit's Size loss > Discipline threshold in this Engagement Phase
  (2) Unit's loss exceeds opposing unit's loss in same Engagement Phase by ≥ 1
Symmetric engagements (equal losses both sides) do NOT trigger Discipline check.
Rationale: PP-231 intent — mutual-cost exchanges should not produce cascade.

## Shield Wall +2D Def Scope (PP-500) [PROVISIONAL]
Shield Wall +2D Def applies to all simultaneous defensive pools regardless of engagement direction. Blanket formation modifier — not per-engagement. Unmitigated flanks still benefit from the +2D Def bonus. Eliminates 21% damage differential vs Option B interpretation.

## Thread-Destroyed Unit Phase 5 Participation (PP-505) [PROVISIONAL]
Simultaneous-damage rule governs. A unit reduced to 0 by Phase 4 Thread effects retains
its Phase 3-end Size during Phase 5 Engagement — damage not yet applied. It participates
in Phase 5 normally and is formally removed at Phase 6 Step 1 with all simultaneous damage.
Practitioner gains no "free kill" window — the unit fights back in Phase 5.

## Bilateral General Personal Combat (PP-506) [PROVISIONAL]
If both generals enter personal combat in Phase 5 simultaneously: mass battle continues.
Both armies uncommanded: PP-273 1D minimum, Line formation, no tactics. Each general
re-establishes Command via Ob 2 check Phase 1 of the following turn.
P(re-establish): Cmd=2: 20%, Cmd=3: 34%, Cmd=4: 46%, Cmd=5: 55%, Cmd=6: 62%.
Low-Command generals take significantly longer to re-establish — intended asymmetry.

## Mutual Destruction Stability Check Clarification (PP-507) [PROVISIONAL]
PP-240 Ob 1 Stability check (mutual destruction = draw) REPLACES §A.13 battle-lost
Ob 1 check. A draw produces no loser — battle-lost consequence does not fire.
Each faction takes exactly one Ob 1 check at Accounting.

## Splitting Doctrine (PP-508) [PROVISIONAL]
Splitting is structurally advantageous in most configurations. Simulation matrix (Att Cmd 2-5 vs Def Cmd 2-5):
split dominates concentration by +9% to +45% win-rate. Negligible advantage only when
attacker already near win-rate ceiling (Att Cmd=4-5 vs Def Cmd=2).
Hard counters to splitting: (1) Narrow Pass terrain (1 engagement per side), (2) Feigned
Retreat to disengage and re-concentrate. Matching the split is not an effective counter.
