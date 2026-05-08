# VALORIA — How to Play a Campaign
## The complete sequence of play from character creation to victory or shared loss
## Mode: Videogame / Hybrid
## Date: 2026-04-15

---

# 1. STARTING THE GAME

## 1.1 Character Creation

You create one protagonist. You have 31 attribute points distributed across 10 attributes (minimum 1 each, maximum 5 for one attribute, 4 for the rest):

**Physical:** Agility (combat, stealth, escape), Endurance (health, stamina), Strength (damage, carrying).
**Mental:** Cognition (investigation, lockpicking, cover), Recall (history knowledge cap), Focus (Thread contact duration, concentration).
**Social:** Attunement (reading people, appraise), Bonds (relationship depth and count), Charisma (persuasion, composure).
**Metaphysical:** Spirit (all Thread operations, sincerity).

You choose up to 3 Histories (skills tied to your background) — each grants +1D when relevant. Your History cap equals your Recall score.

You choose a starting Certainty (0–5): 5 = Orthodox Solmundian, 0 = fully Thread-aware. Most characters start at 3–4. This determines how your character understands reality at the outset.

You choose or are assigned a faction alignment: Crown, Church, Hafenmark, Varfell, or unaligned. This determines your starting NPC relationships (same faction = Disposition +1, hostile faction = Disposition −2 to −3) and which faction's Domain Actions you can influence.

## 1.2 Thread Sensitivity

You do not start with Thread Sensitivity unless your background specifically grants it. Most characters begin at TS 0 — they cannot perceive threads at all. You gain TS through:

- **Encounter:** Entering a territory with active thread instability (Calamity radiation zone, typically territories adjacent to the Southernmost once MS drops below 60). First encounter grants TS 5–15 depending on severity.
- **Contact with a practitioner:** An NPC practitioner (Edeyja, Vaynard, Maret Uln) can intentionally expose you. Grants TS 10–20.
- **Traumatic revelation:** Witnessing a Gap formation, a Threadcut being, or a failed Thread operation. Grants TS 15–30.
- **Gradual exposure:** Extended time near the Southernmost or with Wardens. +5 TS per season of sustained proximity.

At TS 30+, you can Leap (enter Thread contact). Below that, you can perceive threads but not manipulate them. Your Thread Pool Score = TS ÷ 10, which replaces the +3 in the standard pool formula: your Thread pool is (Spirit × 2) + History + TPS.

**The decision of when and whether to pursue Thread Sensitivity is one of the game's central strategic choices.** It gives you access to the most powerful personal-scale system (Thread operations can modify the peninsula's most important clock, Metaphysical Stability) but costs you: each Thread operation degrades your Coherence (10 → 0), Church detection via the Attention Pool makes you a target for Heresy Investigation, and your Certainty shifts toward 0, potentially alienating Church-aligned NPCs.

---

# 2. THE SEASON

The game proceeds in seasons (4 per year). Each season has three phases that always occur in the same order.

## 2.1 Phase 1 — Personal Phase

This is the core gameplay loop. You move your character through the peninsula and take **scene actions**. A scene action is one of:

### What you can do:

**Move** to an adjacent territory (free — does not cost a scene action, but travel between non-adjacent territories takes additional scenes).

**Investigate** (Fieldwork). Choose an action:
- *Examine* — physical evidence. Pool: (Cognition × 2) + History + 3.
- *Interview* — question an NPC. Pool: (Charisma × 2) + History + 3. May trigger a social contest if the NPC is resistant.
- *Research* — study documents, records. Pool: (Recall × 2) + History + 3.
- *Surveil* — covert observation. Pool: (Attunement × 2) + History + 3. Grants +2 Evidence but also +2 Exposure (detection risk).
- *Thread-Read* — perceive thread state of a location or person (requires TS 30+). Pool: (Spirit × 2) + History + TPS.
- *Reconstruct* — piece together a narrative from gathered evidence. Pool: (Cognition × 2) + History + 3.

Each success advances the **Evidence Track** toward its threshold (Simple = 3, Complex = 5, Structural = 8). When the threshold is met, the investigation is complete — you have your finding, which can be used as Corroboration in a social contest, as political leverage, or as the trigger for an NPC arc.

