# VALORIA — Derived Stat System Specification
## Date: 2026-04-17
## Status: PROPOSAL — architectural addition to videogame layer
## Scope: Derived values from 1–7 faction stats, separating capacity (dice pools) from state (granular resources)
## Principle: Stats are what your faction CAN do. Derived values are what your faction HAS right now.

---

## §1 — The Problem

The 1–7 faction stat system was designed for a board game where stats ARE dice pools. This is elegant — one number serves two functions. But for a videogame, it creates three problems:

1. **Granularity.** ±1 on a 1–7 scale is a 14–100% change in capability. You can't express "a modest drain" because the smallest drain is enormous.
2. **Feedback.** The player sees "Wealth 4 → 3" and has to mentally calculate what that means. There's no visceral feedback.
3. **Conflation.** "How wealthy is my faction" (capacity) and "how much money do I have" (state) are forced into one number. A faction can be structurally wealthy (good trade infrastructure) but temporarily broke (just fought an expensive war), or vice versa.

## §2 — The Solution: Stats + Derived Values

Every faction stat (1–7) remains the dice pool for Domain Actions. No mechanical change to the resolution engine. Each stat additionally produces a **derived value** — a granular resource the player tracks and the engine consumes.

**Core principle:** Stats change rarely and represent structural capability. Derived values change frequently and represent current state. Stat damage (−1 Wealth) means your economy is structurally damaged. Derived value drain (−50 Treasury) means you're spending resources.

**Stat → Derived value mapping:**

| Stat | Dice Pool For | Derived Value | Derivation | What It Represents |
|------|--------------|---------------|------------|-------------------|
| **Mandate** | Govern, Crown Treaty, Peninsular Strain checks | **Legitimacy** | Mandate × 20, starting = stat × 20 | Popular/institutional trust capital. Spent by unpopular decisions, crisis responses, emergency authority invocations. Replenished by successful governance. |
| **Wealth** | Trade, Muster Wealth checks | **Treasury** | Wealth × 100, starting = stat × 100 | Accumulated economic resources. Spent by military upkeep, Campaign Supply, muster costs, construction. Replenished by Trade actions and territorial Prosperity income. |
| **Military** | Muster, BG Battle pool | **Levies Available** | Military × 2 (max units fieldable simultaneously) | Force projection capacity. Not a spendable resource — a ceiling. Raising units doesn't reduce it; it constrains how many you can have active. |
| **Influence** | Diplomacy, Intel, Treaty, Seizure | **Reputation** | Influence × 15, starting = stat × 15 | Political capital across factions. Spent by diplomatic actions, spy operations, political maneuvers. Replenished by successful diplomacy and intel wins. |
| **Stability** | Stability checks only (not a pool for actions) | **Cohesion** | Stability × 10, starting = stat × 10 | Internal faction unity. Drained by defeats, failed governance, internal conflict. Replenished by peaceful seasons and successful Govern. |

## §3 — How Derived Values Work

### 3.1 Income and Drain

Each derived value has **seasonal income** (automatic at Accounting) and **drains** (from actions, events, and ongoing costs).

**Treasury (from Wealth):**
- Seasonal income: Σ(Prosperity of controlled settlements) × 10 gold/season
- Trade Success: +Wealth × 25 gold (one-time)
- Trade Overwhelming: +Wealth × 50 gold
- Campaign Supply (units in hostile territory): −100 gold/season
- Siege (attacker): −100 gold/season per active siege
- Muster (Levy): −50 gold
- Muster (Professional): −150 gold
- Muster (Heavy Infantry/Cavalry): −300 gold
- Muster (Artillery): −500 gold
- Unit upkeep (professional units, per season): −25 gold per unit
- Construction (Fortify, infrastructure): −200 gold per action

**When Treasury reaches 0:** Faction cannot Muster, cannot Fortify, cannot perform any action with a gold cost. Professional units begin Discipline degradation (−1/season). At the NEXT Accounting where Treasury is still 0: **Wealth −1** (the economy is structurally damaged — not just broke, but broken). This is the only path from derived value depletion to stat damage.

**When Wealth stat drops:** Treasury maximum drops (new max = Wealth × 100). Treasury does NOT automatically drop — you keep what you have, but your income capacity is reduced. Recovery requires Trade actions to rebuild Wealth stat (existing mechanic, unchanged).

