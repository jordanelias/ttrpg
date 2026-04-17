# VALORIA — EMERGENT ARC SKELETON TEST — BATCH 2
## Session: 2026-04-17 | Continuation of emergent_arc_skeleton_test_2026-04-17.md
## New surfaces: Obligations (§6.1), Chain Contests (§6.3), Parliamentary mechanics (§5), NPC Conviction Crisis (§3.3 ≥3 Scars), NPC Recruitment × Settlement, Thread-in-Contest (§9.3/§9.4), Occupation × Accord Reset, institutional consolidation positive loop, Knot-Mediated Remote Investigation, Mine/Port passive Wealth chain, Accord → TCV removal, new faction Parliament gap, style bonus fix interaction
## Does NOT repeat scenarios NEW-S1 through NEW-S22 or Loops A/B/C from Batch 1

---

## CATEGORY G: OBLIGATIONS × SETTLEMENT LAYER

---

### NEW-S23: SETTLEMENT-TARGETED OBLIGATION — NPC PRIORITY TREE BLOCK

```
Root: Grand Contest Obligation (§6.1 social_contest_v30): tracked as clock, 4 seasons or until condition
      Settlement-targeted Obligations (C-08): "Crown must maintain Defense ≥ 2 in S-006 Lowenskyst Fortress"
      NPC priority tree: any action violating the Obligation is BLOCKED while Stability ≥ 3

PLAYER WINS GRAND CONTEST AGAINST ALMUD (Parliament or Royal Audience setting)
│
├─ Contest subject: Crown's garrison policy at Lowenskyst Fortress
│   Player argues: Löwenritter autonomy at S-014 violates Crown authority at S-012
│   Grand Contest victory (Conviction Track ≥ 7)
│   Player names one specific Obligation (must be achievable and verifiable):
│   "Crown must maintain Defense ≥ 2 in S-006 Lowenskyst Fortress for 4 seasons"
│
├─ OBLIGATION REGISTERED (clock_registry_v30):
│   Duration: 4 seasons
│   Verification condition: S-006 settlement stat Defense ≥ 2
│   Violation trigger: Defense < 2 for any accounting period
│   NPC modification: Almud's priority tree blocks any Domain Action that would reduce Fortress Defense
│
├─ WHAT THE OBLIGATION BLOCKS:
│   │   Almud's AI priority tree: Institutional Filter → Conviction Filter → Decision Fork
│   │   Any action that would pull garrison from S-006 (for military use elsewhere):
│   │   → Blocked by Obligation (acts as +∞ Ob on that specific Domain Action for 4 seasons)
│   │   Almud cannot redeploy the Lowenskyst garrison even in an IP 75+ emergency
│   │   Without the garrison: effective Defense = settlement Defense only (4, still high)
│   │   But: Obligation also blocks voluntary transfer of the fortress to Löwenritter management
│
├─ THE STRATEGIC LEVERAGE:
│   IP 75+: Altonian pressure peaks. Almud wants to reinforce eastern passes.
│   Almud's priority tree: send Lowenskyst garrison to reinforce Spartfell
│   → BLOCKED by Obligation
│   Almud can break the Obligation (violation): Mandate −2, Stability −1, +2 Ob on next DA targeting player
│   → Almud faces: military necessity (IP crisis) vs institutional credibility (Obligation)
│   → This is a Trigger 2 scenario (forced into unfavorable position) applied at the personal scale
│
├─ VIOLATION CONSEQUENCE CASCADE:
│   Almud violates Obligation (military necessity forces it):
│   Mandate −2 (immediately drops from baseline 5 → 3)
│   Stability −1 (Obligation breach = Trigger 4 equivalent — Major Subterfuge)
│   Player's next Domain Action targeting Crown: +2 Ob (Crown credibility lost)
│   → Himlensendt observes: "The King's word means nothing. Parliament should act."
│   → TC +1 (Church leverages Crown credibility failure)
│   → Ehrenwall Coup Counter: if this was the second violation of sovereignty principles → +1
│
├─ SETTLEMENT-TARGETED OBLIGATION AS MILITARY CONSTRAINT:
│   A player who controls Obligation terms carefully can freeze enemy garrison policy
│   systematically across multiple Grand Contest wins over multiple seasons:
│   Season 1: "Crown must maintain Defense ≥ 2 in S-006"
│   Season 2: "Crown must not station Löwenritter at S-012 Ehrenfeld Citadel"
│   Season 3: "Crown must maintain Order ≥ 3 in S-010 Stillhelm" (Calamity boundary)
│   → Three settlement Obligations = Crown military policy frozen for 4 seasons each
│   → Crown cannot respond to IP pressure without violating Obligations serially
│   → Serial violations: Mandate drops catastrophically; Coup Counter advances
│
└─ NPC-ON-PLAYER OBLIGATIONS:
    Player loses a Grand Contest against Himlensendt → Obligation imposed on player:
    "Player must not conduct Thread operations in S-023 Himmelenger Cathedral for 4 seasons"
    → Dialogue Lattice Thread-Read at Himmelenger Cathedral: BLOCKED (violates Obligation)
    → If player violates: faction Mandate −2, Stability −1, Heresy Investigation active (+1 pool)
    → [NEW-S12]: The Himlensendt arc trigger delivery sequence requires Thread-Read at the Cathedral
    → Himlensendt imposing an Obligation blocks the player's optimal arc-trigger path
    → This makes the Himlensendt Contest sequence genuinely risky: losing = Obligation that blocks the win condition
```

**New emergence:** Settlement-targeted Obligations transform Grand Contest victories into sustained strategic constraints that reach into NPC decision trees. The mechanic creates a "legal" layer of political warfare that operates independently of military power — and has military consequences when violated.

---

### NEW-S24: OBLIGATION CLOCK × CHAIN CONTEST CASCADE

```
Root: Chain Contest (§6.3): Compromise (Track 4-6) → Priority 1 Scene Slate entry next season
      Obligation (§6.1): Grand Contest win → 4-season clock binding NPC action
      Both tracked via clock_registry_v30

PLAYER ACCUMULATES UNRESOLVED CHAIN CONTESTS OVER MULTIPLE SEASONS
│
├─ Season 1: Contest with Baralta re: Gransol Harbor trade access
│   Result: Compromise (Track 5) → deferred tension → Priority 1 Slate entry Season 2
│
├─ Season 2: Priority 1 Slate entry fires (Baralta-Gransol tension)
│   Player also has: Contest with Vaynard re: Southernmost access
│   Result: Compromise (Track 4) → deferred tension → Priority 1 Slate entry Season 3
│   Player addresses Season 1 deferred Baralta entry (1 scene action)
│
├─ Season 3: TWO Priority 1 deferred entries (Baralta resolved Season 2 + Vaynard now)
│   Player also has: Contest with Himlensendt (Priority 1 — TC > 40)
│   Mandatory: RS threshold scene (Priority 0)
│   Total Priority 0-1 entries: 4
│   Scene budget (Normal): 4 actions
│   → Budget FULLY consumed by Priority 0-1 entries
│   → No Duties addressed (Standing −1)
│   → No Convictions pursued (no Momentum)
│
├─ THE COMPOUND:
│   Active Obligation from Season 1's eventual Grand Contest win (Baralta finally resolved):
│   "Baralta must not expand Hafenmark naval presence at S-016 Gransol Harbor for 4 seasons"
│   Baralta's AI: Harbor expansion blocked by Obligation for 4 seasons
│   But: the Chain Contest residues filled the Scene Slate for 3 seasons while the player
│   was trying to generate the wins that would produce Obligations
│   → The process of winning Obligations through Chain Contest resolution is itself the crisis
│
├─ STRATEGIC IMPLICATION:
│   Players who attempt many social actions against many NPCs in the same season
│   generate Chain Contest residues that compound across seasons
│   → The optimal play is: one Grand Contest per season, resolved completely, to prevent Chain accumulation
│   → Social actions against multiple NPCs simultaneously creates multi-season Priority 1 debt
│   → This debt is paid by consuming scene actions that could have been personal pursuits
│
└─ OBLIGATION AS CHAIN TERMINATOR:
    Grand Contest win (Conviction Track ≥ 7): Obligation generated, tension fully resolved
    → Chain Contest (§6.3) does NOT generate from Grand Contest outcomes (tension fully resolved)
    → Only Formal Contest Compromise generates Chain entries
    → The player should escalate to Grand Contest (5 exchanges, high cost) specifically to
       terminate the Chain Contest loop and replace it with a deterministic Obligation
    → Resource question: is the additional cost of 5 exchanges vs 3 exchanges
       worth avoiding 2 seasons of Priority 1 Slate debt?
       At Hard difficulty (3 scene actions): YES — 2 Priority 1 entries costs 2 scene actions,
       leaving only 1 for personal pursuits. Grand Contest costs 1 scene action but prevents the debt.
```

**New emergence:** Chain Contests create a Priority 1 Scene Slate debt that compounds faster than it can be paid down if the player runs multiple concurrent social actions. The optimal strategy is deliberate escalation to Grand Contest resolution precisely to install Obligations (which are clean) and prevent Chain Contest accumulation (which is noisy).

---

## CATEGORY H: NPC CONVICTION CRISIS × PLAYER INTERACTION

---

### NEW-S25: 3+ SCAR ROLL 6 — PLAYER'S LAST INTERACTION BECOMES NPC DRIVER

