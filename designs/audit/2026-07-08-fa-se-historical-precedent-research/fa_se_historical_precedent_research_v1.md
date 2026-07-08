# FA/SE Historical-Precedent Research — Faction Actions & Settlement Management

## Status: FILED — 2026-07-08 · Lanes: FA, SE. Step-3 proposals docketed as ED-FA-0008..NNNN /
## ED-SE-0007..NNNN (see `handoffs/HANDOFF_FA.md` / `HANDOFF_SE.md` and `canon/editorial_ledger.jsonl`
## for the per-item filing + which have been executed vs left `needs_jordan`). Not itself canon —
## a research/synthesis artifact the docket items cite as provenance.

**Session:** 2026-07-08 · READ-ONLY research pass (no repo edits)
**Scope:** `sim/provincial/faction_action.py`, `sim/territory/registry.py`, the FA design quartet (`faction_canon_v30`, `faction_layer_v30`, `faction_behavior_v30`, `faction_state_authoring_v30`, overview `faction_systems_overview_v30`), the SE set (`settlement_layer_v30`, `settlement_adjacency_v30`, `territory_temperaments_v30`, `governance_play_redesign_v1` [PROPOSAL], `geography_v30`), plus the personal-scale faction adapters (`sim/personal/contest/faction.py`, `sim/personal/parliamentary_vote.py`, `sim/personal/parliamentary_stay.py`, `sim/provincial/parliamentary_transfer.py`).
**Method:** Step 1 = repo audit of what is grounded vs fiat; Step 2 = new historical/political-science research covering territory the existing corpora have NOT mined (duplication-checked against fresh inventories of both prior research corpora); Step 3 = concrete mechanical distillations, each tagged target + citation + promote-ready vs needs_jordan.

---

## STEP 1 — What is already there

### 1.1 Code-level audit: `sim/provincial/faction_action.py`

| Mechanic | Value | Grounding status |
|---|---|---|
| Action mix | 30% unique / 35% Conquest / 20% Muster / 15% Govern | **`M7_ASSUMPTION_SIX`** — explicitly an assumption carried from v17; no historical or behavioral rationale anywhere in the corpus |
| Strategic roll | d6 ≥ 4 per die | v17 convention (engine-level, fine) |
| Conquest gate | `faction.Mil < 3.0` → invalid | Fiat threshold, uncited |
| Conquest consequences | loser `L −10`; `t.adjust_accord(−25)`; `garrison = True` | Fiat magnitudes; no storm-vs-surrender distinction (all conquests treated as maximally alienating) |
| Muster | pool=Mil, Ob 1; +5/+3 Mil; Failure → `W −3` | All fiat. No Wealth *cost* to muster (only a failure penalty), inverted relative to the fiscal-military logic the corpus itself invokes elsewhere (faction_layer §5.7 FSS-LOOP-2 cites Habsburg re-muster) |
| Govern | pool=I, Ob 2; Accord +15/+10; Failure → `Sta −5` | All fiat. Govern is scalar Accord-pumping; it does not touch the (inert) per-settlement L/PS even though LPS-2e says that is where political acceptance lives |
| Church priority | Excomm > Council > Absolution, L-gated | Heuristic ordering, uncited |
| Terrain | `terrain=None` | `[GAP]` — deferred |
| Whole module | | **[PRE-LPS-1 / PORT-BLOCKING — ED-FA-0004]**: scalar-L reads; no per-settlement L/PS; no `da.*` Keys |

### 1.2 Code-level audit: `sim/territory/registry.py`

| Field / rule | Status |
|---|---|
| `legitimacy`, `popular_support` (0–7, §1.8) | **Declared but NEVER read or written anywhere in `sim/`** (inline ED-FA-0004 banner; "an INERT LPS-1 schema stub"). Wiring them into Mandate is ED-FA-0004 Stratum-B work. **This is the single largest grounding vacuum in the SE lane: the settlement-political-acceptance pipeline exists as schema only, with no derivation events.** |
| `order`, `prosperity`, `defense` (0–5) | Read by `province_accord` (floor-mean of Order) and `province_effective_prosperity` (sum); starting values PROVISIONAL (ED-SETT-01 deferred) |
| `ap = 2 + FacilityTier (+1 Seat/Cathedral)` | From governance_play_redesign §1.1 — a PROPOSAL, not ratified canon |
| `pressure: float = 4.0` | Default from the proposal's Π homeostat; uncalibrated |
| `suspicion`, `church_attention`, `governor_emergence`, `active_directive`, `open_needs`, `deck_state` | Proposal-referenced state with no resolution rules in canon yet |
| `succeed_governor` | Durable-ledger persistence; fine |

### 1.3 Design-doc audit: which sections are under-grounded

**FA lane:**
- `faction_layer_v30 §5.4` Parliamentary action table (proposer minima, Majority/Supermajority, costs/durations) — thresholds asserted without rationale; the 50%/60% pair is the only part with (Venetian/conciliar) lineage via the SC-lane research.
- `faction_layer_v30 §3` treaty tables (cession → Stability deltas; Tributary −1/yr; treaty-type → hegemony list) — asserted; only FSS-LOOP-1/2 carry explicit historical anchors (Byzantine 1204 / Habsburg bankruptcies — both added 2026-05-30 by the resolution diagnostic, notably the only two mechanics in the whole file with named precedent).
- `faction_layer_v30 §3.5 / parliamentary_transfer §3` Casus Belli: 8 sources, mode mapping `[FLAG]`ged PROVISIONAL (PARL-VOTE-MODIFIER-001, PARL-MODE-DRIFT-001); no grounding in the historical law-of-war / just-cause tradition.
- `faction_canon §9` unique-action table: Royal Decree fatigue (+1 Ob/season), Excommunication degree table, CI-60 seizure Ob = 7 − PT — magnitudes fiat; the *actions themselves* (Royal Progress, Great Work, Coronation Renewal, Excommunication, Council) are historically shaped but nowhere cited.
- `faction_behavior §3.4–3.6` λ/α/β/strictness coefficients — declared "starting values; calibrate at Stage 10"; the temperament table's only anchors are one-phrase period examples ("Florentine merchant class").
- `faction_action.py` 30/35/20/15 mix (above).
- No taxation/fiscal mechanic at all between settlement Prosperity and faction Wealth/Treasury beyond a flat `Prosperity × 50` (derived_stats, settlement_layer §1.3) / `× 10` (§1.8 note) rollup and the proposal's `Levy` verb. No tax-rate choice, no collection mode, no fiscal-legitimacy coupling — despite Wealth-zero and Muster both being fiscal-military mechanics.
- Succession: `succession()` split ratios 0.60/0.55/0.50 (contest/faction.py §7.2.1) uncited; no regency mechanic despite the Generational Shift clock (settlement_layer §7.1) explicitly aging leaders toward death.

