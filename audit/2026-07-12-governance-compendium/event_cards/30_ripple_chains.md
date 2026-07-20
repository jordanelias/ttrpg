# 30 — Ripple Chains (THR- chained-card threads)

## Status: extracted verbatim from source audit — not yet vetted against the live card corpus

Source: `designs/audit/2026-07-10-historical-concerns-action-catalogue/historical_concerns_action_catalogue_v1.md`
§3 "Cross-domain ripple chains". Each chain there names the specific `follow_on` seed that carries
state from one step's card into the next step's trigger predicate — a `follow_on` writes a durable
Ledger tag / raises Π / sets a hidden stat, and the next card's trigger references exactly that
tag/Π/stat. Domains are tagged `[G]`eopolitical, `[g]`eographical, `[C]`limatic, `[E]`conomic.

Twelve chains are preserved below as THR entries, one per chain, in source order. Nothing has been
added, merged, or dropped from the source; wording of conditions/payoffs is condensed from the
source prose, not reworded to change meaning.

---

### THR-01 — The debasement→famine→coup spiral

**Domain path:** E→E→G→C→G

**Card sequence:**
1. Roman 3rd-c. *Levy:Debase*
2. Gresham's Hoarding Crisis (England Great Debasement) — with side-branches to the Ottoman
   capitulations / Sunset Review trigger and Zimbabwe *Develop:Redistribute*'s stale-Assessment FO
3. Ancien Régime Directive: Fiscal Reform
4. Great Famine 1315 (Needs-driven)
5. Muscovite Time of Troubles

**Advancing condition (per step):** `Levy:Debase` stacks `Capital-Posture:Debased` → Gresham's
Hoarding stalls Prosperity and drives capital out of circulation → the thinner base plus
`Capital-Posture:Debased` satisfies Fiscal Reform's `Debt-to-Prosperity over threshold, privileged
veto` trigger; a Defy writes the hidden `Concealed Deficit` Precedent that auto-escalates the next
drawn Crisis's severity → a General/17th-c. Crisis Cooling flag raises baseline Π everywhere and the
concealed deficit means no Remit slack, so Great Famine 1315 fires with `Σ(unserved Needs)`
uncushioned → the famine's FO (unserved 3+ seasons → Order collapse + rival-patron Intrigue) writes
`Reputation:Hated` + Grudge, satisfying Muscovite's pretender-Intrigue trigger
(`Reputation∈{Weak,Hated} during a leadership vacancy`).

**Terminal payoff:** the debasement four steps back is what ultimately unseats the dynasty.

---

### THR-02 — Chokepoint toll funds a private army

**Domain path:** g→E→G

**Card sequence:**
1. Danish Sound Dues / Toll
2. Kongo's "Lineage Head Arms Retinue"
3. Ottoman Interregnum / Toluid

**Advancing condition (per step):** the toll accrues foreign-faction toll-`Debt`; its FO seeds a
"rival contests the strait" Friction once Debt crosses threshold → the contesting rival, denied a
Compact, routes trade underground, satisfying Kongo's `untaxed trade node bypassing the Levy method`
trigger; the un-Ratified Wealth compounds into a private Military → Kongo's FO (un-Ratified lineage →
Crisis at next leader-loss) is exactly the Toluid mandatory-contest row (`≥2 contenders each holding
independent Military`).

**Terminal payoff:** the toll the governor built to enrich the settlement financed the very appanage
strength that fractures the faction. Recall Directive (Toluid) is the un-pulled lever.

---

### THR-03 — Single-commodity Develop → blockade → blockade-runner corruption → plague

**Domain path:** E→G→E→C

**Card sequence:**
1. Union Blockade
2. Spanish Fury / Antwerp
3. Blockade-runners (Anaconda defender branch)
4. Black Death "Emergency Grain Compact"
5. Plague Crisis

**Advancing condition (per step):** a single-commodity `Develop`-funding concentration makes the
faction blockade-vulnerable; the blockade's FO seeds successive garrison-funding-collapse Crises →
garrison-funding collapse satisfies Spanish Fury's `Debt(garrison_pay) unresolved ≥3 seasons` trigger
→ mutiny sacks the host; its FO writes contagion Grudge at loyalist settlements → to fund resistance
the governor Sponsors blockade-runners, whose FO seeds a corruption Intrigue (skimmed runner
profits) → the runner corridor is an unvetted long-distance route, satisfying the Emergency Grain
Compact's `Contagion Vector` condition; the relief shipment's FO near-guarantees a Plague Crisis next
season.

**Terminal payoff:** the commodity-concentration choice becomes an epidemic.

---

### THR-04 — Neglected dike diverted to war → flood → relocation → Charter fight

**Domain path:** g→C→g→G

**Card sequence:**
1. St. Elizabeth's Flood
2. Val di Noto 1693
3. Hanseatic Novgorod / Revoke Franchise **or** Suez / Nationalize Charter

**Advancing condition (per step):** a war Directive diverts St. Elizabeth's Flood dike-`Maintenance`;
a severe-storm roll fires the flood Crisis; its FO seeds Petition pressure toward a standing
institution if the settlement survives → if it doesn't, Weight drops below the survivability floor,
satisfying Val di Noto's relocation trigger (`Weight below floor AND Charter held by a
feudal/ecclesiastical actor`) → relocation is gated by Charter consent via Quo Warranto — a hostile
Charter-holder converts the disaster into a Revoke Franchise / Nationalize Charter fight (`the
holder's leverage has eroded`); the arbitration FO writes a `charters contestable by force` Precedent
lowering every future bypass bar.