**Legitimacy (from Mandate):**
- Seasonal income: +5 per territory at Accord ≥ 2 (governed population supports the regime)
- Successful Govern action: +Mandate × 5
- Consensus Delay override (RM): −20 (community perceives authority violation)
- Emergency authority invocation: −30
- Unpopular Domain Action (action that drops Accord in any territory): −15
- Battle in own territory: −10 (population perceives failure to protect)
- Peninsular Strain Mandate check failure: Legitimacy −25 AND Mandate −1 (existing mechanic — stat damage triggers from crisis)

**When Legitimacy reaches 0:** Mandate check at Accounting (Ob 2). Failure: Mandate −1. The regime is losing structural authority, not just popular support. Accord −1 in all territories (population loses faith in governance).

**Reputation (from Influence):**
- Seasonal income: +5 per diplomatic relationship at Disposition ≥ +2
- Successful Intel/Spy action: +Influence × 5
- Successful Diplomacy: +Influence × 10
- Failed diplomatic initiative: −15
- Exposed Niflhel operation / Altonian Alignment discovery: −50
- Church Attention triggered against faction: −10
- Casus Belli declared against faction: −20

**When Reputation reaches 0:** Diplomatic actions take +1 Ob (nobody trusts you). Intel operations take +1 Ob (your agents are known and watched). At next Accounting with Reputation still 0: Influence −1.

**Cohesion (from Stability):**
- Seasonal income: +10 per peaceful season (no battle, no crisis event)
- Successful Govern action: +5
- Battle loss: −15
- Accord drops to 0 in any territory: −20
- Faction leader death/succession: −30
- Coup (Löwenritter): −50
- Internal faction schism (RM Schism, Church Cardinal defection): −40

**When Cohesion reaches 0:** Stability check at Accounting (Ob 1). Failure: Stability −1. Further Cohesion drain at Stability ≤ 2 triggers faction collapse checks per existing rules.

**Levies Available (from Military):**
This works differently — it's a ceiling, not a spendable pool. Military × 2 = maximum units that can be active simultaneously. If Military drops (from battle losses), the ceiling drops — if you're over the new ceiling, you must disband units until you're at or below the limit (representing loss of command infrastructure, not individual soldiers).

### 3.2 Stat Damage Only From Structural Failure

The key design rule: **no game event directly modifies a 1–7 stat except through derived value depletion or explicit major events.**

Current design has ~85 places where stats change by ±1 or ±2 from specific game events. Most of these should be converted to derived value changes:

| Current Rule | Conversion |
|-------------|-----------|
| "Battle loss: Military −1" | Treasury −200 (war costs) + Cohesion −15 (morale damage). Military −1 only if battle was Campaign-scale defeat. |
| "Campaign Supply: Wealth −1/season" | Treasury −100/season. Wealth −1 only when Treasury reaches 0. |
| "Stability −1 from failed Govern" | Cohesion −15. Stability −1 only when Cohesion reaches 0. |
| "Mandate −1 from Peninsular Strain" | Legitimacy −25. Mandate −1 only at Strain ≥ 7 (major crisis). |
| "Accord −1 in territory" | Stays as-is — Accord is already a per-territory value, not a faction stat. No conversion needed. |

**Events that SHOULD still directly modify stats (major structural shifts):**
- Faction collapse trigger (Stability directly to 0)
- Coup (Mandate directly modified)
- CI=100 Mass Seizure Declaration (stat resets for seized territories)
- Altonian Occupation beginning (stat overrides for occupied territories)
- Parliamentary Outlawry (Mandate −2, direct political destruction)
- Generational Shift (stat resets per succession rules)

These are rare, dramatic, campaign-altering events. The player should feel them as structural shocks, not routine fluctuations.

### 3.3 What the Player Sees

The faction overview screen shows:

```
CROWN OF VALORSMARK
━━━━━━━━━━━━━━━━━━━

Mandate ████████░░ 5      Legitimacy: 87/100
Wealth  ██████░░░░ 4      Treasury:  340/400 gold
Military ████████░░ 5     Levies: 7/10 fielded
Influence █████████░ 5    Reputation: 62/75
Stability ████████░░ 4    Cohesion: 35/40

Treasury this season: +65 income, −125 costs = −60 net
  Income: Valorsplatz (40) + Kronmark (15) + Feldmark (10)
  Costs:  Army in Lowenskyst (−100) + Unit upkeep (−25)
```