```
Root: NPC Conviction Crisis (§3.3): 3+ Scars → d6 per major decision
      Roll 6: NPC acts on whichever Conviction most aligns with last PC interaction
      Player creates this state by deliberately straining NPC Conviction beyond recovery

HIMLENSENDT REACHES 3+ SCARS (player has been systematically targeting his Faith Conviction)
│
├─ Player has delivered Evidence Resonant Style attacks over 3 seasons:
│   Scar 1: "The Church-Niflhel connection — Olafsson's letters"
│   Scar 2: "The Cardinals who handled the originary Locks requested reassignment"
│   Scar 3: "Klapp's CE accumulation from objects your Church venerates"
│   → Himlensendt: Conviction Crisis state (3 Scars on Faith primary Conviction)
│
├─ HIMLENSENDT'S DECISION PROCEDURE NOW:
│   Per §3.3 Conviction Crisis table, each major decision (Domain Action, Parliamentary vote, Inquisitor deployment):
│   d6 roll:
│   1–2: Faith (institutional reflex) → Standard Zealot behavior
│   3–4: Order (secondary Conviction) → Stability maintenance; less aggressive
│   5: Autonomy → Church self-preservation (pull back from exposed positions)
│   6: Last PC interaction → NPC acts on player's most recent engagement
│
├─ THE ROLL 6 CONSEQUENCE:
│   Player's most recent interaction with Himlensendt:
│   If player argued "Thread reality is real and you must confront it":
│   → Roll 6: Himlensendt acts as if Thread-reality is true
│   → Domain Action: Himlensendt orders investigation into the originary Locks in Church archives
│   → This is an investigation Himlensendt himself would never order in a stable state
│   → The investigation surfaces evidence that damages Church institutional claims
│   → TC −1 (Church institution contradicted by its own investigation)
│   → Church Stability −1 (Himlensendt's public Scar: the Confessor is visibly unstable)
│
│   If player's most recent interaction was a Solidarity appeal (personal bond):
│   → Roll 6: Himlensendt acts to protect the player specifically
│   → Domain Action: Himlensendt halts Inquisitor operations that were targeting the player
│   → Inquisitor recall: Church Attention Pool loses 1 (player's Exposure reduced)
│   → The player's enemy is now their protector because his Conviction is broken
│
├─ THE PARADOX:
│   Player who over-strains Himlensendt's Conviction too far (3 Scars)
│   loses predictable enemy behavior (Zealot arc)
│   gains unpredictable ally behavior (6/6 chance his last impression governs each major action)
│   → This is better ONLY if the player controls the content of their last interaction
│   → Optimal Conviction Crisis exploitation:
│       Produce the 3rd Scar through Evidence → player holds the state
│       Then: maintain a reconciliatory-Thread last interaction ("I'm not your enemy; look at what your relics show")
│       Each Accounting: Himlensendt's major actions 1-in-6 align with Thread-reality acknowledgment
│   → 5-in-6 of the time: still acting as Faith/Order/Autonomy
│       1-in-6 of the time: acting as the player's position
│
├─ THE RISK:
│   Player argues AGAINST Himlensendt's interests in the most recent interaction:
│   Roll 6: Himlensendt acts against the player's interests more strongly than his stable self would
│   A Conviction Crisis NPC is more dangerous when last-interaction was hostile
│   The player MUST manage the content of their most recent contact
│   → Scene Slate: player should always schedule a "last contact" scene before Accounting
│       to set the Roll 6 anchor
│   → This creates a sustained relationship maintenance obligation for a fully-destabilized NPC
│
└─ SECOND-ORDER EMERGENCE:
    If both Himlensendt (Faith Conviction 3+ Scars) AND Klapp (CE 4, TS 30, Trajectory B/C)
    are simultaneously in crisis states:
    Church major decisions = d6 + d6 per decision
    Two unpredictable primary church actors → Church Domain Actions become probabilistic
    → TC generation rate: uncertain (could accelerate or brake depending on crisis outcomes)
    → The Church's threat becomes non-linear: it might suppress itself before player intervention
    → Or it might take catastrophic offensive action on a bad roll week
    → [Collision A: Church Double Fracture] is now a probabilistic state machine, not a fixed arc
```

**New emergence:** The 3+ Scar Roll 6 rule creates a "last impression wins" mechanic for fully-destabilized NPCs. Players who understand this can weaponize Conviction crises by managing the content of their most recent interaction to steer NPC behavior on the 1-in-6 roll. This is an entirely new form of relationship manipulation that requires ongoing scene investment.

---

## CATEGORY I: PARLIAMENTARY MECHANICS × NEW SYSTEMS

---

### NEW-S26: PARLIAMENTARY INTENT × EVIDENCE CHAIN × DIPLOMATIC CAPITAL

```
Root: Parliamentary Intent (integration bridge Gap 3): Standing 3+ player flags Evidence for Parliamentary use
      Evidence-as-Corroboration in Parliament: +1D to faction's Ratification roll
      Parliamentary Conviction Track: +1D lobbying offset per successful Diplomacy action preceding vote

PLAYER RUNS PARALLEL INVESTIGATION AND PARLIAMENTARY PREPARATION
│
├─ TRACK A: Investigation (seasons 1-3):
│   Scene actions devoted to Structural investigation (threshold 8) of Niflhel-Church connection
│   Reaches Structural threshold → Casus Belli eligible AND Parliamentary evidence
│
├─ TRACK B: Parliamentary Preparation:
│   Player has Standing 3 (Counselor) in Crown
│   Parliamentary Intent declared as scene action: flags Structural evidence for Parliamentary use
│   Season 3: Baralta issues Parliamentary Motion → Censure against Church (for Olafsson connection)
│   Player's Structural evidence: +1D to Crown's Ratification roll when voting on this Censure motion
│
├─ PARLIAMENTARY VOTE MECHANICS (§5.3 + Starting Track modification):
│   Baralta (Censure proposer): pays no proposer cost for Censure
│   Starting Conviction Track: 5 ± lobbying offset
│   Player's prior Diplomacy scene (preceding season) → +1 toward Baralta's side
│   Player's Structural evidence via Parliamentary Intent → +1D additional for Crown's vote
│   Guild AI vote: Censure is not Blockade or Outlawry → Guilds vote for whoever weakens highest Mandate faction
│   Highest Mandate is Church (5): Guilds vote FOR Censure (it weakens Church)
│
├─ VOTE COMPOSITION:
│   Crown Mandate 4 + player's evidence bonus +1D = 4D+1D (equivalent 5 Mandate votes effective)
│   Hafenmark Mandate 4 + Baralta's lobbying +1D = 4D+1D
│   Varfell Mandate 3: neutral → votes based on TCV advantage calculation
│   Guilds: AI rule → vote FOR Censure (Church is highest Mandate)
│   Against: Church Mandate 5 → cannot vote on own Censure (targeted faction excluded)
│   Löwenritter Mandate 2 → 2 votes (likely Abstain per institutional interests)
│
│   Majority threshold: > 50% of participating Mandate
│   Participating Mandate: Crown 4 + Hafenmark 4 + Varfell 3 + Guilds ~2 + Löwenritter 2 = 15
│   Majority: > 7.5 → 8 votes needed
│   FOR (Censure): Crown 4 + Hafenmark 4 + Guilds 2 = 10 (+ lobbying/evidence bonuses)
│   → Censure passes comfortably
│
├─ CHURCH SACRED VETO DECISION:
│   Church can cancel the Censure vote (Sacred Veto, §5.3): costs Mandate −1 if against a passing motion
│   Himlensendt's options:
│   ├─ USE VETO: Mandate −1 (5→4); motion blocked; but self-interested veto → additional Mandate −1 (4→3)
│   │   → Himlensendt uses Veto: Mandate 3 (two decrements in one move)
│   │   → Church is now below Crown and Hafenmark in Mandate
│   │   → TC generation: Passive +1/season (Church Mandate ≥ 3); still fires
│   │   → But: Church parliamentary power collapsed
│   │
│   └─ DO NOT VETO: Censure passes → Church Stability −1; Church Mandate −1 (Censure effect)
│       → Same outcome mechanically, but Church Mandate stays at 4 (not 3)
│       → More Mandate = more Sacred Veto uses in future seasons
│       → Not using Veto is actually better for Church long-term Mandate preservation
│       → But Himlensendt's primary Conviction (Faith, Zealot arc) would resist appearing weak
│       → Decision Fork: Faith (use Veto to defend Church dignity) vs Reason (preserve Mandate for future)
│       → At Scar 0: Faith wins → Himlensendt uses Veto
│       → At Scar 1: Decision Fork activates → player's prior Resonant Style attack context matters
│
├─ DOMAIN ECHO FROM PLAYER'S INVESTIGATION:
│   Parliamentary Intent + Structural evidence → faction Intelligence +1 (per Domain Echo table)
│   Censure passes (with player's evidence contribution) → Church Mandate −1, Stability −1
│   → Player's investigation caused a Parliamentary vote outcome
│   Domain Echo fires: ±1 Influence for player's faction (Partial) → Crown Influence +1 if success
│   → Three compounding effects from one Structural investigation: Casus Belli, Parliament result, Domain Echo
│
└─ PLAYER PARLIAMENTARY STANDING:
    Standing 3 was required to declare Parliamentary Intent
    If Censure passes: this is a "Duty exceeded" outcome (Standing +2 instead of +1)
    Player's Standing: 3→5 in one compounding season (if they also met the Duty conditions)
    → Succession eligibility trigger: Standing 5 → player is now Crown succession candidate
    → This is the fastest possible path from Counselor to Successor through a single Parliamentary chain
```

**New emergence:** Parliamentary Intent transforms long-form investigation into political capital that amplifies a Parliamentary vote. The compound consequence (Evidence → Parliament → Domain Echo → Standing advancement) creates a "Scholar-Diplomat" arc where patient investigation delivers compounding political returns.

---

### NEW-S27: CHURCH SACRED VETO × TC MANDATION COLLAPSE × TC ACCELERATION PARADOX