**SE lane:**
- `settlement_layer §1.8` (LPS-2e): the Mandate aggregation is calibrated (K=6, Stage-4 sim) and cites *game* precedents (CK3/EU4/Victoria/ROTK) — but the **per-settlement L/PS derivation events themselves** (what raises/lowers L and PS *in a settlement*) inherit only the faction-level PP-686 λ-lists, uniformly applied. Nothing distinguishes how a *settlement* grants or withdraws acceptance (entry oaths, privileges, dearth, billeting, courts).
- `settlement_layer §4.3` events table: "Prosperity 0 → Famine... Order −1 automatic" is the entire subsistence-politics model. Meanwhile `geography_v30` carries **ED-054 / BALANCE-005: "Hafenmark food dependency has no mechanical teeth — Feldmark unreachable by Hafenmark"** — an open item that is precisely a grain-politics gap.
- `settlement_layer §3.3` subnational management grant (Ob 1) / revocation (Ob = Influence÷2; Order −1, Disposition −2) — asserted; the charter/privilege tradition it is unknowingly modeling is uncited.
- `settlement_layer §5.1` siege ("defender Order −1/season → surrender at 0") and Assault — no storm/surrender distinction, no terms-of-capitulation surface, despite §2.3 Accord-on-transfer tables elsewhere caring about *how* control transferred.
- `governance_play_redesign_v1` (PROPOSAL, ED-SE-0001 tracking): Directive/Petition/suspicion/recall, Levy, method-choices — the strongest FA/SE-facing design surface, and almost entirely un-grounded in named precedent (its own text cites EU4 estates and the "Geneva trap" only).
- `territory_temperaments_v30` — per-territory α/β assignments have one-line rationales; fine as authored color, but the typology's period examples are the only grounding.

### 1.4 What is ALREADY cited (do not duplicate)

**In the FA/SE docs themselves:**
- Renaissance stat analogues (papal bulls, Medici banking diplomacy, Venice's Council of Ten, Pazzi conspiracy, Visconti-Sforza succession) — faction_canon §5.1.
- Crown sheet: Wars of the Roses deed-claim, Avignon papacy, Investiture Contest. Church sheet: Avignon + medieval Inquisition + Counter-Reformation, Spanish Inquisition proceduralism.
- Varfell doctrine: Hannibal at Trasimene, Belisarius, Mongol envelopment, oblique order; Talleyrand-style diplomatic intelligence (faction_layer §1.5).
- FSS-LOOP-1: Byzantine 1204, Habsburg bankruptcies; FSS-LOOP-2: Spanish Habsburg re-muster; treaty resolver note: early-modern treaty-making as power-structure-decisive (faction_layer §1.4/§3.3/§5.7).
- Church settlement infrastructure: Papal States, Calvin's Geneva ("Geneva trap", Parish Social Services §1.6), 1979 Iran, post-collapse parish priest (Pastoral Assumption §1.7) — from a prior `historical_precedents_analysis` doc (no longer present in the tree; its distillates ARE in canon via ED-682/683).
- RM cell resilience: Solidarity, Bolshevik cells, ANC underground (settlement_layer §3.3). Intelligence brokers: Ems Dispatch pattern (§4.8).
- Temperament typology period examples (Florentine merchant class, etc.).
- Game-design precedents: KOEI ROTK, CK3, EU4, Victoria (settlement_layer header + §1.8).

**In the prior research corpora (verified by fresh inventory passes this session):**

*2026-06-28 social-contest source-research* (five files + critique): the dialogue-game apparatus (Suits, Rawls 1955, Searle, Huizinga, Caillois, Wittgenstein, Goffman, Hamblin's commitment store, Lorenzen/Lorenz, Hintikka, Walton & Krabbe, pragma-dialectics, Pound's "sporting theory," Hart, Priest–Klein/Schelling/Raiffa/Putnam two-level games); a 13-family catalog of pre-1600 decision procedures (Athenian kleroterion & ostracism, Florentine *imborsazione*/*squittinio*/Tratte, Venetian doge lot-ballot hybrid & *broglio*, Roman auspices/*obnuntiatio*, Byzantine acclamation, papal conclave & *sanior et maior pars*, Haudenosaunee Great Law, liberum veto, Cortes of León 1188 supply-for-redress, Golden Bull electors, tanistry, kurultai, *keju*, *shūrā*/*bayʿah*, Gadaa); Renaissance civic humanism (Bruni, Baron, Contarini, Machiavelli's *Discorsi*, Guicciardini, conciliarism/Marsilius/Cusa, Bartolus *civitas sibi princeps*, Justinianic *universitas* / *quod omnes tangit*); machination theory (Padgett & Ansell "Robust Action," Greif, Tsebelis nested games, Botero/Lipsius reason-of-state, Dowlen & Buchstein on sortition, Finlay, Rubinstein). **The inventory's bottom line: every distillation in that corpus targets the personal-scale social-contest module; FA/SE docs appear only as borrow-sources ("DO NOT re-author Varfell — it is done"), and nothing in it flags FA/SE grounding as an open gap — the gap this report now fills.**

*2026-04-28 political-dynamics session:* per its own framing and this session's earlier review, the same conciliar/republican research tradition (Venice, Florence's *consulte e pratiche*, Polybius, conciliar movement, canon-law corporation theory, liberum veto, Putnam, sortition scholarship) was brought in for institutional/faction-scale politics but its mechanical landing zone became the opinion-architecture / social-contest / NERS stress-test line (personal scale), with settlement-layer contact limited to signal-integration files (SIM_C, file 27). **Disjointness verified by direct keyword sweep of the full directory:** none of this report's Step-2 anchors (Weber, Tilly, Levi, Olson, Hirschman, Thompson, Scott, Sen, Ibn Khaldun, Kantorowicz, Grotius, publicani/iltizam/Ferme Générale, residencia, advowson, interdict, Magdeburg law, Hansa, quo warranto, Joyeuse Entrée, granaries, Grenzer/coloniae, Danegeld/Ragusa, regency) appears anywhere in the 2026-04-28 corpus, with a single exception: one passing "Byzantine themata-civil rivalry" analogy inside a stress-test narration (file 10, not a mined precedent — acknowledged at SE-9).

### 1.5 The gap, stated precisely

The FA/SE systems are *institutionally shaped* (parliament, treaties, excommunication, governors, charters are all real-institution silhouettes) but their **quantities, triggers, and above all their missing subsystems** — fiscal extraction, subsistence politics, agent oversight, conquest-terms, local church-state jurisdiction, frontier colonization, succession interregna, corporate/charter politics — have no grounding tradition attached. The existing research trilogy grounds *how bodies deliberate*; nothing yet grounds *how rulers extract, feed, audit, colonize, and legitimate*.

---

## STEP 2 — New historical / political-science research, by theme

Ten themes, chosen to be disjoint from the deliberation-and-procedure tradition already mined, and each aimed at a *specific* FA/SE mechanical vacuum identified in Step 1. Each theme names institutions, periods, mechanisms, and scholars at the standard the existing trilogy holds itself to.

### T1. Fiscal sociology: the extraction–coercion loop (the missing spine between Prosperity, Wealth, and Military)

Charles Tilly's dictum — "war made the state, and the state made war" ("War Making and State Making as Organized Crime," 1985; *Coercion, Capital, and European States, AD 990–1992*, 1990) — describes a loop Valoria already half-implements and half-omits: war requires revenue; revenue requires extraction; extraction requires administrative apparatus; the apparatus outlives the war and *is* the state. The corpus has the downstream half (Wealth-zero demobilization, FSS-LOOP-2's Habsburg re-muster) but no upstream half: **there is no extraction decision anywhere** — Treasury is a flat `Σ Prosperity × k` rollup with no rate, no mode, no legitimacy coupling. Three refinements matter:

