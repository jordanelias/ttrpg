# VALORIA — EMERGENT ARC SKELETON TEST — BATCH 5
## Session: 2026-04-17 | Continuation of Batches 1-4
## New surfaces: Mass Combat World Bridge (§D.1-D.3), Named Unit Officers, post-battle consequence scenes, General death stages, Command pool formula, Southernmost military restriction, Formation/Tactic card interactions, Thread in mass battle (Phase 4 vs 5), Woven unit brittleness, Coherence depletion over battle duration, all faction victory conditions, Löwenritter Regency, RM Phase 2 Cultural Uprising, Church Seizure Accord formula, Partition Pressure marker, Warden Cooperation RS recovery, effective hegemony, BG tactic card faction specifics
## Does NOT repeat NEW-S1 through NEW-S63 from Batches 1-4

---

## CATEGORY AM: MASS COMBAT WORLD BRIDGE × SETTLEMENT SYSTEMS

---

### NEW-S64: NAMED UNIT OFFICER → SETTLEMENT GOVERNOR PIPELINE

```
Root: §D.2 Named Unit Officers: officer at Disposition ≥ +2 after battle → eligible as settlement governor
      Officer Disposition shifts: +1 for sound commands/saving retreats; −1 for Size losses ≥ 2; −1 for player absence
      Officer death roll: 1d10 ≤ Size lost → officer killed
      Settlement governor (settlement_layer §3.2): assigned after battle = "ROTK post-conquest appointment"

PLAYER LEADS ASSAULT ON S-019 SPARTFELL FORTRESS (T10, HAFENMARK-CONTROLLED)
│
├─ BATTLE SETUP:
│   Player's Crown force: 1 Heavy Infantry unit (Size 5, Power 4, Command = player's Command stat)
│   Player Command: ⌈(Charisma 4 + Cognition 4) ÷ 2⌉ = 4
│   Named officer assigned at Muster: "Captain Aldric" (Conviction: Order, from Crown faction)
│   Starting Disposition: +1 (mustered into player's faction)
│
├─ BATTLE OUTCOMES THAT BUILD OFFICER DISPOSITION:
│   Turn 1: player uses Concentration tactic (Ob 1, sound call) → succeeds → +1 Disposition (Aldric: +2)
│   Turn 2: unit takes 2 Size losses (down to 3) from Hafenmark crossbow fire
│   Officer death roll: 1d10 ≤ 2 → on rolls 1 or 2: Aldric killed (20% chance)
│   Assume Aldric survives (rolls 3+): Disposition +1 if player chose a saving action (Shield Wall) that limited casualties
│   But: player may have ordered the assault knowing the unit would take damage
│   → If Size loss was ≥ 2 AND player ordered it: Disposition −1 (net: no change from saving action)
│
├─ POST-BATTLE AFTERMATH SCENE (§D.1, mandatory, Priority 0):
│   Player chooses "Survey the damage" (Cognition Ob 1)
│   Success: reveals exact casualties, infrastructure damage, one hidden consequence
│   → Hidden consequence at S-019 Spartfell Fortress: a Hafenmark officer who did NOT flee
│     is present in the surrender scene — this is an NPC with Disposition 0 toward player
│     who could be either: a problem (Hafenmark loyalist who resists occupation)
│     OR an opportunity (disgruntled officer open to recruitment)
│
├─ OFFICER-TO-GOVERNOR TRANSITION:
│   Aldric at Disposition +2: meets eligibility threshold for governor assignment
│   Settlement: S-019 Spartfell Fortress (Defense 3, Order 3, Prosperity 1)
│   Player assigns Aldric as governor
│   → Fortress type: Löwenritter natural manager → Aldric (Crown officer, Order conviction) fits
│   → Military efficiency: Defense +1 passive (per settlement_layer §3.3 subnational: Löwenritter type)
│     But Aldric is Crown, not Löwenritter → no passive Defense bonus
│   → Standard Crown governor: Order priority → Pacify → Develop → Fortify (settlement NPC AI)
│
├─ OFFICER-AS-COMPANION ELIGIBILITY:
│   After 3 seasons of service (Disposition +2, 3+ prior scenes):
│   Aldric Disposition now: +2 (barely eligible; needs +1 more for companion eligibility)
│   Player has been in 3 battles with Aldric → 3 "scenes" counted
│   Connect action next season: Bonds Ob 2 → if success: Disposition +3 → companion eligible
│   Formation Ob for Aldric companion: floor(Crown loyalty ÷ 2) + 1 = floor(4÷2)+1 = Ob 3
│   → Officer-as-companion is harder than civilian companion (military loyalty is high)
│
├─ OFFICER DEATH DURING GOVERNORSHIP:
│   If Aldric is assigned as governor AND the player later returns to battle in the same territory:
│   §D.2: "companion-officer still commands their unit in battle — dual role"
│   → Aldric fights AND governs: during battle, he is a Contested Figure (named NPC in combat)
│   → If Aldric dies in this second battle:
│     "departure scene fires as a combat death, not a social departure"
│     Settlement governor: VACANT immediately (combat death ≠ departure scene delay)
│     Knot consequences if Knotted (possible at Disposition +3+): Knot becomes dormant
│     → Settlement unmanaged: Order −1/season begins at NEXT Accounting (combat death timing)
│
└─ THREE-WAY SYNERGY:
    Mass battle (build Disposition with officers) → post-battle scene (confirm survivor, find hidden NPC)
    → governor assignment (military officer as settlement administrator) → companion formation (if Disposition built)
    → remote investigation through Knot (if companion Knotted)
    → the entire arc from battle to intelligence network passes through a single named officer
    Each step is specified in a different design document; none specifies this full chain explicitly
```

**New emergence:** The officer-to-governor-to-companion pipeline creates a specific cross-system arc that turns military success into political infrastructure. The officer death roll (1d10 ≤ Size lost) creates a persistent risk at each stage — an officer at Disposition +3 who dies takes the companion slot, settlement governance, and remote investigation access with them.

---

### NEW-S65: POST-BATTLE CONSEQUENCE SCENE × SETTLEMENT ORDER × PLAYER MORALE EFFECT COMPOUND

