Verification complete — I opened every file I cite. Here are the four sections.

---

# §3 FLATTEN — "settlement-governance"

Every `status` below is measured against the working tree, not against a document's own header. **INERT** means the code exists and executes correctly when called, and nothing calls it.

### Primitives

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| `Settlement` | primitive | The base civic unit: 25 fields spanning identity, three stats, political acceptance, governance economy, presences, memory, and deck state | BUILT — 8 of 25 fields ever populated | `systems/settlements/sim/registry.py:54` |
| `prosperity` / `defense` / `order` (0–5) | primitive | The only three settlement stats loaded from data; Order is the input to province Accord | BUILT | `registry.py:61-63`, seeded from `valoria_geography_v30.yaml` |
| `legitimacy` / `popular_support` (0–7) | primitive | Per-settlement political acceptance — the aggregation input to faction Mandate, and the consent gate on the governance cascade | INERT — declared, serialised, no read or write outside `to_dict`/`from_dict` | `registry.py:69-74` |
| `governor_id` | primitive | Who holds the seat | INERT — its only writer is `succeed_governor`, which nothing calls | `registry.py:61` |
| `npc_ids` | primitive | The settlement's resident cast, uncapped | INERT — empty list, no writer anywhere | `registry.py:87` |
| `ledger` (list of `LedgerTag`) | primitive | Durable governance memory that lives on the *place*, not the officeholder, so it survives succession | INERT — no production writer | `registry.py:88`, `ledger.py` |
| `TAG_KINDS` = Precedent · Grudge · Debt · Reputation · **Leverage** | primitive | The closed five-family memory vocabulary. Compact is a recurring Debt subtype (`Debt(key="compact:<quota>", ttl=term)`), ruled ED-IN-0046 D3, which unblocks §1.3a | BUILT (enum) / INERT (nothing writes tags) | `ledger.py:30` |
| `suspicion` | primitive | The governor's accumulated exposure to audit and recall | INERT — zero writers tree-wide | `registry.py:78` |
| `pressure` (Π), default 4.0 | primitive | Per-settlement pressure scalar that would drive event-deck draw count and family bias | INERT — zero writers; no homeostat code on `main` | `registry.py:79` |
| `facility_tier` (0–3) | primitive | Built institutional infrastructure; drives AP and Settlement Weight | INERT — never set; all 37 settlements load at 0 | `registry.py:77` |
| `active_directive` | primitive | The Provincial Authority's standing order for the season | INERT, and typed bare `str \| None` with no enum enforcement | `registry.py:81` |
| `subnational` (dict) | primitive | Footholds of the seven subnational archetypes (Church, Guilds, Ministry, Löwenritter, RM, Wardens, Niflhel) | INERT — round-trips through serialisation, nothing populates it | `registry.py:86` |
| `religious_building` | primitive | Church building tier on the settlement | INERT, and shadowed: the live store is `InfrastructureState.religious_building`, keyed by *territory* | `registry.py:82` vs `infrastructure.py` |
| `church_attention` / `governor_emergence` | primitive | Inquisitor pressure; a governor's drift toward independent faction emergence | INERT | `registry.py:83-84` |
| `open_needs` / `deck_state` | primitive | Per-settlement carrier for the event deck's unresolved asks and draw history | INERT — the deck does not exist | `registry.py:89-90` |
| `InfrastructureState` (4 church axes) | primitive | Religious Building / Templar Station / Inquisitor Base / Church Governor, combinable in any configuration | Read side BUILT (`count_infrastructure`, `seizure_ob_modifier` called by `mass_seizure.py:53`); write side INERT | `systems/settlements/sim/infrastructure.py` |
| Settlement type roster | primitive | Code accepts 11 types; the Weight table defines base values for 9 | BUILT with a canon hole — Fortress-City and Cathedral-City have no Weight | `registry.py:45` vs `settlement_layer_v30.md:160` |
| Two-Tier Authority (Provincial Authority / Settlement Governor) | primitive | Two authority slots per settlement whose disagreement is the intended source of governance tension | DESIGNED | `settlement_layer_v30.md:526` |
| Institutional Facility slots (Wing/Suite/Chamber/Billet) | primitive | Finite, faction-allocated seats for rank-holders; capacity by settlement type | DESIGNED | `settlement_layer_v30.md:63-69` |
| Clerk Capacity (0–3) + hidden Clerk Corruption | primitive | A second, opaque AP source bought with Wealth that silently raises Intrigue weight | PROPOSED | `governance_play_redesign_v1.md` §1.1a |
| Event card + seven families | primitive | Petition/Friction/Opportunity/Crisis/Intrigue/Ambition/Thread, each with trigger predicates, Π-scaled weight, cooldowns, responses, follow-on seeds | PROPOSED | `governance_play_redesign_v1.md:166,189` |
| Standing crisis-defusing institution (class) | primitive | Build-once, family-scoped, ring-fenced from the ordinary Treasury/AP cycle — Granary, Water Board, Lazzaretto | PROPOSED | governance compendium pt. 44 |
| Five candidate new levers | primitive | StockLevel · Assessment tag · Capital-Posture · Consent-Rule · route/corridor Precedent — each changes what *kind* of decision a settlement presents | PROPOSED, held on ruling R-1 | `governance_ripple_substrate_v1.md:93` |

