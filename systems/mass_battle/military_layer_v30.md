<!-- SKELETON — mechanical spec only -->
<!-- Infill: military_layer_v30_infill.md -->
<!-- PP-TBD series — awaiting patch assignment -->
<!-- Sources: mass_battle_v30.md §A.4, §A.13, §B.2, §B.3, §B.5; params_board_game.md §Unit Muster Ob Table, §Accord, §CI Generation; canonical_sources.yaml -->
<!-- Status: CANONICAL — approved 2026-04-17 (editorial batch acceptance) -->
<!-- Date: 2026-04-14 -->

# VALORIA — Military Layer: Unit Bridge & CI Revision
## v1.0 — Faction-layer unit representation → mass battle; CI competitive formula

---

## §0 — AUDIT NOTE

This document resolves two open editorial items:

| ID | Description | Resolution |
|---|---|---|
| FACTION-P2-01 | Military stat → unit Power/Discipline ceiling mapping | Adopted from mass_battle_v30 §A.4 table, confirmed |
| FACTION-P2-03 | Muster → unit stats | Size=2, Power=floor(Military/2)+1 per §A.13 adopted; modifiers added below |
| Command-EDIT-01 | Same as FACTION-P2-01 | Confirmed |
| Command-EDIT-03 | Same as FACTION-P2-03 | Confirmed |
| PP-402 | CI passive +1 per season | Revised to conditional passive; see §2 |

---

## §1 — UNIT REPRESENTATION: BOARD → MASS BATTLE

### §1.1 What a Unit Token Represents

A unit token on the board is a named military formation stationed in a specific territory. It has four stats, all tracked on the physical token or unit card:

| Stat | Range | What it means |
|---|---|---|
| **Type** | See §1.2 | Equipment, training, weapon class, armour class — set at Muster, fixed |
| **Size** | 1–7 | Headcount. Health pool. Casualties reduce it. At 0: formation destroyed. |
| **Discipline** | 1–7 | Organisational integrity. Degrades under combat stress. At 0: breaks. |
| **Experience** | 0–2 | Campaign history. Modifies effective Power within faction ceiling. |

Type, Power, weapon, and armour are pre-printed on the unit token (per mass_battle_v30 §B.2). Size and Discipline are tracked with markers on the token. Experience is a flip/stamp state (Fresh → Seasoned → Veteran).

### §1.2 Unit Types and Stats

Canonical from mass_battle_v30 §B.2. TTRPG equivalences are PROVISIONAL (marked [PROV]).

| Type | BG Martial | BG Disc | BG Health | TTRPG Power | TTRPG Size (TARGET) [PROV] | Weapon | Armour |
|---|---|---|---|---|---|---|---|
| Levy | 1 | 1 | 7 | 1 | 3 | LightCut | None |
| Light Infantry | 3 | 3 | 9 | 3 | 4 | LightCut | Light |
| Heavy Infantry | 4 | 4 | 10 | 4 | 5 | HeavyCut | Medium |
| Cavalry | 4 | 5 | 9 | 5 | 4 | HeavyCut | Heavy |
| Archer | 3 | 3 | 8 | 3 | 3 | Piercing/Bow | Light |
| Crossbow | 3 | 3 | 8 | 3 | 3 | Piercing/Crossbow | Light |
| Sling | 2 | 2 | 8 | 2 | 3 | Blunt/Sling | Light |
| Artillery | 2 | 2 | 8 | 2 | 3 | HBl (siege) | None |
| Knights Templar | 5 | 6 | 11 | 5 | 6 | HeavyBlunt | Heavy |

**TARGET Size (PP-714, MB-02 — editorial 2026-04-30):** The Size column above is the **target size** — what a fully reinforced unit looks like at full strength. It is NOT the muster output. A freshly mustered unit produces Size per §1.4 formula (base 2 + Prosperity modifier, max 4). Units build toward their TARGET via Reinforcement seasons (mass_battle_v30 §A.13). Upper bound on Reinforcement: cannot exceed TARGET. Knights Templar TARGET 6 is reachable via repeated reinforcement — Templar formations historically grew over years of recruitment, not single muster events.