```
Root: Church Sacred Veto (§5.3): cancels any non-military Parliamentary vote; Mandate −1 if against passing motion; additional −1 if self-interested
      TC generation (existing): Passive +1/season if Church Mandate ≥ 3
      Church Mandate at 3: still generating TC (barely)

HIMLENSENDT USES SACRED VETO THREE TIMES IN FIVE SEASONS
│
├─ Season 1: Censure motion against Church (Niflhel exposure)
│   Himlensendt Veto: Mandate 5 → 5 − 1 (against passing motion) − 1 (self-interested) = 3
│   TC: still generating (+1/season)
│
├─ Season 3: Outlawry motion against Church (Church military overreach)
│   Outlawry requires Supermajority; Himlensendt uses Veto
│   Mandate 3 → 3 − 1 − 1 = 1
│   TC generation: STOPS (Mandate < 3; passive TC generation pauses)
│   TC is currently at, say, 45
│   TC stalled: no passive generation
│
├─ THE PARADOX:
│   Church used Sacred Veto to PROTECT ITSELF from political damage
│   Result: Church Mandate collapsed to 1
│   TC generation paused (the very mechanism that gives Church power is offline)
│   Church at Mandate 1: cannot propose Parliamentary motions (needs Mandate 2)
│   Cannot use Sacred Veto again (needs Mandate 1 to maintain the next Veto; but Veto costs Mandate −1)
│   → Another Veto = Mandate 0 → Church has no Parliamentary presence at all
│
├─ MANDATE 1 CHURCH: STRATEGIC VULNERABILITIES
│   Parliamentary actions against Church: no Sacred Veto to block
│   Church cannot issue Censure against player (needs Mandate 2)
│   Church Domain Actions: Suppress (TC action) now harder — Stability checks harder at low Mandate
│   Military: Church has no Military stat (non-military faction)
│   → Church at Mandate 1 is institutionally paralyzed
│
├─ TC STALLED WITH CHURCH PARALYZED:
│   TC at 45 (stalled at Mandate 1 block)
│   Players can act on Thread reality, RM support, etc. without TC advancing
│   This is the largest possible "breathing room" state in the game:
│   No TC advancing + Church institutionally frozen
│   RS can be stabilized (Mending operations, no TC pressure)
│
├─ CHURCH RECOVERY PATH:
│   Church Absolution (unique action): +1 Stability to target; Church Influence +1
│   But this doesn't restore Mandate directly
│   Löwenritter endorsement: +1 Stability + Löwenritter Mandate +1 → does not help Church Mandate
│   Mutual peace treaty: +1 Stability (not Mandate)
│   → No direct Mandate recovery mechanism visible in current spec
│   → GAP IDENTIFIED: How does Church recover Mandate once collapsed to 1?
│
│   Likely path: Himlensendt's Challenge resolution (arc branch condition)
│   Arc B (Crisis of Faith): Mandate may stabilize under new doctrinal framing
│   Arc A (Zealot): Mandate recovery through aggressive TC suppression action success
│   But both require standing above Mandate 1 to execute...
│   → Church at Mandate 1 may be LOCKED OUT of its own recovery mechanisms
│
└─ STRATEGIC TIMING (player-facing):
    The player who wins three Parliamentary Censure motions against Church over 5 seasons
    forces Himlensendt to choose: let each Censure pass (Mandate −1 each) or Veto (Mandate −2 each)
    Both paths lead to Mandate 1 within 3 Censures
    → Sustained Parliamentary pressure (not combat, not Thread) collapses Church institutional power
    → This is the non-violent Church destruction path
    → TC is collateral beneficiary: it stalls when Church Mandate falls below 3
    → [ARC 4: Niflhel-Church exposure] is the Censure material; systematic Parliament is the delivery mechanism
```

**New emergence:** The Sacred Veto is a self-defeating defense mechanism. Systematic Parliamentary pressure forces Himlensendt to exhaust his Veto uses in Mandate-collapse, paradoxically stalling TC generation (the very power the Church was trying to protect). This is an entirely political path to TC management that wasn't visible before the Parliamentary mechanics were specified.

---

## CATEGORY J: OCCUPATION × ACCORD × SETTLEMENT STATE

---

### NEW-S28: OCCUPATION ACCORD FREEZE × SETTLEMENT ORDER MEMORY

```
Root: Occupation effects (§2.3 faction_layer): Accord frozen at pre-Occupation value during military contest
      Control transfer via 3-season occupation: Accord set to 1 (Resistant)
      Military recapture Overwhelming: Accord restored to PRE-OCCUPATION value
      Settlement Order → Province Accord (settlement_layer §1.3)

PROVINCE T8 GRANSOL IS OCCUPIED BY CROWN (3 settlements: Gransol Parliament, Gransol Harbor, Gransol Market)
│
├─ PRE-OCCUPATION STATE:
│   S-015 Gransol Parliament: Order 4
│   S-016 Gransol Harbor: Order 3
│   S-017 Gransol Market Quarter (Guild-managed): Order 3
│   Province Accord (derived): floor((4+3+3)/3) = floor(3.33) = 3 (Aligned)
│   Accord 3 = full Effective Prosperity for Hafenmark; Defender +1D in battle
│
├─ CROWN OCCUPIES (Occupation established):
│   Accord frozen at 3 during contest period
│   Settlement Orders: FROZEN (occupation suspends governance — population loyalty suspended)
│   The order values at time of occupation lock the province's social state
│
├─ OCCUPATION DURATION EFFECTS:
│   Season 1: Accord = 3 (frozen)
│   Season 2: Accord = 3 (frozen; Hafenmark Stability −1/season ongoing)
│   Season 3 end: 3-season threshold → automatic control transfer
│   New Accord set to 1 (Resistant) regardless of pre-Occupation Accord 3
│   → Hafenmark loses 2 Accord points at transfer (3 → 1)
│   → Settlement Orders: now under Crown NPC governor management
│   → Crown NPC governors: prioritize Order ≥ 2 → settlements slowly recover from freeze
│
├─ HAFENMARK RESISTANCE STRATEGY:
│   Resistance Check (free Accounting action): displaced faction rolls to hold or reduce occupier
│   City-state Baralta (if already collapsed): can still use Resistance Check
│   Combined Embargo+Blockade via Parliament: reduces Crown Military (garrison cost −1/territory occupied)
│   → Parliament is Hafenmark's anti-occupation tool even without military
│
├─ MILITARY RECAPTURE (Overwhelming — Baralta allies with player-led force):
│   Accord restored to PRE-OCCUPATION value (Accord 3)
│   BUT: settlement Orders were frozen during occupation
│   Post-recapture: governors need to be reassigned (occupation removed NPC governors)
│   Settlement Order values: still frozen at pre-occupation levels (4, 3, 3)
│   → Province Accord immediately derives from those frozen Order values = 3
│   → Liberating Gransol (Overwhelming recapture) returns the province to Aligned status instantly
│
├─ THE MEMORY MECHANIC:
│   What the order values were AT THE MOMENT OF OCCUPATION matters for the recovery value
│   A player who IMPROVES settlement Orders before an anticipated occupation
│   (from Order 3 → Order 4 in all settlements = Province Accord 4, but capped at 3)
│   creates a frozen high-water mark that can be restored on Overwhelming recapture
│   → Pre-occupation governance investment = post-liberation political capital
│   → Governing Gransol well BEFORE the invasion pays dividends after liberation
│
├─ SUCCESS (not Overwhelming) RECAPTURE:
│   Accord = max(pre-Occupation − 1, 1) = max(3 − 1, 1) = 2
│   Settlement Orders: still frozen; governor reassignment needed
│   Province Accord 2 (Compliant) — functional but not optimal
│   Full restoration requires 1 additional season of governance to return Order values to pre-occupation levels
│
└─ GUILD-MANAGED S-017 INTERACTION:
    Gransol Market Quarter is Guild-managed (subnational faction management rights)
    During Crown occupation: does Guild management persist?
    Province faction (now Crown) retains taxation and military authority
    But Guild management of Market settlements: historically a traditional right
    Crown may grant or revoke Guild management (Domain Action, §3.3 settlement_layer)
    → Crown revoking Guild management of Gransol Market: Order −1 in S-017 (population disruption)
    → Guild Disposition toward Crown: −2
    → Guild Parliamentary vote shifts: from neutral to AGAINST Crown in all votes
    → [NEW-S26 Parliamentary chain]: Guild votes now hostile to Crown in any Parliament motion
```

**New emergence:** Occupation creates a temporal snapshot of settlement Order values. Pre-occupation governance investment directly determines post-liberation political recovery speed. Players who anticipate occupation (predictable from IP track or clock thresholds) can "pre-load" high Order values to maximize Accord recovery on liberation.

---

## CATEGORY K: ECONOMIC CHAIN × SETTLEMENT TYPE

---

### NEW-S29: MINE PROSPERITY → PROVINCE WEALTH → FACTION ECONOMY ENGINE

```
Root: Mine settlement type + Prosperity 3+: Resource surplus → Province Wealth +1 at Accounting (passive)
      Port settlement + Guilds management: +1 Trade per season (feeds Prosperity chain)
      Faction Wealth: governs military mustering, treaty negotiation bonuses, Subsidy capacity

PLAYER GOVERNS MINE SETTLEMENT (S-021 Halvarshelm Mines, T17, Hafenmark, starting P=3/D=0/O=2)
│
├─ Starting state: Prosperity 3 (already at Mine surplus threshold)
│   Province Wealth contribution: +1 at Accounting (passive, no player action required)
│   Player's governance action available: Develop (Cognition + Wealth-relevant History, Ob floor(3÷2)+1 = Ob 2)
│
├─ DEVELOP ACTION CHAIN:
│   Player Develop success: Prosperity +1 → Prosperity 4
│   At Prosperity 4: Resource surplus still fires → Province Wealth +1 (larger contribution)
│   But: Mine type max Prosperity = ? (not specified in settlement_layer; SETT-02 flags this)
│   Assumption: Mine type max Prosperity = 4 (resource exhaustion ceiling)
│   → Prosperity 4 is sustainable; another Develop fails (already at ceiling)
│
├─ PROVINCE WEALTH ACCUMULATION:
│   Province T17 Halvarshelm: 2 settlements (S-021 Mine + S-022 Town)
│   S-021 Prosperity 4: +1 Province Wealth/season
│   S-022 Town at Prosperity 3 (not mine): no surplus trigger (Town type lacks Mine surplus rule)
│   → Province T17 generates +1 Faction Wealth/season from S-021 alone
│   Annual accumulation: +4 Wealth/year (4 seasons)
│   Seasonal cap on faction stats: ±2/season → Wealth +1/season is within cap
│
├─ STACKED MINE + PORT ECONOMY:
│   If player also governs S-016 Gransol Harbor (Port, Guilds-managed):
│   Guild management: +1 Trade per season (feeds Wealth independently)
│   Combined: Mine surplus +1 Wealth/season + Guild Trade +1 Wealth/season
│   = +2 Wealth/season → AT THE SEASONAL CAP
│   → Two well-governed settlements of the right types generate maximum passive Wealth growth
│
├─ FACTION WEALTH → MILITARY POWER CHAIN:
│   Wealth → Military mustering (Muster action requires Wealth ≥ 1)
│   Wealth 0 → Military −1 each Accounting (mercenaries unpaid, §5.7 faction_layer)
│   Conversely: sustained Wealth growth through Mine + Port governance
│   → Faction never faces Military decline from Wealth zero
│   → Faction can sustain Blockade/Embargo from opponents without Military collapse
│
├─ THE GOVERNANCE ECONOMIC ENGINE:
│   Player governing 2 specific settlement types (Mine + Port) generates:
│   +2 Wealth/season passive → +8 Wealth/year
│   A faction starting at Wealth 4 reaches cap (likely 7 per faction stats) in 0.375 years (1.5 seasons)
│   → Faction Wealth is permanently capped after 1.5 seasons of dual Mine + Port governance
│   → Military is never threatened by economic siege
│   → Parliamentary Subsidy capacity: faction can now offer Subsidy to allies (§5.4 Parliament)
│
├─ DOMAIN ECHO SPECIFICITY:
│   This is a settlement-governor Domain Echo that doesn't require player scene action
│   It fires automatically at Accounting from settlement type + Prosperity threshold
│   Compare to: Domain Echo table "Governance — sustained (3+ consecutive seasons): +1 Accord permanent cap raise"
│   → Sustained Mine governance = permanent Accord floor raise + passive Wealth
│   → Both positive Domain Echo paths operating simultaneously from the same governance role
│
└─ PLAYER FACTION BUILDING:
    A player in Stage 2-3 (Organization to Movement, settlement_layer §6.2)
    controlling a Mine (Prosperity 3+) and Port (Guild-managed) generates faction-level Wealth
    even before having a full faction stat sheet
    → The Mine/Port combination is the bootstrap economic engine for faction emergence
    → A player who deliberately seeks out and governs these settlement types
       reaches Stage 4 (full faction) with a pre-built economic base
    → [NEW-S30 below]: compare to "Administrative Blitz" — this is the "Economic Blitz" variant
```

