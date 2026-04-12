<!-- version: v0.16-PP500-512 | sources: stage6_factions.md (TTRPG), bg_v05 (BG/Hybrid) | last_updated: 2026-04-07 -->
<!-- NOTE: stage6_factions.md is STALE for BG faction mechanics. Use BG column for board game/hybrid. -->
<!-- PATCHES APPLIED: PP-167, PP-168; PP-195; PP-402; PP-403; PP-405; PP-428–442; PP-431-COR; PP-441-COR | EDITORIALS RESOLVED: ED-311 (Path B Option A), ED-318 (Total Domination), ED-319 (Parish/Cathedral), ED-320 (Diplomat card), ED-321 (RDT/TD) -->
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
| Restoration Movement | — | — | — | — | — | — | — | — | No faction stats (PP-460). Operates via Presence markers and Community Weaving. Victory via Cultural Uprising of T9 Himmelenger. |
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
Ob = floor(relevant stat / 2) + 1.
Attacker bonus dice: own faction's relevant stat if holding faction leadership.
Non-Player Character faction rolls: relevant stat as d10 pool, TN 7.

## TC Passive Advance (PP-402)
Theocracy Counter (TC) advances by **+1 per season** from institutional momentum, regardless of Church action.
Applied at Accounting before Assert/Suppress resolution.

| Action | TC effect |
|--------|-----------|
| Passive baseline | +1 (always) |
| Assert (Church) | +2 total (replaces passive; not additive) |
| Suppress (Crown or Hafenmark Domain Action) | Negates passive +1 for that season only. TC does not decrease. Ob = floor(Church Mandate / 2) + 1 ÷ 2 (round up, min 1). |

Suppress may be declared once per season by one faction. It cannot reduce TC below its value at season start.
TTRPG: same rule applies. BG: same rule applies; Suppress is a Standard Action consuming one card.


## Failed Domain Action Stability Cost (PP-403)
A Domain Action that results in **Failure** (net successes ≤ 0) costs the acting faction **−1 Stability**.
Partial success (net > 0 but < Ob): no Stability cost.
Success/Overwhelming: normal effect, no cost.

**Scope exclusions:**
- Does not apply to self-improvement Domain Actions (acting faction targeting own stats).
- Does not apply to TTRPG personal scene rolls or Thread operations.
- Does not apply to Restoration Movement (RM has no Stability — PP-460).
- Applies to faction-layer Domain Actions only.