The player sees at a glance: my economy is bleeding (negative net treasury), my stability is fine, my reputation is moderate. They know they need to either pull troops back from Lowenskyst or Trade to boost income. The stat bars tell them structural capability; the derived numbers tell them current state.

### 3.4 Why This Is Better Than a Resource-Only Economy

The 1–7 stats remain the resolution engine. When the player attempts a Trade action, they still roll Wealth dice (4d10) against Ob. The Treasury is the *consequence* of Trade success, not the *input*. This preserves the elegant stat-as-pool design while giving the player granular feedback on their economic state.

If we went pure resource economy (5572 gold, no Wealth stat), the player would need to understand what gold amount maps to what probability of trade success, what military capacity their treasury buys, etc. The two-layer system (stats for capability, derived values for state) gives the player two different kinds of information through two intuitive displays.

## §4 — Settlement-Level Derived Values

The same principle applies at settlement scale. Settlement stats (Prosperity, Defense, Order) are 0–5 on the current design. These also benefit from derived values:

| Settlement Stat | Derived Value | Derivation |
|----------------|---------------|-----------|
| Prosperity | **Local Economy** | Prosperity × 50. Drained by siege, military action, famine events. Contributes to faction Treasury income. |
| Defense | **Garrison Strength** | Defense × 20 + Fort Level × 30. This is what the player sees when evaluating "how defended is this settlement." |
| Order | **Public Order** | Order × 20. Drained by oppressive actions, siege, faction transition. Below 0: riot events generate. |

Settlement derived values work the same way: granular drain/recovery, stat damage only from structural failure (Prosperity −1 only when Local Economy hits 0 and stays there).

**This connects settlement to faction:** a settlement's Local Economy contributes to the controlling faction's Treasury income. A settlement under siege has Local Economy draining, which reduces faction income, which drains faction Treasury, which eventually (if sustained) causes Wealth stat damage. The cascade is: siege → settlement economic damage → faction income loss → treasury depletion → structural economic damage. Each step is visible to the player. Each step is a decision point (lift the siege? trade harder? accept the loss?).

## §5 — Integration with Existing Mechanics

### 5.1 What Changes

- All "Stat ±1" events in current design documents are reviewed and converted to derived value changes EXCEPT explicit major structural events (listed in §3.2).
- Domain Action results (Trade Success = +gold, Govern Success = +legitimacy) replace stat modifications in most cases.
- The seasonal Accounting step adds derived value income/drain calculation before stat checks.
- UI displays both stat bars and derived value numbers.

### 5.2 What Does NOT Change

- The 1–7 stat scale.
- The d10 dice pool resolution engine.
- Ob tables for all Domain Actions.
- The card system (card hand, cooldown, action mapping).
- TC, PT, Accord, RS, IP — these are already distinct tracked values, not faction stats.
- Personal character stats (Charisma, Cognition, etc.) — these operate at a different scale and don't need derived values.
- Thread mechanics (Coherence, Thread Sensitivity) — already granular (10→0 and percentage scales).

### 5.3 Videogame Implementation

The engine maintains both layers:
- **Stat layer:** 1–7 values, used for dice pool resolution. Rarely modified. Displayed as capability bars.
- **Derived layer:** Granular values (0–max), used for economic simulation, upkeep, event consequences. Frequently modified. Displayed as resource numbers with income/drain breakdown.
- **Cascade rule:** Derived value reaching 0 AND remaining at 0 through next Accounting triggers stat −1. This is the ONLY routine path from derived to stat damage.

The player never sees dice pool calculations directly. They see: "Trade action — 72% success chance" (derived from Wealth stat pool vs Ob). "Treasury +340 gold on success" (derived from Wealth × 25 × modifiers). The engine translates between the two layers transparently.

## §6 — Calibration Notes

All derived value numbers in this document are PROVISIONAL. They need simulation to confirm:
- Income rates produce sustainable economies for each faction at starting stats
- Drain rates create meaningful pressure without immediate collapse
- Stat damage triggers are rare enough to feel consequential (once every 5–10 seasons, not every season)
- Starting derived values give factions 3–5 seasons of runway before economic pressure forces Trade actions