### §1.3 Military Stat → Unit Power Ceiling

Per mass_battle_v30 §A.4 (confirmed, resolves FACTION-P2-01):

| Faction Military | Max unit Power | Starting Discipline ceiling |
|---|---|---|
| 1 | 1 | 2 |
| 2 | 2 | 3 |
| 3 | 3 | 4 |
| 4 | 4 | 5 |
| 5 | 5 | 6 |
| 6 | 6 | 7 |
| 7 | 7 | 7 |

A faction's Military stat sets both the highest Power unit it can field and the Discipline a fresh unit starts with. Hafenmark (Military 3) cannot field Power=4 Heavy Infantry regardless of Wealth or Prosperity — their training culture tops out at Professional.

**Crown standing army — Löwenritter (PP-701, doctrine note 2026-04-30):** Crown's pre-coup standing military force is the Löwenritter Order. Crown Military stat 5 is expressed through Löwenritter elite units (Power 5, Discipline 6). All Crown muster operations field Löwenritter units by default. Post-coup (Coup Counter trigger), Löwenritter splits as an independent faction with its own tactic cards (mass_battle §B.4) and its own row in stat tables. See faction_layer §1.5 for full doctrine note.

**Hafenmark equipment-quality doctrine (PP-700, mechanism TBD via simulation 2026-04-30):** Hafenmark Military stat 4 is mid-tier numerically but expressed mechanically as superior equipment quality from mining (T17 Halvarshelm) and smithing (T8 Gransol) infrastructure. Hafenmark-mustered units field above-quality-tier weapons and armour relative to peers. Exact mechanical expression — weapon damage modifier, effective Armour tier shift, or both — pending simulation testing. Doctrine canon fixed; calibration open. See faction_layer §1.5 and ED-776 standing flag.

Knights Templar (Power 5, Disc 6) are Church-only and not governed by the Military ceiling. They are raised through a separate ecclesiastical process, not standard Muster.

### §1.4 Muster Output

Per mass_battle_v30 §A.13 (PROVISIONAL — FACTION-P2-03):

