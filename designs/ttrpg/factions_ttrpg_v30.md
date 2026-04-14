<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: factions_ttrpg_v30_infill.md -->

<!-- v30 baseline — design-layer doc created 2026-04-13 from compilation/v0.14/stage6_factions_deprecated.md -->
<!-- UNVERIFIED: mechanical values in this doc have not been confirmed by simulation. -->
<!-- Flag any value used in simulation: [UNVERIFIED: <value> — pending stress test] -->
<!-- Mode: TTRPG -->
<!-- Authority: designs/ working layer — pending compilation -->

# PART EIGHT: FACTIONS


---

## 8.1 Faction Mechanics

### Faction Stats (6-stat, 1–7 scale)

| Stat | Represents |
|---|---|
| Mandate | Public legitimacy and popular support |
| Influence | Political reach and diplomatic weight |
| Wealth | Economic capacity |
| Military | Armed force and unit capacity |
| Intel | Intelligence network and covert operations |
| Stability | Internal cohesion and crisis resistance |

**Partial sheets:** Niflhel (no Mandate, no Military), Revolution (Influence, Stability, Intel only), Lowenritter (no Mandate, no Wealth — Military, Intel, Influence, Stability only).


### Starting Values

| Faction | Mandate | Influence | Wealth | Military | Intel | Stability |
|---|---|---|---|---|---|---|
| Crown | 5 | 5 | 4 | 4 | — | 4 |
| Church | 5 | 6 | 5 | 4 | — | 5 |
| Hafenmark | 4 | 4 | 5 | 3 | — | 4 |
| Varfell | 4 | 4 | 4 | 4 | — | 4 |
| Guilds | 3 | 4 | 6 | 2 | — | 5 |
| Niflhel | — | 5 | 4 | — | — | 4 |
| Revolution | — | 3 | — | — | — | 3 |
| Lowenritter | — | 3 | — | 5 | 3 | 5 |

*Schoenland is not a faction — it is a spoiler actor. See §8.10.*

**Public Instability Track — BG mechanics (PP-255, PP-281):**
Range: 0–10. Starting value: 5 (BG). Not a separate track in TTRPG mode (effects folded into Institutional Pressure).
- **Accrual:** +1 per season in which any faction's Mandate drops below 3 at accounting. **Rate cap (PP-281):** PI cannot increase by more than +2 per season from any combination of sources.
- **Recovery:** −1 per season in which zero hostile Domain Actions targeted any faction's Stability that season.
- **Cap:** 0–10.
- **PI ≥ 8:** Revolt risk — at accounting, each faction with Stability ≤ 3 makes a Stability check Ob 2. Failure: Mandate −1. **Cascade brake (PP-281):** Any faction that passes this check gains Stability +1.
- **PI = 10:** General uprising — GM narrative event fires. Magnitude and faction determined by campaign state. No automatic mechanical resolution.
- PI does not reset between seasons automatically.

### Domain Actions


**Domain Ob:** Target faction's relevant stat directly (1–7 scale; no division). A faction at stat 4 sets Ob 4. The rolling character may add their own faction's relevant stat as bonus dice if they hold leadership of that faction.


**Domain Action → Social Contest escalation (PP-246):** A Domain Action always produces a mechanical outcome on its own. Escalation to a full Social Contest occurs only when all three hold: (a) both parties are personally present, (b) stakes are explicitly contested by both, AND (c) the DA roll produces a Partial. On Partial: GM may call a Contest at Conviction Track 5 (neutral); DA outcome held pending Contest resolution. On Success or Failure: outcome is final, no Contest.

**Community Weaving canonical spec (PP-270):** The PP-195 version is canonical. Pool: Mandate + relevant History. TN 7, Ob 3. On success: target RS track +1 (shared world track). All other Community Weaving specifications (PP-168 pool and PP-195 partial variants) are superseded.

**Seasonal cap:** ±2 per stat per season, applied at seasonal accounting (PP-242). Multiple actions may accumulate more than ±2 change within a season; the net is clipped to ±2 at accounting. Institutional momentum does not reverse between actions.

### Ethical Framework Modifiers


- **−1 Ob:** Actions aligned with the faction's ethical framework
- **+1 Ob:** Actions that contradict or strain the framework
- **+2 Ob:** Church only — actions that would reveal Thread truth (institutional perceptual prophylaxis)


### Leader vs Institution



### Nine Political Axes


