<!-- version: v0.14-AUD3 | sources: stage6_factions.md (TTRPG), bg_v05 (BG/Hybrid) | last_updated: 2026-04-02 -->
<!-- NOTE: stage6_factions.md is STALE for BG faction mechanics. Use BG column for board game/hybrid. -->
<!-- PP-287 (DA sequential timing), PP-288 (stat cap cost clarification), PP-289 (high-Wealth recovery) -->
<!-- PATCHES APPLIED: PP-167, PP-168; PP-195 (Community Weaving procedure) -->
<!-- STALE CHECK: TTRPG column from v0.14 compiled. BG column from bg_v05 design. -->

# params_factions.md — Factions

## Stats (1–7 scale)
Mandate / Influence / Wealth / Military / Intel / Stability
Seasonal cap: ±2 per stat per season (TTRPG); ±varies (BG — see accounting).

## Starting Stats
| Faction | M (TTRPG) | M (BG) | I | W (TTRPG) | W (BG) | Mil | Int | Sta |
|---------|-----------|--------|---|-----------|--------|-----|-----|-----|
| Crown | 5 | 5 | 5 | 4 | 4 | 4 | — | 4 |
| Church | 5 | 5 | 6 | 5 | 5 | 4 | — | 5 |
| Hafenmark | 4 | 4 | 4 | 5 | 5 | 3 | — | 4 |
| Varfell | 4 | 4 | 4 | 4 | 4 | 4 | — | 4 |
| Guilds | 3 | 3 | 4 | 6 | 6 | 2 | — | 5 |
| Niflhel | — | — | 5 | 4 | 4 | — | — | 4 |
| Restoration Movement | — | 2 | 3/4 | — | 2 | — | — | 3 |
| Löwenritter | — | 3 | 2/3 | — | — | 5/6 | 3 | 5/4 |

Note: Varfell BG Mandate 3/Wealth 3 is intentional (political isolation at game start, not their full institutional depth).

## Clock Starting Values
| Clock | TTRPG | BG (bg_v05 P-32) | Shared Loss |
|-------|-------|-----------------|-------------|
| Theocracy Counter | 0 | 28 | — |
| Rendering Stability | 60 | 72 | Rendering Stability = 0 |
| Institutional Pressure | 20 | 20 | — |
| Public Instability | — | 5 | — |

## Domain Action Rules (TTRPG)
Ob = target faction's relevant stat (1–7 directly, no division).
Attacker bonus dice: own faction's relevant stat if holding faction leadership.
Non-Player Character faction rolls: relevant stat as d10 pool, TN 7.

## Ethical Framework Ob Modifiers
| Condition | Modifier |
|-----------|---------|
| Action aligned with framework | −1 Ob |
| Action contradicts framework | +1 Ob |
| Church only: reveals Thread truth | +2 Ob |

## Leadership Deviation Stability Check Obs
Crown: 2 | Church: 3 | Hafenmark: 2 | Varfell: 2 | Guilds: 2 | Restoration Movement: 2 | Löwenritter: 2

## Unique Actions (TTRPG, from stage6)
| Faction | Action | Roll | Effect |
|---------|--------|------|--------|
| Crown | Royal Decree | Mandate vs Ob 2 | One faction stat ±1 immediate. Consecutive: +1 Ob/season. Cannot target Intel. |
| Church | Excommunication | Mandate vs target Mandate (leader) / Ob 2 (non-leader) | Strips Circles bonus; target faction Mandate −1. Reversal: Grand Debate (5 exchanges) or new Confessor. |
| Church | Theocracy Counter 60 Territorial Seizure | Mandate vs owner's Mandate ÷ 2 (round up, min 1) | Per-territory roll. Success: administrative control. Failure: Mandate −1. |
| Restoration Movement | Community Weaving | Presence markers −1 Ob (base Ob 2) | Mending Mandate prerequisite: Mandate ≥ 1 |
| [Others] | See stage6_factions.md §8.4–8.9 | — | Hafenmark, Varfell, Guilds, Niflhel, Löwenritter unique actions not extracted |