**New emergence:** Specific settlement type combinations generate passive faction-level Domain Echoes without player scene investment beyond initial governance establishment. The Mine + Port combination is the highest-efficiency passive economic engine, producing capped Wealth growth that protects military capacity from Parliamentary economic siege.

---

## CATEGORY L: THREAD IN CONTEST × HERESY EVIDENCE

---

### NEW-S30: PRACTITIONER CONTEST THREAD BONUS × HERESY INVESTIGATION FIRING

```
Root: §9.3 social_contest_v30: Practitioner TS ≥ 30 in active Thread contact adds floor(TS÷30)D in contests
      Visible to ALL observers → Church may file Heresy Investigation on observation
      After each exchange: Coherence check Ob 1
      Public Contest setting: Crowd adjudicator (Parliament or public forum)

PRACTITIONER PLAYER (TS 60) PARTICIPATES IN GRAND CONTEST AT PARLIAMENTARY SESSION
│
├─ Setup: Grand Contest, 5 exchanges, Crowd adjudicator (Parliament present)
│   Player activates Thread contact before Exchange 1 (Leap declared, Priority 5)
│   Contact established; Focus window: 5 rounds (one per exchange)
│
├─ BONUS DICE FROM THREAD CONTACT:
│   TS 60: floor(60÷30) = 2 additional dice in each exchange
│   Standard Argue pool: (Cognition × 2) + History (e.g., 8+History)
│   With Thread: 8+History+2 = 10+History per exchange
│   → Substantial advantage; at Ob 3 (Grand Contest typical): much higher success rate
│
├─ HERESY INVESTIGATION FIRING:
│   Thread contact is VISIBLE TO ALL OBSERVERS (§9.3: visible)
│   Participating factions in Parliament can observe the Thread contact
│   Church observer: mandatory — any Thread use in public = Church Attention Pool +1
│   If Church Attention Pool reaches threshold: Heresy Investigation opens
│   With 5 exchanges: Church observes Thread contact 5 times
│   Church Attention Pool: +5 (one per observed exchange)
│   → Heresy Investigation: CERTAIN to open (any threshold is passed in a single Grand Contest)
│
├─ COHERENCE COST PER EXCHANGE:
│   After each exchange: Coherence check Ob 1 (Spirit + History + TPS, TN 7)
│   5 exchanges = 5 Coherence checks
│   At 37% failure rate per check: expected 1.85 failures → expected Coherence −1.85
│   Realistic outcome: Coherence −2 across the 5-exchange contest
│   If practitioner starts at Coherence 10: exits at Coherence 8 (Stable, fine)
│   If practitioner starts at Coherence 6 (prior degradation): exits at Coherence 4 (Fragmented — severe)
│
├─ THE NET CALCULATION:
│   Exchange 1-5 WITH Thread: +2D per exchange → very high win probability
│   Exchange 1-5 WITHOUT Thread: standard pool → ~50-60% win rate at Ob 3
│   Thread advantage: shifts each exchange from ~55% to ~75%+ success
│   → In a 5-exchange Grand Contest: Thread gives ~1-2 additional exchange wins
│   → At Conviction Track 5 (start), each exchange win moves Track toward win
│   → Thread makes an even contest into a decisive win
│   COST: Heresy Investigation opened, Coherence −2, visible political identity (confirmed practitioner)
│
├─ POLITICAL CONTEXT MATTERS:
│   Parliament setting: Crown present, Hafenmark present, Varfell present, Church present
│   All observe Thread contact
│   Crown response (if player is Crown-aligned): Crown Stability −1 (Trigger 4: Subterfuge against faction — no, this is overt. Actually: Crown Mandate −1 if they're seen to employ a heretic)
│   Varfell response: TK +1 (witnessing Thread used instrumentally; Vaynard notes this)
│   Hafenmark response: Baralta files Thread contact as evidence (she's gathering Thread evidence, ARC 3)
│   → Using Thread in Parliament doesn't just help the contest — it reshapes all faction relationships simultaneously
│
├─ OPTIMAL USE CASE:
│   Thread bonus in Contests is worth the Heresy cost ONLY if:
│   1. The Contest outcome is critical enough to justify Heresy Investigation opening
│   2. The player can survive or exploit the resulting Heresy Investigation
│   3. Player's Coherence is healthy (Coherence ≥ 8 to safely absorb 5-exchange drain)
│   → This is a "nuclear option" for crucial Grand Contests: use Thread, win decisively, accept the political cost
│
└─ HERESY INVESTIGATION AS INTENDED CONSEQUENCE:
    Some player arc configurations benefit from confirmed Heresy Investigation status:
    Independent path (no faction): Heresy Investigation exposes the player → they become a known practitioner
    → Renown +1 (investigation resolved at Complex threshold — "investigation of player resolved")
    → NPC Outreach: NPCs seeking practitioner contact now approach the player openly (known quantity)
    → Church antagonism is maximized: TC +1 from public practitioner confirmed
    → But: RS benefits if player uses the resulting attention to publicly advocate for Mending
    The practitioner who uses Thread in Parliament is CHOOSING public identity
    → This is a strategic decision, not an accident
```

**New emergence:** Thread use in Contests (§9.3) creates a triple cost (Heresy Investigation, Coherence drain, political visibility) against a single benefit (extra dice). The cost structure makes this a high-stakes "nuclear option" for decisive Grand Contests. Players who understand the political reshaping effect can use the Heresy Investigation opening as a deliberate identity declaration.

---

## CATEGORY M: KNOT-MEDIATED REMOTE INVESTIGATION × COMPANION

---

### NEW-S31: COMPANION GOVERNOR × KNOT-MEDIATED REMOTE INVESTIGATION

```
Root: fieldwork_v30 §2.6 Knot-Mediated Remote Investigation: practitioner with active Knot can investigate
      where the Knot partner is, without being physically present
      Companion formation: requires Knot (Connect success → Disposition at max → Knot formation)
      Companion governor: stationed at specific settlement

PLAYER (PRACTITIONER) KNOTS COMPANION WHO GOVERNS S-015 GRANSOL PARLIAMENT
│
├─ Knot formation prerequisites:
│   Player has Disposition max with companion (floor(Bonds÷2)+1, per PP-632)
│   Connect success at maximum Disposition → Knot formed
│   Companion stationed at S-015 Gransol Parliament as governor
│
├─ REMOTE INVESTIGATION FROM SIGURDSHELM (S-026):
│   Player is in Varfell territory; companion is in Hafenmark territory
│   Thread-Read as Perceptive Leap (fieldwork §4.5): Knot-mediated
│   Knot partner's location IS accessible remotely
│   → Player can investigate S-015 Gransol Parliament WITHOUT traveling there
│   → Saves: inter-province travel cost (1 scene action per province traversed)
│   → Gransol (T8) from Sigurdshelm (T12): requires traversing T11, T14, T8 = ~3 provinces
│   → Travel cost: 3 scene actions saved by remote investigation
│
├─ WHAT CAN BE INVESTIGATED REMOTELY:
│   Knot-mediated: the partner's perception channel (not a Thread-Read of the location per se)
│   → Player perceives through the companion's Thread presence at the location
│   → Depth access: limited by companion's TS (if companion has TS ≥ 10, Depth 3 accessible)
│   → Evidence quality: Thread-filtered perception (same evidence, different access route)
│   → The companion's Conviction shapes what the remote investigation surfaces
│      (their awareness, their attention, what they find significant)
│
├─ STRATEGIC APPLICATION:
│   Player at Standing 3 (Counselor): needs intelligence from multiple locations simultaneously
│   Companion at Gransol: remote investigation possible (saves 3 scene actions)
│   Player's own location: active investigation scene (uses 1 scene action)
│   → Effective parallel investigation: 2 territories investigated per scene-action budget period
│   → Compare to sequential investigation: 4 scene actions to travel to Gransol + investigate
│   → Remote investigation compresses what would take 2 full seasons into 1 season
│
├─ COMPANION GOVERNOR + REMOTE INVESTIGATION:
│   Companion's free governance action (social OR governance):
│   If companion takes governance: Order maintained, free social action lost
│   If companion takes social (Administer): reveals one local NPC's active Conviction
│   → Administer output: NPC Conviction revealed → feeds player's remote investigation
│   Player Thread-Reads through the companion → gets access to what the companion's Administer revealed
│   → Companion's Administer action + player's remote Thread-Read = compound intelligence gathering
│   → The companion's free governance action produces Evidence that the remote investigation then harvests
│
├─ KNOT STRAIN INTERACTION:
│   Thread-mediated remote investigation through a Knot: "Knot strain + 1 per full Leap"
│   (per threadwork_v30 §2.6 or equivalent; depends on operational scale)
│   If player uses remote investigation heavily (multiple seasons): Knot strain accumulates
│   → Heavy remote use degrades the relationship resource it depends on
│   → Same trap as companion-governor: extractive use (governance only, no Connect) → Knot strain
│   → Remote investigation is another form of relationship extraction
│   Optimal balance: 1 remote investigation / 2-3 seasons + 1 Connect per season to manage strain
│
└─ THE INTELLIGENCE NETWORK ARCHITECTURE:
    Player with 2 companions (max) stationed at 2 settlements = 2 remote investigation nodes
    Each companion at a different province capital (Gransol Parliament + Valorsplatz Palace)
    → Player can Thread-Read from anywhere into both political centers
    → Intelligence gathering radius: the entire peninsula if companion placement is strategic
    → This is the mechanically grounded version of the "spy network" concept:
       not abstract intelligence points, but specific Knot-mediated Thread channels
       with Coherence costs, Knot strain accumulation, and companion TS gating
    → [NEW-S8: "Building to be fired"] at high Renown + remote investigation network:
       player is an independent operator who observes everything from personal safety
```