**Terminal payoff:** a diverted dike ends in a constitutional precedent about who owns land.

---

### THR-05 — Un-staged Muster spreads plague that strips the war machine

**Domain path:** G→C→G

**Card sequence:**
1. Conquest (frontier)
2. Antonine Plague Muster (un-staged redeploy)
3. Chongzhen famine-plague cascade
4. Rebel-warlord Ambition → open Conquest-target

**Advancing condition (per step):** a frontier Conquest followed by an un-staged Antonine Plague
Muster redeploy fires the epidemic in every interior settlement; its FO seeds the faction-level
"muster route is a plague road" Friction → that Friction lowers the faction's mil-advantage signal,
and the interior Order−1/Prosperity−1 hits satisfy Chongzhen's trigger where
`Granary_FacilityTier==0` (Treasury was on the war, not granaries) → Chongzhen's FO seeds a
rebel-warlord Ambition that at threshold becomes an open Conquest-target.

**Terminal payoff:** the faction's own aggressive Muster manufactured the internal rebellion that a
rival now exploits. Staged Demobilization was the un-pulled lever at step 1.

---

### THR-06 — Overcrowding refuge → plague kills the patron → contested succession

**Domain path:** G/C→C→G

**Card sequence:**
1. Refuge Walls (without same-season relief)
2. Plague of Athens
3. Year of the Four Emperors / Anarchy
4. Extract Succession Oath (Anarchy action — the un-taken option)
5. "Baronial Free Agency" (recurring)

**Advancing condition (per step):** Refuge Walls without same-season relief stacks `Overcrowding`;
the Plague of Athens FO on a failed patron-NPC mortality check seeds a succession vacancy → that
vacancy, with the patron eliminated and the heir weak, is the Anarchy trigger (`heir.Disposition<3
AND comparable-Standing rivals`); a Donative-bought military win's FO reseeds the Crisis unless
Ratify closes it → if the win instead came via Extract Succession Oath never taken, the G≤1 SPLIT FO
seeds recurring "Baronial Free Agency."

**Terminal payoff:** a defensive-overcrowding choice at a single settlement cascades into a
nineteen-winter faction fracture.

---

### THR-07 — Siltation → merchant exodus → merchant-capital captures the ladder

**Domain path:** g→E→E→G

**Card sequence:**
1. Zwin/Bruges (un-dredged, SiltLevel + Guild tariff Comply)
2. "Merchant Exodus" Crisis
3. Fugger / Underwrite
4. Plassey / Jagat Seth