## Nine Political Axes (qualitative — not tracked numerically)
1. Sovereignty: Crown authority vs Church authority
2. Knowledge: Thread truth accessible vs suppressed
3. Legitimacy: Constitutional monarchy vs Theocratic governance
4. Cultural identity: Einhir recovery vs Colonial settlement
5. Economic control: Guild autonomy vs State/Church taxation
6. Military authority: Ducal/Crown vs Templar independence
7. Information: Transparency vs Secrecy
8. External threat: Accommodation vs Resistance to Altonia
9. Ontological: World as it appears vs World is more

## Faction Non-Player Character Trigger Conditions (key)
| Non-Player Character | Trigger | Effect |
|-----|---------|--------|
| Ehrenwall | Coup trigger | Martial Law; Crown Loyalty check |
| Vaynard | TK threshold | Research acceleration |
| Baralta | Theocracy Counter suppression | Church Mandate −1/season while Mandate ≥ 4 |
| Schoenland | Active spoiler | Various faction disruptions |

Rendering Stability ≤ 10 adds +1 to coup/succession trigger check pools.

## Unique Actions — All Factions (PP-168)

### Crown — Royal Decree
Roll: Mandate vs Ob 2. Once per season.
| Degree | Result |
|--------|--------|
| Overwhelming | One faction stat ±1 immediate; consecutive seasons: +1 Ob/season |
| Success | One faction stat ±1 immediate; consecutive seasons: +1 Ob/season |
| Failure | — |
Cannot target Intel. Effect is immediate and unilateral.

### Church — Excommunication
Roll: Mandate vs target Mandate (faction leader) or Ob 2 (non-leader).
| Degree | Result |
|--------|--------|
| Success | Strips target's Circles bonus; target faction Mandate −1 |
| Failure | — |
Reversal: Grand Debate (5 exchanges) or new Confessor appointed.

### Church — TC 60 Territorial Seizure
Trigger: Theocracy Counter (TC) reaches 60. Fires once per territory.
Roll: Mandate vs owner's Mandate ÷ 2 (round up, min 1).
| Degree | Result |
|--------|--------|
| Success | Administrative control of territory. Domain Actions vs Church authority require +2 Ob. Flat Theocracy Counter value fires immediately. |
| Failure | Mandate −1 |
Riskbreaker exposure removes seized territory and prevents re-seizure for one season.

### Hafenmark — Sovereign Authority Doctrine
Roll: Mandate vs Ob 4. Once per campaign arc.
| Degree | Result |
|--------|--------|
| Overwhelming | Theocracy Counter −3; Church Mandate −1; Heresy Investigation blocked this season; +1D social vs Church for the arc |
| Success | Theocracy Counter −2; Church Mandate −1; Heresy Investigation opens (Ob 4 to pursue) |
| Partial | Theocracy Counter −1; Heresy Investigation opens immediately; Church Influence +1 |
| Failure | Theocracy Counter +1; Heresy Investigation immediate; Baralta's Mandate −1 |
TC Suppression: while Baralta's Mandate ≥ 4, Theocracy Counter −1/season. Suppression ends if Mandate < 4 or excommunication (TC +4 immediately).

### Varfell — The Private Collection
Roll: Intel vs Ob 2. Once per season.
| Degree | Result |
|--------|--------|
| Success (choose one) | +2D to one Thread-related Domain Action this season; OR reveal one hidden faction attribute; OR −1 Ob to one Einhir Research action this season |
| Failure | Artefact's Thread signature detected by a practitioner; Church Intel +1D vs Varfell for 1 season; Thread Tension +1 |
Long-term cost: each use: +1 to Vaynard's hidden Thread Sensitivity (TS). At Thread Sensitivity 14+, each use triggers Spirit check TN 7 Ob 1 for a Discovery Event.
Player Character takeover: collection transfers as institutional asset; triggers mandatory Discovery Event for new leader (Spirit TN 7 Ob 1; Success: Thread Knowledge (TK) +1; Failure: Certainty −1, new Belief offered).