**New emergence:** Companion Governor + Knot formation + Remote Investigation creates a geography-collapsing intelligence architecture. The player need not be present in a territory to investigate it — but the cost is Knot strain from overuse, binding the intelligence efficiency to the health of the companion relationship.

---

## CATEGORY N: GUILD BLOCKADE × WEALTH → MILITARY → SETTLEMENT DEFENSE

---

### NEW-S32: SUSTAINED PARLIAMENTARY SIEGE — WEALTH ZERO → MILITARY COLLAPSE → SETTLEMENT VULNERABILITY

```
Root: Combined Embargo+Blockade: Wealth −2/season + Stability −1/season (both sides pay Wealth −1/season)
      Wealth 0 (§5.7): Military −1 per Accounting
      Garrison Discipline = military unit stat; Effective Defense = settlement Defense + garrison Discipline
      Löwenritter (Military 4, Stability 3): natural Blockade proposer with political motivation

HAFENMARK RUNS COMBINED EMBARGO+BLOCKADE AGAINST CROWN OVER 6 SEASONS
│
├─ PROPOSER REQUIREMENTS:
│   Combined Embargo+Blockade: both Mandate 3 (Embargo) AND Military 3 + Mandate 3 (Blockade)
│   Hafenmark has Parliamentary Manoeuvre (existing action); Mandate 4, Military 2 (limited)
│   But: Hafenmark doesn't need Military for Embargo (only Blockade)
│   Baralta can propose Embargo (Mandate 4) → Guilds and Varfell join → majority passes
│   Löwenritter proposes Blockade separately (Military 4, Mandate 2)
│   Combined: passes if majority for each component
│
├─ CROWN UNDER COMBINED EMBARGO+BLOCKADE:
│   Ongoing costs: Wealth −2/season + Stability −1/season
│   Crown starting: Wealth 5 (assumed), Stability 6
│   Season 1: Wealth 4, Stability 5
│   Season 2: Wealth 3, Stability 4
│   Season 3: Wealth 2, Stability 3
│   Season 4: Wealth 1, Stability 2 → Stability ≤ 2: Faction AI enters Survival priority (Stability ≤ 2)
│   Season 5: Wealth 0 → Military −1 at Accounting; Stability 1
│   Season 6: Military −1 again; Stability 0 → Faction Fracture risk
│
├─ MILITARY COLLAPSE TIMELINE:
│   Crown Military baseline: ~5 (assumed)
│   Season 5: Military 4 (−1 from Wealth 0 penalty)
│   Season 6: Military 3 (−1 again)
│   Season 7: Military 2 → GARRISON COLLAPSE
│
├─ GARRISON DISCIPLINE → SETTLEMENT DEFENSE CHAIN:
│   Crown garrisons at: S-006 Lowenskyst (Discipline 3→2→1), S-012 Ehrenfeld (Discipline 3→2→1)
│   Effective Defense at S-006: Defense 4 + Discipline 3 = 7 (initially)
│   By Season 7: Defense 4 + Discipline 1 = 5
│   Bypass now possible for Military ≥ 8 (3+ above Defense 5)
│   → Altonian army (if invasion fires): can now bypass Lowenskyst with Military 8
│   → Crown's defensive line collapses not from military defeat but from Parliamentary siege
│
├─ THE COUNTER-MOVES AVAILABLE TO CROWN:
│   ├─ Rebuttal (§5.5): roll Mandate vs Ob 2 (Embargo) or Ob 3 (Outlawry)
│   │   Overwhelming Rebuttal: both costs negated + proposer Mandate −1 → Hafenmark weakened
│   │   Crown's best play: Rebuttal early (while Mandate is still high and pool is good)
│   ├─ Player Parliamentary Intent (Standing 3+): flag Crown counter-evidence
│   │   +1D to Crown's Rebuttal roll → better chance of success
│   └─ Institutional Consolidation: if Crown somehow avoids all triggers for 1 season
│       +1 Stability + Accord +1 in one territory
│       → Delays the Stability collapse by 1 season but doesn't stop Wealth drain
│
├─ PLAYER POSITIONED ON CROWN SIDE:
│   Player at Standing 3 (Counselor) can:
│   ├─ Declare Parliamentary Intent to gather evidence against Baralta's Blockade justification
│   ├─ Support Crown's Rebuttal with Structural investigation findings (+1D)
│   └─ Conduct scene to undermine Löwenritter's Blockade motivation (social contest with Ehrenwall)
│   → Three parallel interventions; each costs 1 scene action
│   → Player at Normal difficulty (4 actions): can do all three AND still pursue 1 Conviction
│
└─ THE GUILDS PIVOT POINT:
    Guilds AI vote rule: votes against Blockade and Combined Embargo+Blockade
    (threatens Wealth → commercial instinct)
    → Guilds VOTE AGAINST this motion if it passes Supermajority review
    But: Combined Embargo+Blockade requires Supermajority (per §5.4)
    Guilds have ~2 Mandate
    Against Supermajority: 60% of participating Mandate required
    If Crown refuses to participate (targeted faction doesn't vote):
    Participating: Hafenmark 4 + Varfell 3 + Löwenritter 2 + Guilds 2 + Church 5 = 16 Mandate
    Supermajority: ≥10
    FOR: Hafenmark 4 + Varfell 3 + Church 5 = 12 (voting FOR to weaken Crown)
    AGAINST: Guilds 2 + Löwenritter 2 = 4 (Guilds resist Blockade; Löwenritter is military not economic)
    → 12 FOR vs 4 AGAINST: Supermajority passes (12÷16 = 75% > 60%)
    → Player needs to flip at least one faction to prevent the motion
    → Church Sacred Veto: if Crown is allied with Church... Church would block it
    → But Church Veto costs Mandate −1 (−2 if self-interested) → Church won't spend Veto on Crown
    → Player must flip Varfell through relationship/evidence or delay through Rebuttal
```

**New emergence:** Parliamentary economic siege is a specific multi-season arc that collapses faction military through Wealth depletion, which cascades into settlement Defense degradation. The chain Parliamentary → Wealth → Military → Garrison → Settlement Defense is now a specified, traceable path. The Guilds' voting behavior creates the pivot point that player intervention can exploit.

---

## CATEGORY O: INSTITUTIONAL CONSOLIDATION POSITIVE LOOP

---

### NEW-S33: CLEAN SEASON COMPOUNDING — THE STABILITY ACCELERATION LOOP

```
Root: Institutional Consolidation (§1.3 faction_layer): No Triggers 1-5 this season → Stability +1 + Accord +1 in one territory
      Province Accord (settlement_layer): derived from settlement Order averages
      Accord +1 at controller's choice: picks which territory gets the bonus

FACTION ACHIEVES 3 CONSECUTIVE CLEAN SEASONS
│
├─ CLEAN SEASON REQUIREMENTS:
│   No Trigger 1 (Territory loss/Occupation) — maintain all provinces
│   No Trigger 2 (Unfavorable treaty terms) — no capitulations
│   No Trigger 3 (Antagonistic Parliamentary vote) — no successful Censure/Outlawry against faction
│   No Trigger 4 (Major Subterfuge) — no successful Sabotage or Assassination against faction
│   No Trigger 5 (Failed Military) — no significant military defeats
│   AND: Accounting Stability check (§1.4): no ≥2 attribute losses this season
│
├─ SEASON 1 (CLEAN):
│   Stability +1 (toward seasonal cap ±2)
│   Accord +1 in one territory (player or faction AI chooses which)
│   → Target: lowest-Accord territory (to get it above the Accord 1 → 0 danger threshold)
│   → Or: highest-TCV territory (to maximize effective Prosperity recovery)
│
├─ SETTLEMENT ACCORD INTERACTION:
│   Province Accord is now DERIVED from settlement Order averages (not directly set)
│   "Accord +1 in one territory": does this modify settlement Order or is it a province-level bonus?
│   → GAP: settlement_layer derives Accord from Order, but faction_layer §1.3 grants direct Accord +1
│   → Resolution needed (NEW-OI-11 below)
│   Assuming: the consolidation Accord +1 functions as a direct province bonus, not through Order
│   → One province gets Accord +1 regardless of settlement Order averages
│   → This makes the consolidation bonus a province-level bypass of the settlement derivation
│
├─ SEASON 2 (CLEAN):
│   Stability +1 again (if below cap; cap is ±2/season)
│   Accord +1 in different territory (optimal: next-most-vulnerable)
│   After 2 clean seasons: 2 territories have Accord +1 bonus, Stability +2
│
├─ SEASON 3 (CLEAN):
│   Stability +1 → Stability now at baseline + 3 (three seasons of recovery)
│   Accord +1 in third territory
│   → 3 territories with Accord protection; Stability is high enough to shrug off 1-2 Triggers without crisis
│
├─ THE COMPOUNDING EFFECT:
│   High Stability → Accounting Stability check (§1.4) easier to survive (higher Stability pool)
│   Higher Stability pool on Accounting check → less likely to fail → Stability doesn't drop from cascade
│   → The clean season Stability gain makes future clean seasons MORE likely
│   → Cascade immunity: Stability 6+ means you can absorb 2 attribute losses without Accounting cascade
│       (Ob = magnitude of total attribute loss; at Ob 1-2, Stability 6+ pool wins comfortably)
│   → High Stability + preserved Accord → Province Effective Prosperity → Faction Wealth
│
├─ PLAYER ROLE IN ENABLING CLEAN SEASONS:
│   Player at Standing 3 (Counselor): can prevent Censure motions (Parliamentary defense)
│   Player fieldwork: expose Subterfuge before it fires (prevent Trigger 4)
│   Player governance: maintain Order ≥ 2 in all settlements (prevent Trigger 1 risk)
│   Player Thread ops: prevent RS crises that create territory instability (prevent cascade Triggers)
│   → A player who systematically prevents triggers enables faction clean seasons
│   → This is the "defensive specialist" arc: not winning grand victories but preventing losses
│   → After 3 clean seasons: faction is significantly stronger than it was at game start
│       even without the player taking any offensive action
│
└─ COMPOUND WITH MINE/PORT (NEW-S29):
    Clean seasons + Mine Prosperity passive Wealth + Port Trade passive Wealth
    = Stability rising + Wealth accumulating simultaneously
    After 4 clean seasons with Mine + Port governance:
    Faction Wealth: at cap (if starting at 4: Wealth 4 + 2/season = cap by Season 1.5)
    Faction Stability: +4 from consolidation (Stability at 6 for most factions by Season 4)
    → Faction is economically and institutionally at maximum strength without any offensive Domain Actions
    → Passive governance excellence is the foundation for the eventual offensive push
```

