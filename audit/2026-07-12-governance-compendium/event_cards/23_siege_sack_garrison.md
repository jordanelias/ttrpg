# Event Cards — Siege / Sack / Occupation / Garrison (Section 2.3)

*Key: `siege_sack_occupation_garrison_crises`. Two spines: **unpaid garrisons treat plunder as wages** (Contribution System / Settle Arrears / mutiny contagion), and **pre-crisis Fortify tier is the win/loss table** (Inundation, Coalition Pool, Circumvallate).*

### HEV-SIEGE-01 — Sack of Magdeburg (1631, Holy Roman Empire) · Crisis
- **Historical grounding:** Unpaid Catholic League garrison storms and sacks the Protestant city after Tilly's siege breaks down into massacre and fire — §1.3/§1.3a/§1.4/§1.6.
- **Trigger:** `Extract/Tax at severe magnitude AND Defy AND Π≥8 AND no relief in range AND besieger.Treasury < garrison upkeep (unpaid-troops flag)`
- **Response branches:** On storm: Order→0, catastrophic Prosperity, a durable regionally-legible `Hated`/legendary-infamy Reputation; the besieger's unpaid-garrison Debt turns plunder into wages, worsening the severity table even under restraint orders.
- **Follow-on (FO):** An empire-wide `magdeburgisieren` Precedent that *lowers* Defy-appeal locally (terror compliance) while *raising* Grudge/Intrigue regionally — a Precedent that cuts opposite ways by scale.
- **Introduces (Action):** Contribution System / Kontributionssystem (new negotiated-extorted Levy method, sibling to Encabezamiento, funding garrison upkeep from the occupied region).
- **Loop:** Besieger Treasury below upkeep modifies the Crisis severity roll upward regardless of officer intent; the Contribution System keeps it solvent pre-siege and removes the modifier, at the cost of Debt/Grudge tags in the *occupied* territory taxed.

### HEV-SIEGE-02 — Spanish Fury at Antwerp (1576, Low Countries) · Crisis
- **Historical grounding:** Unpaid Spanish tercios mutiny and sack their own garrisoned host city — §1.3/§1.6 Debt "fires when due"/Treat chit, ED-SE-0005.
- **Trigger:** `Debt(garrison_pay) unresolved ≥3 seasons AND besieger Treasury critically low AND host Prosperity high`
- **Response branches:** Garrison mutinies and sacks its own host — Order/Prosperity collapse + a Grudge written at *every loyalist settlement that hears* (contagion).
- **Follow-on (FO):** A "loyalist provinces petition to remove the garrison" Friction chaining to a cross-settlement Treat/Bargain coalition (Pacification-of-Ghent analogue).
- **Introduces (Action):** Settle Arrears (new Levy sub-action: pay down garrison-pay Debt before it escalates, resetting the clock).
- **Loop:** Letting the Debt go uncalled raises Mutiny draw-weight and severity; Settle Arrears removes the trigger; if it fires, contagion Grudge at *other* settlements raises their future Defy-propensity — mutiny as contagious political-capital loss.

### HEV-SIEGE-03 — Siege of Leiden (1574, Dutch Republic) · Crisis
- **Historical grounding:** Leiden endures prolonged Spanish siege, is relieved by deliberate flooding of the polders, and is rewarded with a founding charter — §1.3 Fortify/Sponsor, §1.6.
- **Trigger:** `under active siege AND Π≥8 AND Defense below survival threshold`
- **Response branches:** Order/Prosperity attrition scales with duration and starting Defense, prior Fortify reduces both.
- **Follow-on (FO):** *Surviving* unlocks a Sponsor "Found an Institution" (university/charter) card converting the ordeal into durable `Generous`/`Just` Reputation + Precedent.
- **Introduces (Action):** Inundation (mid-Crisis-only Fortify-adjacent method: trade Prosperity — flood productive land — for an immediate Defense/relief bonus).
- **Loop:** Pre-crisis Fortify sets the baseline casualty/duration table exactly when the card fires; Inundation is the costly fallback when that was insufficient, and surviving unlocks the Sponsor payoff no Fortify-only path grants.

