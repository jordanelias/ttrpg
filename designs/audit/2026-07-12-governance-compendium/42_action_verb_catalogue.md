# Part 42 — Consolidated Domain-Action / Verb Catalogue

## Status: PROPOSED — compiled 2026-07-12, Lane: IN (cross-cutting; touches FA, SE, MB, GO)

**Source.** Every entry below is extracted from the `Introduces (Action)` line of an event card in
`designs/audit/2026-07-10-historical-concerns-action-catalogue/historical_concerns_action_catalogue_v1.md`
§2.1–§2.10, cross-checked against the compiled event-card files in
`designs/architecture/governance_compendium_v1/event_cards/*.md` (HEV-* IDs). Nothing here is newly
invented for this compendium — it is a deduped, verb-grouped index over already-proposed mechanics.
**All entries are PROPOSED** (the historical-concerns audit is explicitly "not itself canon — a
research/synthesis artifact for a follow-up authoring pass," per that doc's own header) and none of
this has been ratified into `governance_play_redesign_v1.md`, `faction_politics_v30.md`, or
`settlement_layer_v30.md`. Treat every row as a candidate for a future authoring pass, not as an
implemented rule.

**Purpose of this Part.** The historical-concerns catalogue is organized by *event* (10 subsections,
~94 cards). A designer or Godot implementer instead needs the inverse view: "what can a governor
*do*, and which existing verb does it hang off of?" This Part re-indexes the same ~90 distinct
actions by their parent verb (the eight base verbs already in the governance model — **Develop,
Fortify, Keep Order, Hold Court, Sponsor, Treat, Levy, Investigate** — plus **Directive**, the
PA-issued order type, and a **NEW** bucket for actions that don't cleanly extend any existing verb).
Within each verb group, rows are ordered as they appear in the source catalogue (§2.1 → §2.10).

**How to read a row.**
- **Action** — the proposed action/method name, as named in its source card's `Introduces (Action)` line.
- **Extends** — which of the eight base verbs (or Directive) it is a sub-method/branch/extension of,
  or **NEW** if the card proposes a freestanding verb/mechanic with no clean parent.
- **Mechanic** — what it mechanically does (condensed from the card's `Introduces` + `Loop` lines).
- **Cost** — the AP/Treasury/Reputation/Grudge/Standing price tag as described in the source, where stated.
- **Motivating event(s)** — the historical event card(s) that motivated it, with a pointer to the
  `HEV-*` event-card ID where one exists in the compiled `event_cards/` files.
- **§** — the source subsection in the historical-concerns catalogue.

Several actions recur near-identically across multiple cards (e.g. a Sponsor-funded standing granary
appears under three different famine events); those are consolidated into one row with multiple
motivating events rather than duplicated, per the "dedupe" instruction. A short **§2.11 Reskin
clusters** note at the end flags the handful of same-mechanic/different-name near-duplicates the
source catalogue itself did not collapse, for a future ratification pass to resolve.

---

## 1. Develop-family actions

| Action | Extends | Mechanic | Cost | Motivating event(s) | § |
|---|---|---|---|---|---|
| Rebuild Infrastructure | Develop | High-cost multi-season sub-project restoring a *permanently capped* Develop ceiling (e.g. destroyed irrigation) back to normal | Multi-season Treasury/AP sink | Mongol Siege of Baghdad (1258) — HEV-SIEGE-07 | 2.3 |
| Rebuild-to-Code | Develop/Fortify | Pre-emptive (or Comply-triggered) method lowering future Earthquake/Fire trigger weight + severity; writes a durable `Rebuild-to-Code` tag | Treasury; often funded by curtailing a patron's Standing (Precedent), raising their Grudge | 1755 Lisbon Earthquake/Tsunami/Fire | 2.4 |
| Housing Code | Fortify/Develop | Regulates high-density dwelling construction, lowering the casualty multiplier on Earthquake cards — the pre-emptive mirror of Rebuild-to-Code | Treasury; needs Court Attendance to authorize promptly | 1556 Jiajing (Shaanxi) Earthquake | 2.4 |
| Water Infrastructure | Fortify (Walls extension) | Extends the Fortify:Walls method to cover water-mains, lowering fire-following-earthquake severity | Treasury/AP | 1906 San Francisco Earthquake & Fire | 2.4 |
| Relocate Settlement | Develop (heavy multi-season method) | Full relocation ("New [Settlement]"), gated by Charter-holder consent via Quo Warranto; raises the Prosperity ceiling and writes a `planned capital` Precedent | Multi-season Treasury/AP sink; Charter-holder consent required | 1693 Val di Noto Earthquake | 2.4 |
| Dredge Harbor | Develop (funding/method) | Resets a harbor's SiltLevel stat; pairs with a Treat to hold tariffs flat while retaining trade | Treasury | Zwin siltation / fall of Bruges, rise of Antwerp | 2.5 |
| Charter Reclamation Corporation | Develop (fourth funding method) | Private capital reclaims marginal/wetland terrain for a standing Concession + reduced governor control; plants a hidden SubsidenceRisk stat | Reduced governor control over the reclaimed land (Concession) | Bedford Level Corporation / draining the Fens | 2.5 |
| Crop Substitution | Develop (adaptive swap) | Trades production ceiling for lower Crisis odds by swapping a failing staple crop (e.g. wheat→barley) under rising SalinityLevel | Lower production ceiling | Canal siltation / salinization in southern Mesopotamia | 2.5 |
| Diversify Corridor | Develop (funding sub-method) | Routes trade through 2+ independent corridors instead of one; +1 AP and slower Prosperity growth, writes a `route-diversified` Precedent lowering future single-corridor Crisis weight | +1 AP, slower Prosperity | Plague of Justinian (541–549 CE) | 2.7 |
| Lighthouse | Develop (follow-on, gated) | Locked until a storm Crisis fires once at a given naval-basing settlement; then unlockable Develop upgrade lowering future storm severity | Treasury; only purchasable post-Crisis | The Great Storm of 1703 | 2.8 |
| Adopt Local Practice | Develop (method-fork for isolated/frontier settlements) | Trades a Precedent/Disposition hit with the metropole (read as drift/heterodoxy) for a durable resilience bonus against a persistent Cooling-flag decline | Disposition hit with metropole | Collapse of the Norse Greenland colonies (c. 1350–1450) | 2.8 |
| Develop:Redistribute | Develop (new method) | Reallocates land/charter rights away from Guild/Actor holders; invalidates the current Assessment until a Survey refresh, so Levy/Extract keeps targeting the stale pre-redistribution figure | Multi-season Prosperity penalty; Grudge from dispossessed holders | Zimbabwe hyperinflation (2000s) | 2.9 |

---

## 2. Fortify-family actions

| Action | Extends | Mechanic | Cost | Motivating event(s) | § |
|---|---|---|---|---|---|
| Standing Fleet | Fortify + Muster investment | Gates a Defy branch (punitive fleet) that is otherwise mechanically unavailable — without prior investment, a coastal-tribute Friction collapses to Comply-only | Treasury/AP investment banked ahead of time | Barbary Tribute System (16th–19th c.) | 2.2 |
| Coalition Fortify Pool | Fortify (new acquisition path) | Multiple factions jointly pre-fund a threatened settlement's Fortify ahead of a known Crisis; unlocked by surviving an existential siege | Shared multi-faction Treasury | Great Siege of Malta (1565) | 2.3 |
| Inundation | Fortify-adjacent (mid-Crisis-only method) | Trades Prosperity (flooding productive land) for an immediate Defense/relief bonus during an active siege | Prosperity loss | Siege of Leiden (1574) | 2.3 |
| Refuge Walls | Fortify (fourth method) | Shelters rural population inside walls for +1 Defense/PS, but writes a durable `Overcrowding` tag unless paired same-season with a Sponsor relief action or sized Fortify:Walls | Overcrowding tag (feeds Epidemic trigger) unless mitigated same season | Plague of Athens (430 BCE) — HEV | 2.7 |
| Sanità Lazzaretto | Fortify (facility) | Grants a Quarantine Tier 0–3 reducing draw-weight of Plague cards whose trigger references a *trade/sea* vector only — explicitly does not cover military-transit | 2 AP + Treasury | Venice Lazzaretto / 1630–31 quarantine failure | 2.7 |
| Sea Wall | Fortify (new method) | Lowers coastal storm-Crisis severity for an anchored/staged fleet or settlement | Treasury/AP | Kamikaze typhoons vs the Mongol fleets (1274 & 1281) | 2.8 |
| Sheltered Dockyard | Fortify (basing-location method) | Alternative to cheap "Roadstead Mooring"; sharply reduces storm-roll severity for moored fleets | Treasury/AP, higher than Roadstead Mooring | The Great Storm of 1703 | 2.8 |
| Harbor Defenses | Fortify (mitigation) | Reduces Conquest severity/odds specifically if a tributary settlement later Defies a Directive tribute obligation | Treasury/AP | Kilwa Sultanate's Sofala gold monopoly / Sack of Kilwa (1505) | 2.10 |

---

## 3. Keep Order-family actions

| Action | Extends | Mechanic | Cost | Motivating event(s) | § |
|---|---|---|---|---|---|
| Quarter | Directive (new type, sibling to Host) | Forces Force-method Keep Order over the governor's own preference | PS loss + Grudge each season it runs | Colonial Billeting / Quartering Acts (1765–1774) | 2.3 |
| Force (Crisis-tier violence branch) | Keep Order | Explicit high-Π downside on the existing Force method: risk of spawning mob/pogrom violence against a resident Rival Cohort, beyond the normal PS/Disposition cost | Grudge + Outlawed tag on the targeted cohort | 1923 Great Kanto Earthquake | 2.4 |
| Evacuate | NEW (emergency sub-verb) | Spend AP ahead of a telegraphed Crisis to relocate population, converting a Weight-zeroing "erasure" outcome into a survivable-with-losses one | AP spent against a threat that most seasons doesn't land (warning-fatigue cost) | 79 AD Vesuvius | 2.4 |
| Segregation Camps | Keep Order (harsher Force sub-branch) | Buys a larger/faster Order/Π recovery from a Plague Crisis at double the Disposition penalty, a guaranteed Grudge, and an assassination-class Intrigue draw-weight flag | Double Disposition penalty; guaranteed Grudge; assassination-Intrigue risk | Third Plague Pandemic (from 1894) | 2.7 |
| Court Officer Disposition | Keep Order/Treat lever | Shores up a high-rank officer's loyalty, denying a rival faction the Rival Cohort opening for a bribed defection/coup | AP/Treasury | Battle of Plassey / Jagat Seth bankers / Diwani of Bengal (1757) | 2.10 |
| Conceal Source | Keep Order (information-control sub-option) | Spends AP/Clerk Capacity each season to suppress a "Route Known" tag, keeping a trade-secrecy Thread dormant | Recurring AP/Clerk Capacity | Mali Empire's trans-Saharan gold-salt monopoly | 2.10 |
| Assembly Cohesion | Keep Order (feeds ladder Recognition/Rival Cohort dimensions) | Raises a Guild-type faction's internal Recognition/Cohesion to counter erosion that would otherwise make it an annexation target | AP/Treasury | Muscovite conquest of Novgorod (1478) | 2.10 |

---

## 4. Hold Court-family actions

| Action | Extends | Mechanic | Cost | Motivating event(s) | § |
|---|---|---|---|---|---|
| Ratify (paired with Donative) | Hold Court (Ratify/Reject/Amend branch) + Levy | Converts a bought fait-accompli military win into legitimacy via a Consulta vote, writing a closing `military-acclamation-legitimate` Precedent | Consulta vote cost; without it, Mandate stays depressed and the Crisis reseeds | Year of the Four Emperors (Rome, 69 CE) — HEV-SUCC-01 | 2.1 |
| Denounce as Heretic | Hold Court (new Intrigue social contest via Tribunal branch) | Routes a rival succession contender through the Church Tribunal; conviction guts their Influence-based Stage-1 pool, acquittal backlashes on the accuser | Priced tit-for-tat social-contest roll | Mughal War of Succession (1657–1661) — HEV-SUCC-04 | 2.1 |
| Quarantine Waiver Petition | Hold Court (new branch, structurally identical to Ordenanza Ratification) | Ratify waives a shipment's Sanità inspection (Guild Influence+1, but voids that shipment's Quarantine Tier discount, spiking Plague Crisis weight to near-certain); Reject imposes Guild Master Standing/Grudge cost; Investigate-first exposes the bribery vector | Guild patronage spent to push Ratify; voided quarantine protection if Ratified | Great Plague of Marseille (1720) | 2.7 |

---

## 5. Sponsor-family actions

| Action | Extends | Mechanic | Cost | Motivating event(s) | § |
|---|---|---|---|---|---|
| Open Emergency Granary | Sponsor (pre-funding method) | Pre-funds a Prosperity floor ahead of a province-wide climate shock | Treasury, banked ahead of time | 1815 Tambora / 1816 Year Without a Summer | 2.4 |
| Guild Relief | Sponsor (faction-side act) | A resident Guild pays relief obligations "in full" (Reputation gain, `Honored their word`) or invokes technicalities (Grudge + `Weaseled`) — either banks onto that faction's own Standing ladder | Treasury (Guild-side) | 1906 San Francisco Earthquake & Fire | 2.4 |
| Ever-Normal Granary | Sponsor/Develop (standing facility) | Accumulates a StockLevel across good seasons, auto-drawn against famine/drought rolls to blunt Order/PS loss and block a rebel-Ambition follow-on | Sponsor spend each good season; decays if Treasury is diverted to Muster/Conquest | Chongzhen Drought/fall of the Ming; North China Famine 1876–1879; Chongzhen drought/Great Plague 1633–1644 | 2.5, 2.6, 2.7 |
| Civic Granary | Develop (fourth funding method) | Lowers both the famine-severity roll and the Σ(unserved Needs) Π contribution | Treasury | Great Famine of 1315–1317 (climate-shift framing) | 2.8 |
| Blockade-Runner Sponsorship | Sponsor (defender-exploit) | Recovers Treasury lost to a naval blockade via smuggling; risks a Corruption/Order Intrigue if the network is broken | Corruption/Order risk | Union Blockade / Anaconda Plan (1861–1865) | 2.2 |
| Underwrite | Sponsor (sub-option) | A capital-holding faction finances a Directive shortfall in exchange for a Concession on a specific extractive resource; raises the lender's Standing and Ministry/Consulta eligibility | Debt + Concession tag pair | Fugger mining monopolies / Habsburg election financing (1519) | 2.10 |
| Capital Partnership | Sponsor (sub-option) | Issues a *cross-settlement* Concession (usable at any settlement) rather than a settlement-bound Compact, funding a Guild's mobility/profit-share | Treasury; accrues Debt whose unresolved Friction raises Π | Mongol ortoq merchant-partnership under the Pax Mongolica | 2.10 |
| Charter Intelligence Compact | Sponsor (cross-linking into the Muster/Conquest pipeline) | Licenses a Guild for both a trade monopoly and pre-Conquest reconnaissance, tying a Sponsor payoff to future Conquest-planning quality | Expands the Guild's own-courts autonomy each renewal (accumulating Concession) | Aztec pochteca merchant guild's chartered monopoly | 2.10 |

---

## 6. Treat-family actions

| Action | Extends | Mechanic | Cost | Motivating event(s) | § |
|---|---|---|---|---|---|
| Renegotiate Compact | Treat/Levy | Emergency-breaks an active fixed-extraction Compact mid-term; writes a Precedent other Compact-bound settlements can cite via Petition | Precedent exposure across the broader Compact network | 1783–84 Laki Eruption / Móðuharðindin | 2.4 |
| Broker Diversion | Treat | Mediates between two settlements over a live Crisis (e.g. an eruption), converting a unilateral act into a negotiated Compact | AP now, for lower Π in both settlements later | 1669 Etna Eruption / Catania Lava Diversion | 2.4 |
| License Exception | Treat (chit extension of an Embargo Directive) | Grants a bounded licensed corridor exempt from an enforced Embargo; each exception is a standing Debt-family chit | Standing Debt chit; bloc-wide erosion of the embargo if overused | Napoleon's Continental System (1806–1814) | 2.2 |
| Alternate Corridor | Sponsor extension (Treat-adjacent) | Hard-preconditioned on a prior Fortify airbase/corridor FacilityTier; ongoing AP+Treasury spend that bleeds Π down and denies an attrition-Conquest | Cannot be reacted into existence mid-Crisis — must be pre-banked | Berlin Blockade (1948–49) | 2.2 |
| Sovereign Bargain | Directive-Bargain (rank-gated) | Standing-6+ only; converts an open-ended reprisal massacre into a bounded one-time Compact indemnity | Rank-scarce — unavailable to an ordinary governor | Nadir Shah's Sack of Delhi (1739) | 2.3 |
| Improvised Relief | Muster variant | Bypasses exhausted Levy capacity to relieve a besieged, legitimacy-linked settlement; success fast-tracks the leading NPC's Recognition, bypassing the normal Initiation Gate | AP; paired with a "Legitimacy Siege" flag | Siege of Orléans (1428–1429) | 2.3 |
| Emergency Grain Compact | Treat (famine sub-case) | Influence+history roll vs a distant supplier; +1 Prosperity now, but writes both a Debt tag *and* a Contagion Vector flag | Debt tag + guaranteed-weight Plague draw next season | The Black Death (1347–1351) | 2.7 |
| Foreign Loan | Treat (method-variant) | Debt cost scales with how many seasons a currency-protecting Comply-delay was chosen before finally borrowing | Escalating Debt with each deferred season | Finnish Famine 1866–1868 | 2.6 |
| Treat: Index Wages | Treat (minor side-deal) | Re-pegs a fixed-nominal garrison/salaried Obligation to current Capital-Posture at an ongoing Treasury cost | Ongoing Treasury cost | Ottoman akçe debasement / 1585–86 monetary crisis | 2.9 |
| Sunset Review | Treat/Levy (periodic, low-AP sub-action) | Checks whether a long-standing Concession's terms still match the real balance of Standing, forcing reconciliation instead of stale drift | Low AP, periodic | Ottoman capitulations / Bursa silk trade reversal | 2.10 |
| Charter Review | Levy (Quo Warranto sub-option) | Audits a long-standing foreign Concession's reciprocity before a rival domestic Guild's Petition forces the issue | AP/Clerk cost | Hanseatic Kontor system / revocation of the London Steelyard (1598) | 2.10 |

---

## 7. Levy-family actions

| Action | Extends | Mechanic | Cost | Motivating event(s) | § |
|---|---|---|---|---|---|
| Toll | Levy (chokepoint-gated method) | Auto-succeeding standing income stream at a chokepoint settlement; hard-gated on prior Fortify FacilityTier as a multiplier | Accrues Debt/Grudge over sustained use, seeding a future Friction contesting the strait | Danish Sound Dues / Øresundstolden (1429–1857) | 2.2 |
| License Waters | NEW (joint Levy+Fortify precondition) | Licenses a *zone*, not a single settlement, with patrol upkeep; self-financing via License income | Patrol upkeep; accumulating Grudge feeds rivals' Conquest weight | Portuguese Cartaz System (Indian Ocean, 16th c.) | 2.2 |
| Contribution System / Kontributionssystem | Levy (negotiated-extorted method, sibling to Encabezamiento) | Funds a besieger's garrison upkeep directly from the occupied region, keeping the besieger solvent and removing the "unpaid-troops" severity modifier | Debt/Grudge tags in the occupied territory | Sack of Magdeburg (1631) | 2.3 |
| Settle Arrears | Levy (sub-action) | Pays down garrison-pay Debt before it escalates, resetting the mutiny clock | Treasury | Spanish Fury at Antwerp (1576) | 2.3 |
| Gauge-Indexed Levy | Levy (new method) | Reads its extraction rate off a tracked environmental stat (e.g. FloodIndex), auto-scaling without a per-season roll | None beyond the facility (Gauge) that enables it | The Nilometer / flood-indexed taxation (Egypt) | 2.5 |
| Mita Conscription | Levy (coercive method) | Forced labor draft holding mine Output steady despite falling OreGrade | Order−2 and Grudge(indigenous) each season it runs | Potosí silver depletion / mita / amalgamation | 2.5 |
| Regalian Mining Charter (with Tribunal renegotiation) | Levy (depleting-resource-keyed method) | Cross-references OreGrade so the extraction rate can be renegotiated down via Tribunal review as a mine depletes, instead of staying locked at the charter's peak-yield rate | AP for the Tribunal review | Erzgebirge Bergordnungen / mining boom-bust | 2.5 |
| Corvée Desilting Levy | Levy (recurring labor-tax) | Suppresses a farmland's rising SalinityLevel below crop-loss thresholds | Order−1 recurring | Canal siltation / salinization in southern Mesopotamia | 2.5 |
| Price Ceiling / Export Embargo | Levy/Treat (method-variant) | Suppresses immediate Order loss from a grain-price Crisis, but attaches a Precedent raising escalation weight if the shortage persists | Precedent raising future escalation | Great Famine of 1315–1317 | 2.6 |
| Granary Prefecture | Levy (capital-only facility unlock) | Unlocks a "Subsidized Distribution" Levy method-variant; raises FacilityTier lowering the AP cost/failure of that method | Treasury (facility); Complying plants an `Entitlement` Precedent making future refusal costly | Rome's Cura Annonae / Egyptian grain | 2.6 |
| Divert Logistics to Muster | Directive option (Levy/Muster interaction) | Commits Treasury/Logistics to an active Muster during a famine instead of relief; raises readiness now, multiplies next-season famine severity/Grudge | Next-season Levy yield/Disposition suppression | Deccan Famine 1630–1632 | 2.6 |
| Remission (sub-option on revenue-extraction Directives) | Levy/Directive | Comply-rigid / Bargain-remit-and-report / Defy-withhold fork on a fixed-quota extraction Directive during famine | Grudge if rigid; Reputation cost with the Authority if Defied | Great Bengal Famine of 1770 | 2.6 |
| Liberalize Grain Trade | Treat/Levy (method-variant, opposite pole from a fixed-price/narh method) | Removes price-ceiling escalation risk in exchange for exposing Prosperity/Order to harvest RNG | Exposure to a poor-harvest Crisis + Reputation-attack Intrigue | The Flour War (Guerre des Farines, 1775) | 2.6 |
| Relief Obligation | Keep Order (workhouse/Poor-Law mechanic) | Available regardless of a standing free-trade Precedent, decoupling relief from export/doctrine policy | Local AP/Ledger cost; Reputation friction with the doctrine's champion faction | Great Irish Famine 1845–1852 | 2.6 |
| Grain Ministry | Levy (capital-only enforcement facility) | Raises FacilityTier gating the success of a fixed-price-control Levy method | Treasury (facility); repeated Petition failures at low tier block the Develop path to build it (bootstrapping trap) | Ottoman Istanbul provisioning / narh price control | 2.6 |
| Staged Demobilization | Muster (sub-choice) | Routes returning legions/troops through a quarantine interval before redeployment to the interior, suppressing an Epidemic trigger at the cost of a season's delay | Extra Wealth + one season's delay | Antonine Plague (165–180 CE) | 2.7 |
| Emergency Resurvey | Survey (extends the live sub-verb) | Usable outside its normal ~8-season cooldown when an external-shock flag is active, at an Ob penalty, to refresh a stale Assessment before Extract strips the settlement below subsistence | Ob penalty | Cocoliztli epidemics 1545 & 1576 (New Spain) | 2.7 |
| Flota Scheduling | Levy (scheduled-convoy method) | Hard seasonal storm-avoidance bonus inside its departure window / penalty if a Loading-Delay Friction is left unresolved past it | Fixed-calendar rigidity; a Salvage Concession is the only slow post-loss recovery | 1622 hurricane destruction of the Spanish treasure fleet (Nuestra Señora de Atocha) | 2.8 |
| Expedite | Friction-resolution spend (Levy-adjacent) | Spends AP/Treasury to resolve a Loading-Delay Friction before a convoy's departure window closes | AP/Treasury | 1622 hurricane destruction of the Spanish treasure fleet | 2.8 |
| Annona Route Diversification | Levy (centralization-vs-redundancy fork, parallel to Encabezamiento/Flota Scheduling) | Trades per-season cost against the risk that a single source province's own Crisis collapses empire-wide Remit capacity | Higher per-season cost for redundancy | Late Antique Little Ice Age (536–660 AD) + Justinianic Plague onset | 2.8 |
| Levy:Debase | Levy (third method) | Auto-succeeds; extracts Treasury with a smaller immediate Order/Prosperity draw, but writes/stacks a permanent `Capital-Posture:Debased` tag raising future Levy Ob and fiscal-Crisis weight | Permanent stacking tag; a one-way ratchet | Roman Third-Century Crisis debasement / Diocletian's edicts | 2.9 |
| Recoinage | Directive-level (rare, PA-approval-gated) | Retires debased coin, clears all `Capital-Posture:Debased` tags, resets Levy Ob | Steep, one-time cost; the only clearing action, so deferral raises its price | England's Great Debasement / Elizabethan Great Recoinage | 2.9 |
| Levy:Farm | Levy (tax-farming variant) | Pledges a future season's Levy yield to a Sponsor-tier actor as collateral for immediate Treasury/AP infusion, writing a Debt tag | Debt tag; Defy converts it to a permanent Outlawed tag blocking further Sponsor/Treat with that faction | Edward III's default on the Bardi & Peruzzi (1340s) | 2.9 |
| Levy:Charter Fiat | Levy (paper-Treasury method) | Issues paper Treasury backed by a granted Charter/Concession asset instead of real Prosperity; each unit adds to a `Capital-Posture:Speculative` tag whose backing ratio sets a deterministic Bank Run trigger | Permanently burns the method once the Bank Run fires (blocked reuse) | John Law's Mississippi Bubble / Banque Royale collapse (1716–1720) | 2.9 |
| Currency Reset | Directive-level (same family as Recoinage) | Clears a land-backed `Capital-Posture:Speculative` collapse; writes a permanent "Precedent: Monetary Failure" raising baseline Π for several seasons | Baseline Π raised for several seasons post-Reset | French assignat hyperinflation (1790s) | 2.9 |
| Funding & Assumption | Directive-level | Consolidates multiple settlements' separately-accrued Debt/Capital-Posture into one faction-level Compact for a Concession, permanently strengthening the PA's direct extraction reach | Concession cost scales with how fragmented the prior debts were | Continental currency collapse / Hamilton's 1790 funding & assumption | 2.9 |
| Fund Resistance | Levy/Keep Order (emergency uncapped sub-choice) | Funds resistance (e.g. to an occupier) directly from Treasury with no AP ceiling, driving `Capital-Posture:Debased` to maximum in a single season | Forces a *mandatory* Currency Reset at forced-trigger severity next season | Weimar hyperinflation (1923) | 2.9 |
| Monopsony Enforcement | Conquest (gated by a repudiated-Compact Crisis tag) | A legitimacy precondition rather than bare aggression; success installs a Company-run Governor Assignment over the native elite | Requires a prior repudiated-Compact Crisis flag | VOC conquest of the Banda Islands / nutmeg monopoly (1621) | 2.10 |

---

## 8. Investigate-family actions

| Action | Extends | Mechanic | Cost | Motivating event(s) | § |
|---|---|---|---|---|---|
| Investigate (pretender-exposure use) | Investigate | Exposes/voids an unverified External-backed succession pretender before it is treated as real at the next Stage-1 contest | AP | Muscovite Time of Troubles (1598–1613) — HEV-SUCC-06 | 2.1 |
| Investigate (bribery-exposure use, Hold Court branch) | Investigate | Exposes a bribery vector behind a Quarantine Waiver Petition before choosing Ratify/Reject | AP | Great Plague of Marseille (1720) | 2.7 |

---

## 9. Directive-family actions (PA-issued order types)

| Action | Extends | Mechanic | Cost | Motivating event(s) | § |
|---|---|---|---|---|---|
| Recall | Directive (new type, sibling to Extract/Tax/Suppress/Install/Host/Cede) | Disbands an appanage prince's independently-granted forces | AP/Standing spend; a diagnostic Defy reveals rebellion intent | Toluid Civil War (Mongol, 1260–1264) — HEV-SUCC-07 | 2.1 |
| Embargo | Directive (new type, targets a *third* faction, not the settlement) | A hegemon crashes a Grudge-target rival's trade network at zero direct AP cost, converting political leverage into economic warfare | Deferred to the hegemon's allies' war-readiness if it escalates | The Megarian Decree (Athens, 432 BCE) | 2.2 |
| Multilateral Embargo | Directive (coalition-coordinated, gated through Ministry/Consulta) | Removes the Bargain branch entirely from a targeted faction's response fork — only Comply or Defy remain | Structurally forecloses a core response option for the target | ABCD Line & US Oil Embargo on Japan (1940–41) | 2.2 |
| Nationalize Charter | Quo Warranto bypass (Crisis-gated) | Seizes a foreign-held Charter outside the normal 16-season Quo Warranto window, once a patron-Friction has weakened the holder | Risks a Charter-holder coalition Conquest; resolved via Ministry/Consulta arbitration, not the battlefield | Suez Crisis & Canal Closure (1956) | 2.2 |
| Extract Succession Oath | NEW (Compact-family tag + mass social contest, parallel to Negotiate Quota) | Gives a named heir a fifth, oath-based claim basis; taxes later defectors with Grudge + `Reputation:Oathbreaker` | Mandate/AP cost | The Anarchy (England, 1138–1153) — HEV-SUCC-02 | 2.1 |
| Fratricide Law | NEW (Crown-tier post-Contest option) | Strips all losing succession claimants rather than let them persist as splinters | Severe Demotion-Magnitude-"total" Reputation/Grudge cost | Ottoman Interregnum / Fetret Devri (1402–1413) — HEV-SUCC-03 | 2.1 |
| Partible Succession | NEW (durable faction-configuration Precedent, set once at founding) | Maximizes a dynasty's living footprint but permanently disables the peaceful Smooth/Regency succession rows | Irreversible once adopted | Inca Civil War / Huáscar vs Atahualpa (c. 1529–1532) — HEV-SUCC-05 | 2.1 |
| Elective Succession | NEW (config flag) | Routes contested succession rows to an institutional electoral tally (electors) instead of pure strength/Standing math | Electors reward capability, so private lineage Wealth/Military still compounds | Kongo Civil Wars (17th–18th c.) | 2.1 |
| Trade Writ | Levy (new method, Ratify/Reject/Amend a trade node's Wealth flow) | Caps an untaxed lineage's independent Wealth at a Disposition cost, or drives it underground if Rejected | Disposition cost; Reject → Outlawed+Grudge | Kongo Civil Wars (17th–18th c.) | 2.1 |
| Convene Consulta / Convene Rival Assembly | Directive/Hold Court (regency election / contest-stage exploit) | Convene Consulta: tallies Standing+Disposition+Influence for a majority-wins Regency succession, bypassing the dice resolver. Convene Rival Assembly: lets a losing succession claimant convene their own legitimating assembly and Defy the verdict | Convene Consulta spends capital early; Convene Rival Assembly can override a G≥3 Unified resolution into a permanent SPLIT | Muscovite Time of Troubles (1598–1613); Toluid Civil War (1260–1264) | 2.1 |
| Settle & Confiscate | NEW (post-Conquest domain action) | Forced subnational faction-roster replacement/land reallocation after a "quarter denied" atrocity; writes a fresh Outlawed tag | Raises future Grudge/Intrigue generationally | Siege & Sack of Drogheda (1649) | 2.3 |
| Circumvallate | Conquest method (besieger) | Trades tempo (multi-season, AP/Treasury-heavy) for near-elimination of assault casualties | Multi-season AP/Treasury; only available after Bargain/Treat is closed off by a prior broken treaty | Siege of Numantia (134–133 BCE) | 2.3 |
| Water Board | NEW (standing flood-defense institution) | Funded by its own dedicated levy, ring-fenced from Directive diversion — decouples flood-defense funding from war-Directive competition | Dedicated levy income, structurally protected from reallocation | St. Elizabeth's Flood of 1421 (Netherlands) | 2.5 |
| River Conservancy Directorship | Fortify (Scour-vs-Broad-Relief fork) + province-tier standing office | Scour raises capital-adjacent Prosperity/Defense but plants a slow-incrementing RisingWaterLevel tag on a *downstream* settlement; Broad-Relief sacrifices capacity to avoid it | Treasury+1 (Scour) vs. reduced capacity (Broad-Relief) | Yellow River course change / Pan Jixun's engineering (Ming) | 2.5 |
| Water Magistracy | Directive/Ministry extension (province-tier veto institution) | Overrides a settlement's Develop request when its externalities (e.g. shared lagoon SiltLevel) threaten a shared downstream resource | Local Disposition−1 on the vetoed settlement | Venice's river diversions / Magistrato alle Acque | 2.5 |
| Remit | Directive (new type) | Tax/tribute forgiveness at Treasury cost; a relief-configured Ministry gets an AP/Treasury discount on Remit during an active Cooling flag | Treasury | General/Global Crisis of the 17th century (Maunder Minimum onset) | 2.8 |
| Directive: Fiscal Reform | Directive (reverse-scale — PA issues it to itself) | Resolved collectively by privileged faction ladders via Ministry/Consulta acting as the veto surface | Craters privileged Disposition faction-wide if Complied; Defy (concealment) writes a hidden Π-raising Precedent | Ancien Régime France / Estates-General (1787–89) | 2.9 |

---

## 10. NEW verbs / mechanics with no clean single-verb parent

| Action | Extends | Mechanic | Cost | Motivating event(s) | § |
|---|---|---|---|---|---|
| Donative | Levy + Hold Court (paired, see §4/§7 rows) | Spends Treasury to buy a contender's Stage-1 military-Loyalty check during a succession contest | Treasury; leaves Mandate depressed and Π high unless paired with Ratify | Year of the Four Emperors (Rome, 69 CE) | 2.1 |
| Storm-Season Staging Exposure / Storm-Season Withdrawal | Muster/Conquest (timing rule / timing sub-choice) | Multi-season fleet anchoring inside a storm-season window accrues a shared storm-loss multiplier scaled to season-of-year; Withdrawal cedes tempo instead of rolling | Cedes tempo (Withdrawal) or risks a shared multi-faction Mil loss (Staging) | Kamikaze typhoons vs the Mongol fleets (1274 & 1281); The Great Hurricane of 1780 | 2.8 |
| Purpose-Built Galleon | Levy (quality/quantity fork, gated) | Cheap/fast Levy fields more hulls at a higher storm multiplier; Purpose-Built costs more per hull but lowers it — unlocked only after a Crisis fires once | Higher per-hull Treasury cost; unlock gated behind a prior loss | Spanish Armada destroyed by Atlantic storms (1588) | 2.8 |

---

## 11. Note on same-mechanic reskin clusters (§2.11, flagged not resolved)

The historical-concerns catalogue itself did not collapse these — flagged here per the companion
governance docket's judgment-pass discipline (`designs/audit/2026-07-10-...`, §7) for a future
ratification pass to fold together rather than ship as N near-duplicate verbs:

- **Standing famine-buffer facility**, proposed three times under three names for the same underlying
  mechanic (a Sponsor/Develop-funded stock that auto-draws against a famine/drought roll): **Ever-Normal
  Granary** (§2.5, §2.6, §2.7) and **Civic Granary** (§2.8). Recommend consolidating to one facility
  (`Ever-Normal Granary`) with a `Civic` variant flag for the guild/city-funded ownership case rather
  than two facility types.
- **Currency-clearing Directive**, proposed twice for the same underlying mechanic (retire a bad-money
  tag, reset Levy Ob, raise baseline Π for a recovery window): **Recoinage** (metallic debasement case,
  §2.9) and **Currency Reset** (land-backed fiat collapse case, §2.9). The source explicitly notes the
  land-backed case "cannot reset as cleanly as a metallic debasement" — likely two severity tiers of one
  mechanic rather than two mechanics.
- **Convoy/fleet timing-exposure mechanic**, proposed three times under event-specific names for the
  same underlying "staging inside a hazard window raises a shared severity roll" shape: **Storm-Season
  Staging Exposure / Storm-Season Withdrawal** (§2.8, naval), **Flota Scheduling** (§2.8, convoy-specific),
  and implicitly the Loading-Delay-Friction interaction underneath both. Recommend one generic "Hazard-
  Window Staging" sub-rule parameterized by hazard type, with Flota Scheduling and Storm-Season Staging
  as its two named instances rather than independent mechanics.
- **Crisis-gated post-loss unlock**, the general pattern behind **Lighthouse** (unlocked only after a
  storm Crisis fires once), **Purpose-Built Galleon** (unlocked only after a Crisis fires once), and
  **Coalition Fortify Pool** (unlocked by surviving an existential siege) — three instances of "you must
  suffer the loss once before the mitigation becomes purchasable." Worth naming as one general design
  rule (a "hard-won lesson" unlock class) rather than three bespoke gates, since a Godot implementer will
  otherwise re-derive the gating condition three separate times.
- **Recall vs. Monopsony Enforcement vs. Quo Warranto/Nationalize Charter/Charter Review**, all variants
  of "a legitimacy-gated route to strip an actor's independently-held grant/Charter/franchise" at
  different scales (an appanage prince's troops; a repudiated trade Compact; a foreign Charter). Not
  necessarily mergeable (different holders, different Directive families) but worth a single cross-
  reference note in a ratification pass so they're implemented against one shared "strip-a-grant"
  sub-resolver rather than three independent ones.

---

*End of Part 42. Cross-references: source catalogue
`designs/audit/2026-07-10-historical-concerns-action-catalogue/historical_concerns_action_catalogue_v1.md`
§1–§4 (executive framing, full catalogue, ripple chains, cross-reference against the companion
governance docket's 44 proposals); compiled event cards `designs/architecture/governance_compendium_v1/
event_cards/*.md` (HEV-* IDs, §2.1–2.10 + §3 ripple chains in `30_ripple_chains.md`). This Part performs
no new ratification — flip status lines in the source docs first, then update this Part's own
`## Status:` line to match, per CLAUDE.md §"Merging a PR ratifies its PROPOSED contents by default."*
