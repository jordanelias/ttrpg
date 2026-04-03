<!-- version: v0.14-AUD2 | sources: stage6_factions.md (TTRPG), bg_v05 (BG/Hybrid) | last_updated: 2026-04-02 -->
<!-- NOTE: stage6_factions.md is STALE for BG faction mechanics. Use BG column for board game/hybrid. -->
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
| Varfell | 4 | 3 | 4 | 4 | 3 | 4 | — | 4 |
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