- **Margaret Levi, *Of Rule and Revenue* (1988):** rulers are revenue-maximizers constrained by bargaining power, transaction costs, and discount rates; her key construct is **quasi-voluntary compliance** — subjects pay at low enforcement cost when they believe the ruler's demands are fair and others are paying too. Compliance cost falls as legitimacy rises. This is a *formula shape*: effective yield = rate × base × f(L), with f increasing in settlement Legitimacy.
- **John Brewer, *The Sinews of Power* (1989):** Britain's 18th-century military dominance rode on an excise bureaucracy — trained gaugers, measured warehouses, standardized assessment — i.e., *administrative infrastructure raises extractable yield without raising resentment proportionally*. Valoria's `FacilityTier` is the natural carrier: institution-building should raise fiscal yield, not just Settlement Weight.
- **Tilly's typology:** capital-intensive polities (Venice, the Dutch Republic) rented coercion with borrowed money; coercion-intensive polities (Brandenburg-Prussia, Muscovy) squeezed manpower and kind directly from an agrarian base; capitalized-coercion hybrids (England, France) won. This maps startlingly well onto Hafenmark (capital-intensive: mercantile-procedural, equipment-quality doctrine) vs Varfell (coercion-intensive: "tribute and conscription" is literally in its Mission's aligned categories) and gives the two factions *differentiated muster economics* instead of a shared fiat table. Schumpeter's "The Crisis of the Tax State" (1918) supplies the legitimacy-side warning: the fiscal system is where the polity's real constitution shows.

Also directly relevant: **Gabriel Ardant & Richard Bonney (*The Rise of the Fiscal State in Europe, c. 1200–1815*, 1999)** on the tribute→domain→tax-state sequence, and **Thomas Ertman, *Birth of the Leviathan* (1997)** on why early parliamentary bargaining produced either bureaucratic or patrimonial infrastructures — the latter being exactly the venality/tax-farming complex of theme T2.

### T2. Tax farming and the sale of extraction rights

Where administrative capacity is thin, pre-modern states sold the right to collect: the Roman **publicani** (whose provincial abuses were notorious enough to make "publican" a term of contempt); the Ottoman **iltizam** (short-term revenue farms auctioned to the highest bidder) and its 1695 mutation into **malikâne** (life-term farms — trading yield for the farmer's longer time horizon, an explicit discount-rate fix Levi analyzes); the French **Ferme Générale**, whose forty farmers-general financed the crown, ran a private customs army, built the Wall of the Farmers-General around Paris — and 28 of whom were guillotined in 1794, the legitimacy bill arriving all at once. The structural trade is constant across all three: **cash now + collection outsourced = over-extraction by the farmer + odium accruing partly to the state + the farmer becoming a political actor in his own right.** The mirror institution is the **venality of office** — the French *paulette* (1604) made offices hereditary property for an annual fee: revenue and elite buy-in now, permanent loss of administrative control later (Ertman's patrimonial trap).

Valoria hooks: the `governance_play_redesign` Levy verb and Guild-charter Develop funding are one-off versions of this; the settlement registry's `suspicion`/broker apparatus is the natural home for the farmer-as-political-actor consequence.

### T3. The moral economy of subsistence (dearth is politics, not weather)

- **E. P. Thompson, "The Moral Economy of the English Crowd in the Eighteenth Century" (*Past & Present*, 1971):** grain "riots" were disciplined popular enforcement of customary price norms — crowds seized grain, sold it at the "just price," and returned the money to the merchants (*taxation populaire*). The riot targets millers, forestallers, and exporters before it targets the state; the state loses legitimacy when it visibly sides with the market against the norm.
- **James C. Scott, *The Moral Economy of the Peasant* (1976):** the subsistence ethic — peasants judge extraction not by the average take but by whether it ever pushes them below subsistence in a bad year; a ruler who takes 40% in good years and *remits in bad years* is legitimate, one who takes 25% invariantly is not. **Extraction invariance under dearth, not extraction level, is what detonates revolt.**
- **Amartya Sen, *Poverty and Famines* (1981):** famines are entitlement failures, not food-availability failures — Bengal 1943 starved amid adequate aggregate supply because purchasing power and distribution collapsed. Mechanically: dearth should key off *access* (routes, prices, levies), not just local Prosperity 0.
- **The state's answer, historically:** Rome's **cura annonae** (a permanent prefecture guaranteeing the capital's grain, subsidized then free — emperors fell when it faltered); the Ming–Qing **ever-normal granaries** (*changpingcang*) buying high-harvest and selling dear-season, the largest civilian food-security apparatus of the early-modern world (Pierre-Étienne Will & R. Bin Wong, *Nourish the People*, 1991); the Tudor **Book of Orders** (1587) obliging JPs to survey stocks and force sales in dearth. Athens' dependence on Black Sea grain (protected by law: no Athenian could ship grain elsewhere) and the Hanseatic Baltic grain trade through Danzig show the *strategic* face: grain routes are war objectives.

Valoria hooks: settlement_layer §4.3's one-line famine row; geography's open **ED-054/BALANCE-005** ("Hafenmark food dependency has no mechanical teeth"); the Feldmark "Breadbasket" / Feldmark Storehouse sub-feature ("controls food supply to northern provinces") which is currently pure flavor.

### T4. Urban charters, corporate liberties, and collective economic coercion

The medieval commune bought, fought, or bluffed its way to chartered self-rule: **Magdeburg law** propagated as a template to hundreds of central/east-European towns; **"Stadtluft macht frei nach Jahr und Tag"** (serfs became free after a year and a day of town residence — settlements as Exit destinations); Iberian **fueros**; English borough charters *confirmed — for a fee — at each accession*. Two mechanisms matter beyond the charter grant itself:

- **Quo warranto:** Edward I's 1278–94 campaign demanded every franchise-holder show "by what warrant" they held their liberties; Charles II's 1683 quo warranto against the City of London *revoked* its charter — legally effective, politically explosive (reversed 1690). Revoking a hardened privilege is never an administrative act; it is a regime-legitimacy event. Age hardens privilege into right (prescription).
- **The Hansa's collective embargo (Verhansung):** the Hanseatic League's kontors (Bruges, Bergen, Novgorod, London Steelyard) enforced privileges by *collective withdrawal of trade* — the blockades of Bruges (1358, 1451–57) starved the city's commerce until privileges were restored. A merchant corporation with no army coerced territorial princes routinely. (The Florentine **Arti** and the **Ciompi revolt** of 1378 give the intra-city version: guild membership as the franchise, and the excluded wool-workers' brief revolutionary guild.)

Valoria hooks: settlement_layer §3.3's grant (Ob 1)/revoke (flat Ob) pair; Hafenmark's existing `charter_of_liberties` action; the Guilds NPC faction, which currently has a vote rule and an "Economic Leverage" one-liner but no grounded coercion mechanic. Note the *conceptual* substrate (canon-law *universitas*) is already mined by the 06-28 corpus — what is new here is the **operational** politics: confirmation-for-fee, quo warranto, prescription, collective embargo.

### T5. Principal–agent control of provincial governors (audit, rotation, venality)

The governor problem — your agent is far away, better informed than you, and accumulating local ties — produced a convergent toolkit:

- **Castile and the Indies:** the **residencia** (a standing judicial audit at end of tenure: the outgoing official stayed put while a judge collected sworn complaints from the governed) and the **visita** (an unannounced inspection mid-tenure). Every viceroy of New Spain knew the residencia was coming; it disciplined *ex ante*.
- **Ming–Qing China:** the **rule of avoidance** (officials barred from serving in their home province; ~3-year rotations) traded local knowledge for capture-resistance, and the **Censorate** (*duchayuan*) ran a parallel surveillance hierarchy whose only job was impeaching field officials.
- **Ottoman timar rotation** kept cavalry-fief holders moving so revenue rights never congealed into heritable local lordship — exactly the congealment that *did* happen when the system decayed into malikâne.
- The failure mode is **venality** (T2): the *paulette* made French offices property; the crown could no longer rotate, audit, or dismiss what it had sold.

Valoria hooks: `governance_play_redesign` §1.4 already invents the suspicion track and the Recall scene *ex nihilo* — the residencia/visita pair is its exact historical template and supplies the missing design distinctions (scheduled end-of-tenure audit vs surprise inspection vs rotation). The registry's `suspicion` field and the unread `governor_emergence` field are the state carriers.

### T6. Conquest terms: siege law, sack, and the entry ceremony

Early-modern siege warfare ran on a shared convention (Grotius, *De iure belli ac pacis* III; Geoffrey Parker, "Early Modern Europe," in *The Laws of War*, 1994): a garrison that surrendered on terms after a "practicable breach" received the **honors of war** — march out with flags, keep private property, town spared; a garrison that forced a **storm** forfeited protection — the town was liable to sack. The convention was brutally incentive-compatible (it economized on the attacker's costliest phase) and everyone priced it. Its catastrophic breach cases — the **Sack of Magdeburg, 1631** (20,000+ dead; "Magdeburgization" became a verb, and the atrocity's propaganda cost haunted the Imperial cause for the rest of the Thirty Years' War) and the Sack of Rome 1527 — show that sack was *cheap tactically and ruinous reputationally, peninsula-wide*.

The other half of conquest is the **entry**: the **Joyeuse Entrée of Brabant (1356)** conditioned the duke's recognition on his sworn confirmation of the province's privileges — obedience was explicitly contractual, and Brabanters claimed the right to refuse service if the charter was violated; English kings issued **coronation charters** (Henry I, 1100 — the model for Magna Carta) confirming "the laws of Edward the Confessor"; virtually every European town expected its privileges confirmed at a new lord's accession, and the new lord expected to be *paid* for confirming. A conqueror or heir who confirmed bought cheap legitimacy at the price of constrained extraction; one who imposed new law bought full extraction at the price of a resentful base.

Valoria hooks: `_try_conquest`'s undifferentiated `adjust_accord(−25)`; settlement_layer §5.1 siege (Order→0→surrender with no terms surface); faction_layer §2.3's Accord-on-transfer tables, which already vary by *treaty* mode but not by *military* mode.

### T7. Church vs. secular jurisdiction at the parish level

The conclave/conciliar material already mined is *summit* politics. The settlement-scale church-state interface was a different, denser fight:

- **Advowson** — the property right to *nominate the parish priest* — was among the most litigated rights in medieval English common law (the assize of *darrein presentment* existed just for it, and the **Constitutions of Clarendon (1164)** claimed advowson disputes for the king's court). Whoever named the priest shaped the pulpit — the settlement's one mass medium.
- **Clarendon/Becket** more broadly: jurisdiction over "criminous clerks," appeals to Rome, and **benefit of clergy** (clerics tried in church courts, which did not hang) — a running dual-sovereignty seam inside every settlement, alongside church-court monopoly over marriage, wills, and tithes, plus the right of **sanctuary**.
- **The local interdict:** Innocent III's interdict on England (1208–14) suspended sacraments — no masses, no church burials — across the realm to coerce John; interdicts were also laid on single cities (Venice repeatedly, most famously 1606). The weapon works by making the *populace* miserable so that it pressures the *ruler*; but prolonged use bred resentment against the clergy itself and confiscations flowed the other way — a genuinely two-edged instrument.

Valoria hooks: the Church currently jumps from settlement infrastructure passives (§1.5–1.7) straight to faction-scale Excommunication/Seizure; the registry's `religious_building` and `church_attention` fields are semantically thin; there is no contested *appointment* right and no settlement-targeted coercion tool.

### T8. Frontier colonization and garrison settlement

- **Byzantine themata (7th–11th c.):** soldiers settled on hereditary military lands (*stratiotika ktemata*), owing service tied to the land — defense capacity without treasury pay, at the price of eventually powerful provincial magnates.
- **Habsburg Militärgrenze (1522–1881):** the Military Frontier against the Ottomans — **Grenzer** free-peasant soldiers received land, religious toleration (Orthodox Serbs under a Catholic crown), and exemption from feudal dues in exchange for perpetual militia duty; a two-century institutionalized garrison-settlement belt.
- **Roman coloniae** (veteran colonies as instruments of both defense and Romanization) and late-imperial **limitanei** (frontier soldier-farmers); **Cossack hosts** (autonomy and land for border service, with the registered-Cossack bargain repeatedly renegotiated); Chinese **tuntian** agricultural garrisons (Cao Cao, 196 CE) and the Ming **weisuo** system.
- **The marcher-lord bargain:** Welsh Marches lords held quasi-palatine liberties (own courts, castles, private war) *because* they defended the frontier — and were, precisely for that reason, the crown's most chronic over-mighty-subject problem.

Valoria hooks: `march_layer` exists; Outposts/Villages exist; the registry's `governor_emergence` field (declared, never read) is a marcher-lord counter waiting for a derivation rule; Varfell's "tribute and conscription" identity and the Askeheim/Altonian frontiers give natural placement.

### T9. Succession interregna, regency, and partition

- **Ernst Kantorowicz, *The King's Two Bodies* (1957):** the legal fiction that the corporate Crown never dies ("the king is dead, long live the king") was *engineered specifically to abolish the interregnum* — the moment when obligations lapse and every charter-holder tests the new hand. Normal succession preserves institutional Legitimacy precisely because the corporate person persists; contested succession exposes every settlement's acceptance to re-negotiation.
- **Regency:** minority rule was the stress test — Henry VI's minority council (1422–37) governed for fifteen years through a conciliar compact; the French regency crisis of 1483–84 forced the Estates-General of Tours; Castilian regencies repeatedly fractured into magnate coalitions. Structural signature: during regency the council's members' *own* agendas leak into faction conduct (in PP-686 terms: cascade α of non-leader roots rises), the polity avoids initiating major action, and rivals probe.
- **Partition:** Frankish partible inheritance (the *divisio regnorum*; **Treaty of Verdun, 843** cutting the Carolingian empire into three) shows splits producing durable successor polities along resource/affinity lines rather than clean halves; the Ottoman alternative — Mehmed II's kanunname legitimizing **fratricide**, later replaced by *kafes* seniority — shows the other equilibrium: destroy co-claimants to prevent partition, at moral-legitimacy cost.

Valoria hooks: the Generational Shift clock ages leaders toward death but nothing catches the interregnum; `succession()`'s split ratios (0.60/0.55/0.50) are uncited; PP-686 §3.5.1 gives `succession normal → L +1` with no theory attached.

### T10. Legitimacy theory proper: Weber, Olson, Hirschman, Ibn Khaldun

- **Max Weber (*Economy and Society*, 1922):** three pure types of legitimate domination — **traditional** (sanctity of immemorial rule), **legal-rational** (belief in enacted procedure), **charismatic** (devotion to demonstrated extraordinary performance). This is the cleanest available theorization of Valoria's own L/PS split: **settlement Legitimacy (slow, institutional) = traditional + legal-rational acceptance; Popular Support (fast, performance-keyed) = the charismatic/performance channel** — and Weber's routinization-of-charisma is exactly the L←PS drift the §1.8 feedback already implements. The doc's α (outcomes) / β (conduct) temperament weights are a Weberian mixture parameter. This costs nothing to adopt and gives the whole LPS-2e edifice a named theoretical spine.
- **Mancur Olson, "Dictatorship, Democracy, and Development" (*APSR*, 1993):** the **stationary bandit** rationally moderates extraction and invests in governance because he internalizes future output; the **roving bandit** takes everything. Time horizon, not virtue, drives governance quality. Mechanically: governing yield should scale with secure tenure; fresh conquerors and about-to-collapse factions should govern extractively or badly.
- **Albert Hirschman, *Exit, Voice, and Loyalty* (1970):** a declining polity's members exit (emigration — settlement_layer already has "population leaving" as flavor), voice (petitions — the proposal's card family), or stay loyal (loyalty = the damping term); loyalty buys time for voice to work. Supplies a unifying frame for Weight loss, Petition cards, and high-L damping.
- **Ibn Khaldun, *Muqaddimah* (1377):** *asabiyyah* — group cohesion — is strongest in the founding generation and decays by the third–fourth as the dynasty urbanizes and luxuriates; his cycle is the classical theory of exactly what the Generational Shift clock (settlement_layer §7.1) hand-waves.
- Supporting: **Jack S. Levy (*War in the Modern Great Power System*, 1983)** — great powers were at war in ~95% of 16th-century years, declining by century thereafter — evidence that a high baseline war-weight in the action mix is *defensible*, but that war-proneness tracks system state (opportunity, capability preponderance — cf. Blainey, *The Causes of War*, 1973), not a coin flip.
- **Tribute without humiliation:** Ragusa (Dubrovnik) paid the Ottoman *haraç* for centuries while *prospering* — tribute purchased trade access across the Ottoman world and de facto protection; the Danegeld shows the extortion-spiral variant ("once you have paid him the Dane-geld / you never get rid of the Dane"). Tributary status ran the full range from ruinous to lucrative depending on what it bought — Valoria's flat `Tributary → Stability −1/year` models only the humiliation pole.

---

## STEP 3 — Concrete mechanical distillations

Each proposal: **target file + section · mechanic (stat / formula-shape / trigger / verb) · historical grounding · status** (`promote-ready` = a design-authoring pass can write it into the doc as PROPOSED without a taste ruling; `needs_jordan` = genuine fork / roster addition / tone call). All numeric values below are shape-suggestions to be sim-calibrated, per §7 discipline — none should be committed as ledger constants without a seeded run.

### FA lane — fiscal spine

**FA-1. Fiscal Stance (extraction rate) — the missing tax decision.**
*Target:* new § in `faction_layer_v30` (or the ED-FA-0002 `domain_actions` home doc, which is the better landing zone since it is already work-ordered); consumed by `sim/territory/registry.py` (per-settlement yield) and the Accounting Treasury rollup.
*Mechanic:* per-faction (or per-province) stance ∈ {Light, Standard, Extraction}. Treasury yield per settlement = `Prosperity × k × rate_mult × compliance(L_s)`, where `compliance(L_s)` rises with settlement Legitimacy (shape: `0.5 + L_s/14`, i.e. 50%–100%) — Levi's quasi-voluntary compliance made literal. Extraction stance: yield ×1.5, but settlement PS −1/season and Order decay resumes; Light: yield ×0.75, PS +1 in dearth seasons only (Scott: remission in bad years is what registers).
*Grounding:* Levi 1988 (compliance–legitimacy coupling); Brewer 1989 (FacilityTier could add +10%/tier yield — administrative capacity); Scott 1976 (invariance-under-dearth trigger, see SE-2); Tilly 1990.
*Status:* **promote-ready** as shape (it fills an admitted void and touches only PROVISIONAL surfaces); rate constants sim-calibrated. Interaction with the `governance_play_redesign` Levy verb should be declared (Levy = one-off spike on top of stance).

**FA-2. Muster re-grounded as fiscal-military purchase.**
*Target:* `sim/provincial/faction_action.py::_try_muster` + `faction_layer` §5.7 vicinity.
*Mechanic:* Muster costs `W −1` up front (mercenary contract / provisioning); pool = Mil + floor(W/2) (money raises troops); on Failure the Wealth is still spent (currently the sim charges W only on failure — historically inverted: you pay the enterpriser whether or not the muster prospers). Keep FSS-LOOP-2 re-muster untouched (already grounded).
*Grounding:* Fritz Redlich, *The German Military Enterpriser and His Work Force* (1964) — the condottiere/Wallenstein model: armies were purchased instruments; Tilly's extraction→coercion loop; composes with the already-anchored Habsburg re-muster rule.
*Status:* **promote-ready** (fixes an internal incoherence the corpus itself created by citing the fiscal-military cycle elsewhere).

**FA-3. Coercion-intensive vs capital-intensive muster asymmetry (Hafenmark/Varfell).**
*Target:* `faction_canon_v30` Part B (Hafenmark, Varfell sheets — both currently missing from Part B; this is content for their authoring) + `faction_layer` doctrine notes §1.5.
*Mechanic:* Hafenmark musters via capital: may substitute `W −2` for the Mil prerequisite (hired companies), no PS cost. Varfell musters via conscription: no W cost, but PS −1 in the levied province (the levy is the tax). Same verb, two political economies.
*Grounding:* Tilly 1990's capital-intensive (Venice/Holland) vs coercion-intensive (Brandenburg/Muscovy) trajectories; Varfell's own Mission text ("tribute and conscription", `faction_state_authoring §5`).
*Status:* **needs_jordan** — it differentiates faction identity mechanically (a design-taste surface Jordan has previously reserved, cf. ED-776 leaving Hafenmark equipment expression open).

**FA-4. Farm the Revenues (collection-mode toggle).**
*Target:* ED-FA-0002 domain-actions home doc; per-province flag consumed at Accounting; interacts with `registry.py` brokers (§4.8).
*Mechanic:* verb `Farm Revenues (province)`: immediate `W +2` (the farmer's advance), then for its 4-season term the province yields −25% to Treasury, PS −1/season in farmed settlements, and one Intelligence-Broker-grade NPC ("the Farmer") is created with a stake in extraction — a leverage/exposure surface for rivals (Investigate/Expose hooks already exist in the proposal). Early termination = buy out the farm (`W −2`) or eat a Grudge tag.
*Grounding:* Roman publicani; Ottoman iltizam/malikâne 1695 (term-length as the design dial); French Ferme Générale (odium accrues to the state; the farmer as political actor — 1794 as the worked example of deferred legitimacy cost).
*Status:* **promote-ready** as a PROPOSED verb (bounded, reversible, sits on existing broker machinery); term/magnitudes sim-calibrated.

### FA lane — action selection & conquest

**FA-5. State-conditioned action mix (retiring M7_ASSUMPTION_SIX).**
*Target:* `sim/provincial/faction_action.py::faction_take_action` + a short grounding note in the domain-actions home doc.
*Mechanic:* keep the 30/35/20/15 vector as the *prior*, then re-weight by state before drawing: Conquest weight ×(1 + 0.5·has_CB + 0.5·Mil_advantage_vs_best_target) (opportunity-driven war); Govern weight ×(1 + deficit) where deficit = share of owned territories below Accord 2 (the stationary bandit maintains what he keeps); Muster weight ×(1 + threat) with threat from GD-2's own eligibility signal; renormalize. Degenerates to the current mix in a neutral state, so the v17 oracle remains the zero-state baseline.
*Grounding:* Levy 1983 (high war baseline is period-correct — great powers at war ~95% of 16th-c. years — so the fix is *conditioning*, not pacification); Blainey 1973 (wars cluster where power preponderance/opportunity is perceived); Olson 1993 (maintenance investment scales with secure holdings).
*Status:* **promote-ready** as shape — it strengthens an existing GD-2 commitment ("mandatory before stochastic") rather than contradicting anything; multipliers sim-calibrated. NOTE: must be staged with ED-FA-0004 (the module is PORT-BLOCKING pre-LPS-1; this proposal should ride the Stratum-B rewrite, not precede it).

**FA-6. Storm vs Terms at conquest (differentiating the −25).**
*Target:* `sim/provincial/faction_action.py::_try_conquest` + `mass_battle_integration_v30 §4.10` + `settlement_layer §5.1` (siege).
*Mechanic:* on attacker victory, a Terms fork: **(a) Accept surrender on terms** — available if defender not routed (degree Success, not Overwhelming): Accord −10 (not −25), settlement L seeds at 2, Prosperity intact, defender garrison marches out (defender Mil partially preserved — honors of war); **(b) Storm** — always available: current effects (Accord −25), Prosperity −1 (battle damage); **(c) Sack** (only after storm): `W +2` to attacker, settlement PS→0, Order→0, and *every other settlement on the peninsula* shifts PS −1 toward the attacker for 2 seasons (the Magdeburg effect — atrocity is cheap locally, ruinous reputationally). Siege already ends in surrender at Order 0 → siege capitulation takes branch (a) pricing by construction, making siege the legitimacy-preserving slow path (consistent with ED-SETT-04's intent).
*Grounding:* Grotius III; Parker 1994 (the breach-and-chamade convention); Sack of Magdeburg 1631 / Rome 1527 (reputational contagion); dovetails with the treaty-mode Accord table faction_layer §2.3 already has for *diplomatic* transfers.
*Status:* branches (a)/(b) **promote-ready** (they refine a fiat constant along an axis the corpus already models for treaties); branch (c) Sack **needs_jordan** (atrocity content and a W-for-legitimacy exchange rate is a tone/taste ruling).

**FA-7. Regency interregnum on leader death.**
*Target:* `faction_behavior_v30 §3.2/§3.9` (edge cases) + `faction_layer §1` + Generational Shift consumers.
*Mechanic:* when a leader dies (Generational Shift, assassination) with no adult designated heir: faction enters **Regency** until succession resolves — unique action locked; Mandate read −1 (effective, not stored); cascade re-resolves with council members as temporary multi-roots at elevated α (their private agendas leak — PP-686 already has the machinery: this is a defined trigger for §3.2.2 multi-root plus §3.2.5-style damping suspension); rival factions gain a CB-grade window (Adjacent-Instability CB vs the regent faction qualifies automatically).
*Grounding:* Henry VI minority council 1422–37; Estates-General of Tours 1484; Castilian regency fractures; Kantorowicz 1957 for why *normal* succession does NOT trigger this (the corporate crown never dies — see SE-6).
*Status:* **needs_jordan** — a new subsystem state (bounded, but it changes campaign texture and interacts with the Royal Assassination fuse arcs D/E/F).

**FA-8. Protected-Tributary treaty variant.**
*Target:* `faction_layer_v30 §3.1` treaty table.
*Mechanic:* second Tributary row: **Protected Tributary** — tributary pays `W −1/year` AND gains hegemon trade access (`W +1/year` gross — net 0) plus casus foederis (hegemon must respond to attacks on the tributary within 1 season or lose L in all its settlements); Stability cost 0 (vs the existing row's −1/year). The existing row becomes "Extortive Tributary" (Danegeld pole).
*Grounding:* Ragusa's haraç relationship with the Porte (tribute purchasing prosperity and protection, 15th–19th c.) vs the Danegeld spiral; Ottoman millet/tributary gradation generally.
*Status:* **needs_jordan** — a genuine fork (does Valoria want subordination-without-humiliation as a stable diplomatic equilibrium? It softens the hegemony path GD-1 counts Tributary toward).

**FA-9. Guild collective embargo (grounding "Economic Leverage").**
*Target:* `faction_canon_v30 §9` (Guilds row) + eventual Guilds sheet in Part B; NPC behavior `faction_layer §5.8`.
*Mechanic:* Guilds unique action **Withdrawal of Trade** (Verhansung): target faction's Port/City/Mine settlements yield −50% Treasury and Prosperity growth frozen while active; costs Guilds nothing but exposure (each season active, target may attempt a counter-charter or seizure); ends when target restores/grants a Guild privilege (charter tag) or buys them out. Distinct from Parliamentary Embargo (§5.4) — this is *private*, no vote, no Mandate minimum, which is exactly its historical character.
*Grounding:* Hanseatic blockades of Bruges 1358 & 1451–57 (privilege enforcement by collective trade withdrawal, no army required); London Steelyard privilege fights.
*Status:* **needs_jordan** (adds an action to an NPC faction's roster — same class of call as the blocked Church/Hafenmark roster items; but flag that it gives the Guilds' existing "Economic Leverage ≥ Guild Favour 5" line its missing mechanism).

### SE lane — the L/PS derivation layer (ED-FA-0004 Stratum-B fuel)

**SE-1. Weberian derivation table for per-settlement L and PS (the Stratum-B event list).**
*Target:* `settlement_layer_v30 §1.8` (new subsection "L/PS derivation events, settlement grain"); implements toward `registry.py`'s inert fields.
*Mechanic:* enumerate settlement-grain events by channel — **L-channel (traditional/legal-rational):** entry oath sworn / privileges confirmed (+1 one-time), charter granted (+1), regular court held (Hold Court ≥2 consecutive seasons, +1 cap), succession `normal` (no change — continuity, see SE-6), tithe/tax collected *within announced stance* (0; but stance broken → −1), governor rotated per policy (0) vs governor imposed over protest (−1). **PS-channel (charismatic/performance):** dearth relieved (+2), festival sponsored (+1), settlement defended from raid (+2), levy taken (−1), forced billeting/garrison in home (−1), public execution of a local (−2). The §1.8 Mandate feedback (L +1 drift toward Mandate) is retained and *named*: routinization of charisma.
*Grounding:* Weber 1922 (the L/PS split is his traditional+legal vs charismatic-performance distinction — adopting the typology also justifies α/β temperament as a mixture weight); Hirschman 1970 (loyalty as damping).
*Status:* **promote-ready** — this is the highest-value item in the report: it converts the registry's inert fields into a specified pipeline, is pure addition to a section Jordan already ruled on (LPS-2e), and every row above is an event type the corpus already emits or the proposal already names. Magnitudes sim-calibrated.

**SE-2. Dearth chain + granary (the moral-economy engine).**
*Target:* `settlement_layer §4.3` (replace the one-line famine row) + `governance_play_redesign` deck (Crisis family) + new registry field `granary: int (0–3)`.
*Mechanic:* **Dearth** triggers on entitlement failure, not just Prosperity 0: any of {Prosperity 0; grain-route cut (SE-3); Levy/Extraction stance in a Prosperity ≤1 settlement}. On trigger, the governor's response verb sets the outcome: **Open Granary** (requires granary ≥1: −1 granary, Order/PS unchanged, PS +1 — Scott's remission); **Fix Prices** (Thompson's *taxation populaire* pre-empted: Order −0, Guild/merchant Disposition −1, black-market emergence check); **Requisition** (feed this settlement by stripping a neighbor: displaces the dearth); **Ignore** (Order −2, PS −2, riot card targeting millers/merchants first, THEN the governor — Thompson's targeting order made mechanical). New verb **Provision** (1 AP): granary +1, `W` cost. Extraction-invariance clause: taking the *standard* levy during Dearth counts as Ignore (Scott: it is the invariance that detonates).
*Grounding:* Thompson 1971; Scott 1976; Sen 1981 (entitlement trigger); cura annonae; Will & Wong 1991 (*changpingcang* — the granary verb); Tudor Book of Orders 1587 (Fix Prices).
*Status:* **promote-ready** as a PROPOSED §4.3 replacement riding the governance_play_redesign ratification track (ED-SE-0001); granary cap/magnitudes sim-calibrated.

**SE-3. Grain routes — mechanical teeth for ED-054/BALANCE-005.**
*Target:* `settlement_adjacency_v30` (edge attribute) + `geography_v30` open items + `settlement_layer §4.3`.
*Mechanic:* tag breadbasket provinces (T5 Feldmark, T6 Stillhelm; Feldmark Storehouse sub-feature is the anchor) as grain sources; each non-breadbasket province needs a traced route (existing adjacency graph) to a source or a Port; a cut route (occupation, blockade, siege of a waypoint) puts dependent settlements one season from Dearth (SE-2). Hafenmark (whose provinces are highland/mining) becomes structurally grain-dependent through the T8↔T9↔T2 corridor or Schoenland imports via Port — closing the exact "Feldmark unreachable by Hafenmark" complaint by making the *dependency itself* the mechanic rather than adjacency.
*Grounding:* Athens' Black Sea grain law; Rome's Egyptian fleet (cura annonae's strategic face); Hansa/Danzig Baltic grain; siege as entitlement warfare (Sen).
*Status:* **promote-ready** (closes a named open item using only existing graph machinery); route-tracing rule needs one design decision (per-province vs per-settlement tracing) flagged inline, defaulting to per-province.

**SE-4. Charters, quo warranto, and prescription (re-grounding §3.3 grant/revoke).**
*Target:* `settlement_layer §3.3` + Ledger tags (`governance_play_redesign §1.6` — Charter as a durable tag).
*Mechanic:* granting subnational management writes a **Charter** tag (durable, survives succession) with a grant-season. Revocation Ob is no longer flat: Ob = base + floor(charter_age/8) (prescription — privilege hardens into right); revocation of a charter older than ~16 seasons is a **Quo Warranto scene** (social contest with the subnational leader, public) and on success still costs Order −1 *in every settlement that faction-type manages peninsula-wide* (London 1683: revoking one city's charter frightened every chartered city). New-controller interaction: see SE-5. Confirmation-for-fee: at control transfer or succession, confirming existing charters yields `W +1` (the confirmation fine) and L +1 in chartered settlements.
*Grounding:* Magdeburg-law charter diffusion; Edward I quo warranto 1278–94; City of London 1683/1690; accession confirmation fines; prescription doctrine.
*Status:* **promote-ready** (refines an existing PROVISIONAL rule in-place; the peninsula-wide revocation echo is the only bold stroke — flag it inline as vetoable).

**SE-5. Entry Terms at control transfer (Confirm vs Impose).**
*Target:* `settlement_layer` new §5.3 + `faction_layer §2.3` Accord-on-transfer tables (compose, don't replace).
*Mechanic:* whenever settlement control transfers (conquest branch (a)/(b) of FA-6, treaty cession, seizure), the new controller chooses: **Confirm Privileges** (Joyeuse Entrée): keep all Charter/Precedent tags, settlement L seeds at 3, fiscal stance capped at Standard for 4 seasons; **Impose Administration:** strip tags, L seeds at 1, no stance cap, Order −1. The existing treaty-mode Accord table remains the Order-side effect; this adds the L-side and gives the §1.8 pipeline its transfer-boundary rule (currently: nothing seeds L/PS on transfer at all — LPS-2e only specifies game-start seeding from `faction_state_authoring §8`).
*Grounding:* Joyeuse Entrée of Brabant 1356 (conditional obedience sworn at entry); Henry I's coronation charter 1100; universal accession-confirmation practice; Olson 1993 (Impose = roving-bandit pricing).
*Status:* **promote-ready** — it fills a specified hole (transfer-boundary L/PS seeding) with a two-option fork whose *existence* is historically forced even if magnitudes move.

**SE-6. Succession continuity rule (the King's Two Bodies patch).**
*Target:* `faction_behavior_v30 §3.5.1` + `settlement_layer §1.8`.
*Mechanic:* `state.succession` with `mode == normal`: settlement L unchanged (the corporate crown never dies) and the one-time +1 applies only where an entry/confirmation ceremony is performed (ties to SE-5's confirmation-for-fee). Modes `contested/emergency/imposed`: L −1 in all held settlements (interregnum exposure) and Regency check (FA-7).
*Grounding:* Kantorowicz 1957 — the fiction was engineered to abolish the interregnum; *dignitas non moritur*.
*Status:* **promote-ready** (it sharpens an existing PP-686 rule and cites the canonical theory of why).

**SE-7. Residencia / Visita / Rotation — the oversight toolkit (naming + completing §1.4 of the proposal).**
*Target:* `governance_play_redesign §1.4` (riding ED-SE-0001) + registry `suspicion` semantics.
*Mechanic:* three named instruments for the Provincial Authority: **Visita** (surprise inspection, any season, cheap: reveals true settlement state + governor tag ledger; suspicion −1 or +2 depending on findings); **Residencia** (mandatory end-of-tenure audit scene when a governor leaves office *for any reason*: a social contest where accumulated Grudge/Debt tags are literally the evidence dossier — sworn complaints from the governed); **Rotation policy** (faction-level: governors rotate every N seasons — clears local Grudge/Precedent tags (anti-capture) but each rotation costs Order −1 and forfeits Precedent bonuses (local knowledge lost — rule of avoidance's known price)). Suspicion threshold → early Residencia (the existing Recall scene, now named and evidenced).
*Grounding:* Castilian/Indies residencia & visita; Ming–Qing rule of avoidance + Censorate; Ottoman timar rotation (and its malikâne decay as the venality warning).
*Status:* **promote-ready** (it is a naming-and-mechanism completion of machinery the proposal already asserts; the tags-as-evidence link is pure composition). The venal-appointment variant (sell a governorship: `W +2` now, governor α ↑, audit rights waived — the *paulette*) is **needs_jordan** (tone: does Valoria sell offices?).

**SE-8. Advowson + Local Interdict (parish-level church-state seam).**
*Target:* `settlement_layer §1.5–1.7` extension + registry (`religious_building` gains a `patron: faction|church` attribute; `church_attention` gains a derivation) + Church roster in `faction_canon §9`.
*Mechanic:* **(a) Advowson:** every settlement with a religious building has a *patron* who nominates its priest — default Church, but grantable/purchasable/claimable (a Charter-class tag). Patron biases the pulpit: province-faction patron → PT drift −0.25/season and Parish Order bonus retained; Church patron → PT +0.25 and `church_attention` +1/season. Contested via court scene (darrein presentment as a Hold Court card) — a *settlement-scale* church-state fight that never touches the faction layer. **(b) Local Interdict:** Church action against one settlement (Ob vs controller L): suspends Parish Social Services (§1.6 bonuses off), Order −1/season, PS −1/season *toward the controller*; but each season active, cumulative 1-in-6-style check → Church L −1 in that settlement (resentment cuts both ways, John's England); auto-ends on concession or absolution. Slots below Excommunication in the `_try_faction_unique` Church ladder.
*Grounding:* advowson & assize of darrein presentment; Constitutions of Clarendon 1164 / Becket (jurisdiction seam); Innocent III's interdict of England 1208–14; Venice interdict 1606; composes with the already-canonized Geneva-trap parish bonuses (§1.6 — same instrumental logic, coercive face).
*Status:* Advowson **promote-ready** (it gives two inert registry fields their derivation and reuses existing scene machinery); Local Interdict **needs_jordan** (Church roster addition — same class as the blocked Pass-2f Church items, so it should queue behind, or with, that audit).

**SE-9. Military colony + marcher autonomy (deriving `governor_emergence`).**
*Target:* `settlement_layer` Part 5 + `march_layer_v30` + registry `governor_emergence` derivation; muster interaction in FA-2.
*Mechanic:* **(a) Plant Colony** (faction action or 2-AP governor verb at a Village/Outpost on a frontier province): `W −1` + one season → settlement becomes a garrison-colony: Defense +1 permanent, militia defends without garrison upkeep, L seeds 5 *toward the founder* (settlers owe him), PS seeds 1 (natives displaced), Weight +1 after 8 seasons (the colony takes root). **(b) Marcher autonomy:** in frontier provinces (border edge to Altonia passes or Askeheim gates), governor `suspicion` accrues at half rate (the crown needs the march held and asks fewer questions) but `governor_emergence` +1/season while the governor personally wins defensive engagements — at threshold, the governor may take the Stage-2→3 faction-emergence path *with the colony settlements as his base* (the over-mighty marcher lord, now a derived pipeline instead of an unread int).
*Grounding:* Byzantine themata / stratiotika ktemata (the 04-28 corpus already gestures at "themata-civil rivalry" in a stress-test aside — file 10 — this proposal is that aside made mechanical); Habsburg Militärgrenze Grenzer bargain (service-for-land-and-toleration); Roman coloniae & limitanei; tuntian/weisuo; Welsh Marches palatine liberties → over-mighty-subject problem.
*Status:* (b) **promote-ready** (it is a derivation rule for an existing declared field, feeding the existing GD-3 emergence pipeline); (a) **needs_jordan** (new action + a settlement-creation-adjacent effect — touches the fixed 37-settlement registry, so it must be framed as *converting* an existing Village/Outpost, never adding nodes — flagged so the authoring pass doesn't drift into registry growth).

**SE-10. Weight loss as Exit (Hirschman closure).**
*Target:* `settlement_layer §1.8` (Weight) + §4.3 (Prosperity-0 row).
*Mechanic:* a settlement that spends ≥2 consecutive seasons in Dearth or at Order ≤1 loses 1 Settlement Weight (emigration — "population leaving" made mechanical, lowering its Mandate contribution and its Treasury base); Weight recovers +1 per 4 stable seasons (capped at type base + Prosperity + FacilityTier as now). Exit destination: +0.5 Prosperity-growth season in the nearest higher-Order settlement (Stadtluft macht frei — towns grew by absorbing the countryside's refugees).
*Grounding:* Hirschman 1970 (Exit as the silent vote); *Stadtluft macht frei* custom (year-and-a-day town freedom as the exit magnet).
*Status:* **promote-ready** (small, closes the loop between the flavor text and the §1.8 aggregate; makes misgovernance bite Mandate through the channel LPS-2e built).

### Citation patches (near-zero-risk grounding annotations, all promote-ready)

- **CP-1.** `contest/faction.py §7.2.1` split ratios (0.60/0.55/0.50): annotate with partition precedent — Treaty of Verdun 843 (three-way *divisio* along affinity lines; splits produce durable successor polities, never clean halves) and the Western Schism's asymmetric obediences. Target: code comment + `faction_succession_split_v30`.
- **CP-2.** `settlement_layer §7.1` Generational Shift: annotate with Ibn Khaldun's *asabiyyah* cycle (Muqaddimah — third/fourth-generation decay); optionally add founder-cohesion `Sta +1` that expires at Threshold 2 (**this option needs_jordan**; the annotation alone is promote-ready).
- **CP-3.** `parliamentary_vote.py` abstention-resistance (`BG_VOTE_ABSTAIN_*`) and `band_of` committee margin: annotate with Venetian balloting's *non sinceri* (the formal uncommitted ballot; high non-sinceri counts sent measures back for redrafting — committee referral as institutional fact, composing with the broglio material already mined by the 06-28 corpus).
- **CP-4.** `faction_layer §3.5` CB + War Authorisation: annotate with Roman fetial procedure (*rerum repetitio* — the formal demand for redress with a compliance window before war was religiously licit) and the medieval *diffidatio* (formal defiance dissolving the bond before hostilities); optionally add a "Demand Redress" step that converts a CB into either compliance-extraction or a −1 Ob first strike (**option needs_jordan**).
- **CP-5.** Crown Initiative modes: Royal Progress ← itinerant kingship (Ottonian/Angevin iteration; Elizabeth I's progresses — presence as governance, the court eating the countryside as extraction-cum-theater); Coronation Renewal ← *Festkrönungen* (ritual crown-wearings at Christmas/Easter/Whitsun) and the *Laudes Regiae*; Great Work ← cathedral/civic-works legitimacy (and its fiscal shadow: Beauvais). Target: `ci_political_v30`/part10 §3.2–3.4 annotations.

### Priority & sequencing recommendation (for the follow-on authoring pass)

1. **SE-1** (L/PS derivation table) — unblocks everything; it is the Stratum-B fuel ED-FA-0004 says is missing.
2. **SE-5 + SE-6** (transfer-boundary and succession-boundary L rules) — the two boundary conditions SE-1 needs.
3. **FA-1 + FA-2** (fiscal stance + muster purchase) — the extraction spine; then **SE-2/SE-3** (dearth + grain routes; closes ED-054/BALANCE-005).
4. **SE-7, SE-4** ride the ED-SE-0001 governance_play_redesign ratification track.
5. **FA-5, FA-6(a/b)** ride the ED-FA-0004 Stratum-B faction_action rewrite.
6. needs_jordan queue (one consolidated decision memo): FA-3, FA-6(c), FA-7, FA-8, FA-9, SE-7-venality, SE-8(b), SE-9(a), CP-2/CP-4 options.

### Anti-fabrication note

Per CLAUDE.md §5/§7: every number above is a **shape proposal**, not a ledger value. The follow-on authoring pass should file each adopted proposal under a fresh `ED-FA-`/`ED-SE-` id, cite this report as provenance, and route any constant that reaches `sim/` through a seeded calibration run before it is ledgered — the historical citation grounds the *mechanism*, never the magnitude.