### Guilds — Economic Leverage
Trigger: Guild Favour ≥ 5 in target territory (1–7 territory track).
Roll: Wealth vs target faction's Wealth.
| Degree | Result |
|--------|--------|
| Overwhelming | Target loses 1 Wealth + 1 Prosperity in that territory |
| Success | Target faction loses 1 Wealth for 1 season |
| Failure | Guild Favour −1 in that territory |
Cannot target factions in territories where Guild Favour < 5.

### Niflhel — The Quiet Network
Choose mode before rolling. One deployment per season.
**Intelligence mode:** Intel vs target's Intel → Success: learn one hidden faction attribute or one Non-Player Character's active Belief; Overwhelming: learn two.
**Sabotage mode:** Intel vs target's Stability → Success: Stability −1; Failure: operative exposed (Niflhel Intel −1 for 1 season; target gains Grievance Marker).
**Assassination mode:** Intel vs target's Intel +2 → Overwhelming: Non-Player Character eliminated, no evidence; Success: eliminated, evidence trail; Partial: wounded, evidence trail; Failure: operative captured, full exposure, Niflhel Stability −2.
Long-term cost: each Quiet deployment this season: Thread Tension +0.5 (cumulative).

### Restoration Movement — Community Weaving
Roll: Influence vs Ob = Thread Tension ÷ 20 (round up).
Requires: at least one practitioner with Thread Sensitivity (TS) 30+ affiliated with the Restoration Movement.
| Degree | Result |
|--------|--------|
| Overwhelming | Thread Tension −2 |
| Success | Thread Tension −1 |
| Partial | Thread Tension unchanged; Stability −1 |
| Failure | Stability −1; Thread Tension +1 |
Co-Movement Card drawn on every result (P-01 compliance).
Prerequisite: Mandate ≥ 1 for Mending prerequisite (see stage6 §8.8).

### Löwenritter — Martial Law / Coup Trigger
No standard Unique Action roll — Löwenritter action is triggered by Coup Counter reaching 3.
**Coup Counter increments (+1 each):**
- Theocracy Counter reaches 40 while Crown took no action to reduce it that season
- Torben's loyalty reaches 3–2 or lower
- Crown loses 2+ territories in one season without a military response Domain Action
Counter never decrements. Fires at next seasonal accounting once at 3.
**Martial Law effects:** All non-Military Domain Actions in Crown territories require secondary Military check (Löwenritter Military pool, TN 7, Ob 2); failure blocks the action. Persists until players remove it (Influence vs Ob = Löwenritter Military ÷ 2, round up, min Ob 3) or Theocracy Counter drops below 40.
## Mandate Recovery (ED-066b resolved — provisional)
Factions with Mandate < starting value recover +1 Mandate/season when:
- No hostile Domain Action targeting that faction this season
- Stability ≥ 2
Cap: cannot recover above starting Mandate value via this mechanic. [PROVISIONAL]

## Hafenmark Wealth Sink (ED-064b resolved — provisional)
Wealth above 5 may be spent as bonus dice on trade-adjacent Domain Actions:
- 1 Wealth token → +1D on Trade or Diplomacy Domain Action (max +2D per action)
- Token is consumed on spend
[PROVISIONAL]

## Military Stat Change on Unit Destruction (ED-017 resolved — provisional)
When a unit is destroyed in TTRPG mass combat: Faction Military −1 (immediate). Cap: −2 per season from destruction. [PROVISIONAL]

## Military Seasonal Cap (ED-039 resolved — provisional)
Military stat cap: ±2/season from all Domain Actions combined. Hard cap = faction Military rating (cannot exceed starting value +1 via Domain Actions alone). [PROVISIONAL]

## Institutional Mandate Trigger (ED-003 resolved — provisional)
Institutional Mandate fires when:
- Faction Mandate ≥ 4, AND
- A Domain Action directly challenges the faction's core institutional authority:
  Crown: sovereignty or legal authority; Church: spiritual authority or excommunication power;
  Guilds: trade monopoly or taxation; Hafenmark: guild autonomy; Varfell: territorial governance;
  Restoration: community organizing; Löwenritter: military authority.
[PROVISIONAL]

## PC Faction Embedding — BG Layer (ED-075 resolved — provisional)
PCs are always mechanically present in their primary faction between Zoom Ins.
Effect: the PC's faction gains +1D on one Domain Action per season in territories the PC is physically located in (narrative confirmation required). [PROVISIONAL]

