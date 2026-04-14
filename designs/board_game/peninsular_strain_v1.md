# VALORIA BG — Peninsular Strain System v1
## Status: DESIGN — proposal for integration into victory_v30.md
## Date: 2026-04-14
## Supersedes: victory_v30.md §1 TCV table (partial — TCV revaluation), victory_v30.md §3 (faction-specific victory conditions replaced by universal condition), victory_v30.md §4 (co-victory restructured), victory_v30.md §5 (shared loss retained with modifications)
## Dependencies: geography_v30.md (territory numbering), params_board_game.md (card-hand PP-177, faction stats, Prosperity per territory, Diplomatic Token PP-517/521, Standing PP-515, Institutional Mandate PP-189), victory_v30.md §2 (PT track retained), victory_v30.md §6 (Askeheim/RS retained), victory_v30.md §7 (TC generation retained), victory_v30.md §9 (Hybrid integration retained)
## Propagation required: victory_v30.md, params_board_game.md, geography_v30.md (TCV only)

---

## Design Principle

Every faction shares the same victory condition: sovereign control of the peninsula. Asymmetry is in the tools each faction uses to get there, not in the destination. Military conquest is always available but structurally expensive — four interlocking pressures ensure that governance, institutional authority, and cultural legitimacy are faster paths than violence.

The peninsula is 35 years post-secession. The population has living memory of the independence war. Military conquest across the peninsula recreates the Altonian pattern of domination; the population resists it.

---

## §1 Territory Consolidation Values (TCV) — Revised

