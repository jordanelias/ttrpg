<!-- SKELETON — mechanical spec only -->
<!-- Companion infill: tc_political_redesign_v30_infill.md -->
<!-- Sources: params_board_game.md, mass_battle_v30.md, victory_v30.md, geography_v30.md, faction_layer_v30.md -->
<!-- PP-TBD — awaiting patch assignment -->
<!-- Status: PROPOSAL — awaiting approval -->
<!-- Date: 2026-04-14 -->

# VALORIA — TC Political Legitimacy Redesign, Stat Economy & Card System
## v1.0

---

## §0 — AUDIT: WHAT CHANGED AND WHY

| Item | Prior state | This document |
|---|---|---|
| TC ceiling | 75 (freeze + seizure) | 100 (no freeze; Unification attempt at 100) |
| TC territory values | Contributed to 75-threshold seizure | Repurposed as Spiritual Weight (SW) — see §1 |
| TC political role | Clock only; no gameplay intersection except Church seizure | Defines Church's political pool bonus in all institutional contexts |
| TC passive | PP-402 unconditional +1 | Conditional passive per military_layer_v30 §3.2 |
| Card renewal | Not modelled in sim | Cooldown Track implemented |
| Govern effect | Mandate +1 on success (sim) | Mandate recovery (OW in capital per PP-174) + Accord maintenance |
| Battle → RS/IP | Not modelled in sim | Battle → RS −1, IP +2 per season with inter-faction battle |
| AI postures | Greedy / single-turn evaluation | Threat-aware, stat-priority ordering |

Conflicts resolved:
- ED-110 (Church TC Gain redesign): directly addressed via competitive formula in military_layer_v30 §3
- TC 75 freeze (PP-421): superseded; TC runs to 100

---

## §1 — SPIRITUAL WEIGHT: TERRITORY VALUES REPURPOSED

The TC-contribution values that previously fed the 75 → seizure threshold are repurposed as **Spiritual Weight (SW)** per territory. SW is a fixed attribute on the territory card representing its ecclesiastical importance — cathedral density, historical presence of Church, popular piety tradition.

SW is NOT the same as Piety Track (PT). PT is dynamic (changes through action). SW is fixed (set at game start). SW gates how much TC and political legitimacy can flow through a territory.