## Institutional Mandate — Uphold / Appease (PP-189)
Trigger: Mandate ≥ 4 AND Domain Action directly challenges faction core institutional authority.
| Choice | Timing | Effect | Cost |
|--------|--------|--------|------|
| Uphold | Before roll | Roll proceeds | None |
| Appease | Before roll | Action cancelled | Mandate −1 |
NPC: Appease if Mandate ≥ 4 AND Stability ≤ 3.


## Community Weaving — Procedure (PP-195) [PROVISIONAL]
Revolution Domain Action. Pool: Mandate (as dice) + History, TN 7, Ob 3. Prerequisite: Mandate ≥ 1.
| Degree | RS Effect | Other |
|--------|-----------|-------|
| Overwhelming | RS +2 | Mandate unchanged |
| Success | RS +1 | Mandate unchanged |
| Partial | RS +0 | Wasted action |
| Failure | RS +0 | Mandate −1 |
Frequency: once per season. Consumes 1 Domain Action.
## Simultaneous Catastrophe Rule (PP-199 — ED-077)
If RS=0 AND IP≥80 both trigger in the same Accounting phase:
1. RS=0 resolves first (Shared Loss: game-ending Thread collapse condition).
2. IP≥80 Altonian invasion pressure resolves second.
Both are independent effects. Priority: RS=0 > IP threshold. If RS=0 triggers Shared Loss end condition, IP escalation is moot.
## Reformed Settlement Standing Effect (PP-201 — ED-081)
When Reformed Settlement is in force (Theocracy Counter ≥ 40 and Church has Resisted):
- All Diplomacy Domain Actions targeting Hafenmark: permanent +1 Ob (Church institutional antagonism).
- Effect persists until Theocracy Counter drops below 40 OR Reformed Settlement is withdrawn.
[Source: bg_v05 Cascade Test 2 simulation]

## Restoration Movement — Named NPCs (ED-005 resolved 2026-04-03)
1. **MARET VOSSEN** — Primary contact. Grassroots organiser. TS 0, Charisma 5+, Circles 3+ in working-class networks. Non-practitioner. Full stat block deferred to campaign development.
2. **ALDRIC HANN** — Operational doer. Lower Charisma than Vossen, higher Circles in logistics and street-level networks. Full stat block deferred.

## Riskbreakers — Identity Confirmed (ED-006 resolved 2026-04-03)
Extralegal arm of the Löwenritter. Small-cadre elite consequentialists loyal to Valoria as concept — not to Crown, institution, or faith.
Will go extralegal (blackmail, hostage, theft, murder) when judged necessary for Valoria's survival.
Existence known only to Crown and Lions' Table. Active concealment is core doctrine.
Some members are Thread Practitioners. Operate alone or in small teams; present as ordinary people.
Will not permit Valoria to fall under weak-willed, foreign, or religious rule.
Parallel archetype: Shadow Warriors (Sousou no Frieren).
Individual profiles and stat blocks deferred to campaign development.

---
<!-- PP-236 applied 2026-04-04: Crown covert actions rule -->
<!-- PP-237 applied 2026-04-04: Public Instability Hybrid definition -->
<!-- PP-238 applied 2026-04-04: Lowenritter reactive Military NPC guidance -->
<!-- PP-241 applied 2026-04-04: Crown-Lowenritter covert delegation rule (PROVISIONAL) -->
<!-- PP-244 applied 2026-04-04: Scene→Mass transition modifier table (PROVISIONAL) -->
<!-- PP-246 applied 2026-04-04: Niflhel + Lowenritter ethical framework modifiers extracted -->

## Crown Covert Actions (PP-236) [PROVISIONAL — ED-147]
Crown has NO Intel stat. Crown covert actions (investigation, sabotage, intelligence gathering) use the **Influence** pool at **+1 Ob**. This is a faction design constraint: Crown is institutionally weakest at covert operations. The +1 Ob penalty applies to all Crown-initiated covert Domain Actions regardless of the action's formal label.