| Axis | Pole A | Pole B | Primary Factions |
|---|---|---|---|
| 1. Sovereignty | Crown authority | Church authority | Crown vs Church |
| 2. Knowledge | Thread truth accessible | Thread truth suppressed | Varfell/Revolution vs Church |
| 3. Legitimacy | Constitutional monarchy | Theocratic governance | Crown/Hafenmark vs Church |
| 4. Cultural identity | Einhir recovery | Colonial settlement | Revolution vs Crown/Church |
| 5. Economic control | Guild autonomy | State/Church taxation | Guilds vs Crown/Church |
| 6. Military authority | Ducal/Crown command | Templar independence | Hafenmark/Crown vs Church |
| 7. Information | Transparency | Secrecy | Revolution vs Niflhel/Varfell |
| 8. External threat | Accommodation of Altonia | Resistance | Crown (split) vs all |
| 9. Ontological | The world is what it appears | The world is more | Church vs practitioners |

**Using the axes:**
3. War justification (casus belli) maps to axes
4. Domain Echo content is described in terms of the relevant axis

---

## 8.2 Faction 1: The Crown (Monarchy)

**Ethical Framework: Virtue Ethics**


- Public, visible, virtuous actions (defending the weak, upholding law, honouring treaties): **−1 Ob**
- Covert, expedient, or morally ambiguous actions: **+1 Ob**



**Leadership Deviation:** Acts against tendency (breaks treaty, supports practitioners, ignores Parliament): Stability check **Ob 2** at next accounting.

**Unique Action — Royal Decree**


| | |
|---|---|
| **Roll** | Mandate vs Ob 2 |
| **Success** | One faction attribute change (any faction, ±1) takes effect immediately rather than at seasonal accounting |
| **Failure** | Mandate −1 (overreach) |
| **Constraint** | Cannot target Intel — decrees are public acts. Cannot target a stat absent from the target faction's sheet (e.g. Niflhel has no Mandate; Löwenritter has no Wealth). (PP-243) |
| **Limit** | 1/season; consecutive seasons: +1 Ob per consecutive use (decree fatigue) |

**Altonian invasion units — provisional (PP-282, ED-036 resolved):**
At IP ≥ 75, the following provisional unit stats apply for simulation. **NOTED: subject to worldbuilding confirmation.**

| Unit | Size | Power | Discipline | Morale | Weapon | Armour |
|------|------|-------|-----------|--------|--------|--------|
| Altonian Vanguard | 4 | 4 | 4 | 5 | LightCut + HP | Medium |
| Altonian Heavy Infantry | 5 | 5 | 5 | 5 | HeavyCut | Heavy |

Invasion wave: 3 Vanguard + 2 Heavy Infantry. NPC general Command 5.

**Victory balance (PP-262):** Crown's victory condition requires at least one deed that demands active mid-game play (not pre-met at session start). The GM should confirm that Crown's deed set includes at least two deeds achievable only through Domain Actions or military success after Season 1. If Crown's starting position pre-meets 3 of 5 deeds, replace one pre-met deed with: 'Hold Valorsplatz and maintain Mandate ≥ 5 at end of Season 6.'

**Default Leader: King Almud Almqvist**

---

## 8.3 Faction 2: The Church of Solmund

**Ethical Framework: Divine Command**


- Doctrine-aligned actions (suppressing heresy, expanding Piety, enforcing moral law): **−1 Ob**
- Actions contradicting doctrine or undermining Church authority: **+1 Ob**
- Actions revealing Thread truth (supporting practitioners, Southernmost investigation): **+2 Ob**


**Leadership Deviation:** Confessor acts against doctrine: Stability check **Ob 3**. Hardest deviation cost of any faction — theological coherence is the Church's structural strength.


**Unique Action — Excommunication**

| | |
|---|---|
| **Roll** | Church Mandate vs target's Mandate (faction leader) or Ob 2 (non-leader) |
| **Overwhelming** | Target loses Circles bonus with Church contacts; target faction Mandate −1; target barred from public office and Church-loyal command; personal Reputation −1 with all factions |
| **Success** | As Overwhelming minus the Reputation penalty |
| **Failure** | Church Mandate −1; target gains Mandate +1 (sympathy martyr) |
| **Constraint** | Requires Church Mandate ≥ 3 (on 1–7 scale: institutional authority threshold) |
| **Reversal** | Grand Debate (5 exchanges) or appointment of a new Confessor |

**Player Character excommunication — faction succession (PP-244):** If the excommunicated target is a PC faction leader, the faction reverts to institutional tendency (Game Master-run) until: (a) the PC is reinstated via Reversal above, or (b) a replacement leader is designated through narrative play (Influence Domain Action Ob 2 by any PC, or Game Master succession).