```
Root: §D.1 Aftermath scene: "Address the population" — Charisma Ob 2: Success → Settlement Order +1; Failure → Order −1
      §D.3 Player Morale Effect: units in player's territory gain +1 Discipline while player present
      §D.3: if player wounded (2+ wounds) or incapacitated during battle → all friendly units −1 Discipline immediately
      Settlement Order → Province Accord derivation

PLAYER TAKES 2 WOUNDS DURING THE ASSAULT ON S-019, THEN ADDRESSES THE POPULATION
│
├─ DURING BATTLE:
│   Player takes 2 wounds → all friendly units: −1 Discipline immediately (morale shock)
│   Heavy Infantry Discipline: 4 → 3 (reduced by player wound shock)
│   Player's pool: −1D from first wound (standard wound penalty, combat_v30)
│   → At reduced pool, player's combat contribution weakens
│   → Battle may still be won (Command still operative while conscious; wounds add +1 Ob to tactic rolls)
│
├─ POST-BATTLE AFTERMATH SCENE (mandatory, free):
│   Player selects "Address the population" (Charisma check, Ob 2)
│   Player's Charisma pool: (Charisma × 2) + History
│   BUT: player is Wounded (2+ Wounds) → scene action budget −1 modifier applies NEXT season
│   Does wound penalty apply to the aftermath scene's social roll?
│   → Wound −1D applies to combat rolls; social fieldwork is unaffected by physical wounds (fieldwork §2.2)
│   → Player can roll full social pool despite wounds
│   → Charisma 4: pool 8 + History vs Ob 2 → ~90% success
│
├─ ADDRESS THE POPULATION — OUTCOMES:
│   Success: Settlement Order +1 (Spartfell Fortress: Order 3 → 4)
│   → Province Accord recalculation: T10 has S-019 (Order 4) + S-020 (Order 2) → floor((4+2)/2) = 3 (Aligned)
│   → Military conquest normally produces Accord 1 (peninsular_strain §2.3, §D.1 settlement anchoring)
│   → BUT: the aftermath scene gives Order +1 BEFORE the Accounting that sets Accord
│   → Settlement Order 4 + 2 = average 3 → Province Accord = 3 (Aligned) despite military conquest
│   → TIMING QUESTION: does the aftermath scene's Order +1 apply before or after Accord is calculated?
│   → [GAP NEW-OI-41]: Aftermath scene applies at Province level (Priority 0 scene within battle resolution)
│     Does its Order +1 effect apply before Accounting's Accord derivation?
│     If YES: player can partially negate military conquest's Accord 1 penalty through immediate aftermath speech
│     If NO: Accord derives first (at 1), then Order +1 applies (Order 4 feeds next season's Accord = 3)
│
│   Failure (20% chance): Settlement Order −1 (Order 3 → 2)
│   → Province Accord: floor((2+2)/2) = 2 (Compliant) — but with Accord 1 from military conquest:
│     the Accord from conquest (1) vs settlement-derived Accord (2) creates a conflict
│   → If Accord 1 is a hard set (conquest overrides settlement derivation for 1 season):
│     next season governance is needed to restore Accord above 1
│
├─ OVERWHELMING AFTERMATH (net ≥ 2×Ob AND net ≥ 3 at Ob 2):
│   Settlement Order +1 AND +1 Renown
│   → Province Accord 3 (Aligned, via Order improvement)
│   → Territory grants: defender +1D (Aligned), full Effective Prosperity
│   → Essentially: the aftermath speech transforms conquered territory from contested to aligned in one action
│   → This is the fastest non-military Accord improvement available
│   → Compare to Govern action (Administer, Ob 2, Attunement): same Ob but different attribute pool
│
└─ PLAYER MORALE COMPOUND IN BG MODE:
    §D.3 BG: if PC embedded during battle → friendly units +1D on first battle roll (stacks with Commander bonus)
    Player was in T10 during the assault: +1D on Crown's first battle roll
    This first roll represents Volley Phase (Phase 2 equivalent in BG)
    → Crossbow units with +1D Volley = substantially higher Size reduction on Hafenmark defenders
    → Spartfell Fortress (Defense 3) already partially vulnerable; +1D could produce BG Success vs Partial
    → BG Success outcome (§B.3): territory captured; Defender Military −1
    → Player's physical presence in BG terms produces both the +1D AND the aftermath scene access
    → BG absence: BG resolution fires (no aftermath scene); Territory captured but Order impacts unavailable
    → The player who is PRESENT gets both tactical bonus AND governance opportunity; BG-only play gets neither
```

**New emergence:** The aftermath scene's Order +1 interacts with the timing of Accord derivation to potentially negate the military conquest Accord 1 penalty — if the Order change applies before Accounting. The player's physical presence in battle is doubly valuable: tactical (+1D in BG or Command in TTRPG) and governmental (aftermath scene access). BG-only resolution loses both the aftermath scene and the potential Order recovery.

---

## CATEGORY AN: GENERAL DEATH STAGES × COMMAND POOL FORMULA

---

### NEW-S66: GENERAL TWO-STAGE DEATH × BILATERAL PERSONAL COMBAT × COMMAND COLLAPSE

```
Root: General two-stage death: Stage 1 (incapacitated) → −1 Morale all units, Command halved, Morale floor suspended
      Stage 2 (killed): fires at start of following turn's Phase 5 if not stabilised (Medicine Ob 2 in 1-turn window)
      Bilateral general personal combat: both armies fight uncommanded (1D minimum per unit, Line formation, no tactics)
      Wounds carry over: wounds from personal combat add +1 Ob to Command tactic execution rolls

PLAYER GENERAL (PC) CHALLENGES NPC GENERAL TO PERSONAL COMBAT DURING MASS BATTLE
│
├─ SETUP:
│   Player enters personal combat in Phase 5 (Contested Figure duel, Scenario 14)
│   NPC general simultaneously enters personal combat with player (both sides declare)
│   → BILATERAL GENERAL PERSONAL COMBAT fires (§A.5 PP-506)
│   Both armies fight uncommanded simultaneously
│
├─ UNCOMMANDED ARMY CONSEQUENCES:
│   Both forces: PP-273 floor = 1D minimum per unit (not Effective Combat Pool)
│   Both forces: Line formation only (no tactics available)
│   → Units with Power 5 (Elite) at 1D minimum — all formation advantage lost
│   → Any flank the player had set up disappears; the formation advantage resets
│   → A Crown Heavy Infantry unit (normally Power 4, effective pool ~7-8D): now 1D
│   → Hafenmark Light Infantry (Power 3, effective pool ~5-6D): now 1D
│   → The armies are equal in effectiveness regardless of Power differential
│   → This is the "heroic duel equalizer" — personal combat between generals levels the battlefield
│
├─ DURATION AND TIMING:
│   Personal combat duration: 1–5 exchanges (maximum before forced disengage)
│   Each exchange = 1 mass battle turn (per Scenario 14)
│   During 5 exchanges: armies fight at 1D for 5 turns in Line vs Line
│   Casualties accumulate despite reduced effectiveness (1D vs TN 7 Ob various)
│   → Expected damage per turn at 1D: ~25% hit rate → slow attrition during the duel
│
├─ PLAYER WINS PERSONAL COMBAT (NPC general defeated):
│   NPC general: Stage 1 (incapacitated) OR Stage 2 (killed) depending on degree
│   If Stage 1: NPC general's Command halved + Morale floor suspended
│   Player must stabilise or kill in 1 turn (Phase 5) otherwise Stage 2 fires next turn
│   → If player lets the NPC die (no mercy): Stage 2 fires → NPC's army: Command = 0
│   → Command 0: all units fight at 1D minimum indefinitely (still no Command)
│   → Rout check: §A.12, Recall Ob 2 (but Command = 0 → no Command check possible)
│   → Army routs automatically without a general (Command 0 = no Morale floor)
│   Domain Echo: "Named NPC defeated" → Faction Mandate −2 + NPC arc trigger (per Domain Echo table)
│
├─ PLAYER TAKES WOUNDS DURING DUEL:
│   Wounds carry over: each wound → +1 Ob to Command tactic execution rolls
│   Player exits personal combat with 2 wounds → all future tactic rolls: +2 Ob
│   Player's Command (value 4): tactic rolls now Ob = tactic Ob + 2
│   → Concentration (Ob 1) becomes Ob 3; Hammer & Anvil (Ob 3) becomes Ob 5
│   → High-Ob tactics (Ambush Ob 4, Feigned Retreat Ob 3) become nearly impossible with wounds
│   → Player's tactical effectiveness sharply reduced despite winning the duel
│
├─ RE-ESTABLISHING COMMAND:
│   After personal combat resolves: Command check Ob 2 in Phase 1 of next turn
│   Player Command = 4 → pool 4 dice vs Ob 2 → ~85% success
│   But with 2 wounds: Command pool is unaffected (§A.5: Coherence does not affect Command; wounds DO)
│   Wait — wounds add +1 Ob to tactic EXECUTION rolls, not to the Command re-establishment check
│   → Re-establishment check uses Command dice (not affected by wounds per spec)
│   → Player re-establishes Command normally despite wounds
│   → Once established: tactic execution is wound-penalized, not Command itself
│
└─ THE BILATERAL GAMBLE:
    Player entering bilateral personal combat takes: 5 turns of uncommanded army risk
    + personal wound risk (tactics penalized)
    + personal combat 1-exchange-per-turn limit
    Against: NPC general elimination → permanent Command 0 army rout
    Net calculation: worth it if armies are otherwise evenly matched (bilateral levels field)
    AND if player is confident of winning personal combat within 2-3 exchanges (before army attrition matters)
    NOT worth it if the enemy army is significantly stronger (bilateral doesn't help if they have more units)
    → The bilateral gamble is optimal only in close battles, not disadvantageous ones
    → Players who are outmatched should AVOID personal combat (it doesn't help enough)
    → Players who are winning should ALSO avoid it (they lose their advantage during the duel)
    → The optimal personal combat trigger: rough parity where the general duel tips the balance
```