**New emergence:** Clean season compounding creates a defensive specialization arc where player intervention focuses on preventing negative events rather than creating positive ones. The Stability + Accord accumulation makes the faction progressively more resilient, enabling aggressive future actions from a position of strength.

---

## CATEGORY P: NPC RECRUITMENT × SETTLEMENT GOVERNANCE OFFER

---

### NEW-S34: TERRITORY GOVERNANCE OFFER × FRAGILE LOYALTY × GOVERNOR RELIABILITY

```
Root: NPC Recruitment §9.5 Step 3: "Territory governance (NPC gains administrative role over a territory): −2 Ob"
      Loyalty gate: Disposition +4 or +5 = not recruitable (genuinely loyal)
      Fresh recruit Disposition: 0 to +3 (barely above threshold or not at all)
      Settlement governor: if no governor, Order −1/season

PLAYER RECRUITS NPC OFFICER USING TERRITORY GOVERNANCE INCENTIVE
│
├─ NPC TARGET: Varfell military officer (Disposition +2 toward current faction, Disposition −1 toward Crown)
│   Loyalty gate check: Disposition +2 to Varfell → NOT at +4 or +5 → recruitable
│   Recruitment Ob: floor(2÷2)+1 = Ob 2
│   With governance incentive: Ob 2 − 2 = Ob 0 (minimum Ob 1: floor applies)
│   → Effectively auto-succeed with any roll (Ob 1 minimum per core engine)
│
├─ NEWLY RECRUITED NPC AS SETTLEMENT GOVERNOR:
│   Player assigns this NPC to govern S-028 Grauwald (T4, Town, Varfell territory, Order 2)
│   NPC at recruitment: Disposition toward player ~0 to +1 (just recruited, barely committed)
│   Conviction: unknown to player (not revealed at recruitment unless Overwhelming)
│   → Player has a settlement governor whose inner life is opaque
│
├─ WHAT THE GOVERNANCE OFFER MEANS MECHANICALLY:
│   The NPC's Loyalty (previously to Varfell): Disposition ~+2 to Varfell persists after recruitment
│   NPC now also has Disposition toward player: starts at 0 (no prior relationship)
│   → NPC is simultaneously:
│   ├─ Player's faction officer (duty-bound by recruitment)
│   └─ Varfell sympathizer with historical loyalty (+2 to former faction)
│
├─ FACTION INTELLIGENCE LEAK RISK:
│   NPC at Disposition +2 to Varfell: Vaynard's AI may target this NPC for counter-recruitment
│   Counter-recruitment Ob: floor(2÷2)+1 = Ob 2 (same as the original recruitment)
│   But: no governance incentive for Vaynard (NPC is now in player's faction)
│   Vaynard offers alternative incentive: faction resources, military advancement
│   → The governance offer that recruited the NPC made them cheap to get; it also leaves them cheap to lose
│
├─ CONVICTION UNKNOWN RISK:
│   NPC's Conviction is not revealed unless Overwhelming recruitment roll
│   Player assigned this NPC as governor of a settlement adjacent to RM cultural sites (Grauwald)
│   If NPC has hidden RM sympathy (deviation NPC in original territory):
│   → NPC governor of Grauwald actively facilitates RM Community Weaving (covert)
│   → CV −1/season potential in Grauwald (RM management effect)
│   → Province T4's Piety Track declining: Piety −1 → faction Accord in T4 affected
│   → Player doesn't know this is happening until they take Administer action (reveals one NPC Conviction)
│
├─ THE LOYALTY DEVELOPMENT PROBLEM:
│   NPC at Disposition 0 to player: doesn't meet companion formation requirements (needs +3)
│   NPC as governor: receives player's governance interaction (Administer reveals their Conviction)
│   But: player may never build Disposition high enough to know the governor's actual loyalties
│   → A settlement governed by an opaque NPC is a governance liability
│
├─ ADMINISTER AS LOYALTY INTELLIGENCE:
│   Player takes 1 scene at Grauwald settlement (costs scene action)
│   Administer action: Attunement + Governance History, Ob 2
│   Success: Order maintained + reveals one local NPC's active Conviction
│   → Reveals either the governor's Conviction OR an ambient NPC's Conviction
│   → Not guaranteed to reveal the governor specifically
│   At Overwhelming (net ≥ 2× Ob): reveals governor's Conviction (player chooses what to discover)
│   → Investment: 1 scene action to definitively understand your governor's loyalty
│
└─ OPTIMAL RECRUITMENT PRACTICE:
    Reveal Conviction before assigning governance:
    Recruitment success: NPC joins
    THEN: Take Administer scene before assigning to settlement (to learn Conviction)
    Cost: 1 additional scene action
    Payoff: governance assignment is informed (matching Conviction to settlement type)
    → An Equity-conviction NPC governs the market settlement (aligns with fair trade)
    → An Order-conviction NPC governs the fortress (aligns with military discipline)
    → A Faith-conviction NPC should NOT govern the RM outpost (Conviction conflict → governance failure)
    → [Companion formation §2.2]: Overwhelming recruitment reveals one personal Conviction automatically
       → If player needs to recruit a governor quickly: Overwhelming recruitment is worth pursuing
       because Conviction revelation is a governance prerequisite
```

**New emergence:** The governance incentive (−2 Ob) makes recruitment cheap but creates a "cheap-and-opaque" NPC who may be a loyalty risk from day one. Players who use governance offers to recruit will eventually need to spend scenes identifying the governor's true Conviction, paying the investigation cost they avoided at recruitment. The optimization trap: paying once for investigation vs paying repeatedly for unknown governance outcomes.

---

## CATEGORY Q: ACCORD → TCV → PENINSULAR SOVEREIGNTY CHAIN

---

### NEW-S35: ACCORD ZERO → TERRITORY LOSS → TCV REMOVAL — THE NON-MILITARY CONQUEST PATH

```
Root: Peninsular_strain §2: Accord 0 → territory becomes Uncontrolled at Accounting
      Faction_layer §2.3: Occupied territory TCV = 0 for both parties
      Peninsular_strain §1: Universal Victory = TCV ≥ 19 + Accord ≥ 2 in all controlled provinces
      Settlement Order → Province Accord (settlement_layer §1.3): Order floor can drop Province Accord to 0

OPPONENT FACTION RUNS SYSTEMATIC ACCORD SUBVERSION TARGETING ENEMY'S WEAKEST SETTLEMENTS
│
├─ TARGET: Crown province T5 Feldmark (2 settlements: S-008 Order 4, S-009 Order 2)
│   Province Accord: floor((4+2)/2) = 3
│   Vulnerability: S-009 at Order 2 is the weak link
│
├─ PHASE 1: SUBVERSION OF S-009 (2 seasons):
│   Domain Action: Subversion vs settlement Order
│   S-009 Feldmark Storehouse (Mine type, Order 2): Ob = Order + 1 = Ob 3
│   Season 1 success: Order 2 → 1; Province Accord = floor((4+1)/2) = floor(2.5) = 2 (still compliant)
│   Season 2 success: Order 1 → 0; Province Accord = floor((4+0)/2) = floor(2.0) = 2? 
│   → BUT: Order 0 triggers Settlement Revolt automatically
│   → Settlement Revolt: governor expelled, Order effectively drops further
│   → Province Accord = floor((4+0)/2) = 2 WITH revolt active → does revolt impact the calculation?
│
├─ INTERPRETATION: ORDER 0 CONTRIBUTION:
│   If Order 0 counts as 0 in the average: floor((4+0)/2) = 2 (Province Accord barely holds)
│   If Order 0 triggers additional Accord penalty (revolt = active disruption): Province Accord drops to 1
│   → Need ruling (NEW-OI-12 below)
│   Assuming revolt adds −1 to province average: Province Accord 2 − 1 = 1 → Resistant
│   → Territory Effective Prosperity = 0 (Accord 1 = Resistant)
│   → Territory requires garrison or Accord → 0 next Accounting
│
├─ PHASE 2: LETTING GARRISON COST DRAIN THE DEFENDER:
│   Crown must garrison T5 to prevent Accord 0 → Uncontrolled
│   Garrison cost: −1 Military pool per garrisoned territory (faction_layer §2.3)
│   Crown has multiple occupied/vulnerable territories (T5, T6, potentially T3)
│   Each garrison = −1 Military
│   → Crown Military draining from garrison requirements without any battles
│   → [NEW-S32 chain]: Military decline → Garrison Discipline decline → Settlement Defense decline
│
├─ PHASE 3: ACCORD 0 → UNCONTROLLED:
│   If Crown garrison fails the Accounting Revolt check (Military vs Ob 2):
│   Garrison retreats; territory becomes Uncontrolled
│   TCV consequence: Uncontrolled territory → TCV 0 for both parties
│   T5 Feldmark TCV: 1 (from peninsular_strain §1 table)
│   Crown TCV: 12 (starting) − 1 (T5 lost) = 11
│   → Crown is now 1 TCV below starting position without any military engagement
│
├─ REPEATING: SYSTEMATIC NON-MILITARY EROSION
│   Season 1-2: T5 subverted → Uncontrolled (TCV 11)
│   Season 3-4: T2 Kronmark (weakest Order among remaining Crown territories) subverted
│   T2: S-004 Order 3 + S-005 Order 3 → harder (Ob 4 per settlement) but achievable over 3-4 seasons
│   → Crown TCV eroding by 1 TCV/2 seasons through subversion alone
│   After 8 seasons: Crown TCV could be at 9 (from 12) without a single battle
│
├─ UNIVERSAL VICTORY GATE:
│   The opponent faction's victory condition: TCV ≥ 19 + Accord ≥ 2 in all controlled provinces
│   They are not gaining TCV by subverting Crown (Uncontrolled territories give 0 TCV)
│   BUT: Crown is losing TCV → opponent's relative position improves
│   → Plus: Uncontrolled territory can be reclaimed through Govern action (cheaper than conquest)
│   After Crown revolts occur: opponent Governs the Uncontrolled territories (Domain Action)
│   Govern success → Accord 1 installed → territory comes under opponent control with minimal military
│
└─ PLAYER DEFENSE:
    Player governing player-controlled settlement: maintains Order ≥ 2 → province immune to subversion
    The only provinces immune to subversion are player-governed ones (proactive defense)
    → Player as settlement governor is not just a progression arc; it's the ONLY defense against this attack
    → [NEW-S1]: Province Accord sabotage + [NEW-S35]: TCV removal chain = the full non-military conquest arc
    → Together: the opponent can dismantle Crown's territorial position using Parliament + Subversion + Govern
      in sequence with zero military engagement, zero combat, zero Thread operations
    → This is the "Political Conquest" path: the game's most elegant (and most dangerous) factional arc
```