**Stability 1 edge case:** If Stability is already 1, a Failure reduces it to 0, triggering an immediate Stability Check (existing mechanic). Factions with low Stability are further discouraged from sub-threshold gambles.


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
| Church | Theocracy Counter 60 Territorial Seizure | Mandate vs floor(owner's Mandate / 2) + 1 | Per-territory roll. Success: administrative control. Failure: Mandate −1. |
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
Roll: Mandate vs floor(target Mandate / 2) + 1 (faction leader) or Ob 2 (non-leader).
| Degree | Result |
|--------|--------|
| Success | Strips target's Circles bonus; target faction Mandate −1 |
| Failure | — |
Reversal: Grand Debate (5 exchanges) or new Confessor appointed.

### Church — TC 60 Territorial Seizure
Trigger: Theocracy Counter (TC) reaches 60. Fires once per territory.
Roll: Mandate vs floor(owner's Mandate / 2) + 1.
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

## Community Weaving — Cross-Reference (PP-250)
Community Weaving canonical formula in params_threadwork.md PP-250.
Prior entries under PP-168 (Influence/TT÷20) and PP-195 (Mandate+History/Ob3) are deprecated.
Not a Domain Action. No faction stat output. RS restoration only.

## Church Martyrdom Effect (PP-259)
When a public accusatory Contest against a Church leader fails (net < Ob, public venue, wrong Resonant Style):
Church gains Stability +1.
Conditions: (a) public venue with witnesses, (b) accusatory mode used vs Consequence-mode NPC, (c) Failure or Partial result.
Applies to: Himlensendt, Olafsson, Klapp as institutional representatives.

## Resentment Tokens (PP-405 — ED-298 resolved)
Generated when a faction votes **No** on a parliamentary motion that is successfully blocked.
- Acting faction gains **+1 Standing** (blocking reward).
- A **Resentment token** (cube) is placed between the blocking faction and the proposing faction.
- Effect: blocking faction gets **−1 Ob** on Domain Actions targeting the proposer; proposer gets **+1 Ob** on Domain Actions targeting the blocking faction.
- Scope: parliamentary votes only. Domain Actions do not generate Resentment.
- Expiry: cleared at Year-End if neither faction took a hostile Domain Action against the other during the year.
- Early resolution: Diplomacy action (Ob 2), both factions must consent.
- Abstaining generates no Resentment and no Standing gain.


## Canonical Coalition Pairs (PP-504 — supersedes PP-405; ED-299 resolved)
Used by PP-404 (Missed Coalition Ob Penalty). A coalition trigger requires both factions'
relevant stats to meet or exceed the listed threshold simultaneously.

| Coalition | Factions | Trigger condition | Effect on activation |
|-----------|---------|-------------------|----------------------|
| Diplomatic Alignment | Church + Hafenmark | Both Influence ≥ 5 | +1D to each other's Diplomacy rolls for the season; once per season during a Parliamentary Session, both factions count as same-side voters regardless of their declared votes (PP-526) |
| Military Compact | Varfell + Löwenritter | Both Military ≥ 5 | Shared unit deployment: one faction's Legionary card may be played in the other's adjacent territory without adjacency restriction; on activation both factions jointly declare one Named Enemy — each gains 1 CB vs Named Enemy (PP-507 cap); Named Enemy may be changed by mutual Phase 1 agreement; Compact dissolves if either partner plays Legionary targeting the other |
| Trade Compact | Crown + Hafenmark | Crown TCV ≥ 14 AND Hafenmark TCV ≥ 10 | Each faction's Trade/Govern in the other's territory: −1 Ob this season |
| Thread Stewardship | Varfell + Restoration Movement | VTM ≥ 3 AND RM has ≥ 2 Presence markers | Restoration Community Weaving in Varfell territories: −1 Ob; Varfell Tribune actions in RM Presence territories: +1D |

Fog-of-war exemption applies to all coalitions per PP-404.
Coalition triggers are public knowledge (the threshold conditions are known); only the current stat values are subject to fog of war.



## Hafenmark — Diplomat Card (ED-320 RESOLVED)
See params_board_game.md §Hafenmark — Diplomat Card for full mechanics.
**Summary:** Senator Outward, Influence vs Ob = floor(target Mandate / 2) + 1, once/season. Diplomatic Tokens enable Parliamentary Session pre-commitment. Restriction: not Church if PI < 3.

## Hafenmark — RDT/TD Tracks (ED-321 RESOLVED)
Full tables in params_board_game.md §RDT/TD.
**Summary:** RDT 0–5 (Reformed Settlement advances); TD 0–5 (activates at RDT 2, advances when Church Asserts).

## Church — Parish/Cathedral (ED-319 RESOLVED)
Full rules in params_board_game.md §Parish/Cathedral System.
**Summary:** 2 Consul Inward successes + 1W = Parish (PT floor 1). 5 total + 3W total = Cathedral (PT floor 2 + Prominence +1). Parish survives control change; Cathedral degrades to Parish.

## Total Domination (ED-318 RESOLVED)
**Available to all factions.** TCV ≥ 28 + all rivals at Stability 0 (eliminated OR Submitted) for 2 consecutive Accounting steps. Submission: voluntary at Stability 0; submitted faction becomes NPC vassal.

## Varfell — Warden Recognition (WR) Track (ED-311 RESOLVED)
Range 0–4. Replaces WA+WC split for Path B. See params_board_game.md §Varfell Path B for full rules.

## Varfell — Revelation Tokens (PP-439)
Full reveal = Overwhelming Tribune Investigate OR 4 consecutive PC Spy successes.
Token placed on target faction mat (public, permanent). Two tokens on different rival mats = Path A fully revealed condition met.

## Crown — Royal Charter (PP-433)
Max active Charters = floor(Mandate / 2) + 1. Charter territory: Govern/Trade −1 Ob for all factions; Church Seizure +1 Ob; Crown own actions −2 Ob. Dissolves on control transfer.

## Crown — Thread Liaison (PP-436)
Phase 1 declarative. Designate one allied faction. Their Thread operations in Crown territories count toward Crown co-victory RS tracking. Dissolves on military conflict.

## Crown — Diplomatic Outreach to Schoenland (PP-437)
Senator Outward, Crown only. Influence vs Ob = AER level min 1. Cannot combine with Formal Crown Treaty same season.

## Counter-Intelligence Postures (PP-442)
- Crown Royal Guard: cancel 1 Intel action targeting Crown per season (Phase 4 Priority 1, no card).
- Hafenmark Procedural Objection: on Varfell Investigate success, costs Challenge use; if M ≥ 4, revealed stat falsified for non-Varfell observers.
- Church Sanctuary extension: also blocks Varfell 4-PC Spy once per season.

## Baralta BG Conviction [PP-482, ED-080 resolved]
Fires at any Accounting where PI ≥ 6 OR Hafenmark TCV ≥ 12.
Effect: Hafenmark Mandate +1. One-time per game.
## Vaynard BG Conviction [PP-483, ED-081 resolved]
Fires at any Accounting where VTM ≥ 4 AND Varfell controls T9 or T13.
Effect: Varfell Mandate +1 AND VTM +1. One-time per game.
## Varfell Succession — Maret Uln [PP-486, ED-308 resolved]
If Vaynard eliminated (Loyalty 0 + Mandate 0): Maret Uln becomes faction leader. VTM resets to 0.
Varfell aligns with RM goals: cannot target RM, cannot seize RM-held territory.
This is factional realignment, NOT RM Emergence — RM does not gain faction stats or independent actions.
The triple-condition hostile RM Emergence trigger remains the canonical path for RM as a playable faction.
## Baralta Succession — PI-Gated [PP-487, ED-309 resolved]
If Baralta eliminated (Loyalty 0 + Mandate 0):
- PI ≥ 4: institutional succession. Hafenmark Mandate −1, Stability −1. All mechanics intact.
- PI < 4: fracture. Hafenmark Mandate halved (round down). TCV victory requirement +2. Parliamentary Sovereignty unavailable until PI recovers to ≥ 4.
No named successor. Hafenmark's identity is institutional.
## Cardinal Focus Temperance — AER Gain [PP-490, ED-328 resolved]
AER +1 requires 2 consecutive seasons of Cardinal Focus declaration (not each season).
Season 1: mark Focus-declared on Church faction mat.
Season 2 (consecutive): AER +1 fires.
If the Church misses a season, the consecutive chain resets. No AER gain from a single-season declaration.
This prevents Season-1 AER 3 and preserves meaningful commitment cost.
## Torben Loyalty After Crown Elimination [PP-494, ED-332 resolved]
If Crown is eliminated: Torben Loyalty track transfers to Löwenritter as dynastic successor.
Löwenritter inherits Torben's current Loyalty value. Track meaning shifts:
0 = Torben aligns with anti-Löwenritter faction (Church or Restoration). 7 = full Löwenritter loyalty.
If Löwenritter is also eliminated: Torben Loyalty track becomes contested — all remaining factions
may spend 1 Domain Action (Diplomat Inward) to bid for Torben's allegiance. Highest bid wins Torben
as a named NPC ally (+1D on one Domain Action category per season).
[PROVISIONAL]
## Cardinal Death — Holy See Succession [PP-498, ED-336 resolved]
When a Cardinal is killed (by PC action or event):
- Cardinal-specific BG mechanics (Fortitude Templar, Justice Inquisitor, Prudence Tithes, Temperance AER)
  are suspended for 1 season (the Holy See appointment procedure takes time).
- At next Accounting: Church player rolls Church Mandate vs Ob 2 (Holy See appointment).
  Success: new Cardinal appointed, full mechanics resume.
  Overwhelming: Appointment + AER +1 (the crisis galvanises Church unity).
  Failure: gap extended 1 additional season. Another attempt at next Accounting.
- TC effect: Cardinal death triggers TC +1 (institutional disruption).
[PROVISIONAL]

## Restoration Movement — Mode and Founding Status (PP-478, PP-495)
**BG-only mode:** Not a playable faction. No player controls RM.
**Hybrid mode:** Not present at game start. Founded mid-campaign via Founding Mechanic (see params_board_game.md §RM Founding Mechanic). Post-founding stats depend on Founding degree (Success: Mandate 1/Influence 2/Wealth 1/Military 0/Stability 3; Overwhelming: Mandate 2/Influence 3/Wealth 1/Military 0/Stability 4).
**TTRPG mode (PP-495):** Not present at campaign start. GM introduces RM as an emergent faction when all narrative conditions converge: (1) cultural shift visible — at least 2 communities/NPCs have expressed dissatisfaction with Church authority or sympathy for Einhir practice in play; (2) substrate strain noticeable — Thread operations have produced visible consequences (Thread Wounds, Coherence loss, RS decline); (3) player engagement — at least one PC has interacted with Einhir cultural knowledge, Southernmost artefacts, or practitioner communities. GM declares the Founding Scene. A named NPC or PC becomes the Founding Agent. RM gains the stat block from §8.8. Floor: session 6 of a standard campaign (political landscape must develop before RM complicates it).
Prior RM stat entries (Mandate -, Influence -, etc.) reflect pre-Founding state (RM does not exist). Post-Founding stats supersede those entries.