**New emergence:** The bilateral general personal combat mechanic creates a narrow strategic window where personal combat is genuinely optimal — close battles where the general duel tips the balance. Both the "winning" and "losing" player should avoid personal combat in asymmetric battles. The wound-carries-over penalty creates a lasting cost even for victorious duels.

---

## CATEGORY AO: SOUTHERNMOST MILITARY × VICTORY CONDITIONS

---

### NEW-S67: SOUTHERNMOST MILITARY RESTRICTION × RM PHASE 2 × PRACTICAL FORCE COMPOSITION

```
Root: §A.11 Southernmost: units dissolve without awareness on entry if TS < 30 (remove from map, no Morale trigger)
      Only RM communities and Varfell forces with VTM ≥ 2 can field meaningful military forces there
      RM Phase 2 Cultural Uprising: Weaver Thread pool vs Ob = TC ÷ 10; WC ≥ 2 adds +1D
      WC (Warden Cooperation) ≥ 2: RS decay rate halved; ≥ 3: RS +2/season

THE SOUTHERNMOST AS AN INVERTED MILITARY DOMAIN
│
├─ FORCE COMPOSITION ANALYSIS BY FACTION:
│   Crown: standard armies (Heavy Infantry TS 0) → dissolve on entry
│   Church: Templar-level forces (Templar TS: not specified — religious training ≠ Thread sensitivity)
│   → Templars almost certainly TS 0 (Church is TS-suppressive): dissolve on entry
│   Hafenmark: standard forces → dissolve
│   Guilds, Niflhel: standard forces → dissolve
│   Varfell (VTM ≥ 2): some practitioners → TS 30+ fraction of force survives
│   RM: community Weavers (TS 30+) → survive; non-practitioner RM members → dissolve
│   Edeyja/Wardens: TS 50+ → survive (full operational capacity)
│   Player practitioner (TS 30+): survives; companions with TS 30+ survive
│
├─ VARFELL PATH B MILITARY IMPLICATION:
│   Deed 1 requires garrison or Tribune in T15 (Southernmost)
│   Tribune = intelligence agent (not a military unit → no TS requirement)
│   Garrison = military unit → must survive entry → requires TS 30+ soldiers
│   At VTM 2: Varfell has "Thread awareness sufficient" but not necessarily TS 30+ forces
│   → VTM measures Vaynard's personal TK, not force TS composition
│   → VTM 2 unlocks the expedition but doesn't guarantee garrison viability
│   → Varfell must specifically RECRUIT practitioner-capable soldiers (RM sympathizers, Warden contacts)
│   → This is a force composition challenge: not just Muster (which produces standard Power-based units)
│   → [GAP NEW-OI-42]: How does Varfell raise units with TS ≥ 30 capability?
│     Standard Muster produces units at Power = floor(Military÷2)+1 with no TS qualifier
│     Special recruitment mechanic needed for Southernmost-viable forces
│
├─ RM PHASE 2 UPRISING × MILITARY DEFENSE:
│   After T9 transfers to RM administration:
│   "Church cannot perform Territorial Seizure on T9 while RM holds it: Seizure Ob +3"
│   But: RM has Military 0 (no military forces)
│   Church can still attempt MILITARY seizure (Battle, not Territorial Seizure)
│   → Church's Templar units enter T9 (not Southernmost): no TS restriction applies
│   → Battle: Templar force vs RM resistance (RM Military 0 → no units to deploy)
│   → RM cannot field military → loses the Battle without a roll (no defending units)
│   → T9 falls to Church military conquest: Accord 1, PT may shift
│   → BUT: "Church cannot Seize while RM controls" ≠ "Church cannot Battle for T9"
│   → RM Phase 2 is only stable if another faction (Crown, Hafenmark, Varfell) militarily defends T9
│   → RM victory requires political coordination for military defense it cannot provide itself
│
├─ WARDEN COOPERATION AS MILITARY ENABLER:
│   WC ≥ 2: RS decay halved (world-scale benefit)
│   WC ≥ 3: RS +2/season at Accounting (powerful RS recovery)
│   But also: WC ≥ 1 adds +1D to ALL Thread operations peninsula-wide
│   → Players building Warden Cooperation gain: RS recovery + Thread combat bonus in all battles
│   → In Southernmost battles: Warden cooperation directly enables military viability
│   → Outside Southernmost: +1D Thread bonus improves practitioners' combat contributions
│   → WC ≥ 2 halved RS decay: combined with Community Weaving, effectively arrests RS decline
│   → This makes Warden relationship investment the highest-return single track in the game
│     (affects RS, Thread combat, Varfell Path B, RM Phase 2, and potentially Edeyja Arc B)
│
└─ ALTONIAN VANGUARD × SOUTHERNMOST:
    Altonian Vanguard (IP ≥ 75): standard military force → TS 0 → cannot enter Southernmost
    → If Altonian Vanguard advances along the peninsula coast toward T13/T15:
    → T15 is a military dead zone for standard forces
    → Vanguard cannot garrison T15 or use it as a staging point
    → This limits Altonian invasion to T10→T8→T1 western approach and T3→T1 northern approach
    → T15 Southernmost is simultaneously: the most contested non-military space AND the most secure from invasion
    → Player who moves Thread operations to T15 is tactically safe from Altonian military threat
    → Edeyja's Warden control of T15 is not just metaphysical — it's the peninsula's only militarily inviolable position
    → [ARC 7: Southernmost] as military sanctuary: practitioners who need to operate without Altonian interference
      can base operations from T15 with complete military safety (Altonian forces dissolve on entry)
```

**New emergence:** The Southernmost TS restriction creates a complete military inversion — the most contested spiritual/political space is simultaneously the most militarily secure for practitioners. RM Phase 2 victory is structurally dependent on other factions providing military defense that RM cannot provide. Warden Cooperation is revealed as the highest-return single track in the game, affecting five distinct system dimensions.

---

## CATEGORY AP: THREAD IN BATTLE × COHERENCE DEPLETION PLANNING

---

### NEW-S68: THREAD IN MASS BATTLE × 7-TURN COHERENCE ARITHMETIC × POSITIONING RACE