**New emergence:** Settlement subversion → Province Accord collapse → territory Uncontrolled → TCV removal → opponent Governs creates a complete non-military conquest path. Combined with NEW-S32 (Parliamentary economic siege) and NEW-S26 (Censure/Parliament), an opponent can systematically dismantle a faction's territorial position through governance and politics alone.

---

## CATEGORY R: NEW FACTION PARLIAMENT GAP

---

### NEW-S36: FACTION EMERGENCE DECLARATION → PARLIAMENT ACCESS → MANDATE BOOTSTRAP PROBLEM

```
Root: Faction Emergence Stage 4 → "new faction" (settlement_layer §6.2)
      Formal Faction Declaration: Domain Action (Influence pool = Renown ÷ 2, Ob 3)
      Parliament participation: "any faction with Mandate ≥ 2 may declare Parliamentary Motion" (§5.2)
      New faction starts with what Mandate?

PLAYER COMPLETES FACTION EMERGENCE DECLARATION (STAGE 4)
│
├─ PREREQUISITES MET:
│   Renown 7+ (player), Control 4+ settlements across 2+ provinces, Renown 7+
│   Declare faction: Influence pool = floor(7÷2) = 3 dice, Ob 3
│   Roll: success → new faction formally declared
│
├─ THE MANDATE BOOTSTRAP PROBLEM:
│   New faction: no specified starting Mandate in current design
│   Without Mandate: cannot propose Parliamentary motions (needs Mandate 2)
│   Without Parliamentary access: cannot issue Censure, Embargo, War Authorisation
│   Cannot participate in Treaty Ratification votes (the primary mechanism for legitimacy)
│   Cannot be subject to Parliamentary motions affecting them meaningfully
│   (they have no Mandate to lose from Censure)
│
├─ WHAT THE NEW FACTION DOES HAVE:
│   Influence (from Renown operations): floor(Renown÷2) as independent Domain Action pool
│   Wealth (from Mine/Port governance if established)
│   Military (if player has built military capacity through mass combat)
│   Settlements (4+ → Stage 4)
│   → All non-Mandate faction stats may be present but Mandate is unspecified
│
├─ MANDATE SOURCES IN EXISTING DESIGN:
│   TCV contributes to some form of Mandate (params_board_game.md §Institutional Mandate PP-189)
│   Institutional Mandate presumably derives from territorial control
│   Player's 4+ settlements across 2+ provinces: some TCV value
│   → If TCV = Mandate: player with 4 settlements might have TCV 2-4
│   → But: TCV calculation for settlements vs provinces is not specified for sub-provincial factions
│
├─ THE PRACTICAL GAP:
│   New player-faction declares at Stage 4
│   Existing factions (Crown Mandate 5, Church Mandate 5, Hafenmark Mandate 4) have high Mandate
│   Parliament Supermajority (60%): new faction with Mandate 2 is a minor voice
│   Church Sacred Veto: can cancel any motion by the new faction
│   → New faction enters Parliament at the bottom of the power hierarchy
│   → Every motion they propose can be blocked by Church Veto
│   → They cannot Censure established factions (insufficient Mandate to pass)
│
├─ RECOGNITION CHALLENGE AS ENTRY MECHANISM:
│   Succession Endorsement (§5.4): "any signatory Mandate 3" can propose
│   War Authorisation (Mandate 2): new faction with Mandate 2 can propose War Authorisation
│   → War Authorisation gives the first military Casus Belli against an established faction
│   → War Authorisation requires Majority: 50% of participating Mandate
│   → With Guilds and Niflhel voting strategically, new faction can potentially pass War Authorisation
│      against the weakest established faction (Varfell after Vaynard crisis, Mandate 3-4)
│   → First Parliamentary action of new faction: WAR AUTHORISATION against Varfell
│   → This is the entry into national-level conflict with institutional legitimacy
│
├─ PLAYER SOCIAL PATH TO MANDATE GROWTH:
│   Winning contested social scenes, Grand Contests, and achieving Domain Echoes
│   → "NPC arc influenced" = Renown +1; some arc resolutions may carry Mandate implications
│   Parliamentary Subsidy (receives): allied faction votes Subsidy to new faction → Wealth +1
│   Subsidy receipt indirectly enables mustering (Military growth)
│   → New faction must be subsidized by established allies before it can act effectively
│
└─ THE BARALTA CITY-STATE PRECEDENT (from NEW-S20):
    Baralta city-state (Gransol Duchess, no national-level Mandate):
    Her Influence 4 + Parliament institutional knowledge
    → If Baralta city-state is formally recognized by Parliament: Mandate 2 (Recognition Challenge proposable by allied faction)
    → Recognition Challenge: costs proposer Mandate −1; if passed, city-state gets Mandate presence
    → BARALTA'S RE-ENTRY: allied faction proposes Succession Endorsement (or Recognition Challenge) for Baralta
    → Baralta re-enters Parliament at Mandate 2 (city-state level)
    → New player faction allies with Baralta: combined Parliamentary voice = Mandate 2 + Mandate 2 = 4
    → The bootstrap problem for the new faction is solved by Baralta's city-state providing
       institutional legitimacy through alliance
    → [NEW-S20] × [NEW-S36]: these two scenarios chain: player builds faction → discovers Parliament gap
       → allies with Baralta city-state → bootstraps Parliamentary presence through existing institution
```

**New emergence:** The new faction Parliament gap is a structural design hole that forces player-built factions to find workarounds. The most elegant workaround — Baralta city-state alliance — creates an emergent political pairing where two nominally weak actors combine to reach effective national-level Parliamentary participation.

---

## CATEGORY S: CROSS-SYSTEM INTERACTION — STYLE BONUS FIX

---

### NEW-S37: STYLE BONUS FIX × AUDIENCE COMPOSITION × PARLIAMENTARY GRAND DEBATE

```
Root: social_contest_v30 §3 Step 3 (revised): genre+orientation → style bonus dice
      Base: primary genre = +1D; Audience boost adds +1D to arguments matching their boosted axis
      Faction boosts are FIXED per faction: Church (Obscuring), Crown (Revealing), Varfell (Projection), Hafenmark (Memory)
      Parliamentary setting: all factions present → multiple audience boosts active simultaneously

GRAND DEBATE AT PARLIAMENT (Baralta's Solmund Claim, ARC 3)
│
├─ AUDIENCE COMPOSITION (all factions present in Parliament):
│   Church boost: Obscuring (+1D to any Obscuring-orientation argument)
│   Crown boost: Revealing (+1D to any Revealing-orientation argument)
│   Varfell boost: Projection (+1D to any Projection-genre argument)
│   Hafenmark boost: Memory (+1D to any Memory-genre argument)
│
├─ THE STYLE MATRIX AT PARLIAMENT:
│   Any argument can receive UP TO +2D from genre+orientation alignment:
│   Memory + Revealing (Citation): Hafenmark +1D + Crown +1D = +2D bonus
│   Memory + Obscuring (Suppression): Hafenmark +1D + Church +1D = +2D bonus
│   Projection + Revealing (Vision): Varfell +1D + Crown +1D = +2D bonus
│   Projection + Obscuring (Insinuation): Varfell +1D + Church +1D = +2D bonus
│
├─ BARALTA'S OPTIMAL STYLE (she is arguing for Solmund-ordained authority):
│   Her argument: "Solmund appeared and acted in Hafenmark; my authority is older than the Church's interpretation"
│   Evidence-based (she needs to cite records): Memory genre (past precedent) + Revealing orientation (show facts)
│   → Citation style = Memory + Revealing
│   Audience bonus at Parliament: Hafenmark +1D + Crown +1D = +2D
│   → Baralta arguing Citation gets maximum audience bonus from two factions simultaneously
│
├─ HIMLENSENDT'S OPTIMAL COUNTER-STYLE:
│   Faith Conviction + Divine Command Ethical Framework: prefers Obscuring (institutional weight)
│   To counter Baralta's Citation: he needs Memory + Obscuring (Suppression — "the records must be reinterpreted")
│   Audience bonus for Himlensendt's Suppression: Hafenmark +1D (Memory) + Church +1D (Obscuring) = +2D
│   → Both sides get +2D from Parliament audience if they choose optimally
│   → The audience boost is SYMMETRICAL — it doesn't advantage either side
│
├─ THE GENUINE STRATEGIC DIFFERENCE:
│   Himlensendt's Faith conviction + Evidence Resonant Style = vulnerable to Revealing evidence
│   His optimal style (Suppression: Memory + Obscuring) means he's SUPPRESSING, not revealing facts
│   But: he has Conviction Wound 2 (from prior Lattice sessions, per NEW-S12)
│   At Wound 2: involuntary reveal in filter chain
│   → Himlensendt is trying to run Suppression but his Conviction state is LEAKING information
│   → The style he should run (Suppression) is undermined by his Conviction Wound state
│   → His filter-chain responses are involuntarily revealing despite his stylistic intent
│
├─ THE PARLIAMENT AUDIENCE GRAND CONTEST ADVANTAGE:
│   First exchange: standard preparation (+1D per §9.1) + audience boost (+2D) + Belief alignment (+1 Momentum → auto-success pre-roll spend)
│   Maximum Exchange 1 pool for aligned orator: standard pool + 1D (prep) + 2D (audience) + 1 auto-success (Momentum)
│   → This is the highest-advantage opening exchange in any Contest type
│   → Parliament Grand Debates are MORE decisive than private Grand Contests
│   → The style fix means choosing the right style at Parliament is worth ~+2D more than choosing wrong
│
└─ PLAYER APPLICATION:
    Player supporting Baralta's claim in the Grand Debate:
    Player's Argument style: Citation (Memory + Revealing) = +2D from Hafenmark + Crown
    But: player's best attribute may not be Memory (Recall)
    If player's primary attribute is Attunement (no adjudicator) but this is Crowd (Parliament):
    Primary Attribute SHIFTS to Charisma (Crowd adjudicator)
    → Style bonus (+2D) + primary attribute mismatch (Charisma for a non-Charisma player) = net neutral
    → A player who prepares for a Parliamentary Grand Contest must optimize both:
       Style (for audience bonus) AND attribute (for Crowd adjudicator type)
    → This is why the §4 structure note matters: Appraise the audience BEFORE committing to style
```

