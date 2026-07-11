# VALORIA — Settlement Layer Specification
## Date: 2026-04-16
## Status: CANONICAL — approved 2026-04-17 (editorial batch acceptance)
## Scope: Sub-territory settlement nodes, dual-authority governance, subnational factions, invasion granularity, player progression from settlement to national, faction emergence/collapse, extended timeline, succession
## Precedent: KOEI ROTK (officer-city assignment, development, provincial control), Crusader Kings III (barony-county-duchy-kingdom hierarchy, vassal governance, realm fragmentation)
## Affects: S03 Geography, S04 Clocks, S06 Faction Layer, S07 Victory, S08 CI, S09 Military, S10 NPC Behavior, S14 Fieldwork, S15 Mass Combat, S17 Scale Transitions, Player Agency, Companion Specification
## Canon compliance: P-01 (settlement-level Thread phenomena), P-03 (settlement as rendered environment), P-15 (settlement identity as cultural-layer persistence)

---

# PART 1: ARCHITECTURE

## §1.1 The Two-Tier Map

The existing 17 territories become **provinces** — the strategic layer. Each province contains 1–3 **settlements** — the personal layer. Provinces are where factions operate. Settlements are where people live and where the player acts.

| Layer | Unit | Count | Control | Mechanical Function |
|-------|------|-------|---------|-------------------|
| Province | T1–T17 | 17 | National-level faction | Domain Actions, faction stats, Accord, military movement |
| Settlement | S-001 to S-036 | 36 | Governor (NPC, player, or subnational faction) | Scene actions, fieldwork, social engagement, local governance, economic output |

**Provinces are not changed.** All existing province-level mechanics (Accord, Piety Track, TCV, Fort Level, Calamity radiation, adjacency) continue to operate at the province level. Settlements add granularity beneath provinces — they do not replace them.

**The ROTK principle:** A national-level faction controls a province. It assigns officers to manage settlements within that province. An officer who governs well builds standing. An officer who governs badly or rebels can be replaced. A player who accumulates enough settlements can challenge for provincial control. A faction that loses all its provinces may retain a single settlement as a city-state.

**The CK3 principle:** Settlements have types (Seat, City, Town, Fortress, Cathedral, Port). Type determines what the settlement produces and which subnational factions have a natural claim to manage it. A Market settlement naturally aligns with Guild management. A Cathedral settlement naturally aligns with Church management. The controlling province faction can override these natural alignments, but doing so costs Accord.

## §1.2 Settlement Types

| Type | Function | Natural Manager | Stats |
|------|----------|-----------------|-------|
| **Seat** | Provincial capital. Administrative center. Court location. | Province-controlling faction | Prosperity, Defense, Population |
| **City** | Major urban center. Trade, population, culture. | Province-controlling faction or Guilds | Prosperity, Population, Trade |
| **Town** | Smaller settlement. Local governance. Agricultural or resource base. | Province-controlling faction | Prosperity, Population |
| **Fortress** | Military installation. Chokepoint defense. Garrison base. | Province-controlling faction or Löwenritter | Defense, Garrison Capacity |
| **Port** | Coastal or river settlement. Naval access. Trade hub. | Province-controlling faction or Guilds | Prosperity, Trade, Naval |
| **Cathedral** | Church institution. Theological center. Piety generator. | Church (regardless of province controller) | Piety Influence, Population |
| **Mine** | Resource extraction. Economic output. | Province-controlling faction or Guilds | Prosperity (raw), Population (low) |
| **Outpost** | Frontier settlement. Observation, defense, or Thread monitoring. | Province-controlling faction or Wardens | Defense (low), Special (varies) |

## §1.3 Settlement Stats

**Derived values (`designs/scene/derived_stats_v30.md` §9/§14.1):** Settlement stats (Prosperity/Defense/Order, 0–5) produce derived values for the videogame layer. **Citation corrected 2026-07-08 (ED-IN-0029 docket, OPT-AV-7)** — previously cited a nonexistent file, `derived_stats_v1`; the real doc's §9 currently marks these formulas "PENDING — Not canonicalized" even though they are unchanged here and already live-gated in `references/module_contracts.yaml` (a separate canonicity-status question, not a citation error — tracked, not resolved by this fix):

| Stat | Derived Value | Derivation | Player Sees |
|------|--------------|-----------|-------------|
| Prosperity | Local Economy | Prosperity × 50 | Gold income contribution to faction Treasury |
| Defense | Garrison Strength | Defense × 20 + Fort Level × 30 | Settlement defensibility score |
| Order | Public Order | Order × 20 | Civil stability meter — below 0 triggers riot events |

Settlement derived values feed upward to faction derived values: Local Economy contributes to faction Treasury income. Garrison Strength is displayed when evaluating military targets. Public Order generates events when drained. Stat damage (Prosperity −1) only occurs when a derived value hits 0 and stays through Accounting — same rule as faction stats.

Each settlement has 3 stats tracked on a 0–5 scale:

| Stat | What it represents | Effect |
|------|-------------------|--------|
| **Prosperity** | Economic output and quality of life | Contributes to province Effective Prosperity. Each point of settlement Prosperity adds to the province's Prosperity pool. |
| **Defense** | Fortification and garrison readiness | Determines Ob for attackers. Defense 0 = undefended (auto-capture). Defense 5 = major fortress. |
| **Order** | Local institutional stability and compliance | Analogous to province Accord but at settlement scale. Order 0 = local revolt. Order 3+ = stable governance. Feeds upward into province Accord. |

**Province Accord derivation (REVISED):** Province Accord is now the floor of the average Order across all settlements in the province, rounded down. If a province has 3 settlements with Order 4, 2, and 1, the province Accord = floor((4+2+1)/3) = floor(2.33) = 2. This means province Accord emerges from settlement governance rather than being set directly. Existing Accord change rules (peninsular_strain §2.3–2.4) now operate by modifying settlement Order values, which cascade upward.

## §1.4 Institutional Facility Tiers (PP-661)

Each Seat-type and certain City-type settlements offer a bounded number of **Institutional Facility slots** that the faction controlling the settlement can allocate to rank-holders per faction_politics_v30 §1 Hall Tier specification. Facility slots are a finite settlement resource; when full, new rank-holders at the corresponding tier receive "pending" status until a slot opens.

### §1.4.1 Facility Slot Capacity by Settlement Type