Himmelenger revalued to 5 (Cathedral City, 5 adjacencies, site of Cultural Uprising, focal point of TC/PT mechanics). Gransol revalued to 3 (Hafenmark's power is parliamentary/institutional, not territorial primacy).

| T# | Territory | TCV | Controller |
|----|-----------|-----|------------|
| T1 | Valorsplatz | 5 | Crown★ |
| T9 | Himmelenger | 5 | Church★ |
| T8 | Gransol | 3 | Hafenmark★ |
| T12 | Sigurdshelm | 3 | Varfell★ |
| T3 | Lowenskyst | 2 | Crown |
| T14 | Ehrenfeld | 2 | Crown |
| T10 | Spartfell | 1 | Hafenmark |
| T7 | Rendstad | 1 | Hafenmark |
| T17 | Halvarshelm | 1 | Hafenmark |
| T2 | Kronmark | 1 | Crown |
| T5 | Feldmark | 1 | Crown |
| T6 | Stillhelm | 1 | Crown |
| T13 | Oastad | 1 | Varfell |
| T11 | Halvardshelm | 1 | Varfell |
| T4 | Grauwald | 1 | Varfell |
| T15 | Askeheim | 0 | Uncontrolled |
| T16 | Schoenland | — | Not in territorial play |
| | **Total** | **31** | |

**Starting TCV:** Crown 12, Hafenmark 6, Church 5, Varfell 6.

---

## §2 Accord (Per-Territory Attribute) — NEW

Accord represents the population's acceptance of the current controller's governance. It modifies the territory's effective Prosperity.

**Range:** 0–3 (dial or marker on territory card, alongside Fort and PT).

**Effective Prosperity:** A territory's base Prosperity (from params_board_game.md territory table) is modified by Accord.

| Accord | Name | Effective Prosperity | Other Effects |
|--------|------|---------------------|---------------|
| 3 | Aligned | Base Prosperity (full) | Defender +1D in Battle. |
| 2 | Compliant | Base Prosperity (full) | Normal operations. |
| 1 | Resistant | 0 (no Prosperity contribution) | Govern Ob +1. Garrison required (≥ 1 military unit) or Accord → 0 at Accounting. |
| 0 | Revolt | Territory becomes Uncontrolled at Accounting | Garrison (if present) fights Popular Uprising: Military vs Ob 2. Win: territory held, Accord → 1. Loss: garrison retreats to adjacent friendly territory. |

**Note on Govern/Trade Ob interaction:** Govern Ob and Trade Ob use base Prosperity (unchanged by Accord). Accord 1 adds +1 Ob to Govern in that territory. This means governing resistant territory is harder (higher Ob) AND less rewarding (no Prosperity contribution).

**Accord and TCV:** A territory's TCV counts toward your total only if Accord ≥ 2. Territories at Accord 1 are nominally yours but do not contribute to sovereignty. At Accord 0 the territory is lost entirely.

### §2.1 Starting Accord

| Territory | Controller | Accord | Rationale |
|-----------|-----------|--------|-----------|
| T1 Valorsplatz | Crown★ | 3 | Royal capital |
| T2 Kronmark | Crown | 2 | Heartland |
| T3 Lowenskyst | Crown | 2 | Border fortress |
| T5 Feldmark | Crown | 2 | Breadbasket |
| T6 Stillhelm | Crown | 2 | Southern farmland |
| T14 Ehrenfeld | Crown | 2 | Military hinge |
| T8 Gransol | Hafenmark★ | 3 | Hafenmark capital |
| T7 Rendstad | Hafenmark | 2 | Timber valley |
| T10 Spartfell | Hafenmark | 2 | Border castle |
| T17 Halvarshelm | Hafenmark | 2 | Northern mines |
| T9 Himmelenger | Church★ | 3 | Cathedral city |
| T12 Sigurdshelm | Varfell★ | 3 | Varfell seat |
| T13 Oastad | Varfell | 2 | Southern fjords |
| T11 Halvardshelm | Varfell | 2 | Central fjords |
| T4 Grauwald | Varfell | 2 | Highland territory |
| T15 Askeheim | Uncontrolled | — | No Accord (no settled population centre) |
| T16 Schoenland | Schoenland | — | Not in territorial play |

### §2.2 Starting Piety Track (PT) Values — NEW

| T# | Territory | Starting PT | Rationale |
|----|-----------|-------------|-----------|
| T1 | Valorsplatz | 3 | Capital, moderate piety, diverse population |
| T2 | Kronmark | 3 | Crown heartland, orthodox but not zealous |
| T3 | Lowenskyst | 3 | Border fortress, practical piety |
| T4 | Grauwald | 2 | Highland, old Einhir traditions persist |
| T5 | Feldmark | 3 | Agricultural, conventional faith |
| T6 | Stillhelm | 1 | Southern, Calamity proximity erodes orthodox faith |
| T7 | Rendstad | 3 | Timber valley, conventional |
| T8 | Gransol | 3 | Hafenmark capital, Baralta is devout but parliamentary culture moderates |
| T9 | Himmelenger | 5 | Cathedral city, spiritual centre (existing canonical value) |
| T10 | Spartfell | 3 | Border castle, practical |
| T11 | Halvardshelm | 2 | Central fjords, old Einhir ways |
| T12 | Sigurdshelm | 2 | Varfell seat, Restoration-sympathetic |
| T13 | Oastad | 1 | Southern fjords, Calamity proximity, Restoration stronghold |
| T14 | Ehrenfeld | 3 | Military hinge, institutional piety |
| T15 | Askeheim | 0 | Hard-fixed (existing canonical value) |
| T16 | Schoenland | — | Not in territorial play |
| T17 | Halvarshelm | 3 | Northern mines, conventional |

### §2.3 Accord Changes — Gaining

| Method | Accord Change | Notes |
|--------|--------------|-------|
| Govern (Consul Inward), Success | +1 | Cap: Accord 3. |
| Govern (Consul Inward), Overwhelming | +1, removes garrison requirement for 1 season if territory was Accord 1 | Decisive governance calms resistance. |
| 2 consecutive seasons: no hostile action in territory, garrison present | +1 | Passive normalisation. Cap: Accord 2 (Accord 3 requires active Govern). |
| Church Seizure, Success | Accord set to max(floor(PT/2) + 1, 2) | Guarantees ≥ 2. Political act backed by institutional authority. |
| Church Seizure, Overwhelming | Accord set to floor(PT/2) + 2, max 3 | Strong institutional mandate. |
| Dynastic Proclamation (Hafenmark), Success or Overwhelming | Accord set to 2 | Diplomatic transfer with dynastic legitimacy. |
| Cultural Reformation (Varfell), Success or Overwhelming | Accord set to 2 | Cultural alignment with population. |
| Crown Treaty — diplomatic transfer | Accord set to 2 | Legitimacy inherited from prior ruler. |
| Territory transfer via Co-Victory partition | Accord set to 2 | Negotiated handover. |

### §2.4 Accord Changes — Losing

| Trigger | Accord Change | Notes |
|---------|--------------|-------|
| Military conquest (March + win Battle) | Accord set to 1 | Regardless of prior value. |
| Battle in a territory you control (you are defender) | −1 | War came to their home. |
| Church Seizure, Partial | Accord set to 1 | Contested seizure, politically messy. |
| Controller's Stability drops to ≤ 2 | −1 in all territories controlled by that faction | Destabilised faction loses trust. One-time per Stability-drop event. |
| Faction that conquered by force loses Battle elsewhere | −1 in all force-conquered territories held by that faction | Military weakness emboldens resistance. |
| Peninsular Strain threshold effects | See §4 | Global war-weariness erosion. |

### §2.5 Accord — Restoration Movement Exception

RM does not use Accord. RM controls T9 (if taken via Cultural Uprising) through cultural presence, not governance. RM-held T9 control is maintained while RM has ≥ 3 Presence markers in T9 AND PT ≤ 1 (existing rule from victory_v30.md §3.5). RM has no Stability, Mandate, or Military — Accord triggers do not apply.

### §2.6 Accord — Löwenritter Adaptation

Löwenritter uses Accord but gains access to **Martial Governance**: a Govern variant using Military as pool instead of Influence. Accord +1 on Success, same as standard Govern. Ob = floor(Prosperity/2) + 2 (harder than civil governance). Löwenritter cannot exceed Accord 2 via Martial Governance (cap); reaching Accord 3 requires standard Govern with Influence pool.

---

## §3 Battle Consequences — NEW

Automatic consequences firing when Battle is resolved on Valorian soil. Not optional. Not faction-specific.

### §3.1 Substrate Fracture (Pressure 1)

Each Battle resolved on Valorian soil: **RS −1.**

| Battle type | RS cost | Rationale |
|------------|---------|-----------|
| Standard Battle (Legionary contested entry) | −1 | Mass violence degrades the Rendering. |
| Mass Battle (Campaign/War scale per mass_battle_v30.md §A.3) | −2 | Larger scale violence, greater substrate damage. |
| Siege (Fort ≥ 2 defended) | −1 | Concentrated but geographically contained. |
| Church Seizure requiring Battle (garrisoned territory) | −1 | The Battle component triggers RS cost; Seizure itself does not. |
| Popular Uprising (Accord 0 → Revolt) | −1 | Violence is violence; the substrate does not distinguish. |
| Altonian Vanguard Battle | −1 | Foreign invasion also damages the substrate. |
| Covert action (Tribune Investigate, Spy) | 0 | Not mass-violence events. |
| Church Seizure, ungarrisoned territory | 0 | Political act, no violence. |

### §3.2 Vulnerability Signal (Pressure 2)

Each season in which a Battle between playable factions is resolved: **IP +2.**

Altonia monitors the peninsula for weakness. Civil war signals vulnerability. This fires once per season regardless of how many battles occur (one season of warfare = one intelligence signal). Battles against NPC factions (Altonian Vanguard, Popular Uprising, Löwenritter coup) do NOT trigger IP advancement — Altonia does not gain intelligence from its own operations, and internal unrest is a different signal from inter-faction civil war.

**IP advancement from civil war is independent of Peninsular Strain (§4).** The two tracks do not feed each other.

---

## §4 Peninsular Strain Counter — NEW

Global track, range 0–10. Starts at 0. Public (visible counter on board).

### §4.1 Advancing Strain

| Trigger | Strain Change |
|---------|--------------|
| Season in which a Battle between playable factions is resolved | +1 |
| Playable faction eliminated (Stability 0) | +2 |
| Territory Revolt (Accord 0 → Uncontrolled) | +1 |

### §4.2 Reducing Strain

| Trigger | Strain Change |
|---------|--------------|
| Season with NO inter-faction battles AND no Revolts | −1 (min 0) |
| Public diplomatic resolution (Crown Treaty formed, Open Pledge honoured, Co-Victory declared) | −1 (max one from this source per season) |

### §4.3 Strain Threshold Effects

| Strain | Name | Effect |
|--------|------|--------|
| 0–2 | Peace | No effect. |
| 3–4 | Tension | All factions: Mandate check at Accounting (Mandate pool vs Ob 1). Failure: Mandate −1. |
| 5–6 | Fracture | All factions: Accord −1 in one territory (lowest-Accord first, controller's choice among ties). |
| 7–8 | Crisis | All factions: Accord −1 in ALL non-capital territories. Mandate check Ob 2 at Accounting. |
| 9–10 | Collapse | Non-capital territories: Accord cap at 2. Mandate check Ob 3. RS −1/season additional. |

**Löwenritter Strain exemption:** Löwenritter emergence (coup) adds Strain +1 (not +2 — the coup is a succession event, not faction elimination). Battles in the first 2 seasons after Löwenritter activation do not advance Strain (the population expects military governance during succession crisis). After 2 seasons: normal Strain rules apply.

### §4.4 Strain and IP — No Cross-Feeding

Strain and IP are independent tracks. Strain effects at Fracture/Crisis/Collapse do NOT add IP. IP advances from its own triggers (Altonian pressure table, TC > 60, civil war battles per §3.2). Both may advance from the same battle event but through separate rules.

---

## §5 Faction Toolkits — Non-Military Territory Acquisition

Each faction has a non-military domain action for acquiring territory that produces Accord ≥ 2. These are categorically better than military conquest (Accord 1) for legitimacy purposes and do not trigger RS/IP costs (unless Battle is required for garrisoned territories).

### §5.1 Crown — Formal Crown Treaty (Existing)

See victory_v30.md §3.1 for full Treaty mechanics (PP-512/513/514/523).

**Card type:** Senator Outward (Crown only).
**Ob:** floor(target Mandate / 2) + 1, min 1.
**Pool:** Influence.

Crown Treaty subordinates rival factions diplomatically. Treaty-bound factions count toward Crown's effective hegemony for the universal victory condition. Territories held by Treaty-bound factions are counted as Crown-controlled for sovereignty purposes.

**Accord on diplomatic transfer:** If a Treaty-bound faction cedes a territory to Crown as part of Treaty terms (negotiated between players or via NPC consent rules), that territory starts at Accord 2.

**Defensive interaction with Institutional Mandate (PP-189):** Target faction may Appease (Mandate −1, Treaty cancelled) if Mandate ≥ 4. This is the existing defensive mechanic.

### §5.2 Church — Graduated Seizure (Existing, Accord Formula Revised)

See victory_v30.md §3.2 for full Seizure mechanics (PP-494).

**Card type:** Special/Unique Power (Priority 6).
**Pool:** Influence + floor(TC / 15).
**Ob:** 7 − PT.
**Prerequisites:** Church Mandate ≥ 4. Prominence (Church Mandate > controlling faction Mandate).

**Revised Accord on Seizure:**

| Degree | Accord | Formula |
|--------|--------|---------|
| Overwhelming | floor(PT/2) + 2, max 3 | High institutional authority. PT 5 → Accord 3. PT 3 → Accord 3. PT 1 → Accord 2. |
| Success | max(floor(PT/2) + 1, 2) | Guaranteed ≥ 2. PT 5 → Accord 3. PT 3 → Accord 2. PT 1 → Accord 2. |
| Partial | 1 | Politically messy. Contested seizure fails to establish authority. |
| Failure | N/A | Seizure fails. Stability −1. |

**Defensive interaction:** Controlling faction gains Casus Belli on every seizure attempt (PP-510, existing rule). Institutional Mandate (PP-189) applies — controlling faction may Appease to cancel Seizure before roll.

**Fort interaction:** Unchanged (PP-506). Fort does NOT modify Seizure Ob. If garrisoned: Battle required first (existing rule). The Battle triggers RS −1 per §3.1.

### §5.3 Hafenmark — Dynastic Proclamation — NEW

Baralta's divine-right claim. "Faith is not mediated — it is lived. Anyone who is truly faithful can hear Solmund. Anyone who cannot should not rule."

**Card type:** Diplomat (Hafenmark faction card). Once per season.
**Pool:** Influence.
**Ob:** floor(target faction Stability / 2) + 1. Modifiers: if target territory PT ≤ 1: +1 Ob (Restoration-leaning population resists divine-right authority). If Hafenmark has active Diplomatic Token on target faction mat: −1 Ob (existing diplomatic leverage).
**Prerequisites:** Hafenmark Mandate ≥ 4 AND Hafenmark Mandate > target territory controlling faction's Mandate. Target territory must be adjacent to Hafenmark-controlled territory.

| Degree | Effect |
|--------|--------|
| Overwhelming | Territory control transfers. Accord set to 2. Target faction Mandate −1. Hafenmark Mandate +1 (momentum of divine right). No Casus Belli (legitimate succession claim). +1 Standing (PP-515: the claim was publicly made and upheld). |
| Success | Territory control transfers. Accord set to 2. Target faction Mandate −1. |
| Partial | Territory does not transfer. Hafenmark gains Casus Belli vs target (rejected claim = justification for force). Target territory Accord −1 (population destabilised by competing claims). |
| Failure | Hafenmark Stability −1 (overreach). No Casus Belli. |

**Diplomatic Token interaction (PP-517/521):** If Hafenmark has Diplomatic Token on target faction AND uses Proclamation: Token provides −1 Ob (above). On Overwhelming Proclamation: Token is NOT consumed (unlike military conflict, which removes Tokens). On Partial/Failure: Token remains. Token is consumed only if Hafenmark subsequently uses military force against that faction (existing PP-517 rule).

**Standing interaction (PP-515):** Proclamation may be declared as an Open Pledge in Phase 1 ("I will assert my divine right over [territory] this season"). Honour: +1 Standing. Breach (failing to play Diplomat card for Proclamation): Stability −1 + Casus Belli per PP-515 rules.

**Defensive interaction:** Target faction may invoke Institutional Mandate (PP-189) if Mandate ≥ 4 (Appease: Mandate −1, Proclamation cancelled). Target faction may also contest via Parliamentary Session (Hafenmark's Proclamation is a constitutional claim — Parliament has standing to adjudicate). If Parliamentary Session vote opposes Proclamation: +1 Ob to Proclamation this season.

**Why Diplomat card, not Senator:** Hafenmark has 1× Senator and 1× Diplomat. Diplomat is Hafenmark's unique card. Proclamation is Hafenmark's unique acquisition tool. Using Diplomat preserves Senator for Diplomacy and Parliamentary Manoeuvre. The Diplomat card's existing function (place Diplomatic Tokens) creates a natural two-phase strategy: first deploy Diplomatic Tokens (build leverage), then Proclaim (use leverage for territorial acquisition).

### §5.4 Varfell — Cultural Reformation — NEW

Vaynard's revolutionary program: shatter the caste system, expel Altonian influence, remove Church from political life.

**Card type:** Colonist. Once per season.
**Pool:** Influence + floor(VTM / 2).
**Ob:** PT + 1 (target territory). Low-PT territories are easier (population already leans Restoration). High-PT territories resist cultural reformation. PT 0 → Ob 1. PT 3 → Ob 4. PT 5 → Ob 6.
**Prerequisites:** VTM ≥ 2. Target territory PT ≤ 3 (population must have some openness to Restoration ideas). Target territory adjacent to Varfell-controlled territory OR territory where Varfell has intelligence presence (Tribune operation successfully completed there within 2 seasons).

| Degree | Effect |
|--------|--------|
| Overwhelming | Territory control transfers. Accord set to 2. PT −1 in target territory. TC −1 (Church institutional grip weakens). |
| Success | Territory control transfers. Accord set to 2. PT −1 in target territory. |
| Partial | Territory does not transfer. PT −1 in target territory (cultural seed planted). Varfell gains intelligence presence in territory if not already present. |
| Failure | Varfell Stability −1. TC +1 (Church reaction). Church Attention Pool +1. |

**Why Ob = PT + 1:** This makes Varfell's expansion tool inversely correlated with Church's. As PT drops (through Calamity Drift, RM activity, or Varfell's own Partial results planting seeds), Varfell's Reformation becomes easier. As PT rises (through Church cultivation), it becomes harder. Varfell can directly influence PT through Tribune intelligence operations, Counter-Narrative (existing action targeting Church-Prominent territories), and by succeeding at Reformation (each success lowers PT further). This creates a feedback loop: success → lower PT → easier future success — but only in the low-PT band.

**Why Colonist card:** Varfell has 1× Colonist in starting hand. Colonist is thematically coherent — Cultural Reformation IS cultural colonisation. Using Colonist preserves Tribune for intelligence operations (Investigate, Spy) and avoids forcing Varfell to choose between intelligence and expansion on the same card type.

**Defensive interaction:** Target faction may invoke Institutional Mandate (PP-189) if Mandate ≥ 4. Church may invoke Counter-Reformation (new): if Church is Prominent in the target territory AND plays a Senator card targeting that territory in the same Phase 4, Church adds +1 Ob to Reformation. Costs Church one card play.

**Open Pledge interaction (PP-515):** Reformation may be declared as Open Pledge ("I will culturally reform [territory] this season"). Honour: +1 Standing. Breach: standard PP-515 consequences.

**Anti-Altonian effect:** Territories gained via Cultural Reformation: Altonian intelligence operations (espionage, proxy actions) face +1 Ob. The population has been culturally inoculated against foreign influence. (Does not apply to territories gained by military conquest.)

---

## §6 Universal Victory Condition — Peninsular Sovereignty

All factions share the same victory condition. Available in all modes (BG, Hybrid).

### §6.1 Peninsular Sovereignty (Primary)

All conditions simultaneous at Accounting, held for 2 consecutive Accountings:

| Condition | Threshold |
|-----------|-----------|
| Territory control | All 15 playable territories (T1–T14, T17) — directly or via effective hegemony |
| Accord | ≥ 2 in all directly-controlled territories |
| Peninsular Strain | ≤ 6 (peninsula not in Crisis) |

**Effective hegemony** counts rival-held territories toward sovereignty if the rival faction is:
- Treaty-bound (Crown Treaty or equivalent bilateral agreement), OR
- Submitted (Stability 0, formal submission per ED-318), OR
- Institutionally dominated (rival Mandate ≤ 1 AND hegemon Mandate ≥ 5)

Territories held by Treaty-bound or Submitted factions do not need to meet Accord ≥ 2 for the hegemon — the legitimacy question belongs to the subordinate.

### §6.2 Faction-Specific Victory Conditions — RETAINED as Alternate Paths

The existing faction-specific conditions from victory_v30.md §3 are retained as alternate victory paths, representing each faction's ideological endpoint rather than total peninsular control.

- Crown Peninsula Sovereignty (TCV ≥ 14, suppress 2 of 3 rivals, IP < 60, PI ≥ 3)
- Church Solmundan Orthodoxy (TCV ≥ 8, PT ≥ 3 in all held territories)
- Hafenmark Dynastic Assertion (TCV ≥ 12, Crown Mandate ≤ 1, hold T1, Hafenmark Mandate ≥ 5, Torben Loyalty ≤ 3)
- Varfell three paths (A/B/C retained as-is)
- RM Cultural Revolution (Hybrid only, retained as-is)
- Löwenritter Regency / Military Consolidation (retained as-is)

These are EASIER than full Peninsular Sovereignty and represent shorter-game victories. Peninsular Sovereignty is the prestige win. Faction-specific victories are the standard wins.

**Note:** Hafenmark Parliamentary Sovereignty is replaced by Dynastic Assertion as the primary path (per faction identity discussion). Parliamentary Sovereignty is struck.

### §6.3 Co-Victory: Peninsular Partition

Available when playing with 2+ human players. Two factions agree to divide the peninsula.

All conditions simultaneous at Accounting, held for 2 consecutive Accountings:

| Condition | Threshold |
|-----------|-----------|
| Collective territory control | Both factions collectively control all 15 playable territories — directly or via effective hegemony over remaining factions |
| Individual minimum | Each faction controls territories with TCV ≥ 10 |
| Accord | ≥ 2 in all territories controlled by each faction |
| Non-aggression | No Battle between the two factions in preceding 4 seasons |
| Peninsular Strain | ≤ 6 |
| Institutional standing | Both factions Mandate ≥ 3 |

**Partition declaration:** Both players formally declare Partition at the same Accounting.

**Incompatible pairings:** Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM (structurally contradictory programs).

Existing co-victory pairings from victory_v30.md §4 are retained as alternate co-victories with their existing (lower) thresholds, alongside the new Partition option.

### §6.4 Shared Loss Conditions

| Condition | Trigger | Outcome |
|-----------|---------|---------|
| Rendering Stability Rupture | RS = 0 at Accounting | All factions lose. Second Calamity. |
| Altonian Conquest | IP ≥ 100 AND AER ≤ 1 at Accounting | Altonia annexes Valoria. All factions lose. |

Total Institutional Collapse (all factions Stability 0) is subsumed — if all factions are eliminated, the outcome is determined by whichever shared loss condition fires first (RS Rupture or Altonian Conquest) or anarchy (all territories Uncontrolled, no governance).

---

## §7 Accounting Integration

New steps to add to Phase 5 Seasonal Accounting (params_board_game.md):

Insert after existing Step 4 (Clock advances):

**Step 4c — Accord checks:**
1. Each territory at Accord 1: if no garrison present (no military unit from controlling faction), Accord → 0.
2. Each territory at Accord 0: Revolt fires. Garrison fights Popular Uprising (Military vs Ob 2) or retreats. Territory becomes Uncontrolled. Peninsular Strain +1.
3. Passive normalisation: each territory with garrison present AND no hostile action this season for 2 consecutive seasons: Accord +1 (cap Accord 2).

**Step 4d — Peninsular Strain update:**
1. If no inter-faction battles AND no Revolts this season: Strain −1 (min 0).
2. If diplomatic resolution occurred (Treaty, Pledge honoured): Strain −1 (max one from this source).
3. Apply Strain threshold effects per §4.3.

**Step 4e — Battle consequence accounting:**
1. If Battle between playable factions occurred this season: IP +2 (§3.2).
2. RS adjustments from battles already applied during Phase 4 resolution (immediate, not deferred to Accounting).

Modify existing Step 12 (Victory condition check): Check universal Peninsular Sovereignty condition (§6.1) alongside existing faction-specific conditions (§6.2). Either type of victory is valid. Co-Victory (§6.3) checked simultaneously.

---

## §8 Open Items

| # | Item | Status |
|---|------|--------|
| 1 | Starting PT values (§2.2): proposed, requires user review before canonical. | PROVISIONAL |
| 2 | Hafenmark Parliamentary Sovereignty → struck, replaced by Dynastic Assertion as primary. Confirm. | AWAITING USER |
| 3 | Church Counter-Reformation defensive action (§5.4): new mechanic, needs formal PP. | NEEDS SPEC |
| 4 | Varfell Colonist card availability: confirm Varfell starting hand includes 1× Colonist. | CONFIRMED (params_board_game.md) |
| 5 | Accord physical component: dial on territory card vs separate marker. Production decision. | DEFERRED |
| 6 | NPC AI priority trees (npc_behavior_v30.md): need Accord-aware updates. NPC factions must factor Accord into Govern decisions. | PROPAGATION NEEDED |
| 7 | Hybrid mode: Accord changes from Zoom In personal scenes queue as Domain Echoes (±1 Accord max per Zoom In), consistent with PT transfer rules (victory_v30.md §9.1). | NEEDS SPEC |

---

## §9 Propagation Checklist

| Target File | Change Required | Priority |
|-------------|----------------|----------|
| victory_v30.md §1 | TCV revaluation (Himmelenger 5, Gransol 3, total 31) | P1 |
| victory_v30.md §3 | Add universal victory condition (§6.1) as primary. Retain faction-specific as alternates. Strike Hafenmark Parliamentary Sovereignty. | P1 |
| victory_v30.md §4 | Add Partition co-victory (§6.3). Retain existing pairings as alternates. | P1 |
| victory_v30.md §10 | Update win probability assessment for revised TCV and universal condition. | P2 |
| params_board_game.md §Starting Values | Add: Accord per territory (§2.1), Starting PT (§2.2), Peninsular Strain (start 0, range 0–10). | P1 |
| params_board_game.md §Clock Environmental Effects | Add: Peninsular Strain threshold table (§4.3). | P1 |
| params_board_game.md §Accounting | Add steps 4c/4d/4e per §7. | P1 |
| params_board_game.md §Faction Actions | Add: Dynastic Proclamation (§5.3), Cultural Reformation (§5.4). | P1 |
| params_board_game.md §Starting TCV | Update Crown 12, Hafenmark 6, Church 5, Varfell 6. | P1 |
| geography_v30.md | No change needed (TCV is in victory_v30.md, not geography). | — |
| npc_behavior_v30.md | Update NPC priority trees for Accord-aware governance. | P2 |
| designs/hybrid/scale_transitions_v30.md §9 | Add Accord Domain Echo rules for Zoom In/Out. | P2 |

---

## §10 Patch Register Entries

| PP | Scope | Description |
|----|-------|-------------|
| PP-NEW-01 | TCV | Himmelenger TCV 3 → 5. Gransol TCV 4 → 3. Total TCV 30 → 31. Starting: Crown 12, Hafenmark 6, Church 5, Varfell 6. |
| PP-NEW-02 | Victory | Universal Peninsular Sovereignty condition added. Faction-specific conditions retained as alternates. |
| PP-NEW-03 | Victory | Peninsular Partition co-victory added. Existing co-victory pairings retained. |
| PP-NEW-04 | System | Accord per-territory attribute (0–3). Modifies effective Prosperity. Accord ≥ 2 required for TCV contribution. |
| PP-NEW-05 | System | Peninsular Strain counter (0–10). Advances from inter-faction battles, faction eliminations, revolts. |
| PP-NEW-06 | System | Battle consequences: RS −1 per battle on Valorian soil. IP +2 per season with inter-faction battle. |
| PP-NEW-07 | Hafenmark | Dynastic Proclamation domain action (Diplomat card). Replaces Parliamentary Sovereignty as primary path. |
| PP-NEW-08 | Varfell | Cultural Reformation domain action (Colonist card). |
| PP-NEW-09 | Church | Seizure Accord formula revised: Success → max(floor(PT/2)+1, 2). Guaranteed ≥ 2. |
| PP-NEW-10 | PT | Starting PT values per territory proposed (§2.2). |
| PP-NEW-11 | Löwenritter | Accord adaptation: Martial Governance (Military pool Govern, Ob +1, cap Accord 2). Strain exemption for first 2 seasons post-coup. |
| PP-NEW-12 | Hafenmark | Parliamentary Sovereignty (victory_v30.md §3.3 primary) struck. Dynastic Assertion promoted to primary. |