**Why investigate?** Because information is power. Discovering Haelgrund's hidden Thread Sensitivity (TS 12) gives you leverage over the Church's most dangerous internal actor. Finding evidence of Varfell's secret Thread experiments gives Crown diplomatic ammunition. Investigation produces the facts that drive every political contest in the game.

**Socialize** (Fieldwork). Build or damage NPC relationships:
- *Connect* — attempt to improve Disposition. Pool: (Charisma × 2) + History + 3, Ob = max(1, base Ob − current Disposition). BUT: if your intent is instrumental (you're befriending them to extract information), you must pass the **Sincerity Gate** first — Spirit TN 7 Ob 1, 37% failure rate. Failure means the NPC detects your insincerity and Disposition does not improve.
- *Read* — Appraise an NPC's state. Pool: Attunement + Recall, Ob = floor(NPC's Charisma / 2) + 1. Success reveals their current Conviction, Certainty, Disposition toward you, and (on Overwhelming success) a pressure point.

Your Disposition with each NPC ranges from −4 to floor(Bonds/2)+1. At Disposition above +2, it decays −1 per season — deep relationships require maintenance. At maximum Disposition, you can form a **Knot** (a deep interpersonal bond that grants mechanical benefits: remote Thread-Read, emotional anchoring, +1 Coherence recovery).

**Fight** (Combat). Personal combat follows: both sides roll initiative (Combat Pool vs Combat Pool — higher net declares last). Each exchange, you split your Combat Pool (Agility × 2 + History + 3) between Offense and Defense dice. You can Strike, Feint (partial commitment — commit some dice to attack, keep the rest for defense, margin = dice opponent loses next round), Rescue (redirect an attack to yourself — no Defense, armor only, +2 Momentum on success), Escape, or use environmental Stunts.

Damage = net hits + Strength + weapon modifier − armor DR. Damage accumulates toward your Wound Threshold (Endurance + 6). At threshold: you take a Wound (−1D to all pools), counter resets. At max Wounds (floor(Endurance/2)+1): incapacitated.

**Debate** (Social Contest). Engage in formal argument. The adjudicator determines your primary attribute: Expert judge → Cognition, Crowd → Charisma, No adjudicator → Attunement. You choose one of four argument styles — each is a single choice, not two separate steps:
- **Precedent** (Memory + Revealing): cite what happened openly.
- **Suppression** (Memory + Obscuring): bury inconvenient history.
- **Vision** (Projection + Revealing): propose a transparent future.
- **Insinuation** (Projection + Obscuring): imply unstated consequences.

Each exchange: Appraise (read opponent) → Declare style → optionally Corroborate (spend gathered evidence for +1D) → Argue (roll your contest pool) → Resolve (compare results). The Piety Track moves toward your position or your opponent's. When one side hits 0 or 10, the contest ends. Composure (Charisma + 6) is your social health — take enough social damage and you're Rattled (+1 Ob) or Spent (−2D, must regroup).

**Perform Thread Operations** (requires TS 30+). Enter Thread contact (takes Focus score in rounds to establish). Choose an operation:
- *Weaving* — cohere a thread (strengthen/repair reality). TN 7.
- *Pulling* — open a thread (reveal hidden structure). TN 7.
- *POP* — temporal displacement (shift when something was). TN 8.
- *Locking* — freeze a thread state (preserve current reality). TN 8. Causes chronic MS drift.
- *Dissolution* — tear a thread (unmake something). TN 8. Risk of Gap formation.
- *Mending* — repair a Gap or wound in the substrate. TN 7, Depth Ob −1. Immune to opposition. This is the only way to directly restore Metaphysical Stability.