```
Root: §A.10: Battle scale Thread Ob and Coherence auto-cost:
      Skirmish → Personal scale, TS 30, Ob 2, Coherence 0/op
      Battle → Territorial scale, TS 50, Ob 4, Coherence −1/op
      Co-movement at mass battle scale: general loses Phase 5 action d3 turns; Command −1 for d3 turns; takes 1 Wound
      "A practitioner operating every turn of a 7-turn battle loses 7 Coherence." → Coherence 3 after 7 turns (Fragmented)

PRACTITIONER WITH TS 60 OPERATES AT BATTLE SCALE FOR MAXIMUM EFFECT
│
├─ COHERENCE PLANNING:
│   Starting Coherence: 10 (full)
│   Battle scale: −1/operation (Territorial scale auto-cost)
│   7-turn battle, 1 operation per turn: Coherence 10 → 3 (Dissonant, then Fragmented at turn 8 if continued)
│   BUT: Phase 4 operations fire BEFORE Phase 5 Engagement
│   → Practitioner's operation pool is unaffected by Coherence until below 4
│   → At Coherence 4 (turn 7): +1 Ob on ALL Thread operations including Leap
│   → Turn 7 operation: Ob 4 (Battle Territorial) + 1 (Coherence Fragmented) = Ob 5
│   → With TS 60 TPS 6: pool = (Spirit×2) + History + 6 → likely 13-15 dice vs Ob 5
│   → Success rate at Ob 5 with 14 dice: ~85% — still effective but visibly degraded
│   → Turn 8 (if battle continues): Coherence 3 (Fragmented), +1 Ob → Ob 6
│   → Success rate at Ob 6 with 14 dice: ~70% — significant degradation
│
├─ CO-MOVEMENT AT BATTLE SCALE:
│   Each operation fires co-movement (P-01)
│   Mass battle co-movement (§A.10 COMOVE-P2-01):
│   → Temporal result: general loses Phase 5 action for d3 turns
│   → Epistemic result: Command −1 for d3 turns
│   → Actual result: general takes 1 Wound
│   These are the TEMPORAL, EPISTEMIC, and ACTUAL auto-effects at mass battle scale
│   Per 7 operations: expected 7 co-movement events
│   → Temporal (each): average 1.5 turns lost Phase 5 action → ~10.5 turns of Phase 5 inability (impossible in 7-turn battle)
│   Wait: "loses Phase 5 action for d3 turns" — does this mean consecutive or cumulative?
│   If cumulative: 7 co-movements = ~10.5 Phase 5 actions lost (more than the battle's turns)
│   If independent rolls (each fires independently, not stacking): most turns the general loses Phase 5
│   → Either way: the general who threads every turn barely participates in Phase 5 (personal combat, mass engagements)
│
│   → Epistemic (each): Command −1 for d3 turns → cumulative −7 Command potential over 7 turns
│   Command 4 general: by turn 4-5, expected accumulated Command −4+ = effectively Command 0
│   → All units: beyond Command limit → 1D minimum → effectively the same as bilateral general absence
│   → A general who threads every turn DESTROYS their own Command through co-movement
│
│   → Actual (each): +1 Wound per operation → 7 operations = 7 Wounds
│   Combat Wound threshold (Endurance 4): incapacitation at 3 Wounds
│   → 7 Wounds while incapacitation threshold is 3: general is incapacitated by Turn 3's co-movement at the latest
│
├─ THE OPERATIONAL CEILING:
│   At Battle scale, a practitioner operating EVERY TURN:
│   → Incapacitated (3+ Wounds from co-movement Wound) by Turn 3-4
│   → Command collapsed from epistemic Command −1 stacking
│   → Phase 5 actions lost from temporal co-movement
│   → Thread effectiveness: still high (Coherence fine until Turn 7-8)
│   CONCLUSION: Thread operations at Battle scale have a HARD operational ceiling of 2-3 turns
│   before co-movement creates collapse even for TS 70+ practitioners
│
├─ OPTIMAL BATTLE THREAD STRATEGY:
│   Use Thread operations selectively: 2-3 per battle maximum
│   Choose the HIGHEST-IMPACT turns (Turn 1-2 for initiative advantage; Turn 5+ for rout prevention)
│   Position in Rear (Reserve, not front line): Phase 4 safe window
│   Don't use Thread if Command will be degraded by co-movement
│   Collective operations: helpers in Reserve (§A.10); helpers only lose 1 Coherence per op (not wound)
│   → Anchor + 2 helpers: Anchor takes wounds and Command loss; helpers are safe
│   → This is why collective operations (§2.5) are optimal for sustained battle Thread use
│
└─ WOVEN UNIT BRITTLENESS (§A.14):
    Thread-Woven Discipline boost on a unit: if unit takes Size loss > Discipline in single turn
    → GM may rule the Woven configuration shatters into a Shifting Object
    → The Shifting Object persists until Mended (Ob 2, next battle?)
    → Thread Gaps from battle (§A.10 EDGE-05): registered on territory card at resolution
    → Each battle in T10 Spartfell that involves Thread Weaving:
      creates risk of persistent Shifting Objects in the territory
      → RS drain: Micro-Gap persisting to Accounting = RS −1 per
    → A practitioner who Weaves military units generates RS-costing artifacts from every brittle unit loss
    → The military benefit (Discipline boost) risks producing the war's secondary Thread damage
```

**New emergence:** The co-movement system at Battle scale imposes a hard operational ceiling of 2-3 Thread operations per battle before the Wound and Command degradation cascades make the general combat-ineffective. This is the correct design consequence: Thread in battle is powerful but self-limiting. Woven unit brittleness creates RS-draining Shifting Objects as a side effect of military Thread use.

---

## CATEGORY AQ: VICTORY CONDITIONS × PLAYER STRATEGY

---

### NEW-S69: LÖWENRITTER REGENCY × SUCCESSOR CONFIRMATION × RS GATE RACE