### HEV-SIEGE-04 — Great Siege of Malta (1565, Mediterranean) · Crisis
- **Historical grounding:** The Knights Hospitaller withstand an existential Ottoman invasion of Malta on the strength of prior fortification and eventual relief — §1.3 Fortify/Sponsor, §1.6 Grudge, mass_battle_v30 relief.
- **Trigger:** `large invading force AND Fortify tier insufficient alone vs force-ratio AND strategic_value==existential`
- **Response branches:** Survival probability reads directly off cumulative pre-crisis Fortify.
- **Follow-on (FO):** Surviving seeds a rare "Pan-Faction Sponsorship" Opportunity (allied/Church Treasury into a new fortress-settlement) + a Precedent easing future cross-faction pooling.
- **Introduces (Action):** Coalition Fortify Pool (new acquisition path: multiple factions jointly pre-fund a threatened settlement's Fortify ahead of a known Crisis).
- **Loop:** Accumulated Fortify (often motivated by an old unresolved Grudge) is the single stat deciding the win/loss table; surviving unlocks cross-faction pooling that raises future capacity beyond any one faction — investment and survival compound across crisis cycles.

### HEV-SIEGE-05 — Siege & Sack of Drogheda (1649, Ireland) · Crisis
- **Historical grounding:** Cromwell's forces deny quarter after the town's defiance, driven by unresolved atrocity grudges, and follow with mass confiscation of the population's land — §1.4/§1.6 Grudge+Outlawed, mass_battle_v30, faction_action.py.
- **Trigger:** `Grudge(unresolved_atrocity) active AND Directive.type∈{Suppress,harsh} AND Defy`
- **Response branches:** A "quarter denied" branch — severe Order/Reputation loss beyond the normal table + a new Outlawed tag marking the population for confiscation.
- **Follow-on (FO):** Seeds a "Settle & Confiscate" Govern/Conquest action (mass roster/land reallocation) writing a fresh Outlawed tag raising Grudge/Intrigue for generations.
- **Introduces (Action):** Settle & Confiscate (new post-Conquest domain action: forced subnational faction-roster replacement).
- **Loop:** An old Grudge raises the punitive branch's severity ceiling; executing Settle & Confiscate writes a new Outlawed tag raising future Grudge/Intrigue — a self-reinforcing spiral the Ledger makes explicit and inheritable across governor succession.

### HEV-SIEGE-06 — Colonial Billeting / Quartering Acts (1765–1774, British American colonies) · Friction
- **Historical grounding:** Forced quartering of troops on colonial hosts escalates from resented Force-method Keep Order through Petition and into Boston-Massacre-style violence — §1.3 Keep Order Consent/Force/Clergy, §1.4 Host, §2.3 escalate.
- **Trigger:** `Keep Order.method==Force (or Directive Quarter) in a Prosperity-above-threshold settlement AND PS trending negative`
- **Response branches:** Ignoring the Petition raises Π and escalates to a Boston-Massacre-style Crisis (Order loss, Actor-Disposition collapse, Grudge).
- **Follow-on (FO):** The Crisis chains to a Directive-tier authority shift from negotiated to unilateral Force-method, seeding a longer rebellion Ambition arc.
- **Introduces (Action):** Quarter (new Directive type, sibling to Host, forcing Force-method Keep Order over the governor's preference).
- **Loop:** Force-method accrues PS loss + Grudge each season; an ignored Friction fires a Crisis that hardens Actor-Disposition and makes Consent politically *unavailable* going forward — a ratchet narrowing the governor's own future menu toward more Force (the 1765→1774 shift).

### HEV-SIEGE-07 — Mongol Siege of Baghdad (1258, Abbasid Caliphate) · Crisis
- **Historical grounding:** The Mongols besiege and raze Baghdad after the Caliph refuses submission, permanently destroying the irrigation infrastructure underlying its prosperity — §1.3 Develop, §1.4 Defy, §1.6 durable-infrastructure-loss extension.
- **Trigger:** `capital-tier Defy with no submission AND no relief coalition AND internal Grudge/split unresolved`
- **Response branches:** A rare branch *permanently caps* the Develop ceiling (destroyed irrigation) — a multi-generation wound, not a one-season loss.
- **Follow-on (FO):** Long-horizon Develop-degradation state + an Intrigue among survivors over the diminished settlement.
- **Introduces (Action):** Rebuild Infrastructure (high-cost multi-season Develop sub-project restoring a capped ceiling).
- **Loop:** An unresolved internal split raises the probability of the *permanent* loss branch; once fired, the ceiling stays capped until Rebuild completes, narrowing the governor's viable menu (heavier Levy/Treat reliance) for the rebuild's duration.

### HEV-SIEGE-08 — Nadir Shah's Sack of Delhi (1739, Mughal Empire) · Crisis
- **Historical grounding:** Riots against Nadir Shah's occupying force trigger open-ended reprisal massacre, checked only by a negotiated fixed indemnity — §1.3 Treat/Force, §1.3a Compact fixed-term, §1.4 Bargain, faction rank-gated authority.
- **Trigger:** `occupation active AND Keep Order Force fails (riot) AND Π≥8`
- **Response branches:** Open-ended reprisal massacre unless a sovereign-rank actor invokes Bargain converting it to a bounded Compact indemnity (fixed payment ending the plunder).
- **Follow-on (FO):** Successful Bargain writes a fires-once Compact + Reputation shift; unresolved reprisal seeds further Grudge/Intrigue.
- **Introduces (Action):** Sovereign Bargain (rank-gated Directive-Bargain, Standing-6+ only, converts open-ended loss to a one-time Compact).
- **Loop:** A Force-failure raises severity proportional to existing Friction; a high-rank Sovereign Bargain caps it (better conversion at higher Standing) — a rank-scarce mitigation unavailable to an ordinary governor.

### HEV-SIEGE-09 — Siege of Numantia (134–133 BCE, Roman Hispania) · Crisis
- **Historical grounding:** After repeated failed assaults and a broken treaty, Scipio Aemilianus circumvallates Numantia into slow starvation; the defenders choose mass self-destruction over surrender — mass_battle_v30/faction_action.py Muster/Conquest, §1.3a broken-treaty flag, §1.6.
- **Trigger:** `besieger repeated failed Conquest attempts ≥N against same settlement AND Grudge(broken_treaty) active`
- **Response branches:** Circumvallate resolves slowly but near-guarantees capitulation without assault casualties, but broken trust forces the defender toward the worst-case branch (total resistance / mass self-destruction).
- **Follow-on (FO):** Writes a "no negotiated peace available" flag permanently removing Bargain/Treat between them for the conflict.
- **Introduces (Action):** Circumvallate (new besieger Conquest method: trade tempo — multi-season, AP/Treasury-heavy — to near-eliminate assault casualties).
- **Loop:** A previously reneged Compact writes a Grudge closing the Bargain option, pushing the besieger toward Circumvallate and the defender toward maximal resistance — the earlier broken deal narrows both sides' menus in the eventual siege.

### HEV-SIEGE-10 — Siege of Orléans (1428–1429, Kingdom of France) · Crisis
- **Historical grounding:** The relief of besieged Orléans, led by Joan of Arc's improvised muster, reverses the Dauphin's contested legitimacy and fast-tracks his formal coronation — §1.3 Hold Court/Precedent, §1.4, §1.0b Recognition Fork, Standing-3 Formal Recognition.
- **Trigger:** `settlement legitimacy_linked to a contested claimant's Recognition track AND active siege AND Recognition contested/pending`
- **Response branches:** The outcome writes directly into the claimant's Recognition Fork (a fall costs a rank-track setback regardless of local stats; a relief win auto-triggers a Formal Recognition / coronation Event).
- **Follow-on (FO):** A successful relief seeds an Ambition card fast-tracking the low-Standing NPC who led the improvised relief, bypassing the normal Initiation Gate.
- **Introduces (Action):** Improvised Relief (new Muster variant bypassing exhausted Levy capacity, paired with a "Legitimacy Siege" flag routing the Crisis into a Recognition Fork).
- **Loop:** Legitimacy-flagging means a fall costs a faction-ladder rank independent of local Fortify/Order; a relief that saves it triggers a Recognition Event for the leading NPC — an alternate non-Initiation-Gate advancement path that exists only because the Crisis was legitimacy-flagged.