**Default Leader: Confessor Arne Himlensendt**
- Conviction: Faith · Resonant Style: Evidence · Thread Sensitivity: 0 (theologically foreclosed)
- Sincerely devout. Zero awareness of Galbados's actual nature. Not cynical — wrong.


**Theocracy Counter 60 — Territorial Seizure Procedure**


**Roll:** Church Mandate (pool, TN 7) vs territory owner's Mandate ÷ 2 (round up, minimum Ob 1).

**Territory Theocracy Counter value (flat, on seizure — no per-season accrual):**

| Territory Type | Theocracy Counter on Seizure |
|---|---|
| Minor territory (rural, low-prosperity) | +1 |
| Major territory (trade hub, fortified, ducal seat) | +3 |
| Capital or key institutional site (Valorsplatz, cathedral city) | +5 |

**Outcome on success:** Church gains administrative control of the territory. The territory's Domain Actions may no longer target Church authority without +2 Ob. The flat Theocracy Counter value fires immediately on seizure.

**Outcome on failure:** No seizure. Church Mandate −1 (overreach).

**Counter-play options:**
- Parliamentary vote to dispute seizure (Influence vs Ob 3): success reverses seizure; Theocracy Counter does not fire.

---

## 8.4 Faction 3: Hafenmark (Duchy)

**Ethical Framework: Categorical Imperative**


- Actions based on legal precedent, constitutional authority, established procedure: **−1 Ob**
- Ad hoc, situational, or precedent-breaking actions: **+1 Ob**



**Leadership Deviation:** Baralta acts against tendency (extralegal action, breaking with Parliament, allying with Niflhel): Stability check **Ob 1**. Low cost — Baralta IS the institution. Her personal authority is so thoroughly embedded that deviation costs are minimal. This is her structural advantage.

**Unique Action — Sovereign Authority Doctrine**


| Degree | Result |
|---|---|
| **Overwhelming** | Theocracy Counter −3. Church Mandate −1. Heresy Investigation blocked this season. +1D social vs Church for the arc. |
| **Success** | Theocracy Counter −2. Church Mandate −1. Heresy Investigation opens against Baralta (Ob 4 to pursue). |
| **Partial** | Theocracy Counter −1. Heresy Investigation opens immediately. Church Influence +1. |
| **Failure** | Theocracy Counter +1. Heresy Investigation immediate. Baralta's Mandate −1. |

*Roll: Mandate vs Ob 4. Once per campaign arc.*

*Heresy Investigation consequence:* Grand Debate (5 exchanges). If it succeeds without player intervention: Mandate −2, Theocracy Counter +3, Theocracy Counter suppression removed.

**Theocracy Counter Suppression:** While Baralta's Mandate remains 4+ (on 1–7 scale), she suppresses Theocracy Counter at −1/season. If Mandate drops below 4, suppression disappears. If excommunicated: Theocracy Counter +4 immediately.

**Default Leader: Duchess Inge Baralta**

---

## 8.5 Faction 4: Varfell (Duchy)

**Ethical Framework: Consequentialist Pragmatism**


- Actions with measurable outcomes within one season (concrete, verifiable results): **−1 Ob**
- Actions with uncertain or long-term payoff (ideological campaigns, relationship-building, cultural investment): **+1 Ob**




**Leadership Deviation:** Vaynard acts against tendency (public ideological commitment, open Restoration support, military aggression without intelligence preparation): Stability check **Ob 2**. The institution expects its leader to be clever, not bold.

**Unique Action — The Private Collection**


| | |
|---|---|
| **Roll** | Intel vs Ob 2 |
| **Success (choose one)** | +2D to one Thread-related Domain Action this season; *or* reveal one hidden faction attribute; *or* −1 Ob to one Einhir Research action this season |
| **Failure** | Artefact's Thread signature detected by a practitioner. Church Intel gains +1D vs Varfell for 1 season. Thread Tension +1. |
| **Long-term cost** | Each use: +1 to Vaynard's hidden Thread Sensitivity. At Thread Sensitivity 14+ (his starting value), each use triggers Spirit check TN 7 Ob 1 for a Discovery Event. |

**Player Character takeover — Collection Discovery Event:** If a non-Vaynard Player Character takes over Varfell, the Private Collection transfers as an institutional asset (the artefacts exist physically). However, encountering the collection for the first time triggers a mandatory Discovery Event: the new leader finds Vaynard's research notes alongside Thread-locked objects of obvious significance. Spirit check TN 7 Ob 1. Success: the player understands what they have inherited and gains TK 1 immediately. Failure: the weight of the collection lands without context — Certainty −1 and a new Belief is offered from behind a position of ignorance.