## Crown-Lowenritter Covert Delegation (PP-241) [PROVISIONAL — ED-149]
When Crown delegates a covert Domain Action to Lowenritter, the roll uses **Lowenritter Intel** pool. The Crown covert +1 Ob penalty does NOT apply — the constraint is institutional, not operational. Lowenritter acts as Crown's deniable agent. Political consequences of Lowenritter action discovery fall on Crown, not Lowenritter.

## Public Instability — Hybrid Mode (PP-237) [PROVISIONAL — ED-148]
Public Instability is a Hybrid-mode secondary clock.
- Range: 0–10. Starting value: 5.
- In TTRPG mode: not a separate clock. Effects folded into Institutional Pressure.
- Hybrid increases: +1 per season Revolution Agitation resolves (any degree); +1 per season IP increases while TC > 40.
- Hybrid decreases: −1 per season Crown or Guilds completes successful social Domain Action in contested territory.
- Threshold 8: Revolution gains one free Agitation action at no Domain Action cost.
- Threshold 10: Shared loss condition check (Institutional collapse — distinct from RS=0 Rupture).

## Lowenritter Reactive Military NPC Guidance (PP-238)
Lowenritter NPC AI priority: if any bordering faction's Military exceeds Lowenritter Military, Lowenritter NPC AI prioritises Military Consolidation (internal) the following season. This is a guidance rule, not a threshold mechanic — no automatic trigger fires.

## Scene→Mass Transition Modifiers — Hybrid (PP-244) [PROVISIONAL — ED-151]
When a personal combat scene precedes or overlaps a Strategic Phase mass action:
- PC Overwhelming success: mass action at −1 Ob (officer neutralised, morale advantage)
- PC Success: no modifier
- PC Partial: mass action at +1 Ob (position degraded)
- PC Failure: mass action at +2 Ob (PC captured/incapacitated; morale cost)
Mid-combat zoom: pause combat. Resolve Strategic Phase. Apply mass outcome as context. Resume personal combat next session.

## Ethical Framework Modifiers — Niflhel and Lowenritter (PP-246)
| Faction | Framework | Aligned (−1 Ob) | Contradict (+1 Ob) |
|---------|-----------|----------------|-------------------|
| Niflhel | Transactional Survival | Covert actions (always −1 Ob; covert is their native mode) | Open/public actions |
| Löwenritter | Martial Honour | Military actions + Crown-loyal actions | Political manipulation; acting against Crown interest |

## PP-242 — Seasonal cap timing
±2 cap applied at accounting. Multiple actions within a season tally; net clipped at accounting.

## PP-243 — Royal Decree partial-sheet
Decree may only target stats present on target faction's sheet.

## PP-244 — PC excommunication succession
Excommunicated PC faction leader: faction reverts to NPC institutional tendency until PC reinstated (Reversal) or replacement designated (Influence DA Ob 2 or GM succession).

## PP-246 — DA→Contest escalation
DA always produces outcome. Contest escalation only when: (a) both parties present, (b) stakes contested, (c) DA roll = Partial. On Partial: Contest at Conviction Track 5. On Success/Failure: no Contest.

## PP-254 — TC seizure classification
Territory seizure TC gains = distinct category (not DA). All TC sources subject to ±5/season combined cap. ±3 DA sub-cap does not apply to seizure.

## PP-255 — Public Instability full design (BG)
Range 0–10. Start 5. Accrual: +1/season any faction Mandate < 3 at accounting. Recovery: −1/season zero hostile Stability-targeting DAs. PI ≥ 8: revolt check (Stability ≤ 3 factions → Stability Ob 2; fail → Mandate −1). PI = 10: GM narrative uprising event.

## ED-174 provisional — PI cascade brake
At PI ≥ 8: factions passing Stability Ob 2 gain Stability +1. PI increase cap +2/season from all sources combined. Awaiting user confirmation.

## PP-281 — PI cascade brake
At PI ≥ 8: revolt-pass → Stability +1. PI increase rate cap: +2/season max from all combined sources.

## ED-005 Resolution (PP-286) — Restoration Movement Leader [FLAGGED]
Primary NPC contact: **Maret Vossen** (confirmed existing). Secondary: **Aldric Hann**.
Full stat blocks deferred to campaign development. Names canonical from existing params.
[FLAGGED: stat blocks required before NPC roster compilation.]