```
Root: Löwenritter Regency Establishment: TCV ≥ 10, TC < 50, IP < 60, RS > 40, PI ≥ 4, Successor confirmed (Elske OR Torben Loyalty ≥ 6)
      If Regency not achieved in 8 Löwenritter seasons → Military Consolidation becomes available (TCV ≥ 16, Military ≥ 5, RS > 35, TC < 60)
      Both conditions require RS thresholds

LÖWENRITTER WINS COUP (COUNTER = 3), ENTERS REGENCY PURSUIT
│
├─ REGENCY ESTABLISHMENT CONDITION ANALYSIS:
│   TCV ≥ 10: Crown starts at 12; Löwenritter inherits Crown territories → immediately achievable
│   TC < 50: starting TC 28, Baralta's structural suppression gone → TC rises ~+2/season
│   → TC reaches 50 in ~11 seasons (28 + 11×2 = 50) — tight timeline
│   IP < 60: starting IP 5; Löwenritter less diplomatically capable than Crown → IP rises faster
│   → IP at +2/season baseline: reaches 60 in ~28 seasons — not the binding constraint
│   RS > 40: starting RS 28 — BELOW the threshold from game start
│   → RS > 40 requires RAISING RS from 28 to 41+ (RS recovery of +13 before conditions align)
│   → Without sustained Mending: RS continues declining (winter −1, Locks −1 to −2/season)
│   → RS going UP while all other pressures increase is the hardest condition
│   PI ≥ 4: Coup starts at PI +3-4 → PI threshold likely met immediately after coup
│   Successor confirmed: Elske confirmed OR Torben Loyalty ≥ 6
│
├─ THE SUCCESSOR CONFIRMATION RACE:
│   Torben Loyalty: transferred to Löwenritter at coup, currently ≤ 3 (declining under Altonian influence)
│   Löwenritter Intel Domain Action (covert contact maintenance): harder than Crown (Military-primary faction)
│   → Torben Loyalty recovering from ≤ 3 to ≥ 6 requires: sustained Intel success AND Torben retrieval
│   → At Löwenritter's Intel capability (lower than Crown): contact maintenance fails more often
│   → Torben Loyalty ≥ 6 may be unreachable without player assistance
│   Elske confirmation: Parliamentary path (faster, requires Hafenmark cooperation)
│   → Hafenmark Disposition toward Löwenritter (post-coup): hostile (Baralta opposed the coup)
│   → Elske confirmation requires convincing Hafenmark to cooperate → social investment needed
│
├─ RS > 40 AS THE BINDING CONSTRAINT:
│   RS at 28: must reach 41+ for Regency condition (RS > 40)
│   Sources of RS recovery: Mending (+1 to +2/success), Community Weaving (+1 to +2), Warden Cooperation ≥ 3 (+2/season)
│   Sources of RS loss: winter −1/season, Lock drift, active Gaps, battle RS costs (−1 per Campaign battle)
│   Löwenritter's post-coup military operations: battles → RS −1 per battle
│   → A militaristic faction pursuing Regency through military consolidation DESTROYS the RS condition it needs
│   → Löwenritter must: fight to hold territories (IP control, defend against Altonian Vanguard)
│     AND NOT fight in ways that burn RS
│   → Only battles defending against external invasion (Altonian Vanguard) are "acceptable" (they don't increment IP further)
│   → Inter-faction battles: IP +2 per season, Strain +1, RS −1 → strictly prohibited for RS recovery
│
├─ THE 8-SEASON WINDOW:
│   If Regency not achieved in 8 seasons: Military Consolidation available (TCV ≥ 16, Military ≥ 5, RS > 35, TC < 60)
│   Military Consolidation is EASIER (RS > 35 vs > 40; TC < 60 vs < 50; no Successor requirement)
│   → Löwenritter has an incentive to fail Regency quickly (within 8 seasons) to access Military Consolidation
│   → A player who is Löwenritter-aligned can deliberately NOT confirm a Successor
│     (neither Elske nor Torben Loyalty ≥ 6) for 8 seasons → Military Consolidation unlocks
│   → This is the "intentional failure to unlock easier path" strategy
│   → It requires: holding TCV ≥ 16 (more territory needed) and Military ≥ 5 (military investment required)
│   → But: RS > 35 is easier to achieve than RS > 40 (only need to arrest RS decline partially)
│
└─ PLAYER ROLE IN REGENCY:
    Player at Standing 3+ (Counselor) in Löwenritter post-coup:
    Duty: "Governance — maintain Accord in assigned territories" (prevents RS burning through Territory Revolt)
    Duty: "Diplomacy — negotiate Elske's confirmation" (the path to Successor condition)
    Player's Knot/relationship with Edeyja (Warden Arc B): unlock WC ≥ 3 → RS +2/season
    → Warden Cooperation ≥ 3 + player Mending: RS can rise at +3 to +4/season effective rate
    → RS 28 → 41 in ~4-5 seasons with full cooperation
    → Within the 8-season window for Regency, RS > 40 is achievable with player investment
    → Without player investment: RS continues declining → only Military Consolidation is viable
    → The player's Thread/Warden investment directly determines which Löwenritter victory path is available
```

**New emergence:** The Löwenritter Regency's RS > 40 threshold is the binding constraint — below the starting RS of 28, requiring active RS recovery. The "intentional failure to unlock Military Consolidation" strategy shows that victory condition design can create counterintuitive optimal play (deliberately failing one condition to access an easier one). Player Thread/Warden investment is the determinant of which Löwenritter path is viable.

---

### NEW-S70: CHURCH + HAFENMARK PARTITION PRESSURE MARKER × ONE-SEASON WARNING

```
Root: Church + Hafenmark Partition (ED-304, §3.2): triggered when Crown Mandate ≤ 1, TC ≥ 50, Church ≥ 2 territories, Hafenmark ≥ 3, no active military conflict between them
      Partition Pressure marker (ED-338, PP-566): placed if all conditions EXCEPT TC ≥ 50 are met → other factions have 1 season to disrupt before TC threshold check fires
      Incompatible co-victories: Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM

THE PARTITION PRESSURE MARKER AS STRATEGIC ALARM
│
├─ MARKER PLACEMENT CONDITIONS:
│   Crown Mandate ≤ 1: Crown has been systematically weakened (Parliamentary Censure campaign, Territory loss)
│   Church controls ≥ 2 territories: TC reached 75, Graduated Seizure fired twice
│   Hafenmark controls ≥ 3 territories: Dynastic Proclamations succeeded, TCV at 3+ acquired territories
│   No active Church-Hafenmark military conflict: the two factions have not battled each other
│   TC is currently at 45-49 (just below 50 threshold) → Partition Pressure marker placed
│
├─ THE ONE-SEASON WINDOW:
│   Marker placed at Accounting: all factions see it publicly (it's a public marker per PP-566)
│   Next season: if TC crosses 50 with all conditions still met → Partition fires
│   → One season for other factions to disrupt ANY of the five conditions
│
├─ DISRUPTION OPTIONS BY CONDITION:
│   Disrupt Crown Mandate ≤ 1: Crown Mandate recovery → Institutional Consolidation (+1 if clean season)
│   But: Crown Mandate 1 → 2 takes at minimum 1 clean season (no Triggers 1-5)
│   Crown in this state has likely been losing territories → Trigger 1 fires constantly
│   → Near-impossible to recover Crown Mandate from 1 to 2 in 1 season under military pressure
│
│   Disrupt TC crossing 50: Suppress Church TC this season (Mandate vs Ob = floor(5÷2)+1 = Ob 4)
│   Baralta's Structural Suppression: TC −1/season (if Baralta Mandate ≥ 4)
│   But wait: Baralta IS part of the Partition condition (Hafenmark controls ≥ 3 territories → Baralta benefits)
│   → Does Baralta suppress TC to prevent the Partition she's building toward?
│   → If Baralta wants the Partition: she suppresses only enough to prevent TC from crossing 50 prematurely
│   → The Partition marker exists because Hafenmark is NOT blocking TC this season (intentional)
│
│   Disrupt Hafenmark territory control: Declare war on Hafenmark (Varfell, Crown, or Löwenritter)
│   → Creates active military conflict WITH Hafenmark → breaks the "no active Church-Hafenmark conflict" condition
│   → But: Partition requires no Church-Hafenmark conflict, not no other-faction conflicts
│   → Varfell attacking Hafenmark: disrupts Hafenmark's territory control (Military battle → Accord 1 on captured)
│   → But Varfell-Hafenmark conflict also: IP +2, Strain +1, RS −1 → collateral costs
│
│   Disrupt Church territory (simplest?): Another faction recaptures a Church-seized territory
│   → Requires Military battle vs Church's Templar-defended territory
│   → Church uses Fortitude Cardinal (military response) → hard battle
│
├─ PLAYER INTERVENTION OPPORTUNITY:
│   Player at Standing 3+ in ANY non-Partition faction: 1 season to disrupt
│   Optimal disruption: file Emergency Parliamentary Censure against BOTH Church AND Hafenmark
│   Censure Church: Mandate −1, Stability −1 → Church Stability might drop to ≤ 3 (losing Territorial Seizure capacity)
│   Censure Hafenmark: Mandate −1 → if Hafenmark Mandate drops below 4, Dynastic Proclamation becomes harder
│   But: dual Censure requires 2 Parliamentary motions in 1 season
│   Parliament §5.2: max 3 active motions per Accounting → dual Censure is possible
│   → Player Parliamentary Intent: +1D to both motions via prior evidence
│   → Double Censure + player evidence: disrupts both sides of the Partition simultaneously
│
└─ WHEN PARTITION FIRES (if player fails to disrupt):
    Church + Hafenmark victory: "Partition Pressure" → conditional victory for both (ED-304)
    Crown faction: effectively eliminated from victory (its Mandate is ≤ 1, no recovery)
    Varfell: not in the Partition → still pursuing own victory condition
    → Post-Partition world: Church (ecclesiastical authority) + Hafenmark (constitutional governance) divide the peninsula
    → TC freezes at 75 (already frozen since TC ≥ 75 triggered phase transition earlier?)
    Wait: TC ≥ 50 is the Partition condition; TC freezes at 75 (the phase transition for seizure)
    → If TC is at 50-74: it hasn't frozen yet; Partition fires before the phase transition
    → This is a "premature victory" scenario: Church wins before reaching its strongest seizure state
    → Church + Hafenmark Partition is actually Church's SECOND-BEST outcome
    → Church's best: Primary Victory with TCV ≥ 8 and PT ≥ 3 in all territories
    → Partition gives Church victory without needing all that PT work
```