**Default Leader: Duke Magnus Vaynard**
- Conviction: Reason · Resonant Style: Consequence · Thread Sensitivity: 14 (Dormant; unrecognised)

**Thread Investigation Track (TK) — 0 to 5**


| TK | Campaign Effect |
|---|---|
| 1–2 | Informed questions. Acute awareness, not understanding. No Theocracy Counter effect. |
| 3 | Structural theory (wrong in detail, correct in structure). Succession leverage formally linked to Southernmost access terms. Theocracy Counter +1. |
| 4 | Urgency. Willing to offer collection access (including originary locks) for Thread education and Southernmost partnership. Theocracy Counter +2. |
| 5 | Dangerous knowledge — understands what Galbados was structurally. Seeks capability, not further knowledge. Theocracy Counter +3. |

TK advances through: practitioner relationship (sustained season, cap ×2); originary lock examination with practitioner context (cap ×1); Church archive access via Niflhel channels (+1/archive); players sharing Thread-level knowledge directly (+1–2 by depth); Discovery Event triggering Thread Sensitivity 30 (+2 immediately).

---

## 8.6 Faction 5: The Guilds

**Ethical Framework: Moral Relativism**


- Actions benefiting trade, economic stability, or guild autonomy: **−1 Ob**
- Actions requiring moral consistency across contexts (enforcing a single law, demanding uniform behaviour, ideological campaigns): **+1 Ob**



**Leadership Deviation:** The Guilds are governed by a rotating Guildmaster Council — no single leader. Redirecting Guild policy requires convincing the Council: Influence vs Ob 3 as a Domain Action. Guilds are slow to change course but resistant to disruption from the top.

**Unique Action — Economic Leverage**

The Guilds apply economic pressure to any faction present in a territory where Guild Favour ≥ 5 (on the 1–7 territory-level track).

| | |
|---|---|
| **Roll** | Wealth vs target faction's Wealth |
| **Overwhelming** | Target loses 1 Wealth + 1 Prosperity in one territory (full economic warfare) |
| **Success** | Target faction loses 1 Wealth for 1 season (trade disruption, supply price increases, labour withdrawal) |
| **Failure** | Guild Favour −1 in that territory (backlash against perceived extortion) |
| **Constraint** | Cannot target factions in territories where Guild Favour < 5 |

**Leader: Guildmaster Council (Non-Player Character collective)**

---

## 8.7 Faction 6: Niflhel (Shadow Network)

**Ethical Framework: Amoral Consequentialism**


- Covert Domain Actions (intelligence, sabotage, assassination, smuggling): **−1 Ob**
- Public Domain Actions (anything requiring Niflhel to act openly or claim credit): **+2 Ob**


**Partial sheet:** No Mandate. No Military. (Influence, Wealth, Intel, Stability only.)


**Leadership Deviation:** Four-arm decentralised structure (Dockworkers, Reckoners, Burned, Quiet). No single leader can deviate without the other arms' consent. Redirecting any arm requires Intel vs Ob 3 within Niflhel. Failure: the arm acts independently against the redirecting leader's interests.

**Unique Action — The Quiet Network**


**Intelligence mode:**
- Roll: Intel vs target's Intel
- Success: learn one hidden faction attribute or one Non-Player Character's active Belief
- Overwhelming: learn two

**Sabotage mode:**
- Roll: Intel vs target's Stability
- Success: target Stability −1
- Failure: operative exposed — Niflhel Intel −1 for 1 season; target gains Grievance Marker

**Assassination mode:**
- Roll: Intel vs target's Intel +2
- Overwhelming: named Non-Player Character eliminated; no evidence trail
- Success: named Non-Player Character eliminated; evidence trail exists
- Partial: target wounded, not killed; evidence trail
- Failure: operative captured; full exposure; Niflhel Stability −2

**Long-term cost:** Each Quiet deployment in a season: Thread Tension +0.5 (cumulative). Niflhel's Southernmost harvesting supply chain disturbs the Thread-configurational environment. They do not know this.



---

## 8.8 Faction 7: The People's Revolution (Restoration Movement)

**Ethical Framework: Rawlsian Social Contract**


- Actions demonstrably benefiting the common population (reducing taxation, expanding access, challenging noble privilege, protecting Einhir cultural practice): **−1 Ob**
- Actions concentrating power, benefiting elites, or suppressing popular expression: **+1 Ob**


