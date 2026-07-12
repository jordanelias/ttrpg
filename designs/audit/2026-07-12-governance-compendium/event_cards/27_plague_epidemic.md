# 2.7 Plague and epidemic disease, climate/trade-correlated (Climatic ↔ Geographical/Economic)

*Key: `historical-concerns-plague-epidemic-v1`. The through-line: **the vector is a governance action** — Refuge Walls overcrowding, an un-staged Muster redeploy, a single-corridor Develop, a famine-relief Treat, a Host Directive routing troops, a waived quarantine inspection — and the response verb (Force/Segregation) that ends the epidemic manufactures the next political Crisis.*

### HEV-PLAGUE-01 — Plague of Athens (430 BCE) · Crisis
- **Historical grounding:** Thucydides II; NatGeo; HistorySkills.
- **Trigger:** `Π≥8 AND recent Fortify(Refuge Walls) within 2 seasons AND Order≤3 AND Overcrowding tag`
- **Response branches:** Sponsor relief (Order+1, Π−2, downgrades but doesn't clear Overcrowding); Force (Order+1 but Disposition−1 all Actors, Grudge); Ignore (Π+3, patron-NPC mortality check).
- **Follow-on (FO):** A failed patron mortality check seeds a succession Crisis (Pericles' death mid-plague); a persisting Overcrowding reseeds the Crisis next eligible season.
- **Introduces (Action):** Refuge Walls (fourth Fortify method: shelter rural population for Defense+1/PS bump but writes a durable Overcrowding tag unless paired same-season with Sponsor relief or Fortify:Walls sized to the influx).
- **Loop:** Refuge Walls without same-season relief raises Π and stacks Overcrowding — the literal trigger of the Epidemic card, so the defensive choice reproduces itself; if it fires and the patron check fails, the succession vacancy removes the AP/Standing the governor needed for the relief Sponsor — the historical trap in mechanical form.

### HEV-PLAGUE-02 — Antonine Plague (165–180 CE) · Crisis
- **Historical grounding:** Wikipedia; WHE; PLOS One (2025) SIR/SEIR; Masaryk CEDRR.
- **Trigger:** `last action Conquest(frontier) AND next action Muster(redeploy to interior) AND NOT used Staged Demobilization AND Order≤4`
- **Response branches:** Fires in every interior settlement receiving troops (Order−1, Prosperity−1, Mil−2/−3 reversing the season's troop purchase) unless Sponsor/Consent absorbs it.
- **Follow-on (FO):** Repeated hits across the redistribution wave seed a faction-level "the muster route is a plague road" Friction raising the Ob on the faction's next Conquest via a lowered mil-advantage signal.
- **Introduces (Action):** Staged Demobilization (Muster sub-choice: extra Wealth + a season's delay to route legions through a quarantine interval, trading faster Mil gain for suppressing the trigger).
- **Loop:** Frontier Conquest + an un-staged Muster is the mechanism raising the Crisis weight in every receiving settlement; if it fires it strips Mil from the very Muster that caused it, lowering the faction's mil-advantage signal and its Conquest weight next dispatch cycle — a direct write-back from event severity into the faction AI's action-selection odds.

### HEV-PLAGUE-03 — Plague of Justinian (541–549 CE) · Crisis
- **Historical grounding:** Wikipedia; OeAW; Mordechai & Eisenberg, Past & Present 244 (2019); Mordechai et al., PNAS 116(51) (2019).
- **Trigger:** `Precedent("single-corridor-trade") AND external_shock(climate) AND Prosperity drop ≥2 in one season AND Π≥7`
- **Response branches:** Sponsor Emergency Wage Edict (Order+1, floor held, Debt tag — the edict must be renewed or Disposition−2); Force (Order+1 but PS−1 + Grudge); Ignore (Π+2, Prosperity−2, `chokepoint confirmed fragile` deepens).
- **Follow-on (FO):** The deepened Precedent raises repeat-Crisis weight on the next external_shock + seeds a Guild Treat/Compact petition to formalize an alternate route.
- **Introduces (Action):** Diversify Corridor (Develop funding sub-method: 1 extra AP + slower Prosperity to route through 2+ independent corridors, writing a `route-diversified` Precedent lowering future weight).
- **Loop:** The cheaper single-corridor Develop funding *writes the trigger predicate*, so a Prosperity-maximizing governor is most exposed when a climate shock lands; once it fires Keep Order narrows to the costlier Force unless Diversify Corridor or a Wage Edict was banked — the event retroactively punishes the earlier method choice.

### HEV-PLAGUE-04 — The Black Death (1347–1351) · Friction
- **Historical grounding:** Bauch & Büntgen, Comm Earth & Env (2025); Wikipedia Black Death/migration; Cambridge news.
- **Trigger:** `Prosperity≤2 AND external_shock(climate/famine) AND Treasury≤threshold`
- **Response branches:** Treat (Emergency Grain Compact with a distant supplier: Prosperity+1 but writes a Debt tag AND a Contagion Vector flag); Directive-Bargain for Crown relief (partial, no Contagion flag, Standing-debt); Ignore/refuse (no flag but escalates to a Famine Crisis next season).
- **Follow-on (FO):** A Contagion-Vector-flagged settlement near-certainly draws a Plague Crisis next season regardless — the double-bind: grain now/plague later, or famine now with no plague.
- **Introduces (Action):** Emergency Grain Compact (Treat famine sub-case: Influence+history roll vs a distant supplier, Debt-chit + a Contagion Vector flag when the supplier is on an unvetted long-distance corridor).
- **Loop:** The famine-relief Treat branch trades an immediate Prosperity save for a guaranteed-weight Plague draw via the Contagion Vector — the same climate shock that makes the Treat attractive is what carried the pathogen on the relief shipment, reproducing the historical double-edge instead of a free relief action.

### HEV-PLAGUE-05 — Venice Lazzaretto / 1630–31 quarantine failure · Crisis
- **Historical grounding:** Sapiens.org; CDC EID (2013); Alfani/Melegaro, Scientific Reports (2020); Wikipedia 1629–1631 Italian plague.
- **Trigger:** `Quarantine_Tier≥1 (trade-vector protected) AND external_shock(military_transit — Host Directive or Levy troop movement) AND Π≥8`
- **Response branches:** Because the tier only discounts *trade*-vector triggers, this fires at near-full severity regardless (Order−2, Prosperity−1, Reputation→Weak); responses apply at no discount.
- **Follow-on (FO):** Seeds an Intrigue circulating the failure as evidence the Sanità is captured/incompetent → a Petition to defund it (rolling back the tier investment).
- **Introduces (Action):** Sanità Lazzaretto (Fortify facility, 2 AP+Treasury, granting a Quarantine Tier 0–3 reducing draw-weight of Plague cards whose trigger references a *trade/sea* vector — explicitly not military-transit).
- **Loop:** The facility lowers Plague odds only along trade predicates, so a governor treating it as blanket protection and complying with a Host Directive routing troops through eats a full-severity Crisis, which writes the Reputation/Intrigue follow_on threatening the very investment that didn't cover the actual vector — asymmetric mitigation as mechanics, not flavor.

### HEV-PLAGUE-06 — Cocoliztli epidemics 1545 & 1576 (New Spain) · Crisis
- **Historical grounding:** Acuna-Soto et al., EID 8(4) (2002); PMC7110390; Wikipedia.
- **Trigger:** `Assessment(assessed_base) AND seasons_since_Survey≥8 (never refreshed) AND external_shock(drought, multi-season) AND Prosperity < assessed_base×0.5`
- **Response branches:** The Extract Directive keeps charging the stale base through the drought (§1.3a failure mode), stripping below subsistence (Prosperity−3, Order−2, mass-mortality flag, Grudge(Crown)).
- **Follow-on (FO):** Seeds a repeat harder-Ob Crisis each season until a Survey/Negotiate-Quota resets the figure — an escalating loop.
- **Introduces (Action):** Emergency Resurvey (extends the live Survey sub-verb: usable outside its ~8-season cooldown when an external_shock flag is active, at an Ob penalty, to refresh the Assessment before Extract strips the settlement).
- **Loop:** Skipping Survey during a megadrought is a modeled trap: Extract reads a stale-high base and drives Prosperity below subsistence (the trigger), the Crisis spikes Π and writes Grudge(Crown) that raises the Ob on the *next* Survey/Negotiate attempt (Reputation Weak/Hated makes renegotiation harder) — the neglect that caused the collapse also makes it harder to fix.

### HEV-PLAGUE-07 — Chongzhen drought / Great Plague of 1633–1644 · Crisis
- **Historical grounding:** Climate MDPI 11(3):71 (2023); Copernicus CoP (2024); Wikipedia late-Ming plague.
- **Trigger:** `Granary_FacilityTier==0 (never Developed) AND external_shock(drought ≥3 seasons) AND faction military Levy-extraction ≥ high (war Directives crowding out settlement AP)`
- **Response branches:** Famine→plague→unrest at full severity (Prosperity−3, Order−3, a rebel-warlord Ambition on a named Actor); Sponsor relief is the only mitigation but competes for the same AP the Extract Directive consumes.
- **Follow-on (FO):** If under-resourced, seeds a rebel Ambition (Li Zicheng) accelerating with every unserved famine Need → an open Conquest-target for a rival.
- **Introduces (Action):** Ever-Normal Granary (Develop funding method stockpiling a famine buffer, releasable via Sponsor, competing for the AP a Directive's military Extract already draws).
- **Loop:** Heavy Levy/Extract starves the settlement's AP for the Granary Develop, so when the drought fires no buffer exists and the cascade hits full severity; the Order collapse + rebel Ambition further degrades Disposition, raising future Levy resistance and the faction's own extraction costs — granary neglect and extraction pressure feed each other bidirectionally.

### HEV-PLAGUE-08 — Great Plague of Marseille (1720) · Intrigue
- **Historical grounding:** Wikipedia; STAT News (2020); Rodama blog; edwardworthlibrary.ie.
- **Trigger:** `Quarantine_Tier≥1 (Sanità exists) AND Guild Standing ≥ threshold AND Guild.Disposition(governor) high (patronage) AND a trade-fair Treasury deadline`
- **Response branches:** Hold Court gains a Ratify/Reject/Amend branch — Ratify (waive inspection: ship clears, Guild Influence+1, but the Quarantine_Tier discount is voided for that shipment, spiking the Plague Crisis weight to near-certain), Reject (Guild Master−2, Grudge, no spike), Investigate first (exposes the bribery vector for the four-way disposition).
- **Follow-on (FO):** Ratify seeds the Plague Crisis at near-guaranteed weight; if it fires, a Demotion chain against the Guild Master who pressured the waiver.
- **Introduces (Action):** Quarantine Waiver Petition (new Hold Court branch, structurally identical to Ordenanza Ratification §1.3c, Ratify voiding that shipment's tier protection).
- **Loop:** A high-Standing/Disposition Guild spends patronage to push Hold Court toward Ratify, zeroing the Sanità discount for one shipment and spiking the Plague weight; if it fires, the Grudge/Reputation collapse hits both governor and the Guild Master's own Standing (a public-scandal-class §1.0a trigger dropping the Master 2 ranks) — the event punishes the same faction-ladder leverage that produced it.

### HEV-PLAGUE-09 — Third Plague Pandemic (from 1894) — Hong Kong, Bombay, steamship spread · Crisis
- **Historical grounding:** Wikipedia 1894 HK plague / Third pandemic; JMVH; Grokipedia Bombay.
- **Trigger:** `recent Keep Order(Force:Segregation Camps) within 2 seasons AND Order still ≤2 AND Grudge(magnitude≥2) AND Π≥8`
- **Response branches:** The prior forced-segregation resolves the epidemic pressure (Order recovers, Π drops) but the card is the political bill — an Intrigue "assassination plot" against the governor/administrator scaled to the Grudge the Force generated.
- **Follow-on (FO):** A successful assassination (W.C. Rand, 22 June 1897) forces a Recall/succession + Π spike; detected/countered → a durable Reputation hit without the succession shock.
- **Introduces (Action):** Segregation Camps (harsher Force sub-branch under Keep Order, buying a larger/faster Π/Order recovery at double the Disposition penalty + a guaranteed Grudge + an assassination-class Intrigue draw-weight flag).
- **Loop:** Segregation Camps end a high-Π Plague Crisis fast (Order/Π recover) but the Disposition/Grudge cost is exactly the trigger for the assassination Intrigue — the action that solves the Crisis manufactures the next; because the underlying sanitation underinvestment that made Force "necessary" is untouched, repeated reaching for it accumulates Grudge faster than Order, converging on the Rand outcome rather than stability.