**New emergence:** The Partition Pressure marker is a one-season public warning that creates a coalition-building moment: every non-Partition faction simultaneously wants to disrupt it. The "double Censure" Parliamentary intervention (against both Church and Hafenmark simultaneously) is the player's cleanest single-season disruption. The Partition paradoxically benefits Church even before its strongest seizure state — making the Partition a genuinely tempting early-game play for Church.

---

### NEW-S71: VARFELL PATH A INTELLIGENCE HEGEMONY × "STATS FULLY REVEALED" × CONTESTED INVESTIGATION

```
Root: Varfell Path A: TCV ≥ 10, VTM ≥ 3, at least 2 rival factions' stats fully revealed, ≥ 1 territory outside starting 4
      "Stats fully revealed" — not defined precisely in victory_v30; Varfell Intel actions (Tribune Investigate) reveal hidden stats
      Contested Investigation (§4.6): rival factions can conceal stats against investigation

VARFELL PURSUES PATH A — THE INTELLIGENCE HEGEMONY VICTORY
│
├─ "STATS FULLY REVEALED" DEFINITION GAP:
│   The condition is not precisely defined in victory_v30
│   Candidates: (a) all 5 stats revealed for 2 factions, (b) Military and Wealth revealed (the most strategically relevant), (c) any intel action that surfaces faction state
│   Varfell Intel actions: Tribune Investigate (Intel vs Ob = floor(target Intelligence÷2)+1)
│   Each success: one hidden stat revealed
│   → To fully reveal Crown (5 stats: Mandate, Influence, Wealth, Military, Stability): 5 successful Intel actions
│   → At Intel pool of 5 (Varfell starting) and Ob 3 (average): ~65% per action
│   → Expected 7-8 actions for 5 stats → roughly 2 seasons of dedicated Intelligence Domain Actions
│   → 2 factions fully revealed: ~4 seasons of dedicated Intel work
│   → [GAP NEW-OI-43]: Define "fully revealed" for Path A — all 5 stats or a subset?
│
├─ RIVAL CONCEALMENT OPTIONS:
│   Church/Crown may use Domain Actions to obscure their stats (no specific rule exists)
│   Contested Investigation (§4.6): applies to personal fieldwork but also potentially to BG-level intelligence?
│   → If rival factions can "run Concealment" against Varfell Intel: Ob increases
│   → Varfell Shadow Intel tactic card: "see opponent's tactic card before revealing yours"
│   → This implies intelligence advantage in battle, but not necessarily in stat revelation
│   Niflhel Priority 3: "Tribune Investigate against faction with highest hidden stats"
│   → Niflhel is also doing intelligence work → their Intel results could be shared with Varfell (for a price)
│
├─ PLAYER FACILITATING PATH A:
│   Player at Standing 3+ in Varfell: can flag Varfell's Intel Domain Actions as Duty-aligned
│   Player investigation (TTRPG fieldwork) of rival faction: produces Evidence
│   Parliamentary Intent: flags evidence for faction use → +1D to Varfell's Intel roll
│   → Player's personal fieldwork DIRECTLY advances Varfell's Path A conditions
│   → The personal-scale investigation system (Evidence Track, fieldwork) feeds the BG victory condition
│   → This is the most explicit Domain Echo from personal investigation to faction victory condition:
│     player investigates Church archives → finds Church Mandate evidence → Varfell Intel roll with +1D
│     → Church stats partially revealed → Path A progress
│
├─ "AT LEAST 1 TERRITORY OUTSIDE STARTING 4" INTERACTION WITH PATH B:
│   Path A requires: ≥ 1 territory outside T4, T11, T12, T13 (Varfell's starting territories)
│   Path B requires: T4 AND T13 (both already in Varfell's starting territories)
│   → Path B doesn't require new territories (uses starting holdings)
│   → Path A requires territorial expansion (outside starting)
│   → Both paths require VTM ≥ 3 (same prerequisite)
│   → Path A is harder (expansion + Intel) but doesn't require Warden Recognition (WR)
│   → A Varfell player with poor Warden relationship should prefer Path A
│   → A Varfell player with good Warden relationship should prefer Path B
│   → The two paths create distinct play styles from the same faction
│
└─ CO-VICTORY INTERACTION:
    Varfell + RM co-victory: VTM ≥ 3 AND WR ≥ 2 AND ≥ 3 territories PT ≤ 1 AND RS ≥ 40 AND Varfell controls T13
    → Path A's "fully revealed stats" condition is NOT required for the co-victory
    → A Varfell player pursuing co-victory can ignore Intelligence Hegemony entirely
    → Path A is exclusively a solo victory path; it has no co-victory variant
    → This makes Path A the "independent" path: Varfell wins alone by knowing everything
    → All other Varfell paths (B, C, co-victories) involve other factions or world conditions
    → Path A is the game's only pure intelligence/isolation victory
```

**New emergence:** Path A's "stats fully revealed" creates an undefined victory condition that depends on interpretation of what "fully revealed" means. Player personal investigation feeding into faction Intel rolls via Parliamentary Intent creates the clearest mechanical bridge from TTRPG investigation to BG faction victory. Path A is uniquely a solo victory path with no co-victory equivalent.

---

## CATEGORY AR: FORMATION/TACTIC CARD INTERACTIONS

---

### NEW-S72: NIFLHEL ASSASSINATION CARD × COMMAND COLLAPSE × BILATERAL TIMING EDGE CASE