### Derivatives and formulae

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| `AP = 2 + facility_tier + (1 if Seat/Cathedral/Cathedral-City)` | formula | The season's action budget — the scarcity that makes governing a choice | INERT — the property computes; zero readers. All 37 load at facility_tier 0, so today it would be 2 everywhere except S-001, S-031, S-036 at 3 | `registry.py:92-97` |
| `province_accord = floor(mean member Order)` | derivative | Rolls settlement Order up to the province | BUILT — one production caller, and that caller is a report-only probe | `registry.py:185` |
| `province_effective_prosperity = Σ member prosperity` | derivative | Province economic pool | INERT | `registry.py:194` |
| Local Economy = P×50 · Garrison = D×20 + Fort×30 · Public Order = O×20 | formula | The videogame-facing derived values | INERT — `settlement.py` has zero importers | `settlement.py:34-38` |
| `W_s = base(Type) + Prosperity + FacilityTier` | formula | Settlement Weight — how much a settlement's acceptance counts | RULED-UNEXECUTED, with an arithmetic hole: no `base(Type)` for Fortress-City or Cathedral-City, i.e. S-014 Ehrenfeld and S-036 Himmelenger | `settlement_layer_v30.md:160` |
| `Mandate = clamp(round(7T/(T+6)),0,7)`, `T = Σ W_s·(q_s/7)`, `q_s = 0.5L+0.5PS` | formula | Faction Mandate as the size-weighted aggregate of settlement acceptance | RULED-UNEXECUTED — and D4 separately retired this expression as the collapse carrier, reserving "Mandate" for the faction meter | `settlement_layer_v30.md:163`; `governance_consolidation_v1.md:42` |
| `compliance(s) = clamp((q−1.0)/(6.0−1.0),0,1)` | formula | Throttles realised Treasury/AP by local acceptance — the mechanical form of the consent gate | PROPOSED | `lps_wiring_v1.md:85` |
| `control_state`: HELD q≥3 · CONTESTED 1≤q<3 · SLIPPING q<1 | formula | Two consecutive SLIPPING Accountings trigger an Independence roll, reusing the built insurgency 2-season cadence | PROPOSED | `lps_wiring_v1.md:100` |
| Π homeostat (corrected): `Π + needs + grudges + ambitions + shock − releases + sign(3−Π)·min(1,\|3−Π\|)`, clamp 0–10 | formula | The pressure meter's accrual and restoring terms | PROPOSED | `goldenfurt_slice/sim_build_spec.md:132` |
| Π bifurcation | formula | Arithmetic property, not a tuning choice: accrual ≤ 1.00/season settles at 3+accrual; accrual > 1.00 pins the ceiling in ≈(10−Π₀)/(accrual−1) seasons. Six ambition clocks contribute up to +3.0/season, so accrual > 1 is the default regime | — | derived from the formula above |
| `draw n = 1 + floor(Π/3)` | formula | 1 card at peace, 4 in crisis | PROPOSED | `governance_play_redesign_v1.md:203` |
| Charter revocation `Ob = ceil(subnational Influence/2) + floor(charter_age/8)` | formula | Privilege hardens into right with age; revoking an old charter becomes a public contest | PROPOSED | `settlement_layer_v30.md:589` |
| Entry Terms seeds | formula | Confirm Privileges: charter kept, L seeds 3, fiscal capped 4 seasons. Impose Administration: charter stripped, L seeds 1, Order −1 | PROPOSED — and the only rule anywhere that seeds L | `settlement_layer_v30.md:961` |
| Parish Social Services | formula | Chapel +0.5 Order/season, Church +1 once, Cathedral +1 once and Order-decay −1 | DESIGNED — `PT_GAIN_*`, `CI_GAIN_TEMPLAR`, `ORDER_GAIN_*` exist as constants in `infrastructure.py` with no code that applies them | `settlement_layer_v30.md:121` |
| `resolution_quality` | formula | The gap between what a Directive/Need demanded and what the season delivered, weighted by who you answer to — the event→standing bridge | PROPOSED, and unwired: no Demotion trigger reads it | `governance_ripple_substrate_v1.md:158` |

