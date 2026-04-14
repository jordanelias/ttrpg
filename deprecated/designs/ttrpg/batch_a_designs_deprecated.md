<!-- DEPRECATED -->
> **DEPRECATED — 2026-04-11**
> Phase 1 design briefs (2026-03-25, Session 4). Content absorbed into params files and compilation/v0.14/. Superseded.
> Do not use as a canonical source.

---

# Phase 1 — Batch A: TTRPG Core Gap Designs
## Date: 2026-03-25 (Session 4)
## Status: Design briefs for editorial review

---

## G-053: CP Spending Menu Expansion

### Problem
Current CP sinks: attribute advancement (score × 3 CP) and History advancement (3 CP/point). Two options. Players accumulate CP with nothing interesting to spend it on.

### Design

| Purchase | Cost | Constraint | Notes |
|----------|------|-----------|-------|
| Attribute +1 | Current score × 3 CP | Max 5 per attribute | Unchanged |
| History +1 (beyond test track) | 3 CP | Cap = Memory score | Unchanged |
| New History at 0 points | 5 CP | Must narrate origin scene; requires Game Master scene | Establishes eligibility; no pool bonus at 0 |
| New Inspiration at 1 point | 4 CP | Total Inspiration value ≤ Spirit; must name focus and narrate two pursuit scenes | Faster than the freeform "two scenes + two rolls" path |
| Inspiration +1 point | 3 CP | Individual cap = Spirit; total ≤ Spirit | Alternative to scene-based recovery |
| New Knot (establish) | 2 CP | Total significant Knots ≤ Bonds score | Formalizes a relationship the player wants tracked |
| Knot +1 strain capacity | 3 CP | Max strain capacity per Knot = 5 | Hardens a relationship against breaking |
| Circles +1D (permanent) | 4 CP | Max bonus = Presence score | Represents expanding social network |
| Resources +1D (permanent) | 4 CP | Max bonus = Presence score | Represents improving economic standing |
| Remove 1 Wound | 6 CP | Between seasons only; requires narrative (healer, rest, Thread intervention) | Emergency long-term recovery |
| Approach Training | 8 CP | Thread Sensitivity ≥ 30; must have witnessed ≥1 Thread operation; replaces mentorship/breakthrough paths | CP-gated alternative to existing acquisition paths |

### Design rationale
- CP costs scale: cheap (2–3) for relationship/social investment, moderate (4–5) for capability expansion, expensive (6–8) for recovery and rare unlocks.
- All purchases have narrative requirements — CP alone is never sufficient. This prevents "spreadsheet advancement."
- Approach Training at 8 CP is deliberately expensive — it should feel like a campaign milestone, not a shopping decision.
- No CP purchase for Thread Sensitivity growth, Intelligibility recovery, or Certainty recovery. These are play-driven, not purchasable.

### Canon compliance
- P-01 (inseparability): CP spending doesn't bypass co-movement. Thread operations still produce Thread Depth/Thread Tension effects regardless of how Approach Training was acquired.
- P-09 (memory pull = messy): New Histories require narrated origin — no clean mechanical acquisition.

---

## G-040: Inspiration Acquisition and Recovery Mid-Campaign

### Problem
Current rules: new Inspiration requires "two scenes of pursuit + two Spirit rolls." Recovery = full scene engaged with focus gives +1 point. No procedure for what happens when an Inspiration's focus is destroyed, captured, or fundamentally changed.

### Design

**New Inspiration (mid-campaign):**
1. Player declares intent and names the focus.
2. Two scenes where the character actively engages with the focus (Game Master confirms engagement is genuine).
3. After each scene: Spirit check TN 7, Ob 1.
   - Both succeed: Inspiration established at 1 point.
   - One succeeds, one fails: Inspiration established at 1 point, but with a Complication Tag (Game Master assigns a narrative condition — e.g., "contingent on Lenneth's approval," "only while in Valorsplatz").
   - Both fail: Focus is not yet crystallized. Player may retry next season with new scenes.
4. **CP shortcut:** 4 CP + one scene of genuine engagement + one Spirit check. On success: established at 1 point, no Complication Tag. On failure: 4 CP spent, retry next season.

**Recovery (from reduced value):**
- Full scene engaged with the focus: +1 point. Unchanged.
- If focus is physically present and uncontested: automatic +1, no roll. (Seeing your daughter safe after a battle restores Duty to Family without a dice check.)
- Maximum recovery per season: 2 points per Inspiration (prevents instant full restoration).

**Focus destroyed or permanently lost:**
- Inspiration drops to 0 immediately.
- Player may convert to a new Inspiration with a different focus through a **Grief Scene**: one scene of genuine reckoning + Spirit check TN 7 Ob 2. Success: new Inspiration at the old value −1 (minimum 1). The new focus must relate to the loss. Failure: Inspiration lost entirely; CP refunded at half value (round down).
- [EDITORIAL: Is half-CP refund on permanent loss correct, or should the loss be total? Total loss is harsher but more dramatic.]