```
Root: Niflhg Tactic card "Assassination": "target opponent commander; −1D all opponent units"
      General Stage 1: Command halved, Morale floor suspended
      Bilateral general personal combat: both armies fight uncommanded
      Feigned Retreat + Discipline Ob 1: pursuing-side Discipline check

NIFLHEL PLAYS ASSASSINATION CARD SAME TURN AS PLAYER DECLARES BILATERAL PERSONAL COMBAT
│
├─ TIMING CONFLICT:
│   Phase 1: Player general declares personal combat (bilateral trigger pending)
│   Phase 1: Niflhel plays Assassination card (resolve at battle resolution)
│   Both effects target the same general (the opposing NPC general OR the player general)
│
├─ SCENARIO A: NIFLHEL PLAYS ASSASSINATION vs ENEMY GENERAL (targeting NPC general)
│   Assassination: NPC general hit → −1D all NPC units
│   Bilateral personal combat also fires: armies fight uncommanded (1D minimum per unit)
│   → Both effects apply to NPC units: −1D from Assassination AND 1D minimum from bilateral
│   → At 1D minimum (bilateral): −1D from Assassination has no additional effect (already at floor)
│   → The Assassination card is wasted if bilateral fires simultaneously
│   Niflhel's optimal play: wait for a non-bilateral turn to play Assassination
│   Shadow Intel (Varfell) allows seeing opponent's tactic card before revealing → knows if bilateral incoming
│   → If Niflhel has Shadow Intel information: can see player's personal combat declaration and adjust
│   → But Assassination is declared simultaneously with tactic cards (Phase 1 simultaneous, secret)
│   → No "see opponent tactic" information about personal combat declaration before Phase 1
│
├─ SCENARIO B: NIFLHEL PLAYS ASSASSINATION vs PLAYER (player is general)
│   Assassination: player hit → "target opponent commander" = −1D all player's units? Or commander killed?
│   "Target opponent commander; −1D all opponent units" — this is ONE effect
│   The card hits the commander AND reduces their army's dice
│   → If the card "kills" (how? Is it an attack or a stat effect?): unclear mechanical specification
│   → [GAP NEW-OI-44]: Assassination card — does it produce a Stage 1/Stage 2 death effect on the general
│     (using the same mechanic as personal combat incapacitation), or is it simply a dice penalty?
│     If Stage 1: all complex consequences (Command halved, Morale floor suspended, stabilisation window)
│     If dice penalty only: simpler; just −1D all units this engagement
│
├─ FEIGNED RETREAT × DISCIPLINE CHECK × WOVEN UNITS:
│   Feigned Retreat: pursuing Discipline check Ob 1 (87% pass for Discipline 4; 40% pass for Discipline 1)
│   If player has Woven the pursuing unit's Discipline (+1 or +2 from Thread Weaving):
│   → Woven Discipline: unit is now at Discipline 5 (above 4 cap? depends on whether Weaving breaks Discipline caps)
│   → At Woven Discipline 5: Discipline check Ob 1 → ~95% pass rate
│   → Feigned Retreat becomes near-useless against a Woven-Discipline unit
│   BUT: Woven unit brittleness (§A.14): if unit takes Size loss > Discipline in single turn
│   → Feigned Retreat lures the pursuing unit forward → Feigned Retreat re-engagement could deal high damage
│   → If the returning unit deals Size loss > Woven Discipline (5): brittleness triggers → Shifting Object forms
│   → The Feigned Retreat's high-damage re-engagement can break the Woven configuration it was trying to exploit
│
└─ NARROW PASS × CONCENTRATION × PLAYER POSITIONING:
    Narrow Pass terrain: 1 engagement per side (Fibonacci bonus impossible)
    Player Concentration tactic (Ob 1): "all sub-units on one target; max Fibonacci"
    In Narrow Pass: Fibonacci is impossible → Concentration tactic is UNAVAILABLE
    → Player preparing Concentration in Narrow Pass: must declare in Phase 1 (after terrain is known)
    Narrow Pass terrain is set BEFORE Phase 1 (environment known from Manoeuvre Phase 3)
    → Player should know Concentration is illegal before declaring; if declared anyway:
    → Treat as "Standard Advance" (default if tactic cannot execute)
    → This creates a Phase 1 declaration trap: player thinks Concentration is available, commits to tactic,
      discovers in Phase 5 it's negated by terrain
    → Solution: players must check terrain availability before tactic card selection
    → Optimal Narrow Pass play: Disciplined Defence or Standard Advance
    → Anti-Narrow Pass play: Feigned Retreat to reposition out of the Pass into open terrain
    → The Narrow Pass is the tactical defeat condition for the splitting-dominant meta:
      it forces equal-pool confrontation regardless of Command advantage
```

**New emergence:** The Assassination card's interaction with bilateral personal combat timing creates a simultaneous-declaration edge case where Niflhel's most powerful tactic is wasted. Woven unit Discipline creates a brittleness vulnerability precisely to the Feigned Retreat damage it was supposed to resist. The Narrow Pass is the correct tactical counter to the splitting-dominant meta — mechanically specified but requiring player awareness of terrain legality before Phase 1 declarations.

---

## CATEGORY AS: CO-VICTORY INCOMPATIBILITY × POLITICAL COALITION CONSTRAINTS

---

### NEW-S73: INCOMPATIBLE CO-VICTORIES × FACTION STRATEGY CONSTRAINTS × UNEXPECTED ALLIANCE MATH

