# Part 45 — Hidden Long-Fuse Environmental Stats

## Status: PROPOSED — needs a granularity ruling

**Source.** `designs/audit/2026-07-10-historical-concerns-action-catalogue/historical_concerns_action_catalogue_v1.md` §2.5 (Flood, drought, siltation, resource-geography shifts), cross-referenced against §2.4 (Earthquake, eruption, terrain-altering events) and §2.6 (Famine and multi-year crop failure). Filed 2026-07-10, Lane IN, read-only research pass. **None of the stats below are ratified canon** — they are the catalogue's proposed mechanism for the §2.5 through-line: *"slow hidden stats … are long fuses — an engineering/extraction method choice at one node silently changes another node's Crisis odds seasons later."*

---

## 0. Read this before anything else — the abstraction caveat

**Jordan's standing ruling is that food-supply and similar granular resource meters can ABSTRACT to Prosperity rather than requiring dedicated tracked stats.** That ruling is not overridden by anything below. This Part is not a proposal to add eight new tracked numbers to every settlement sheet; it is a catalogue of *what a depth layer would look like if one is wanted*, organized so each stat can be evaluated independently against the abstraction default.

Concretely, this means the default assumption for every stat in §2 is: **"folds into Prosperity/Order drift, no dedicated tracker, no dedicated card family."** Only promote a stat off that default where the catalogue's evidence shows the abstraction genuinely loses something the design needs — asymmetric information between settlements, a multi-decade fuse that a single Prosperity number can't carry, or a distinct institutional counter-play that wouldn't make sense as a generic Prosperity-boosting Sponsor. §3 makes that call per stat, but it is a **recommendation for a follow-up authoring pass to ratify or reject, not a decision already made.**