The specific multipliers (×100 for Treasury, ×20 for Legitimacy, etc.) are tuning knobs that can be adjusted without changing the architecture.

[EDITORIAL: ED-683 — Derived stat system. Architectural addition to videogame layer. Does not modify existing board game / hybrid mechanics — adds a presentation and simulation layer for Godot implementation.]

## §7 — Stat Modification Conversion Registry (PP-680)

Audit of all 51 stat ±1/±2 references across design docs. Each classified as CONVERT (routine → derived value drain) or KEEP (structural → direct stat modification).

### Converted to Derived Value (routine fluctuations):

| Original | Converted To | Files Affected |
|----------|-------------|----------------|
| Campaign Supply: Wealth −1/season | Treasury −100/season | mass_battle_v30 |
| Battle Partial: Stability −1 | Cohesion −15 | mass_battle_v30, military_layer_v30 |
| Battle loss (routed): Stability check Ob 1 | Cohesion −15 | mass_battle_v30 |
| Campaign defeat: Stability check Ob 2 | Cohesion −30 | mass_battle_v30 |
| Siege supply: Wealth −1/season | Treasury −100/season | military_layer_v30 |
| Siege failure: Stability −1 | Cohesion −15 | military_layer_v30 |
| Siege parley rejected: Stability −1 | Cohesion −15 | military_layer_v30 |
| Assert failure: Stability −1 | Cohesion −15 | tc_political, victory_v30 |
| Suppress failure: Stability −1 | Cohesion −15 | tc_political, victory_v30 |
| Govern failure at Prosperity 0: Stability −1 | Cohesion −15 | tc_political |
| Trade Success: Wealth +1 | Treasury +Wealth×25 | tc_political |
| Strain 3–4: Mandate check → Mandate −1 | Legitimacy −25 | tc_political, peninsular_strain |
| Seizure failure: Stability −1 | Cohesion −20 | peninsular_strain |
| Proclamation failure: Stability −1 | Cohesion −20 | peninsular_strain |
| Cultural Reformation failure: Stability −1 | Cohesion −20 | peninsular_strain |
| IP 90 inter-faction Battle: Stability −1 | Cohesion −20 | victory_v30 |
| Settlement expansion: Wealth −3 | Treasury −300 | settlement_layer |
| Mine surplus: Wealth +1 | Treasury +50/season | settlement_layer |

### Kept as Direct Stat Modification (structural events):

| Event | Stat Change | Rationale |
|-------|-----------|-----------|
| Battle loss (margin ≥2): Military −1 | KEEP | Losing a battle decisively IS structural military damage |
| Unit destroyed: Military −1 | KEEP | Permanent force loss |
| Campaign defeat: Mandate −1 | KEEP | Major political event |
| Crown Treaty: target Mandate −1 | KEEP | Diplomatic victory — structural |
| Appease (Institutional Mandate): Mandate −1 | KEEP | Deliberate institutional sacrifice |
| Parliamentary Censure/Outlawry: Mandate −1/−2 | KEEP | Formal political action |
| Crown-break: Stability −2, Mandate −1 | KEEP | Treaty betrayal — structural crisis |
| RM Uprising: Church Mandate −2/−1 | KEEP | Loss of territory — structural |
| Dynastic Proclamation success: target Mandate −1 | KEEP | Major political act |
| Trade Overwhelming: Wealth +1 | KEEP | Exceptional success = structural improvement |
| Govern OW in capital: Mandate +1 | KEEP | Exceptional governance = structural |
| Faction collapse triggers | KEEP | Terminal events |
| Coup, Occupation, Generational Shift | KEEP | Campaign-altering events |
| Peninsular Strain ≥7: Mandate check | KEEP | Existential crisis level |

### Design Principle

The dividing line: **would a real-world state experience this as "we had a bad quarter" (derived drain) or "our government has been fundamentally weakened" (stat damage)?** A failed siege is a bad quarter. A campaign-scale military defeat is structural. A failed trade mission is a bad quarter. An Overwhelming trade success that opens new markets is structural. The derived value layer absorbs the routine. The stat layer records the permanent.