A single Muster action produces one unit with:
- **Size = 2** (base)
- **Power = floor(faction Military / 2) + 1** (base)
- **Discipline** = min(general's Command, faction Military ceiling) — for BG: min(floor(Military/2), ceiling from §1.3)
- **Type** = determined by prerequisites met at Muster time (see §1.5)

**Population modifier to initial Size:**
Territory population governs the levy pool available for drafting. A heavily populated territory can fill out a formation faster.

| Territory Prosperity | Initial Size bonus |
|---|---|
| 1–3 | +0 (Size = 2 base) |
| 4–5 | +1 (Size = 3) |
| 6–7 | +2 (Size = 4) |

This is a one-time modifier at Muster, not ongoing. A Levy mustered in Valorsplatz (high Prosperity) starts larger than one raised in Oastad. After Muster, both are subject to the same attrition rules.

**Aggregation:** Multiple units of the same Type stationed in the same territory may be merged at any Muster action: combine their Sizes (max 7 total). Merged units share the lower Discipline value. This represents consolidating scattered formations into a single coherent force.

Multiple Muster actions without merging produce additional separate unit tokens — each deployable independently. Separate tokens allow garrisoning multiple adjacent territories from a central muster point.

### §1.5 Muster Prerequisites

Per params_board_game §Unit Muster Ob Table:

| Type | Ob | Prerequisites |
|---|---|---|
| Levy | 1 | None |
| Light Infantry | 1 | None |
| Heavy Infantry | 2 | Territory Prosperity ≥ 5 AND Wealth Ob 2 (separate roll) |
| Cavalry | 3 | Territory Prosperity ≥ 6 OR named officer with Cavalry History |
| Ranged (Archer/Crossbow/Sling) | 2 | Named officer with Ranged proficiency |
| Artillery | 4 | Wealth Ob 4 (separate roll) + 1 season construction delay |
| Knights Templar | Church only | Sacred Assembly action (not standard Muster); see §1.8 |

**Prosperity** governs what quality troops can be raised from a territory's population. A rich farming province (Feldmark, Prosperity 4) can sustain Light Infantry but not Heavy Infantry — the population doesn't have the metallurgical infrastructure. Only wealthy urban or heavily garrisoned territories (Valorsplatz, Ehrenfeld) meet the Heavy Infantry Prosperity threshold.

**Wealth** gates professional unit quality — you need money to equip and pay soldiers. Wealth expenditure (Ob 2 for HI, Ob 4 for Artillery) is a separate roll from the Muster roll. Both must succeed for the unit to be raised at that quality. On Muster Success but Wealth Failure: unit raised as Light Infantry instead (the cheaper available type).

### §1.6 Experience

A unit gains one Experience step after surviving a battle in which its faction won or drew, and it was not destroyed (Size > 0 at resolution):

| Experience | Status | Effect |
|---|---|---|
| 0 | Fresh | Power = base (from §1.4 formula) |
| 1 | Seasoned | Power +1 (cannot exceed faction Military ceiling from §1.3) |
| 2 | Veteran | Power +1 additional (cannot exceed faction Military ceiling) |

Experience is marked on the unit token (flip/stamp states). It represents the soldiers who survived understanding how to fight, not just being told.

A destroyed unit (Size = 0) loses all Experience. Re-mustering that formation (new Muster action on the same token) resets Experience to 0. This makes experienced units worth protecting — they cannot be trivially replaced.

Experience does not transfer when units are merged. Merged unit retains the higher Experience of the two constituent units.

### §1.7 Wealth Zero and Unit Degradation

When a faction's Wealth reaches 0:
- At each subsequent Accounting, all Heavy Infantry and Cavalry units belonging to that faction lose Discipline −1 (mercenaries and professional soldiers going unpaid)
- Levy and Light Infantry units are unaffected (they are conscripts or locally sustained)
- Discipline at 0 destroys the unit (they desert or disintegrate)

This is more specific than the prior simulation's Military −1 at Wealth 0. Military stat itself does not degrade from Wealth shortage — the faction still has officers and doctrine. It loses the ability to keep its professional formations intact.

Recovery: when Wealth rises above 0, Discipline degradation stops. Discipline does not auto-recover — requires Muster action on existing unit (representing retraining and equipment replacement). **This applies between battles as well (PP-712, MB-04, editorial 2026-04-30):** Discipline degradation accumulated in battle persists across battle boundaries. Garrison time alone does not restore Discipline; only a Muster action on the existing unit does. Wealth-Zero degradation stacks with battle degradation.

### §1.8 Knights Templar (Church Only)

Knights Templar units cannot be raised through standard Muster. They require Sacred Assembly: a Senator (Social) action in Himmelenger (T9) or a Church-held territory with PT ≥ 4. Ob = 3. No Wealth roll required — Templar funding is internal to the Church.

Knights Templar: Martial 5, Discipline 6, Health 11. TTRPG: Power 5, Size 6, HeavyBlunt, Heavy armour. Anti-Armour keyword (pre-printed).

Unit cap for Templar: max 2 Templar units active simultaneously, regardless of Military stat. They are elite and rare.

Templar units have CI implications — see §2.5.

---

### §1.9 Siege Action (NEW — ED-633, approved 2026-04-17)

Extended encirclement targeting a fortified territory. Replaces Battle against garrisoned Fort ≥ 2.

**Card:** Legionary Inward. Requires 1 Legionary card + ≥ 1 unit adjacent to target.  
**Pool:** (Attacker Military stat) + 3 (siege engineering bonus — engineers, equipment, sapper crews), TN 7. **Ob:** 2 + Fort Level. *(PP-715, MB-07 — editorial 2026-04-30. Replaces prior "Pool = Military stat" formulation, which produced mathematically impossible calibration: Fort 3 + Mil 4 = Ob 5 from 4 dice = 0%, contradicting stated ~2% rate. New formula: Fort 3 + Mil 4 = Ob 5 from 7 dice = ~2% match.)*

| Degree | Fort effect | Cost |
|--------|-------------|------|
| Overwhelming | Fort −2 | MS −1, Wealth −1 |
| Success | Fort −1 | MS −1, Wealth −1 |
| Partial | No change | MS −1, Wealth −1 |
| Failure | No change | Stability −1, Wealth −1 |

**Cap:** 5 seasons. Then: Assault (at current Fort) or Withdraw. **MS:** −1/season (threadwork §5.2).  
**Garrison supply:** Consul Outward Ob 2 from adjacent territory. Fail: Garrison Discipline −1/season.  
**Calibration:** Fort 3, Military 4 = Ob 5 from pool 7 ≈ 2%/season (matches stated rate). Requires Military 5+ (pool 8, ~5%) or political bypass for practical reduction. Higher-Mil factions can sustain siege; low-Mil factions cannot reduce a Fort 3+ stronghold without diplomatic or Thread approaches.

## §2 — BG BATTLE RESOLUTION (CANONICAL)

### §2.1 Pool Formula

Per mass_battle_v30 §B.3 (canonical design doc, supersedes simplified PP-499 description):

**Battle pool = Σ(Martial of all engaged unit tokens) + floor(faction Military / 2)**

- Each unit token physically present in the territory contributes its Martial value
- Commander bonus = floor(Military stat / 2) — this is the generalship abstraction (PP-555)
- Fort Level adds bonus dice to the defending pool (per existing rule)
- Tactic card disposition sets Ob (base Ob 2 for Standard Advance vs. Standard Advance)

**Why this is correct:** The BG pool formula means that deploying more units to a battle genuinely matters — a faction with 3 Light Infantry tokens (3+3+3 = pool 9 before commander bonus) is substantially stronger than a faction with 1 Light Infantry token (pool 3 + bonus). This models the mass-of-troops dimension of real battles. The TTRPG formula (min(Size,Command)+Command) achieves the same result through the Size stat — more soldiers = more dice until capped by Command.

### §2.2 Battle Outcome (Margin System)

Per mass_battle_v30 §B.3, §PP-104:

| Result | Condition | Outcome |
|---|---|---|
| Attacker wins | Attacker net ≥ Defender net + 2 | Territory captured; Defender Military −1 |
| Partial | Margin ≤ 1 either direction | No territory change; Attacker Stability −1 (commitment cost) |
| Defender wins | Defender net ≥ Attacker net + 2 | No territory change; Attacker Military −1 |

**Unit damage:** distribute net successes × Martial Damage Modifier across defender's units (attacker chooses which units take damage, reducing their Health/Size). Formation Break at Size 0.

**Fort bonus dice to defender:** applies to the defender's pool, not as Ob. A Fort 3 territory gives the defender +3 dice on top of their Martial sum + commander bonus. This represents fortifications giving defenders a material advantage in the engagement, not making attackers less accurate.

### §2.3 BG → TTRPG Handoff

Per mass_battle_v30 §B.5. When PC faction leader is present in the contested territory, TTRPG mass battle rules fire:

| BG stat | TTRPG equivalent |
|---|---|
| Unit Type (token) | → Power, Weapon, Armour per §1.2 table |
| Unit Size (tracked on token) | → Size (direct) |
| Unit Discipline (tracked on token) | → Discipline (direct) |
| Faction Military stat | → Command rating for NPC generals |
| Commander bonus = floor(Military/2) | → informational; TTRPG uses full Command |

Units from BG with Size tracked: use that Size directly. Do not use the B.2 TTRPG Size default — that is for newly minted units without tracked Size.

---

## §3 — CI REVISION: COMPETITIVE FORMULA

### §3.1 Repeal of PP-402 (Unconditional Passive)

PP-402 (CI +1 passive per season, unconditional) is **repealed** by this document.

**Rationale.** The unconditional passive treated the Church Influence as a countdown clock whose advance required no Church action and could not be zeroed out even by sustained opposition. Historically, the Church's institutional authority required continuous active maintenance — preaching, charitable works, military enforcement of doctrine, and genuine popular piety. These are not passive. When the Church failed to perform them — when secular authorities provided welfare, when heresy spread, when Templar orders were expelled — CI fell. The passive ensured Church always won in long games regardless of play quality.

PP-402 is replaced by a conditional passive (§3.2) and explicit competitive sources (§3.3–§3.6).

**Legacy CI sources note (from params_board_game):** "Altonian diplomacy momentum, Attention Pool threshold, Emergency Powers, Free Trade Decree, Church unit presence are subsumed into the Piety Yield system." This document restores Church unit presence as an explicit source (§3.5) and formalises the Wealth/charity dimension (§3.4). Piety Yield is retained and refined (§3.3).

### §3.2 Conditional Passive

CI advances by +1 passively each season **only if** Church is Prominent in **2 or more territories** at Accounting time. **Prominent:** Church controls the territory, OR Church Mandate > the controlling faction's Mandate. (CI-01 fix 2026-04-29: Church is always Prominent in territories it controls.)

| Prominent territory count | CI passive |
|---|---|
| 0–1 | +0 (Church is marginal; no institutional weight) |
| 2–4 | +1 (Church has meaningful civil presence) |
| 5+ | +2 (Church dominates civil society across the peninsula) |

Church prominence is the existing ED-326 mechanic (Church Mandate > controlling faction Mandate per territory), updated every Accounting. This conditional passive preserves the historical reality that the Church's calendar, sacraments, and parish infrastructure are always operating — but only generates CI momentum when the Church actually has institutional reach.

### §3.3 Piety Yield (Retained, Refined)

For each territory where Church is Prominent:

| Territory PT | CI yield |
|---|---|
| 5 | +1 |
| 4 | +0.5 (fractional; floor at Year-End Accounting) |
| 3 | +0.25 (fractional; floor at Year-End Accounting) |
| 1–2 | +0 |

This is the existing Piety Yield mechanism, extended to include PT 3 as a fractional contributor. PT 3 represents a population that attends church and observes the sacraments but isn't devoted enough to drive institutional authority. Over multiple seasons it accumulates.

**PT 5 in T9 Himmelenger** (starting value) generates +1 CI/season whenever Church is Prominent there. Losing T9 or allowing PT to drop below 5 meaningfully reduces Church's CI income.

### §3.4 Charity Advantage

Church has a unique ability to translate Wealth into CI through acts of charity, almsgiving, and institutional welfare provision that rival secular authorities.

At each Accounting: for each territory where Church is Prominent AND Church Wealth ≥ (controlling faction Wealth + 2):

- CI +0.5 per qualifying territory (fractional; floor at Year-End)

**Maximum from this source:** +1 CI per season (requires 2+ qualifying territories).

This represents the Church outspending the secular government on social welfare in that territory — feeding the poor, maintaining hospitals, supporting orphans. When the Church is richer than the duke and visibly more generous, CI rises because the population's loyalty tilts ecclesiastical.

**Church must actively maintain Wealth** to trigger this. If Church Wealth drops (from Parliamentary Embargo, Blockade, or general economic pressure), this source dries up. It rewards economic investment in the Church's institutional role, not just aggressive military or political action.

### §3.5 Templar Presence

Each territory where Church has a Knights Templar unit stationed AND the territory's PT ≥ 3:

- CI +1 per qualifying territory
- **Maximum from this source:** +2 CI per season

Templars enforce ecclesiastical law physically — suppressing heresy, protecting Church property, projecting authority. Their presence in a pious territory reinforces the Church's institutional claim over that territory in ways that no number of sermons alone can match.

The PT ≥ 3 gate matters: Templars stationed in a secular or resistant territory (PT 1–2) don't generate CI because the population regards them as occupying forces, not defenders of the faith.

**Design note:** This restores the legacy CI source "Church unit presence" (subsumed by PP-205/Piety Yield system) as an explicit named source. It is not redundant with Piety Yield — it fires additionally when Templar units are physically present, representing enforcement, not merely popular piety.

### §3.6 Assert Action

Assert (existing Standard Action, Church only, Pontifex/Senator Priority):

| Assert result | CI effect | Stability effect |
|---|---|---|
| Overwhelming | +2 CI | — |
| Success | +1 CI | — |
| Partial | +0 CI | — |
| Failure | +0 CI | Church Stability −1 |

Assert represents Church actively preaching, issuing papal decrees, performing public ecclesiastical acts of authority. The Overwhelming result represents Assert so decisive that no secular argument can answer it — the Church has won the narrative battle for that season.

Assert is a proactive investment. Church must spend an action slot on it, choosing between Assert and other priorities (Seizure, Charity operations, diplomatic actions).

### §3.7 Suppress (Opponent)

Existing rule retained. Any PLAYABLE faction may declare Suppress as a Senator/Mandate action.

| Suppress result | CI effect | Stability effect |
|---|---|---|
| Overwhelming | Negate this season's conditional passive AND Piety Yield | — |
| Success | Negate this season's conditional passive only | — |
| Partial | No effect | — |
| Failure | No CI effect | Suppressing faction Stability −1 (existing named exception to PP-403 repeal) |

Suppress requires real political capital — it is a public act of secular authority challenging Church institutional claims. A powerful, stable Crown or Hafenmark can do this successfully. A weakened, occupied faction cannot.

### §3.8 Hafenmark Structural Suppression (Baralta)

Existing rule retained. While Inge Baralta NPC Mandate ≥ 4: CI −1 per season automatically at Accounting. This is institutional expertise, not a Domain Action.

### §3.9 CI Seasonal Cap

Per PP-504 (unchanged): ±5 CI per season from all sources combined. ±3 from player-initiated Domain Actions specifically.

### §3.10 CI Cap and Seizure

CI caps at 100 (no freeze). Church Mass Seizure available at CI ≥ 60 (one-shot). See victory_v30 §3.2/§7.

### §3.11 Full CI Accounting Sequence

Execute in order at Phase 5 Step 4:

1. **Conditional Passive** (§3.2): 0, +1, or +2 based on Prominent territory count
2. **Piety Yield** (§3.3): fractional per Prominent territory × PT tier
3. **Charity Advantage** (§3.4): fractional per qualifying territory
4. **Templar Presence** (§3.5): +1 per Templar in PT ≥ 3 Prominent territory (max +2)
5. **Assert result** (§3.6): fires if Assert action was played this season
6. **Suppress result** (§3.7): fires if Suppress action was played this season; may negate Steps 1-2
7. **Hafenmark Structural Suppression** (§3.8): −1 if Baralta Mandate ≥ 4
8. Apply seasonal cap (PP-504): ±5 total

---

## §4 — ACCORD AND PROSPERITY: MILITARY INTERACTION

### §4.1 Accord as Population Commitment

Accord (per-territory, 0–3) already governs Prosperity and PV per params_board_game. It also directly affects military engagement:

| Accord | Battle effect | Muster effect |
|---|---|---|
| 3 (Aligned) | Defender +1D (already canonical) | All unit types available per Prosperity |
| 2 (Compliant) | No modifier | All unit types available per Prosperity |
| 1 (Resistant) | Martial −1 for all units raised here this season | Only Levy available regardless of Prosperity |
| 0 (Revolt) | Cannot use these units offensively | No Muster possible |

**Resistant territory (Accord 1):** The population is conscripted, not committed. Units mustered in Resistant territories have Martial effectively −1 for the battle in which they defend or are deployed from that territory. This is not a permanent stat change — it resolves at end of battle. Represents the fragility of press-ganged formations.

**Revolt (Accord 0):** Any garrisoned unit fights a Popular Uprising each Accounting (Military vs Ob 2, existing rule). No new Muster possible until Accord rises to 1+.

### §4.2 Prosperity → Unit Quality Gate

Territory Prosperity governs the industrial, agricultural, and population base required to sustain professional units. The Muster prerequisites table (§1.5) gates unit type by Prosperity. This is how territory quality translates to army composition without requiring a separate population stat:

- High-Prosperity territories (capitals, industrial towns) → can field Heavy Infantry, Cavalry
- Low-Prosperity territories (fjords, highland timber, border ruins) → Levy and Light Infantry only
- Territory Prosperity is already tracked on territory cards via the Govern action economy

---


## §5.1 — THREAD INTEGRATION CROSS-REFERENCES (F-02)

The military layer bridges BG units to mass battle. Mass battle §A.10 has extensive Thread integration that this bridge must preserve:

**Practitioner-general Coherence:** NPC generals who are practitioners operate under npc_behavior_v30 §4.3 Coherence AI thresholds. Coherence ≤ 5 → defensive Thread ops only. Coherence ≤ 3 → cease Thread operations. When assigning generals to units, faction AI must account for practitioner Coherence state.

**Battle MS cost:** Each battle on Valorian soil costs MS −1 (Campaign/War: −2) per peninsular_strain_v1 §3.1 and ms_budget.md. This is not a penalty — mass violence degrades the substrate (Foundations A1).

**Unit quality and Thread:** Accord (§4.1) is the population-level expression of social thread-coherence. Low Accord means the population's rendered social structures resist the governing faction — not political opposition in the conventional sense, but substrate-level misalignment between the population's thread-configuration and the faction's institutional rendering.

**Devout vs. practitioner army composition:** Church armies are always Devout (cannot use or counter Thread — mass_battle_v30 EDGE-01). Varfell armies include practitioner-generals. Crown and Hafenmark choose based on MS state and enemy Thread capability.

## §5 — OPEN EDITORIAL ITEMS

<!-- Updated 2026-04-19 PP-668 — PP-667 resolutions propagated. See designs/audit/gap_resolution_2026-04-19.md §2.2 -->

| ID | Description | Status |
|---|---|---|
| FACTION-P2-01 | Military → Power/Disc ceiling confirmed | RESOLVED |
| FACTION-P2-03 | Muster → Size=2, Power=floor(Mil/2)+1 confirmed | RESOLVED |
| ED-NEW-MIL-01 | Population modifier to initial Size (Prosperity tiers). | **RESOLVED (PP-667)** — Prosperity 1-2: Size +0 · 3-4: Size +1 · 5: Size +2. |
| ED-NEW-MIL-02 | Accord 1 → Martial −1: offence or defence? | **RESOLVED (PP-667)** — BOTH. |
| ED-NEW-MIL-03 | Experience stack ceiling. | **RESOLVED (PP-667)** — ceiling is faction Military stat (1–7). |
| ED-NEW-MIL-04 | Wealth Zero → HI/Cavalry Discipline −1/season. | **RESOLVED (PP-667)** — confirmed; supersedes "Military −1" prior rule. |
| ED-NEW-CI-01 | Conditional passive thresholds (0-1/2-4/5+). | **DEFERRED (PP-667)** to engine_v4 smoke-test. |
| ED-NEW-CI-02 | Charity Advantage Wealth differential ≥ 2. | **RESOLVED (PP-667)** — threshold = 2. |
| ED-NEW-CI-03 | PT 3 Piety Yield. | **RESOLVED (PP-667)** — raised to +0.5 (was +0.25). Integer-stable granularity. |
| BALANCE-NEW-CI-01 | CI reform pace. | **DEFERRED (PP-667)** to engine_v4 smoke-test. |
| CLOCK-EDIT-02 | Church military victory → no CI change. | **RESOLVED (PP-667)** — confirmed. CI changes only via Piety Yield / Assert / Suppress / Charity Advantage. |