The core design tension the catalogue itself surfaces (§2.5's framing, quoted above) is that the *interesting* mechanical idea — a Fortify/Develop choice at one settlement silently loading a Crisis at a **different, downstream** settlement, invisible to that settlement's own governor — is structurally incompatible with full abstraction-to-Prosperity, because Prosperity is a **local** stat and the whole point of several of these fuses (Yellow River siltation → downstream RisingWaterLevel; Fens reclamation → downstream SubsidenceRisk) is that they are **not local** to the settlement whose action caused them. An abstract-to-Prosperity treatment can preserve the *within-settlement* slow-fuse texture (SiltLevel silting your own harbor, SalinityLevel salting your own farmland) but cannot represent the *cross-settlement* fuse without some tracked handoff mechanism. That's the crux of the granularity ruling this Part is asking for.

---

## 1. Depth-layer decision framework

Before the per-stat catalogue, the three questions a "track explicitly vs. abstract to Prosperity" call should answer for each stat:

| Question | If yes → lean toward tracking | If no → lean toward abstraction |
|---|---|---|
| **Is the fuse cross-settlement?** (Does node A's action change node B's Crisis odds, where B has no visibility into A's choice?) | Track (a Prosperity number can't carry information between settlements) | Abstract |
| **Is the fuse multi-decade / multi-generation?** (Does the effect outlive the governor who caused it, in a way a single-season Prosperity delta would wash out?) | Track (or at minimum a durable Precedent/tag, not a raw meter) | Abstract into a one-time Prosperity-ceiling adjustment |
| **Does the institutional counter-play need a legible number to gate on?** (Does "Water Board," "Ever-Normal Granary," etc. need a threshold to check against, or can it just be a flat Fortify/Develop method that nudges Prosperity trajectory?) | Track (the institution's entire premise is reading a gauge) | Abstract — model the institution as a Prosperity-stabilizing Sponsor/Fortify method with no separate meter behind it |

Applying this framework below, per stat, in §3.

---

## 2. The catalogue of proposed stats

Format per stat: **What it tracks** · **Raises it** · **Lowers it / defused by** · **Crisis it fuses toward** · **Standing institution/action that defuses it** · **Historical grounding**.

### 2.1 SiltLevel

| Field | Detail |
|---|---|
| **What it tracks** | Accumulated sediment buildup in a harbor, canal, or river channel serving (or threatening) a settlement. |
| **Raises it** | No standing Dredge/Scour investment over consecutive seasons; upstream engineering choices at a *different* settlement (canal-narrowing, dike-raising) that solve that settlement's throughput problem by displacing sediment/flow downstream; natural riverine/tidal siltation with zero intervention. |
| **Lowers it / defused by** | Dredge Harbor (Develop funding/method resetting SiltLevel to baseline); a province-tier Water Magistracy vetting Develop requests against shared SiltLevel before approval. |
| **Crisis it fuses toward** | Friction→Crisis: harbor traffic collapses, trade/Guild Standing shifts to a rival port (Zwin siltation → fall of Bruges, rise of Antwerp); at province scale, a "Harbor Choked" Crisis affecting every coastal settlement sharing the same lagoon/estuary (Venice's Magistrato alle Acque case). |
| **Defusing institution** | Dredge Harbor (single-settlement Develop method) · Water Magistracy (province-tier veto institution, extends Ministry/Consulta) · River Conservancy Directorship (the Yellow River case — a standing office mediating the Scour-vs-Broad-Relief fork). |
| **Historical grounding** | Zwin siltation/Bruges (§2.5); Yellow River course change/Pan Jixun (§2.5); Venice Magistrato alle Acque (§2.5). |

### 2.2 OreGrade

| Field | Detail |
|---|---|
| **What it tracks** | The quality/yield-per-unit-effort of a mine's ore body — a depleting resource, distinct from the mine's raw output cap. |
| **Raises it** | Not raisable by governance action in the catalogue's cases — it is a depleting natural endowment. (A Develop-tier "new vein discovered" Opportunity could reset it upward, but this isn't in the source catalogue.) |
| **Lowers it / defused by** | Continues to fall on its own schedule regardless of policy; the mechanical lever is not preventing the fall but **keeping extraction demands scaled to the falling grade** — Amalgamation (Sponsor/Develop process upgrade raising yield-per-OreGrade, the patio process) or Tribunal renegotiation of a fixed mining charter. |
| **Crisis it fuses toward** | Opportunity→Friction/Crisis: a fixed Treasury quota or fixed regalian charter rate set at peak-OreGrade stops scaling down as the ore depletes, forcing either coercive extraction (Mita Conscription: Order/Grudge cost every season) or an "Uprising" Crisis once Grudge crosses threshold, plus a permanent PS-decline demographic tag; unresolved, seeds a "New Rush" Opportunity migrating miners/capital to a rival settlement. |
| **Defusing institution** | Amalgamation (Develop process upgrade decoupling yield from raw OreGrade) · Regalian Mining Charter with Tribunal renegotiation (periodically re-pegs the extraction rate to current OreGrade instead of the charter-issuance baseline). |
| **Historical grounding** | Potosí silver depletion/mita/amalgamation (§2.5); Erzgebirge Bergordnungen mining boom-bust (§2.5). |

### 2.3 SalinityLevel

| Field | Detail |
|---|---|
| **What it tracks** | Salt buildup in irrigated farmland from sustained high-intensity irrigation without drainage maintenance. |
| **Raises it** | Consecutive high-intensity-irrigation seasons with no Corvée-desilting Levy; running a single-crop (e.g. wheat) regime past the point local drainage can support. |
| **Lowers it / defused by** | Corvée Desilting Levy (recurring labor-tax that actively suppresses SalinityLevel, at an Order cost) · Crop Substitution (Develop-tier adaptive swap — e.g. wheat→barley — trading yield ceiling for lower Crisis odds once salinity is already elevated). |
| **Crisis it fuses toward** | Friction→Crisis→Ambition: crosses crop-viability thresholds, and past a final threshold becomes **irreversible** (permanent ceiling loss, not a recoverable dip) — culminating in Prosperity/PS collapse and a Standing/Recognition transfer to a rival power (the historical Sumer→Akkad shift). |
| **Defusing institution** | Corvée Desilting Levy (ongoing suppression) · Crop Substitution (adaptive fallback once suppression has failed to keep pace). |
| **Historical grounding** | Canal siltation/salinization in southern Mesopotamia (§2.5). |

### 2.4 SubsidenceRisk

| Field | Detail |
|---|---|
| **What it tracks** | Ground-level collapse risk from drained/reclaimed wetland or over-extracted peat/aquifer terrain — a delayed structural liability on land that reads as a Prosperity *gain* in the season it's created. |
| **Raises it** | Open-channel drainage engineering used to reclaim marginal wetland terrain (the mechanism that also grants the near-term Prosperity gain); no counter-investment once reclamation is chartered. |
| **Lowers it / defused by** | Not resettable by an in-catalogue action — the source case (Bedford Level/Fens) treats it as a structural consequence of the reclamation method chosen, not a stat with a maintenance lever. The closest defuse is choosing the Bargain path at reclamation time (compensated, less-land, lower-intensity drainage) over the Comply/Concession path, trading away some of the near-term Prosperity gain to cap how high SubsidenceRisk climbs. |
| **Crisis it fuses toward** | A multi-decade delayed "Peat Subsidence Flood" Crisis landing on the *same land the original Opportunity granted* — the reclamation's own success is what eventually floods it. |
| **Defusing institution** | None standing in the catalogue — this is the starkest "no institutional defuse, only an upstream method choice" case of the eight, which is itself a design-relevant asymmetry worth flagging. |
| **Historical grounding** | Bedford Level Corporation / draining the Fens (§2.5). |

### 2.5 RisingWaterLevel

| Field | Detail |
|---|---|
| **What it tracks** | A cross-settlement hidden tag: water level rising at a **downstream** settlement as a direct consequence of an engineering choice made at an **upstream** settlement (dike-raising / channel-narrowing that displaces flood volume rather than absorbing it). |
| **Raises it** | Upstream Comply-Scour (narrow the channel, raise the dikes at the capital-adjacent settlement — resolves *that* settlement's throughput/Prosperity/Defense problem while planting the tag downstream). |
| **Lowers it / defused by** | Upstream Bargain-Broad-Relief (widen the channel instead, sacrificing capacity to reduce downstream risk) · a River Conservancy Directorship mediating the Scour-vs-Broad-Relief fork province-wide instead of settlement-by-settlement. |
| **Crisis it fuses toward** | A delayed "Rising Lake Threatens [Settlement]" Crisis firing at the downstream node **independent of that settlement's own choices** — potentially decades after the upstream decision, with no visibility for the downstream governor into why. |
| **Defusing institution** | River Conservancy Directorship (province-tier standing office, like a Ministry seat, holding the Scour-vs-Broad-Relief fork above any single settlement's local incentive). |
| **Historical grounding** | Yellow River course change / Pan Jixun's engineering, Ming dynasty (§2.5) — explicitly the catalogue's paradigm case for "a Fortify choice at one node silently changes Crisis odds at another many seasons later." This is the sharpest example of the cross-settlement-fuse problem described in §0 above — genuinely hard to represent as a pure Prosperity abstraction, because the entire dramatic point is that the downstream settlement's sheet shows nothing wrong until the Crisis fires. |

### 2.6 FloodIndex

| Field | Detail |
|---|---|
| **What it tracks** | A read-only environmental gauge (not driven by governance action) measuring the current season's flood level against a historical baseline — the thing a Nilometer-style facility *measures*, not a stat governance choices move. |
| **Raises it** | Natural/seasonal — not a governance lever. A good flood raises it; a poor flood lowers it. |
| **Lowers it / defused by** | N/A directly — the mechanical question is not "how do we raise FloodIndex" but "does our Levy formula respond to it." |
| **Crisis it fuses toward** | Friction→Crisis when a **fixed/unadjusted Levy** is charged regardless of a low reading — Defy triggers a "Famine Unrest" Crisis; repeated Comply (honoring the gauge) instead writes a `gauge-bound assessment` Precedent locking future Levy to the reading. |
| **Defusing institution** | Gauge-Indexed Levy (new Levy method reading its rate directly off FloodIndex, auto-scaling without a per-season roll) — installing it doesn't change FloodIndex itself, it removes the *mismatch* between a fixed quota and a variable environment that is the actual trigger predicate. |
| **Historical grounding** | The Nilometer / flood-indexed taxation, Egypt (§2.5). |

### 2.7 DroughtIndex

| Field | Detail |
|---|---|
| **What it tracks** | The severity/duration of an active drought — the environmental read that a granary policy is checked against, structurally parallel to FloodIndex but for scarcity rather than gauge-mismatch. |
| **Raises it** | Natural/climatic, not governance-driven (may correlate with a world-level Cooling flag per §2.8 of the source catalogue). |
| **Lowers it / defused by** | N/A directly — again the lever is not the index itself but whether a buffer exists to absorb it. |
| **Crisis it fuses toward** | Crisis, checked against Granary StockLevel (§2.8 below) at a famine floor: Comply (open granaries, StockLevel drawn) vs. Defy/empty (Order−3, Π+3, Grudge); an unmet drought seeds a rebel/warlord Ambition gaining Standing (the Chongzhen drought / fall of the Ming case), i.e. drought severity that outstrips buffer capacity can transfer faction-ladder rank to a rival. |
| **Defusing institution** | Ever-Normal Granary (see StockLevel, §2.8) — DroughtIndex itself is never defused, only survived. |
| **Historical grounding** | Chongzhen Drought / fall of the Ming (§2.5); North China Famine 1876–1879 / Ever-Normal Granary collapse (§2.6); Great Famine of 1315–1317 (§2.6, climate-shift framing). |

### 2.8 StockLevel

| Field | Detail |
|---|---|
| **What it tracks** | Accumulated grain/food reserves in a standing Granary facility — the buffer DroughtIndex is checked against. |
| **Raises it** | Sponsoring the Granary in good seasons (Ever-Normal Granary / changping-cang mechanism: banking surplus rather than spending it). |
| **Lowers it / defused by** | Auto-drawn when a drought/famine Crisis fires (that's its purpose); decays from underinvestment if Treasury is diverted elsewhere (e.g. to Muster/Conquest) over consecutive seasons even absent a drought. |
| **Crisis it fuses toward** | StockLevel itself doesn't cause a Crisis — it's the mitigation lever checked *at* the DroughtIndex/famine Crisis. Zero StockLevel converts an ordinary drought roll into full-severity famine → Order collapse → rebel Ambition/rival Standing gain; nonzero StockLevel blunts the identical roll and blocks that follow-on. |
| **Defusing institution** | Ever-Normal Granary (Develop Facility upgrade persisting across seasons, decays if Treasury is diverted — same facility as DroughtIndex's counter, listed separately here because StockLevel is the trackable meter and DroughtIndex is the trigger it's checked against). |
| **Historical grounding** | Chongzhen Drought / fall of the Ming (§2.5); North China Famine 1876–1879 (§2.6); Rome's Cura Annonae / Granary Prefecture (§2.6, structurally identical mechanism at capital scale). |

---

## 3. Per-stat abstract-vs-track recommendation

Applying the §1 framework. **This is a recommendation for the follow-up authoring pass to weigh, not a ruling.**

| Stat | Cross-settlement? | Multi-decade? | Needs a legible gate? | Recommendation |
|---|---|---|---|---|
| **SiltLevel** | Yes, at province scale (Venice case); mostly no at single-harbor scale (Zwin case) | Sometimes (Zwin: generations) | Yes — Water Magistracy's whole premise is a shared number to veto against | **Track**, but only where a province-tier institution (Water Magistracy) is in play; single-settlement SiltLevel can abstract to a Prosperity-trajectory modifier if no cross-settlement lagoon/harbor is modeled. |
| **OreGrade** | No (local to one mine) | Yes (multi-generation depletion) | Yes — Tribunal renegotiation needs a number to re-peg the charter rate against | **Track**, if mining settlements are meant to have a depletion arc at all; otherwise **abstract** — a mine that never runs a charter-renegotiation subplot has no mechanical need for OreGrade separate from a Prosperity/Treasury-yield trajectory that just declines over time. |
| **SalinityLevel** | No (local to one settlement's farmland) | Yes, and the endpoint is irreversible | Borderline — Corvée Desilting Levy could plausibly be a flat recurring-Order-cost method with no separate meter | **Abstract candidate** — the irreversibility is the interesting part, and that can be modeled as a one-way Prosperity-ceiling ratchet (each ignored season permanently lowers the ceiling a notch) without a full 0–100 SalinityLevel meter. |
| **SubsidenceRisk** | No (local) | Yes, decades | No standing institution gates on it at all (§2.4 above) | **Abstract** — with no institutional counter-play reading the number, there's little lost by folding it into "reclaimed-wetland terrain carries a durable Prosperity-ceiling malus that resolves as a one-time delayed Crisis," i.e. a scheduled follow_on rather than a tracked stat. |
| **RisingWaterLevel** | **Yes — the defining case** | Yes, decades | Yes — River Conservancy's fork literally is "check this number before choosing Scour vs. Broad-Relief" | **Track.** This is the one stat in the set where abstraction genuinely breaks the mechanic: the entire design point is an invisible cross-settlement debt that the downstream governor cannot see coming. A Prosperity number is local by construction and cannot carry this. If the depth layer is adopted at all, start here. |
| **FloodIndex** | No (it's a read-only external gauge, not a settlement-owned meter) | No (resets each season) | Yes — Gauge-Indexed Levy needs a number to auto-scale against | **Track only if Gauge-Indexed Levy is adopted as a Levy method**; otherwise this is really just "was the harvest good or bad this season," which most designs already roll into Prosperity/Harvest_Yield variance and don't need a second named stat for. |
| **DroughtIndex** | No | No (per-episode) | Yes — checked against StockLevel at a famine floor | **Abstract candidate**, structurally identical to FloodIndex — likely collapses into whatever Harvest_Yield/Prosperity-shock roll already exists rather than needing its own named severity index, *unless* the Ever-Normal Granary mechanic (below) is adopted, in which case something has to be the thing StockLevel is checked against. |
| **StockLevel** | No | No (draws down per-Crisis, refills per-Sponsor) | Yes — this is the actual mechanical payload: "did you save for the drought or not" | **Track if — and only if — Ever-Normal Granary is adopted as a Develop facility at all.** Given Jordan's standing abstraction ruling on food supply specifically, this is the stat most directly in tension with that ruling: StockLevel *is* a granular food-supply meter. The clean resolution is a binary design choice, not a partial one — either (a) food supply stays abstracted to Prosperity and Ever-Normal Granary becomes a flat Fortify/Sponsor method that reduces future famine-Crisis severity with no separate meter behind it, or (b) the granary mechanic is adopted whole-cloth with its own StockLevel tracker. A half-tracked StockLevel (present but not really gating anything) would be worse than either pure option. |

**Summary read:** of the eight, **RisingWaterLevel** is the strongest case for a genuinely new tracked stat (the cross-settlement invisibility is the mechanic, not decoration), **SiltLevel** is a conditional case (track only where a province-tier institution consumes it), and the remaining six (**OreGrade, SalinityLevel, SubsidenceRisk, FloodIndex, DroughtIndex, StockLevel**) each have a workable abstract-to-Prosperity treatment that preserves most of the dramatic beat at the cost of losing the fine-grained "you can see the number creeping" texture — which is exactly the trade Jordan's standing ruling already accepts for food supply elsewhere. **StockLevel is the one genuinely blocked on a prior binary decision** (adopt Ever-Normal Granary as a mechanic at all, yes/no) rather than a granularity spectrum — it can't be "a little bit tracked."

---

## 4. Cross-references

- Source catalogue: `designs/audit/2026-07-10-historical-concerns-action-catalogue/historical_concerns_action_catalogue_v1.md` §2.4, §2.5, §2.6.
- Sibling compendium parts drawing on the same catalogue: Part 43 (`43_directive_types.md`, Embargo/Recall/etc.), and any companion action-verb part covering Dredge Harbor / River Conservancy Directorship / Gauge-Indexed Levy / Ever-Normal Granary as Develop/Levy/Fortify methods (see `42_action_verb_catalogue.md` if those methods are catalogued there).
- Binds conceptually to `designs/territory/settlement_layer_v30.md` (Prosperity, FacilityTier, Develop) and `designs/provincial/faction_politics_v30.md` (Standing/Grudge machinery the Crisis follow-ons write into) — **no edits made to either**, per the source catalogue's read-only discipline.
- Per repo convention (`CLAUDE.md` §5): none of the numbers above are typed engine-params: they are prose distillations of a research pass, not sourced `PP-NNN`/`ED-NNN` canon. Do not lift a threshold or magnitude from this Part as if it were ratified.