**Advancing condition (per step):** un-dredged Zwin/Bruges SiltLevel + Guild tariff Comply fires the
Merchant Exodus Crisis; its FO permanently transfers trade-Reputation to a named rival settlement →
the rival settlement's merchant surge satisfies the Fugger `Banking faction Standing ≥ threshold with
capital` trigger; repeated Underwrite Comply's FO seeds the Ambition where the financier claims a
Ministry/Consulta seat → with the Crown fiscally dependent, the Plassey / Jagat Seth Intrigue trigger
is met (`Treasury dependency on a Banking faction ≥ threshold, disaffected officer`); a funded-coup
Govern FO installs a diwani-equivalent Levy assignment.

**Terminal payoff:** a silted harbor ends with a merchant house running the province.

---

### THR-08 — Cooling epoch → correlated famine → cascade → mass demotion → recovery-incapacity

**Domain path:** C→C→G→G

**Card sequence:**
1. General Crisis Cooling flag
2. Great Famine 1315 / Deccan (simultaneous, multi-settlement)
3. Demotion Magnitude (faction_politics §1.0a)
4. Norse Greenland (implicit-abandonment FO)

**Advancing condition (per step):** the Cooling flag raises Π everywhere; a faction that keeps
issuing Extract/Tax (never built a relief Ministry) accumulates roster-wide Grudge, whose FO seeds a
multi-settlement Crisis cascade → the cascade fires simultaneous Great Famine 1315 / Deccan cards;
Deccan's `Divert Logistics to Muster` FO (if the faction is mid-Conquest) deepens each settlement's
famine one further tier → the correlated Grudge triggers concurrent Demotion Magnitude events on the
faction's own ladder; its FO strips exactly the Standing-4+ governors needed to authorize
Remit/relief → with governors demoted, the next Cooling-arc Π spike lands on a leaderless roster and
the Norse Greenland implicit-abandonment FO (a slow Dismissal, no ships) plays out at multiple
frontier settlements at once.

**Terminal payoff:** Remit + a relief Ministry were the un-built levers at step 1.

---

### THR-09 — Fixed quota through drought → resurvey-neglect death spiral → outlawry

**Domain path:** E→C→G

**Card sequence:**
1. Bengal 1770 (`Precedent(Fixed Revenue Quota)`)
2. Cocoliztli
3. Drogheda / Settle & Confiscate

**Advancing condition (per step):** a Bengal 1770 fixed-quota Precedent set in a normal season sits
latent as a silent check → a Cocoliztli megadrought fires with `seasons_since_Survey≥8`; Extract
charges the stale-high `assessed_base` below subsistence; the FO seeds a repeat harder-Ob Crisis each
season and writes Grudge(Crown) raising the next Survey's Ob → the compounding Grudge +
mass-mortality flag satisfies Drogheda's trigger (`Grudge(unresolved_atrocity) + harsh Directive +
Defy`); its Outlawed-tag FO raises Grudge/Intrigue in the territory for generations.

**Terminal payoff:** a bookkeeping choice (never refreshing the Survey) ends in a confiscation
regime. Emergency Resurvey was the un-pulled lever at step 2.

---

### THR-10 — Cheap hulls → storm loss → locked out of the fix → embargo vulnerability

**Domain path:** g/C→C→E→G

**Card sequence:**
1. Spanish Armada / Purpose-Built Galleon (cheap-Levy fork)
2. Rendezvous Failure
3. Edward III / Levy:Farm
4. ABCD Line / Multilateral Embargo

**Advancing condition (per step):** a cheap-Levy fleet meets the Rendezvous Failure Friction, whose
FO forces it onto a high-exposure route; the storm Crisis writes Debt/`Weak` on the Crown → that Debt
gates the Treasury for the Purpose-Built upgrade, locking the faction out of its own mitigation; the
residual Debt satisfies Edward III / Levy:Farm's default-pressure trigger if concentrated in one
Sponsor → a default's Outlawed-tag FO removes that Sponsor as a financier, and with the navy gutted
the faction's single-source resupply becomes an ABCD Line / Multilateral Embargo target
(`supermajority of one resource from one source`).

**Terminal payoff:** the coalition embargo collapses the response fork to Comply/Defy. Storm-Season
Withdrawal + Purpose-Built Galleon were the un-pulled levers.

---

### THR-11 — Quarantine complacency → trade-fair bribe → plague → assassination

**Domain path:** E→C→G

**Card sequence:**
1. Marseille / Quarantine Waiver Petition
2. Venice Lazzaretto (Plague Crisis)
3. Segregation Camps (Third Pandemic action)
4. Rand, 1897 (assassination-class Intrigue)

**Advancing condition (per step):** a high-Standing Guild's patronage leverage meets the Quarantine
Waiver Petition trigger; a Ratify voids the Sanità `Quarantine_Tier` for one shipment, whose FO
spikes the Venice Lazzaretto Plague Crisis to near-certain → the Plague Crisis, resolved via
Segregation Camps to recover Order fast, writes Grudge(magnitude≥2); its FO seeds an
assassination-class Intrigue → the assassination succeeding forces a Recall/succession scene and a Π
spike.

**Terminal payoff:** a merchant guild's trade-fair bribe three steps back kills the governor. The
unbuilt sanitation Develop that made Force "necessary" is the structural root.

---

### THR-12 — Untaxed mine wealth → depletion revolt → Standing transfer

**Domain path:** g→g→G

**Card sequence:**
1. Potosí / Mita
2. Erzgebirge
3. Mesopotamia salinization / Sumer→Akkad

**Advancing condition (per step):** Potosí / Mita conscription buys time against OreGrade depletion;
its FO accrues Grudge toward the Uprising Crisis + a permanent PS-decline tag → as the mine plays
out, the Erzgebirge fixed-charter Friction fires (`OreGrade below the charter baseline, no Tribunal
renegotiation`); its FO seeds a "New Rush" Opportunity at a rival settlement — miners and capital
migrate → the source settlement's collapsing Prosperity/PS + the rival's surge satisfies the
Mesopotamia salinization / Sumer→Akkad endgame pattern (a `Standing/Recognition transfer on the
faction ladder to a rival`).

**Terminal payoff:** resource geography playing out rewrites the rank ladder. Amalgamation + Tribunal
renegotiation were the un-pulled levers.

---

## Coverage note

12/12 ripple chains from the source §3 are represented above (THR-01 through THR-12), in source
order, with no chains merged or dropped.