### Mechanics

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| `succeed_governor` | mechanic | Swaps the officeholder **and** sweeps the ledger, so durable tags (ttl=None) survive the handover — the player→world persistence guarantee | INERT — zero callers; nothing else writes `governor_id` | `registry.py:199-208` |
| `build_infrastructure` | mechanic | Installs a church axis on a territory | INERT on the write side — the only caller is a test | `infrastructure.py` |
| `seizure_ob_modifier` / `count_infrastructure` | mechanic | Church presence lowers the Ob of a Mass Seizure against that territory | BUILT — the one settlement-adjacent mechanic with a live production consumer | `infrastructure.py`, read by `mass_seizure.py:53,159,260` |
| Governor's Turn verb menu | mechanic | Develop · Fortify · Keep Order · Hold Court · Sponsor · Treat · Levy · Investigate, plus Retain Clerks, Survey, Negotiate Quota, Bind the Cells, Ordenanza, Petition-Defy — each with an AP cost, a roll, and a named political tradeoff | PROPOSED — no code for any verb | `governance_play_redesign_v1.md:47` |
| Old four-verb menu (Develop/Fortify/Pacify/Administer) | mechanic | One free stat-pump per season | DESIGNED, superseded by the AP menu; retained as fallback baseline | `settlement_layer_v30.md:550` |
| Directive response fork (Comply / Bargain / Defy) | mechanic | The mandatory down-stroke: the Provincial Authority's order, which the governor must answer | PROPOSED | `governance_play_redesign_v1.md` §1.4 |
| Pastoral Assumption | mechanic | With no governor and at least a Chapel, the Church installs a Church Governor at Ob 1 | DESIGNED | `settlement_layer_v30.md:135` |
| Bishop-Governor / Ecclesiastical Appointment | mechanic | Influence vs Ob 1; installs a bishop, redirects Prosperity/Order to the Church, fractures the province, generates no casus belli | DESIGNED | `conflict_architecture_proposal.md:48` |
| Charters + Quo Warranto | mechanic | Granting subnational management writes a durable Charter; revoking one older than ~16 seasons is a public social contest with a peninsula-wide Order −1 echo | PROPOSED | `settlement_layer_v30.md:589` |
| Za patron-lapse | mechanic | A guild charter carries a patron; if the patron's standing falls, privileges lapse automatically at Accounting with no contest, one season after a warning card | DESIGNED | `settlement_layer_v30.md:638` |
| Seggio Council | mechanic | 1–5 hereditary bodies with non-transferable privileges, sharing one joint council seat; not grantable or revocable by Domain Action | PROPOSED | `settlement_layer_v30.md:667` |
| Subnational Faction Governance | mechanic | Seven archetypes, each aligned to settlement types, each applying a distinct management effect when granted control | DESIGNED | `settlement_layer_v30.md:567` |
| RM Cell Resilience | mechanic | RM presence in 3+ settlements of a province adds +1 Ob to suppress, stacking with Inquisitor surveillance | DESIGNED | `settlement_layer_v30.md:577` |
| Dearth chain | mechanic | Fires on entitlement failure (Prosperity 0, cut grain route, or extraction at Prosperity ≤1), with five governor responses — Open Granary, Fix Prices, Requisition, Ignore, Provision | PROPOSED — requires a `granary` field that does not exist | `settlement_layer_v30.md:740` |
| Grain routes | mechanic | Breadbaskets and Ports are sources; every other settlement traces a route or sits one season from Dearth | PROPOSED | `settlement_layer_v30.md:795` |
| Settlement Events table | mechanic | 0–1 local events per season keyed on stats and type — Dearth, Raid, Local Revolt at Order 0, Flourishing at Order 5 + Prosperity 4 | DESIGNED — no evaluator exists | `settlement_layer_v30.md:724` |
| Black Markets / Intelligence Brokers / Thread Exploitation Sites | mechanic | Location-based emergent phenomena at low Order, high Prosperity, or low Thread Proximity | DESIGNED | `settlement_layer_v30.md:870` |