## ED-006 Resolution (PP-287) — Riskbreakers Identity [FLAGGED]
Riskbreakers: extralegal arm of Löwenritter. Small-cadre elite consequentialists,
loyal to Valoria-as-concept not to Crown or institution. Will go extralegal when
judged necessary. Already documented in params_factions §Riskbreakers. Confirmed.
[FLAGGED: full operational profile deferred to NPC roster development.]


## ED-019 Resolution (PP-288) — Faction Tactic Cards [FLAGGED]
Provisional minimal tactic card set (2 per faction):
| Faction | Tactic A | Tactic B |
|---------|----------|----------|
| Crown | Royal Prerogative (+2D one Mandate roll, 1/season) | Iron Decree (cancel 1 opposing DA, 1/campaign) |
| Church | Sanctuary (protect 1 NPC from targeting 1 season) | Inquisition (force reveal 1 hidden faction stat) |
| Hafenmark | Trade Leverage (+1D all Wealth rolls 1 season) | Constitutional Check (−2 Ob one Crown action) |
| Varfell | Intelligence Supremacy (learn full stat block of 1 faction) | Patience Protocol (pass; bank +2D for any future roll) |
| Restoration | Community Shield (reduce RS cost of 1 Weaving by 2) | Solidarity (+1D all Presence marker actions 1 season) |
| Löwenritter | Martial Discipline (immune to Feigned Retreat 1 battle) | Riskbreaker Activation (deploy Quiet-equivalent 1/campaign) |
[FLAGGED: placeholder designs. Full design required before BG compilation.]


## ED-024 Resolution (PP-289) — Mode 3 Entity Stats [FLAGGED]
Minimal provisional stat block for simulation:
| Stat | Value | Notes |
|------|-------|-------|
| Thread Pool Score | 8 | Acts as TS 80+ practitioner |
| Wound threshold | 12 | Physical damage valid only in material-adjacent state |
| Initiative | Always last | Responds, does not initiate |
| Thread operation | Weaving (automatic, no Leap) 1/round, Object scale |
| Coherence | N/A | No rendering substrate to degrade |
Full stat blocks require designer decision. Floor for simulation only.
[FLAGGED: full Mode 3 design deferred to Southernmost supplement.]


## ED-029 Resolution (PP-290) — Purpose Tracking / Clarity [FLAGGED]
Clarity countdown adopted: Clarity = d3+1 at zone entry. −1 per hour of exposure.
Clarity 0: Spirit TN7 Ob2 or forced exit. TS ≥ 40: +1 Clarity at entry.
[FLAGGED: confirm d3+1 range and Spirit check parameters.]


## ED-034 Resolution (PP-291) — Ceiral Ritual RS Asymmetry
BG Co-Movement cap (RS +1) applies only to BG-layer Thread abstraction.
Ceiral Ritual is a TTRPG Zoom In — operates at full TTRPG RS values, bypassing BG cap.
Not a contradiction. ED-034 resolved — no mechanical change needed.


## ED-036 Resolution (PP-292) — Altonian Invasion Unit Stats [FLAGGED]
Provisional stats for simulation unblocking (ED-036 P1-BLOCKER):
| Unit | Size | Command | Discipline | Power | DR |
|------|------|---------|-----------|-------|----|
| Vanguard Infantry | 6 | 4 | 5 | 3 | 2 |
| Vanguard Cavalry | 4 | 5 | 4 | 4 | 1 |
| Vanguard Siege | 3 | 3 | 3 | 5 | 3 |
Altonian faction: Mandate 6, Military 7, Stability 5. No Influence/Wealth/Intel in Valoria context.
[FLAGGED: confirm unit stats before Altonian engagement is canonically simulated. P1-BLOCKER cleared provisionally.]