**Partial sheet:** No Mandate (rejects the legitimacy of the system that confers Mandate). No Military. No Wealth (operates through informal economies). Influence, Stability, Intel only.

**Institutional Tendency:** Spread pamphlets. Undermine elite Mandate. Protect practitioners. Recover Einhir cultural knowledge. Defaults to information warfare and cultural advocacy.

**Leadership Deviation:** No formal leader — a movement. Directing it requires Influence vs Ob 2 within the movement (easier than Niflhel due to ideological coherence). Directing the Revolution toward violence, authoritarianism, or elite alliance triggers Stability check **Ob 3** (the movement fractures if it betrays its own principles).

**Unique Action — Community Weaving**


| | |
|---|---|
| **Roll** | Influence vs Ob = Thread Tension ÷ 20 (round up) |
| **Overwhelming** | Thread Tension −2 |
| **Success** | Thread Tension −1 |
| **Partial** | Thread Tension unchanged; Stability −1 (working strained the community) |
| **Failure** | Stability −1; Thread Tension +1 (attempt disturbed what it tried to heal) |
| **Constraint** | Requires at least one practitioner with Thread Sensitivity 30+ affiliated with the Revolution |
| **Co-movement** | Draw a Co-Movement Card. Even beneficial Thread work has consequences. (P-01) |



---

## 8.9 Faction 8: The Löwenritter (Military Order)

**Partial sheet:** Military 5 · Intel 3 · Influence 3 · Stability 5. No Mandate, no Wealth.



**Counter increments (+1 each):**
- Torben's loyalty reaches 3–2 or lower (Altonian alignment)
- Crown loses two or more territories in one season without a military response Domain Action



- All non-Military Domain Actions in Martial Law territories require a secondary Military check (Löwenritter Military pool, TN 7, Ob 2) to proceed. Failure: the action is blocked this season.
- Stability enforcement: Löwenritter Military pool replaces faction-specific pools for all Stability-related Domain Actions in affected territories.
- Faction restriction: only Löwenritter and Crown may act openly. All other factions must succeed at a Covert Domain Action (Ob 3) to operate at all.
- Duration: Martial Law persists until a Player Character-driven Domain Action removes it (Influence vs Ob = Löwenritter Military ÷ 2, round up, minimum Ob 3) OR Theocracy Counter drops below 40 (Church threat recedes; Ehrenwall withdraws).
- Scope: Crown territories only. Hafenmark, Varfell, and Church territories are unaffected.

**Riskbreakers:** The extralegal arm of the Löwenritter. Operations are not recorded in official documents. See §9.3.

---

## 8.10 Schoenland (Spoiler Actor)



**Board game representation:** Territory 15. Modifies Trade orders. Game Master-driven.


---

## 8.11 Parliamentary Vote


1. Both sides roll relevant faction pools (typically Mandate for legitimacy claims, Influence for procedural contests)
2. Ob = opponent's relevant stat directly (1–7)
3. Best of **3 exchanges.** First side to win 2 exchanges wins.
4. If neither side wins 2 of 3 (draws possible when both meet Ob): motion fails by abstention — Thread Tension +1 and Theocracy Counter +1 (institutional paralysis)

---

## 8.12 Seasonal Accounting — Faction Phase

At the end of each campaign season (~4 sessions):

1. Apply pending Domain Action outcomes
2. Each faction rolls **Stability check**: pool = Stability score (d10s, TN 7)

| Situation | Stability Check Ob |
|---|---|
| Quiet season, no major events | 1 |
| One active threat (military, political, or economic) | 2 |
| Two concurrent threats | 3 |
| Active attack on Mandate or Wealth | 4 |
| Campaign-level crisis (war, heresy investigation, economic collapse) | 5 |

- Failure: Stability −1
- Overwhelming (net ≥ 2× Ob): Stability +1 (max 7)
- **Anti-death-spiral floor:** Faction at Stability 2 or lower is treated as Ob 4 regardless of actual pressure. Prevents immediate cascade; gives players a window to intervene.

3. Apply Thread Tension drift and all Thread Tension-lowering events
4. Check floors (Stability 0 = collapse event) and ceilings (Mandate or Stability 7 = dominance event)
5. Award CP for Domain Actions and personal goals
6. Apply Theocracy Counter changes from threshold conditions

---


<!-- NOTE: BG faction starting stats and BG-specific actions are in designs/board_game/board_game_v30.md -->
<!-- This doc covers: TTRPG faction stats, ethical frameworks, domain actions, unique actions, parliamentary procedure -->