### Processes

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| World-gen settlement load | process | `populate_from_geography` registers all 37 settlements, validating type against `LEGAL_TYPES` | BUILT — but reads only the `settlements:` block, so 8 of 25 fields load; the authored `provinces:` block (17 provinces with anchor, polygon, fort_level, spiritual_weight, proximity_calamity, starting_pros, membership list) has no code reader at all | `registry.py:212-270` |
| Season accounting cascade | process | The live per-season loop: CI, MS at year-end, insurgency triggers, insurgency promotion, NPC ecology, province-Accord drift probe. **Six steps, none of which touches a settlement except the probe** | BUILT | `systems/overview/sim/accounting.py:96-143` |
| The two-stroke churn loop | process | The world always acts on the player (mandatory Directive + Π-guaranteed draw); the player always acts on the world (every verb emits a delta that becomes next season's trigger) | PROPOSED | `governance_play_redesign_v1.md:268` |
| VSG generation stack (P1–P15) | process | Fifteen weighted, seeded, conditioned paradigms drawing a settlement top-to-bottom, calibrated to reproduce Goldenfurt from its seed | PROPOSED — 1 of 15 weight tables authored | `settlement_generator_v1.md:39` |
| Suspicion → Recall spine (D5/D6) | process | Cumulative per-Defy suspicion, capped +1/season, triggering a G606 Recall scene with an always-available Submit-to-audit escape at −2 | RULED-UNEXECUTED — and ruled conditional on E11, a symmetric decay mechanic, landing in the same authoring pass | `governance_consolidation_v1.md:45,105` |
| Residencia / Visita / Rotation | process | Cheap surprise inspection, mandatory end-of-tenure audit where accumulated Grudge/Debt tags are the evidence dossier, and rotation that clears capture at the cost of local knowledge | PROPOSED | `fa_se_historical_precedent_research_v1.md:280` |
| Governor succession + protégé handoff | process | On death or removal the province must appoint or the settlement goes unmanaged at Order −1/season; a cross-generational handoff starts a new character at Standing 0 with Renown/2 | DESIGNED | `settlement_layer_v30.md:1121` |
| L/PS wiring pipeline (E5) | process | Five write-side sources accrued into `pending_dLPS`, applied once at the Accounting boundary, then aggregate → gate → consume, in a fixed five-step sequence | PROPOSED, buildable spec | `lps_wiring_v1.md` |

---

# §4 WITHIN-SYSTEM ANALYSIS — "settlement-governance"

### What playing this system is actually like right now

Nothing. Not "thin" — nothing. There is no season in which a settlement presents the player with a decision, because no code path reaches a settlement after world-gen.

Concretely: `create_world` loads 37 settlements from the geography file and fills eight of twenty-five fields. Then `run_accounting` runs six steps a season for the life of the campaign, and the only one that so much as looks at a settlement is a report-only probe that compares two Accord numbers, records a divergence counter, and writes nothing. Every settlement therefore ends the campaign exactly as it started, except where a *faction* action reaches down and writes `Territory.accord` over its head.

If you sat a player in front of this, they would govern nothing. The AP budget computes to 2 everywhere (facility_tier never leaves 0, so only the three Seat/Cathedral-City settlements reach 3). There are no verbs to spend it on. No Directive ever arrives, because `active_directive` has no writer. No card is drawn, because the deck engine — `governance.py`, `directives.py`, `events/` — does not exist; only S0 and S1 of the build spec ever landed. No pressure builds, because Π has no writer. No consequence is remembered, because the ledger has no writer. No governor is appointed or removed, because `succeed_governor` has no caller and there is no person to appoint.

The bleak part is how *close* it is. `succeed_governor` already does the subtle thing right: it sweeps expired tags and lets durable ones survive the handover, so a demoted governor's record outlives him. `ledger_add` already dedupes by (kind, key) and treats Reputation as a single read of the officeholder. The chassis is not a sketch. It is finished, correct, and parked.

### The load-bearing conflicts

**1. L/PS inert, and everything above it counterfactual.** `Settlement.legitimacy` and `popular_support` are declared, serialised, and touched by nothing but their own serialiser. Above them sit three ratified rulings — LPS-2e (acceptance is per-settlement, Mandate is its size-weighted aggregate), the consent-gate ruling (L/PS decides whether an imposed governance type sticks), and the hierarchy cascade that gate modulates. All three are reasoning about a field that no code reads. *What decides it:* nothing left to decide — `lps_wiring_v1.md` is a worked buildable spec, and the seed table already exists in `faction_state_authoring_v30` §8 with no loader. This is execution, not design.

**2. Two architectures for "what happens to a settlement each season," and content is being authored into both.** The 500-seed framework used a predicate sweep with no action economy; the redesign, Goldenfurt and the 58-card deck use a stateful Π-weighted deck on an AP budget. *What decides it:* already ruled. D1 makes the card deck canonical for player-facing play and demotes the predicate sweep to a balance-regression oracle; D2 makes the AP economy canonical. Both rulings are unexecuted, so the fork keeps re-presenting itself to anyone reading the docs rather than the rulings.

**3. The death-spiral bias.** Two independent methods converged: a 7-seed agent playout and a 500-seed executed run (whose harness has since left the tree with `sim/`, so its numbers stand as reported rather than re-derivable) both found the substrate biased toward unrecoverable collapse — Flourishing crowded out at roughly 3.7 events per seed against 659 revolts. The Π bifurcation explains the mechanism arithmetically: the restoring term saturates at ±1, so any accrual above 1.00/season pins the ceiling, and the design's own six ambition clocks supply up to +3.0 before a single unserved need. *What decides it:* the code, once written — and the ruling already says E1 cannot ship without E3 (a subsistence floor capping accrual) and E7 (a release path) in the same commit.

**4. Facility tier never rises, so the whole progression axis is flat.** `facility_tier` is the AP driver, a Weight term, and the institutional-slot ladder — and nothing sets it, including the loader. *What decides it:* the code; it is a loader gap, not a design question.

### What this system needs from others

**personnel-roster is the blocking dependency, and it is a missing entity, not a missing field.** `governor_id` needs a person; `npc_ids` needs a cast; recall, Residencia, suspicion and the entire Positional pressure vector need someone whose career is at stake. Faction carries no leader field at all, so even the succession Key has no coded source for its payload. Until people exist, succession is circularly blocked: nothing appoints because there is nobody to appoint.

**faction-strategy owns both ends of the churn loop.** The Directive — the mandatory down-stroke of the season — is a faction/Provincial-Authority artifact. Mandate, the consumer of aggregated L/PS, is a faction meter. Treasury, the sink that `compliance(s)` would throttle, is faction-owned. The settlement layer cannot produce felt pressure until something above it makes demands.

**territory-world owns the settlement's address.** `province_id` is an unvalidated free string with no referential check that it names a live territory — which is exactly how S-037 came to sit in a province the world does not contain. It also owns the adjacency graph the grain-route rule would trace and the Accord the province aggregate feeds.

**resolution-kernel is not connected at all.** The `settlements` package imports one module: its own ledger. No dice engine, no sigma leverage, no RNG. Every settlement outcome today is a threshold comparison. The verb menu's rolls (`Cognition + Wealth-history vs Ob ⌊Prosperity/2⌋+1` and its siblings) need that seam opened.

**economy-accounting** owes the granary/StockLevel field the Dearth chain requires and the settlement→faction Treasury contribution. **cross-scale-plumbing** owes `engine_clock`, which carries `doc: null` and blocks anything with latency — the Relay Tier, and the Directive's response window.

### The cheapest thing that would make this system playable

**Write the caller, not the mechanic.** The chassis is built; what is missing is a step in the season loop that touches it. Add a seventh step to `run_accounting` — `tick_settlements(world)` — composed almost entirely of functions that already exist and already work:

1. `ledger_sweep` every settlement's ledger on the season boundary (the function exists; it has never been called in a campaign).
2. Where `governor_id` is None, call `succeed_governor` with whatever placeholder the personnel layer can supply, so the appointment path is exercised rather than theoretical.
3. Load the authored per-settlement L/PS seed table in `populate_from_geography` — roughly ten lines against a table that already exists in canon — so the field starts non-zero and `q_s` is computable.
4. Resolve the Accord probe in one direction instead of measuring it: pick `province_accord` as the writer or pick `Territory.accord`, and make the loser derived.

That is on the order of forty lines, adds no new mechanic, and converts four inert primitives — ledger, `governor_id`, `succeed_governor`, `province_accord` — into live state. It also produces the first thing this layer has never had: a seeded campaign in which settlement state moves, which means the goldens move, which means the next change to it is observable. Step 4 is the one item that carries a design decision rather than a wiring decision; the other three are pure callers.

---

# §3 FLATTEN — "territory-world"

### Primitives

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| `Territory` (T1–T17) | primitive | tid, owner, accord, pt, garrison, prosperity, fort_level, templar, uncontrolled_since. Despite the name, this is what the ratified hierarchy calls a **Province** | BUILT | `engine/autoload/game_state.py:234-253` |
| `Territory.accord` (0.5–7.0 continuous) | primitive | Political alignment of a holding; bucketed through `ACCORD_MAP {0:1.0, 1:2.5, 2:4.0, 3:5.5, 4:7.0}` | BUILT — written by conquest, Govern, Mass Seizure, Parliamentary Transfer, Crown Initiative | `game_state.py:236,248` |
| `Territory.pt` (Piety Track) | primitive | The Church/Restoration axis; gates seizure Ob | BUILT | `game_state.py:237` |
| `prosperity` / `fort_level` / `garrison` / `templar` | primitive | Economic and military standing of a holding; `fort_level` is derived from `garrison` rather than authored, `templar` is true for T9 only | BUILT — seeded from `world_initial_state` tables, **not** from the geography file's own per-province `starting_pros` / `fort_level` | `game_state.py:315-327` |
| `uncontrolled_since` | primitive | The clock the insurgency trigger reads | BUILT | `game_state.py:242` |
| `world.territories` — 16 members (T1–T15, T17) | primitive | The playable map | BUILT, and **mismatched against the settlement registry's 16 provinces (T1–T14, T16, T17)**. T16 Schoenland hosts S-037 and is absent from the world; T15 Askeheim is in the world and canonically holds zero settlements. Because both counts are 16, no count-based check can see it | `engine/substrate/world_initial_state.py` |
| `ALL_PLAYABLE_15` | primitive | The victory denominator; excludes T15 and T16 | BUILT | `game_state.py:53` |
| `ADJACENCY` | primitive | The contiguity graph the insurgency BFS walks | BUILT and asymmetric: 16 keys (T1–T15, T17); T16 appears only as a value inside T1's neighbour set, so any walk that reaches it dead-ends | `systems/settlements/sim/adjacency.py:9-26` |
| geography `provinces:` block | primitive | 17 provinces with authored anchor, polygon, fort_level, spiritual_weight, proximity_calamity, starting_pros and settlement membership | Authored, **zero code readers** — the richest world data in the repo is dead at runtime | `valoria_geography_v30.yaml` |
| Territory temperament (α/β, five typologies + drift store) | primitive | An ethical-conduct axis per province, drifting under strain, aggregating population-weighted into faction temperament | INERT — `temperaments.py` has zero importers | `systems/settlements/sim/temperaments.py` |
| `world.clocks` | primitive | CI, MS, IP, PI, Strain, Turmoil | BUILT as a dict; CI and MS are driven every season. **IP, PI, Strain and Turmoil are initialised at world-gen and never written again** | `game_state.py:338` |
| Turmoil (Strain) 0–10 | primitive | The peninsula's political temperature; the third clause of the sole victory condition | INERT — one write at seed, one read at the victory gate | `game_state.py:338`, `victory.py:73` |
| IP (Institutional Pressure) 0–100 | primitive | Altonian imperial pressure, feeding the Phased Occupation era | INERT — both entry points are typed no-op stubs | `systems/overview/sim/ip_track.py:29-42` |
| `InsurgencyRecord` | primitive | A territory-holding, non-parliamentary body with its own Legitimacy and holdings | BUILT | `systems/world/sim/insurgency_pipeline.py` |
| Southernmost Awareness (SA) 0–7 | primitive | Institutional knowledge of the Southernmost substrate; gates a ladder of faction actions | DESIGNED — no field anywhere | `systems/world/southernmost_v30.md:47` |
| Warden Cooperation (WC) 0–3 | primitive | The world-survival contest's endgame lever, competing with sovereignty for the same action budget | DESIGNED — no field | `systems/overview/wc_survival_spine.md:22` |
| Franchise (per-territory 0–5) | primitive | Structural parliamentary weight independent of Prosperity or Order; would re-weight every Influence pool | PROPOSED — and would replace `faction.I` at ~15 live call sites with no migration path | `systems/factions/franchise_v30.md:18` |
| The ruled Territory tier | primitive | A genuine tier between Settlement and Province, holding multiple settlements | RULED-UNEXECUTED — zero representation in code | `scale_hierarchy_v1.md` §1 |
| Province as conditional aggregation | primitive | A province exists only while its constituent territories share a faction holder; it dissolves and re-forms rather than fracturing | RULED-UNEXECUTED — no key announces formation or dissolution | `scale_hierarchy_v1.md` §2 |
| Church infrastructure store | primitive | Keyed by `territory_id`, while canon specifies per settlement — silently coarsened to province grain | BUILT at the wrong grain | `infrastructure.py` |

### Derivatives and formulae

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| Peninsular Sovereignty (GD-1) | formula | `held ≥ 15 ∧ all(accord ≥ 2) ∧ Turmoil ≤ 6`, sustained 2 consecutive Accountings — the sole victory condition for every faction | BUILT, with the Turmoil clause structurally always-true | `engine/autoload/victory.py:52-80` |
| Fallback winner | formula | `score = held_count + Faction.L + len(Faction.territories)`, max wins when nobody achieves GD-1 by the season cap | BUILT, computed outside `victory.py` and undocumented in the module contracts | `engine/mc_v18.py` |
| `province_accord = floor(mean settlement Order)` | derivative | The settlement-grain Accord aggregate | BUILT, read-only | `registry.py:185` |
| `canonical_accord(continuous) → 0–4` | derivative | Converts the continuous field to the canonical index for like-for-like comparison | BUILT | `game_state.py` |
| Insurgency formation | formula | 2+ contiguous Uncontrolled territories, sustained 2 consecutive seasons | BUILT, runs every season | `insurgency_pipeline.py:139-196` |
| Insurgency promotion | formula | `L ≥ 3 ∧ territories ≥ 2 ∧ avg Accord ≥ 4`, sustained 2; PT < 3 gives an extra-parliamentary RM variant | BUILT and **unreachable** — `rec.L` is set once to 1.0 at formation and never written again | `insurgency_pipeline.py:199-255` |
| Turmoil accrual/decay | formula | +1 per held territory at Accord ≤ 1 (cap +3/season), +2 per faction elimination, +1 per revolt; −1 quiet season, −1 per active treaty pair (cap −2), −1 per public diplomatic resolution | DESIGNED — zero writers | `peninsular_strain_v30.md:286` |
| Accord ladder effects | formula | 3 = full Prosperity + defender die; 2 = full Prosperity; 1 = zero Prosperity contribution + Govern Ob +1 + garrison requirement; 0 = Uncontrolled at next Accounting | DESIGNED — the accounting cascade has no such step | `peninsular_strain_v30.md:47` |
| Turmoil threshold ladder | formula | 3–4 Legitimacy −25 all factions; 5–6 Accord −1 in one territory; 7–8 Accord −1 all non-capitals + Mandate check; 9–10 Accord capped at 2 and MS −1/season | DESIGNED | `peninsular_strain_v30.md` |
| March budget | formula | `Military×100 × 1.5 (cavalry majority) × 1.3 (skirmish-only)`, stacking capped at 1.7× | DESIGNED | `march_layer_v30.md:15` |
| Effective vision | formula | `240px × terrain × weather × season` | DESIGNED | `march_layer_v30.md:64` |
| Territory-scale ranges (0–4, balanced at 2) | formula | Accord, Piety, Prosperity, Fort Level all on 0–4 — never cross-referenced against the settlement scale's 0–5 stats and 0–7 acceptance | DESIGNED, collision open | `canonical_registry.md:58` |
| Fractional province PV share | formula | `share_s = (P_s / ΣP) × base_PV`, re-aggregated per faction at Accounting | PROPOSED — `Territory.owner` is a single `str \| None`, so partial control cannot be expressed | `fractional_province_ownership_v30.md:36` |

### Mechanics

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| Faction writes to `Territory.accord` | mechanic | Conquest, Govern, Mass Seizure, Parliamentary Transfer and Crown Initiative each move Accord directly, bypassing settlement Order | BUILT — this is the live Accord model | `faction_action.py:513,524,577`, `mass_seizure.py:296`, `parliamentary_transfer.py:346` |
| Province-Accord drift probe | mechanic | Measures divergence between the two Accord models per season and records a counter; never writes either | BUILT, report-only — the only thing connecting the two models | `accounting.py:54-93` |
| Accord Domain Echo Key | mechanic | Wired end-to-end — built, emitted, routed through the deferred-apply scheduler, subscribed | BUILT and never fires: no live producer sets `echo['scene_outcome']` | `engine/cross_scale/echo_transport.py` |
| RM PT decay / Latent RM emergence (GD-3 Stages 1–2) | mechanic | The background pressure that would seed insurgencies in the first place | Stub — both entry points are typed no-ops | `systems/world/sim/restoration_movement.py:30-43` |
| Miraculous Event | mechanic | A high-Ob Mending near T15 grants SA +1 to every present faction, +1 Accord, and a Proximity modifier | Stub — zero production callers | `systems/world/sim/miraculous_event.py:28` |
| Insurgency / Promoted-Faction dissolution (4 paths) | mechanic | Military defeat, sponsor withdrawal, amnesty, or persist — ratified ED-881 | RULED-UNEXECUTED — no dissolution function of any kind exists; an InsurgencyRecord, once created, is permanent | `insurgency_pipeline_v30.md:229` |
| Territorial Occupation | mechanic | A distinct state from control: 3-season transfer window, per-season costs to both sides, a free Resistance Check | DESIGNED — conquest transfers ownership immediately, skipping the phase entirely | `faction_layer_v30.md:234` |
| Independence / cross-scale claiming | mechanic | Any settlement, territory or province can break from its holder; a settlement can be claimed directly by a faction of a different scale, skipping tiers | RULED-UNEXECUTED | `scale_hierarchy_v1.md` §5.2 |
| The governance-type cascade | mechanic | Each tier's authority sets the type of the tier below, bidirectionally and noisily, gated by L/PS consent | RULED-UNEXECUTED | `scale_hierarchy_v1.md` §3–§4 |
| The two bypassing authorities | mechanic | The monarch reaches any tier regardless of ownership nesting; Parliament holds no chain position but can forcibly act on any province, territory or settlement | RULED-UNEXECUTED | `scale_hierarchy_v1.md` §5.3 |
| Relay Tier / Beacon Network | mechanic | Tiered propagation between settlements — a neighbour's alarm shortens your reaction — named the strongest new-state case in the corpus | PROPOSED, blocked on `engine_clock` (`doc: null`) | `proactive_governance_scale_research_v1.md:243` |
| Territory Reach-Cap | mechanic | A settlement-count or AP-load threshold past which the governor cannot reach everyone, removing the option to decline a Partition without compounding decay | PROPOSED — the one place a bare number is unavoidable | `proactive_governance_scale_research_v1.md:251` |
| Cordon-Complete | mechanic | A chain bonus that pays only while the chain is geographically unbroken; one member falling drops it for the whole territory | PROPOSED | `proactive_governance_scale_research_v1.md:247` |
| Grant Ledger / Muster tag / Reserve Pool | mechanic | Third-party revenue rights over a settlement bundle; land-tenure-for-defence with no upkeep; a surplus buffer that moves *between* settlements | PROPOSED — all three are Territory-scale objects with no home | `proactive_governance_scale_research_v1.md:244-246` |

### Processes

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| `create_world` | process | Builds factions, territories and settlements in one call — **two settlement-scale entity families from two different sources**, cross-validated by nothing but the report-only probe | BUILT | `game_state.py:304-350` |
| GD-3 Revolt → Insurgency → Faction pipeline | process | Neglect spawns insurgencies that can hold territory, invade the faction whose neglect spawned them, and win the game | Stages 3–4 BUILT and running every season; Stages 1–2 stub; promotion unreachable; dissolution absent | `insurgency_pipeline.py`, called from `accounting.py:124-133` |
| World-state eras | process | Post-Calamity (MS=0), Occupation (IP ≥ 100), Anarchy (all factions collapsed), and Second Calamity — the only true campaign terminal | DESIGNED — four contract-declared gates, zero code, and the era-name strings appear in no `.py` file | `peninsular_strain_v30.md:461`, `module_contracts.yaml` |

---

# §4 WITHIN-SYSTEM ANALYSIS — "territory-world"

### What playing this system is actually like right now

This is the one layer that genuinely runs, and it plays like a war of pure territorial arithmetic.

Factions take domain actions; those actions write `Territory.accord` and flip `owner`. Every season `run_accounting` moves CI, moves MS at year-end, checks whether two or more contiguous territories have sat Uncontrolled for two seasons — and if so, forms an insurgency — then checks every open insurgency for promotion, drifts NPC stances, and records the Accord drift counter. At the season cap, either someone holds 15 of 15 playable territories at Accord ≥ 2 for two consecutive Accountings, or a fallback score of held count plus Legitimacy plus territory count picks a winner.

What the player would feel is a map that changes hands and a peninsula that never gets hotter. Turmoil — the political-stability clause of the only win condition — is set to 0.0 at world creation and read once by the victory check; nothing in the tree writes it, so `ps_ok` is unconditionally true for the life of every campaign. The same is true of IP, PI and Strain. The peninsula has four pressure gauges and all four are painted on.

The insurgency pipeline is the sharpest version of this system's pathology, because it is *correct*. It forms insurgencies from real contiguity data, walking the real adjacency graph, and it iterates every open insurgency every season looking for promotion. But promotion requires Legitimacy ≥ 3, and `InsurgencyRecord.L` is assigned 1.0 at formation and never written again anywhere. So a rebellion can start, hold ground, and persist forever — it can never become a faction, and no code path can ever dissolve it either. The game's only mechanism for producing new political agents is a closed loop with the exit welded shut.

### The load-bearing conflicts

**1. The map has two rosters and they are not the same 16.** `world.territories` holds T1–T15 and T17; the settlement registry's provinces are T1–T14, T16 and T17. T16 Schoenland hosts S-037, carries an authored coastal edge to T1, and does not exist in the world — while `adjacency.py` names it only as a value in T1's neighbour set, never as its own key. T15 Askeheim is the inverse and is *not* a defect: canon says Askeheim is unincorporated Calamity wilderness with zero settlements. So this is one real hole, not a symmetric pair. *What decides it:* the code, and it is a one-identifier fix — but fourteen sites index `world.territories[...]` directly and would raise on the S-037 province id, so the fix has to land with them.

**2. Two uncoordinated Accord write models.** `registry.province_accord` derives Accord from the floor-mean of settlement Order; `Territory.accord` is a continuous field written directly by five faction actions that never look at a settlement. Both are live. The only thing linking them is a probe that counts the divergence and resolves nothing. *What decides it:* Jordan, or whoever rules OI-37 — because it is a real design fork, not a bug. If settlement Order is the source of provincial Accord, then settlements govern the map; if faction actions are, then the settlement layer is decorative even after it is wired.

**3. "Territory" names two different tiers.** The 2026-07-13 ruling establishes Settlement → Territory → Province → Duchy → Country, with Territory as a new intermediate tier holding several settlements, and provinces as conditional aggregations that exist only while their territories share a holder. The code's `Territory` (T1–T17) is what that ruling calls a Province. The ruled Territory tier has no representation anywhere. *What decides it:* already ruled — this is propagation work the ruling's own §6 enumerates, not an open question.

**4. Turmoil, and the victory condition it gates.** GD-1 has three clauses and one of them is inert, which means the sole win condition is materially "hold 15 at Accord ≥ 2." *What decides it:* the code. The accrual model is fully specified and every one of its inputs — per-territory Accord, faction elimination, revolt — is already live state.

### What this system needs from others

**settlement-governance owes it Order, and owes it membership integrity.** `province_accord` reads settlement Order, so the entire settlement-derived half of the Accord model is downstream of a layer that never ticks. And `Settlement.province_id` is an unvalidated free string with no referential check against the live territory set — the exact absence that let S-037 name a province the world does not contain, while the settlement-type field on the same record *does* raise on an illegal value.

**faction-strategy owns every writer this system has.** Accord, ownership, garrison and elimination all move through faction actions. Turmoil's accrual reads faction elimination; the fallback winner formula reads `Faction.L`. Whatever the faction layer does not do, the map does not feel.

**personnel-roster owes the cascade its officers.** The governance-type cascade requires an authority at each tier that sets the tier below, and the ruling's worked example is explicit: the King appoints provincial governors who vet settlement councils. There is no territory-scale governor concept in code or in PP-726, and no AP aggregation across a multi-settlement holding.

**cross-scale-plumbing owes it Keys and a clock.** No key type announces province formation or dissolution, a territory-scale Accord-0 revolt, or a governor change, so victory scoring and franchise recalculation silently re-derive the world's shape every Accounting with no record it changed. `engine_clock` is unauthored and blocks every cross-settlement latency mechanic.

**mass-battle-seam owns the violent transfer path** — siege and assault — while the non-violent Mandate Challenge is a forward reference that names a procedure nobody has written.

### The cheapest thing that would make this system playable

**Give `InsurgencyRecord.L` a writer.** One accrual rule in `insurgency_pipeline.py` — Legitimacy rises while the insurgency holds ground at acceptable Accord, and falls when it loses territory or its sponsor — and the entire GD-3 pipeline comes alive. Nothing else changes: formation already fires from real contiguity, promotion already runs every season for every open record, the parliamentary/extra-parliamentary branch on average PT already works, and a promoted faction is already eligible to win. The mechanism is built, wired, and called; it is missing exactly one number's second writer.

This is worth more than the alternatives at the same price. Wiring Turmoil (comparably cheap, all inputs live) restores a clause to the victory check, which makes an existing outcome harder — valuable, but subtractive. Fixing T16 removes a latent crash. The insurgency writer is the only cheap change that *adds an agent to the world*: neglected ground starts producing rebellions that grow into factions that can invade the power whose neglect made them, which is the one place this design already says the world should generate its own opposition rather than waiting for a player.

It is a writer, not a mechanic — the same shape as the settlement layer's fix, and for the same reason. This corpus's characteristic failure is not missing design. It is finished machinery with no hand on the key.