```
Root: Incompatible co-victories: Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM
      Compatible: Crown + Hafenmark, Crown + Varfell, Varfell + RM, Hafenmark + RM, Löwenritter + Hafenmark, Church + Hafenmark
      Effective hegemony: rival Mandate ≤ 1 AND hegemon Mandate ≥ 5 → counts rival territory toward hegemon's control

STRATEGIC IMPLICATIONS OF COMPATIBILITY MAP FOR 5-PLAYER GAME
│
├─ INCOMPATIBILITY ANALYSIS:
│   Crown + Church: structurally opposed (sovereignty vs theocracy; Crown suppresses TC, Church advances it)
│   Crown + Löwenritter: the Coup Counter relationship — a co-victory with the faction threatening you
│   Church + Varfell: Church views Thread practice as heresy; Varfell pursues Thread mastery
│   Church + RM: theological antipodes (Solmundic Orthodoxy vs Einhir Restoration)
│
├─ THE EFFECTIVE HEGEMONY SHORTCUT:
│   Universal Victory requires "all 15 territories controlled directly or via effective hegemony"
│   Effective hegemony: rival Mandate ≤ 1 AND hegemon Mandate ≥ 5
│   → If Crown achieves Mandate ≥ 5 AND Church drops to Mandate ≤ 1 (Parliamentary campaign):
│     Crown can COUNT Church territory as "effectively hegemonized"
│   → Crown doesn't need to militarily conquer Himmelenger (TCV 5)
│   → They just need Church institutionally dominated
│   → This is the "institutional domination" path to Universal Victory — never specified as a "strategy" but
│     emerges directly from the effective hegemony rule
│   → Crown + Hafenmark pursuing this: Crown handles Church (Mandate suppression + Parliamentary Censure)
│     while Hafenmark handles Varfell (Dynastic Proclamation) and Guilds (trade Wealth investment)
│
├─ HAFENMARK'S COALITION VALUE:
│   Hafenmark is the ONLY faction compatible with ALL others (Church, Crown, RM, Löwenritter — not Church + RM simultaneously)
│   Compatible with: Crown (Crown + Hafenmark co-victory), Löwenritter (Löwenritter + Hafenmark), Church (Partition), RM (Hafenmark + RM)
│   → Hafenmark can co-victory with any faction depending on who wins the political contest
│   → In a 5-player game: every other player has reason to ally with Hafenmark
│   → Hafenmark becomes the "kingmaker" faction: who they co-victory with determines the winner
│   → This mirrors their BG position: they're the parliamentary faction that mediates everyone else
│
├─ CROWN + VARFELL COALITION ANALYSIS:
│   Crown + Varfell co-victory: Crown TCV ≥ 12 AND Varfell TCV ≥ 8 AND VTM ≥ 3 AND RS ≥ 50
│   → Crown and Varfell are both structurally threatened by Church (TC) and Altonia (IP)
│   → Both have Thread-adjacent interests (Crown via Almud TS development, Varfell via VTM)
│   → Combined condition: RS ≥ 50 requires active Mending → both factions share RS interest
│   → This co-victory creates the "Thread-realist" coalition against Church theocracy and Altonian invasion
│   → Their combination makes the two factions who most benefit from RS recovery co-victorious
│   → Mechanically elegant: the co-victory condition (RS ≥ 50) is exactly what both factions need to survive
│
├─ PLAYER COALITION ARCHITECT AT RENOWN 9+:
│   Renown 9+: all factions evaluate player at Priority 2
│   Player can construct the co-victory coalition through sustained relationship investment
│   Example: player builds Standing 4 in Crown AND has Disposition +3 with Vaynard
│   → Player declares Crown-Varfell co-victory intent (Parliamentary motion? Not specified)
│   → Player coordinates: Crown Mandate ≥ X, Varfell VTM ≥ 3, RS raised to 50
│   → As coalition architect, player's Domain Echo contributions count toward BOTH factions' conditions
│   → This is the Renown 9 "Grand Contest" equivalent at the macro level:
│     calling a co-victory coalition is the political version of a personal Grand Contest
│
└─ THE INCOMPATIBLE PAIRING EDGE CASE:
    5-player game with Crown, Church, Hafenmark, Varfell, RM all active
    Crown + Church (Incompatible) — no co-victory available
    But: Crown can pursue effective hegemony over Church territory WITHOUT co-victory
    → Crown Mandate 5+ AND Church Mandate 1- → Church territories count for Crown Universal Victory
    → This is effectively "co-victory without consent" — Crown uses Church's institutional collapse for territorial credit
    → The incompatibility prevents mutual benefit but doesn't prevent asymmetric exploitation
    → A dominant Crown with Mandate ≥ 5 doesn't NEED Church's cooperation — it just needs Church's weakness
    → This creates the game's most interesting political dynamic: crushing an incompatible partner is mechanically correct
```

**New emergence:** The effective hegemony rule creates an "institutional domination" path to Universal Victory that bypasses military conquest. Hafenmark's universal co-victory compatibility makes them the game's structural kingmaker. The Crown + Varfell co-victory's RS ≥ 50 condition elegantly aligns with both factions' intrinsic interests. The incompatible pairing edge case reveals that asymmetric exploitation (crushing Church to count their territory via hegemony) is mechanically valid even when co-victory is impossible.

---

## BATCH 5 OPEN ITEMS

| ID | Finding | Priority |
|----|---------|----------|
| NEW-OI-41 | Aftermath scene "Address the population" Order +1 timing: does this apply before or after Accounting's Accord derivation? If before, military conquest's Accord 1 penalty can be immediately partially offset. If after, it applies to the following season's Accord calculation. Affects NEW-S65 compound. | P1 |
| NEW-OI-42 | Varfell raising TS ≥ 30 military forces for Southernmost garrison (Deed 1): standard Muster produces units with no TS qualifier. Is there a special recruitment mechanic for Thread-capable units? Without one, Deed 1 garrison condition may be mechanically impossible for standard Varfell armies. | P2 |
| NEW-OI-43 | Varfell Path A "stats fully revealed" condition: does this mean all 5 stats (Mandate, Influence, Wealth, Military, Stability) for 2 rival factions, or a subset? Precise definition needed for victory condition clarity. | P1 |
| NEW-OI-44 | Niflhel Assassination tactic card: does "target opponent commander" produce a Stage 1 death effect (Command halved, Morale floor suspended, stabilisation window) or simply a −1D dice penalty? The card as written is ambiguous. | P2 |
| NEW-OI-45 | Bilateral general personal combat (§A.5 PP-506): armies fight at "1D minimum per unit" — does this override ALL modifiers (including size bonuses, formation bonuses) or just reduce the base pool to 1D if the pool would otherwise be below 1? Clarify whether 1D minimum is an absolute floor or just the PP-273 floor applied under uncommanded conditions. | P2 |
| NEW-OI-46 | Co-victory "calling" mechanism: how do players formally declare a co-victory pursuit? Is there a Parliamentary motion, a bilateral declaration, or is it automatic (conditions checked at Accounting)? In a 5-player game, factions may be pursuing incompatible co-victories simultaneously. Which co-victory fires if multiple are simultaneously met at the same Accounting? | P2 |
| NEW-OI-47 | Woven unit Discipline cap: can Thread Weaving increase a unit's Discipline above its starting maximum (e.g., above Discipline 4 for Cavalry)? The brittleness rule references "Size loss > Discipline" which changes if Discipline can be raised above its baseline. If Weaving can exceed the normal cap, the brittleness threshold is harder to reach. | P2 |
| NEW-OI-48 | Named unit officer Conviction assignment: "Inherited from faction (one of the faction's two Conviction values per npc_behavior_v30 §2)." Which two Conviction values does Crown use? Crown has Primary: Order and Secondary: Reason (from Almud §2.1). Does this mean Crown officers have either Order or Reason Conviction, chosen at Muster? Or always Order (the primary)? | P3 |
| NEW-OI-49 | Officer death roll clarification: "Roll 1d10. On result ≤ Size lost, officer killed." — does this roll once per engagement or once per turn? A unit losing 1 Size per turn over 5 turns: 5 separate 10% rolls vs a unit losing 5 Size in one turn: 1 roll at 50%. Same expected value but very different tension dynamics. | P2 |
| NEW-OI-50 | RS ≤ 20 → ALL territories CV −1 (Calamity Drift §1.3): this includes T1 Valorsplatz (CV 4), T9 Himmelenger (CV 5 soft cap), T14 Ehrenfeld (CV 4). At RS 20, Church's highest-CV territories begin losing CV. Does Church's TC Conviction Yield also begin declining at RS 20 from this CV erosion? If T9 drops from CV 5 to CV 4: Conviction Yield changes from +1 to +0.5. RS catastrophe suppresses the theocracy that was supposed to dominate at RS 40. | P2 |

---

*End of Batch 5 document.*
*10 new scenarios (NEW-S64 through NEW-S73), 10 additional open items (NEW-OI-41 through NEW-OI-50).*
*Combined totals across all five batches: 73 emergent scenarios, 5 feedback loops, 50 open items.*
*Key new coverage: Mass Combat World Bridge (officer-to-governor pipeline, aftermath scenes, player morale effect), General two-stage death and bilateral combat, Southernmost TS military restriction (RM Phase 2 defense dependency, Altonian vanguard exclusion), Thread in battle operational ceiling (co-movement incapacitation within 3 turns), all faction victory conditions (Löwenritter RS gate, Church+Hafenmark Partition Pressure marker, Varfell Path A "stats revealed" gap), effective hegemony path to Universal Victory, Hafenmark as universal co-victory kingmaker, incompatible pairing asymmetric exploitation, tactic card edge cases (Assassination timing, Narrow Pass Concentration illegality).*
