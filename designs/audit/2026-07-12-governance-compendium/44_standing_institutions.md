# Part 44 — Standing Crisis-Defusing Institutions + the Crisis-Recoverability Synthesis

## Status: PROPOSED (research-derived; not yet ratified into `faction_politics_v30.md` / `governance_play_redesign_v1.md` / `settlement_layer_v30.md`)

**Sources.** Three read-only research/stress artifacts, none of them canon:

1. `designs/audit/2026-07-10-historical-concerns-action-catalogue/historical_concerns_action_catalogue_v1.md` (filed 2026-07-10, Lane IN) — the ~94-entry historical event catalogue, whose per-entry **Loop** property is the raw material for this Part's synthesis. (The stress-test run below exercised a 58-card provisional deck; the broader authored/catalogued event surface across the co-filed `event_cards/` chunks runs to ~124 card-shaped entries. Where card counts differ, both figures are the sources' own — reconcile before ratification.)
2. `designs/audit/2026-07-11-proactive-governance-scale-research/proactive_governance_scale_research_v1.md` (filed 2026-07-11, Lane IN) — the four-scale proactive-governance research, which supplies the cross-scale standing levers (Standing Reserve, Territory Reserve Pool, Beacon Network, Cordon, Muster).
3. `designs/audit/2026-07-12-settlement-season-stress-sim/stress_test_synthesis_v1.md` (filed 2026-07-12, Lane IN) — the 7-seed × 5-season adversarial stress test of the PR#119 provisional governance mechanics, whose headline finding is that **the system is biased toward doom-spirals** (the tragic-downfall arc is the default, not the edge case).

**What this Part does — two jobs.**

- **Job 1 (§§44.1–44.4):** catalogue the class of **build-once standing facility/institution** that *auto-defuses a whole crisis family* rather than resolving one card at a time. For each: what it pre-empts, its build cost, its per-season upkeep/accumulation, and the crisis **draw-weight** (or severity) it removes.
- **Job 2 (§§44.5–44.8): the synthesis no prior pass made** — cross-walk the event catalogue's per-card **Loop** property against the stress test's doom-spiral finding, to classify which crises are **RECOVERABLE dips** versus **TERMINAL doom-loops**, and to map **which standing institution breaks which doom-loop.** This is the explicit bridge between the event research (2026-07-10/-11) and the balance findings (2026-07-12) — two dockets that until now spoke past each other.

**Two hard constraints carried from the corpus.**

- **No numbers cross into the engine here (CLAUDE.md §5).** Costs below are reproduced as the sources state them — prose tiers ("major-infra tier", "2 AP", "capital-only"), never synthesized values. The few explicit integers the catalogue itself cites (e.g. London Assize of Buildings "AP 2"; Sanità Lazzaretto "2 AP + Treasury") are reproduced *as cited* and are themselves PROPOSED, not ratified params.
- **Every item on this page is PROPOSED.** None is ratified canon. Per CLAUDE.md §2 (ED-1094), if a PR lands any of this as ratified, flip the relevant `## Status:` lines, the ED ledger, and `CURRENT.md` in the same merge.

---

## 44.1 The standing-institution class, defined

The historical catalogue's §2.4–§2.6 through-lines converge on one recurring object that is mechanically distinct from an ordinary action-verb spend:

> A **standing crisis-defusing institution** is a *build-once* facility, office, or charter that, once established, **automatically and pre-emptively lowers the draw-weight and/or the severity of an entire family of Crisis cards** — consuming its own accumulated stock or its own ring-fenced funding to blunt a shock, without a per-season reactive roll.

Four properties define the class and separate it from a reactive verb:

1. **Build-once, pre-emptive.** It must exist *before* the trigger predicate fires. The catalogue is emphatic and repeated on this: Berlin-Blockade **Alternate Corridor** "cannot be reacted into existence mid-Crisis"; **Sea Wall** must predate the storm window; the **Ever-Normal Granary** must have accumulated StockLevel across prior good seasons; the Great-Storm **Sheltered Dockyard** and **Lighthouse** are "gated behind having first suffered the loss." A crisis is, in the catalogue's own words, "a retroactive audit of a Fortify/Develop method skipped seasons earlier."
2. **Family-scoped, not card-scoped.** It removes weight from a whole *trigger family* (all flood cards, all drought/famine cards, all trade-vector plague cards) rather than resolving one card. This is what makes it worth a large up-front cost.
3. **Self-consuming or self-funding.** It either accumulates a stock that a crisis draws down automatically (Granary StockLevel, Standing Reserve), or it is funded by a **ring-fenced** stream immune to Directive competition (Water Board's dedicated levy). Its resilience logic sits *outside* the ordinary Treasury/AP cycle.
4. **Decoupling is the signature move.** Nearly every institution works by *decoupling* a defensive function from the pressure that would otherwise starve it: the Water Board decouples flood funding from the war Directive; the Standing Reserve decouples famine buffering from the Treasury cycle; the Beacon Network decouples alarm-timing from event magnitude. **The terminal doom-loops of §44.6 are, structurally, coupling failures** — and the institution is the de-coupler. Hold this claim; it is the hinge of the whole synthesis.

**A named anti-institution.** The catalogue also surfaces the inverse — a build that *creates* a crisis family rather than defusing one: **Refuge Walls** (Plague of Athens, §2.7). Sheltering rural population raises Defense/PS but writes a durable **Overcrowding** tag that is *the literal trigger* of the Epidemic card, "so the defensive choice reproduces itself." An institution audit must distinguish defusers from self-triggering builds; Refuge Walls is the canonical cautionary case.

---

## 44.2 The institution catalogue (build-once defusers)

Grouped by crisis family. Each row: what it pre-empts · build cost · per-season upkeep/accumulation · draw-weight or severity removed · source card (with the catalogue's citation). All PROPOSED.

### 44.2.1 Water / flood / siltation family

| Institution | Pre-empts | Build cost | Upkeep / accumulation | Draw-weight / severity removed | Source |
|---|---|---|---|---|---|
| **Water Board** | Flood Crisis triggered by `flood-defense Maintenance below threshold` (diverted to a war levy or weakened by peat extraction) + a severe-storm roll | Chartered institution — and pointedly **"a win condition, not an automatic grant"**: catastrophic flood resolution seeds cross-settlement Petition pressure to charter it; it is earned, not bought off a menu | Funded by **its own dedicated levy, ring-fenced from Directive diversion** | **Decouples flood funding from Directive competition** so a war-funding choice *cannot* starve flood defense — cutting the Crisis's odds independent of the Directive. The purest decoupling institution in the corpus | St. Elizabeth's Flood, 1421 (§2.5) — *Wikipedia; boards predate the flood* |
| **Water Magistracy** | Province-wide "Harbor Choked" Crisis from `shared Lagoon/Harbor SiltLevel` accumulating out of un-checked settlement Develop | Province-tier standing veto office **extending Ministry/Consulta** | Standing Ministry seat (recurring office upkeep) | Inserts a **check on shared SiltLevel before any Develop against the lagoon is approved** — prevents the province Crisis from accumulating at all; without it each Develop is locally rational but collectively silts the shared resource | Venice *Magistrato alle Acque* (§2.5) — *Wikipedia; ResearchGate lagoon diversions* |
| **River Conservancy Directorship** | The delayed, multi-decade **"Rising Lake Threatens [Settlement]"** downstream Crisis from a `RisingWaterLevel` fuse tag; and canal-silting regional collapse | Fortify **Scour-vs-Broad-Relief** engineering fork **+ a province-tier standing office like a Ministry seat** | Standing office upkeep | Governs the cross-node externality: the Scour choice *plants* the hidden downstream tag "that nothing there can see or defuse"; the Conservancy is the oversight layer that can choose Broad-Relief and see the fuse. **Note the trap:** the office reduces the odds of *unwitting* downstream harm, but the Scour verb it governs is itself the fuse-planter — the institution manages the fork, it does not make Scour safe | Yellow River / Pan Jixun, Ming (§2.5) |
| **Gauge-Indexed Levy (Nilometer)** | Famine-Unrest Friction→Crisis from a `fixed/unadjusted Levy` charged into a low-flood season | Requires a **Gauge facility (FacilityTier ≥ prerequisite)** | Auto-scaling; no per-season roll | **Ties the Levy formula to `FloodIndex`** so a bad flood auto-reduces extraction and **denies the Friction its escalation**; a fixed rate re-rolls the same Friction every low-flood season with rising Π/Grudge | The Nilometer, Egypt (§2.5) |
| **Corvée Desilting Levy** | The "Land Exhausted" depopulation chain from `SalinityLevel` compounding past crop-viability thresholds | Recurring labor-tax standing method | Recurring **Order −1**-class cost each season it runs | Keeps `SalinityLevel` below crop-loss thresholds; skipping lets it compound **irreversibly** (wheat "permanently lost by ~2000 BC") | S. Mesopotamia salinization (§2.5) |
| **Dredge Harbor** | "Merchant Exodus" Crisis (permanent Prosperity/trade-Reputation transfer to a rival) from harbor `SiltLevel` rising un-dredged | Develop funding/method | Per-use (resets SiltLevel); pairs with Treat holding tariffs flat | Keeps SiltLevel below the trigger and **denies the rival its Opportunity gain** — converts an otherwise-permanent Reputation transfer back into a reversible dip | Zwin siltation / fall of Bruges (§2.5) |

### 44.2.2 Famine / crop-failure / storage family

| Institution | Pre-empts | Build cost | Upkeep / accumulation | Draw-weight / severity removed | Source |
|---|---|---|---|---|---|
| **Ever-Normal Granary** (*changping-cang*) | Drought/famine Crisis (`DroughtIndex > severe` vs a famine floor) **and its rebel-warlord Ambition follow_on** | Develop Facility upgrade; **Sponsor each good season** to raise StockLevel | **Accumulates `StockLevel` in good seasons; decays if Treasury is diverted** (to Muster/Conquest) | Auto-drawn when drought draws: **caps severity, keeps state-run Levy relief available, and blocks the rebel-Ambition follow_on** — "same roll, radically different consequence gated by a prior Sponsor choice." The archetypal accumulate-then-auto-consume defuser | Chongzhen drought / North China Famine 1876–79 (§2.6, §2.7) — *Will & Wong, Nourish the People (Michigan 1991)* |
| **Granary Prefecture** | "Bread Dole Demand" Petition escalating to "Urban Riot" (`capital Population above threshold AND Grain_Import_Route disrupted`) | **Capital-only** Facility | Raises FacilityTier | Unlocks a Levy **"Subsidized Distribution"** method-variant and **lowers its AP cost/failure** when the Petition fires. **Caveat (a coupled cost):** Complying plants an **Entitlement Precedent** making any future *refusal* of a grain obligation cost extra Disposition — a granted entitlement is politically hard to revoke | Rome *Cura Annonae* (§2.6) — *Tacitus, Annals III–IV* |
| **Grain Ministry** (*Zahire Nezareti*) | "Bread Price Petition" escalating to "Hoarding Panic" | **Capital-only** enforcement Facility | Raises FacilityTier | **FacilityTier multiplies the fixed-price method's success.** **Bootstrapping trap:** repeated Petition failures at low tier both escalate to Crisis *and block the Develop path that would build the very Facility needed* — the institution is hardest to build exactly when most needed | Ottoman Istanbul provisioning / narh (§2.6) |
| **Civic Granary** | Needs-driven famine Crisis where `Σ(unserved Needs)` compounds Π to ≥8 with Prosperity below floor | Fourth Develop funding method | Standing reserve | **Lowers both the famine severity roll AND the `Σ(unserved Needs)` Π contribution** — attacks the doom-loop's Π-accumulation term directly | Great Famine 1315–17 / Bruges-Ypres-London reserves (§2.6, §2.8) — *W.C. Jordan (Princeton 1996)* |

### 44.2.3 Earthquake / eruption / fire family

| Institution | Pre-empts | Build cost | Upkeep / accumulation | Draw-weight / severity removed | Source |
|---|---|---|---|---|---|
| **Rebuild-to-Code** | Earthquake/Fire Crisis (`Π≥8 AND Weight≥high AND no Rebuild-to-Code tag AND crowd-multiplier`) | New Fortify method; **pre-emptive, or as Comply's follow-on** after a first quake | Durable Fortify tag | **Lowers future Earthquake/Fire trigger weight + severity.** No Rebuild-to-Code = higher draw-weight/severity | 1755 Lisbon (§2.4) — *Kendrick; §1.3/§1.6* |
| **Housing Code** | The pre-emptive *mirror* of Rebuild-to-Code: lowers the earthquake **casualty multiplier** in dense settlements | Fortify method regulating high-density dwelling. *(London Assize of Buildings 1189 variant, "Fortify: Code": cited as **AP 2, no Treasury**; +1 Defense + a standing "Building Code" flag dampening fire cards)* | Standing flag; property owners bear cost → **Disposition −1**; Precedent closes future boundary Petitions without a fresh roll | Lowers the structural-floor casualty multiplier; skipping it leaves the floor low (higher weight + casualties) | 1556 Jiajing/Shaanxi (§2.4); London Assize of Buildings 1189 (§2A/S7) |
| **Water Infrastructure** | Fire-following-earthquake severity (`no water-infrastructure Fortify tag AND a Force-heavy Keep Order history`) | Fortify Walls extension covering water-mains | Fortify tag | Raises fire-suppression capacity; skipping it raises fire-following-earthquake severity | 1906 San Francisco (§2.4) |

### 44.2.4 Naval / storm / fleet family

| Institution | Pre-empts | Build cost | Upkeep / accumulation | Draw-weight / severity removed | Source |
|---|---|---|---|---|---|
| **Standing Fleet** | Being **locked into Comply-only** on a raider-tribute card (a recurring per-season Treasury levy + Debt tag) | **Fortify + Muster investment** (banked) | Banked capacity | **Gates a Defy branch that literally does not exist until banked** — converts a Comply-only card into a real fork (a punitive fleet). *Two-edged:* investing adds an option *and* raises the stakes of a failed Defy (escalates to Crisis) | Barbary Tribute System (§2.2) — *NMAD; Barbary Wars* |
| **Sea Wall** | Coastal storm-Crisis severity against an anchored fleet | New Fortify method | Fortify tag | Lowers the coastal storm-Crisis roll, reducing an attacker's effective Mil; symmetrically, an over-staying attacker raises the same roll against itself | Kamikaze typhoons vs the Mongol fleets, 1274/1281 (§2.8) |
| **Sheltered Dockyard** | Storm Crisis against a fleet moored on cheap **Roadstead Mooring** | New Fortify **basing-location** method | Fortify tag | Sharply reduces storm severity vs the exposed roadstead; the upgrade (+ Lighthouse, + Underwriting) is itself **gated behind first suffering a storm loss** | Great Storm of 1703 (§2.8) |

*Related standing **conventions** (timing rules, not facilities, but same build-once/pre-emptive logic):* **Storm-Season Withdrawal** (Great Hurricane 1780 — cede tempo, take no roll), **Flota Scheduling** (Atocha 1622 — hard seasonal storm-avoidance window), **Staged Demobilization** (Antonine Plague — route legions through a quarantine interval), **Purpose-Built Galleon** (Armada 1588 — costlier hulls, lower storm multiplier; unlocked only after a Crisis fires once), **Annona Route Diversification** (LALIA 536–660 — centralization-vs-redundancy fork).

### 44.2.5 Siege / garrison family

| Institution | Pre-empts | Build cost | Upkeep / accumulation | Draw-weight / severity removed | Source |
|---|---|---|---|---|---|
| **Coalition Fortify Pool** | Existential siege loss (`large invading force AND Fortify tier insufficient alone`) | **New acquisition path: multiple factions jointly pre-fund** a threatened settlement's Fortify **ahead of a known Crisis** | Cross-faction pooled Treasury | Accumulated Fortify is "the single stat deciding the win/loss table"; surviving unlocks **further cross-faction pooling** (investment and survival compound across crisis cycles) | Great Siege of Malta, 1565 (§2.3) — *mass_battle_v30 relief* |
| **Contribution System** (*Kontributionssystem*) / **Settle Arrears** | The **unpaid-garrison severity modifier** and the Antwerp-style mutiny that sacks its own host (`Debt(garrison_pay) unresolved ≥3 seasons`) | New negotiated-extorted Levy method (Contribution System); a Levy sub-action (Settle Arrears) | Funds garrison upkeep from the occupied region; Settle Arrears resets the Debt clock | **Removes the severity modifier / mutiny trigger** — at the cost of Debt/Grudge tags in the *occupied* territory taxed. Mitigation with a displaced externality | Sack of Magdeburg 1631; Spanish Fury at Antwerp 1576 (§2.3) |
| **Alternate Corridor** | Enclave siege-by-attrition (`no contiguous land supply route AND rival Muster advantage`) | Sponsor extension, **hard-preconditioned on a prior Fortify airbase/corridor FacilityTier** | Ongoing AP + Treasury while active (bleeds Π down) | **"Cannot be reacted into existence mid-Crisis"** — survival is set entirely by a Fortify investment made years earlier; converts siege into a stalemate the besieger must formally lift | Berlin Blockade 1948–49 (§2.2) |

### 44.2.6 Epidemic family

| Institution | Pre-empts | Build cost | Upkeep / accumulation | Draw-weight / severity removed | Source |
|---|---|---|---|---|---|
| **Sanità Lazzaretto** | Plague cards whose trigger references a **trade/sea vector** | Fortify facility — cited as **2 AP + Treasury** | Grants a **Quarantine Tier 0–3** | Reduces draw-weight of trade-vector plague cards — **explicitly NOT military-transit.** The catalogue's clearest **asymmetric-mitigation** case: a governor who treats it as blanket protection and complies with a Host Directive routing troops eats a *full-severity* Crisis, which then seeds a Petition to defund the facility | Venice Lazzaretto / 1630–31; Great Plague of Marseille 1720 (§2.7) — *CDC EID 2013; Alfani/Melegaro, Sci. Reports 2020* |
| **Diversify Corridor** | Justinianic-type plague on a `single-corridor-trade` Precedent + a climate shock | Develop funding sub-method: **1 extra AP + slower Prosperity** to route through 2+ independent corridors | `route-diversified` Precedent | Lowers future plague/shock weight; the *cheaper single-corridor* Develop "writes the trigger predicate" — a Prosperity-maximizing governor is most exposed | Plague of Justinian 541–549 (§2.7) |

### 44.2.7 Fiscal / extraction family

| Institution | Pre-empts | Build cost | Upkeep / accumulation | Draw-weight / severity removed | Source |
|---|---|---|---|---|---|
| **Recoinage / Currency Reset** | The debasement ratchet: `Capital-Posture:Debased` stacks and the Gresham's-Hoarding / hyperinflation Crises they seed | **Rare Directive-level action requiring PA approval** beyond a single governor; costed steep | One-time (clears all `Capital-Posture:Debased` tags, resets Levy Ob) | **The only clearing action for the one-way debasement ratchet** — deferral makes the exit more expensive. *Currency Reset* (land-backed fiat) additionally writes a permanent "Precedent: Monetary Failure" raising baseline Π — "a land-backed fiat collapse cannot reset as cleanly as a metallic debasement" | England Great Recoinage 1560–61; assignat 1790s (§2.9) |
| **Regalian Mining Charter w/ Tribunal** | Mining boom-bust Friction→Ambition (`OreGrade below the charter baseline AND a fixed regalian charter still active`) + the rival-settlement "New Rush" migration | Depleting-resource-keyed Levy **cross-referencing `OreGrade`**, with a **Tribunal renegotiation** mechanism | Standing charter + periodic Tribunal review | **Running the Tribunal review before threshold keeps the rate credible** and denies the rival its departing-miner seed; locking the rate at peak and never renegotiating widens the fixed-terms/real-yield gap until Grudge/Friction fire | Erzgebirge *Bergordnungen* (§2.5) |
| **Sunset Review / Charter Review** | Stale-Concession drift: a foreign franchise's terms silently diverging from the real balance of Standing until a rival Guild's Petition forces a rupture | Low-AP periodic Levy/Directive sub-action | Periodic review | Reconciles the Concession Ledger to the real balance on the Crown's terms *before* the forcing Petition — "this category is defined by the long-run *absence* of the action, not its presence" | Ottoman capitulations; Hanseatic Steelyard 1598 (§2.10) |

### 44.2.8 Extraction-during-crisis (the anti-strip clamps)

Not a facility so much as a **standing rule/verb** that breaks the deterministic-strip loop (see §44.6, Pattern C):

- **Emergency Resurvey** (Cocoliztli 1545/1576) — extends the live Survey sub-verb to be usable *outside* its ~8-season cooldown when an `external_shock` flag is active, at an Ob penalty, to refresh a stale-high Assessment *before* Extract strips the settlement below subsistence.
- **Renegotiate Compact** (Laki 1783–84) — Treat/Levy sub-action to emergency-break an active fixed-extraction Compact mid-term, at a Precedent other settlements can cite.
- **Remission** (Bengal 1770) — a `Comply-rigid / Bargain-remit-and-report / Defy-withhold` sub-option on revenue-extraction Directives.
- **Remit** (General Crisis, §2.8) — a whole Directive type (tax/tribute forgiveness at Treasury cost); a relief-configured Ministry gets an AP/Treasury discount on Remit during a Cooling flag — Parker's "flexible institutions weather the shock."
- **Relief Obligation** (Irish Famine) — a workhouse/Poor-Law mechanic on Keep Order, available **regardless of a free-trade Precedent** — decoupling relief from export policy.

These are grouped here because the stress test's single most damaging structural doom-loop (the deterministic below-subsistence strip) is precisely a *missing-clamp* problem, and these are the clamps.

---

## 44.3 Cross-scale standing levers (from the proactive-governance research)

The 2026-07-11 four-scale research adds standing institutions that live **above** the single settlement — Territory- and Organization-scale defusers. All PROPOSED; all subject to the research's own caveats (§44.9).

| Lever | Scale | What it defuses / provides | Cost & accumulation | Note |
|---|---|---|---|---|
| **Standing Reserve / endowed institution flag** | Settlement | Dampens **one specific Π-event family** with self-replenishing logic **external to the Treasury cycle** | AP + seed Treasury/elite grain; minimal upkeep; tiered (None/Established) | The one settlement entry that "earns new state" — changes a settlement's *resilience curve against a specific event type*, not a Treasury deposit. Zhu Xi *she-cang* (S10). Its multi-settlement rollout is itself a Territory policy-adoption action |
| **Territory Reserve Pool** | Territory | A **shared cross-settlement buffer** that *moves surplus between* walled Treasuries in crisis — "impossible at settlement scale" | Reuses Prosperity/Treasury for the flow; a distinct shared store | Inca *Qollqa* (T2) / Song Ever-Normal (T10) — build once, share one implementation. Internal interest/replenish logic is **underspecified** in the source |
| **Beacon Network** | Territory | Tier 0–3: an attack Key on **any** member auto-emits a warning Key to networked settlements in hop-radius → **reduced surprise Ob / a free reactive tick** before their own event resolves | Treasury + territory AP to build; ongoing Treasury upkeep separate from any settlement; lapse auto-seeds a mutiny-risk trigger + Grudge | Ming *Jiubian* (T6). **The single strongest "new state" case in the corpus — but contingent** on Valoria's turn structure actually having inter-settlement *latency* to model (`engine_clock` is `doc: null`; §44.9) |
| **Frontier Cordon / Complete the Line** | Territory | A **Cordon-Complete** chain-topology flag: a defensive bonus that **pays out only while the chain is geographically unbroken**; one member below threshold drops it for the whole territory | Reuses per-settlement Defense (each member's Fortify) + Treasury toll income | Roman Limes / Hadrian's Wall (T4); Belgorod Line (T5) — second independent instance ⇒ build once |
| **Muster tag** | Territory | A **permanent Defense floor with NO ongoing Treasury upkeep**, paid for by a permanent reduction to Prosperity-growth (land granted to soldier-settlers); auto-answers Levy Directives with troops instead of Treasury | Founding AP/Treasury; then upkeep-free | Byzantine *kleisourai* (T11) / Ottoman *serhad* (T15). **Disposition-contingent — if garrison Disposition collapses it flips to Grudge and the garrison can refuse/defect.** A *different kind of decision* than Fortify (temp Defense for Treasury-now) |
| **Fugger Audit-Branch** (org-scale) | Organization | Converts a **hidden, silently-compounding embezzlement risk** into a **visible, scheduled** one, by reusing the Investigate resolver *inward* on the org's own branch officers | Org AP + an Investigate roll vs the manager's concealment | O5 — the cleanest "new identity from changing the *kind* of decision, not the number." **Directly relevant below:** it is the pre-built circuit-breaker for the stress test's Clerk-Corruption loaded-gun loop (Pattern F) |

---

## 44.4 Bridge preamble — why these two dockets belong on one page

Until now the event research (2026-07-10/-11) and the balance stress test (2026-07-12) have been read as separate work: one produced a *library of options*, the other produced a *list of gaps*. **They are the same finding seen from two ends.**

- The event catalogue's **Loop** property already encodes, card by card, whether a crisis is a *recoverable dip* or a *terminal spiral* — it simply never aggregated that judgment.
- The stress test found, subsystem by subsystem, that the live mechanics are *biased toward terminal spirals* — but it did not connect that to the catalogue's institution class, because the stress test ran on a **compressed 58-card kernel** that (per its own §0 verification layer) had *dropped* the standing-institution detail.

The synthesis is: **the standing-institution class of §44.2–§44.3 is precisely the missing circuit-breaker library the stress test says the system lacks** — but it only works pre-emptively, which is exactly why the stress test (a deliberate depth-3 *failure* sweep with no institutions pre-built) saw doom everywhere. §§44.5–44.8 make that rigorous.

---

## 44.5 The doom-spiral finding (stress test, restated)

The 2026-07-12 stress test's core, surviving-verification yield (its §0 downgraded two loud "author-everything" alarms as digest artifacts — see §44.9). The recurring **emergent** failure-cascade patterns, each an L1→L2→L3 shape that recurred across the 7 seeds:

| Pattern | Shape | Recurrence | Axis |
|---|---|---|---|
| **A — Demotion spiral** | Negative resolution_quality Key → rank held → 2 more failures → §1.0a Demotion fires → **Appeal fails** | **7/7 universal** — "the tragic-downfall arc is the default, not an edge case" | **Standing/rank** |
| **B — Π runaway / no circuit-breaker** | Grudges written → Π climbs → crosses the R-4 band cliff (Π 7→8, Intrigue→Crisis) and **pins** (no Grudge decay, no valve) | ~6/7 (S5 pinned at Π10 for 3 seasons) | World-state Π |
| **C — Compact/Assessment lock-in during a *worsening* crisis** | Survey locks assessed_base at pre-crisis Prosperity → Fiscal Stance reads stale figure → Prosperity falls → town stripped **below subsistence**, no reversal ~8 seasons, no defined below-subsistence state | ~4/7 (S4,S5,S6,S7) — **"a deterministic strip, not a probabilistic risk"** | Prosperity/extraction |
| **D — Collective-Liability cell-revolt stacking** | Bind the Cells → one infraction → whole-cell Disp−1 → stacks to 3 → **Cell Revolt Crisis** (Order→0/1, secession-class) | ~6/7 — "the Order tool becomes the crisis engine" | Order |
| **E — Patron-lapse un-shielding the queued Demotion** | w_d-high governor accrues negative Keys under a patronage shield → §3.3b Za-lapse pulls the shield → shielded Keys convert *en masse* to Duty-failure → Demotion | ~4/7 (the §5.5 template) | **Standing/rank** |
| **F — Clerk-Corruption loaded gun** | Retain Clerks → hidden counter starts, +1 AP → Treasury leaks, Intrigue rises, failed Investigates raise concealment (positive feedback, no cap) → entrenched clerk becomes a power center / −2 Demotion vector | ~6/7 | Treasury/Intrigue |
| **G — Absentee/Defy → Suspicion → Recall on an undefined threshold** | Repeated Defy/absence → Suspicion accrues (increment undefined) → Recall fires at a threshold nobody defined | ~3/7 (S2 ran the whole Recall on fiat) | **Standing/rank** |
| **H — Cross-scale Mandate drag REFUTED** | Peripheral collapse *should* pull Mandate down; actual `Mandate = clamp(round(7T/(T+6)))` is saturating + Seat-dominated, so a revolt→secession moved rounded Mandate **not at all**; §1.8 L-feedback even *inflated* the dying settlement's Legitimacy | S6 headline (degenerate S4,S5) | Cross-scale |

**The balance verdicts that make these terminal** (stress test §5): the demotion spiral is *near-deterministic given roll cadence* (3–4 major rolls/season, most ~40–60%; mid `dice_pool` rolls are ~55% not the agents' assumed ~48%, per §0.3 — a *marginal* softening, not a reversal); **Appeals succeed 0/6 across seeds** (~20–31% vs a Std-7 adjudicator); the R-4 cliff has **no relief valve**; §1.3a stale-high Assessment is a **deterministic strip**; Mandate saturation **masks the exact collapse it should surface.**

---

## 44.6 The Loop property as a recoverability classifier

The event catalogue writes a **Loop** clause for every card. Read across the whole catalogue, that clause is a **latent recoverability classifier** — its own vocabulary sorts cards into two disjoint classes:

**TERMINAL-loop vocabulary** (the card describes irreversibility, a one-way ratchet, a permanent cap, a self-reinforcing/inheritable spiral, or "the neglect that caused it makes it harder to fix"):

> "a one-way ratchet whose only exit grows more expensive" · "permanently caps the Develop ceiling" · "compounds irreversibly (wheat permanently lost)" · "a self-reinforcing spiral the Ledger makes explicit and inheritable across governor succession" · "converging on the Rand outcome rather than stability" · "a two-sided disinvestment spiral ending in implicit abandonment" · "the neglect that caused the collapse also makes it harder to fix" · "permanent Prosperity-floor drop" · "deterministically fires the Bank Run, which permanently burns the method" · "coordination failure inflates the price of its own fix" · "compounding rather than resolving the tax-base collapse."

**RECOVERABLE-dip vocabulary** (the card describes a shock that is *blunted, denied its escalation, or converted to survivable* — almost always by a pre-built institution or a banked investment):

> "blunting Order/PS loss and blocking the rebel-Ambition follow_on" · "denies the Friction its escalation" · "converts siege into a stalemate the besieger must formally lift" · "converting erasure to survivable-with-losses" · "keeps SalinityLevel below crop-loss thresholds" · "denies the rival its Opportunity gain" · "same roll, radically different consequence gated by a prior Sponsor choice" · "cutting the Crisis's odds independent of the Directive."

**The discriminating variable, in nearly every case, is a single bit: was a standing institution built (and funded/accumulated) before the trigger?** The *same underlying roll* (drought, storm, siege, flood) is a recoverable dip with the institution and a terminal loop without it. The catalogue states this in almost identical words at three different families:

- Drought: *"Sponsoring each good season raises StockLevel that a drought consumes automatically… skipping it leaves StockLevel zero so the identical roll escalates to famine → Order collapse → a rival's Standing gain — same roll, radically different consequence gated by a prior Sponsor choice."*
- Flood: *"a Water Board decouples flood funding from Directive competition so war-funding choices cannot starve flood defense — cutting the Crisis's odds independent of the Directive."*
- Siege/enclave: *"survival is set entirely by a Fortify investment made years earlier; the Crisis is a retroactive audit."*

So recoverability is not an intrinsic property of a crisis card. **It is a property of the world-state the card lands in — specifically, of which standing institutions exist.** This is the hinge the two dockets share.

---

## 44.7 Classification — RECOVERABLE dips vs TERMINAL doom-loops

Applying §44.6's classifier across the catalogue's families. "Recoverable-*if*" means the dip is recoverable **only** when its named institution was pre-built; absent it, the same card is terminal.

### 44.7.1 RECOVERABLE dips (institution-gated)

| Crisis | Recoverable because… | Institution that makes it so |
|---|---|---|
| Drought / famine | StockLevel auto-consumed; rebel-Ambition follow_on blocked | **Ever-Normal Granary / Civic Granary / Standing Reserve / Territory Reserve Pool** |
| River flood | Flood funding ring-fenced from war Directive | **Water Board** |
| Province siltation | Develop checked against shared SiltLevel before approval | **Water Magistracy** |
| Low-flood tax shock | Levy auto-scales off `FloodIndex`; Friction never escalates | **Gauge-Indexed Levy (Nilometer)** |
| Earthquake / fire | Trigger weight + casualty multiplier lowered in advance | **Rebuild-to-Code / Housing Code / Water Infrastructure** |
| Coastal storm / fleet loss | Storm roll lowered; timing exposure avoided | **Sea Wall / Sheltered Dockyard / Storm-Season Withdrawal / Flota Scheduling** |
| Existential siege | Pre-pooled Fortify decides the win/loss table; survival compounds | **Coalition Fortify Pool** (+ Inundation, Alternate Corridor) |
| Enclave blockade | Corridor bled Π down into a stalemate | **Alternate Corridor** (pre-built airbase tier) |
| Garrison mutiny / sack | Unpaid-troops severity modifier removed | **Contribution System / Settle Arrears** |
| Trade-vector plague | Plague draw-weight reduced along trade predicate | **Sanità Lazzaretto** (+ Diversify Corridor, Staged Demobilization) |
| Mining boom-bust | Rate stays credible; departing-miner seed denied | **Regalian Mining Charter w/ Tribunal** |
| Salinization | `SalinityLevel` held below crop-loss threshold | **Corvée Desilting Levy** |
| Harbor decline | SiltLevel reset before the rival's Opportunity fires | **Dredge Harbor** |
| Correlated Cooling shock | Aggregate Extract-vs-Remit choice keeps shocks isolated | **Remit Directive + relief-configured Ministry** |

### 44.7.2 TERMINAL doom-loops (structurally self-reinforcing)

| Doom-loop | Terminal because… | Circuit-breaker (if any exists) |
|---|---|---|
| **Debasement ratchet** (Roman 3rd-c., Great Debasement/Gresham, akçe) | `Capital-Posture:Debased` one-way; exit grows more expensive the longer deferred; price-cap Comply manages symptom, never clears the tag | **Recoinage** (steep, PA-approval) — the *only* clearing action |
| **Charter-Fiat → Bank Run** (Mississippi Bubble) | Crossing the backing ratio **deterministically** fires the Bank Run and **permanently burns the method** | None short of not issuing; province-wide punitive cleanup |
| **Assignat / land-backed fiat** (1790s) | Overprinting deepens the dispossessed faction's Grudge *and* removes the Treat/Sponsor tools that could soften the Reset — "fiscal and political failure tracks coupled by design"; "cannot reset as cleanly" | **Currency Reset** (writes permanent "Precedent: Monetary Failure") — a *degraded* reset, not a clean one |
| **Stale-Assessment / fixed-quota-through-famine strip** (Bengal 1770, Cocoliztli, Zimbabwe Redistribute) | Extract reads a stale-high base off a shrinking economy; refusing relief compounds Grudge that raises the Ob on the *next* Survey — "the neglect that caused the collapse also makes it harder to fix" | **Emergency Resurvey / Renegotiate Compact / Remission / a subsistence-floor clamp** — **the stress test's Pattern C, see §44.8** |
| **Free-Trade doctrine famine** (Irish Famine) | A standing ideological Precedent *locks in* the bad Comply/Bargain menu | **Relief Obligation** (partly decouples relief from export doctrine, at Reputation cost) |
| **Downstream RisingWaterLevel fuse** (Yellow River Scour) | A Fortify choice at one node writes a slow tag on a *different* node "that nothing there can see or defuse" — a multi-decade fuse | **River Conservancy Directorship** (governs the fork; does not make Scour safe) |
| **Salinization past final threshold** (Mesopotamia) | Compounds irreversibly; wheat permanently lost; Crop Substitution becomes *forced* not chosen | Corvée Desilting **only if run every season before threshold** — terminal once crossed |
| **Permanent Develop-ceiling cap** (Mongol Baghdad) | Destroyed irrigation caps the ceiling for multiple generations | **Rebuild Infrastructure** (high-cost multi-season) — recovery, not prevention |
| **Outlawed / Settle-&-Confiscate spiral** (Drogheda) | Each execution writes a new Outlawed tag raising future Grudge/Intrigue — "self-reinforcing… inheritable across governor succession" | None material; only *not* invoking the punitive branch |
| **Segregation-Camps → assassination** (Third Plague) | The action that ends the Crisis *is* the trigger for the next; sanitation underinvestment untouched → "converging on the Rand outcome rather than stability" | Sanitation investment upstream; the reactive Force branch cannot break it |
| **Norse Greenland disinvestment** | Two-sided: settlement bleeds Prosperity (can't afford the pivot); metropole loses willingness to resupply → "implicit abandonment rather than one dramatic Crisis" | **Adopt Local Practice** (early) — a pivot, at a metropole-Disposition cost |
| **General/17th-c. Crisis Cooling cascade** | Uniform Π-raise everywhere → simultaneous **Demotion Magnitude events stripping the governors needed to manage recovery** → deepening Π spike | **Remit + relief Ministry** — **the stress test's Pattern B at world scale** |
| **The Anarchy nineteen-winter loop** | The Split erodes the Mandate needed to ever extract a credible Oath afterward | **Extract Succession Oath** *early* — brakes the mandatory-contest row; useless once the Split has eroded Mandate |
| **Partible/Panaca succession** (Inca) | Set-once, irreversible; the independent Military that made each heir strong is what makes them fight | Structural — avoidable only by never adopting it |

---

## 44.8 The bridge — which standing institution breaks which stress-test doom-loop

This is the synthesis proper: map the stress test's **emergent** patterns (A–H) onto the catalogue's institution class. The result splits cleanly along an axis the stress test named but did not generalize.

| Stress-test pattern | Axis | Is it an institution-breakable doom-loop? | Circuit-breaker |
|---|---|---|---|
| **C — Compact/Assessment deterministic strip** | Prosperity/extraction | **YES — a material crisis with a known institution** | **Emergency Resurvey / Renegotiate Compact / Remission / a subsistence-floor clamp**; upstream, **Ever-Normal Granary / Standing Reserve**. This is exactly the catalogue's stale-Assessment terminal loop (Bengal/Cocoliztli/Zimbabwe). The stress test's HIGH-priority "add a subsistence-floor clamp to §1.3a" **is** the catalogue's missing anti-strip clamp — same fix, two dockets |
| **B — Π runaway / R-4 cliff, no valve** | World-state Π | **YES — the catalogue's Cooling-cascade loop** | A **Π relief valve** (the KEPT VEN-SE-5 Scuole Grandi ceilinged valve, per stress test §5) + **Remit Directive / relief Ministry** + a Grudge half-life. The catalogue's General-Crisis entry independently prescribes "flexible institutions weather the shock" |
| **F — Clerk-Corruption loaded gun** | Treasury/Intrigue | **YES — the org-scale Audit institution exists** | **Fugger Audit-Branch (O5)** — "converts a hidden, silently-compounding risk into a visible, scheduled one." The circuit-breaker is *already designed*; it sits on the (unbuilt) Organization menu, not yet wired to the settlement Clerk-Capacity loop |
| **D — Collective-Liability cell-revolt stacking** | Order | **PARTIAL — a mechanic-reconciliation, not a facility** | The §1.3b-vs-§4.5 actor-cap collision (NERS MERGE, confirmed hard). The "institution" here is *fixing the collision* + a stack-decay/relief on Collective Liability, not a build |
| **A — Demotion spiral (universal)** | **Standing/rank** | **NO — no institution in the catalogue breaks it** | **Substrate tuning only:** a survivable Appeal Ob (Appeals are 0/6), successes that actively *retire* prior failure Keys, lower roll cadence, a higher failure count before §1.0a fires |
| **E — Patron-lapse un-shielding** | **Standing/rank** | **NO** | Substrate: a symmetric non-revocable footing for a patron-dependent actor (stress test §3.3b×§3.3c asymmetry); no facility defuses it |
| **G — Suspicion → Recall on an undefined threshold** | **Standing/rank** | **NO** | Author the missing constant (Suspicion→Recall threshold + per-Defy increment). VEN-SE-7 *Sindici Inquisitori*' roving audit floor is the closest institutional analogue, but the core fix is a defined number |
| **H — Mandate saturation hides collapse** | Cross-scale | **NO — a formula fix** | Re-designate Standing/tag Keys (not Mandate) as the cross-scale collapse carrier; add a below-subsistence Mandate term; fix the §1.8 L-feedback inversion |

### 44.8.1 The load-bearing result: the institution library covers the *world*, not the *self*

Read the table's **Axis** column. The pattern is stark and, as far as the corpus shows, **unstated before now:**

- **Every material-axis doom-loop (Prosperity, Order, Treasury, Defense, Π) has a standing-institution circuit-breaker in the catalogue.** The institution class of §44.2–§44.3 is a **near-complete circuit-breaker set for the world-state axes.** Flood, famine, fire, storm, plague, siege, siltation, extraction, fiscal ratchet, correlated cooling — each terminal loop names, *in its own Action field*, the build-once institution that pre-empts it.
- **No standing institution in the catalogue breaks the Standing/rank doom-loops (A, E, G) — the stress test's #1 and most universal finding.** The demotion spiral is not a world-state crisis you can build a granary against. It is a property of the **resolution substrate** (§5 resolution_quality → Standing bridge, §1.0a magnitude, no Grudge decay, Appeals 0/6). Its circuit-breaker is not a *facility* but a *rule change*.

**Stated as a single sentence — the bridge:** *the event research produced a library of institutions that defuse the world, but the balance stress test's dominant doom-loop lives in the self (the rank ladder), where no institution reaches — so the proactive-institution program and the resolution-substrate tuning program are complementary, not substitutes, and shipping only the first would leave the game's most universal tragic spiral fully intact.*

### 44.8.2 Two corollaries the bridge forces

1. **Build-before-crisis is not a play-style, it is the architecture.** The terminal loops are terminal *because the reactive verb menu cannot break them mid-crisis* — Alternate Corridor "cannot be reacted into existence," the granary must have accumulated, the Sea Wall must predate the storm. The stress test saw doom everywhere partly *because it was a depth-3 failure sweep with no institutions pre-built.* This vindicates the stress test's structural verdict ("no circuit-breaker past the cliff") and simultaneously locates the fix: **circuit-breakers are architecturally pre-emptive, and nothing in the current loop forces or rewards building them against a threat that "most seasons doesn't land."** The Vesuvius **Evacuate** loop names this exactly — "warning-fatigue made mechanical" — and it is the reason a rational myopic governor *under*-builds institutions, manufacturing the doom the stress test measured.
2. **The institution's job is decoupling; the doom-loop's cause is coupling.** Every terminal loop in §44.7.2 is a coupling failure — flood funding coupled to the war Directive, relief coupled to export doctrine, Levy coupled to a stale Assessment, fiscal collapse coupled to political dispossession. Every institution in §44.2 is a de-coupler — the ring-fenced levy, the self-replenishing reserve external to the Treasury cycle, the alarm-timing network decoupled from event magnitude. **A crisis family is terminal exactly to the degree that its defensive function is coupled to a pressure that can starve it; the institution is defined by which coupling it severs.** This gives a design test for whether a *proposed* institution is real: name the coupling it breaks. If it breaks none, it is a stat bump, not a defuser.

---

## 44.9 Caveats, corrections, and open questions (all PROPOSED)

Carried faithfully from the three sources; do not let this Part read as more settled than they are.

- **The two loudest "author-everything" alarms were phantom (stress test §0).** (a) "The Crisis family has ZERO resolvable cards" was a **compressed-kernel digest artifact** — Crisis cards *do* carry branch structure and **route to the `d_sigma` resolver**; they are resolvable. The real (much smaller) residual is uneven per-branch stat-delta tables — a completeness-audit polish item, not a content hole. (b) "§2.5a defines no Gu-Std2→3 rung" **collapses** — the Guild ladder is authored through Gu-Std 6. This matters *for this Part* because the recoverability classification of §44.7 is **not** "Crisis = unresolvable"; it is the finer "resolvable-and-recoverable vs resolvable-but-terminal-loop."
- **Legible-vs-engine odds divergence (stress test §0.4) — a live reconciliation item.** The deck promises a **legible** `d_sigma` model (base 50% + flat +10%/pt, FLOOR .05 / CAP .90), but the `[CANONICAL]` engine (`sim/autoload/sigma_leverage.p_success()`) is a **continuous normal-CDF** that diverges materially at the tails (e.g. base_Ob 3, pool 7, +major: engine 78% vs a linear read ~90%). **Consequence for §44.7:** the recoverability a *player* perceives (from legible odds) may not match the recoverability the *engine* rolls. A crisis a player reads as a recoverable ~90% may be a 78% coin-shave in the engine. Decide which model is the odds contract before the recoverability classification is player-facing.
- **Beacon Network / Relay Tier are contingent on a temporal model that isn't authored.** They presume Valoria has *inter-settlement latency* to gate. If turns resolve simultaneously/abstractly, these two levers — the strongest "new state" cases on paper — have nothing to model. This needs confirmation against `engine_clock` (CLAUDE.md §6 flags it `doc: null` — unwritten).
- **Tag-family proliferation.** The corpus now proposes Compact, Concession, Outlawed, Capital-Posture *and* a new Muster family atop Precedent/Grudge/Debt/Reputation. A consolidation pass on the tag taxonomy is warranted before all five ship (Muster/Compact may be collapsible; Concession/Capital-Posture overlap in the frontier entries).
- **The Organization economy is unspecified.** "Org AP" / "Org Treasury" / dues / responsions / assay fees are an *entity + verbs* without a resource loop — the single biggest authoring gap behind the org-scale defusers (incl. the Fugger Audit-Branch that breaks Pattern F).
- **No numbers, by design (CLAUDE.md §5).** The one place a *number* is genuinely required is the Territory **Reach-cap** trigger (X9); it is deliberately left unspecified here. Nothing on this page crosses into Godot until authored as prose params with a `PP-NNN`/`ED-<LANE>-NNNN` citation.
- **The structural caution the research itself raised (proactive §6, X4/X5).** Several of these levers are historically *load-bearing for collapse* — intendants fed the Fronde, reneged compensation detonated Satsuma. The proactive-institution menu and the reactive Crisis-card system **must ship as one loop**: if stacked Grudges do *not* auto-seed Crisis-family cards, the game gets the centralizing/defusing upside with none of the historical downside — an inaccurate and undramatic model. This is the same "ship as one loop" logic that §44.8.1 states from the balance side.

**One-line handoff for the authoring pass.** Ratify the world-axis institution class (§44.2–§44.3) and the resolution-substrate tuning (Pattern A/E/G fixes) **together** — they are the two halves of one anti-doom-spiral program, and the bridge (§44.8) is the argument that neither half is sufficient alone.