| T# | Territory | TCV | Spiritual Weight |
|---|---|---|---|
| T1 | Valorsplatz | 5 | 2 (seat of secular power; Church is present but contested) |
| T2 | Kronmark | 1 | 2 |
| T3 | Lowenskyst | 2 | 2 |
| T4 | Grauwald | 1 | 1 |
| T5 | Feldmark | 1 | 2 |
| T6 | Stillhelm | 1 | 1 |
| T7 | Rendstad | 1 | 2 |
| T8 | Gransol | 4 | 3 (trading city; strong Church commercial presence) |
| T9 | Himmelenger | 3 | 5 (cathedral city; Church's primary anchor) |
| T10 | Spartfell | 1 | 2 |
| T11 | Halvardshelm | 1 | 1 |
| T12 | Sigurdshelm | 3 | 2 |
| T13 | Oastad | 1 | 1 |
| T14 | Ehrenfeld | 2 | 3 (military stronghold with significant Church benediction tradition) |
| T15 | Askeheim | 0 | 0 (Calamity ground; Church presence impossible) |
| T16 | Schoenland | — | 1 |
| T17 | Halvarshelm | 1 | 2 |
| **Total SW** | | | **32** |

**SW use cases:**

1. **Piety Yield weighting:** TC from Piety Yield = Σ(PT tier × SW factor) per prominent territory, where SW factor = SW/5.
   - T9 (SW 5, PT 5): yield = 1.0 × (5/5) = 1.0
   - T8 (SW 3, PT 3): yield = 0.25 × (3/5) = 0.15 (negligible)
   - T14 (SW 3, PT 3 default): yield = 0.25 × (3/5) = 0.15

2. **Church political pool (§3):** Church's parliamentary/negotiation pool includes Σ(SW of Prominent territories) / 5 bonus dice.

3. **PT momentum:** PT change actions in high-SW territories have +1 die (raising or lowering PT). A high-SW territory is more religiously contested — both sides fight harder there.

---

## §2 — TC: 0-100, NO FREEZE

### §2.1 TC Runs to 100

TC no longer freezes at 75. The 75 threshold is replaced by a new milestone system:

| TC | Milestone | Effect |
|---|---|---|
| 28 | Starting value | — |
| 40 | Church Assertive | Church gains +1D on all Assert and Seizure rolls |
| 55 | Church Prominent | All factions: Ob +1 to actions directly opposing Church Domain Actions (Parliament motions targeting Church, Suppress attempts) |
| 65 | Church Dominant | Secular factions must spend an extra action slot (any card type) to pass Parliamentary motions against Church (i.e., two slots not one) |
| 80 | Church Ascendant | Seizure Ob reduced by 1 globally. All territory PT drifts +1 toward piety pole at Year-End (unless Warden Cooperation ≥ 2) |
| 100 | Theocracy Unification Attempt | See §2.2 |

The prior TC 75 Seizure protocol (Ob = 2 + Fort Level + max(0, 3 − PT)) remains active from TC 40 onward. It is no longer gated by TC 75. It is gated by Church Mandate ≥ 4 and Church Prominent in target territory (existing ED-326 condition).

### §2.2 TC 100 — Theocracy Unification Attempt

When TC reaches 100:
- TC does not continue to advance
- Church publicly declares Papal Sovereignty over the peninsula
- **Unification campaign begins:** each Accounting, Church may declare Unification Seizure on any territory (not just prominent territories), Ob = 2 + Fort Level
- Secular factions each get one free Parliamentary motion (no card slot) to oppose Church per season while Unification is active
- Unification ends (and TC drops to 75) if: Church loses 3 territories to secular counterattack in a single Year-End, OR Church Mandate drops to 3 or below (authority collapses), OR Crown Treaty forms against Church (Church as the suppressed faction)
- If Church successfully controls ≥ 10 territories while Unification is active for 2 consecutive Year-Ends: Church wins (Theocracy Unification victory)

### §2.3 Starting Value

TC starts at 28 per P-32. Unchanged.

### §2.4 Seasonal Cap

±5 TC per season from all sources combined (PP-504). ±3 from player Domain Actions specifically. Unchanged.

---

## §3 — TC AS POLITICAL LEGITIMACY

### §3.1 Design Basis: Historical Precedent

In the Italian peninsula of the 15th and 16th centuries, the Pope's political weight in civil matters was not constant — it fluctuated with the Church's demonstrated authority. When Julius II (1503–1513) was at the height of his temporal power, secular rulers needed his blessing for major acts. When the Avignon papacy (1309–1377) was seen as a tool of the French crown, papal legitimacy was widely questioned. The Church's political reach in secular governance was earned, sustained, and lost through the same mechanisms that raised and lowered the TC: piety, wealth, military presence, successful sermons, and above all, demonstrable institutional competence where the secular state was failing.

This maps directly to TC as a modifier: high TC = Church's institutional claims are credible and hard to dismiss in public forums. Low TC = Church is one voice among many.

### §3.2 TC Bonus Dice (Church in Political Forums)

When Church acts in any of the following contexts, it adds floor(TC/20) bonus dice to its roll:

| Context | Roll affected |
|---|---|
| Parliamentary motion (proposing or defending) | Mandate pool |
| Treaty positioning roll | Influence pool |
| Treaty ratification roll | Mandate pool |
| Crown Treaty targeting Church as subject | Church defensive Rebuttal roll |
| Diplomacy vs PLAYABLE faction (Senator Outward) | Influence pool |

**Examples:**
- TC 28 (start): floor(28/20) = +1D
- TC 40: +2D
- TC 60: +3D
- TC 80: +4D
- TC 100: +5D

This is a large bonus at high TC. It is by design. A Church operating at TC 80 is historically comparable to the papacy of Julius II or Innocent III — a genuinely dominant institutional force that secular rulers cannot dismiss without cost.

### §3.3 TC Obstacle Modifier (Opposing Church)

Conversely, when secular factions target Church with Parliamentary motions (Censure, Embargo, Blockade, Outlawry targeting Church as subject):

Ob of the vote threshold calculation is unchanged, but each secular faction voting against Church reduces their effective Mandate contribution by floor(TC/30):

| TC | Reduction to voting Mandate |
|---|---|
| 0–29 | 0 |
| 30–59 | −1 |
| 60–89 | −2 |
| 90+ | −3 |

This represents the political cost of being seen to oppose the Church publicly when the Church has high institutional legitimacy. Secular rulers whose populations attend church, who depend on Church welfare networks, and who need Church endorsement for legitimacy can't simply vote to Embargo the Church without consequence.

**Design note (ED-110 resolution):** This gives Church more ways to exert political power than Baralta can suppress. Baralta (TC −1/season) operates on the TC total. Church's parliamentary immunity grows with TC, meaning Hafenmark's structural suppression is a long game — it slows Church's rise but doesn't neutralise its political leverage once TC is already high.

### §3.4 Faction Political Pool (Parliamentary and Negotiation)

For all factions including Church, the working political pool in Parliamentary motions is:

**Political pool = Mandate + floor(TC/20) [Church only] + any modifiers**

For non-Church factions, the political pool in Parliament is:
**Political pool = Mandate − floor(TC/30) [if voting against Church in a motion targeting Church]**

This creates an asymmetry that mirrors historical reality: the Church's opponents pay a legitimacy cost proportional to TC; the Church gains a legitimacy bonus proportional to TC.

---

## §4 — STAT ECONOMY: INCREASE AND DECREASE RULES

### §4.1 How Stats Change

Stats change through Domain Actions and Trigger events. The seasonal cap (±2 per stat per season) governs all changes from any single source, per existing rules. Summary of canonical change paths:

**Mandate:**
| Path | Change | Source |
|---|---|---|
| Govern Overwhelming in own capital | +1 (max once/season; max = starting Mandate) | PP-174 |
| Crown Treaty Success/OW | −1 to target; Crown +1 (OW) | victory_v30 §3.1 |
| Parliamentary Censure | −1 | faction_layer_v30 §5 |
| Parliamentary Outlawry | −2 | faction_layer_v30 §5 |
| Faction collapse (Stability 0) | Not directly — collapse removes faction | — |
| Battle loss (margin −2+) | Defender Military −1 (not Mandate) | mass_battle_v30 §B.3 |
| Peninsular Strain Mandate check | Failure → −1 | Strain table |
| Seizure Failure | −1 to Church | victory_v30 §3.2 |
| Diplomatic success vs NPC | +1 (per sim convention) | params_board_game |

**Stability:** Governed exclusively by Triggers 1–5 per faction_layer_v30. Plus Accounting Stability Check (≥2 attribute loss) and Consolidation recovery (+1 clean season).

**Wealth:**
| Path | Change | Source |
|---|---|---|
| Trade Success | +1 | Standard action |
| Occupation (ongoing) | −1 per occupied territory per season | faction_layer_v30 §2 |
| Blockade active | −2/season | faction_layer_v30 §5 |
| Wealth Zero | Professional unit Discipline −1/season | military_layer_v30 §1.7 |
| Tributary | +1/year (receiver) | faction_layer_v30 §3 |

**Military:**
| Path | Change | Source |
|---|---|---|
| Battle loss (defender) | −1 | mass_battle_v30 §B.3 |
| Battle loss (attacker, margin −2+) | −1 | mass_battle_v30 §B.3 |
| Unit destroyed | No direct stat change (unit lost, not stat) | — |
| Muster (Success) | Unit created; no stat change | — |

**Influence:**
| Path | Change | Source |
|---|---|---|
| Spy/Intel Success | +1 | Standard action |
| Officer capture | +1 to captor | ED-334/335 |

### §4.2 Govern Action — Full Effect

Govern (Consul Inward) pool = Mandate, Ob = floor(Prosperity/2)+1, −1 in own capital.

| Degree | Effect |
|---|---|
| Failure | No change; Stability −1 if Prosperity was 0 in that territory (resource mismanagement) |
| Partial | Accord maintained (no drift this season); no improvement |
| Success | Accord +1 in target territory (max 3); OR Mandate recovery +1 if in capital (max starting Mandate, once/season, PP-174) |
| Overwhelming | Both: Accord +1 AND Mandate +1 in own capital (PP-174) |

**Govern is the primary stat-maintenance action.** Without Govern, Accord drifts downward under Peninsular Strain pressure, eventually triggering revolts that cost Stability. Factions that neglect Govern for military expansion find their home territories destabilising behind them — exactly the dynamic that destabilised over-extended Italian condottiere states.

### §4.3 Trade Action — Full Effect

Trade (Consul Outward) pool = Wealth, Ob = floor(Prosperity/2)+1. +1 Ob at IP≥30. +1 Ob at T2.

| Degree | Effect |
|---|---|
| Failure | No income |
| Partial | Wealth maintained (no change) |
| Success | Wealth +1 |
| Overwhelming | Wealth +2 (capped by seasonal cap of +2) |

### §4.4 Peninsular Strain Effects on Stats

Peninsular Strain (range 0–10) rises from inter-faction battles (+1/season with battle), faction eliminations (+2), revolts (+1). Decays −1 per peaceful season.

| Strain | Effect on faction stats |
|---|---|
| 0–2 | No effect |
| 3–4 | All factions: Mandate check at Accounting (Mandate pool vs Ob 1). Failure → Mandate −1 |
| 5–6 | All factions: Accord −1 in one non-capital territory (controller's choice) |
| 7–8 | All factions: Accord −1 in ALL non-capital territories. Mandate check Ob 2 |
| 9–10 | Non-capital territories: Accord cap 2. Mandate check Ob 3. RS −1/season additional |

**Battles → RS −1 per battle (missing from prior sim builds).** Each season in which at least one inter-faction battle occurred: RS −1 immediately at Accounting. Campaign/War scale: RS −2. This is canonical (params_board_game §Battle Consequences / peninsular_strain_v1.md §3).

**Battles → IP +2 per season with inter-faction battle** (also missing from prior sim builds). Each season with battle: IP +2 at Accounting.

---

## §5 — CARD SYSTEM AND RENEWAL

### §5.1 Card Hands (PP-177)

Each faction has a fixed hand of cards. Cards are spent to perform Domain Actions. Used cards are placed on the Cooldown Track.

| Faction | Hand |
|---|---|
| Crown | 2× Legionary, 1× Consul, 1× Senator, 1× Prefect, 1× Recess |
| Church | 2× Senator, 1× Pontifex, 1× Consul, 1× Legionary, 1× Recess |
| Hafenmark | 2× Consul, 1× Senator, 1× Legionary, 1× Diplomat, 1× Recess |
| Varfell | 2× Tribune, 1× Legionary, 1× Consul, 1× Colonist, 1× Recess |

**Domain Expertise** (+1D when playing this card type):
- Crown = Legionary
- Church = Senator
- Hafenmark = Consul/Prefect
- Varfell = Tribune

### §5.2 Card → Action Mapping

| Card type | Permitted actions |
|---|---|
| Legionary | Muster, March (military) |
| Consul | Govern, Trade, Fortify, Survey (domain) |
| Senator | Diplomacy, Crown Treaty, Suppress, Parliamentary Motion, Assert (Church), Parliamentary Manoeuvre (Hafenmark) |
| Pontifex | Thread operations, Assert (Church), Sacred Assembly (Templar muster) |
| Tribune | Intel, Spy, Investigate (covert) |
| Prefect | Crown Decree, tax enforcement (Crown unique) |
| Diplomat | Dynastic Proclamation, trade negotiation (Hafenmark unique) |
| Colonist | Varfell Transformation/Settlement (Varfell unique) |
| Praetor | Community Projects (RM only) |
| Recess | Pass; take no action this turn |

### §5.3 Cooldown Track and Renewal

When a card is played, it is placed on the Cooldown Track with a slot count equal to its Cooldown Duration. At each Accounting (Phase 5 Step 3): all items on the Cooldown Track −1 slot. At 0 slots: card returns to hand and is immediately available.

| Card type | Cooldown Duration (seasons) |
|---|---|
| Legionary | 1 |
| Consul | 1 |
| Senator | 1 |
| Pontifex | 2 (Thread work is demanding) |
| Tribune | 1 |
| Prefect | 2 |
| Diplomat | 1 |
| Colonist | 2 |
| Recess | 0 (returns immediately; using Recess costs nothing) |

**Implication:** Most cards are available every other season. A faction with 1 Consul card can Govern or Trade once, then must wait one season before doing so again. This is the core action economy constraint: you can't do everything every season. The Recess card (always available) represents strategic patience — sometimes the right move is to do nothing and let others exhaust themselves.

**Crown's 2× Legionary advantage:** Crown can conduct military action two seasons in a row before both Legionary cards are on cooldown. This reflects Crown's larger standing army and military bureaucracy.

**Church's 2× Senator advantage:** Church can conduct social/diplomatic/TC actions two seasons in a row. Assert, Suppress, Diplomacy, Parliamentary actions — Church has more political bandwidth than any other faction.

---

## §6 — AI POSTURE REDESIGN

### §6.1 Posture Priority Framework

Replace pure EXPAND/CONSOLIDATE/DEFEND/DIPLOMACY with a threat-first priority stack. Each season, factions evaluate threats in order and act on the first one that applies:

**Priority 1 — EXISTENTIAL (Stability ≤ 1 or territory count = 1):**
Spend all available actions on: Govern (Mandate recovery), Trade (Wealth recovery), Recess if neither card available. Do not use military. Do not attack. Survive.

**Priority 2 — DEFEND (enemy unit adjacent to own ungarrisoned territory):**
Muster new unit in the threatened territory. If can't Muster this season (no Legionary card), use Recess to conserve. Do not expand.

**Priority 3 — CONSOLIDATE (Stability ≤ 2 OR Wealth ≤ 1 OR Mandate ≤ 2):**
Govern + Trade. No military expansion. Mandate recovery is the target; Wealth maintenance prevents unit degradation.

**Priority 4 — COUNTER-THREAT (TC ≥ 55 AND faction is HF or Crown):**
Hafenmark: Suppress is mandatory Priority-4 action every season when available. Crown: pursue Crown Treaty if Mandate ≥ 4 and TCV ≥ 10.

**Priority 5 — EXPAND (all Priority 1-4 conditions clear):**
Military expansion if border units available. Seizure (Church). Intel operation (Varfell).

**Priority 6 — OPPORTUNISTIC (no clear priority):**
Govern in capital (Mandate recovery), Trade (Wealth building).

### §6.2 Faction-Specific Priorities

**Crown:**
- Must maintain Mandate ≥ 4 to be a viable Crown Treaty user. Govern (capital) is always Priority if Mandate < 4.
- Crown Treaty targets: PLAYABLE factions only, Mandate ≥ 2. Prefer faction with lowest TCV (easiest to suppress).
- Military: defend T1, T14, T2, T3 (core territories). Only expand when those four are garrisoned.
- PI awareness: if PI ≥ 10, Crown should prioritise Parliamentary actions over military.

**Hafenmark:**
- Suppress = highest non-existential priority at TC ≥ 40. Church's Mandate rising means HF's structural suppression (Baralta) is insufficient alone — active Suppress is critical.
- Consul cards: Trade when Wealth < 4, Govern when Mandate < 4 or Accord at risk.
- Military: defensive only. T8 and T10 must remain garrisoned. T7 is expendable.
- Parliamentary Manoeuvre: use whenever PI ≥ 5 to rebuild PI (HF victory needs PI ≥ 5 which is the starting value — they need to prevent PI from falling).

**Church:**
- Assert when TC < 60 and Legionary cards unavailable (Senator cards used for Assert).
- Church Seizure when TC ≥ 40 and prominent territories have PT ≥ 3.
- Govern in T9 to maintain Accord 3 (Aligned) — highest PT territory is most valuable.
- Military (Templar): position Templar units in PT ≥ 3 territories for TC bonus.

**Varfell:**
- Intel ops against Crown (highest Mandate rival) — information is Varfell's tool.
- Govern internally when Mandate/Stability threatened.
- Military expansion only when VTM ≥ 2 (Warden path) or territory count ≤ 3 (recovery from losses).

---

## §7 — AUDIT OF ALL CHANGES AGAINST EXISTING MECHANICS

### §7.1 TC Cap vs New Milestones

Old cap: ±5/season (PP-504). Still applies.
New ceiling: 100 (replacing 75 freeze). No conflict — seasonal cap prevents runaway.
New milestones at 40/55/65/80/100 add effects but don't change TC formula.

**Check:** Prior victory_v30 §3.2 Church victory requires TC ≥ 65. With TC running to 100, this threshold remains as a Church win condition sub-requirement; the TC Unification at 100 is an additional/alternate path.
**Flag (ED-NEW-TC-10):** Confirm whether Church victory condition at TC 65 + TCV ≥ 8 remains as-is or is replaced by TC 100 Unification only.

### §7.2 Political Pool vs Mandate Pool

Existing: Parliament votes by Mandate (§5.3 faction_layer_v30).
New: Church gets floor(TC/20) bonus dice; opposing factions get −floor(TC/30) voting Mandate.
**No conflict:** These are additive modifiers to the Mandate pool, not replacements.

**Check:** At TC 100, Church bonus = +5D; opposing Mandate reduction = −3/faction.
Crown (Mandate 5) voting against Church: effective votes = 5−3 = 2. Church (Mandate 5 + 5 bonus = 10D, against Ob 2) has overwhelming Parliament dominance.
This is by design — TC 100 represents a Church that has politically dominated the peninsula. Secular factions should have acted to prevent this.

### §7.3 Territory SW vs TCV

TCV is unchanged (existing victory condition calculation). SW is a new attribute. No conflict.
TCV used for: victory threshold checks, occupation TCV zeroing.
SW used for: Church political pool, Piety Yield weighting, PT momentum.

### §7.4 Govern Full Effect vs PP-174

PP-174 (Govern OW in own capital: Mandate +1) is retained.
New: Govern Success in any territory = Accord +1. Govern OW in capital = Mandate +1 AND Accord +1.
No conflict — PP-174 specifies OW in capital; we add the Success-in-any-territory Accord effect.

### §7.5 Battle → RS and IP

New: Battle → RS −1 per season with battle; IP +2.
Check against existing: RS baseline decay is −1/year-end (annual). Battle RS damage is separate and immediate. No conflict — both apply.
Check against IP: existing IP +1 from Torben Loyalty ≤ 3. Battle IP +2 is additional. No conflict.

### §7.6 Seizure Changes (TC milestone vs old TC 75 gate)

Old: Seizure gated by TC ≥ 75 (now removed as a gate).
New: Seizure available from TC ≥ 40 (milestone). Existing Seizure Ob formula unchanged.
**Check victory_v30 §7 (TC 75 Seizure protocol):** The prior seizure at TC 75 used "Ob = 2 + Fort Level + max(0, 3 − PT)". With TC running past 75, this Ob formula still applies at TC 40+. The TC 80 milestone reduces Seizure Ob by 1 globally (stacks with formula).
**Flag (ED-NEW-TC-11):** Confirm Seizure Ob formula: is it still 2+Fort+max(0,3−PT) or does it use the updated Ob = 7−PT formula from the Church victory redesign?

### §7.7 Accord Degradation in Sim

Accord was not modelled in prior sim. Now required for Peninsular Strain → stat impacts.
Starting Accord: capitals = 3, all other home territories = 2. Per params_board_game.
Accord degradation triggers: Accord 1 without garrison → 0 at Accounting; Peninsular Strain effects.
Accord recovery: Govern action (Success → +1, max 3).

### §7.8 BG Mode vs TTRPG Mode Applicability

All §1-6 mechanics apply to BG and Hybrid modes.
TTRPG mode: TC political legitimacy bonus (§3) applies when Church acts in social contests or domain scenes. Floor(TC/20) bonus dice on relevant Influence/Mandate rolls.
No conflict with scale_transitions_v30 §3 (Domain Echo handles TTRPG → faction layer translation).