## ED-143–146 Resolution (PP-323) — PC Simulation Constructs [FLAGGED]
Canonical test characters adopted for mechanical testing:
- **Mira Sondhal** (ED-143): Practitioner-Scholar. TS 61. Confirmed.
- **Arend Voss** (ED-144): Crown Agent-Soldier. Confirmed.
- **Sister Dagmara Kuhl** (ED-145): Church Renegade. Confirmed.
- **Theron Ault** (ED-146): Guilds Fixer. Confirmed.
Designer retains right to revise names and backstory before player-facing publication.
[FLAGGED: confirm canonical adoption or request redesign.]


## ED-147 Resolution (PP-324) — Crown Covert Penalty [FLAGGED]
Crown covert actions use Influence pool at +1 Ob (no Intel stat). PP-236 confirmed.
+1 Ob is the provisional modifier — represents Crown's institutional weakness at covert operations.
[FLAGGED: confirm +1 Ob or set alternative modifier before Crown Domain Action compilation.]


## ED-148 Resolution (PP-325) — Public Instability Hybrid [FLAGGED]
Public Instability: Hybrid secondary clock. Range 0–10, start 5.
Increases: +1/season Revolution Agitation resolves (any degree); +1/season IP rises while TC > 40.
Decreases: −1/season Crown or Guilds completes successful social DA in contested territory.
Threshold 8: Revolution free Agitation action. Threshold 10: Institutional collapse check.
[FLAGGED: confirm thresholds before Hybrid cascade compilation.]


## ED-149 Resolution (PP-326) — Crown-Löwenritter Delegation [FLAGGED]
When Crown delegates covert DA to Löwenritter: roll uses Löwenritter Intel pool.
Crown +1 Ob penalty does NOT apply — constraint is institutional, not operational.
Political consequences of discovery fall on Crown. PP-241 confirmed.
[FLAGGED: confirm penalty non-application to delegated actions.]


## ED-151 Resolution (PP-328) — Scene→Mass Transition [FLAGGED]
Modifiers confirmed (PP-244/251):
- PC Overwhelming: mass action −1 Ob
- PC Success: no modifier
- PC Partial: +1 Ob
- PC Failure: +2 Ob
Mid-combat zoom: pause at round boundary, resolve Strategic Phase, resume next session.
AUD-P1-15 provisionally closed.
[FLAGGED: confirm modifier values before Hybrid compilation.]


## ED-152 Resolution (PP-329) — Domain Echo Formal Rule [FLAGGED]
Domain Echo: Cascade Phase conversion of personal scene outcome to faction stat change.
Magnitude: Overwhelming = stat ±2 or clock ±3; Success = stat ±1 or clock ±2; Partial = narrative only; Failure = own faction stat −1.
One Domain Echo max per scene per faction. GM determines relevant stat and direction.
[FLAGGED: confirm clock magnitudes before Hybrid compilation.]


## ED-174 Resolution (PP-335) — Public Instability Cascade Brake [FLAGGED]
When Revolution passes a revolt-check (Agitation Partial or better and PI > 5):
Stability +1 (internal movement cohesion). This prevents PI from spinning Revolution into
a Stability death spiral. Applies once per season max.
[FLAGGED: confirm +1 Stability cascade brake before IP/PI interaction compilation.]


## Domain Action Intra-Season Stat Update Timing (PP-287)
Stats update IMMEDIATELY after each Domain Action resolves within a season (sequential model).
A stat depleted by DA-1 provides a lower pool for DA-3 in the same season.
GMs track running stat totals on the faction sheet during Domain Action resolution.
Rationale: batch resolution would allow impossible actions (spending Wealth already spent).

## Seasonal Stat Change Cap — Cost Clarification (PP-288)
The ±2 seasonal cap applies to net **gains** from Domain Action outcomes only.
Domain Action **costs** (Wealth expenditure, Stability backlash) are NOT subject to the cap.
A faction may lose more than 2 Wealth in a season if multiple DAs each cost 1 Wealth.
A faction may not gain more than 2 in any single stat from DA outcomes in one season.

## High-Wealth Passive Recovery (PP-289)
A faction with Wealth >= 5 at Accounting that suffered no active economic Domain Action against it
this season recovers +1 Wealth automatically (economic resilience).
Applies to: Guilds (starting W=6), Hafenmark (starting W=5). Does not apply under Trade Embargo or Siege.