**New emergence:** The style bonus fix creates a "Parliament optimization" problem where the audience composition simultaneously advantages BOTH sides if they choose their styles correctly. The strategic lever is using Conviction Wound states (from prior Lattice sessions) to prevent the opponent from executing their optimal style — making the pre-contest relationship management as important as the contest itself.

---

## CROSS-NEW-SCENARIO FEEDBACK LOOPS (BATCH 2)

---

### NEW-LOOP D: PARLIAMENTARY PRESSURE → MANDATE COLLAPSE → PARLIAMENT IMMUNITY PARADOX

```
A faction under sustained Parliamentary attack:
│
├─ Censure motion passes (Mandate ≥ 3 proposer, Majority): Mandate −1, Stability −1
├─ Faction uses Rebuttal (Mandate pool vs Ob 2): fails → Censure proceeds
├─ Faction loses Mandate below 3: Church cannot use Suppress normally (TC anchor weakens)
├─ Without Mandate 3: faction cannot PROPOSE Parliamentary motions (needs Mandate 2 minimum)
│   → A faction at Mandate 1 cannot propose Rebuttal against further Censure!
│   → [Rebuttal is a "declare in Phase 4" action that costs an action slot — not a roll-less defense]
│   → Actually: Rebuttal is available at Mandate 1 (it's an action slot, not a Mandate gate)
│   → But: the Rebuttal roll pool (Mandate pool vs Ob 2) at Mandate 1 = tiny pool
│   → 1 die vs Ob 2: near-certain failure
├─ Next Censure: Rebuttal fails → Mandate −1 → Mandate 0
└─ Mandate 0: faction has no Parliamentary voice
    But: no Parliamentary voice = no further Mandate costs from Censure (no Mandate to lose)
    → The faction at Mandate 0 is IMMUNE to further Parliament Censure (nothing to take)
    → TC pauses (if Church at Mandate 0)
    → But: Outlawry (Mandate −2) could force Mandate below 0 (floor at 0? Or negative?)
    → If Mandate floors at 0: Parliament attacks eventually exhaust themselves
    → If Mandate can go negative: the faction is permanently debilitated
    → [GAP NEW-OI-13]: Mandate floor not specified for negative territory
```

---

### NEW-LOOP E: RECRUITMENT INCENTIVE → FRAGILE GOVERNOR → COUNTER-RECRUITMENT → SETTLEMENT INSTABILITY

```
Player recruits NPC with governance incentive (NEW-S34):
│
├─ NPC placed as governor of settlement (governance offer fulfilled)
├─ NPC has historical Disposition +2 to former faction
├─ Former faction detects officer loss → counter-recruitment Domain Action
│   Ob: floor(2÷2)+1 = Ob 2 (same easy Ob)
│   Former faction offers something player cannot: return to home faction + advancement
├─ Counter-recruitment SUCCESS: NPC flips back to former faction
│   Settlement governor: VACANT (departed back to former faction)
│   Order −1/season begins (unmanaged)
│   Province Accord declining
│   Player's faction Disposition with former faction: −1 (officer poached back)
│   → [NEW-S3 chain]: companion-governor departure producing settlement crisis
├─ BUT: player used governance OFFER as the recruitment incentive
│   → NPC received governance role from player; leaving = breaking the arrangement
│   → If NPC leaves: Obligation violation? Was an Obligation created by the recruitment?
│   → [GAP NEW-OI-14]: Does the governance incentive create an implicit Obligation for the NPC?
└─ COUNTER-RECRUITMENT ARMS RACE:
    Player must now SECURE governors against counter-recruitment
    Security mechanism: build Disposition with the governor (3+ Connect scenes → Disposition +3)
    At Disposition +3: NPC is now approaching companion formation eligibility
    But: companion formation max = 2 companions
    → If player already has 2 companions: cannot formally companion the governor
    → Player has a governor they care about but cannot protect through companion system
    → The only protection: Knot formation (requires companion status or alternative mechanism)
    → [GAP NEW-OI-14b]: Can a non-companion NPC form a Knot with the player?
```

---

## OPEN ITEMS FOR JORDAN'S REVIEW (BATCH 2)

| ID | Finding | Priority |
|----|---------|----------|
| NEW-OI-11 | Institutional Consolidation "Accord +1 in one territory" (faction_layer §1.3) interacts with settlement-derived Province Accord. Does the +1 grant override the Order average calculation, or does it require increasing one settlement's Order value? Two different implementations. Needs ruling. | P1 |
| NEW-OI-12 | Settlement Order 0 (Revolt state) contribution to Province Accord average: does Order 0 count as 0 in the floor(average) calculation, or does active revolt add an additional penalty to Province Accord? If Order 0 counts literally, floor((4+0)/2) = 2 (Compliant), which means a single settlement revolt doesn't immediately crash Province Accord in a 2-settlement province. This seems too forgiving — verify intent. | P1 |
| NEW-OI-13 | Mandate floor: can faction Mandate go below 0? Parliamentary Outlawry (Mandate −2) against a faction already at Mandate 1 would produce Mandate −1. Does the floor apply? If no floor: repeated Outlawry can drive Mandate to −∞. If floor at 0: Mandate 0 faction is immune to further Parliament stat damage. | P1 |
| NEW-OI-14 | Governance offer as recruitment incentive (NPC Recruitment §9.5): does the governance assignment create a binding Obligation on the NPC, or is it a pure incentive? If pure incentive, the governance role can be abandoned (counter-recruitment). If Obligation: NPC must serve as governor for a specified duration or face consequences (but who enforces?). | P2 |
| NEW-OI-14b | Non-companion Knot formation: can a named NPC who is not a companion form a Knot with the player? The fieldwork system (§5.6) discusses Knot integration but doesn't explicitly require companion status. If non-companion Knots are possible: all high-Disposition NPCs (governors, officers, allies) could be Knotted. This dramatically expands the remote investigation network (NEW-S31). | P2 |
| NEW-OI-15 | New faction starting Mandate: the faction emergence declaration (settlement_layer §6.2) specifies no Mandate value for a newly declared faction. Either: (a) Mandate derives from TCV (and new faction needs to specify its TCV contribution), or (b) Mandate starts at 2 (minimum for Parliamentary participation), or (c) Mandate starts at 0 and must be built. Option (c) creates the Parliament bootstrap problem (NEW-S36). Which is intended? | P1 |
| NEW-OI-16 | Knot-mediated remote investigation (fieldwork §2.6) + Thread-Read Coherence cost: does remote investigation through a Knot carry the same Coherence cost as a standard Perceptive Leap? If yes: Knot-mediated remote investigation is Coherence-costly. If no: it's a "cheaper" form of investigation that the remote-investigation-as-intelligence-network (NEW-S31) may be over-powered. | P2 |
| NEW-OI-17 | Resistance Check (faction_layer §2.5): "once per Accounting, displaced faction may declare Resistance Check (free Accounting action)." Does a city-state (collapsed faction with no Mandate) retain the right to declare Resistance Checks? The Resistance Check is explicitly a "displaced faction" action — city-state Baralta was displaced from Hafenmark territory. She should qualify. Confirm. | P2 |
| NEW-OI-18 | Settlement-targeted Obligations (§6.1 C-08): "violation consequences are the same as province-level Obligations." But settlement stats are numerically lower than faction stats. Obligation "Crown must maintain Defense ≥ 2 in S-006" — if Crown withdraws garrison and Defense drops to base 4 (above 2 even without garrison): technically no violation. Needs clarification on whether settlement Defense means base stat only or effective stat (base + garrison Discipline). | P2 |
| NEW-OI-19 | Conviction 3+ Scar Roll 6 timing: "NPC acts on whichever Conviction most aligns with last PC interaction" — what is the temporal scope of "last"? Is it the last scene in the current season? The last scene ever? If "last scene this season": a player could set the Roll 6 anchor by engineering their last seasonal interaction. If "last scene ever": more stable but requires tracking. Define. | P2 |
| NEW-OI-20 | Style bonus fix (social_contest_v30 Step 3) + Dialogue Lattice handoff: when Lattice session escalates to Contest, does the Lattice session's utterance style (Revealing/Obscuring × Memory/Projection) inform the Contest's primary genre? The player made stylistic choices in the Lattice — do those carry as the Contest's starting genre, or does the Contest start fresh with genre determination at GM Setup (Step 2)? | P3 |

---

*End of Batch 2 document. 15 new scenarios (NEW-S23 through NEW-S37), 2 new feedback loops (NEW-LOOP D and NEW-LOOP E), 10 additional open items (NEW-OI-11 through NEW-OI-20).*
*Total across both batches: 37 emergent scenarios, 5 feedback loops, 20 open items.*
*Cross-references: faction_layer_v30 §§1-5, peninsular_strain_v1 §§2-4, social_contest_v30 §§3/6/9, npc_behavior_v30 §§3.3/5.2/9.5, settlement_layer_v30, player_agency_v30, companion_specification_v30*