| Settlement Type | Wing Slots (Std 6+) | Suite Slots (Std 5) | Chamber Slots (Std 3–4) | Billet Slots (Std 1–2) |
|-----------------|--------------------|--------------------|--------------------------|-------------------------|
| Seat | 3 | 5 | 8 | unlimited (shared quarters) |
| City | 1 | 3 | 5 | unlimited |
| Town | 0 | 1 | 3 | unlimited |
| Fortress | 0 | 1 | 4 (military chambers) | unlimited |
| Cathedral | 1 (Prelate's Palace) | 3 (Bishop's Suites) | 5 (Canon's Chambers) | unlimited (cloister) |
| Port | 0 | 1 | 3 | unlimited |
| Mine | 0 | 0 | 1 | unlimited |
| Outpost | 0 | 0 | 1 | unlimited |

### §1.4.2 Allocation Rules

- Slots are allocated by the settlement's controlling authority (usually the province faction).
- At Seat settlements, the faction leader occupies one Wing automatically (counted against the 3-cap). Inner circle NPCs occupy additional Wings per rank.
- Player advancement to Standing 6+ requires an available Wing slot. If none available, advancement is "pending" (FAC-02 standing-debt equivalent per faction_politics_v30 §1.0).
- Wing occupancy is durable across seasons until death, succession, exile, or formal transfer.

### §1.4.3 Capacity Pressure as Political Mechanic

At full capacity, rank advancement becomes politically charged. If a Seat has 3 Wings occupied (leader + 2 inner circle) and the player reaches Standing 6 as a fourth claimant:

1. **Existing Wing-holder departs** (Generational Shift, death, exile, political transition), OR
2. **Settlement expands capacity** via Domain Action **Expand Institutional Capacity** (Treasury −300 (derived_stats_v1), scene action at settlement, +1 Wing added; cap: +1 Wing per settlement per decade), OR
3. **Player accepts Prince-in-Waiting provisional rank** — Std 6 privileges without Wing residency. Each season without Wing, player makes social contest (Disposition pool vs Ob 2) to maintain inner-circle standing. Failure reverts to Standing 5.

This creates structural political pressure: full capacity drives exile, succession, or formal expansion rather than permitting unlimited inner-circle accumulation.

### §1.4.4 Cross-Faction Wing Allocation

At Seat settlements of composite control (e.g., Valorsplatz Cathedral S-003 is Church-controlled within Crown territory T1), Wing slots belong to the settlement's direct controller, not the province's controller. Church-controlled Seats host Prelates and Cardinals regardless of Crown occupation of Valorsplatz Palace.

Cross-faction Wings may be ceded as treaty concessions (ambassadorial residences). A ceded Wing counts against the ceding faction's capacity while occupied by the allied faction.

[EDITORIAL: ED-659 — Hall Tier mechanical integration applied PP-661.]

### §1.5 Church Settlement Infrastructure — Four Independent Axes (campaign_architecture_v1 Part 1)

Church presence in a settlement is NOT a linear tier progression. It is four independent binary/tiered axes that combine in any valid configuration. See campaign_architecture_v1.md §1.1 for the canonical specification.

**Axis 1 — Religious Building (mutually exclusive, one per settlement):** None / Chapel (+0.5 PT/season) / Church (+1 PT/season) / Cathedral (+2 PT/season, +0.5 PT to adjacent territories).

**Axis 2 — Templar Station (binary):** +1 CI/season in territory. Church can interrupt rival Domain Actions (+1 Ob, costs 1 CI).

**Axis 3 — Inquisitor Base (binary):** Surveillance Zone: Thread practitioners make Concealment test each season. RM governance-building actions +1 Ob. RM cultural presence generates 1 Church Attention/season.

**Axis 4 — Church Governor (binary):** Settlement governance uses Church faction stats. De facto Church territory. Removal requires Mass Battle, Mandate Challenge (Ob 6+), or RM community action at OW.

**Seizure Ob Modifiers (stacking, per settlement):** Chapel −0, Church −1, Cathedral −2, Templar −1, Inquisitor −1, Church Governor −2. Cap: −4 per settlement (campaign_architecture_v1 refinement). CI=100 Mass Seizure Declaration triggers simultaneous Seizure across all territories containing Church infrastructure.

**Historical grounding (Papal States, Calvin's Geneva, 1979 Iran):** Church infrastructure grows through governance vacuum filling, institutional capture via demonstrated competence, and pre-positioned parallel infrastructure that activates when existing order fails. See historical_precedents_analysis §1.

### §1.6 Parish Social Services (NEW — historical_precedents_analysis §1.4)

Church buildings provide a Stability bonus to the settlement they occupy, reflecting the social services (education, welfare, dispute resolution) the parish provides. This makes Church infrastructure instrumentally useful to secular governors — the Geneva trap.

| Church Building | Settlement Stability Bonus |
|----------------|--------------------------|
| Chapel | +0.5 Order/season (rounds: +1 every other season) |
| Church | +1 Order at installation (one-time) |
| Cathedral | +1 Order at installation + Order decay −1 (Order is more stable) |

This bonus applies regardless of whether the Church controls the settlement. A Crown governor who permits a Chapel in their settlement benefits from the social cohesion the parish provides — but also accepts the PT generation that comes with it.

**Design intent:** Historically, theocracies grew not through hostility but through helpfulness. Populations and even secular leaders wanted Church infrastructure because it solved real governance problems. The theocratic endpoint was a consequence of rational, self-interested decisions at each step.

### §1.7 Pastoral Assumption (NEW — historical_precedents_analysis §1.4)

When a settlement has no governor (governor killed, faction collapsed, settlement at Order 0 with governor expelled per §4.3) AND the settlement contains at least a Chapel (Axis 1), the Church may install a Church Governor (Axis 4) as a Domain Action at Ob 1 (vs normal governor assignment Ob).

**Rationale:** In post-collapse scenarios historically, the parish priest was often the de facto civil authority — the only literate person with institutional backing still present. This mechanic formalizes the Church's ability to fill governance vacuums.

**Restrictions:** Pastoral Assumption does not change Provincial Authority — the province faction retains taxation, military, and legal framework. It only installs a Church Governor at the settlement level. The province faction may revoke this per §3.3 revocation rules (Ob = Church Influence ÷ 2, Order −1, Disposition −2 with Church).

[EDITORIAL: ED-682 — Historical precedent integration for Church settlement mechanics. Source: historical_precedents_analysis.md §1.]

---

## §1.8 Settlement Legitimacy & Popular Support → Faction Mandate (LPS-2e — Jordan ruling 2026-05-30: re-grained faction→settlement + size-weighted; derived bottom-up + historical, Jordan-vetoable; supersedes the LPS-1 territory-grain model)

**Jordan ruling (2026-05-30, structural/metaphysical layer):** Legitimacy (L) and Popular Support (PS) are **per-settlement** political-acceptance values — **NOT faction-level stats.** Faction **Mandate is the aggregate** of them, with a stabilizing feedback from Mandate back to settlement L/PS. This **supersedes the faction-level L/PS canonized in PP-686 v2** (`faction_behavior_v30 §2/§3.4/§3.5/§4`, `faction_state_authoring_v30 §8`, `faction_canon_v30 §3.4/§5`, `params/factions/stats_1_7_scale.md` "7-stat" header) — those put L/PS at the wrong level. PP-686 had the right stats (L, PS, 0–7) and the right blend; only the *level* was wrong. This section is the corrected canonical home.

**Map-tier terminology (reconciliation — geography_v30 retained, no rename).** `geography_v30` uses **"territory"** for the **17 top-level / province-tier map nodes (T1–T17)** — the coarsest political units, kept exactly as-is. The **base civic/political/living unit is the SETTLEMENT** (§1.1 Two-Tier Map; the siege-target; 37 across the registry); the **province** is the aggregate of its settlements (§2.1). L and PS attach to the **settlement** (the finest tier) and aggregate upward. Where older docs say "per-territory L/PS," read **per-settlement, aggregated through provinces**; geography's "territory" remains the province-tier node and is unaffected.

**Per-settlement values.** Each settlement tracks, for its controlling faction:
- **Legitimacy (L), 0–7** — institutional/constitutional acceptance (slow-moving: dynastic claims, papal bulls, constitutional authority).
- **Popular Support (PS), 0–7** — active populace backing (faster-moving: mobilization, local approval).
These are **distinct from settlement Order** (Order = civil compliance, feeds province Accord via `floor(mean settlement Order)`, §1.3; L/PS = faction-political acceptance) — not conflated.

**Settlement Weight (size).** Operationalizes the **Population** dimension named in §1.2 but left unscaled (§9 PENDING). Weight measures how much a settlement's acceptance counts toward Mandate:
`W_s = base(Type) + Prosperity_s + FacilityTier_s`
- **base(Type)** — inherent population/importance: Seat 3, City 3, Cathedral 3, Town 2, Fortress 2, Port 2, Village 1, Mine 1, Outpost 1 (ranked from §1.2 and the §1.4.1 facility-capacity ladder).
- **Prosperity_s (0–5)** — developed economic capacity (existing stat; rises with development).
- **FacilityTier_s (0–3)** — built institutional infrastructure: highest facility tier present (0 billets only / 1 Chambers / 2 Suites / 3 Wings, §1.4). **This is the infrastructure-investment driver — investing in a settlement raises its Weight, so its acceptance counts for more.**
Range: undeveloped Outpost W=1 → fully-developed Seat W=11.

**Faction Mandate (size-weighted aggregate).** Let per-settlement acceptance `q_s = 0.5·L_s + 0.5·PS_s` (0–7), and weighted legitimacy mass `T = Σ_s W_s · (q_s / 7)` over the faction's controlled settlements. Then:
`Mandate = clamp( round( 7 · T / (T + K) ), 0, 7 )`, with **K = 6** (calibrated, Stage-4 sim below).
- **Size-weighted:** a settlement's acceptance counts in proportion to its Weight — large/developed settlements dominate, sparse ones contribute little. A faction holding **one province of large, developed settlements has a higher Mandate than one holding many provinces of tiny settlements** (more accepted population = more legitimacy) — the intended logic. Equal total accepted population → equal Mandate.
- **Saturating / bounded:** the `T/(T+K)` form gives diminishing returns (the marginal legitimacy of the Nth loyal hamlet is less than the first city) and keeps Mandate in 0–7 for any holding. This is the **Lesson-5 bound** on the loop — `∂Mandate/∂q` shrinks as T grows, damping it.
- **Aggregation is settlement→faction directly**, consistent with the existing settlement→faction rollup (faction Treasury income = `Σ settlement Prosperity × 10`, derived_stats §8.1). The **province** remains the mid-tier for Accord (§1.3); Mandate sources from settlements.
- **Faction aggregate L / aggregate PS** (for consumers needing L and PS separately, e.g. strictness) = the **Weight-weighted means** `aggregate_L = Σ W_s·L_s / Σ W_s`, `aggregate_PS = Σ W_s·PS_s / Σ W_s`.
- **N=1 / zero / embedded / Restoration:** a faction holding one developed province (e.g. Church's Himmelenger Cathedral province) computes normally and lands solidly (sim: Mandate 5). A faction controlling **zero** settlements has T=0 → Mandate 0. An **embedded** faction (Löwenritter pre-coup) acts through its host (Mandate N/A until it holds settlements). **Restoration** is territoryless and operates at the **community** level via Presence markers, so its L/PS live in its Presence localities (per `faction_state_authoring §6` / PP-460 — "L+PS track community-level acceptance") and T is summed over those localities.

**Feedback (Mandate → settlement L/PS) — mean-reverting / stabilizing.** Each Accounting, held settlements drift toward the faction's Mandate (local acceptance regresses toward the realm's overall standing): a settlement whose `q_s` sits ≥1 **below** Mandate gets **L +1** (capped 7); ≥1 **above** gets **PS −1** (capped 0); at most ±1 per settlement per season, within the ±2 faction-stat seasonal cap. This is **negative (stabilizing)** feedback. **Stage-4 sim (2026-05-30):** the coupled Mandate↔settlement system stays bounded 0–7 and converges over 30 seasons under mission shocks (no runaway) for Crown/Church/Varfell holdings; the size-weighted saturating Mandate damps the loop further. Historical anchor for the size weighting: realm legitimacy/levy capacity scales with the population and wealth of held lands — CK3 county Development & control feeding crown authority; EU4 province development; Victoria population-weighted political power; KOEI ROTK city population/development setting yield (one metropolis outweighs several hamlets).

**Faction-level mission outcomes** (PP-686 cascade-fidelity / procedural / violation ΔL/ΔPS) now apply their ΔL/ΔPS **to the faction's controlled settlements** (uniformly, clamped 0–7), which re-aggregate into Mandate — keeping per-settlement L/PS as canonical state and Mandate as the pure derived aggregate.

**Consumers.** PP-686 Public Expectation strictness `base + 0.5·(L/7) − 0.3·(PS/7)` reads the faction **aggregate** L and PS defined above. `derived_stats_v30`'s faction Legitimacy meter (`= Mandate × 20`) is the displayed aggregate and remains consistent as a derivation (Mandate is the settlement-L/PS aggregate); the ×20 meter is a per-system derived buffer (derived_stats §3), sized like the sibling faction meters (Reputation ×15, Discipline ×10, Treasury ×100) and not bound to 0–100; its footnote claiming "PP-686 split Mandate into faction-level L+PS" is corrected by this section. Detailed consumer rewiring is staged in the master ledger `_lps_structural_redesign_2026-05-30`.

**GD-1 synergy.** Parliament votes = current Mandate (`faction_layer §5.3`), and Mandate now aggregates settlement legitimacy weighted by population → a faction's political weight emerges from the size and loyalty of the populace it actually governs, coherent with GD-1 (Peninsular Sovereignty / territorial control as the win condition).

## §1.8a Settlement-grain L/PS derivation events (PROPOSED — ED-SE-0007, 2026-07-08)

**Status: PROPOSED, not yet ratified.** §1.8 above specifies how settlement L/PS *aggregate* into
Mandate and how Mandate *feeds back* into settlement L/PS (the mean-reverting drift), but the only
settlement-grain *source* of an L/PS change currently specified is §1.8's own uniform faction-level
cascade ("Faction-level mission outcomes... apply their ΔL/ΔPS to the faction's controlled
settlements uniformly"). No event distinguishes *how* one settlement's own acceptance rises or
falls from another's — `sim/territory/registry.py`'s `legitimacy`/`popular_support` fields are
declared but have no per-settlement derivation rule to execute (the ED-FA-0004 Stratum-B gap this
subsection exists to fill; provenance and full research:
`designs/audit/2026-07-08-fa-se-historical-precedent-research/fa_se_historical_precedent_research_v1.md`
§Step 3 SE-1).

**Grounding.** Max Weber's three types of legitimate domination (*Economy and Society*, 1922) —
**traditional** (sanctity of immemorial rule), **legal-rational** (belief in enacted procedure), and
**charismatic** (devotion to demonstrated extraordinary performance) — map directly onto this
section's own L/PS split: **Legitimacy (L) is the traditional + legal-rational channel** (slow,
institutional); **Popular Support (PS) is the charismatic/performance channel** (fast, earned by
visible outcomes). Weber's *routinization of charisma* (repeated good performance hardening into
accepted institutional right) is the mechanism §1.8's own Mandate→L feedback already implements
without naming it. Albert Hirschman's *loyalty* (*Exit, Voice, and Loyalty*, 1970) supplies the
damping frame for why these events are additive-and-capped rather than compounding runaway.

**L-channel events (traditional / legal-rational — one-time or slow, capped 0–7):**

| Event | ΔL | Note |
|---|---|---|
| Entry oath sworn / privileges confirmed on control transfer | +1 (one-time) | Ties to a future Entry Terms rule (SE-5); not yet specified here |
| Charter granted (subnational management grant, §3.3) | +1 (one-time) | |
| Regular court held (governance action, ≥2 consecutive seasons) | +1 (capped once per grant) | Rewards sustained, not one-off, adjudication |
| Tax/tithe collected within the faction's announced fiscal stance | 0 | Stance *broken* (collection outside the announced rate) → −1; ties to a future Fiscal Stance rule (FA-1) |
| Governor rotated per stated policy | 0 | Governor imposed over protest → −1 |

**PS-channel events (charismatic / performance — faster-moving, capped 0–7):**

| Event | ΔPS | Note |
|---|---|---|
| Dearth relieved (governance response, ties to a future Dearth rule, SE-2) | +2 | |
| Festival or public event sponsored | +1 | |
| Settlement successfully defended from raid/siege | +2 | |
| Levy or extraction taken from the settlement | −1 | |
| Forced billeting / garrison quartered against local wishes | −1 | |
| Public execution of a local resident | −2 | |

**Scope discipline.** This subsection specifies the *event → ΔL/ΔPS* table only. It does not
itself change §1.8's aggregation formula, the Mandate feedback, or the faction-level cascade
(§1.8's existing paragraph on PP-686 mission outcomes is unchanged and continues to apply
uniformly where no settlement-grain event fires). Events that reference a not-yet-specified rule
(Entry Terms, Fiscal Stance, Dearth) are flagged inline above rather than inventing that rule here;
each is tracked as its own docket item (ED-SE-0007/0008/0011 and ED-FA-0008) and should compose
with this table when it lands. Magnitudes above are shape proposals per the historical grounding,
not sim-calibrated constants — calibrate before treating any value as canon, per CLAUDE.md §5/§7.

## §1.8b Succession continuity and settlement L (PROPOSED — ED-SE-0012, 2026-07-08)

**Status: PROPOSED, not yet ratified.** Patches how a *succession* (the controlling faction's
leadership changing, control unchanged) affects per-settlement L, sharpening the PP-686 succession
rule (`faction_behavior_v30 §3.5.1`) and tying it to §1.8's feedback model and to §5.3 Entry Terms
(SE-5). Provenance: `designs/audit/2026-07-08-fa-se-historical-precedent-research/fa_se_historical_precedent_research_v1.md`
§Step 3 SE-6.

**Grounding.** Ernst Kantorowicz, *The King's Two Bodies* (1957) — the medieval legal fiction of the
corporate crown (*dignitas non moritur*, "the dignity does not die") was engineered *precisely to
abolish the interregnum*: the office persists undiminished across the mortal person of its holder, so
a **normal** succession transmits no gap in legitimacy. §1.8 already models legitimacy as
institutional and slow-moving; this subsection says what a leadership succession does — and,
critically, does *not* do — to settlement L.

**Rule.** Distinguish a **control transfer** (the settlement's controlling *faction* changes —
governed by §5.3 Entry Terms, SE-5) from a **succession** (the controlling faction's *leadership*
changes; control does not move). A single control event resolves under **exactly one** of the two
rules — they never both fire on one settlement in one season, so a §5.3 Entry-Terms L-seed and a
succession L-drift are never applied to the same settlement together.

| Succession mode (`state.succession` Key, `succession_mode` field — faction_behavior_v30 §3.5.1) | Effect on held-settlement L | Note |
|---|---|---|
| `normal` | **L unchanged** | The corporate crown never dies — no interregnum-exposure penalty (Kantorowicz 1957). |
| `normal` + entry/confirmation ceremony performed | **L +1** (one-time, only in each settlement where the ceremony is actually held) | This is the §1.8a "privileges confirmed" L-channel event; applies **only** where a ceremony is performed, not automatically. Ties to §5.3 / §3.3a confirmation-for-fee. |
| `contested` / `emergency` / `imposed` | **L −1 in all held settlements** + Regency check (FA-7) | Disputed/forced succession = interregnum exposure. The Regency subsystem (FA-7) is FA-lane, not specified here. |

**Composition note.** The `+1` confirmation increment above is the *same* event §1.8a lists and the
*same* ceremony §5.3 Confirm-Privileges credits — but on a **control transfer** that credit is already
carried by §5.3's L *seed* (L seeds 3 for Confirm), so the `+1` does **not** additionally stack on a
transfer; it fires only on a **same-faction succession** where a ceremony is separately held. The
`contested/emergency/imposed` −1 is bounded by the ±2 faction-stat seasonal cap (§1.8) and floors at 0.

**Scope discipline.** This specifies only how a succession event moves settlement L; it does not change
§1.8 aggregation, the Mandate feedback, §1.8a's event table, or §5.3's transfer seed (with which it
*composes*, not competes). The Regency subsystem the non-normal modes call is owned by the FA lane
(FA-7) and is not authored here. Magnitudes are shape proposals per Kantorowicz 1957, not
sim-calibrated constants — calibrate before treating any value as canon (CLAUDE.md §5/§7).

## §1.8c Weight loss as Exit (PROPOSED — ED-SE-0016, 2026-07-08)

**Status: PROPOSED, not yet ratified.** Extends the §1.8 Settlement Weight concept and the §4.3
Prosperity-0 row: makes the "population leaving" flavor text bite the §1.8 Weight aggregate.
Provenance: same research report, §Step 3 SE-10.

**Grounding.** Albert Hirschman, *Exit, Voice, and Loyalty* (1970) — when institutional *voice*
fails, the governed **exit**, and exit is the silent vote misgovernance cannot argue with. The
medieval custom *Stadtluft macht frei nach Jahr und Tag* ("town air makes free after a year and a
day") supplies the destination logic: towns grew by absorbing the countryside's refugees,
freedom-after-residence being the historical magnet that turned a neighbor's misrule into one's own
population gain.

**Rule.** A settlement that spends **≥2 consecutive seasons in Dearth (§4.3a, SE-2) or at Order ≤ 1**
loses **1 Settlement Weight** (emigration) — lowering both its Mandate contribution (§1.8's `W_s`
term) and its Treasury base (`derived_stats §8.1`). Weight **recovers +1 per 4 consecutive stable
seasons** (neither Dearth nor Order ≤ 1), capped at its structural ceiling `base(Type) + Prosperity_s
+ FacilityTier_s` (§1.8 — recovery cannot exceed developed capacity). **Exit destination:** the
nearest higher-Order settlement reachable on the adjacency graph (§2.2 / `settlement_adjacency_v30`)
gains a one-time **+0.5 Prosperity-growth season** (the refugees are labor — *Stadtluft macht frei*).

**Composition.** Weight-as-Exit is a *Weight* change, distinct from the L/PS events of §1.8a and the
succession L-drift of §1.8b: misgovernance bites Mandate **here** through the *size* channel (fewer
people counted in `W_s`), **there** through the *acceptance* channel (lower `q_s`). Both can fire in
the same season on the same settlement without double-counting, because they move different terms of
the §1.8 mass `T = Σ W_s · (q_s / 7)`.

**Scope discipline.** Extends §1.8 (Weight) and §4.3 (Prosperity-0 / Dearth) only; does not alter the
Mandate formula, the saturating constant K, or the feedback. The Dearth trigger it reads is SE-2's
(§4.3a); if that lands with a different definition, this rule follows it rather than restating it.
Magnitudes (2 seasons, +1 per 4, +0.5 growth) are shape proposals per Hirschman 1970, not
sim-calibrated — calibrate before canon (CLAUDE.md §5/§7).

# PART 2: THE SETTLEMENTS (PP-726 corrected granularity)

**Status note (PP-726, 2026-05-10):** PART 2 has been refactored to operate at correct granularity per `valoria_political_hierarchy_v30 §1.1`. A settlement is a **city/fortress/village/town** — the siege-target. Districts (Cathedral, Market, Barracks, Harbor, Quarter, Parliament, etc.) and outpost-features (garrison towns, watchtowers, mines, lodges, shrines, watches, storehouses, coves, gates, ruins) are subservient to their parent settlement and are NOT separately siegeable; they appear in §2.2 sub-features registry as properties of their parent.

The Kingdom of Valoria has **35 settlements across 14 provinces in 3 duchies**. Two special-case march-targets (Himmelenger Church city-state, Schoenland foreign Altonian island) bring the canonical adjacency-graph total to **37 settlements**. Askeheim is unincorporated Calamity wilderness with 0 settlements (the Ruins and the Gate are observation features, not siege-targets).

## §2.1 Settlement Registry

### Valorsmark duchy (Almud — also monarch of Valoria)

**Valorsplatz province** (3 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-001 | Valorsplatz | Seat | province primary |
| S-002 | Auerheim | Town | spoke |
| S-003 | Königsbrück | Town | spoke |

**Kronmark province** (3 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-004 | Kronmark | Town | province primary |
| S-005 | Saatfeld | Village | spoke |
| S-006 | Goldenfurt | Town | spoke |

**Lowenskyst province** (2 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-007 | Lowenskyst Fortress | Fortress | province primary |
| S-008 | Tiefental | Village | spoke |

**Feldmark province** (3 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-009 | Feldmark | Town | province primary |
| S-010 | Erntehof | Village | spoke |
| S-011 | Spelzdorf | Village | spoke |

**Stillhelm province** (2 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-012 | Stillhelm | Town | province primary |
| S-013 | Aschenbach | Village | spoke |

**Ehrenfeld province** (2 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-014 | Ehrenfeld | Fortress-City | province primary |
| S-015 | Nordhain | Village | spoke |

### Hafenmark duchy (Baralta)

**Rendstad province** (2 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-016 | Rendstad | Town | province primary |
| S-017 | Holzbrück | Village | spoke |

**Gransol province** (3 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-018 | Gransol | City | province primary |
| S-019 | Niedersol | Town | spoke |
| S-020 | Saltbrück | Town | spoke |

**Spartfell province** (2 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-021 | Spartfell Fortress | Fortress | province primary |
| S-022 | Gelbgrund | Village | spoke |

**Halvarshelm province** (3 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-023 | Halvarshelm Town | Town | province primary |
| S-024 | Erzbach | Village | spoke |
| S-025 | Schmiedhof | Village | spoke |

### Varfell duchy (Vaynard)

**Grauwald province** (2 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-026 | Grauwald | Town | province primary |
| S-027 | Skogheim | Village | spoke |

**Halvardshelm province** (3 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-028 | Halvardshelm | Town | province primary |
| S-029 | Geirsvik | Village | spoke |
| S-030 | Yrnastead | Village | spoke |

**Sigurdshelm province** (3 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-031 | Sigurdshelm | Seat | province primary |
| S-032 | Brynjard | Town | spoke |
| S-033 | Sundfjord | Town | spoke |

**Oastad province** (2 settlements) — 

| S# | Settlement | Type | Role |
|----|------------|------|------|
| S-034 | Oastad | Town | province primary |
| S-035 | Salgrund | Village | spoke |

### Himmelenger Church city-state (Confessor — special case, sovereign ecclesiastical entity, not a province in the duchy hierarchy)

| S# | Settlement | Type | Notes |
|----|------------|------|-------|
| S-036 | Himmelenger | Cathedral-City | Sovereign ecclesiastical city-state. Internal districts: Cathedral (the Confessor's seat), City (lay Church administration, Cardinal of Temperance), Seminary (theological training, Inquisitor recruitment). Single siege-target with three districts. |

### Schoenland (foreign Altonian island — special case, politically independent of the Kingdom; sea-connected via Valorsplatz only)

| S# | Settlement | Type | Notes |
|----|------------|------|-------|
| S-037 | Schoenland | City | Foreign Altonian island. Internal districts: City (governance), Harbor (Altonian/Valorian trade port). Single sea-edge to Valorsplatz; awaiting ED-055 naval-scope expansion for additional routes. |

**Total: 37 march-target settlements** (35 Kingdom + 1 Church city-state + 1 foreign tributary). Province distribution: Valorsmark 6 provinces (15 settlements), Hafenmark 4 provinces (10), Varfell 4 provinces (10). 7 provinces at 3 settlements (capital/breadbasket/commerce-hub/multi-fjord/industrial-mining/ducal-capital density); 7 provinces at 2 settlements (chokepoint/remote-valley/Calamity-edge/highland-sparse). All 35 Kingdom settlements + Himmelenger have ≥2 march-route connections per `valoria_geography_v30.yaml :: settlement_adjacency:` (PP-726 rebuild). Schoenland at degree 1 is foreign-exempt awaiting ED-055.

## §2.2 Sub-features Registry

Sub-features are NOT separate settlements — they are properties of their parent settlement that confer specific mechanical effects. The full taxonomy:

| Sub-feature | Type | Parent settlement | Effect |
|-------------|------|-------------------|--------|
| Valorsplatz Palace district | Royal-court district | S-001 Valorsplatz | Crown's seat of power; Almud's residence; Lion's Table HQ; royal-court scene affordance |
| Valorsplatz Riverside district | Port district | S-001 Valorsplatz | River+sea trade hub; Guild quarter; sea route to Schoenland connects here |
| Valorsplatz Cathedral district | Cathedral district | S-001 Valorsplatz | Solmundic Church presence in capital; ecclesiastical scenes; Church-faction footprint in Crown territory |
| Kronmark Watchtower | Fortified outpost | S-004 Kronmark | Guards northern approach to Valorsplatz; Defense +1 contribution to parent settlement; vision range extension |
| Lowenskyst Garrison Town | Civilian quarter | S-007 Lowenskyst Fortress | Soldiers' families; supply depot; Population +1 to parent; military-unit support |
| Feldmark Storehouse | Industrial facility | S-009 Feldmark | Strategic food storage and processing; controls food supply to northern provinces; Wealth income |
| Stillhelm Watch | Observation outpost | S-012 Stillhelm | Calamity monitoring; Warden contact point; vision into Askeheim wilderness |
| Ehrenfeld Citadel district | Fortress district | S-014 Ehrenfeld | Crown military HQ; Löwenritter base; Defense +2 to parent settlement |
| Ehrenfeld Market district | Trade district | S-014 Ehrenfeld | Trade junction at the crossroads; Wealth income; merchants from all factions |
| Ehrenfeld Barracks district | Military district | S-014 Ehrenfeld | Löwenritter Riskbreaker operations; standing-army production capacity |
| Gransol Parliament district | Government district | S-018 Gransol | Hafenmark Parliament; Baralta's court; constitutional-action venue |
| Gransol Harbor district | Lake-harbor district | S-018 Gransol | Lake trade hub (Gransol is on a lake — landlocked Switzerland-like province); inland waterway commerce |
| Gransol Market Quarter district | Trade district | S-018 Gransol | Guild headquarters; largest trade settlement in Hafenmark; Wealth income |
| Spartfell Village | Civilian quarter | S-021 Spartfell Fortress | Border garrison support; Population +1 to parent |
| Halvarshelm Mines | Industrial district | S-023 Halvarshelm Town | Primary mining operation (iron, copper); Wealth income; Guild labor presence |
| Himmelenger Cathedral district | Cathedral district | S-036 Himmelenger | Solmundic spiritual center; Confessor's seat; highest Piety contribution |
| Himmelenger City district | Lay-Church district | S-036 Himmelenger | Urban population; scholars; Cardinal of Temperance's quarter |
| Himmelenger Seminary district | Cathedral district | S-036 Himmelenger | Church theological training; Inquisitor recruitment site |
| Sigurdshelm Cove | Fjord-port district | S-031 Sigurdshelm | Fjord access; Varfell's limited naval capability; coastal trade |
| Grauwald Lodge | Hidden site | S-026 Grauwald | RM (covert) meeting site; Einhir cultural preservation; thread-witnessed network endpoint |
| Oastad Shrine | Sacred site | S-034 Oastad | Old Einhir ceremonial site; RM stronghold; Community Organizing affordance; thread-witnessed network endpoint |
| Schoenland Harbor district | Port district | S-037 Schoenland | Naval base; Altonian-Valorian trade interface; sea route to Valorsplatz attaches here |

**Askeheim features** (not attached to a parent settlement; canonical observation features in unincorporated wilderness):

| Feature | Type | Notes |
|---------|------|-------|
| Askeheim Ruins | Calamity-zone observation site | Einhir Catastrophe epicenter; active Warden operations; Forgetting barrier restricts physical access; thread-witnessed network endpoint (Warden contact at S-012 Stillhelm Watch) |
| Askeheim Gate | Observation camp | Southern access point; no permanent population; observation only |

These features are NOT siege-targets. They appear in canonical prose (faction operations, Warden activity, thread-witnessed network) but do not participate in the settlement-adjacency march-route graph.

## §2.3 Migration from old §2.1 (PP-726 mapping)

The old §2.1 listed 36 entries (S-001..S-036) mixing settlements with districts and outposts at one granularity. PP-726 re-cuts to 37 settlements (S-001..S-037) at correct granularity. Mapping:

| Old S-ID | Old name | New status |
|----------|----------|------------|
| S-001 | Valorsplatz Palace | Promoted to S-001 **Valorsplatz** (settlement; Palace becomes a district) |
| S-002 | Valorsplatz Riverside | Demoted to Riverside district of S-001 Valorsplatz |
| S-003 | Valorsplatz Cathedral | Demoted to Cathedral district of S-001 Valorsplatz |
| S-004 | Kronmark | Retained as settlement, now S-004 **Kronmark** (canonical primary) |
| S-005 | Kronmark Watchtower | Demoted to Watchtower sub-feature of S-004 Kronmark |
| S-006 | Lowenskyst Fortress | Retained as settlement, now S-007 **Lowenskyst Fortress** (canonical primary of Lowenskyst province) |
| S-007 | Lowenskyst Garrison Town | Demoted to Garrison Town civilian quarter of S-007 Lowenskyst Fortress |
| S-008 | Feldmark | Retained as settlement, now S-009 **Feldmark** |
| S-009 | Feldmark Storehouse | Demoted to Storehouse industrial facility of S-009 Feldmark |
| S-010 | Stillhelm | Retained as settlement, now S-012 **Stillhelm** |
| S-011 | Stillhelm Watch | Demoted to Watch outpost of S-012 Stillhelm |
| S-012 | Ehrenfeld Citadel | Promoted/merged into S-014 **Ehrenfeld** (fortress-city); Citadel becomes a district |
| S-013 | Ehrenfeld Market | Demoted to Market district of S-014 Ehrenfeld |
| S-014 | Ehrenfeld Barracks | Demoted to Barracks district of S-014 Ehrenfeld |
| S-015 | Gransol Parliament | Promoted/merged into S-018 **Gransol**; Parliament becomes a district |
| S-016 | Gransol Harbor | Demoted to Harbor (lake-harbor) district of S-018 Gransol |
| S-017 | Gransol Market Quarter | Demoted to Market Quarter district of S-018 Gransol |
| S-018 | Rendstad | Retained as settlement, now S-016 **Rendstad** |
| S-019 | Spartfell Fortress | Retained as settlement, now S-021 **Spartfell Fortress** |
| S-020 | Spartfell Village | Demoted to Village civilian quarter of S-021 Spartfell Fortress |
| S-021 | Halvarshelm Mines | Demoted to Mines industrial district of S-023 Halvarshelm Town |
| S-022 | Halvarshelm Town | Retained as settlement, now S-023 **Halvarshelm Town** (canonical primary of Halvarshelm province) |
| S-023 | Himmelenger Cathedral | Promoted/merged into S-036 **Himmelenger**; Cathedral becomes a district |
| S-024 | Himmelenger City | Demoted to City district of S-036 Himmelenger |
| S-025 | Himmelenger Seminary | Demoted to Seminary district of S-036 Himmelenger |
| S-026 | Sigurdshelm Keep | Promoted/renamed S-031 **Sigurdshelm** (Vaynard's keep is now the settlement; "Keep" was the keep-district) |
| S-027 | Sigurdshelm Cove | Demoted to Cove fjord-port district of S-031 Sigurdshelm |
| S-028 | Grauwald | Retained as settlement, now S-026 **Grauwald** |
| S-029 | Grauwald Lodge | Demoted to Lodge hidden site of S-026 Grauwald |
| S-030 | Halvardshelm | Retained as settlement, now S-028 **Halvardshelm** |
| S-031 | Oastad | Retained as settlement, now S-034 **Oastad** |
| S-032 | Oastad Shrine | Demoted to Shrine sacred site of S-034 Oastad |
| S-033 | Askeheim Ruins | Demoted to Askeheim observation feature (no parent settlement; unincorporated wilderness) |
| S-034 | Askeheim Gate | Demoted to Askeheim observation feature (no parent settlement) |
| S-035 | Schoenland City | Promoted/merged into S-037 **Schoenland**; City becomes a district |
| S-036 | Schoenland Harbor | Demoted to Harbor port district of S-037 Schoenland |

22 of the 36 old entries were sub-features at wrong granularity; 14 were settlements (now renumbered). PP-726 adds 21 new settlements (the spokes added to bring each province to ≥2: Auerheim, Königsbrück, Saatfeld, Goldenfurt, Tiefental, Erntehof, Spelzdorf, Aschenbach, Nordhain, Holzbrück, Niedersol, Saltbrück, Gelbgrund, Erzbach, Schmiedhof, Skogheim, Geirsvik, Yrnastead, Brynjard, Sundfjord, Salgrund). Net: 14 retained + 21 new = 35 Kingdom settlements + 1 Himmelenger city-state + 1 Schoenland foreign = 37 total.

References to old S-IDs in non-substrate documents (character_canon Part B per-NPC sheets, migration_roster, npc_roster, editorial_ledger historical entries, propagation_map historical entries) are migrated lazily as those documents are next touched.

# PART 3: DUAL-AUTHORITY GOVERNANCE

## §3.1 The Two-Tier Authority Model

Every settlement has two authority slots:

| Slot | Who | What they control |
|------|-----|------------------|
| **Provincial Authority** | The national-level faction controlling the province | Military deployment, taxation, legal framework, Domain Actions targeting the province |
| **Settlement Governor** | An officer (NPC or player) or subnational faction assigned to manage the settlement | Local governance (Order), economic development (Prosperity), local NPC relationships, settlement-level scene generation |

The Provincial Authority sets the rules. The Settlement Governor executes them. When they agree, governance is efficient. When they disagree, tension generates gameplay.

## §3.2 Governor Assignment

The faction controlling a province assigns governors to its settlements. Assignment follows the existing Duty system (player_agency_v30 §3) but at a higher stature level.

| Standing | Governor Eligibility |
|----------|---------------------|
| 0–2 (Operative/Agent) | Cannot be assigned as Governor. Receives standard Duties. |
| 3 (Counselor) | Eligible for Governor of one Town or Outpost. |
| 4 (Lieutenant) | Eligible for Governor of one City, Fortress, or Mine. |
| 5 (Successor) | Eligible for Governor of a Seat or Cathedral (requires faction leader approval). |

**Player as Governor:** When a player is assigned as Settlement Governor, their seasonal Duty IS governance. Each season, the player receives one mandatory governance action (no scene action cost) plus their normal scene actions for personal pursuits. **Companion-governor (per settlement_bridge_unification C-04):** A companion serving as governor gets 1 free action per season — social OR governance, player chooses. Not both. The governance action targets the settlement's stats:

| Governance Action | Pool | Ob | Effect on Success |
|------------------|------|-----|-------------------|
| Develop | Cognition + Wealth-relevant History | floor(Prosperity/2) + 1 | Prosperity +1 (cap: settlement type max) |
| Fortify | Military-relevant stat + History | floor(Defense/2) + 1 | Defense +1 (cap: settlement type max) |
| Pacify | Charisma + local History | floor((3 − Order) + 1), min 1 | Order +1 (cap: 5) |
| Administer | Attunement + Governance History | 2 | Maintain Order (no decay this season). Reveals one local NPC's active Conviction. |

**[ED-SE-0005, 2026-07-08] Administer — DISTILL (folds when the governance-play redesign supersedes §3.2, OPT-16).** The ratified pessimist-action audit (`designs/audit/2026-07-08-pessimist-action-audit/`, ED-IN-0027) dissolves `Administer` into two things it already duplicates: its **information half** (reveal one NPC's active Conviction) into the redesign's richer `Investigate` verb (which reveals *and* offers a four-way disposition choice on what is found), and its **maintenance half** (no Order decay) into the structural state of simply not spending the season's governance action on growth. The row is retained here as the current baseline until `governance_play_redesign_v1` supersedes §3.2; the NPC governor priority tree (ED-SETT-06) keeps Administer as its lowest-priority hold until then.

**NPC Governor:** NPC governors use the faction AI priority tree with settlement-level adaptation. NPC governors always prioritize Order ≥ 2 (institutional stability), then Prosperity development, then Defense only if threatened.

**Bishop-Governor (PP-TBD):** A special governor type installed via Church Ecclesiastical Appointment action. Bishop-governors follow Church NPC Priority Tree (npc_behavior_v30 §8.2) rather than the controlling faction's tree. Settlement governance transfers to Church on appointment. Province fractionalizes if bishop-governor settlement's controller now differs from Seat holder.

## §3.3 Subnational Faction Governance

Certain settlement types naturally align with subnational factions. The provincial authority may grant management rights to a subnational faction, or the subnational faction may already hold traditional rights.

| Subnational Faction | Natural Settlement Types | Management Effect |
|--------------------|------------------------|-------------------|
| Church | Cathedral | +1 Piety Influence per season. Church governor uses Church stats, not province faction stats. Province faction retains taxation rights. |
| Guilds | City, Port, Market, Mine | +1 Trade per season. Guild governor uses Wealth as primary stat. Province faction retains military and legal authority. |
| Ministry | Seat, City | Administrative efficiency: Order decay −1 (Order is more stable). Governor uses Influence as primary stat. |
| Löwenritter | Fortress | Military efficiency: Defense +1 passive. Löwenritter governor uses Military as primary stat. Province faction retains legal authority but military operations defer to Löwenritter. |
| RM | Outpost, Town (in low-CV territories) | Community presence: CV −1 potential per season (Einhir heritage restoration). Only available in territories with PT ≤ 2. Province faction may not know RM is managing the settlement (covert management). |
| Wardens | Outpost (Askeheim, Stillhelm Watch) | Thread monitoring: RS effects detected 1 band earlier. Warden governor operates independently. |
| Niflhel | Any (covert) | Niflhel does not govern openly. Niflhel infiltrates a settlement by placing an operative as a secondary influence. Effect: Intel-gathering at +1D in that settlement. Detection: province faction may discover Niflhel presence via Investigation (Evidence Track threshold 3). |

**RM Cell Resilience (NEW — historical_precedents_analysis §3.4):** If RM has Presence markers in ≥ 3 settlements within a province, Church/Crown suppression actions against RM in that province take +1 Ob. Historical precedent (Solidarity in Poland, Bolshevik cells, ANC underground): distributed cell structures are harder to suppress than concentrated organizations because no single arrest can destroy the network. This modifier stacks with the Inquisitor surveillance +1 Ob (which represents surveillance, not suppression). Result: a well-distributed RM network in a territory with an Inquisitor faces +1 Ob to organize (surveillance) and gives the Church +1 Ob to suppress (resilience). Strategic equilibrium.

[EDITORIAL: ED-683 — RM cell resilience mechanic. Source: historical_precedents_analysis.md §3.]

**[ED-SE-0005, 2026-07-08] Ownership note — Grant/Revoke is a Provincial-Authority Domain Action, single-homed in the FA lane.** The ratified pessimist-action audit (`designs/audit/2026-07-08-pessimist-action-audit/`, ED-IN-0027) confirms Grant/Revoke Subnational Management is exercised in the province-faction (Provincial Authority) capacity, not by the Settlement Governor — mechanically a `da.public_governance` Domain Action that happens to target a settlement. It is single-homed in the FA lane's `domain_actions` inventory (the C-FA-12 reconciliation; the full action definition is authored with the `domain_actions` home doc — ED-FA-0002, pending). The rules below describe its settlement-side **effects**; they are not a second, SE-native player action.

**Granting management:** The province faction may grant management of a settlement to a subnational faction as a Domain Action (Influence, Ob 1 — it is an administrative act, not a contested one). The subnational faction's governor replaces the faction governor for that settlement. The province faction retains Provincial Authority (taxation, military, legal framework).

**Revoking management:** The province faction may revoke subnational management as a Domain Action (Influence, Ob = subnational faction's Influence ÷ 2, round up). Revocation costs Order −1 in the settlement (the population perceives institutional disruption) and Disposition −2 with the subnational faction's leadership.

**Contested management:** If the subnational faction's interests conflict with the province faction's orders (e.g., Church governor refuses to allow RM Community Organizing in a Cathedral settlement), the conflict resolves through social contest (per social_contest_v30 §7 — asymmetric, with the province faction as institutional authority and the subnational faction as petitioner).

### §3.3a Charters, prescription, and Quo Warranto (PROPOSED — ED-SE-0010, 2026-07-08)

**Status: PROPOSED, not yet ratified.** Re-grounds the §3.3 grant/revoke pair above — it *refines
those PROVISIONAL rules in place*, it does not replace them, and it adds **no** new player action
(Grant/Revoke remains the single-homed FA-lane Domain Action per the ED-SE-0005 ownership note
above). Provenance: `designs/audit/2026-07-08-fa-se-historical-precedent-research/fa_se_historical_precedent_research_v1.md`
§Step 3 SE-4.

**Grounding.** The medieval charter tradition: **Magdeburg-law charter diffusion** (a granted
municipal charter was a durable, heritable instrument, not a revocable license), **Edward I's Quo
Warranto campaign 1278–94** ("*Quo warranto?* — by what warrant do you hold this liberty?": the crown
forcing chartered holders to prove title in a public forum), and the **City of London charter
forfeiture 1683 / restoration 1690** (revoking one city's charter by quo warranto frightened every
chartered corporation in the realm — the chilling effect). **Prescription doctrine** (long possession
hardens privilege into right) and **universal accession-confirmation practice** (a new ruler confirms
existing charters for a fee) complete the frame. Through-line: a charter is *legitimacy made durable*,
and pulling one is costly in proportion to its age and to how many other holders fear they are next.

**Rules** (layer onto the §3.3 grant/revoke *effects*; they do not add a second player action):

- **Charter tag on grant.** Granting subnational management (§3.3) writes a **durable Charter tag** on
  the settlement, stamped with its grant-season. The Charter **survives succession** (§1.8b) — it is
  the settlement's, not the grantor-leader's. Grant fires the §1.8a L-channel "Charter granted +1"
  event once.
- **Prescription (age-scaled revocation Ob).** Revocation Ob is no longer flat:
  `Ob = (§3.3 base revoke Ob = subnational Influence ÷ 2, round up) + floor(charter_age_seasons / 8)`.
  Privilege hardens into right the longer it stands.
- **Quo Warranto (public contest for old charters).** Revoking a Charter **older than ~16 seasons** is
  not a quiet administrative act but a public **Quo Warranto scene** — a social contest
  (`social_contest_v30 §7`; province faction as institutional authority vs the subnational leader as
  holder) rather than the §3.3 flat Domain Action. On success the charter is revoked, the §3.3
  revocation effects apply (Order −1 in the settlement, Disposition −2), **AND Order −1 additionally in
  every settlement that faction-type manages peninsula-wide** (the London-1683 contagion — every
  chartered holder now fears its own writ). *[This peninsula-wide echo is the one bold stroke here —
  flagged Jordan-vetoable.]*
- **Confirmation-for-fee at transfer/succession.** On a control transfer (§5.3) or a succession where a
  confirmation ceremony is performed (§1.8b), the new/continuing controller may **Confirm** existing
  Charters: **W +1** (the confirmation fine) and, in each chartered settlement so confirmed, **L +1**
  (the §1.8a "privileges confirmed" event). On a §5.3 **Confirm Privileges** transfer this L credit is
  already carried by that section's L *seed* — do not double-apply (see §1.8b composition note).

**Scope discipline.** Refines §3.3's existing grant/revoke effects and the §1.8a "Charter granted"
event; does not create a new player action (Grant/Revoke stays single-homed in the FA lane,
ED-FA-0002) and does not alter the §3.3 Contested-management path. The confirmation-for-fee hinge is
*shared* with §1.8b (succession) and §5.3 (transfer) — those sections govern *which* fires; this one
only supplies the Charter-side W/L effect. Magnitudes (÷8 prescription slope, 16-season Quo Warranto
threshold, peninsula-wide −1) are shape proposals per the cited precedent, not sim-calibrated —
calibrate before canon (CLAUDE.md §5/§7).

### §3.3b Patron-backed privilege lapse — the Za model (NEW — ED-SE-0021, 2026-07-09)

**Status: PROPOSED.** Extends the §3.3a Charter machinery (does not replace it) with a **patron**
field, giving a Charter a second, independent failure mode beyond Quo Warranto. Provenance:
`designs/audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md`
§Step 3 SE-JP3.

**Grounding.** *Za* trade guilds (Heian–Sengoku Japan): merchant and craft-guild monopoly and
toll-exemption rights were legally enforceable specifically *because* a patron institution — a
temple, shrine, or court noble house — backed them. Kitano Tenman-gū sponsored the yeast-brewers'
za; Enryakuji sponsored oil brokers. The privilege was never freestanding; it was only as durable
as its patron's own standing (*Cambridge History of Japan*, vol. 3; Wikipedia, "Za (guilds)").

**Mechanic.** A Guild-managed settlement's Charter (§3.3a) may carry a **patron** field: a named
institution or NPC (a temple, a noble house, a Ministry — per §7) whose own political standing
backs the guild's privileges. If the patron's standing drops below a set threshold (CI loss,
Disposition collapse from a rival's Intrigue action), the Charter's privileges lapse
**automatically** at the next Accounting step — no Quo Warranto contest required, because nobody
revoked anything; the backing simply gave out. A new Intrigue-family card, **"Patron's Rivals
Move,"** fires one season before automatic lapse, giving the guild (and the governor, if they wish
to intervene) a Bargain window — a `Treat` verb spend (`governance_play_redesign_v1.md` §1.3) to
shore up the patron directly. This creates a new attack vector distinct from Quo Warranto:
breaking a guild monopoly can mean targeting the *patron's* standing rather than the guild's
charter.

**Status:** promote-ready — adds one field and one automatic-lapse trigger to the already-PROPOSED
§3.3a machinery; reuses existing Investigate/Treat verbs and the Intrigue card family; no new
player action.

### §3.3c The Seggio Council — hereditary corporate subnational faction (NEW — ED-SE-0024, 2026-07-09)

**Status: PROPOSED.** A new subnational-faction archetype for the §3.3 table, deliberately
structured to sit *outside* the uniform "Management Effect" pattern every other row in that table
shares, and outside the §3.3a Charter/Quo-Warranto system entirely. Composes with §4.5 Local
Actors for its Eletti bloc. Provenance: same docket, §Step 3 IT-7.

**Grounding.** Naples's *Seggi* (five noble seggi plus one popolo seggio), each electing an
*Eletto* to the joint Tribunal of San Lorenzo, held bespoke, non-transferable civic privileges —
one seggio's prerogative over building regulation, another's over water rights, another's over
coinage or market oversight — that did not reduce to a single uniform grant.

**Mechanic.** At Seat/City settlements, the province faction may recognize 1–5 hereditary Seggio
bodies. Each Seggio holds **one bespoke, non-transferable privilege**, instead of the uniform
Management Effect the §3.3 table specifies for other subnational factions — for example: one
Seggio gates the `Develop` verb's Guild-charter funding option in that settlement; another gates
the `Fortify` verb's Militia option; another sole-adjudicates water or market disputes brought by
Local Actors (§4.5), bypassing the governor's own Hold Court authority for that dispute class. All
resident Seggi share a single joint council seat — an **Eletti bloc** — that the governor must
`Treat` (`governance_play_redesign_v1.md` §1.3) with collectively: one Seggio's Disposition swing
ripples across the whole bloc's vote, since they sit and vote together.

Seggio privileges **cannot** be granted or revoked via the standard §3.3 Domain Action or via Quo
Warranto (§3.3a) — they may only be inherited, married into, or seized by force (a conquest- or
coup-adjacent event, not an administrative one). This is the deliberate point of difference from
the Charter system: Seggio privilege is corporate-noble prerogative, not crown-granted license.

**Status:** promote-ready — adds a new Local-Actor/subnational-faction archetype using only
existing schema fields (Knots, Disposition, the §3.3 table's own format); no new resolver, no
roster fork.

---

# PART 4: SETTLEMENT AS GAMESPACE

## §4.1 Scene Slate Settlement Anchoring

Every Scene Slate entry (player_agency_v30 §4.2) is now anchored to a specific settlement, not just a province. When the Slate says "Baralta's aide wants to discuss the treasury crisis," the scene location is S-015 Gransol Parliament, not "T8 Gransol." The player travels to the settlement, not the province.

**Travel within a province:** Moving between settlements in the same province costs no scene action (local travel). Moving between provinces costs 1 scene per province traversed (existing rule, fieldwork_v30 §3.3).

**Settlement-level fieldwork:** All fieldwork actions (investigation, socializing, exploration) operate at settlement level. The Depth Axis applies per settlement — a character who has explored S-015 Gransol Parliament to Depth 3 has not necessarily explored S-017 Gransol Market Quarter at all. Exposure, however, is tracked per province (existing rule — faction surveillance covers the whole territory).

## §4.2 Subnational Faction Visibility

Settlements make subnational factions visible to the player:

| Subnational Faction | Where Visible | How Visible |
|--------------------|--------------|-------------|
| Ministry | Seat and City settlements | Officials in administrative buildings. Bureaucratic delays. Paperwork. The Ministry is the slow grind of institutional governance — the player sees it in settlement administration. |
| Guilds | City, Port, Market, Mine settlements | Merchants, craftsmen, guild halls, trade disputes, labor actions. The Guilds are the economic texture of urban life. |
| Niflhel | Any settlement (covert) | NOT visible unless discovered. The player may notice: unexplained supply chain activity, strangers who arrive and leave without transaction, a locked warehouse in the dock quarter. Investigation can reveal Niflhel presence. |
| RM | Town and Outpost settlements in low-CV territories | Community gatherings, Einhir cultural practices, whispered songs, the old stone circles maintained despite Church disapproval. RM presence is visible in the cultural texture of daily life. |
| Löwenritter | Fortress settlements | Military patrols, knight chapters, weapons training, the tension between martial discipline and political loyalty. The player sees the Löwenritter as a professional military organization operating semi-independently. |
| Wardens | Outpost settlements near Askeheim | Thread practitioners in practical dress. Equipment for Mending. The work — the constant, unglamorous work of holding the Southernmost together. |
| Local Actors | Any settlement | Mayors, magistrates, elders, community leaders who are not affiliated with any national faction. These NPCs have Convictions and Disposition tracks. They represent the population's autonomous political will. |

## §4.3 Settlement Events

Each settlement generates 0–1 local events per season based on its stats and type. These feed into the Scene Slate at Priority 4 (Territorial).

| Condition | Event |
|-----------|-------|
| Prosperity 0 (or other Dearth trigger) | **Dearth** — see §4.3a (SE-2) for the full entitlement-failure triggers and governor response verbs. Baseline: Order −1 automatic; sustained ≥2 seasons → population leaving via §1.8c Weight-as-Exit. |
| Defense 0 + adjacent hostile military | Raid or siege. Mandatory scene if player is present. |
| Order 0 | Local revolt (analogous to province Accord 0 but at settlement scale). Governor expelled unless garrison present. |
| Order 5 + Prosperity 4+ | Flourishing. Local festival, trade fair, or cultural event. +1 Disposition with all local NPCs. Scene opportunity for the player. |
| RM takes control of settlement | **Governance Transition scene** (historical_precedents_analysis §4.3). Player (or Vossen if NPC) chooses: **Disestablishment** (remove existing governance infrastructure; −1 Order for 2 seasons, then Accord growth +0.5/season; PT −1 immediate); **Accommodation** (maintain existing infrastructure under RM oversight; no penalty, PT drops 0.5 only, standard Accord); **Transformation** (4-season gradual conversion; no penalty during transition; PT −1 and Accord +0.5/season after completion). |
| RM-governed settlement, emergency action | **Consensus Delay** (historical_precedents_analysis §3.4). Emergency Domain Actions (Muster, Fortify, Emergency Diplomacy) in RM settlements take +1 season to resolve. Waivable: RM leader spends 1 Mandate + loses 1 Presence marker in that province (community perceives consensus violation). |
| Cathedral type + CV change in province | Religious event: sermon, ceremony, procession, or protest depending on CV direction. |
| Mine type + Prosperity 3+ | Resource surplus. Province Treasury +50/season at Accounting (economic contribution, derived_stats_v1). |
| Fortress type + hostile military in province | Garrison mobilization. Defense check: Defense pool vs Ob 2. Success: settlement holds. Failure: attacker bypasses or captures. |

### §4.3a Dearth chain and granary response (PROPOSED — ED-SE-0008, 2026-07-08)

**Status: PROPOSED, not yet ratified.** Replaces and extends the §4.3 one-line famine row above.
Rides the ED-SE-0001 `governance_play_redesign` ratification track (PROPOSED — pending central ratification, not asserted as a settled basis here). Provenance:
`designs/audit/2026-07-08-fa-se-historical-precedent-research/fa_se_historical_precedent_research_v1.md`
§Step 3 SE-2.

**Grounding.** The moral-economy tradition: **E.P. Thompson 1971** (the crowd's "moral economy" —
dearth riots were not blind hunger but enforcement of a *legitimate price*, and the crowd's target
order was **millers and merchants first, then authority**; *taxation populaire* = the crowd setting a
just price when the governor would not); **James Scott 1976** (the peasant "subsistence ethic" — it is
not dearth as such but the ruler's **invariance under dearth**, taking the standard levy anyway, that
detonates rebellion; remission/relief is the classic legitimacy-purchasing response); **Amartya Sen
1981** (famine as **entitlement failure**, not food unavailability — people starve when they lose the
means to *command* food, even amid supply). Institutional anchors: Rome's *cura annonae* (the grain
dole as a governing obligation); **Will & Wong 1991** on the Ming-Qing *changpingcang* ever-normal
granaries (the state granary as the operative relief instrument); the Tudor **Book of Orders 1587**
(magistrates fixing grain prices in dearth — the Fix Prices verb).

**Trigger (entitlement failure, not weather).** Dearth fires when **any** of: (i) Prosperity 0; (ii) a
grain route to the settlement is cut (§4.3b, SE-3); (iii) a Levy/Extraction fiscal stance (FA-1) is
taken in a settlement already at Prosperity ≤ 1. **Invariance clause** (per Scott): taking the
*standard* levy during an active Dearth counts as **Ignore** below — it is the invariance that
detonates.

**Governor response verbs** (the season's governance action, §3.2, selects one):

| Verb | Requirement | Effect |
|---|---|---|
| **Open Granary** | granary ≥ 1 | granary −1; Dearth relieved; **PS +1** (Scott's remission). Realizes the §1.8a "Dearth relieved" PS event at settlement grain — see reconciliation note. |
| **Fix Prices** | — | Dearth held off one season (*taxation populaire* pre-empted); Order unchanged; Guild/merchant local Disposition −1; black-market emergence check (§4.7). |
| **Requisition** | a neighbor with grain/granary on the adjacency graph | relieves **this** settlement by stripping a neighbor — **displaces** the Dearth to that neighbor next season. |
| **Ignore** (or standard levy taken during Dearth) | — | Order −2; PS −2; riot event targeting **millers/merchants first, then the governor** (Thompson's documented target order made mechanical). |
| **Provision** | costs W (pre-emptive governance/faction action) | granary +1 (build the stock before the crisis). |

**New registry field.** This chain requires a per-settlement `granary: int (0–3)` on the `Settlement`
dataclass in `sim/territory/registry.py`. **[FOLLOW-ON CODE TASK — SE lane, NOT authored in this
doc-only pass: add `granary` to `registry.py`'s `Settlement`; that Python file is not edited from
here.]**

**Reconciliation with §1.8a.** §1.8a lists "Dearth relieved (governance response… SE-2) **+2**" as a
placeholder that *explicitly defers to this rule*. SE-2 now supplies the per-verb PS deltas: the
operative settlement-grain gain for relieving a Dearth is the **response verb's** value (Open Granary
PS +1), and §1.8a's provisional "+2" is read as the **ceiling** on PS gained from resolving a single
Dearth episode, not an additional stacking bonus. No PS is double-counted: **one Dearth episode → one
relief verb → one PS delta (≤ +2).**

**Scope discipline.** Specifies the Dearth trigger and response verbs and names one new registry
field; it does not alter §1.8/§1.8a aggregation, the other §4.3 event rows, or §4.7 black-market rules
(which it references). The grain-route trigger (clause ii) and Fiscal Stance trigger (clause iii) live
in their own docket items (§4.3b / SE-3 and FA-1) and compose with this table when they land. The
*Weight* consequence of sustained Dearth is §1.8c (SE-10). Magnitudes are shape proposals per the
cited moral-economy literature, not sim-calibrated constants — calibrate before canon (CLAUDE.md
§5/§7).

### §4.3b Grain routes and food dependency (PROPOSED — ED-SE-0009, 2026-07-08)

**Status: PROPOSED, not yet ratified.** Gives mechanical teeth to the open `geography_v30` item
**ED-054 / BALANCE-005** ("Hafenmark food dependency has no mechanical teeth — Feldmark unreachable by
Hafenmark"). This is a **rule on top of** the existing settlement-adjacency graph
(`settlement_adjacency_v30` / `valoria_geography_v30.yaml :: settlement_adjacency`), **not** a new
graph spec — it defines no new edges, edge types, or graph file. Provenance: research report §Step 3
SE-3.

**Grounding.** The classical grain-supply politics of dependent cities: **Athens' Black Sea grain
law** (statutory control of the Bosporan route that fed the city — cutting it was an act of war);
**Rome's Egyptian grain fleet** (the *cura annonae*'s strategic face — the *annona* rode on a specific
sea lane); the **Hanseatic Baltic grain trade through Danzig** (highland/urban regions structurally
dependent on breadbasket imports). **Sen 1981** again: a siege or blockade is **entitlement warfare** —
you starve a city by cutting its *command* over food, not by destroying the food.

**Rule (on top of existing adjacency):**

- **Breadbasket sources.** Tag the breadbasket provinces **T5 Feldmark** and **T6 Stillhelm** as grain
  sources (the Feldmark Storehouse sub-feature, §2.2, is the anchor). **Port-type settlements** are
  import sources (sea grain — Schoenland/Altonian imports).
- **Dependency.** Every non-breadbasket settlement needs a **traced route on the existing adjacency
  graph** to a grain source or a Port.
- **Route-tracing granularity.** **Per-province by default** (a province is fed if any of its
  settlements can trace to a source) — flagged inline as the *one* open design decision (per-province
  vs per-settlement); per-province chosen for tractability and to reuse the existing graph without new
  per-edge machinery.
- **Cut route → Dearth.** A route cut by **occupation, blockade, or siege of a waypoint** settlement on
  the traced path puts every dependent settlement **one season from Dearth** (§4.3a, SE-2). This makes
  Hafenmark's highland/mining provinces structurally grain-dependent through the T8↔T9↔T2 corridor (or
  Schoenland Port imports) — so the **dependency itself is the mechanic**, closing the "Feldmark
  unreachable by Hafenmark" complaint by making unreachability *bite* rather than by editing adjacency.

**Scope discipline.** Reuses only the existing settlement-adjacency graph (`settlement_adjacency_v30`;
the 49-edge block in `valoria_geography_v30.yaml`). Its sole output is a Dearth trigger consumed by
§4.3a (clause ii). The per-province tracing default is the one flagged decision; if a later pass
chooses per-settlement, only the *granularity* changes, not the rule. Geography's ED-054/BALANCE-005 is
the open item this closes; the actual source-tagging of T5/T6 in the geography YAML is a follow-on data
task in the geography/world lane, not authored here. Magnitudes (one-season-from-Dearth) are shape
proposals per the cited precedent — calibrate before canon (CLAUDE.md §5/§7).

### §4.4 Thread Operations at Settlement Level (Throughline T1)

Thread operations at Relational scale or above performed within a settlement produce settlement-level consequences alongside province-level MS effects. Cap: ±1 per settlement stat per season from Thread operations.

| Operation (Relational+ scale) | Settlement Effect on Success | Settlement Effect on Failure |
|-------------------------------|-----------------------------|-----------------------------|
| Weaving | Order +1 (social configurations stabilize) | No settlement effect |
| Pulling | No positive effect | Order −1 (co-movement disrupts local configurations) |
| Past-Oriented Pulling | No positive effect | Prosperity −1 (paradox window disrupts routine) |
| Dissolution | No positive effect | Defense −1 AND Order −1 (substrate torn, structures weaken) |
| Mending | Prosperity +1 (substrate coherence restored, infrastructure strengthens) | No settlement effect |
| Community Organizing | Order +1 AND Prosperity +1 (if PT ≤ 2 in province) | No settlement effect |
| Lock | Defense +1 (configuration becomes architecturally permanent) | No settlement effect |

Object/Personal scale operations: no settlement effect (scale too small).

### §4.5 Local Actors (Throughline T7)

Each settlement generates 1–2 Local Actors — lightweight non-faction NPCs representing the population.

**Profile:** Name (culture-derived), Role (Elder/Magistrate/Merchant/Priest/Artisan/Farmer/Fisher/Miner/Scholar/Healer), one Conviction, Disposition (starting +1 toward governor, 0 toward all others).

**Count by type:** Seat: 2. City: 2. Town: 1. Fortress: 1. Port: 2. Cathedral: 1. Mine: 1. Outpost: 0. Total: ~45–50 across 36 settlements.

**Functions:** Generate Priority 5 Scene Slate entries. Provide free Settled-depth (Depth 1) information. Serve as governance feedback (their Disposition reflects population satisfaction). Recruitment pool for faction emergence (Stage 2→3 at Disposition +3).

**Disposition drivers:** Player governs, Order improves: +1. Order declines: −1. Sponsor event: +1. Public combat in settlement: −2. Defend settlement from invasion: +2. Settlement changes controller: reset to 0. Player fulfills Conviction relevant to settlement: +1.

---

# PART 5: MILITARY GRANULARITY



### §4.7 Black Markets (Niflhel Dissolution — conflict_architecture_proposal)

Any settlement with Order ≤ 1 or no governor develops a black market. Systemic consequence of governance failure.

**Emergence:** Automatic when settlement Order ≤ 1 OR settlement has no governor.
**Disappearance:** Automatic when settlement Order ≥ 3.
**Effects:**
- Settlement Wealth +0.5 (illicit trade is still trade).
- Settlement Accord −0.5 (population distrusts lawless governance).

### §4.8 Intelligence Brokers (Niflhel Dissolution — conflict_architecture_proposal)

Individual NPCs in specific settlements who sell information. Not coordinated — each operates independently for personal profit.

**Discovery:** Discoverable through Tribune or Riskbreaker actions.
**Capabilities:** Sell faction intelligence; fabricate intel when peace reduces demand (Ems Dispatch pattern); can be killed, bought out, or turned.
**Placement:** One broker per settlement with Prosperity ≥ 3 and no governor or governor Stability ≤ 2. Named NPCs with Dispositions.

### §4.9 Thread Exploitation Sites (Niflhel Dissolution — conflict_architecture_proposal)

Settlements at Thread Proximity ≤ 2 where Thread residue accumulates naturally. Location-based phenomenon.

**Emergence:** Any settlement with Thread Proximity ≤ 2.
**Harvesting:** Any faction/actor who discovers the site can harvest. RS −0.5 per harvest per season. Wealth +1 for harvesting faction.
**Discovery:** Requires fieldwork (Investigation action). Thread Proximity not public until RS visibility thresholds (threadwork_v30 §5.6).

---

## §5.1 Invasion and Defense

Invading a province now requires capturing (or bypassing) its settlements. The Seat is the strategic objective — capturing the Seat grants provincial control. Other settlements may be captured, bypassed, or besieged independently.

**Capture sequence:** An invading army entering a province must choose which settlement to attack first. Adjacent settlements within the province are connected by the internal road network. The invader moves through settlements in sequence unless they bypass.

| Action | Requirement | Effect |
|--------|------------|--------|
| Assault | Military vs Defense + garrison | Success: settlement captured. Failure: attacker repelled, takes casualties. |
| Siege | Military ≥ Defense | No immediate roll. Each season: defender Order −1 (starvation/pressure). When Order = 0, settlement surrenders. Attacker cannot move to other settlements while besieging. |
| Bypass | Military > Defense by 2+ | Attacker moves past the settlement to the next one. Bypassed settlement remains hostile — its garrison can attack the invader's supply line (Military vs Ob 1 each season: success = invader takes −1 Discipline on all units in the province). |

**Province capture:** When the Seat is captured, provincial control transfers to the invader. Non-Seat settlements with Order ≥ 3 may resist (maintaining their current governor). The invader must reduce each resistant settlement individually or grant them autonomy (subnational management) to avoid further conflict.

**Fortress as chokepoint:** A Fortress settlement in the invader's path forces engagement — it cannot be bypassed unless the invader's Military exceeds the Fortress Defense by 3+. Lowenskyst Fortress (S-006, Defense 4) requires Military 7+ to bypass — effectively impossible for most armies. This is the design's intended function.

**Surrender on Terms vs Storm at conquest (FA-6, PROPOSED — jointly owned with the faction_action.py lane, ED-FA-0013, 2026-07-08):**

**Status: PROPOSED, not yet ratified.** This section specifies the **rule** (the settlement-side
distinction between the two conquest branches); the code implementing it — **including which branch the
attacking faction's AI selects** — is owned by the FA lane (`sim/provincial/faction_action.py::_try_conquest`)
and is **NOT** specified here. Provenance:
`designs/audit/2026-07-08-fa-se-historical-precedent-research/fa_se_historical_precedent_research_v1.md`
§Step 3 FA-6.

**Grounding.** Hugo Grotius, *De iure belli ac pacis* (1625), **Book III** — the law of war
distinguished a garrison that **surrendered on terms** from one that **forced a storm**. The
early-modern siege convention (**Parker 1994**): once the attacker had opened a **practicable breach**
and the garrison beat the *chamade*, a garrison that surrendered received the **honors of war** (marched
out with arms, colors, safe conduct); a garrison that instead forced the assault **forfeited that
protection**, and by the brutal custom the storming troops were entitled to sack. The **Sack of
Magdeburg 1631** (and Rome 1527) is the anchor for why Storm is costlier than its local damage suggests:
atrocity was cheap *locally* but ruinous *reputationally* — a legitimacy contagion across every other
town watching.

On attacker victory, two branches:

- **(a) Accept surrender on terms** — available **only when the defender is NOT routed** (battle degree
  **Success, not Overwhelming**; and the siege-to-Order-0 capitulation path, §5.1 Siege, takes this
  branch **by construction** — siege is the legitimacy-preserving slow road, consistent with
  ED-SETT-04). Effects: the **lighter Accord penalty**; the settlement's **L seeds low-but-nonzero** via
  §5.3 Entry Terms (the new controller still chooses Confirm vs Impose, but "on terms" surrender makes
  **Confirm** available and keeps Prosperity intact); the **defender garrison is partially preserved**
  (marches out — honors of war).
- **(b) Storm** — **always available**. Effects: the current, **harsher Accord penalty** of the existing
  §5.1 Assault/capture baseline, plus battle damage to the settlement.

**Which branch the attacking faction's AI picks (Terms vs Storm) is a code-side decision owned by the
`faction_action.py` lane, not specified here.** Exact numeric magnitudes (Accord deltas, the L seed
value, the garrison-preservation fraction) are specified by the ED-FA-0013 ledger/report shape and
implemented in that lane — this section specifies only that the two branches **exist**, that (a) is
available only on a non-Overwhelming result, and that (a) is lighter on Accord/L/garrison while (b) is
the harsher current path. *(A third branch — post-Storm **Sack**, the Magdeburg reputational-contagion
effect — is flagged `needs_jordan` in ED-FA-0013 and is deliberately NOT authored here.)* Composes with
§5.3 Entry Terms (the transfer-boundary L seed) and `faction_layer §2.3`'s existing Accord-on-transfer
table (the Order-side effect), neither of which it replaces.

## §5.2 Garrison and Defense

Each settlement can host a garrison (one military unit). The garrison's stats (from military_layer_v30) add to the settlement's Defense for the purpose of Assault checks: effective Defense = settlement Defense + garrison Discipline.

Ungarrisoned settlements with Defense 0 are auto-captured on any hostile military entry — no roll needed. This makes Towns and Outposts vulnerable unless garrisoned, while Fortresses can hold independently.

## §5.3 Entry Terms at control transfer (PROPOSED — ED-SE-0011, 2026-07-08)

**Status: PROPOSED, not yet ratified.** New subsection. Supplies the **transfer-boundary L seeding
rule** that LPS-2e (§1.8) never specified — §1.8/§1.8a seed L/PS only at *game start*
(`faction_state_authoring §8`) and drift them thereafter, but nothing seeds L when a settlement
changes hands mid-campaign. **Composes with (does NOT replace)** `faction_layer §2.3`'s existing
Accord-on-transfer table, which remains the **Order-side** effect; this adds the **L-side**. Provenance:
`designs/audit/2026-07-08-fa-se-historical-precedent-research/fa_se_historical_precedent_research_v1.md`
§Step 3 SE-5.

**Grounding.** The **Joyeuse Entrée of Brabant 1356** — the new duke's "Joyous Entry" was a *sworn
confirmation of the towns' privileges* as the price of their obedience (conditional allegiance,
ceremonially entered); **Henry I's coronation charter 1100** (a new ruler buys legitimacy by confirming
the realm's liberties at the moment of taking power); universal accession-confirmation practice. The
opposite pole is **Mancur Olson 1993** (the "roving bandit" who strips rather than confirms — Impose
Administration is roving-bandit pricing: maximal short-term extraction, no legitimacy investment).

**Trigger.** Fires on **every settlement control transfer** — conquest (FA-6 branches (a) and (b),
§5.1), treaty cession, or seizure. The new controller chooses **one fork per settlement**:

| Fork | Charter/Precedent tags | L seed | Fiscal stance | Other |
|---|---|---|---|---|
| **Confirm Privileges** (Joyeuse Entrée) | **kept** (§3.3a) | **L seeds 3** | capped at Standard for 4 seasons | legitimacy-buying path; Prosperity/PS intact |
| **Impose Administration** | **stripped** | **L seeds 1** | no cap | Order −1 (roving-bandit pricing, Olson 1993) |

**Composition (reconciles with §1.8b, §3.3a, §5.1):**

- **Transfer vs succession.** A control **transfer** (controlling *faction* changes) is governed
  **here** (Entry Terms *seeds* L); a **succession** (same faction, *leadership* changes) is governed by
  **§1.8b**. A single control event is **exactly one** of these — the two never both fire on one
  settlement in one season, so an Entry-Terms seed and a succession drift never stack.
- **Seed, not increment.** On transfer L is **seeded** (set to 3 or 1), not incremented. The §1.8a
  "privileges confirmed +1" L-channel event is the **succession-with-ceremony** case (§1.8b); it does
  **NOT** additionally apply on top of a Confirm-Privileges transfer (the seed of 3 already carries the
  confirmation credit). See the §1.8b composition note.
- **FA-6 linkage.** A branch-(a) "surrender on terms" conquest (§5.1) makes **Confirm Privileges** the
  natural fork and keeps Prosperity intact; a branch-(b) **Storm** does not preclude Confirm but pairs
  with the harsher Accord penalty. Which the AI picks is the FA lane's call (§5.1 note).
- **Charter interaction.** **Confirm Privileges** keeps Charter tags (§3.3a) and enables
  confirmation-for-fee (W +1; the §3.3a **L +1 is subsumed by the seed** on a Confirm transfer — do
  **not** add it on top of the seed of 3, per the "Seed, not increment" bullet above and §3.3a line
  ~627); **Impose Administration** strips
  them — a revocation-by-conquest *without* the §3.3a Quo Warranto contest (the tags simply do not
  survive an Impose).

**Scope discipline.** Adds the L-side of a control transfer and composes with the Order-side
(`faction_layer §2.3`) and the succession-side (§1.8b); it does not alter the Accord table, the §1.8
aggregation, or the FA lane's conquest resolution. Magnitudes (L 3 / L 1, 4-season Standard cap) are
shape proposals per the cited precedent, not sim-calibrated — calibrate before canon (CLAUDE.md §5/§7).

---

# PART 6: PLAYER PROGRESSION — SETTLEMENT TO NATIONAL

## §6.1 The Stature Ladder (Canonical — referenced by player_agency_v30 §5.4)

The existing Standing track (0–5 per faction) and Renown track (0–10 cross-faction) from player_agency_v30 now map to a concrete progression of governance scope:

| Renown | Standing | Governance Scope | ROTK Parallel | CK3 Parallel |
|--------|----------|-----------------|---------------|-------------|
| 0–2 | 0–2 | None. Operative/Agent. Personal actions only. | Officer without assignment | Unlanded courtier |
| 3–4 | 3 | **Settlement Governor.** Manage one Town/Outpost. Free governance action per season. | City governor | Baron |
| 5–6 | 4 | **Multi-Settlement.** Manage up to 3 settlements. May hold settlements across provinces (with faction permission). Province-level influence. | Provincial governor | Count |
| 7–8 | 4–5 | **Provincial Authority.** De facto province controller. Independent Domain Actions via Renown pool. May challenge for formal leadership. | Viceroy | Duke |
| 9–10 | 5 | **National Actor.** Found a new faction or take over existing one. Control provinces directly. Issue Domain Actions. Participate in Parliament. Full parity with Crown, Hafenmark, Varfell, Church. | Independent warlord / Emperor | King |

## §6.2 Faction Emergence — Local to National

A player (or NPC actor like RM) can build a faction from the ground up:

**Stage 1 — Cell (Renown 0–2):** Personal network. Companions and Knots. No institutional structure. No settlements. The player exists at the mercy of existing factions.

**Stage 2 — Organization (Renown 3–4):** Assigned to or seize a settlement. Begin developing it. Recruit local NPCs. The player is visible as a local authority figure. The subnational faction begins to exist — it has one settlement, one governor (the player), and an implicit claim to local autonomy.

**Stage 3 — Movement (Renown 5–6):** Multiple settlements. Cross-settlement coordination. The player's organization has Influence and maybe Wealth as faction stats (partial sheet — like RM or early Löwenritter). The organization can participate in local politics but cannot issue national-level Domain Actions.

**Stage 4 — Faction (Renown 7–8):** Provincial authority. The organization controls enough settlements to claim a province. It now has a full faction stat sheet (Mandate, Influence, Wealth, Military, Stability). It can issue Domain Actions, participate in Parliament, enter treaties. It is a national-level faction — one of the powers on the peninsula.

**Stage 5 — Hegemon (Renown 9–10):** Multiple provinces. The player's faction competes with Crown, Hafenmark, Varfell, Church for peninsular sovereignty. Victory conditions apply. The player has risen from nobody to contender through accumulated deeds, not scripted events.

**Emergence requirements per stage:**

| Stage | Requirements |
|-------|-------------|
| 2 → 3 | Control 2+ settlements. Renown 5+. At least 2 NPC officers with Disposition +3. |
| 3 → 4 | Control 4+ settlements across 2+ provinces. Renown 7+. Declare faction formally (Domain Action: Influence pool = Renown ÷ 2, Ob 3). At least 1 province Seat controlled. |
| 4 → 5 | Control 2+ province Seats. Renown 9+. Full faction stat sheet. Participate in Parliament or equivalent political body. |

### Founded Faction Starting Stats (ED-790)

When a faction emerges at Stage 4 (Faction Declaration), it receives the following starting stat sheet:

| Stat | Starting Value | Rationale |
|------|----------------|-----------|
| Legitimacy (L) | 2 | Limited institutional recognition — newly-declared faction. Advances via Mandate Recovery (+1/season when no hostile DAs target and Stability ≥ 2) and Conviction fulfillment by founder. |
| Popular Support (PS) | 3 | Grass-roots base anchored by founding NPC officers. |
| Influence (I) | floor(Renown ÷ 2) at Declaration | Carries the Declaration roll pool forward as institutional capacity. |
| Wealth (W) | 2 + (# settlements controlled − 1), capped at 5 | Founding economic base plus per-settlement scaling. |
| Military (Mil) | 1 | Militia only at founding; no standing army. Recruits from settlement Order. |
| Intel (Int) | 2 | Informal network from organizing phase. |
| Stability (Sta) | 3 | Loyal officers from Stage 2-3 work; stable orgs. |

Faction stats advance from these baselines via standard Domain Actions and recovery mechanics. The founding faction is institutionally weak (L 2, Mil 1) but politically nimble — the asymmetry mirrors RM and early Löwenritter as canonical examples.

## §6.3 Faction Collapse — National to Local

When a national-level faction loses all its provinces, it does not vanish. It contracts.

**Collapse sequence:**

1. **Province lost:** Faction loses control of a province. Settlements in that province with governors loyal to the collapsing faction may resist the new controller (Order ≥ 3 + governor Disposition ≥ +3 toward the faction). These become holdout settlements.

2. **Last province lost:** The faction has no provinces. But if the faction leader (NPC or player) is alive and located in a settlement they personally control (typically their capital Seat), the faction survives as a **city-state** — a subnational faction controlling one or more settlements without provincial authority.

3. **City-state mechanics:** A city-state faction has a partial stat sheet (Influence, Wealth, Stability — no Mandate, no Military unless garrisoned). It cannot issue national-level Domain Actions but can: defend its settlements, trade, form alliances, participate in subnational politics, and work toward re-emergence via the Stage 2→4 pathway above.

4. **Full collapse:** If the faction leader is killed or captured and no successor exists with Standing 4+, the faction dissolves. Its remaining settlements become unmanaged (NPC governors revert to local actors with no faction affiliation). Its officers become free agents eligible for recruitment by other factions.

**Examples:**

- **Hafenmark falls:** Baralta loses T7, T10, T17 to military conquest. She retreats to S-015 Gransol Parliament with loyal officers. Hafenmark becomes a city-state: Baralta controls Gransol's 3 settlements, retains Parliament as a political institution (even if diminished), and can negotiate from a position of reduced but not eliminated power. She retains Influence 4, Wealth 3 (trade revenue from Gransol Harbor), Stability 3. She is the Duchess of Gransol, not the Duchess of Hafenmark. She can rebuild.

- **Crown collapses via Coup:** Löwenritter Coup fires. Almud is exiled. Crown provinces transfer to Löwenritter control. But Almud escapes to S-010 Stillhelm with Torben and loyal Crown officers. Crown becomes a city-state: Almud controls Stillhelm and possibly Feldmark settlements. The Crown's legitimacy claim persists — Almud is still the King, just a king without a kingdom. He can attempt restoration.

- **Church loses Himmelenger:** Varfell or RM conquers T9. But Church retains S-003 Valorsplatz Cathedral (Church management in Crown territory) and S-023 through S-025 may resist if Order is high enough. The Church's institutional authority transcends territory — it has cathedrals in other provinces. The Church contracts but does not collapse.

---

# PART 7: EXTENDED TIMELINE

## §7.1 Clock Recalibration for 10–30 Year Games

The existing clocks assume a 13–15 year game. With settlements adding governance granularity and the faction emergence pathway adding a bottom-up progression, games may last 20–30 years. Clocks must be recalibrated.

| Clock | Current Rate | Recalibrated Rate | Rationale |
|-------|-------------|-------------------|-----------|
| MS decay | −1/year baseline | −1/year baseline (unchanged) | MS is an existential pressure. 72 → 0 in 72 years without intervention. 30-year game = MS ~42 at game end (Fragile band). This is correct — long games should reach deep Calamity effects. |
| CI (Church Influence) | Passive +1/season | Passive +1/season if Church Mandate ≥ 3 (existing conditional). 28 start. | 30-year game = 120 seasons. CI caps at 75 (phase transition), so the real question is: when does 75 fire? At +1/season: ~47 seasons (~12 years). This is correct — Church pressure should peak in mid-game. |
| IP (Invasion Pressure) | +1/season baseline | +1/2 seasons baseline (halved) | Current rate: 20 start, 100 in 80 seasons (20 years). This is too fast for a 30-year game — invasion would fire before the player completes the settlement→national progression. Halved rate: 100 in 160 seasons (40 years). 30-year game: IP ~80 (Altonian preparation, not yet invasion). Invasion fires only if events accelerate IP. |
| Political Stability | 0 start, +1 per violence event | Unchanged | Cumulative. Self-regulating via victory gate (≤ 6). |

**New clock: Generational Shift (0–10).**

A 30-year game spans a generation. The first leaders (Almud, Baralta, Vaynard, Himlensendt) will age, weaken, and potentially die of natural causes. Generational Shift tracks this.

- Rate: +1 per 5 years of game time.
- Threshold 2 (Year 10): First generation leaders begin showing age. All original faction leaders: −1 to their highest attribute (age penalty). Succession planning becomes relevant. **Exception:** Characters (NPC or PC) with Thread Sensitivity ≥ 50 are exempt — the rendering sustains high-TS beings more robustly (metaphysical justification per P-15).
- Threshold 4 (Year 20): Second generation leaders emerge. Original leaders who have not been replaced are at −2 to highest attribute. NPC arc branches for retirement, abdication, or natural death activate.
- Threshold 6 (Year 30): Original leaders who survive are elderly. −3 to highest attribute. The game's political landscape has fundamentally shifted — the players' generation IS the leadership class, whether they sought it or not.

**[Annotation — CP-2, ED-SE-0017, PROPOSED, 2026-07-08]** The Generational Shift clock's "founding
leaders age, weaken, and their solidarity decays" logic is the game-mechanical shadow of **Ibn Khaldun's
*asabiyyah* cycle** (*Muqaddimah*, 1377): group solidarity (*asabiyyah*) is strongest in the founding
generation that won power through shared hardship, and decays predictably by the **third-to-fourth
generation** as the dynasty urbanizes and softens into sedentary luxury — the classical theory of
exactly the generational decay these Thresholds 2/4/6 hand-wave (the three-to-four-generation span
maps onto the Year-10/20/30 thresholds). *[The optional founder-solidarity Sta +1 that would expire at
Threshold 2 — a numeric/tone call — is `needs_jordan` (ED-SE-0017) and is deliberately NOT implemented
here; this is a grounding annotation only.]*

## §7.2 Succession System (Extended)

**Settlement succession:** When a settlement governor dies, is removed, or departs, the province faction must assign a new governor. If no eligible NPC or player is available, the settlement becomes unmanaged (Order −1 per season until a governor is assigned).

**Province succession:** Existing rules (npc_behavior_v30 §5.2 arc profiles) cover faction leader succession. Extended: if the heir is a player character, the player receives the province with all settlements and their current states. If the heir is an NPC, the NPC becomes the faction leader and the player's Standing is preserved. **Settlement-L effect of a leader succession is specified in §1.8b (ED-SE-0012, PROPOSED):** a `normal` succession leaves held-settlement L unchanged (the corporate crown never dies); `contested/emergency/imposed` modes apply L −1 in all held settlements plus a Regency check (FA-7). A control *transfer* to a different faction is a distinct event governed by §5.3 Entry Terms, not by these succession rules.

**Cross-generational play:** In a 30-year game, the player character may age and retire. If the player has a protégé (a named NPC companion or officer with Disposition +4 and Standing 4+), the player may transfer their governance to the protégé and create a new character — starting at Standing 0 but inheriting Renown ÷ 2 (round down) from their predecessor's reputation. The predecessor becomes an NPC. This is CK3's heir system applied to TTRPG.

---

# PART 8: SYSTEM IMPACT ASSESSMENT

## §8.1 Changes to Existing Systems

| System | Impact | Severity |
|--------|--------|----------|
| S03 Geography | Province map unchanged. Settlement layer added beneath. Adjacency within provinces defined per §2.1. | Moderate — additive, not disruptive |
| S04 Clocks | IP recalibrated (halved baseline). Generational Shift clock added. All other clocks unchanged. | Low — one rate change, one new clock |
| S06 Faction Layer | Provincial Authority slot formalized. Subnational management rights added. Domain Actions unchanged — they still operate at province level. | Moderate — new governance mechanics |
| S07 Victory | Province Accord now derived from settlement Order averages. TCV unchanged. Universal victory still requires Accord ≥ 2 in all provinces. The pathway to Accord ≥ 2 is now through settlement governance. | Moderate — Accord derivation changed |
| S09 Military | Garrison at settlement level. Invasion sequence through settlements. Fortress chokepoints. Unit deployment now specifies settlement, not just province. | Significant — military granularity increased |
| S10 NPC | Settlement governors are NPCs with Stance Triangles. Local actors added as new NPC category. NPC Outreach now settlement-anchored. | Moderate — more NPCs, same system |
| S14 Fieldwork | Fieldwork anchored to settlements. Depth Axis per settlement. Exposure per province (unchanged). | Low — reframing, not redesign |
| S15 Mass Combat | Settlement Defense as pre-battle condition. Siege mechanics added. Fortress bypass rules. | Moderate — new assault/siege layer |
| S17 Scale Transitions | Settlement governance action as new Zoom In entry point. Governor → Province → National as Domain Echo chain. | Moderate — new scale level |
| Player Agency | Governor as Duty. Settlement governance as scene action. Stature ladder revised with governance scope. | Moderate — Renown thresholds now map to settlement control |
| Companions | Companions can serve as settlement governors (dual role). Companion officer from mass combat can govern the settlement their unit is garrisoned in. | Low — extension of existing |

## §8.2 What Does NOT Change

- Province-level mechanics (Domain Actions, faction stats, Parliamentary votes) operate at province level. Settlements add granularity beneath but do not replace the province layer.
- Personal-scale mechanics (combat, contests, Thread operations, fieldwork actions) operate at individual level. Settlements provide the location where these actions occur but do not modify their mechanics.
- The dice engine, pool construction, Ob system, and degree table are unchanged.
- NPC Stance Triangles, Resonant Styles, Conviction Scars — unchanged.
- Clock pressures (MS, CI, IP) — unchanged in function, only IP rate adjusted.
- Calamity radiation — operates at province level per node distance. Settlements within a province share the same radiation band.

---

### §4.6 Settlement POI Templates (Throughline T3)

Each settlement has 2–4 POIs across Depth levels, authored per settlement type.

| Type | Depth 0 (Surface) | Depth 1 (Settled) | Depth 2 (Hidden) | Depth 3+ (Buried/Liminal) |
|------|-------------------|-------------------|-------------------|--------------------------|
| Seat | Court, public buildings | Administrative archives, court records | Private chambers, secret passages, intelligence archives | Thread-locked vault, hidden foundations |
| City | Market square, artisan quarters | Guild halls, merchant ledgers | Smuggling routes, underground economy | Einhir-era foundations, Thread scars |
| Town | Village square, inn | Elder's records, family histories | Concealed caches, factional safe houses | Remnant sites, oral Thread memory |
| Fortress | Battlements, armory | Command archives, prisoner records | Secret sally ports, covert comms | Pre-Catastrophe fortification, Locked configurations |
| Port | Docks, warehouses | Shipping manifests, harbor records | Smuggling networks, Niflhel supply nodes | Submerged Einhir harbor, maritime Thread signatures |
| Cathedral | Nave, clergy quarters | Church archives, theological records | Hidden reliquaries, pre-Solmundic architecture, Inquisition files | Thread-locked artifacts, cathedral as Thread anchor |
| Mine | Mine entrance, worker housing | Geological surveys, production records | Collapsed tunnels with artifacts | Einhir excavation sites, substrate exposure |
| Outpost | Observation post | Patrol logs, environmental readings | Thread monitoring equipment, knowledge caches | Active Thread phenomena, Gap proximity |

**Named narrative-critical POIs:** See throughline_specifications §T3.3 for 7 campaign-defining POIs including the Sealed Codex (Himmelenger), Foundation Stones (Valorsplatz Cathedral), and the Wound Core (Askeheim).

# PART 9: OPEN ITEMS

<!-- Updated 2026-04-19 PP-668 — PP-667 resolutions propagated. See designs/audit/gap_resolution_2026-04-19.md §2.1 -->

| ID | Description | Status (PP-667) |
|----|-------------|-----------------|
| ED-SETT-01 | Settlement starting Prosperity/Defense/Order values need simulation. | **DEFERRED** to engine_v4 smoke-test. Values stand PROVISIONAL. |
| ED-SETT-02 | Settlement governance action pool/Ob calibration. | **DEFERRED** — proposed pool = governor's primary stat; Ob 2 standard / 3 recovery / 4 crisis. Calibration pending smoke-test. |
| ED-SETT-03 | Province Accord derivation edge cases. | **RESOLVED** — single-settlement: Accord = that settlement's Order. Multi-settlement: floor-average; ties broken by Seat getting +1 weight. |
| ED-SETT-04 | Siege duration 4 seasons for Order 4 Fortress. | **RESOLVED** — 4 seasons intended. Siege is slow politico-economic collapse; Assault is the fast path. |
| ED-SETT-05 | Subnational management sovereignty conflict. | **CONFIRMED** — resolved by existing §3.3 Contested management (social contest). |
| ED-SETT-06 | NPC governor priority tree. | **RESOLVED** — settlement-specific (Pacify → Develop → Fortify → Administer); faction-tree override at Stability ≤ 2. |
| ED-SETT-07 | Generational Shift applies to PCs. | **RESOLVED** — yes. Encourages cross-generational play. |
| ED-SETT-08 | Settlement intra-province adjacency. | **SUPERSEDED** by PP-666 `settlement_adjacency_v30` — adjacency is now graph-defined. |
| ED-SETT-09 | Board game physical representation. | **N/A** — videogame-only per project scope. BG physical excluded. |

---

# PART 10: PROPAGATION MAP

| File | Change Required |
|------|----------------|
| designs/setting/geography_v30.md | Add settlement registry. Province map unchanged. |
| designs/board_game/peninsular_strain_v1.md | §2 Accord derivation changed to settlement Order average. §2.3/2.4 Accord change rules now target settlement Order. |
| designs/board_game/faction_layer_v30.md | Add Provincial Authority and Settlement Governor authority slots. Add subnational management grants. |
| designs/board_game/military_layer_v30.md | Add garrison at settlement level. Add Assault/Siege/Bypass mechanics. |
| designs/board_game/victory_v30.md | Verify Accord ≥ 2 still functional with settlement-derived Accord. |
| designs/systems/player_agency_v30.md | §5 Stature ladder revised with governance scope. Governor Duty type added. |
| designs/systems/npc_behavior_v30.md | Settlement governor NPCs. Local actor NPCs. NPC Outreach anchored to settlements. |
| designs/systems/clock_registry_v30.md | IP rate change. Generational Shift clock added. Settlement Order tracked. |
| designs/mass_combat/mass_battle_v30.md | Settlement Defense as pre-battle condition. Siege mechanics. Fortress rules. |
| designs/hybrid/scale_transitions_v30.md | Settlement governance as new scale level. Governor→Province→National Domain Echo chain. |
| designs/systems/companion_specification_v30.md | Companion as settlement governor (dual role). |
| designs/fieldwork/fieldwork_v30.md | Scene location anchored to settlement. Depth Axis per settlement. |
| references/canonical_sources.yaml | New entry: settlement_layer |
| designs/setting/calamity_radiation_v30.md | Confirm province-level operation (no change needed). |

---

*End of document.*