**Inspiration earned through play (no CP):**
- Completing a Belief can convert it to an Inspiration at 1 point (existing rule, retained).
- An Non-Player Character whose Impression Track reaches 5 can become an Inspiration focus (new — connects Impression Track to Inspiration economy).

### Canon compliance
- P-09 (memory pull = messy): Complication Tags on imperfect acquisition. Grief Scene for lost focus.
- P-12 (relational contagion): Impression Track → Inspiration conversion means relationships have mechanical weight.

---

## G-054: Circles/Resources Redesign

### Problem
Circles and Resources are currently identical in structure (Presence + History, TN 7, Ob table, test-track advancement). They're mechanically interchangeable. The S2 editorial decision requires them to be History-based, faction-linkable, and degradable.

### Design

**Circles (revised):**
- **Pool:** Presence + highest applicable History bonus. (Not "any relevant History" — must be the most relevant single History to the network being accessed.)
- **Faction linkage:** Each Circles roll is implicitly or explicitly within a faction's social sphere. Positive Reputation with that faction: +1D per 2 Reputation points. Negative: −1D per 2 Reputation points.
- **History specificity:** "Court Connections" gives full bonus for Crown/Church circles. "Street Network" gives full bonus for Guilds/Revolution/Niflhel circles. A History that doesn't connect to the target faction provides no bonus — raw Presence only.
- **Degradation:** When a Circles contact is burned (betrays, is killed, is exposed through your actions), mark one **Network Damage**. At 3 Network Damage within a faction: −1D permanent to Circles within that faction. Network Damage clears at rate of 1 per season of non-hostile activity within that faction.
- **Advancement:** Test-track system unchanged, but tracked per-faction (each faction's Circles advances independently through use).

**Resources (revised):**
- **Pool:** Presence + highest applicable History bonus. "Merchant Guild Member" → full bonus. "Soldier" → no bonus for economic transactions.
- **Faction linkage:** Faction leaders may roll faction Wealth instead of personal Resources for faction-appropriate expenditure (existing rule, retained). Non-leaders may access faction Resources at +1 Ob if they have positive Reputation with the faction.
- **Tax (revised from Burning Wheel model):**
  - On Partial at any Ob: −1D to next Resources roll this season (temporary strain).
  - On Failure at Ob 3+: −1D permanent until recovered through income event, commerce Domain Action, or seasonal accounting.
  - On Failure at Ob 5: −2D permanent. Economic standing seriously damaged.
- **Recovery:** One successful Resources roll at Ob ≤ 2 during seasonal accounting restores 1 lost die. Alternatively: a full season of commerce-focused activity (no other Domain Actions) restores all lost dice.
- **Degradation from external events:** Territory conquered → all characters with Resources tied to that territory lose 1D permanent. Faction collapse → all characters with Resources tied to that faction lose 2D permanent.

### Design rationale
- History specificity prevents "Circles is just a general social stat." Your network is your past.
- Faction linkage makes Reputation mechanically load-bearing — it's not just flavor.
- Degradation from external events connects personal economics to faction-scale play (cross-scale integration).
- Tax model creates meaningful risk on expensive rolls without making Resources useless.

### Canon compliance
- P-01 (inseparability): Resources degradation from territory conquest = co-movement at economic level.
- P-12 (relational contagion): Network Damage propagates consequences through social connections.

---

## G-048: Resources Degradation on Failed Rolls

### Problem
Subsumed into G-054. The Burning Wheel tax model is incorporated into the Resources redesign above.

### Design
See G-054 Tax section. Summary:
- Partial at any Ob: −1D temporary (this season).
- Failure at Ob 3+: −1D permanent until recovered.
- Failure at Ob 5: −2D permanent.
- Recovery: successful Ob ≤ 2 roll during accounting, or full season commerce activity.

**Gap status: Resolved via G-054.**

---

## G-034: Fortification / Base Building

### Problem
No rules for establishing, improving, or benefiting from fortified positions. Sieges (G-047) need something to besiege.

### Design

**Fortification levels (territory property, 0–3):**

| Level | Name | Benefit | Build Cost | Build Time |
|-------|------|---------|-----------|-----------|
| 0 | Unfortified | None | — | — |
| 1 | Palisade | Defenders: +1D to Cohesion checks; attackers: +1 Ob to assault | Wealth Ob 2 | 1 season |
| 2 | Stone walls | Defenders: +2D Cohesion, +1D attack from walls; attackers: +2 Ob assault, cannot Flank | Wealth Ob 4 | 2 seasons |
| 3 | Citadel | Defenders: +3D Cohesion, +2D attack, garrison can hold at half strength; attackers: +3 Ob, siege required | Wealth Ob 5 + 1 season maintenance per year | 4 seasons |

**Building procedure:**
1. Faction leader or territory governor commits to construction via Domain Action.
2. Pay Wealth Ob per table. Partial: construction begins but costs +1 season. Failure: resources spent, no progress.
3. During construction: territory produces half income (labor diverted).
4. Construction can be interrupted by enemy military action — progress lost if territory changes control.

**Fortification damage:**
- Successful siege: fortification drops 1 level.
- Overwhelming assault victory: fortification drops 2 levels.
- Deliberate demolition (own territory): 1 season, no roll. May be done to deny fortification to conqueror.

**TTRPG personal-scale interaction:**
- Characters inside a fortification during siege: +1D to all defensive rolls from cover.
- Characters attempting to infiltrate a fortification: Ob = fortification level + garrison commander's Intelligence ÷ 2.
- Fortifications provide Circles bonus (+1D) for finding military contacts within.

### Canon compliance
- P-07 (Calamity = rendered-side): Fortifications are rendered-side infrastructure. Their destruction is a material event with co-movement consequences (garrison morale, civilian displacement, Thread Tension effects if Einhir site present).

---

## G-047: Siege Mechanic

### Problem
The VG doc describes siege at strategic level (1–3 seasons, Sortie/Relief/Negotiate). No TTRPG-scale procedure exists.

### Design

**Siege declaration:** An attacking force with Military ≥ defender's garrison Military may declare siege on a fortified territory (Level 2+). Level 0–1 territories are assaulted directly, not besieged.

**Siege phases (one per season):**

Each season of siege, both sides choose one action:

**Attacker options:**
| Action | Roll | Effect on success |
|--------|------|------------------|
| Starve | Military Ob = Fortification level | Defender: −1 Endurance to garrison; −1 Stability to controlling faction |
| Assault | Military Ob = Fortification level + 2 | If Overwhelming: walls breached, mass combat next round at −1 Ob for attacker. If Success: breach attempted, mass combat at standard Ob. |
| Sappers | Intelligence Ob = Fortification level + 1 | Fortification −1 level (undermining). Detected on Partial/Failure: defender gets free Sortie. |
| Negotiate | Influence vs defender's Mandate | Success: conditional surrender terms. Overwhelming: unconditional. |
| Thread bombardment | Practitioner Weaving, scale = Relational+, Ob = Fortification level | Thread Tension +2 regardless of outcome. Success: garrison Cohesion −2. Overwhelming: walls partially dissolved (Fortification −1). Failure: practitioner takes Thread Depth +3. |

**Defender options:**
| Action | Roll | Effect on success |
|--------|------|------------------|
| Hold | Cohesion Ob 1 | Garrison holds. No losses. |
| Sortie | Military Ob = attacker garrison ÷ 2 | Success: attacker loses 1 unit or −2D to next siege action. Failure: sortie force destroyed. |
| Relief call | Circles/Influence Ob 3 | Summons allied force. Arrives in 1–2 seasons. |
| Counter-negotiate | Influence vs attacker's Stability | Success: attacker accepts terms. Overwhelming: attacker withdraws (Mandate −1 for attacking faction). |
| Sabotage | Intelligence Ob = attacker Military ÷ 2 | Success: attacker supply disrupted, −1D to next action. |

**Siege end conditions:**
- Defender Stability reaches 0: garrison surrenders.
- Fortification reaches 0: walls breached; mass combat resolves.
- Attacker withdraws (voluntary or forced by Relief).
- Negotiated settlement: both sides agree on terms (territory control, tribute, prisoner exchange).

**Personal-scale during siege:**
- PCs inside may: run espionage (Intelligence Domain Action), negotiate with besiegers (Social scene), attempt escape (Agility + relevant History Ob = fortification level), perform Thread operations (standard rules; siege does not prevent contact).
- PCs outside may: infiltrate (Agility/Intelligence Ob = fortification level + garrison commander bonus), join assault, perform Thread operations against walls.

**Co-movement during siege:**
- Each season of siege: Thread Tension +1 (concentrated suffering and disruption).
- Einhir site within fortification: +1 additional Thread Tension per season (proximity to active Thread site under stress).

### Canon compliance
- P-01 (inseparability): Siege Thread Tension drift. Even purely military events affect Thread state.
- P-07 (Calamity): Siege is a rendered-side catastrophe with Thread consequences.
- P-14 (all modes): Siege operates at mass combat scale but permits personal-scale zoom-in.

---

## G-052: Player/Game Master Transition Reference Guide

### Problem
Valoria is Game Master-intensive. The system has no guidance for: (a) new GMs taking over mid-campaign, (b) rotating Game Master duties (one player GMs faction turns, another GMs personal scenes), (c) transitioning from TTRPG to board game mode within a session.

### Design

**Part 1: Game Master Knowledge Requirements**

| Category | What the Game Master must know | Where it lives |
|----------|----------------------|----------------|
| World state | Thread Tension, Theocracy Counter, Institutional Pressure values; faction attribute scores; territory control | Faction Dashboard (single sheet) |
| Hidden information | Intelligence scores; Non-Player Character Thread Sensitivity values; pending Heresy investigations; Niflhel operative identities | Game Master Notes sheet (separate from Dashboard) |
| Character state | Player Character attributes, Histories, Beliefs, Inspirations, Knots, Thread Sensitivity, Wounds | Character sheets (player-held) |
| Pending events | Clock threshold events queued; Domain Echo consequences pending; seasonal accounting items | Session Log (running document) |
| Campaign arc | Current Beliefs (tells Game Master what scenes to create); active factional conflicts; Altonian Clock position | Campaign Summary (1-page document updated each season) |

**Part 2: Game Master Handoff Procedure**

When Game Master duties transfer (permanently or for a session):

1. **Outgoing Game Master writes a Handoff Brief** (template provided):
   - Current season and year
   - All faction attribute scores (including hidden Intelligence)
   - All Non-Player Character Thread Sensitivity values and Heresy investigation stages
   - Pending clock events
   - Active Player Character Beliefs (with notes on which scenes are planned)
   - Any unresolved rulings or ambiguous situations
   - Tone notes: "this campaign is currently [grim/hopeful/tense/exploratory]"

2. **Incoming Game Master reads Handoff Brief + Faction Dashboard + Campaign Summary.** No other documents required for immediate play.

3. **First session under new Game Master:** Run a "low-stakes" session (personal scenes, social encounters, investigation) to calibrate tone. Avoid mass combat, clock thresholds, or major factional events until the new Game Master has one session of calibration.

**Part 3: Rotating Game Master Protocol**

For tables that rotate Game Master duties by scale:

| Scale | Who GMs | When |
|-------|---------|------|
| Personal scenes | Primary Game Master (or designated personal-Game Master) | TTRPG phase |
| Faction/strategic turns | Strategy Game Master (may be a player whose character is not a faction leader) | Board game / strategic phase |
| Mass combat | Either Game Master; whoever has more familiarity with disposition table | When mass combat fires |
| Thread operations | Primary Game Master (Thread state is complex) | Whenever Thread ops occur |

**Rotating protocol:** At each scale transition (Zoom In, Zoom Out, Register Shift), the table pauses for 30 seconds. The outgoing scale-Game Master states: current faction scores, pending consequences, and any hidden information the incoming scale-Game Master needs. The incoming scale-Game Master confirms receipt and begins.

**Part 4: TTRPG ↔ Board Game Mode Transition (within session)**

| Step | Action | Time |
|------|--------|------|
| 1 | Game Master announces mode transition and names the trigger | 10 seconds |
| 2 | Record current state: Player Character positions, pending actions, Belief progress | 1 minute |
| 3 | If entering board game: lay out Faction Dashboard, territory map, Order cards | 2 minutes |
| 4 | If entering TTRPG: clear board game components, identify the personal scene's participants and location | 1 minute |
| 5 | Confirm all players understand what their role is in the new mode | 30 seconds |
| 6 | Begin play in new mode | — |

**Total transition time target: under 5 minutes.**

### Canon compliance
- P-05 (three modes distinct): Transition guide respects mode boundaries — no mechanical bleed during transition.
- P-14 (all modes express inseparability): The handoff procedure ensures Thread Tension/Thread Depth/co-movement state transfers between GMs and between modes.

---

## BATCH A SUMMARY

| Gap | Status | Editorial flags |
|-----|--------|----------------|
| G-053 | Designed | Approach Training CP cost (8 CP — correct?) |
| G-040 | Designed | Half-CP refund on permanent Inspiration loss (or total loss?) |
| G-048 | Resolved via G-054 | None |
| G-054 | Designed | Per-faction Circles tracking (adds bookkeeping — acceptable?) |
| G-034 | Designed | None |
| G-047 | Designed | Thread bombardment during siege (Thread Tension +2 automatic — correct severity?) |
| G-052 | Designed | None |

**Editorial decisions needed: 3**
1. G-053: Is 8 CP correct for Approach Training, or should it be higher/lower?
2. G-040: When an Inspiration's focus is permanently destroyed and the Grief Scene fails, should half CP be refunded or should the loss be total?
3. G-054: Per-faction Circles advancement adds tracking per faction per Player Character. Is this acceptable bookkeeping, or should Circles remain a single unified track?

**Gaps resolved this batch: 7 (6 designed + 1 subsumed)**