Your pool: (Spirit × 2) + History + TPS. Obstacle: three-axis system — Depth (how primordial the thread: Fibonacci 1, 2, 3, 5, 8, 13) + Breadth (how much you're affecting) + Distance (how far from your location). Each operation costs 1 Coherence (10 → 0). At Coherence 3: Dissonant (Spirit check or take consequences). At Coherence 0: Rendering Crisis (you can no longer render yourself as rendering — your consciousness fragments).

Every Thread operation automatically produces co-movement across all three dimensions (temporal, epistemic, actualized) per P-01. You can't touch one without touching all three.

**Stealth** (Fieldwork). Operate covertly:
- *Sneak* — move undetected. Pool: (Agility × 2) + History + 3.
- *Disguise* — assume a false identity. Pool: (Charisma × 2) + History + 3.
- *Sabotage* — damage infrastructure. Pool: (Cognition × 2) + History + 3.

Your **Cover** (Cognition + best concealment History) determines how long you can operate before detection. Cover 3 = detected in 3 scenes. Cover 9 = a full season. Cover 12+ = near-immune to casual detection. Your **Exposure** accumulates as you act — at certain thresholds, you're Watched, Suspected, or Identified, which triggers Church Attention Pool advancement and potential Heresy Investigation.

### Between scenes

After each scene action, consequences resolve immediately:
- Evidence Track advances (if investigating).
- Exposure may increase (if acting covertly).
- NPC Disposition may change (if socializing).
- Wounds/Stamina change (if fighting).
- Coherence decreases (if performing Thread operations).
- Church Attention Pool may advance (if Thread operations were visible).

You then choose your next scene action or end the Personal Phase.

## 2.2 Phase 2 — Strategic Phase

After the Personal Phase, the game zooms out to the peninsula level. Every faction acts simultaneously.

### Your faction's turn

If your character holds faction leadership (or advises the leader), you issue one **Domain Action** by playing a card from your faction's hand of 6. Each card type enables different actions:

| Card | Actions Enabled | Cooldown |
|------|----------------|----------|
| Legionary | Muster, Battle, Fortify | 1 season |
| Senator | Assert (Church CI +1), Suppress (negate CI passive), Parliamentary Manoeuvre | 1 season |
| Consul | Govern (Mandate recovery, Accord maintenance), Diplomacy, Trade | 1 season |
| Tribune | Investigate (covert), Spy, Counter-Intelligence | 1 season |
| Pontifex | Heresy Investigation, Excommunicate, Graduated Seizure | 2 seasons |
| Prefect | Survey, Establish Presence, Fortify | 2 seasons |
| Colonist | Cultural Reformation (Varfell acquisition tool) | 2 seasons |
| Diplomat | Crown Treaty, Negotiate Alliance | 1 season |
| Recess | No action; all other cards recover from cooldown | 0 |

Cards on cooldown cannot be played. Playing Recess recovers all cards but wastes your action this season. Each faction has domain expertise — Crown gets +1D on Legionary actions, Church on Senator, Hafenmark on Consul/Prefect, Varfell on Tribune.

**Pool for Domain Actions:** Your relevant faction stat (Mandate, Influence, Wealth, Military, or Stability) as the dice pool, rolled against the action's Ob.

### Specific procedures:

**Generating a Casus Belli:** You need a Casus Belli to declare war or perform hostile military actions. Sources: (1) An NPC faction occupies your territory — automatic CB. (2) A faction violates a treaty — automatic CB. (3) Parliamentary motion accusing a faction — requires Senator card, Parliamentary Manoeuvre, succeed at Ob = opponent's Influence ÷ 2 + 1. (4) Discovery of hostile covert action (via Investigation) — triggers CB against the acting faction. CB persists until used or the provocation is resolved diplomatically.

**Negotiating a Treaty:** Play Diplomat card. Diplomacy pool vs Ob = floor(target faction's Mandate / 2) + 1. Degree of success determines treaty strength: Success = minor terms (single territory, trade agreement). OW = major terms (multiple territories, military alliance, succession arrangement). Both parties must agree — NPC factions evaluate treaties through their AI priority stack (framework-aligned treaties get −1 Ob acceptance). Treaties are binding — violation generates automatic CB for the aggrieved party. Treaty types: Minor Cession (−1 Stability for ceder), Major Cession (−2), Capitulation (−3).

**Calling a Parliamentary Session:** Play Senator card. Parliamentary Manoeuvre at Ob = opponent's Influence ÷ 2 + 1. Parliament votes = each faction's Mandate as voting power. Church gets +floor(CI/20) bonus votes. Factions opposing Church get −floor(CI/30) effective votes. Motions can: censure a faction (Mandate −1), approve a Crown Treaty, authorize military action, or challenge Church authority (costs an extra action at CI ≥ 65). Political Stability advances +1 if the session involves inter-faction conflict.

**Governing a territory:** Play Consul card. Govern pool vs Ob = floor(territory Prosperity / 2) + 1. Success: recover Mandate (if capital) or maintain/improve Accord. OW: Accord +1 OR Prosperity +1. Failure at Prosperity 0: Stability −1. You MUST govern conquered territories or their Accord decays toward Revolt (0).

**Mustering troops:** Play Legionary card. Muster pool (Military) vs Ob from muster table. Success: create a unit with Size based on territory Prosperity (Prosperity 0–1 = Size 2, 2–3 = Size 3, 4 = Size 4), Power = floor(Military/2)+1, Discipline = floor(Military/2)+1. Units persist until destroyed.

### NPC faction turns

All NPC factions execute their AI priority stacks simultaneously. Each NPC leader evaluates their 7-level priority tree from top to bottom, takes the first applicable action. You see the results — Himlensendt Asserts (CI +1), Baralta Governs Gransol, Vaynard Investigates a rival territory, Ehrenwall monitors the border.

### Institutional Mandate

When a Domain Action directly challenges a faction's core institutional authority AND that faction's Mandate ≥ 4, the targeted faction may **Appease** (cancel the action at Mandate −1 cost) or **Uphold** (let the action proceed). NPC factions Appease if Mandate ≥ 4 AND Stability ≤ 3.

## 2.3 Phase 3 — Accounting

Everything resolves in fixed order. This is the season's climax — the consequences of your choices collide with every NPC faction's choices simultaneously.

### Step 1: Domain Echoes

Personal Phase scenes with Sufficient Scope (actions that had territory-level consequences) produce faction stat changes:
- Overwhelming success: ±2 to relevant faction stat.
- Success: ±1.
- Partial success: narrative consequence only.
- Failure: −1.

### Step 2: Clock Advancement

**Metaphysical Stability:** −1 per year baseline (so −0.25 per season approximately, applied at year-end). Additional losses from Thread operations, battles, Gap persistence. Mending and Community Weaving restore +1 to +2 per success.

**Church Influence:** Conditional passive +1 if Church controls Himmelenger (T9) AND Stability ≥ 3. Plus: Piety Yield from Church-aligned territories (weighted by Spiritual Weight). Plus: +1 per Assert action. Minus: Suppress negates the passive. Cap: ±5/season total, ±3 from Domain Actions. Milestones at 40 (Church Assertive: +1D Assert/Seizure), 55 (Church Prominent: opposing factions +1 Ob), 65 (Church Dominant: extra action to oppose Church in Parliament), 80 (Church Ascendant: Seizure Ob −1, Piety drift +1/year), 100 (Theocracy Unification attempt).

**Invasion Pressure:** +2 per season with inter-faction battle. Diplomatic engagement with Altonia can reduce. At 100 + weak border defense = Altonian Conquest (shared loss).

**Political Stability:** +1 per season with inter-faction battle. +2 per faction elimination. +1 per territory Revolt. −1 per peaceful season. −1 per diplomatic resolution. Thresholds: 3–4 = Tension (Mandate check Ob 1), 5–6 = Fracture (Accord −1 in one territory), 7–8 = Crisis (Accord −1 all non-capitals), 9–10 = Collapse (Accord cap 2, MS −1/season).

### Step 3: Threshold Events

Check all clock thresholds. If MS dropped below a band boundary (80/60/40/20), Calamity radiation expands — territories at the new distance from the Southernmost begin experiencing thread instability. If CI hit a milestone (40/55/65/80), Church political power increases. If Political Stability reached a threshold, Accord degrades across the peninsula.

### Step 4: Territory Updates

- **Accord checks:** Territories at Accord 1 without a garrison → Accord drops to 0 (Revolt). Territories at Accord 0 = Uncontrolled — garrison must fight Uprising (Military vs Ob 2) or territory flips.
- **Piety drift:** Territories with Church presence drift toward Piety 4. Territories with RM presence drift toward Piety 0. Rate: +1 or −1 per year (applied at year-end Accounting).
- **Prosperity:** Governed territories maintain Prosperity. Ungoverned territories at Accord ≤ 1 risk Prosperity decline. Territories under blockade: Prosperity −2/season.
- **Occupation costs:** Occupying a foreign territory: Wealth −1/territory/season, Accord −1/season (populations resist occupation).

### Step 5: Faction Accounting

- **Wealth from trade:** Territories at Prosperity ≥ 2 AND Accord ≥ 2 contribute +1D to Trade pool at Accounting.
- **Card recovery:** Cards with 1-season cooldown are available again. Cards with 2-season cooldown recover if played 2+ seasons ago. Playing Recess last season recovers all.
- **Stability check:** If faction suffered 2+ attribute losses this season, roll Stability pool vs Ob = total losses. Failure: Stability −1. If Stability reaches 0: faction dissolved — territories become Uncontrolled, Mandate drops to 0.

### Step 6: Victory Check

Check all victory conditions:
- **Universal Peninsular Sovereignty:** Control all 15 territories with Accord ≥ 2 each, Political Stability ≤ 6, maintained for 2 consecutive seasons. Any faction can achieve this.
- **Faction alternates:** Church Theocracy (CI 100 + specific territory control). Crown Diplomatic Unification. Varfell Thread Mastery / Southernmost Dominion / Partition. Hafenmark Parliamentary Sovereignty. RM Cultural Revolution (Piety ≤ 1 in 8+ territories + MS ≥ 40).
- **Shared losses:** Rupture (MS 0 — everyone loses). Altonian Conquest (IP 100 + weak defense — everyone loses). Anarchy (all factions dissolved — everyone loses).

If no victory or shared loss, the next season begins.

### Year-End (every 4th season)

Additional year-end effects:
- MS baseline decay: −1.
- Piety drift resolves (±1 per territory based on faction presence).
- Disposition above +2 decays −1 (deep relationships erode without maintenance).
- Coherence recovery: +1 for non-practicing practitioners. +1 additional from Knot Anchoring.
- Church Attention Pool resets to 0 in all territories.

---

# 3. ZOOMING IN AND OUT

## 3.1 When you zoom in (board state → personal scene)

The game zooms into a personal scene when board-level events demand personal resolution:

- **NPC arc moment:** An NPC's conviction is wounded, their Certainty shifts, or their loyalty track crosses a threshold. The game presents a personal scene where you interact with that NPC at their crisis point.
- **Territory crisis:** A territory reaches Accord 0 (Revolt), triggering a scene where you witness or participate in the uprising. A territory's Piety reaches an extreme, triggering a religious confrontation.
- **Clock threshold:** MS crosses a band boundary — you experience the Calamity spreading to new territories. CI hits a milestone — you witness Church institutional power increasing (Inquisitors arriving, Piety enforcement).
- **Discovery:** You find evidence of Thread activity, a Warden contact site, a hidden NPC truth (Haelgrund's secret TS, Lenneth's reformist sympathies).
- **Player-initiated:** You can choose to zoom in on any territory you're present in to explore, investigate, or pursue personal objectives.

## 3.2 When you zoom out (personal scene → board state)

After a personal scene concludes, you return to the strategic layer. Your scene outcomes produce Domain Echoes — personal victories translate to faction stat changes (±1 or ±2 depending on success degree). You then continue with the season's remaining phases.

## 3.3 Domain Echo in detail

When your personal action had Sufficient Scope (it affected something beyond just you), the result echoes upward:

- You won a critical social contest against Himlensendt about Church overreach → Influence +1 for your faction, CI advancement slowed.
- You successfully investigated Varfell's secret Thread lab → your faction gains the evidence as diplomatic leverage (can be used as Casus Belli or Corroboration in Parliament).
- You mended a Gap in a territory → MS +1 to +2, that territory's thread instability decreases.
- You failed to prevent a Church Graduated Seizure → the territory flips to Church control at Accord 1, your faction loses Territory Value.

---

# 4. HOW SEASONS CONNECT

## 4.1 Continuity between seasons

Everything persists:
- NPC Dispositions carry forward (but decay above +2).
- Faction stats carry forward (modified by Accounting).
- Territory states carry forward (Accord, Piety, Prosperity, Fort Level all persist).
- Your Wounds heal between seasons (full recovery unless narrative dictates otherwise).
- Your Stamina and Composure reset to full.
- Your Coherence does NOT reset — it recovers +1/season (non-practice) + 1 (Knot Anchoring if applicable).
- Your Exposure resets per-territory at year-end (Church Attention Pool resets).
- Card cooldowns tick down.
- Evidence Track persists across seasons (you can continue an investigation over multiple seasons).

## 4.2 What changes year to year

Each year (4 seasons), the game's macro state shifts:
- MS declines by at least 1 (baseline) + any additional Thread/battle losses.
- CI advances by at least 4 (conditional passive, if not Suppressed).
- IP accumulates from any battles.
- Political Stability resets toward 0 in peaceful periods, climbs in violent ones.
- Calamity radiation may have expanded (if MS crossed a threshold).
- NPC factions have gained or lost territories, stats, and internal stability.

The early game (Years 1–3) is exploration and positioning. The mid game (Years 4–7) is factional competition intensifying. The late game (Years 8+) is convergence — victory conditions become achievable, shared losses become threatening, and every decision is consequential.

---

# 5. INTERACTING WITH THE WORLD

## 5.1 NPCs and factions

NPCs are not quest-givers. They are political actors with their own convictions, goals, and priorities. Your relationship with them evolves through the Disposition system (−4 to floor(Bonds/2)+1). You build relationships through genuine social interaction (Connect actions, Sincerity-gated) or instrumental manipulation (Read actions, investigation, leverage).

Each NPC has convictions (what they believe), pressure points (what can change their mind), and beliefs (specific commitments they'll defend). To shift an NPC's position, you must identify their pressure point and present evidence or consequences that engage it — Evidence against Himlensendt's Faith conviction, Consequence against Almud's Order conviction, Loyalty against Ehrenwall's national-survival priority.

When an NPC's conviction is wounded (through failed defense of their beliefs in a contest, or through confrontation with undeniable evidence), their behavior changes. Wound 0 = they act on conviction. Wound 1 = they act on their unaddressed conviction. Wound ≥ 2 = Crisis table — the NPC may fundamentally change their arc.

## 5.2 Territories

Each territory has: Accord (population acceptance 0–4), Piety (religious orientation 0–4), Prosperity (economic health 0–4), Fort Level (fortification 0–4), Spiritual Weight (fixed — determines CI flow), and potentially active investigations, NPC presence, and Calamity radiation effects.

You interact with territories by being physically present — moving there, investigating, socializing with local NPCs, performing Thread operations, or participating in governance. Your faction interacts with territories through Domain Actions (Govern, Muster, Fortify, etc.).

## 5.3 The Southernmost

The Southernmost (Askeheim, T15) is the epicenter of the Einhir Catastrophe. It is permanently at Piety 0. The Wardens (led by Edeyja) maintain it through constant Mending. Visiting the Southernmost is the most reliable way to gain Thread Sensitivity but also the most dangerous — Threadcut beings, Gap formations, and substrate instability are constant threats. Edeyja (TS 75–80, Coherence 9) is the game's most powerful practitioner and the primary source of Thread knowledge.

---

# 6. REFERENCE: WHAT CAN GO WRONG

**Shared losses** — ways everyone loses:
- **Rupture** (MS 0): The substrate tears open at the Southernmost. The Calamity repeats. Peninsula-wide catastrophe.
- **Altonian Conquest** (IP 100 + weak defense): The Empire invades through the mountain passes. Valoria is reconquered.
- **Anarchy** (all factions dissolved): No functional governance remains. The peninsula collapses into permanent civil war.

These are always live threats. MS decays every year. IP climbs with every battle. Political Stability climbs with every military action. The game's existential question is always: can anyone win before everyone loses?
