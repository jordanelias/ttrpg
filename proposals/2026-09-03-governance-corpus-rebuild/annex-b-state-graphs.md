# Annex B — Per-set state graphs, the unified graph, and the executable model

> The corpus rebuilt as an executable model: twelve sets, each with a state-graph diagram, typed
> primitives with a named owner and a single writer, derivatives written as expressions, and
> pipelines written as state machines with machine-evaluable predicates — followed by the unified
> tick, the scale-composition rules, the conservation properties, and the full code shape (core
> types, ownership, the resolution kernel, pipelines-as-data, cross-scale propagation, the
> data/code boundary, determinism and replay, and worked examples).
>
> The reconciliation decisions of Part III are adopted throughout without comment.
> **◆ marks a decision the corpus did not make** — where it was silent or non-evaluable, the value
> or rule given is this design's choice.
>
> §3.3 is the shortest useful summary of the whole exercise: twenty-two places where the corpus's
> graphs were fighting, and the single resolution taken for each.

---

# C — Valoria: the governance design that is trying to exist

**What this is.** The 33 governance documents, read as one design, unified where they repeat, decided where they are silent, and stated as an executable model for a videogame with no GM. Reconciliation decisions from `RECONCILIATIONS.md` are adopted without comment (province/settlement, `PT`, `Nordhelm`, `Askeheim`, `Valorsplatz`, Standing 0–7, Prosperity 0–6, CI 0–100 no freeze, 11-of-15 victory with fractional shares, 37 settlements / 56 edges, `Community Organizing` ≠ `Thread Weaving`, deterministic trigger order, batch-to-Accounting, one shared loss, rebased MS bands, every referee call becomes a rule).

**Notation.** `SET-nn` sets · `P-nn.mm` primitives · `D-nn.mm` derivatives · `PL-nn.mm` pipelines · `T-nn` types · `PH-nn` tick phases. Corpus lineage is cited as `filename › heading`. **◆** marks a decision the corpus did not make; the corpus is silent or non-evaluable there and the value or rule is this design's choice. Where a mechanic was stated several ways, the one kept is named and the reason given in a clause.

**The design in one paragraph.** Valoria is three nested scales — settlement, province, peninsula — with control composing upward as pure derivation and pressure propagating downward as queued effects. Every stored quantity has one owner and one write path (an `Effect` applied at commit). Every contested outcome, at every scale, is decided by one kernel that turns *strength − difficulty* into one of four degrees. Every action, at every scale and for every kind of actor (faction, governor, player, NPC), is a row in one table. Every multi-season process is a state machine stored as data and advanced at one phase of one tick. Every consequence crosses scales as a typed event that nobody addresses to anybody: subscribers are rules, not modules. The peninsula is the consequence layer, the province is the contest layer, the settlement is the engine layer — and a season is what the engine does, in order, once.

---

## 1. The sets, rebuilt

Twelve sets. Membership is by what a document *specifies*, so a document belongs wherever it states a rule of that set. Each set names what it owns (the stored state nobody else may write), what it is the single authority for (the rules nobody else may restate), and which documents contribute. The **flattened content** paragraph is the set after duplication is collapsed and the reconciled decisions applied.

| Set | Name | Owns (state) | Sole authority for (rules) | Contributing documents |
|---|---|---|---|---|
| SET-01 | Resolution Kernel & Action Schema | nothing durable (RNG draws, per-action instances) | how any check resolves; the degree ladder; the action table; card/AP/scene budgets; seasonal caps | `stats_1_7_scale`, `core`, `strategic_layer`, `ci_political §4–5`, `parliament`, `faction_behavior §3.7`, `governance_play_redesign §1` |
| SET-02 | Calendar & Tick | season, arc, phase, effect queue, RNG streams, derived snapshot | phase order; commit; batching; determinism; save/replay | `phases`, `clocks` (cap), `strategic_layer` (P-18, §9), `treaty_expiration §1`, `insurgency_pipeline §5.1`, `player_agency §7.2`, `conflict_architecture`, `governance_play_redesign §4` |
| SET-03 | Map & Movement | province/settlement registries (fixed), adjacency, units, march state, sieges, fog | geography; proximity; SW; temperament; movement; battle at settlements | `geography`, `settlement_adjacency`, `march_layer`, `valoria_political_hierarchy`, `settlement_layer PART 2, §5`, `territory_temperaments`, `clocks` (Proximity, Vanguard route), `southernmost` (zones) |
| SET-04 | Settlement Governance | every per-settlement stat, governor, presence, pressure, ledger, needs, local actors, NPC ambitions | governance verbs; directives; the pressure homeostat; the settlement deck; dual authority; subnational management; settlement phenomena | `settlement_layer`, `governance_play_redesign`, `conflict_architecture`, `campaign_architecture Part 1`, `faction_behavior` (LPS relocation), `player_agency §9` |
| SET-05 | Province Control & Legitimacy | fractional/stabilisation/vacuum state, attention pool, thread debt, trade route, temperament drift | who controls a province; Accord; PV shares; fragmentation; consolidation; secession; L/PS → Mandate; Prominence | `fractional_province_ownership`, `valoria_political_hierarchy §2.3–2.4`, `tracks` (Accord), `core` (Accord, vacuum), `phases 4c`, `settlement_layer §1.3, §1.8, §5.1`, `settlement_adjacency §2.3`, `geography` (starting control) |
| SET-06 | Polities (Factions & Institutions) | faction stats, hand, cooldown, mission, cascade, offices, status, private tracks | what a polity is; its stat economy; its AI posture; Mission/Cascade/Expectation; emergence and collapse to city-state; institutions as polities | `faction_behavior`, `stats_1_7_scale`, `core` (stats, hands), `ci_political §4, §6`, `ministry`, `institutions`, `settlement_layer §6.2–6.3`, `territory_temperaments`, `strategic_layer` (P-20, P-24, fog bands) |
| SET-07 | Peninsula Clocks & Environment | MS, CI, IP, PI, Turmoil, WC, WR, Loyalties, Generational Shift, invasion phase, expedition state | clock ranges/bands/advancement; radiation; Vanguard/invasion; Southernmost access | `clocks`, `core` (Starting Values), `tracks` (Turmoil), `parliament` (PI), `campaign_architecture Parts 3–5`, `southernmost`, `geography` (Proximity, Expedition, WR), `settlement_layer §7.1`, `ci_seizure`, `stats_1_7_scale` (Public Instability) |
| SET-08 | Church & Piety | PT (per settlement), Church infrastructure axes, RDT/TD, Cardinal offices | CI generation; seizure; bishop appointment; Attention/Inquisitors; excommunication; parish/cathedral | `ci_seizure`, `ci_political §1–3`, `campaign_architecture Part 1`, `tracks` (PT, RDT/TD, Attention), `institutions` (Cardinals, Parish), `settlement_layer §1.5–1.7`, `conflict_architecture` (Bishop Appointment), `geography` (SW), `faction_politics Part 5`, `stats_1_7_scale` (Unique Actions) |
| SET-09 | Diplomacy & Parliament | regard ledger, casus belli ledger, treaties, pledges, policy state | treaties and lapse; pledges; CB economy; parliamentary vote/transfer/manoeuvre; Crown policy; deposition; Ministry mechanics | `treaty_expiration`, `parliamentary_transfer`, `parliament`, `ministry`, `institutions` (Nomination, Deposition), `worldbuilding §6.2`, `march_layer §5.4`, `core` (treaty Ob), `ci_political §3` |
| SET-10 | Succession, Split & Emergence | pipeline instances: autonomy, succession contests, insurgencies, emergence stages, claims | leader loss; contests; splits; Löwenritter autonomy; insurgency pipeline; RM stages; Baralta claim and Consecration; collapse | `faction_succession_split`, `baralta_crown_claim`, `insurgency_pipeline`, `conflict_architecture` (Graduated Autonomy), `core` (Autonomy, Elimination), `institutions` (Reconstitution, Deposition), `settlement_layer §6.2–6.3`, `campaign_architecture Parts 2, 6`, `faction_politics Parts 6, 8`, `stats_1_7_scale` (Coup) |
| SET-11 | Personal Agency & Rank | PC record: convictions, duties, standing per faction, renown, shadow renown, resources, budget; rank offices; lineage | why the player acts; scene slate; duties; rank ladders; caste; renown; generational transition | `player_agency`, `faction_politics Parts 1–3, 9`, `generational_transition`, `campaign_architecture Part 7`, `settlement_layer §3.2, §6.1, §7.2`, `governance_play_redesign Part 1`, `strategic_layer §9.9–9.14` |
| SET-12 | Campaign Arc & Decks | drawn Tensions card, assassination fuse, revelation state, named-character card state, event decks | setup; fuses; all decks (settlement, peninsula, tensions, named-character); revelation triggers; Warden paths | `conflict_architecture`, `early_game_ignition` (superseded precedent), `phases` (Setup), `campaign_architecture Parts 4, 6`, `worldbuilding` (cards), `governance_play_redesign Part 2` (card schema), `strategic_layer` (scenarios) |

### SET-01 — Resolution Kernel & Action Schema

**Flattened.** There is one way to decide a contested thing. An action names an actor strength and a difficulty; the kernel computes margin `M = strength − difficulty` and maps it through the ratified deterministic+stochastic ladder (`stats_1_7_scale › Domain Action Resolution`: `P_success = clamp(0.50 + 0.10·M, 0.05, 0.90)`, Overwhelming at `−0.35`, Partial at `+0.20`), emitting one of Failure / Partial / Success / Overwhelming. Personal-scale scenes (combat, social contest, fieldwork) keep the d10 pool — `1 → −1, 7–9 → +1, 10 → +2`, TN 7, Ob floor 1, degree by PP-179 (`≥ 2×Ob and ≥ 3` Overwhelming; the Ob+1 table in `strategic_layer › CORRECTION 3` is the superseded form and is dropped; the majority-1s catastrophic failure is struck) — but the pool evaluator is the *same kernel in a second mode*, and every modifier in the game is expressed in one unit, the **advantage point**: `+1 point = +1 die (pool mode) = +1 M (margin mode)`, and an Ob shift of ±1 is ∓2 points (the corpus's own legacy mapping `D = max(1, (O−1)·2)`). ◆ That unit is the design's choice; it is what lets bonus dice, Fort dice, coalition dice, Domain Expertise and CI weight all live in one table. Every action — the ~30 faction Domain Actions of `core › Standard Action Ob Reference`, the Unique Actions, the eight governance verbs of `governance_play_redesign §1.3`, the personal fieldwork actions, and the automatic checks that pipelines fire (Fragmentation Check, Stability Check, Forgetting Check) — is one row of one `ActionDef` table: who may act, what it costs (a card, AP, a scene action, or nothing), which stat is the strength, how difficulty is formed (fixed, target's stat, or an expression), whether it is contested, its prerequisites as predicates, and its effects per degree. Budgets are one concept with three instances: cards with cooldown (`ci_political §5.3`), Administration Points `AP = 2 + FacilityTier` (◆ `+1` at Standing ≥ 5, so Standing 6–7 governors are covered), and scene actions by difficulty. Seasonal caps live in the state schema, not in the actions: faction stats `±2/season` net at commit, CI `±5` (`±3` from actions), PI `+2` up, settlement stats `±1` per source class. A Failure on a faction Domain Action costs Stability −1 (PP-403) with its exclusions. The triadic identity modifier `clamp(mission + cascade + expectation, −2, +2)` (`faction_behavior §3.7`) is a modifier row like any other; the struck per-faction "ethical framework" tables that `faction_politics` still quotes are gone.

### SET-02 — Calendar & Tick

**Flattened.** A season is one tick of twelve phases (§3.1). The corpus's four phase schemes — the board game's Phases 1–5, the player-agency `1a/1b/1c/2/3`, the hybrid `Personal → Strategic → Cascade`, and the governance proposal's two-stroke loop — are one sequence: world stroke, orders, personal, settlement, province, commit, derive, peninsula, pipelines, settle, check. The three-scale order (`phases › Three-Scale Resolution Model`: Settlement → Province → Peninsula) is the spine; the Phase 4 priority tiers (Intel → Military → Domain → Social → Thread → Unique → Project, descending Stability within tier, alphabetical for three-way ties, adversarial pairs simultaneous) order actions *inside* the province phase. All action effects batch to a single commit at the head of Accounting; the only immediate writes are read-backs inside a resolution (a battle's casualties before the next battle in the same province). The Cascade Depth Cap of `clocks.md` is retired — its purpose (no runaway chains inside a resolution step) is served structurally, because effects do not fire effects until the next phase; queued effects are applied in `(scale, phase, stable key)` order. Four seasons make a year and an arc (the corpus's "arc" and "year-arc" are the same unit); Year-End and arc-boundary work are one sub-phase. Sustained-N conditions are counters that the tick increments only on consecutive true Accountings. The tick is deterministic: one seeded stream per `(season, phase, subject)`, AI choices are functions of state, player inputs are logged, and replaying the log from the seed reproduces every hash.

### SET-03 — Map & Movement

**Flattened.** The map is 17 nodes (14 duchy provinces + Himmelenger + Askeheim + Schoenland) over 37 settlements joined by 56 edges (`settlement_layer §2.1` registry; edges derived by the hub-and-spoke rule of `settlement_adjacency §1.2` — hub is the Seat or the highest-type settlement, one hub-to-hub edge per province adjacency, eight hand-specified overrides, four Thread-Witnessed edges that carry no armies). Each province carries fixed attributes: duchy, seat, Fort level, Proximity Rating (graph distance from Askeheim), Spiritual Weight (total 32), public temperament (α/β), base PV (the reconciled 15-territory denominator: T15 uncontrollable, T16 foreign). Each settlement carries a type from `{Seat, City, Town, Village, Fortress, Port, Cathedral, Mine, Outpost}` and authored coordinates (◆ needed for the Greater/Lesser naming of fractional provinces and supplied as registry data). Armies are units at settlements; a unit moves `max(1, ⌊Military/2⌋)` edges per season, `+1` if cavalry-majority (◆ the pixel budget of `march_layer §1` is replaced by edge counts because the terrain matrix it needs is not in the corpus; the multipliers survive as edge bonuses), pays edge type costs (road 1, river 1, pass 2, gate 2, coastal 1 from a Port only), and stops when budget is spent or engagement is forced (hostile unit on the node). Entering a province a hostile faction controls without treaty grants that faction a Casus Belli and Regard −1 (◆ the corpus's "IP −2 to the trespasser" is dropped — IP is one global clock). At a hostile settlement the army declares Assault, Siege or Bypass (`settlement_layer §5.1`): Assault is a contested kernel check with edge and settlement-type modifiers; Siege is a per-season `Order −1` until 0; Bypass needs `Military > Defense + 2` and Fortresses need `+3`. A unit beyond 4 edges of a friendly supply node (Seat/Fortress/Port/Mine) accrues attrition: Discipline −1 at Accounting. Fog of war is a display rule over vision (2 hops for scouting); it never changes state.

### SET-04 — Settlement Governance

**Flattened.** The settlement is where power is built. It holds nine stored stats — Prosperity 0–6, Defense 0–5, Order 0–5, Legitimacy 0–7, Popular Support 0–7, Piety 0–5, Facility Tier 0–3, Pressure Π 0–10, Suspicion 0–5 — plus a controller, a governor slot, a Church building tier, two Church binaries (Templar, Inquisitor), a `Presence[institution]` 0–3 for each subnational institution (RM, Guilds, Ministry, Löwenritter, Wardens — one primitive replacing Presence markers, CP-tokens, AP-tokens, Guild Favour and Church Favour), a Ledger of tags (Precedent, Grudge, Debt, Reputation), open Needs, and 0–2 Local Actor NPCs. Two authorities act on it (`settlement_layer §3.1`): the Provincial Authority (the polity holding the province's Seat) issues one Directive a season and may govern directly with a Consul card when the settlement has no governor; the Governor answers the Directive (Comply / Bargain / Defy) and spends AP on eight verbs (`governance_play_redesign §1.3`) each of which forces a *method* that hands power to some institution — Develop by Treasury/Guild charter/Corvée, Keep Order by Consent/Force/Clergy, Fortify by Garrison/Militia/Walls. The faction-level Govern/Trade/Fortify of `core` and the governor's Keep Order/Develop/Fortify are the same action rows with different actor kinds; NPC governors run the priority `Order ≥ 2 → Prosperity → Defense if threatened`. The settlement is also the world's move-generator: Π is a homeostat (◆ with units: Needs weigh 1–3 by type, Grudges 1, ambitions-in-motion 1 each, external shock is the sum of peninsula effects that touched the settlement, releases are authored per card response and per served Need, and Π decays 1 when no Need is open), drawing `1 + ⌊Π/3⌋` cards from a state-filtered deck; NPCs carry ambitions that advance one step per season and emit a card when they mature. Phenomena are derivations, not entities: a black market exists iff `Order ≤ 1 ∨ governor = ∅`; a Thread exploitation site iff `Proximity ≤ 2`; a broker is a Local Actor role assigned iff `Prosperity ≥ 3 ∧ (governor = ∅ ∨ controller.Stability ≤ 2)`. Church buildings raise Order (Parish Social Services — the Geneva trap) and Piety, and make a bishop-governor appointable. Legitimacy and Popular Support are per settlement (`settlement_layer §1.8`, Jordan-ruled) and are the *only* home of faction legitimacy; the faction's Mandate is derived from them.

### SET-05 — Province Control & Legitimacy

**Flattened.** A province is mostly a view. Its controller is whoever controls its Seat settlement; its Accord is `⌊mean(Order)⌋` over members (Seat weighted double on ties — ED-SETT-03), on the 0–3 Accord ladder (`tracks › Accord`: 3 Aligned, 2 Compliant, 1 Resistant with garrison requirement, 0 Revolt → Uncontrolled); its Prosperity is the sum of members'; its Piety is `⌊mean(PT_s)⌋`; its PV is split among controllers of its settlements in proportion to settlement Prosperity (`fractional_province_ownership §2.2`, with the zero-denominator guard). A province is *fractional* iff some member's controller ≠ the Seat's controller; a fractional province rolls a Fragmentation Check each Accounting (Seat-holder Influence vs `2 + count(alien settlements)`) whose Failure lets an alien national controller secede the settlement into an independent holding, and a faction holding ≥ 75% of PV may declare Consolidation (Influence vs `⌈2 × alien share⌉`; each alien controller submits or resists, ◆ AI resists iff `Defense + garrison ≥ 2`). This is the fracturing model kept; `valoria_political_hierarchy §2.3–2.4`'s northern/southern sub-provinces and unification-bonus scalar fold into it — the "bonus" of full control is that only the Seat-holder may issue province-scope actions. Faction Mandate is `clamp(round(7·T/(T+6)))` with `T = Σ W_s·q_s/7`, `W_s = base(type) + Prosperity + FacilityTier`, `q_s = ½L + ½PS` (`settlement_layer §1.8`); held settlements drift toward Mandate each Accounting (L +1 if `q_s ≤ Mandate − 1`, PS −1 if `q_s ≥ Mandate + 1`). Church Prominence in a province is `Church.Mandate > controller.Mandate`, recomputed every derive phase and read as the last snapshot. A province whose faction is eliminated enters Vacuum for one season (no entry, Fort retained) and then Uncontrolled; Uncontrolled provinces are free entry and are the substrate insurgencies form on.

### SET-06 — Polities (Factions & Institutions)

**Flattened.** Everything that owns settlements, plays cards, holds stats or is talked to by diplomacy is one type, `Polity`, with a `status` that gates capability: `national` (Crown, Church, Hafenmark, Varfell; Löwenritter after Split; promoted insurgencies), `institution` (Ministry, Guilds, Löwenritter pre-Split, Wardens), `movement` (Restoration Movement — it has a partial sheet from season 1, Military 0; "statless" was a rule about capability, not about missing numbers), `insurgency`, `city-state`, `foreign` (Schoenland, the Altonian Governorate). Five stored stats (Influence, Wealth, Military, Intel, Stability — 0–7, Influence floor 1) and one derived headline (Mandate). Behaviour is Mission × Cascade × Public Expectation × Legitimacy (`faction_behavior`): a Mission with aligned/contradicted action categories; a cascade of NPC Convictions down a supervisor graph with `α = clamp(0.4 + seniority + institution)` and drift 0.6; a role template of expected Convictions; strictness from aggregate L/PS. ◆ The undefined functions are defined: outcome attribution is the mean of this season's degree scores `{OW +1, S +½, P 0, F −1}` signed by Mission alignment; cascade alignment of an action is the cosine of its authored 13-vector profile with the faction aggregate, thresholded at ±0.3; expectation deviation is `round(2·(1 − fidelity))`; the shock is a seeded triangular draw scaled 0.5 that fires only when a card targeted the faction. NPC polities choose actions by a data-driven posture stack (`ci_political §6`: Existential → Defend → Consolidate → Counter-threat → Expand → Opportunistic) evaluated identically for every polity. Emergence and collapse are statuses in a pipeline: a movement with 2+ settlements is an *organisation*, 4+ across 2 provinces or one Seat is *national*; a national polity that loses its last province with a living leader in a settlement it controls becomes a *city-state* (`settlement_layer §6.3`) with the same sheet and fewer capabilities; Stability 0 at Accounting is elimination.

### SET-07 — Peninsula Clocks & Environment

**Flattened.** Seven peninsula clocks and four relationship tracks, all with evaluable advancement. **MS** 0–100 (start 72): −1 per battle, −1 at Year-End, −1 per aged Thread Debt token, +Mending (Mender tiers by Spirit), halved decay at WC ≥ 2, +2/season at WC 3; 0 is Rupture, the only shared loss; visibility bands rebased to the reachable range (100–73 Restored, 72–60 Quiet Anomalies, 59–40 Observable, 39–20 Peninsula-wide, 19–1 Undeniable); the MS × Proximity radiation table (`clocks.md`) applies per province with the same rebasing. **CI** 0–100 (start 28): the seven-step seasonal procedure of `ci_seizure` with Piety Yield made real (◆ tier `{0:0, 1:0, 2:0.1, 3:0.25, 4:0.5, 5:1.0}` × `SW/5`, summed then floored with a carried fraction), caps ±5/±3, milestones at 40/55/65/80/100. **IP** 0–100 (start 20): ◆ +1 per three provinces at Accord ≤ 1, +2 while Crown Stability ≤ 2, +1 while Torben Loyalty ≤ 3, +1 per season an occupied province exists, −1 when no province is at Accord ≤ 1 and IP > 20; Vanguard at 75, three invasion phases at 100/85/80 with retreats and the three repulsion paths (`campaign_architecture Part 5`). **PI** 0–20 (start 7): bands ◆ completed (≤2 Non-functional · 3–4 Degraded · 5–7 Standard · 8–10 Full · 11–14 Ascendant · 15–19 Supreme · 20 Deposition), +2/season cap, Ministry stabilisation. **Turmoil** 0–10 (start 0) absorbs Public Instability: +1 per season with battle, +2 per elimination, +1 per Revolt, −1 per all-Accord-≥2 season, −1 per diplomatic resolution; bands Peace/Tension/Fracture/Crisis/Collapse with their stat effects. **WC** 0–3 and **WR** 0–4 (Warden relations, Varfell-private WR gating peninsula WC), **Torben** and **Elske Loyalty** 0–7, **Generational Shift** 0–10 (+1 per 5 years). The Southernmost is an expedition pipeline (stage in Stillhelm, Forgetting Check on entry, Edeyja contact), an Awareness stat per polity, and one Ritual (◆ named *the Closing*); Thread Tension is not a second clock — ◆ `TT ≡ 100 − MS`.

### SET-08 — Church & Piety

**Flattened.** Piety (PT, 0–5, the reconciled name) is per settlement; province Piety is its floor-mean; Spiritual Weight is a fixed province attribute. The Church accumulates CI through Prominence, Piety Yield, charity, Templar presence, Assert and Hafenmark's structural suppression, and builds presence in settlements on four independent axes (`campaign_architecture §1.1`: Building None/Chapel/Church/Cathedral; Templar; Inquisitor; Governor), each of which lowers the province's seizure difficulty (per-settlement cap −4, province cap −6) and raises Piety and Order (Parish Social Services). The Church's second expansion path is administrative: Ecclesiastical Appointment (Influence vs 1) installs a bishop-governor where a Church-or-better building exists and the governor is absent or friendly, transferring the settlement's control to the Church with no Casus Belli — the province fractionalises and the ordinary machinery does the rest. The nuclear path is Mass Seizure: one-shot, available at CI ≥ 60, AI-declared with `P = ((CI−60)/40)^3.3`, targeting every province with a Church building, each resolved through the kernel with strength `Influence + ⌊CI/15⌋` against difficulty from `Ob = 10 − PT − infra`, garrisoned provinces requiring a battle first, every attempt granting Casus Belli, seized provinces starting at Accord 1 (2 if PT ≥ 3). Per-province Church Attention 0–10 resets each Accounting; ≥3 places one Inquisitor, ≥6 a second; Heresy Investigation is an action row against an NPC or polity in a province with Attention ≥ 3. Cardinals are four NPC offices with Competence/Corruption; Cardinal death suspends the arm until Year-End; schism at Stability < 3 selects ◆ the Cardinal whose Dicastery Competence is lowest. Excommunication is a contested check that strips Circles and costs −1 L in every target settlement; RDT/TD are Hafenmark's two private 0–5 tracks driven by the Reformed Settlement action (◆ a Diplomat-card row with the prerequisites `tracks.md` lists).

### SET-09 — Diplomacy & Parliament

**Flattened.** Relations are ledgers, all world-owned. **Regard** is a directed −3..+3 value per ordered polity pair (◆ one primitive replacing "Standing tokens", the treaty-violation "Standing −2", and Warden's Accord as `regard[Varfell][RM]`). **Casus Belli** entries are `(holder, target, source, mode-class, expires)` with a ◆ default life of 3 seasons, consumed on use; sources are the eight of `parliamentary_transfer §3` plus seizure attempts, border trespass and pledge breach. **Treaties** are `(parties, kind, bound_season)` with kinds `formal`, `non-aggression`, `sovereignty` (the one that counts for victory); each rolls lapse at 0.90 per arc, memoryless; violation voids, grants CB, Regard −2/+1; re-binding is Senator Outward at Wealth −2, strength `Influence + regard[target][actor]` vs the target's Stability. **Pledges** are single-season public or private commitments; breach is a card-declaration test (◆ the forced-breach exemption is the predicate *a hostile unit entered the pledged province this season that was not adjacent at season open*). Parliament is a deterministic tally: each parliamentary polity casts `Mandate` votes (Church `+⌊CI/20⌋`; opponents of a Church-subject motion `max(0, Mandate − ⌊CI/30⌋)`), side by ◆ `sign(regard[voter][proposer] − regard[voter][holder])`, Diplomatic Alignment overriding; Parliamentary Transfer wraps a kernel check (proposer Influence vs holder Legitimacy + 2) in that vote (majority ±1 point), with last-territory, self-target and extra-parliamentary blocks and four modes that filter CB sources. Parliamentary Manoeuvre, Crown Policy (Emergency Powers is a Policy kind that costs PI −1 per season held), Ministry countersignature, Nomination, Royal Deposition and Motion of No Confidence are rows and pipelines here; the Ministry is a polity of status `institution` whose "AP-tokens" are `Presence[Ministry]` at settlements and whose priority tree is an ordinary posture stack.

### SET-10 — Succession, Split & Emergence

**Flattened.** All changes of who leads, who exists and who counts as a faction are state machines. **Leader loss** opens a Succession Contest at the next Accounting unless a sole heir with Disposition ≥ +3 and Standing ≥ 4 exists; contenders qualify by inner-circle rank, blood, office or external backing; strength is deterministic by claim type; Stage 1 decides who leads (kernel, contested, pairwise from the top; ties by the polity's authored `succession_stat`); Stage 2 decides fragmentation by the deterministic gap `G` (≥3 unified, 2 fractious with a Disposition check, ≤1 split), with the asset division table of `faction_succession_split §2.4` (units by `Disposition + Discipline`, ties disband). **Löwenritter Graduated Autonomy** is a four-state machine (Loyal → Restless → Autonomous → Split, reversible below Split, Coup as a branch), each transition an evaluable predicate over Crown Stability, seasons without Crown military action, lost provinces and Ehrenwall's Disposition. **The insurgency pipeline** is four stages: world-level Piety decay (with ◆ `EINHIR_I_GATE = 4`), Latent RM (`regard[Varfell][RM] ≤ −2 ∧ count(PT ≤ 1 provinces) ≥ 3 ∧ MS ≤ 50`), Insurgency (two contiguous Uncontrolled provinces for two seasons; a polity of status `insurgency`, ◆ Military `clamp(count of held settlements with Order ≥ 2, 1, 3)`), Promoted Faction (L ≥ 3, 2+ provinces, mean Accord ≥ 4, two seasons; parliamentary iff mean Piety ≥ 3, persistent), with the four ratified dissolution paths (military, sponsor loss — deterministic on sponsor collapse/treaty/defeat —, amnesty as a contested check of parent Mandate vs insurgency Stability, persist). **Faction emergence from below** (`settlement_layer §6.2`) is the same pipeline's civilian face: Cell → Organisation (2+ settlements) → Movement → National (4+ settlements over 2 provinces or a Seat; Declaration check) → Hegemon; RM Settlement Emergence fires where `Order = 0 ∧ PT ≤ 1 ∧ Disposition(Vossen) ≥ +3`, once per province per 4 seasons. **Crown succession** adds Baralta's claim (Stake Claim action, +2 contest strength), the Consecration Crisis decided by Church Stability (≥4 refuses, ≤3 consecrates under duress; ◆ Himlensendt with ≥3 scars consecrates regardless), Torben's four-trigger Generational Shift with a Readiness track, and PI 20 as Deposition into the same contest with the Crown excluded. **Collapse** is `Stability 0 at Accounting`: Vacuum, then Uncontrolled, then possibly an insurgency — the bottom of one machine feeds the top of another.

### SET-11 — Personal Agency & Rank

**Flattened.** The player character has three self-authored Convictions, a faction Duty drawn each season from the faction's posture stack (the highest unaddressed need whose ◆ authored `capability_tags` intersect the PC's), a Scene Slate generated deterministically in seven priority steps and pruned to the difficulty's size, a scene-action budget (3/4/5 by difficulty, +1 at Standing 4–5, +2 at 6–7, Knot and wound modifiers), and Resources 0–5. Standing is 0–7 per faction on the eight-position ladders of `faction_politics Part 1` (Petitioner → Regent-Designate, with faction titles, Initiation Duty at 0→1, Formal Recognition at 3, branch choice at 3, hall tier, mentor, demotion magnitudes); sub-office ladders (Löwenritter, Riskbreaker, Inquisitor, Templar, Guild, Warden) are parallel Standings; Renown 0–10 and Shadow Renown 0–10 are cross-faction and non-decaying (+2/season cap); Deniability Debt 0–7 is Löwenritter's covert risk. Caste (Northern / Central / Southern Einhir) is a modifier layer: Initiation Ob, Renown halving in northern provinces for Southern Einhir, inner-circle Disposition floors, and gated ranks — all rows in the ladder data, not code. Governance scope follows Standing (3 governs a Town, 4 a City/Fortress, 5 a Seat). Leadership is reachable at Standing 7 or by challenge at 4+. Death or Portrait Retirement fires the Generational Transition partition (preserve world, transform one Conviction and half the Resources, reset the person, break Knots, transfer obligations) plus a Lineage Act. Personal scenes resolve in the kernel's pool mode and reach the strategic layers only through Domain Echo effects (`S +1, OW +2, cap ±2`) with Sufficient Scope.

### SET-12 — Campaign Arc & Decks

**Flattened.** The game starts on fire because the settlement registry is authored with friction already in it (`conflict_architecture › Starting Friction Points`): a Cathedral building and bishop-eligibility at Valorsplatz, Guild Presence 3 at Gransol, Löwenritter Presence 3 at Ehrenfeld, RM Presence at Grauwald and Oastad. Setup draws one of six Tensions cards, each a fuse (a condition set now, an event at ◆ a uniformly drawn season in 8–12), and for Royal Crisis a uniformly drawn assassination target. Four decks share one card schema (`governance_play_redesign §2.2`: family, trigger predicates, weight, cooldown, exclusions, the ask, responses with effects, follow-ons): the settlement deck, the peninsula event deck (fired by clock band crossings — `phases` step 8), the Tensions deck, and the Named Character deck (`worldbuilding §10`: Jarnstal Independence, Olafsson Exposure, Prudence Crisis, Lions' Table Mutiny, Guild Schism, Guild Forum Revolt, Constitutional Crisis, Ministry Collapse — each with its trigger completed as a predicate). The Thread revelation curve is the MS visibility band plus five trigger events; each is a mandatory slate entry. Warden faction paths A–E are five transitions into the emergence pipeline with the Wardens as the movement. The corpus's superseded 8-card, draw-2 deck remains the authoring reference for card depth; the six-card, draw-one deck is the live one.

---

## 2. State graphs, bottom-up, per set

**Conventions for this section.** Primitives are *stored* state; derivatives are *never stored* and are recomputed by pure function; pipelines are state machines with evaluable predicates. Paths: `s.` settlement, `p.` province, `f.` polity, `n.` NPC, `u.` unit, `w.` world, `pc.` player, `rel.` relation ledgers. Predicates use `∧ ∨ ¬`, comparison, `count(...)`, `Σ`, `mean`, `⌊⌋`, and named derivatives. Types: `Clamped<lo,hi>` is an integer with clamp-on-write; `Fixed` is authored data never written in play. "Writer" names the *only* source allowed to emit an Effect on that path; "commit" means any Effect, from any source, applied at the commit phase — the point is that the state is written in exactly one place even when many rules may cause the write.

### SET-01 — Resolution Kernel & Action Schema

```
        ActionDef (data row) ──declare──▶ ActionInstance ──▶ kernel.resolve(Check) ──▶ Degree
              │                                 │                     ▲                  │
   prerequisites (Predicate)             advantages[]                │            effects[degree]
   cost (Budget kind)                    strength, difficulty        │                  │
   strength_expr / difficulty_expr       mode ∈ {margin, pool}       │                  ▼
   contested?                                                   RNG stream         EffectQueue
   effects per degree ──────────────────────────────────────────────────────────────▶ commit
```

**Primitives**

| ID | Primitive | Type / domain | Owner | Writer | Lineage |
|---|---|---|---|---|---|
| P-01.01 | Degree | enum `{F, P, S, OW}` | a resolved check | kernel | `core › Degree Table`; `stats_1_7_scale › Domain Action Resolution` |
| P-01.02 | Kernel constants | `BASE 0.50, SLOPE 0.10, FLOOR 0.05, CAP 0.90, OW_OFFSET −0.35, PARTIAL_OFFSET +0.20, OW_CAP 0.55, PARTIAL_CAP 0.97` | Fixed | — | `stats_1_7_scale › Domain Action Resolution` |
| P-01.03 | Pool constants | `TN 7; faces 1→−1, 2–6→0, 7–9→+1, 10→+2; Ob floor 1; OW ⇔ net ≥ 2·Ob ∧ net ≥ 3; Ob 10 ⇒ no OW, Partial needs net ≥ 5` | Fixed | — | `core › Dice System`, `› Degree Table (PP-179 + PP-249)` |
| P-01.04 | Advantage | int (points); `+1 = +1 die = +1 M`; `Ob ∓1 = ±2` | per check instance | the modifier rows that apply | ◆ unit; mapping from `stats › Legacy Ob mapping` |
| P-01.05 | ActionDef | row: `id, scale ∈ {settlement, province, peninsula, personal}, actor_kind ⊆ {polity, governor, pc, auto}, budget ∈ {card:type, ap:n, scene:1, none}, strength_expr, difficulty_expr, contested, prerequisites[], target_kind, effects{degree → Effect[]}, cb_on_use, conviction_profile[13], tags[]` | Fixed (data) | — | `core › Standard Action Ob Reference`; `stats › Unique Actions`; `governance_play_redesign §1.3`; `ci_political §5.2` |
| P-01.06 | Card | `type ∈ {Legionary, Consul, Senator, Pontifex, Tribune, Prefect, Diplomat, Colonist, Praetor, Recess}`, `cooldown ∈ {0,1,2}` | polity hand | commit (play → cooldown; return at 0) | `core › Batch Card Hand`; `ci_political §5.3` |
| P-01.07 | Budget | `{kind ∈ {cards, ap, scene}, capacity, spent}` | its actor | commit | `ci_political §5.1`; `governance_play_redesign §1.1`; `player_agency §6` |
| P-01.08 | Seasonal delta tally | per `(path, source_class)`: int | commit ledger | commit | `stats › PP-242` |
| P-01.09 | Cap schema | per path: `range, cap_net_per_season, cap_by_source_class` | Fixed | — | `stats › Stats`; `ci_political §2.4`; `settlement_layer §4.4` |

**Derivatives**

| ID | Derivative | Expression | Lineage |
|---|---|---|---|
| D-01.01 | Margin | `M = strength + Σ advantages − difficulty` | `stats › Domain Action Resolution` |
| D-01.02 | Difficulty from a legacy Ob | `D(O) = max(1, (O − 1)·2)` | `stats › Legacy Ob mapping` |
| D-01.03 | Degree (margin mode) | `P_s = clamp(0.5 + 0.1·M, 0.05, 0.9); P_ow = clamp(P_s − 0.35, 0, 0.55); P_p = clamp(P_s + 0.2, P_s, 0.97); r ~ U[0,1): r < P_ow → OW; r < P_s → S; r < P_p → P; else F` | `stats › Domain Action Resolution` |
| D-01.04 | Degree (pool mode) | `net = Σ faces(pool + Σ advantages); Ob' = max(1, Ob); OW iff net ≥ 2·Ob' ∧ net ≥ 3; S iff net ≥ Ob'; P iff 0 < net < Ob'; F otherwise` | `core › Degree Table` |
| D-01.05 | Contested strength pair | `strength = actor.stat + adv(actor); difficulty = target.stat + adv(target)` | `stats › contested` |
| D-01.06 | Identity modifier (points) | `−clamp(mission_align + cascade_align + expectation_align, −2, +2)` where each term ∈ {−1,0,+1} or `±strictness·{1,2}` (SET-06 D-06.xx) | `faction_behavior §3.7` |
| D-01.07 | Coalition advantage | `+2·(k − 1)` capped `+6`, `k` = count of polities whose declared action this phase has `tags ∋ suppress_L` on the same target | `parliament › PP-296` |
| D-01.08 | Failed-DA cost | `degree = F ∧ actor_kind = polity ∧ ¬tags ∋ self_improve ∧ actor.status ≠ movement → Effect(f.Stability, −1)` | `stats › PP-403` |
| D-01.09 | Budget availability | `cards: hand ∋ type ∧ cooldown(type) = 0`; `ap: capacity − spent ≥ cost`; `scene: capacity − spent ≥ 1` | `ci_political §5.3`; `governance_play_redesign §1.1` |
| D-01.10 | Commit clip | `Δ_applied = clamp(Σ Δ_requested, −cap, +cap)` per path per season; source-class sub-caps first | `stats › PP-242`; `ci_seizure › CI seasonal cap` |
| D-01.11 | AP capacity | `2 + s.FacilityTier + [governor.Standing ≥ 5]` | `governance_play_redesign §1.1` ◆ Standing ≥ 5 |
| D-01.12 | Scene budget | `{Narrative 5, Normal 4, Hard 3} + [Standing ∈ 4..5] + 2·[Standing ≥ 6] + [Knot in territory] − [Stamina = 0] − [Wounds ≥ 2]` | `player_agency §6` |

**Pipelines**

**PL-01.01 Resolve a check.** Entry: `ActionInstance` with prerequisites satisfied. Steps: (1) evaluate `strength_expr`, `difficulty_expr` (contested → D-01.05); (2) collect advantage rows whose predicate holds (identity, expertise `+1` if card type = polity's expertise, terrain, Fort, coalition, CI weight, Regard, temperament); (3) mode = `pool` iff `scale = personal`, else `margin`; (4) D-01.03 or D-01.04 with the stream `rng(season, phase, instance_key)`; (5) select `effects[degree]`; if the degree row is absent take the next lower present row; (6) D-01.08; (7) enqueue Effects with `source_class = action`. Terminal: Degree recorded on the instance; the instance is immutable thereafter (`strategic_layer §9.6` "what has been rolled stands").

**PL-01.02 Card lifecycle.** `in_hand --play(PH-03)--> declared --resolved(PH-05/06)--> cooling(n = cooldown) --PH-11: n−1--> ... --n = 0--> in_hand`. Recess: cooldown 0. Invariant: `|hand| + |cooling| = |authored hand|`.

**PL-01.03 Budget season.** `PH-01: spent := 0, capacity := D-01.11/12 ; PH-03..05: spend ; PH-12: discard`. AP and scene actions do not carry over.

**Transitions out of SET-01.** `Degree` → every set (as the input to `effects[degree]`); `Effect` → SET-02 queue; identity modifier ← SET-06; Fort/terrain advantages ← SET-03; CI weight ← SET-08; Regard ← SET-09.

---

### SET-02 — Calendar & Tick

```
 season N ─▶ PH-01 open ─▶ PH-02 world stroke ─▶ PH-03 orders ─▶ PH-04 personal ─▶ PH-05 settlement
        ─▶ PH-06 province ─▶ PH-07 COMMIT ─▶ PH-08 derive ─▶ PH-09 peninsula ─▶ PH-10 pipelines
        ─▶ PH-11 settle ─▶ PH-12 check & advance ─▶ season N+1   (Year-End / arc work inside PH-12)
                                   ▲
              EffectQueue ◀────────┘ (all action effects from PH-03..06 wait here)
```

**Primitives**

| ID | Primitive | Type / domain | Owner | Writer | Lineage |
|---|---|---|---|---|---|
| P-02.01 | Season index | int ≥ 1; `name = {1:Spring, 2:Summer, 3:Autumn, 0:Winter}[season mod 4]` | world | PH-12 | `phases › Phase 5` step 13 |
| P-02.02 | Phase | enum PH-01..PH-12 | sequencer | sequencer | ◆ unification of the four phase schemes |
| P-02.03 | EffectQueue | ordered list of `Effect{path, op ∈ {add, set, max, min}, amount, source_class, source_ref, key}` | world | any rule (append) ; drained only by commit | `strategic_layer §9.3` "batch to Cascade"; reconciliation |
| P-02.04 | Derived snapshot | cache of all D-values as of the last derive | world | PH-08, PH-12 | ◆ answers "which snapshot" for Prominence, cascade |
| P-02.05 | RNG root seed | 64-bit | world (Fixed at campaign start) | — | ◆ |
| P-02.06 | Input log | list of player decisions `(season, phase, actor, choice)` | world | player input | ◆ replay |
| P-02.07 | Sustained counter | per `(predicate_id, subject)`: consecutive true Accountings | world | PH-12 | `insurgency §5.1`; `phases` step 12 |
| P-02.08 | Once-per-year registry | set of `(effect_id, year)` | world | PH-12 | `phases › Year-End` step 7 |
| P-02.09 | Attribute-loss tally | per polity per season: count of stat decrements | commit ledger | commit | `phases › Phase 5` step 2 |

**Derivatives**

| ID | Derivative | Expression | Lineage |
|---|---|---|---|
| D-02.01 | `is_year_end` | `season mod 4 = 0` | `phases › Year-End` |
| D-02.02 | `is_arc_boundary` | `season mod 4 = 0` (same instant; arc ≡ year) | `treaty_expiration §1.1` |
| D-02.03 | Action order in PH-06 | sort by `(tier(card_type), −actor.Stability, actor.name)`; tier = `{Tribune:1, Legionary:2, Consul/Prefect/Colonist:3, Senator/Diplomat:4, Pontifex:5, unique:6, Praetor:7}`; two actions with equal `(tier, Stability)` that target the same province and are both military resolve simultaneously (both read pre-state) | `phases › Phase 4`; `strategic_layer › P-18` |
| D-02.04 | Effect apply order | `(scale_rank{settlement:0, province:1, polity:2, peninsula:3}, path, key)` | reconciliation ("scale, then phase, then stable key") |
| D-02.05 | `rng(season, phase, key)` | `SplitMix64(hash(seed, season, phase, key))` — one independent stream per subject so reordering unrelated subjects never changes a draw | ◆ |
| D-02.06 | State hash | `blake3(canonical serialisation of all primitives)` after each phase | ◆ |
| D-02.07 | Stability check trigger | `attribute_loss_tally(f) ≥ 2 → auto ActionDef stability_check: M = f.Stability − tally; F → Effect(f.Stability, −1)` | `phases` step 2; `stats › §1.4` |

**Pipelines**

**PL-02.01 The season.** See §3.1 for the full phase list with reads and writes. Terminal states of a season: `continue`, `victory(f)`, `rupture`.

**PL-02.02 Commit.** Entry: PH-07 (action effects) and each of PH-09..PH-11 (accounting effects, applied at the end of their own phase). Steps: (1) stable-sort by D-02.04; (2) group by `(path, season)`; (3) apply source-class sub-caps then net cap (D-01.10); (4) clamp to the path's range; (5) write; (6) emit `state.changed(path, old, new, source_ref)`; (7) record attribute-loss tally. Nothing else writes state.

**PL-02.03 Sustained-N.** For each registered predicate: at PH-12, `counter := predicate ? counter + 1 : 0`. A rule that needs "N consecutive" reads `counter ≥ N`. Registered: victory (N = 2), insurgency formation (2), promotion (2), Mass-Seizure failure window (Year-Ends), fractional stabilisation (4 seasons), unconsecrated rule (3), Löwenritter dwell (4), Latent RM suppression (1).

**Transitions out of SET-02.** The phase enum is what every pipeline's `advance_phase` names; the queue is where every set's effects go; the snapshot is what every derivative read during PH-02..06 returns.

---

### SET-03 — Map & Movement

```
 Province p (Fixed: duchy, seat, fort, proximity, SW, temperament, base_PV)
   ├── Settlement s₁ (hub/seat) ── road ── Settlement s₂ ── river ── s₃      (intra-province edges)
   │        └── hub-to-hub edge to adjacent province's hub (type: road|river|pass|coastal|gate)
   └── Units u at settlements; march budget in edges; Assault | Siege | Bypass at hostile nodes
```

**Primitives**

| ID | Primitive | Type / domain | Owner | Writer | Lineage |
|---|---|---|---|---|---|
| P-03.01 | Province | Fixed: `id, name, duchy ∈ {Valorsmark, Hafenmark, Varfell, none}, seat: SettlementId, members[], fort 0–4, proximity 0–5, SW 0–5, temperament ∈ {pragmatic, traditional, balanced, principled, outcomes_only}, base_PV 0–5, controllable: bool, capital_of: PolityId?` | registry | — | `geography › Territory Table`, `› Spiritual Weight`, `› Proximity Ratings`; `territory_temperaments §2`; `ci_political §1` (PV) |
| P-03.02 | Settlement (fixed part) | Fixed: `id, name, province, type, role ∈ {primary, spoke}, xy, districts[] ⊆ {Palace, Port, Cathedral, Market, Barracks, Citadel, Watch, Storehouse, Mines, Lodge, Shrine, Cove, Parliament, Harbor, Seminary}` | registry | — | `settlement_layer §2.1–2.2`; ◆ `xy` |
| P-03.03 | Edge | Fixed: `(a, b, type ∈ {road, river, pass, coastal, gate, thread}, cost)`; 56 edges; `thread` edges carry no units | registry | — | `settlement_adjacency §1.1–1.2`; reconciliation (56/37) |
| P-03.04 | Unit | `id, polity, at: SettlementId, kind ∈ {levy, professional, cavalry, siege, templar, vanguard}, discipline 1–5, budget_left (edges)` | unit registry | commit | `settlement_layer §5.2`; `march_layer §1`; `clocks › Vanguard` ◆ minimal schema (military_layer absent) |
| P-03.05 | Siege | `(unit, target: SettlementId, since_season)` | unit registry | commit | `settlement_layer §5.1`; `settlement_adjacency §2.4` |
| P-03.06 | Known-state | per polity per settlement: last observed `(season, controller, garrison, Prosperity)` | polity | PH-06 | `march_layer §3.1` (display only) |
| P-03.07 | Expedition | `(polity, champion: NpcId|Pc, stage ∈ {staged, departed, inside, returned}, seasons_inside)` | world | pipelines | `geography › Expedition Procedure` |

**Derivatives**

| ID | Derivative | Expression | Lineage |
|---|---|---|---|
| D-03.01 | March budget (edges) | `max(1, ⌊f.Military/2⌋) + [cavalry_majority(u)]` where cavalry-majority = kind cavalry; skirmish (levy-only, no siege) `+1` more, total cap `⌊f.Military/2⌋ + 2` | `settlement_adjacency §1.3`; `march_layer §1.1–1.2` ◆ edge form |
| D-03.02 | Edge traversable | `type ≠ thread ∧ (type ≠ coastal ∨ (Port ∈ from.districts ∧ ¬(w.IP ≥ 75 ∧ edge crosses to Schoenland))) ∧ budget_left ≥ cost` | `settlement_adjacency §1.1`; `march_layer §6.3` ◆ |
| D-03.03 | Forced engagement | `∃ hostile unit at destination ∨ (dest.type = Fortress ∧ hostile(dest.controller) ∧ f.Military ≤ dest.Defense + 3)` | `march_layer §2.4`; `settlement_layer §5.1` |
| D-03.04 | Attack advantage | `−[edge ∈ {river, pass, gate}] − [edge = coastal]·Fort(p)` | `settlement_adjacency §2.2` |
| D-03.05 | Defence strength | `defender.Military + p.fort + s.Defense/2 + garrison.discipline/2 + [s.type = Seat] + [Accord(p) = 3]` (halves floored) | `settlement_adjacency §2.2`; `tracks › Accord`; `geography › Fortification Combat Rule` |
| D-03.06 | Bypass allowed | `attacker.Military > s.Defense + 2 + [s.type = Fortress]` | `settlement_layer §5.1` |
| D-03.07 | Supply distance | BFS edges from `u.at` to nearest friendly `{Seat, Fortress, Port, Mine}`; attrition iff `> 4` | `march_layer §1.3` ◆ 4 |
| D-03.08 | Garrison | `units at s with polity = s.controller` | `settlement_layer §5.2` |
| D-03.09 | Radiation band effects | table `clocks.md › MS Effects` indexed by `(band(w.MS), p.proximity)` with the rebased bands; yields Ob shifts as advantage rows on actions in `p` | `clocks › Mending Stability (MS) Effects` |
| D-03.10 | Vision | settlements within 2 hops of any friendly unit or controlled settlement; `+` scouted set | `march_layer §3.2` ◆ hop form |

**Pipelines**

**PL-03.01 March.** Entry: unit with `budget_left > 0` and a declared destination path (AI: A* by cost). Steps per edge: `traversable? → move → budget −= cost → entering a province controlled by another polity without treaty → Effect(rel.cb += CB(p.controller → u.polity, source: trespass), rel.regard[p.controller][u.polity] −1) → forced engagement? → stop`. Terminal: at a node.

**PL-03.02 Contact at a hostile settlement.** Entry: unit at hostile-controlled `s`. Branch: `Assault` (auto ActionDef `assault`, contested, strength `attacker.Military + discipline/2 + D-03.04`, difficulty D-03.05) · `Siege` (requires no forced-engagement army present; needs `kind ∈ {professional, siege}` present) · `Bypass` (D-03.06). Assault outcomes: `OW → control(s) := attacker, Prosperity −1, defending units destroyed; S → control(s) := attacker, Prosperity −1, defenders retreat one edge, attacker discipline −1; P → drawn, both discipline −1, hold; F → attacker retreats one edge, discipline −1, and if M ≤ −2 → Effect(attacker.Military, −1)`. Every assault emits `battle.resolved(p, s, attacker, defender, degree)`.

**PL-03.03 Siege.** `besieging --each PH-11: Effect(s.Order, −1)--> ... --s.Order = 0--> surrender: control(s) := besieger; emits battle.resolved(degree = S)`. Broken if the besieger leaves or is defeated by a relief assault.

**PL-03.04 Expedition (T6 → T15).** `staged` requires `control(Stillhelm) = f ∧ champion.TS ≥ 30 ∧ champion at Stillhelm one full season`; `declare` = ActionDef `expedition` (strength `min(3, ⌊TS/10⌋)`, difficulty from Ob 3, advantages `+2` if RM Presence at Stillhelm ≥ 1); `S/OW → departed`; on entry `forgetting_check` (Ob 2): `F → returned, nothing; P → inside, warden_emergence := true; S → inside, WC +1, WR +1; OW → inside, WC +1, WR +1, edeyja_contact := true`. Terminal: `returned`.

**PL-03.05 Vanguard.** Entry: `w.IP ≥ 75` and no vanguard unit → spawn `vanguard` unit (Military-equivalent 5, discipline 5) at Spartfell Fortress. Each PH-10: if no faction unit shares its node for 2 consecutive seasons → advance one node along the authored invasion route `[Spartfell, Lowenskyst, Kronmark, Valorsplatz]`; a faction unit on the node forces a contested assault (defender Military vs difficulty from Ob 3); while at Valorsplatz every national polity `Stability −1` per season. Removed when IP < 60 or by the repulsion paths (SET-07).

**Transitions out of SET-03.** `battle.resolved` → SET-07 (MS, Turmoil) and SET-05 (control, Order); control change → SET-05 (fractional, Accord, PV); supply/attrition → SET-06 (Military via unit loss); Expedition → SET-07 (WC/WR).

---

### SET-04 — Settlement Governance

```
   Provincial Authority ──Directive──▶ ┌───────────── Settlement s ─────────────┐
   (seat-holder of p)                  │ Prosperity Defense Order L PS PT Tier   │
        ▲  Comply/Bargain/Defy         │ controller · governor · Church axes     │
        │  (suspicion)                 │ Presence[inst] · Π · Ledger · Needs     │◀── Local Actors, NPC ambitions
   Governor (NPC / PC / institution) ──│ AP verbs: Develop Fortify KeepOrder     │──▶ settlement deck draw 1+⌊Π/3⌋
        spends AP = 2 + Tier           │   HoldCourt Sponsor Treat Levy Investig.│
                                       └────────────┬────────────────────────────┘
                                 derives upward: Order→Accord, Prosperity→PV share, L/PS→Mandate, PT→CI
```

**Primitives**

| ID | Primitive | Type / domain | Owner | Writer | Lineage |
|---|---|---|---|---|---|
| P-04.01 | `s.Prosperity` | `Clamped<0,6>`; 6 only at the Kingdom capital | settlement | commit | `settlement_layer §1.3`; reconciliation |
| P-04.02 | `s.Defense` | `Clamped<0,5>` | settlement | commit | `settlement_layer §1.3` |
| P-04.03 | `s.Order` | `Clamped<0,5>` | settlement | commit | `settlement_layer §1.3` |
| P-04.04 | `s.L`, `s.PS` | `Clamped<0,7>` each, meaning "acceptance of the *current* controller" | settlement | commit | `settlement_layer §1.8` |
| P-04.05 | `s.PT` | `Clamped<0,5>` Piety | settlement | commit | `tracks › Starting Piety Track`; `fractional §2.5` ("PT applies per-settlement") |
| P-04.06 | `s.FacilityTier` | `Clamped<0,3>` (0 billets, 1 chambers, 2 suites, 3 wings) | settlement | commit | `settlement_layer §1.4, §1.8` |
| P-04.07 | `s.controller` | `PolityId | ∅` | settlement | commit | `settlement_layer §1.1`; `fractional §2.1` |
| P-04.08 | `s.governor` | `NpcId | PcId | PolityId(institution) | ∅` | settlement | commit | `settlement_layer §3.2–3.3` |
| P-04.09 | `s.church.building` | `enum {none, chapel, church, cathedral}` | settlement | commit | `campaign_architecture §1.1` |
| P-04.10 | `s.church.templar`, `s.church.inquisitor` | bool, bool | settlement | commit | `campaign_architecture §1.1` |
| P-04.11 | `s.presence[inst]` | `Clamped<0,3>` for `inst ∈ {RM, Guilds, Ministry, Löwenritter, Wardens}` | settlement | commit | ◆ unifies Presence markers, CP/AP-tokens, Guild Favour (`ministry.md`, `institutions`, `core › Community Organising`, `stats › Economic Leverage`) |
| P-04.12 | `s.pressure` Π | `Clamped<0,10>` | settlement | PH-02 | `governance_play_redesign §2.1` |
| P-04.13 | `s.suspicion` | `Clamped<0,5>` of the governor by the Provincial Authority | settlement | commit | `governance_play_redesign §1.4` ◆ range |
| P-04.14 | `s.ledger[]` | tags `{kind ∈ {Precedent, Grudge, Debt, Reputation}, subject, weight, expires?, ob_shift?}` | settlement | commit | `governance_play_redesign §1.6` |
| P-04.15 | `s.needs[]` | `{kind, weight 1–3, opened_season, served: bool}` | settlement | PH-02 (open), commit (serve) | `governance_play_redesign §1.5` ◆ weight |
| P-04.16 | `s.directive` | `{kind ∈ {Extract, Tax, Suppress, Install, Host, Cede, Hold}, param, response ∈ {∅, Comply, Bargain, Defy}}` | settlement | PH-02 (issue), PH-05 (respond) | `governance_play_redesign §1.4` |
| P-04.17 | Local Actor | an NPC with `role ∈ {Elder, Magistrate, Merchant, Priest, Artisan, Farmer, Fisher, Miner, Scholar, Healer, Broker}` resident at `s` | NPC registry | commit | `settlement_layer §4.5, §4.8` |
| P-04.18 | `s.ap` | Budget kind `ap` | settlement (this season) | PH-01, PH-05 | `governance_play_redesign §1.1` |

**Derivatives**

| ID | Derivative | Expression | Lineage |
|---|---|---|---|
| D-04.01 | Weight | `W_s = base(type) + Prosperity + FacilityTier`, `base = {Seat 3, City 3, Cathedral 3, Town 2, Fortress 2, Port 2, Village 1, Mine 1, Outpost 1}` | `settlement_layer §1.8` |
| D-04.02 | Acceptance | `q_s = (L + PS)/2` | `settlement_layer §1.8` |
| D-04.03 | Black market | `Order ≤ 1 ∨ governor = ∅` → advantage `+1` on covert actions here; income counts `Prosperity + 0.5` (◆ fraction carried); `Order −1` every second season it persists (◆ maps the corpus's 'Accord −0.5') | `settlement_layer §4.7` ◆ (settlements have no Wealth/Accord; mapped to income and Order) |
| D-04.04 | Broker present | `Prosperity ≥ 3 ∧ (governor = ∅ ∨ controller.Stability ≤ 2)` → a Local Actor is assigned role Broker | `settlement_layer §4.8` |
| D-04.05 | Exploitation site | `province.proximity ≤ 2` → harvest ActionDef available; harvest → `w.MS −0.5` (fraction carried), harvester `Wealth +1` | `settlement_layer §4.9` |
| D-04.06 | Provincial Authority | `controller(province.seat)` | `settlement_layer §3.1` |
| D-04.07 | Church services | `building = chapel → Order +½/season; church → +1 once at build; cathedral → +1 once and Order floor 1` | `settlement_layer §1.6` |
| D-04.08 | Bishop eligible | `building ≥ church ∧ (governor = ∅ ∨ disposition(governor, Church) ≥ +2) ∧ controller ≠ Church` | `conflict_architecture › Bishop Appointment` |
| D-04.09 | Pastoral assumption eligible | `governor = ∅ ∧ building ≥ chapel` | `settlement_layer §1.7` |
| D-04.10 | Π next | `clamp(Π + Σ_{needs ¬served} weight + Σ_{Grudge} weight + count(NPC at s with ambition.progress ≥ ⌈timeline/2⌉) + shock − Σ releases − [no open needs], 0, 10)` with `shock = [Accord(p) fell] + 2·[battle in p] + [Turmoil ≥ 7] + Σ card.pressure_delta` | `governance_play_redesign §2.1` ◆ every unit |
| D-04.11 | Deck draw count | `1 + ⌊Π/3⌋`; family weights by band: `Π ≤ 2` favours Opportunity/Ambition ×3, `3..7` Petition/Friction/Intrigue ×2, `≥ 8` Crisis ×3 | `governance_play_redesign §2.1, §2.4` |
| D-04.12 | Needs emitted | `Prosperity = 0 → Need(famine, 3)`; `Order ≤ 1 → Need(justice, 2)`; `Defense = 0 ∧ hostile unit adjacent → Need(defence, 2)`; `presence[Guilds] ≥ 2 ∧ ¬charter → Need(charter, 1)`; `Order = 5 ∧ Prosperity ≥ 4 → Need(expansion, 1)`; `directive ≠ Hold → Need(directive_conflict, 1)` if it conflicts with an open Need | `governance_play_redesign §1.5`; `settlement_layer §4.3` ◆ |
| D-04.13 | Directive generator | the Provincial Authority's top posture-stack row maps to a directive kind: `Existential/Consolidate → Tax`, `Defend → Extract`, `Counter-threat → Suppress(RM|Church)`, `Expand → Extract`, `Opportunistic → Hold`, plus `Install` when a bishop/officer placement is pending and `Cede` when a treaty requires it | `governance_play_redesign §1.4` ◆ |
| D-04.14 | Local Actor count | `{Seat 2, City 2, Port 2, Town 1, Fortress 1, Cathedral 1, Mine 1, Village 1, Outpost 0}` | `settlement_layer §4.5` |
| D-04.15 | Seed state | `Prosperity = authored(province).pros if primary else {City 3, Port 3, Cathedral 3, Town 2, Mine 2, Fortress 1, Village 1, Outpost 0}[type]`; `Defense = max(province.fort, base_def[type]) if primary else base_def[type]`, `base_def = {Fortress 3, Seat 2, City 1, Cathedral 1, Port 1, Outpost 1, else 0}`; `Order = 3 if primary ∨ province.capital_of ≠ ∅ else 2`; `L = PS = controller.authored_seed`; `PT = authored(province).pt`; `FacilityTier = {Seat 3, Cathedral 3, City 2, Town 1, Fortress 1, Port 1, else 0}`; `Π = 2`; `presence` per the friction registry | ◆ the seed-state generator; reproduces the authored starting Accord (capitals 3, home 2) exactly |

**Pipelines**

**PL-04.01 Governor's season.** `PH-02: directive issued, needs emitted, Π recomputed, cards drawn` → `PH-05: respond(directive) ∈ {Comply: suspicion −1, Standing +0, apply directive effect; Bargain: ActionDef bargain (strength governor.Influence-or-Charisma, contested vs Authority.Influence), S → softened directive, F → suspicion +1; Defy: suspicion +1, Regard(local actors) +1, PS +1, directive void}` → `spend AP on verbs` → `play drawn cards' responses` → effects queued. Verbs (each an ActionDef row): **Develop** (2 AP, Ob `⌊Prosperity/2⌋+1`, method `Treasury|Guild|Corvée` → `Prosperity +1` and respectively `controller.Wealth −1 | presence[Guilds] +1 | Order −1`); **Fortify** (2 AP, Ob `⌊Defense/2⌋+1`, `Garrison|Militia|Walls` → `Defense +1` and `presence[Löwenritter] +1 | PS +1, tag(militia) | controller.Wealth −1`); **Keep Order** (`Consent` 2 AP → `Order +1, PS +1`; `Force` 1 AP → `Order +1, PS −1, disposition(local actors) −1`; `Clergy` 1 AP → `Order +1, church.building := max(chapel)`); **Hold Court** (1 AP; a Petition card scene; ruling → `disposition ±1`, tag(Precedent)); **Sponsor** (1–2 AP, `Wealth`/Resources → durable `+1` stat and tag(Debt, expires +4)); **Treat** (1 AP, contested vs institution leader → a chit = tag(Debt) owed by the governor); **Levy** (1 AP → `controller.{Wealth|Military|Intel} +1` and `Order −1 ∨ PS −1`); **Investigate** (1–2 AP, contested vs concealment → reveal covert presence; then `expose|expel|co-opt|shelter`). Terminal: AP exhausted or declined.

**PL-04.02 Suspicion.** `0..2 quiet --suspicion ≥ 3--> recall (mandatory scene: social contest vs Authority; S → suspicion := 1; F → suspicion := 4) --suspicion ≥ 5--> replaced (governor := ∅, unless q_s ≥ Mandate(Authority) + 1, in which case emergence(Stage 2) is offered and the settlement secedes on acceptance)`. ◆ thresholds 3 and 5.

**PL-04.03 Settlement drift (PH-11).** `Order: −1 if Prosperity = 0; −1 if governor = ∅ (unmanaged); +½ if chapel (fraction carried); −1 if besieged; +1 if Order ≥ 4 for 3 seasons ∧ governor ≠ ∅ (◆ passive normalisation, mirrors province Accord +1 rule)`. `Prosperity: +1 at Feldmark and Halvardshelm primaries if no hostile unit in province (authored breadbasket flag); −1 at Prosperity 0 famine`. `L/PS: mean-revert toward Mandate (SET-05 D-05.09); recover +1 toward seed if no hostile DA targeted the controller this season ∧ controller.Stability ≥ 2`.

**PL-04.04 NPC ambition.** `dormant --PH-02 each season: progress += 1 (+1 more if a helping card resolved)--> in_motion (progress ≥ ⌈timeline/2⌉) --progress ≥ timeline--> acts: emit Ambition card; then re-plan: blocked → method shifts lawful → factional → violent/covert; disposition(governor) ≤ −2 → seeks patron / defects; conviction violated → tag(Grudge, self)`.

**PL-04.05 Settlement revolt.** `Order = 0 at PH-12 → if garrison = ∅: governor := ∅, controller := ∅ (Uncontrolled settlement), Turmoil +1; else garrison fights uprising (auto contested check: garrison Military vs difficulty from Ob 2; F → as above)`.

**Transitions out of SET-04.** `Order` → SET-05 Accord; `Prosperity` → SET-05 PV shares, SET-06 income; `L/PS` → SET-05 Mandate; `PT`, church axes → SET-08; `presence[RM]` → SET-10 (Latent RM, emergence); Π/cards → SET-12 decks; Levy → SET-06 stats; Directive ← SET-06 posture stack; Local Actors/ambitions → SET-11 slate.

---

### SET-05 — Province Control & Legitimacy

```
  settlements s ∈ p ──▶ controller(seat) = Provincial Authority
        │                 Accord(p)   = ⌊mean Order⌋              (0–3 ladder)
        │                 PV_share(f,p) = base_PV · Σ_{s: ctl=f} Pros_s / Σ Pros_s
        │                 fractional(p) = ∃ s: ctl(s) ≠ ctl(seat)
        ▼
  faction f ──▶ Mandate(f) = clamp(round(7·T/(T+6))),  T = Σ_{s: ctl=f} W_s·q_s/7
              ──▶ aggregate_L, aggregate_PS (W-weighted means)
              ──▶ Prominence(Church, p) = Mandate(Church) > Mandate(ctl(p))
  pipelines: Fragmentation Check · Consolidation · Secession · Vacuum → Uncontrolled
```

**Primitives**

| ID | Primitive | Type / domain | Owner | Writer | Lineage |
|---|---|---|---|---|---|
| P-05.01 | `p.stabilised_until` | season | province | commit (Fragmentation OW) | `fractional §2.6` |
| P-05.02 | `p.vacuum_until` | season | province | commit (elimination) | `core › Faction Elimination` (PP-500) |
| P-05.03 | `p.attention` | `Clamped<0,10>` Church Attention Pool; resets each PH-11 | province | commit | `tracks › Church Attention Pool` |
| P-05.04 | `p.thread_debt[]` | tokens `{age, serviced}` | province | commit | `phases` step 6; `strategic_layer › G-04` |
| P-05.05 | `p.trade_route` | `{holder, linked: ProvinceId?}` | province | commit | `tracks › Trade Network Investment` |
| P-05.06 | `p.temperament_drift` | `Clamped<−1,+1>` real | province | PH-09 | `faction_behavior §3.4.2` |
| P-05.07 | `p.consolidation` | `{declared_by, pending_responses{s → Submit|Resist|∅}}` | province | PH-06, PH-10 | `fractional §2.4` |
| P-05.08 | `p.hostile_free_seasons` | consecutive seasons with no hostile action in `p` | province | PH-12 | `phases` step 4c(iii) |

**Derivatives**

| ID | Derivative | Expression | Lineage |
|---|---|---|---|
| D-05.01 | Provincial Authority / controller | `ctl(p) = s_seat.controller` (`∅` → Uncontrolled) | `fractional §2.1` |
| D-05.02 | Accord | `⌊(Σ_s Order_s + Order_seat)/(|members| + 1)⌋` (Seat weighted double), clamped 0–3; single-settlement province: `Order_seat` clamped 0–3 | `settlement_layer §1.3`; ED-SETT-03 |
| D-05.03 | Accord effects | `3: defender +1 advantage; 2: —; 1: Govern +2 difficulty points, garrison required; 0: Revolt` (PL-05.04) | `tracks › Accord` |
| D-05.04 | Province Prosperity | `Σ_s Prosperity_s` | reconciliation |
| D-05.05 | Province Piety | `⌊mean_s PT_s⌋` | `fractional §2.5` |
| D-05.06 | PV share | `share(f,p) = base_PV · Σ_{s ∈ p, ctl(s)=f} Pros_s / Σ_{s ∈ p} Pros_s` (1 decimal); if `Σ Pros = 0`: equal split with remainder to Seat and `Accord := 0` next PH-12 | `fractional §2.2` (FRAC-01) |
| D-05.07 | Fractional | `∃ s ∈ p: s.controller ≠ ctl(p)`; `aliens(p) = {s : s.controller ≠ ctl(p)}` | `fractional §2.1` |
| D-05.08 | Mandate | `T = Σ_{s: ctl(s)=f} W_s·q_s/7 ; Mandate(f) = clamp(round(7·T/(T+6)), 0, 7)`; a `movement` sums over settlements with `presence[f] ≥ 1` using `q_s` of those settlements weighted by `presence` instead of `W` | `settlement_layer §1.8`; `faction_behavior §4` |
| D-05.09 | Aggregate L / PS | `Σ W_s·L_s / Σ W_s`, `Σ W_s·PS_s / Σ W_s` over controlled settlements | `settlement_layer §1.8` |
| D-05.10 | Prominence | `Prominent(Church, p) ⇔ Mandate(Church) > Mandate(ctl(p))`; read from the snapshot | `ci_seizure › Seizure Ob`; `phases` step 4b |
| D-05.11 | Consolidation eligible | `share(f,p)/base_PV ≥ 0.75 ∧ fractional(p) ∧ f = ctl(p)` | `fractional §2.4` |
| D-05.12 | Fragmentation difficulty | `D(2 + |aliens(p)|)` (D-01.02) | `fractional §2.6`, FRAC-03 |
| D-05.13 | Greater/Lesser name | Seat-holder's part keeps the name; each alien controller's part is `dir(centroid(alien s) − xy(seat))` ∈ {Northern, Southern, Eastern, Western}, `Outer` if `|dx|,|dy| both < 0.25·extent` | `fractional §2.3` ◆ centroid rule |
| D-05.14 | Uncontested (for Ministry default) | `¬∃ hostile unit in p ∧ ¬∃ cb targeting ctl(p) with source ∈ {military}` | `ministry › Priority 5` ◆ |
| D-05.15 | Effective temperament | `α_eff = clamp(α + 0.2·drift, 0.1, 0.9), β_eff = 1 − α_eff` | `faction_behavior §3.4.2` ◆ conversion |

**Pipelines**

**PL-05.01 Control change at a settlement.** Entry: any commit to `s.controller`. Effects in the same commit group: `s.governor := ∅` unless the new controller is an institution installing one; `disposition(local actors, ·) := 0`; `s.L, s.PS := seed(new controller)` clamped; if `s = seat(p)`: emit `control.transferred(p, old, new)`, `Accord` pinning by acquisition class — military → each member `Order := min(Order, 1)`; administrative (appointment, transfer, consolidation, treaty) → `Order := min(Order, 2)` (◆ "non-military → Accord 2"); trade route token cleared. Then D-05.07 flips `fractional`.

**PL-05.02 Fragmentation Check (PH-10, each fractional `p` with `season ≥ stabilised_until`).** Auto ActionDef `fragmentation`: actor `ctl(p)`, strength `Influence`, difficulty D-05.12. `OW → stabilised_until := season + 4; S → none; P → random alien s (stream) Order −1; F → Secession offered to each alien s whose controller is national: AI accepts iff Order_s ≥ 3 ∧ Defense_s + garrison ≥ 1 (◆); accepted → s.controller := Independent(s)` (a new polity of status `city-state` seeded from `s`, SET-06). Aliens held by a movement or `∅` are never secession candidates; if no candidate, treat F as P.

**PL-05.03 Consolidation.** `declared (ActionDef consolidate: strength Influence, difficulty D(⌈2·(1 − share/base_PV)·base_PV⌉)) --S/OW--> responses pending (each alien controller: Submit → s.controller := ctl(p), Order −2; Resist → mandatory assault next season by ctl(p); AI: Resist iff Defense + garrison ≥ 2, else Submit) --all resolved--> unified`. `P/F → nothing; F costs Stability −1 (D-01.08)`.

**PL-05.04 Province Revolt & Vacuum.** At PH-12: `Accord(p) = 1 ∧ garrison(seat) = ∅ → Order_s −1 ∀ s` (so Accord falls to 0 next season unless governed); `Accord(p) = 0 → Revolt: garrison fights uprising (contested, difficulty from Ob 2) else ctl(p) := ∅ for every member; Turmoil +1`. Elimination of `ctl(p)`: `vacuum_until := season + 1`; in Vacuum no unit may enter and no action targets `p`; after: members `controller := ∅`, Fort retained, presence tokens of the eliminated polity removed. Passive normalisation: `hostile_free_seasons ≥ 2 ∧ garrison ≠ ∅ → Order +1 (cap 4) ∀ s`.

**PL-05.05 L/PS feedback (PH-11).** ∀ `s` with `ctl(s) = f`: `q_s ≤ Mandate(f) − 1 → L +1; q_s ≥ Mandate(f) + 1 → PS −1` (at most one step per settlement per season; within the `±2` cap). Faction-level mission outcomes (SET-06) apply `ΔL, ΔPS` uniformly to controlled settlements.

**Transitions out of SET-05.** `Accord` → SET-07 (Turmoil, IP), SET-09 (adjacent-instability CB), SET-12 (victory count); `Mandate` → SET-01 (strengths), SET-09 (votes), SET-06 (strictness); `Prominence` → SET-08 (CI, seizure); `ctl(p) = ∅` → SET-10 (insurgency substrate); Secession → SET-06 (new polity).

---

### SET-06 — Polities (Factions & Institutions)

```
 Polity f
 ├ status ∈ {national, institution, movement, insurgency, city_state, foreign} ──▶ capability flags
 ├ stats: Influence Wealth Military Intel Stability (stored)   Mandate (derived, SET-05)
 ├ hand[] · cooldown[] · expertise · budget
 ├ mission{text, aligned[], contradicted[]} · cascade_roots[] · institutional_culture
 ├ offices[] {name, holder, competence 0–3, corruption 0–3}
 ├ private tracks (RDT, TD, deniability_debt, awareness, readiness[council])
 └ posture stack (data rows) ──▶ chosen ActionInstances each PH-03 ──▶ Directives (SET-04), Duties (SET-11)
```

**Primitives**

| ID | Primitive | Type / domain | Owner | Writer | Lineage |
|---|---|---|---|---|---|
| P-06.01 | `f.status` | enum above | polity | pipelines (SET-10) | `settlement_layer §6.2–6.3`; `insurgency §4–5`; `core › NPC-Only Factions` ◆ unification |
| P-06.02 | `f.Influence` 1–7, `f.Wealth` 0–7, `f.Military` 0–7, `f.Intel` 0–7, `f.Stability` 0–7 | Clamped | polity | commit | `core › Stat Ceilings and Floors`; `stats › Stats (1–7 scale)` |
| P-06.03 | `f.hand[]`, `f.cooling[]` | cards | polity | commit | `core › Batch Card Hand` |
| P-06.04 | `f.expertise` | card type | Fixed | — | `core › Domain Expertise` |
| P-06.05 | `f.mission` | `{text, primary_objective, aligned_categories[], contradicted_categories[], authored_at, prior}` | polity | PH-10 (mission shift) | `faction_behavior §3.1` |
| P-06.06 | `f.role` | `∈ {sovereign, ecclesiastical, mercantile_procedural, intelligence_diplomatic, reformist, military_order, administrative, commercial, stewardship, occupying}` | Fixed | — | `faction_behavior §3.3.1` ◆ four added roles for institutions |
| P-06.07 | `f.leader`, `f.cascade_roots[]`, `f.institutional_culture` (−0.2..+0.2) | refs, real | polity | SET-10 | `faction_behavior §2, §3.2` |
| P-06.08 | `f.offices[]` | `{id, holder: NpcId?, competence 0–3, corruption 0–3, funded: bool}` — Crown Ministries, Hafenmark Committees, Church Dicasteries, Varfell Councils (readiness folds into competence) | polity | commit | `faction_politics Part 7`; `institutions › Four Cardinals` |
| P-06.09 | `f.rdt`, `f.td` (Hafenmark) 0–5; `f.deniability_debt` (Löwenritter) 0–7; `f.awareness` 0–7; `f.mass_seizure_used` (Church) bool | Clamped / bool | polity | commit | `tracks › RDT/TD`; `faction_politics §2.2b`; `southernmost › Awareness`; `ci_seizure` |
| P-06.10 | `f.posture` | Fixed rows `{priority, when: Predicate, then: ActionTemplate[]}` | data | — | `ci_political §6`; `ministry › Priority Tree`; `settlement_layer §3.2` (NPC governor) |
| P-06.11 | `f.seed` | Fixed authored `{L, PS}` used to seed settlements | data | — | `core › L + PS Starting Values` |
| P-06.12 | `f.succession_stat` | Fixed ∈ stats ∪ {Mandate} | data | — | `faction_succession_split §2.2` ◆ authored per polity |
| P-06.13 | `f.capital` | ProvinceId? | polity | SET-10 | `geography › Starting Control` |

**Derivatives**

| ID | Derivative | Expression | Lineage |
|---|---|---|---|
| D-06.01 | Capabilities | `can_play_cards ⇔ status ∈ {national, city_state, insurgency, foreign}` (movement: Praetor/Pontifex only); `parliamentary ⇔ status = national ∧ ¬extra_parliamentary`; `can_treaty_formal ⇔ parliamentary`; `can_hold_province ⇔ status ∉ {institution}`; `victory_eligible ⇔ status ∈ {national}` (promoted insurgencies included) | `insurgency §4.3, §5.3`; `settlement_layer §6.3`; `core › Restoration Movement` |
| D-06.02 | Income (display) | `Treasury = Σ_{s: ctl=f} Prosperity_s × 50`; Year-End: `Wealth +1` per province with `Σ Prosperity ≥ 3·|members|` (◆ scales the P-22 rule to settlement grain) | `settlement_layer §1.3`; `strategic_layer › P-22` |
| D-06.03 | Unit cap | `count(units of f) ≤ Military`; excess removed at commit | `strategic_layer › P-18` |
| D-06.04 | Effective convictions | `eff(n) = α(n)·personal(n) + (1 − α(n))·eff(supervisor(n))`, `α = clamp(0.4 + lerp(−0.2, +0.4, (Standing−1)/6) + institutional_culture, 0, 1)`; orphans `α = 1`; roots `eff = personal` | `faction_behavior §3.2` |
| D-06.05 | Aggregate convictions | `normalize(Σ_n Standing_n · eff(n))`, per root then root-weighted mean | `faction_behavior §3.2.6` |
| D-06.06 | Cascade fidelity | `cos(aggregate, role_template(role))`, 0 for zero vectors | `faction_behavior §3.3.2` |
| D-06.07 | Strictness | `clamp(0.4 + 0.5·aggL/7 − 0.3·aggPS/7, 0, 1)` | `faction_behavior §3.6` |
| D-06.08 | Mission alignment of an action | `−1` if `action.category ∈ aligned`, `+1` if `∈ contradicted`, else 0 | `faction_behavior §3.1` |
| D-06.09 | Cascade alignment of an action | `c = cos(action.conviction_profile, aggregate)`; `c ≥ 0.3 → −1; c ≤ −0.3 → +1; else 0` | ◆ (`faction_behavior §3.7` named it, did not define it) |
| D-06.10 | Expectation alignment | `dev = round(2·(1 − fidelity)) ∈ {0,1,2}`; modifier `= sign(−cos(action.profile, role_template))·strictness·dev`, rounded (`≥ 0.5 → 1, ≥ 1.5 → 2`) | ◆ distance metric |
| D-06.11 | Attributed outcome | `mean over f's action degrees this season of score{OW +1, S +½, P 0, F −1} × align{aligned +1, neutral 0, contradicted −1} × (1 − 0.5·max(0, leader.self_other))`; 0 if no actions | ◆ aggregation |
| D-06.12 | ΔPS (per controlled settlement) | `α_eff·attributed + β_eff·fidelity·gate + shock`, `gate = 0.5 if attributed < 0 else 1`, `shock = 0.5·tri(−1,0,1) if a card targeted f this season else 0`; rounded to int, clipped ±1 | `faction_behavior §3.4` ◆ shock |
| D-06.13 | ΔL (per controlled settlement) | `0.05·seasons_in_role + 0.3·procedural − 0.6·violation + 0.1·fidelity`, rounded, clipped ±1; procedural/violation scores from the event tables of `§3.5.1–2` | `faction_behavior §3.5` |
| D-06.14 | Posture choice | first row whose `when` holds; the row's `then` templates are instantiated against the best target by the template's `target_rank` expression; ties by stable key | `ci_political §6.1` |
| D-06.15 | Fog display | `{1: ruins, 2–3: poor, 4–5: good, 6–7: excellent}` for other polities; own Intel visible to owner (◆ fixes `strategic_layer §9.2`) | `strategic_layer §9.2` |
| D-06.16 | City-state sheet | same stats; `Mandate` derives from its settlements; `can_play_cards` limited to Consul/Senator/Recess | `settlement_layer §6.3` |

**Pipelines**

**PL-06.01 Polity season.** `PH-03: posture → ActionInstances (players choose instead)` → `PH-05/06: resolve` → `PH-07: commit with ±2 clip` → `PH-11: Stability check if tally ≥ 2 (D-02.07); Consolidation recovery +1 Stability if no stat fell this season ∧ Stability < 5 (◆ the absent §1.3 rule, kept minimal); cooldowns −1; mission-failure counter (4 consecutive contradicted seasons → mission shift)`.

**PL-06.02 Cascade re-resolution.** Trigger: PH-11 each season, or immediately on `succession` events. `new_agg := D-06.05; agg := agg + 0.6·(new_agg − agg)` (damping), except roots with `leader.scars ≥ 3` (no damping). Actions in a season read the previous season's `agg`.

**PL-06.03 Mission shift.** Trigger (any): victory-score crossed ≥ 11 or fell below 5 for the first time; `succession.mode ∈ {contested, emergency, imposed}`; mission-failure counter ≥ 4; authored scenario trigger. Effect: `mission := authored successor(mission, trigger)`; emit `mission.shifted`; procedural +0.5 if authored.

**PL-06.04 Emergence & collapse (status machine).** `movement --controls 2+ settlements--> organisation --4+ settlements over 2 provinces ∨ holds a Seat; Declaration ActionDef (strength ⌊Renown/2⌋ or Influence, difficulty D(3)) S--> national --controls 2+ Seats--> hegemon (label only)`. `national --loses last province ∧ leader alive ∧ leader.at ∈ controlled settlements--> city_state --regains a Seat--> national`. `any --Stability = 0 at PH-12--> eliminated` (units Masterless, claimable; provinces → Vacuum). Founded national sheet: `L 2, PS 3, Influence ⌊Renown/2⌋, Wealth 2 + settlements − 1 (cap 5), Military 1, Intel 2, Stability 3` (`settlement_layer › ED-790`).

**PL-06.05 Office.** `funded (competence +1/2 seasons, cap 3) | unfunded (competence −1/season) ; corruption +1 on Corrupt-Ministry success, −1 on audit; holder death → vacant → suspended effects until Year-End appointment`. Church arms: `competence(Defense) low → Jarnstal Independence card weight ×2` etc. (SET-12).

**Transitions out of SET-06.** Stats → SET-01 strengths; posture → SET-04 directives, SET-11 duties, SET-03 marches; status → SET-09 (parliamentary), SET-12 (victory eligibility); Mission/cascade → SET-01 identity modifier; collapse → SET-05 Vacuum, SET-10 insurgency substrate.

---

### SET-07 — Peninsula Clocks & Environment

```
 w.MS ──band──▶ radiation table × p.proximity ──▶ advantage rows on actions in p (downward pressure)
 w.CI ──seven-step formula ◀── Prominence, PT, SW, charity, Templars, Assert, Suppress, Baralta
 w.IP ──▶ 75 Vanguard · 100/85/80 invasion phases ──▶ Governorate polity · occupied provinces
 w.PI ──bands──▶ Crown Policy gate, Manoeuvre difficulty, 20 = Deposition
 w.Turmoil ──bands──▶ Stability checks, Accord decay, Accord cap
 WC · WR · Torben · Elske · Generational Shift · expedition · awareness
```

**Primitives**

| ID | Primitive | Type / domain | Start | Writer | Lineage |
|---|---|---|---|---|---|
| P-07.01 | `w.MS` | `Clamped<0,100>` (+ fraction accumulator) | 72 | PH-09 | `core › Starting Values`; `campaign_architecture §3.1` |
| P-07.02 | `w.CI` | `Clamped<0,100>` (+ fraction accumulator `ci_frac`) | 28 | PH-09 | `ci_seizure`; `ci_political §2` |
| P-07.03 | `w.IP` | `Clamped<0,100>`; `invasion_phase ∈ {0,1,2,3}`; `repelled: bool`; `freeze_until` | 20 | PH-09, PH-10 | `core`; `campaign_architecture §5` |
| P-07.04 | `w.PI` | `Clamped<0,20>` | 7 | PH-09 | `parliament › PI Scale` |
| P-07.05 | `w.Turmoil` | `Clamped<0,10>` (absorbs Public Instability) | 0 | PH-09 | `tracks › Turmoil`; `stats › PP-255` ◆ fold |
| P-07.06 | `w.WC` 0–3, `w.WR` 0–4, `w.wr_ever_past_1`, `w.wr_returned_to_0` | Clamped, bools | 0, 0 | PH-10 | `core › WC/WR`; `geography › WR track` |
| P-07.07 | `w.torben_loyalty`, `w.elske_loyalty` | `Clamped<0,7>` | 7, 4 | PH-09/PH-12 | `core › Starting Values` |
| P-07.08 | `w.generational_shift` | `Clamped<0,10>` | 0 | PH-12 (Year-End: `+1` every 5th year) | `settlement_layer §7.1` |
| P-07.09 | `w.warden_emergence`, `w.edeyja_contact` | bool | false | PH-10 | `geography › Forgetting Check` |
| P-07.10 | `w.band_crossings[]` this season | list of `(clock, from_band, to_band)` | — | PH-09 | `phases` step 8 |
| P-07.11 | `w.milestones_fired` | set of CI milestones reached | ∅ | PH-09 | `ci_political §2.1` |

**Derivatives**

| ID | Derivative | Expression | Lineage |
|---|---|---|---|
| D-07.01 | MS band | `100–73 Restored · 72–60 Quiet Anomalies · 59–40 Observable · 39–20 Peninsula-wide · 19–1 Undeniable · 0 Rupture` | `campaign_architecture §4.2`; reconciliation (rebased) |
| D-07.02 | ΔMS per season | `−count(battles) − [year_end] − count(thread_debt tokens with age > 1 ∧ ¬serviced) − 0.5·count(serviced tokens, once) + Σ Mending(tier(Spirit), degree) + 2·[WC = 3] − [Turmoil ≥ 9] − 0.5·harvests`; decay terms halved when `WC ≥ 2`; fractions carried | `campaign_architecture §3.1, §3.3`; `phases` step 6; `core › WC Effects`; `tracks › Turmoil` |
| D-07.03 | Mending tiers | Spirit `1–2: S +1 / OW +2`; `3–4: +1 / +3`; `5: +2 / +4`; `6: +2 / +5` | `campaign_architecture §3.3` |
| D-07.04 | ΔCI per season (ordered) | (1) `+1` if `count(p: Prominent) ≥ 2`; (2) `+Σ_{p Prominent} tier(PT_p)·SW_p/5` with `tier = {0:0, 1:0, 2:0.1, 3:0.25, 4:0.5, 5:1.0}`, floored after adding `ci_frac`; (3) `+min(2, ⌊charity_wealth/2⌋)`; (4) `+count(p: Templar unit ∧ Prominent)`; (5) Assert `S → +1`; (6) Suppress `S → cancel (1)`; (7) `−1` while `Hafenmark.Mandate ≥ 4` (`−1` also at RDT ≥ 4 while `≥ 3`); `+1` per season at Himmelenger controlled by Church; caps `±5` total, `±3` from action-sourced | `ci_seizure › CI Generation`; `geography › T9`; ◆ tier and floor-after-sum |
| D-07.05 | CI milestones | `40 Assertive (+1 point on Assert/Seizure); 55 Institutional Reach (+2 difficulty points on actions opposing Church); 65 Dominant (anti-Church motions cost two card slots); 80 Ascendant (seizure −2 difficulty points; PT +1 drift at Year-End unless WC ≥ 2); 100 Unification (Mass Seizure mandatory if unused)` | `ci_political §2.1–2.2` |
| D-07.06 | CI weight | `⌊CI/20⌋` points for Church in political checks; opponents of a Church-subject motion `−⌊CI/30⌋` votes floored 0 | `ci_political §3.2–3.4` |
| D-07.07 | ΔIP per season | `+⌊count(p: controllable ∧ Accord ≤ 1)/3⌋ + 2·[Crown.Stability ≤ 2] + [torben_loyalty ≤ 3] + count(occupied provinces) − [IP > 20 ∧ count(Accord ≤ 1) = 0] + Σ card deltas`; 0 while `repelled` | ◆ (the corpus's table is absent; ED-743 asks for Accord-count advancement) |
| D-07.08 | IP effects | `< 30: Schoenland trade +1; 30–59: Schoenland trade +2 difficulty, Intel +1 point; 60–74: trade +4 difficulty; ≥ 75: Vanguard (PL-03.05); ≥ 90: NW pass event` | `clocks › IP Effects`; `geography › Passes` |
| D-07.09 | PI bands | `≤2 Non-functional (no Manoeuvre; Crown by decree; CI +2 once on entry) · 3–4 Degraded (Manoeuvre +2 difficulty; Decree difficulty 1) · 5–7 Standard · 8–10 Full (Crown Policy needs Mandate ≥ 4) · 11–14 Ascendant (Policy needs Mandate ≥ 5; Manoeuvre −2 difficulty) · 15–19 Supreme (Royal Decree unavailable; No-Confidence needs no Church concurrence) · 20 Deposition (PL-10.06 with Crown excluded)` | `parliament › PI Scale`; ◆ 11–20 |
| D-07.10 | ΔPI per season | `+1 Manoeuvre S; +1 Crown Parliamentary Session policy; +1 Year-End Legislative Record (first Manoeuvre S in year); +1 Ministry posture row; −1 per season Emergency Powers held (Ministry presence at Valorsplatz prevents one); −1 per Church seizure success; −3 Coup; cap +2 up per season` | `parliament`; `ministry` |
| D-07.11 | ΔTurmoil | `+1 [any battle] +2·eliminations +1·revolts +1 [PI ≥ 8 revolt check season] −1 [∀ controllable p: Accord ≥ 2] −1 [diplomatic resolution this season] (max one)` | `tracks › Turmoil`; `phases` 4d |
| D-07.12 | Turmoil bands | `0–2 Peace · 3–4 Tension (all polities: stability_check difficulty 1; F → L −1 in one settlement) · 5–6 Fracture (Order −1 in lowest-Accord province's seat) · 7–8 Crisis (Order −1 in all non-capital seats; check difficulty D(2)) · 9–10 Collapse (Order cap 3 outside capitals; check D(3); MS −1)` | `tracks › Turmoil` (Accord effects mapped onto Order) |
| D-07.13 | Loyalty Year-End | Torben: `+1 [PI ≥ 5] +1 [Crown Mandate ≥ 4 for 2 seasons] +1 [Löwenritter Autonomy ∈ {Loyal, Restless} ∧ ¬Emergency Powers] −1 [torben in Altonia]`; Elske: `+1 [Crown Senator Outward S toward Altonia this year] −1 [IP rose ≥ 10 this year]` (◆ the absent step-5 content) | `phases › Year-End` |
| D-07.14 | Generational Shift effects | `2: original leaders' highest stat −1 (exempt TS ≥ 50); 4: −2 and retirement arcs; 6: −3` | `settlement_layer §7.1` |
| D-07.15 | TT | `100 − MS` (Thread Tension is not stored) | ◆ |

**Pipelines**

**PL-07.01 Clock update (PH-09).** In order: Turmoil (D-07.11) → CI (D-07.04) → IP (D-07.07) → PI (D-07.10) → MS (D-07.02) → compute band crossings → milestone entries. Each clock is one path with one cap set; band crossing emits `clock.band_crossed(clock, from, to)`.

**PL-07.02 Invasion.** `phase 0 --IP ≥ 100--> phase 1: Governorate polity (status foreign; Mandate seed 2/Military 4/Stability 3) occupies the NE-pass province; actions there +2 difficulty; IP decay begins --IP ≥ 85 for 3 seasons--> phase 2: + two provinces along the sea corridor via Schoenland; spawn Insurgency 'Underground Network' in occupied provinces (PL-10.04 with sponsor = the pre-occupation controller) --IP ≥ 80 for 3 more--> phase 3: NW corridor; +4 difficulty in occupied provinces`. Retreats: `IP < 85 → phase max 1; IP < 75 → 0 phases beyond 1; IP < 60 → withdrawal`. Repulsion (any, then `repelled := true`): two consecutive OW assaults vs Governorate units → IP := 60, ceiling 80 for 10 seasons; `elske_loyalty ≥ 6 ∧ social contest vs Vanguard commander S ∧ IP < 80` → IP := 40 (OW: 20 + 20-season non-aggression); Underground Network `Mandate ≥ 3 ∧ Accord = 0 in all occupied ∧ assault S` → IP := 30.

**PL-07.03 Warden tracks (PH-10).** `WR += 1` per Expedition season with degree ≥ S (OW counts 2, cap 4); `WR −2` on Latent RM emergence (SET-10); `WR −1` if no expedition attempted for 3 seasons and `WR ≥ 1`; `wr_returned_to_0 := true` if `WR` hits 0 after `wr_ever_past_1`; `WC` advances only if `WR ≥ 2`: `+1` per Expedition S/OW season (cap 3); WC effects `≥1: +1 point on Thread ops; ≥2: MS decay halved; 3: MS +2/season`.

**PL-07.04 Radiation & Surge.** Each PH-01 the snapshot carries `radiation_row(p) = table[band(MS)][proximity(p)]`, read by SET-01 as advantage rows (e.g. `+2 difficulty points on non-Thread actions` at Proximity 0 in band 79–60 → rebased 72–60). `MS ≤ 10` once: every province with `proximity ≤ 2` uses the next-worse band for one season.

**Transitions out of SET-07.** MS band → SET-12 (revelation scenes), SET-03 (radiation advantages); CI → SET-08 (seizure availability), SET-09 (votes), SET-11 (rank effects); IP → SET-03 (Vanguard), SET-10 (Underground Network); PI → SET-09; Turmoil → SET-04 (Order), SET-06 (stability checks); Loyalties → SET-10 (Torben triggers); Generational Shift → SET-06/SET-11.

---

### SET-08 — Church & Piety

```
 s.PT (per settlement) ─floor-mean─▶ p.PT ─×SW/5─▶ Piety Yield ─▶ w.CI
 s.church.{building, templar, inquisitor} + governor=Church ──▶ infra_mod(s) ≤ 4 ──Σ, cap 6──▶ seizure difficulty
 Prominence(Church,p) ◀── Mandate comparison (SET-05)
 actions: Assert · Suppress · Bishop Appointment · Pastoral Assumption · Build (Chapel→Church→Cathedral) · Templar Station · Inquisitor Base
          · Heresy Investigation · Excommunication · Mass Seizure (one-shot) · Reformed Settlement (Hafenmark) · Cultural Reclamation (Varfell)
```

**Primitives** (beyond the settlement-owned axes in SET-04)

| ID | Primitive | Type / domain | Owner | Writer | Lineage |
|---|---|---|---|---|---|
| P-08.01 | Cardinal offices | four `Office` rows `{Fortitude, Justice, Prudence, Temperance}` with holder NPC, competence, corruption, `suspended_until` | Church polity | commit | `institutions › Four Cardinals`; `worldbuilding §3` |
| P-08.02 | Inquisitor placements | per province: `count ∈ {0,1,2}` (derived each PH-11 from Attention, then stored as placement) | province | PH-11 | `tracks › Church Attention Pool` |
| P-08.03 | Heresy Investigations | `{target: NpcId|PolityId, province, opened, closes_by, degree?}` | Church polity | commit | ◆ (referenced everywhere, defined nowhere) |
| P-08.04 | Excommunication | `{target, penance_remaining 3, banished: bool}` | rel ledger | commit | `institutions › Excommunication` |
| P-08.05 | `w.mass_seizure` | `{declared_season?, targets[], results{p → degree}, failed: bool}` | world | PH-06/PH-12 | `ci_seizure`; `campaign_architecture §1.3` |

**Derivatives**

| ID | Derivative | Expression | Lineage |
|---|---|---|---|
| D-08.01 | Infra modifier | `infra(s) = min(4, {none 0, chapel 0, church 1, cathedral 2}[building] + [templar] + [inquisitor] + 2·[governor = Church])`; `infra(p) = min(6, Σ_s infra(s))` | `campaign_architecture §1.2`; `settlement_layer §1.5` |
| D-08.02 | Seizure difficulty | `D(max(1, 10 − PT_p − infra(p)))` (D-01.02); strength `Influence + ⌊CI/15⌋` `+1` at CI ≥ 40, `+2` at CI ≥ 80 | `ci_seizure › Mass Seizure` |
| D-08.03 | Seizure availability | `CI ≥ 60 ∧ ¬mass_seizure_used ∧ Mandate(Church) ≥ 4`; AI declares with `P = clamp(((CI − 60)/40)^3.3, 0, 1)` from the stream; mandatory at CI 100 | `ci_seizure`; `ci_political §2.2` |
| D-08.04 | Seizure targets | `{p : ∃ s ∈ p: building ≥ chapel} ∖ {Askeheim, Schoenland} ∖ {p: Prominent = false}` | `ci_seizure › Constraints`; `campaign_architecture §1.3` |
| D-08.05 | Attention sources (per province per season) | `+1 per RM Community Organizing here; +2 per Thread op revealed; +1 per Investigate targeting Church here; +1 per Private Collection use (at CI ≥ 65); +1 per Survey failure at depth ≥ 3; +1/season if inquisitor ∧ presence[RM] ≥ 1` | `tracks › Attention`; `core › Survey`; `faction_politics §5.3`; `settlement_layer §1.5` |
| D-08.06 | Inquisitor placement | `attention ≥ 6 → 2; ≥ 3 → 1; else 0`; Organizing S in a province `attention −2` and expels one if below threshold | `tracks › Church Attention Pool (PP-185)` |
| D-08.07 | PT drift per season (per settlement) | `+½ chapel, +1 church, +2 cathedral (+½ to settlements in adjacent provinces), −1 RM Organizing S, −1 Cultural Reclamation S, −1 Stage-1 decay draw, +1 seizure OW (exempt from cap), +1 at Year-End if CI ≥ 80 ∧ WC < 2`; action-sourced `±1/season` cap; Parish floor 1, Cathedral floor 2 | `campaign_architecture §1.1`; `institutions › Parish/Cathedral`; `ci_seizure › Results`; `insurgency §2` |
| D-08.08 | Tithe | `Wealth +½ per season per province where Prominent ∧ ∃ building ≥ church` (fraction carried; halved while Prudence suspended) | `institutions › Prudence` ◆ Favour → Prominence |
| D-08.09 | Excommunication difficulty | contested vs leader: `Mandate − target.Mandate`; else `Mandate − 2`; `+2` L-cost to Church at RDT 5 | `stats › Excommunication`; `tracks › RDT 5` |
| D-08.10 | Reformed Settlement eligible | `Hafenmark controls a province with a Church building ∧ Hafenmark.Mandate ≥ 3 ∧ PI ≥ 4 ∧ once per arc` | `tracks › RDT` |
| D-08.11 | Schism selection | Cardinal with lowest `competence`; tie → lowest `disposition(holder, Confessor)` | ◆ (`institutions › Cardinal schism trigger`) |

**Pipelines**

**PL-08.01 CI season.** Inside PH-09 as D-07.04; Assert/Suppress are PH-06 actions whose results are read here.

**PL-08.02 Church building.** ◆ `institutions › Parish / Cathedral` (2 and 5 Consul successes) unified with the four-axis ladder of `campaign_architecture §1.1`: `none → chapel (1 Consul Inward S) → church (2 more S, Wealth 1; PT floor 1) → cathedral (3 more S, Wealth 2; PT floor 2, Order floor 1)`; one upgrade attempt per settlement per arc; on control transfer a cathedral degrades to church, church and chapel survive; destroyed only by an assault OW.

**PL-08.03 Bishop Appointment.** ActionDef `ecclesiastical_appointment` (Consul Outward, strength Influence, difficulty D(1), prerequisite D-04.08, no CB). `S → s.governor := Church, s.controller := Church` (administrative class → Order pin 2 unless `PT_s ≤ 2`, then Order −1 ◆), PL-05.01 fires, the province fractionalises. Pastoral Assumption is the same row with prerequisite D-04.09.

**PL-08.04 Mass Seizure.** `available --declared (PH-03; one-shot)--> emergency season (all other polities get one free Senator-class motion; mandatory slate scene) --next PH-06, tier 6--> per target p: if garrison(seat) ≠ ∅: assault first (PL-03.02) → on win, seizure check (D-08.02): S/OW → ctl(seat) := Church (Order pin: 1, or 2 if PT_p ≥ 3), OW → PT +1; F → Stability −1; every attempt → CB(ctl(p) → Church), −1 PI per success --PH-12--> failed := Church lost 3 provinces in one year ∨ Mandate(Church) ≤ 3 (no second attempt either way)`.

**PL-08.05 Heresy Investigation.** Prerequisite `attention(p) ≥ 3 ∧ Justice office not suspended`. ActionDef (Tribune-class for Church): strength `Intel`, difficulty from Ob 2 (`+2` if Ministry of Law agenda active), contested vs target's concealment if an NPC/PC. `S → target Standing −2 (or polity Regard −1 from all, Exposure +2); OW → Excommunication offered; F → attention −2, CI −1`. A compromised Justice office (Varfell Intel OW vs Church) flags one investigation this season invalid.

**PL-08.06 Reformed Settlement (Hafenmark).** ActionDef (Diplomat): `S → rdt +1 (max once/arc)`; Church response is an auto posture row: `Resist (CI +3, td +1 if rdt ≥ 2) | Accommodate (td frozen) | Ignore`; TD effects per `tracks › TD` (`5: Gransol unseizable`); TD 2 "schism risk" = Cardinal Independence check (difficulty D(3)) each season `Church.Stability < 3` → Jarnstal Independence card.

**Transitions out of SET-08.** CI ← SET-05 Prominence, SET-04 PT/buildings; seizure/appointment → SET-05 control, SET-09 CB; Inquisitors → SET-04 (RM +2 difficulty), SET-11 (Concealment tests); Excommunication → SET-04 (L −1 in target settlements), SET-11 (Standing −1 dismissal).

---

### SET-09 — Diplomacy & Parliament

```
 rel.regard[a][b] (−3..+3) ──▶ vote side · treaty strength · succession backing · pledge witnesses
 rel.cb[] {holder→target, source, mode_class, expires} ──consumed by──▶ Parliamentary Transfer · war entry · seizure
 rel.treaties[] {a,b,kind,bound} ──arc-boundary lapse 0.90──▶ void · violation ──▶ CB + regard
 Parliament: tally(votes) ──▶ motion outcome ──wraps──▶ kernel check (Transfer, Censure, No-Confidence)
 Crown Policy ──▶ Hafenmark Opposition (Manoeuvre) ──▶ Ministry countersignature ──▶ in force
```

**Primitives**

| ID | Primitive | Type / domain | Owner | Writer | Lineage |
|---|---|---|---|---|---|
| P-09.01 | `rel.regard[a][b]` | `Clamped<−3,+3>` directed, per ordered polity pair; `regard[Varfell][RM]` doubles as Warden's Accord | world | commit | ◆ unifies Standing tokens (`parliament › Open Pledge`, `institutions › Royal Deposition`), treaty-violation Standing (`treaty_expiration §3`), WA (`insurgency §3.1`) |
| P-09.02 | `rel.cb[]` | `{holder, target, source ∈ {trespass, military, adjacent_instability, transfer_partial, treaty_violation, excommunication, scar_threshold, seizure_attempt, pledge_breach, crown_restoration, einhir_partial}, mode_class ⊆ {adversarial, consensual, punishment, appeasement}, created, expires = created + 3}` | world | commit | `parliamentary_transfer §3`; `parliament › PP-515, PP-523`; `ci_seizure › Political cost` ◆ 3-season default |
| P-09.03 | `rel.treaties[]` | `{a, b, kind ∈ {formal, non_aggression, sovereignty, reunification}, bound_season, guarantor?}` | world | commit | `treaty_expiration §1`; `core › Formal Crown Treaty`; `faction_succession_split §2.5` |
| P-09.04 | `rel.pledges[]` | `{polity, visibility ∈ {open, closed}, commitment: {do: tag|abstain: tag|in: ProvinceId}, season, witnesses[], breached?}` | world | PH-03, PH-11 | `parliament › Open Pledge System` |
| P-09.05 | `w.crown_policy` | `{kind ∈ {emergency, session, taxation, trade, martial, ∅}, since, opposed?, countersigned?}` | world | PH-06 | `parliament › Crown Policy Instrument`; `strategic_layer › PP-036` ◆ Emergency Powers as a kind |
| P-09.06 | `w.alignment` | `{season, Church ∧ Hafenmark same side}` declared once per season | world | PH-03 | `parliament › Diplomatic Alignment` |
| P-09.07 | Motion | `{proposer, kind ∈ {transfer, censure, embargo, outlawry, no_confidence, nomination, stay}, subject, mode, cb_ref?, votes{f → (side, n)}, result}` | world (this season) | PH-06 | `parliamentary_transfer §4`; `ci_political §3.3`; `worldbuilding §6.2` |
| P-09.08 | `f.parliamentary_manoeuvre_used`, `f.transfer_used_this_arc` | bools | polity | commit | `parliamentary_transfer §1.1` |

**Derivatives**

| ID | Derivative | Expression | Lineage |
|---|---|---|---|
| D-09.01 | Votes cast | `n(f) = Mandate(f) + [f = Church]·⌊CI/20⌋ − [motion.subject = Church ∧ side(f) = against]·⌊CI/30⌋`, floored 0; only `parliamentary(f)` | `ci_political §3.4` |
| D-09.02 | Vote side | `d = regard[f][proposer] − regard[f][holder]; d ≥ 1 → for; d ≤ −1 → against; 0 → abstain`; `f ∈ {proposer, holder}` vote their own side; alignment forces Church/Hafenmark to the same side (the higher-Mandate one's) | ◆ (`parliamentary_transfer §4` "blocs") |
| D-09.03 | Majority | `for > against → +1 point to proposer; against > for → −1; else 0` | `parliamentary_transfer §4` |
| D-09.04 | Transfer check | strength `proposer.Influence + D-09.03 + [Church]⌊CI/20⌋`, difficulty `holder.aggregate_L + 2` | `parliamentary_transfer §1.1` |
| D-09.05 | Transfer protections | `¬(holder controls exactly one province) ∧ target ≠ proposer's ∧ parliamentary(proposer) ∧ ∃ cb(proposer → holder) with mode_class ∋ mode ∧ ¬transfer_used_this_arc` | `parliamentary_transfer §1.3` |
| D-09.06 | CB source predicates | `adjacent_instability: at arc boundary, Accord(p) ≤ 1 ∧ q adjacent to p ∧ ctl(q) ≠ ctl(p) → cb(ctl(q) → ctl(p))`; `crown_restoration: Crown controls < 6 provinces (refresh per arc)`; `consensual: regard[a][b] ≥ 2 ∧ regard[b][a] ≥ 2`; `appeasement: Turmoil ≥ 7 ∨ insurgency in holder's provinces ∨ (holder.Military ≥ 5 ∧ ∃ holder unit adjacent to proposer's province)`; `punishment: excommunication ∨ treaty_violation ∨ leader.scars ≥ 3` | `parliamentary_transfer §2–3` ◆ predicates |
| D-09.07 | Treaty lapse | at arc boundary, per treaty: `u ~ stream; u < 0.90 → void` (memoryless) | `treaty_expiration §1.1` |
| D-09.08 | Re-binding | Senator Outward: `Wealth −2`; strength `Influence + regard[target][actor]`; difficulty `target.Stability`; `OW → bound + regard[target][actor] +1; S → bound; P → cb-block 1 arc; F → regard −1` | `treaty_expiration §2` ◆ pool |
| D-09.09 | Violation | `treaty(a,b) ∧ (a assaults b's settlement ∨ a initiates Transfer vs b ∨ a grants cb to a third party vs b) → void; cb(b → a, treaty_violation); regard[·][a] −2 ∀; regard[·][b] +1 ∀` | `treaty_expiration §3` |
| D-09.10 | Crown-break | as violation with the corpus timing: dissolution at PH-03; `Crown.Stability −2, L −1 in Crown settlements` at commit; cb at PH-11; usable next season | `parliament › PP-523, PP-525` |
| D-09.11 | Pledge breach | `open: commitment = abstain(tag) ∧ ∃ declared action with tag → breached` unless `exempt = ∃ hostile unit entered commitment.in this season ∧ ¬adjacent at PH-01`; honoured → `regard[w][polity] +1 ∀ witnesses`; breached → `Stability −1, cb(w → polity) ∀ witnesses`; closed pledge revealed at any PH-11 by the injured party → same plus `PI −1` | `parliament › PP-515, PP-527` ◆ exemption predicate |
| D-09.12 | Manoeuvre | Hafenmark Senator: contested `Influence` vs `Crown.Influence` (`−2` points at Ministry presence ≥ 1 at Valorsplatz; `+2` if absent; PI band shifts) → `S: PI +1 and cancel one Crown Policy of this season or pass one pending motion`; free interrupt only against the Policy Instrument | `core › Parliamentary Manoeuvre`; `ministry`; `strategic_layer › P-19` |
| D-09.13 | Policy availability | `Mandate(Crown) ≥ {4 at PI ≤ 10, 5 at PI ≥ 11}`; unavailable at PI ≥ 15 (Decree) ; `Ministry.aggregate_L < 2 → +2 difficulty; = 0 → unavailable`; same kind not two seasons running | `parliament`; `ministry`; D-07.09 |
| D-09.14 | Deposition condition | `PI ≥ 5 ∧ Mandate(Church) ≥ 5 ∧ Mandate(Crown) ≤ 1 ∧ count(f: regard[f][Crown] ≤ −2) ≥ 2` or `PI = 20` | `institutions › Royal Deposition` |
| D-09.15 | No-Confidence | vote (D-09.01–03) with Crown as holder; passes → Confessor concurrence: `concur ⇔ regard[Church][Crown] ≤ −1 ∨ CI ≥ 65` (◆); concur → PL-10.06 with Crown excluded; refuse → `CI +3, MS −2` | `worldbuilding §6.2` ◆ concurrence predicate |
| D-09.16 | Nomination agenda | at Year-End if `Manoeuvre S this year ∧ crown_policy.kind ≠ emergency`: Hafenmark picks `Law | Guilds | Logothetes` with the listed effects; Crown confirms automatically at `Mandate ≥ 3`, else check `Mandate` vs D(2) | `institutions › Parliament Nomination` |

**Pipelines**

**PL-09.01 Treaty.** `proposed (Senator Outward / treaty positioning: contested Influence vs Influence; S → proposer sets terms) → ratification (Mandate vs D(2), +1 with guarantor, Church +⌊CI/20⌋) → bound --arc boundary: D-09.07--> void | --D-09.09--> violated → void`. A `sovereignty` treaty transfers the junior party's victory share to the senior (SET-12 D-12.08) and forbids the senior's Transfer against the junior.

**PL-09.02 Casus Belli.** `created --used (Transfer, assault into target's province, seizure)--> consumed | --season ≥ expires--> expired`. Sources are evaluated at PH-11 (event-driven) and at arc boundary (adjacent instability, crown restoration).

**PL-09.03 Motion.** `declared (PH-03, Senator-class; extra-parliamentary excluded) → PH-06 tier 4: votes (D-09.01–02) → majority (D-09.03) → kernel check where the motion has one (Transfer D-09.04; Censure: proposer Influence vs holder aggregate_L → S: L −1 in holder settlements; Outlawry: same vs +2 → S: L −2; Embargo: S → holder Wealth −2/season for 1 arc) → Stay may be invoked by any parliamentary polity (Senator card) → suspended until a treaty, Crown Session or the arc ends`. Transfer outcomes: `OW → ctl(seat_p) := proposer, holder L −1 (settlements), Order pin 1; S → transfer, Order pin 1 (Appeasement mode: 2); P → cb(proposer → holder, transfer_partial); F → proposer Stability −1, holder L +1 (Punishment mode: instead holder regard −1 from all)`.

**PL-09.04 Crown Policy.** `declared (PH-03; D-09.13) → PH-06 tier 4: Hafenmark may Manoeuvre as interrupt (no card) → Ministry countersign (auto: Ministry.aggregate_L ≥ 2) → in force this season; Emergency Powers: PI −1 per season (Ministry presence at Valorsplatz ≥ 1 prevents one per season), all Crown Domain Actions −2 difficulty, Nomination suspended; Session: PI +1`.

**PL-09.05 Ministry as polity.** Posture rows (data): `1 PI ≤ 3 → Govern(Valorsplatz): S → PI +1` · `2 presence[Ministry](Valorsplatz) = 0 → establish presence` · `3 Church seizure pending in a province with presence ≥ 1 → delay it one season, presence −1` · `4 Mandate(Crown) ≥ 4 ∧ PI < 5 → Decree support: PI +1` · `5 Govern in the highest-Prosperity uncontested settlement with presence`. Corrupt Ministry: Consul Outward, contested `Influence` vs `Ministry.Influence`; `S → row 4 fires for the corruptor; OW → +2 points on the corruptor's actions in one chosen province for a season; F → Stability −1, tag(Grudge) on the Riskbreakers' NPC ambitions`. Collapse at `aggregate_L = 0`: two seasons inert, presence cleared, exit by Crown/Hafenmark Govern at Valorsplatz (difficulty D(2)).

**Transitions out of SET-09.** Transfer/seizure → SET-05 control; treaties → SET-12 victory share, SET-03 (permitted crossings); CB → SET-03 (war entry), SET-08 (seizure cost); Deposition/No-Confidence → SET-10; PI → SET-07; regard ← SET-11 (PC diplomacy scenes), SET-04 (levy grievances via Grudge tags on institutions).

---

### SET-10 — Succession, Split & Emergence

```
 leader lost ──▶ [sole heir ok?] ──yes──▶ smooth (Stability −1)
                        │no
                        ▼
              Succession Contest: contenders → strength → Stage 1 (who leads, kernel) → Stage 2 (gap G)
                        │ G ≥ 3 unified · G = 2 fractious (Disposition check) · G ≤ 1 split
                        ▼
              Split: assets 60/40 · 70/30 · units by Disposition+Discipline · provinces by proximity
 Löwenritter: Loyal ⇄ Restless ⇄ Autonomous ──▶ Split (irreversible) · Coup branch
 Insurgency: decay ─▶ Latent RM ─▶ Insurgency ─▶ Promoted (parliamentary | extra) ─▶ dissolve/persist
 Emergence: Cell ─▶ Organisation ─▶ Movement ─▶ National ─▶ Hegemon  ·  National ─▶ City-state ─▶ National
 Crown: Baralta stake · Consecration Crisis · Torben Generational Shift · Deposition
```

**Primitives**

| ID | Primitive | Type / domain | Owner | Writer | Lineage |
|---|---|---|---|---|---|
| P-10.01 | Autonomy instance | `{stage ∈ {Loyal, Restless, Autonomous, Split, Coup}, entered_season, seasons_since_crown_military, crown_lost_province_this_season}` | pipeline registry | PH-10 | `conflict_architecture › Graduated Löwenritter Autonomy`; `core` |
| P-10.02 | Succession contest | `{polity, opened, contenders[] {npc, claim ∈ {blood, inner_circle, institutional, external}, backer?, strength}, stage, leader?, outcome}` | pipeline registry | PH-10 | `faction_succession_split §2` |
| P-10.03 | Regency | `{polity, since, contests_without_winner}` | pipeline registry | PH-10 | `faction_succession_split §2.3` |
| P-10.04 | Insurgency record | a polity with `status = insurgency`, plus `{origin_provinces[], sponsor?, formed_season, parliamentary_flag?}` | polity | PH-10 | `insurgency §4–5` |
| P-10.05 | Latent RM | `{active: bool, since}` on the RM polity | polity | PH-10 | `insurgency §3` |
| P-10.06 | `w.torben` | `{readiness 0–10, matured: bool, in_altonia: bool}` ; `w.baralta_stake` `{active, season}` | world | PH-10/PH-11 | `faction_politics Part 8`; `baralta_crown_claim §2` |
| P-10.07 | Emergence stage | per movement/PC organisation: `∈ {cell, organisation, movement, national, hegemon}` (a view of `f.status` + counts; stored only as the declared flag) | polity | PH-10 | `settlement_layer §6.2` |
| P-10.08 | Reconstitution attempts | `{polity, attempts}` for city-state → national and Löwenritter PI = 0 | polity | commit | `institutions › Reconstitution`; `strategic_layer §9.10` |

**Derivatives**

| ID | Derivative | Expression | Lineage |
|---|---|---|---|
| D-10.01 | Leader lost | `leader = ∅ ∨ leader.dead ∨ (leader.captured ∧ seasons_captured ≥ 2) ∨ leader.deposed ∨ leader.incapacitated_permanent` | `faction_succession_split §2` |
| D-10.02 | Smooth succession | `∃ heir: heir.canonical ∧ disposition(heir, apparatus) ≥ +3 ∧ heir.Standing ≥ 4 ∧ ¬∃ other claimant with |Standing − heir.Standing| ≤ 1` | `faction_succession_split §2.1` ◆ "comparable" = within 1 |
| D-10.03 | Contender strength | `blood: Mandate(f) + Influence(f) + 2·[bloodline tier]; institutional: Influence(f) + f.stat[succession_stat]; external: backer.Influence + npc.Standing; inner_circle: Influence(f) + npc.Standing` (+2 for an active Baralta stake) | `faction_succession_split §2.2`; `baralta_crown_claim §2, §7.3` |
| D-10.04 | Gap | `G = strength(top1) − strength(top2)`; tie on strength → `top1` is the contender whose claim matches `f.succession_stat`'s domain (military stat → institutional military candidate, Mandate → blood/political), then stable key | `faction_succession_split §2.2–2.3` |
| D-10.05 | Autonomy predicates | `→Restless: Crown.Stability ≤ 3 ∨ seasons_since_crown_military ≥ 4 ∨ crown_lost_province`; `→Autonomous: Crown.Stability ≤ 2 ∨ disposition(Ehrenwall, Almud) < 0 ∨ seasons_in(Restless) ≥ 4`; `→Split: Crown assaults a Löwenritter-held settlement ∨ Crown eliminated ∨ seasons_in(Autonomous) ≥ 4`; `→Coup (from Autonomous): disposition(Ehrenwall, monarch) ≤ −2 ∧ ∃ candidate ∈ {Torben, Elske, a Duke with regard[Löwenritter][duke] ≥ 2}`; reverse one stage: `Crown.Stability ≥ 4 ∧ (Crown military action this season ∨ disposition(Ehrenwall, Almud) ≥ +1)` | `conflict_architecture`; `core › Reversal` ◆ Coup predicate |
| D-10.06 | Autonomy effects | `Loyal: —; Restless: S-014 garrison defensive only, Crown offensive deployments from Ehrenfeld +2 difficulty, fragmentation at Ehrenfeld +2; Autonomous: Crown.Military −count(units at Ehrenfeld), Fort 3 unusable by Crown, PI −1 once; Split: Löwenritter status := national with sheet (Influence 2, Wealth 3, Military 5, Intel 3, Stability 5), Ehrenfeld control := Löwenritter, PI −3, Crown.Military := min(Military, 2), Crown units at Ehrenfeld → Löwenritter; Coup: Crown suspended; installed candidate → Crown resumes (heir) or absorbed (Duke); Löwenritter reverts to institution` | `core › Graduated Autonomy`, `› Coup`; `parliament › PP-569` |
| D-10.07 | Insurgency formation | `∃ P ⊆ provinces: |P| ≥ 2 ∧ connected(P) ∧ ∀ p ∈ P: ctl(p) = ∅ ∧ sustained(ctl(p) = ∅, 2)` | `insurgency §4.1` |
| D-10.08 | Insurgency sheet | `L 1 (per settlement seed), PS 2, Influence 2, Wealth 1, Military clamp(count(s ∈ P: Order ≥ 2), 1, 3), Intel 2, Stability 2; status insurgency (non-parliamentary)` | `insurgency §4.2` ◆ Military |
| D-10.09 | Promotion | `aggregate_L(f) ≥ 3 ∧ provinces(f) ≥ 2 ∧ mean Accord ≥ 2 (◆ the corpus's "≥ 4" is above the 0–3 ladder; 2 = Compliant is the meaningful floor) ∧ sustained 2` → `status := national; extra_parliamentary := mean PT over held < 3` (persistent) | `insurgency §5.1–5.2` |
| D-10.10 | Dissolution (first true, in order) | `provinces(f) = 0 ∨ (aggregate_L < 1 ∧ provinces(f) < 2)` → gone; `sponsor lost (sponsor eliminated ∨ treaty renouncing ∨ sponsor's last province lost) → L −0.5/season until the first rule`; amnesty: parent Senator action, contested `parent.Mandate` vs `f.Stability`, `S → dissolve by agreement (provinces revert)`; else persist | `insurgency §6.2–6.3` ◆ sponsor-loss deterministic |
| D-10.11 | Latent RM trigger / suppression | `regard[Varfell][RM] ≤ −2 ∧ count(p: PT_p ≤ 1) ≥ 3 ∧ MS ≤ 50` → active (`Mandate` from presence, Influence 4, Wealth 1, Military 0, Stability 3; `+2` difficulty on Church actions in presence provinces); suppressed when `regard ≥ 0 ∨ ∀ p: PT_p ≥ 2 ∨ RM.Stability = 0` | `insurgency §3` |
| D-10.12 | RM Settlement Emergence | `Order_s = 0 ∧ PT_s ≤ 1 ∧ mean disposition(local actors, Vossen) ≥ +3 ∧ ¬fired in p within 4 seasons` → `s.controller := RM, governance-transition choice ∈ {Disestablishment, Accommodation, Transformation}` | `faction_succession_split §4`; `settlement_layer §4.3` |
| D-10.13 | Emergence stage predicates | `organisation: settlements(f) ≥ 2 ∧ (Renown ≥ 5 ∨ Influence ≥ 3) ∧ count(officers: disposition ≥ +3) ≥ 2`; `national: settlements ≥ 4 over ≥ 2 provinces ∨ holds a Seat; Declaration check S`; `hegemon: Seats ≥ 2` | `settlement_layer §6.2` |
| D-10.14 | Consecration | `Church.Stability ≥ 4 ∧ Himlensendt.scars < 3 → refused (CI +3, Crown seeds L −2 in Crown settlements; if Mandate(Crown) ≥ 3 for 3 consecutive seasons → CI passive halved thereafter, else contest reopens without Baralta)`; else `consecrated (CI −5, Church.Stability −3)`; `+1` difficulty on Baralta's post-contest Mandate recovery if `disposition(Torben, Baralta) ≤ 0 ∧ torben.matured` | `baralta_crown_claim §3, §7.3` ◆ Lock override |
| D-10.15 | Generational trigger | first of: `season ≥ 24`; `torben.readiness ≥ 5`; `Crown.Stability ≤ 1`; `Almud dead` → outcome by `disposition(Torben, pc)` band `{≥3 Loyal, 1–2 Cooperative, 0 Neutral, −1..−2 Wary, ≤−3 Hostile}` with Stability deltas `{+1, 0, −1, −2, −3}`; Autonomy `+1 stage` if `torben_loyalty ≤ 3 ∨ (readiness path ∧ disposition ≤ 0) ∨ Stability ≤ 1` | `faction_politics Part 8`; `baralta_crown_claim §7.1` |
| D-10.16 | Readiness | `+1` per Protection Duty S, tutoring scene, or Crown stabilising action witnessed by Torben; max `+2/year` | `faction_politics §8.1, §8.3` |

**Pipelines**

**PL-10.01 Succession Contest.** `opened (PH-10 after D-10.01, unless D-10.02 → smooth: leader := heir, Stability −1) → contenders enrolled (inner circle Standing ≥ 3; canonical heirs; office holders; externally backed via a Diplomat/Senator card (Praetor for a movement) played this season, which costs the backer nothing else ◆) → Stage 1: contested kernel, top1 vs top2, M = strength difference; OW/S → top1 leads; F → top2 leads; multi-contender pairwise from the top → Stage 2 by G: ≥3 → unified (Stability −1, L −1 in all settlements; Stage-1 F by top1 → regency instead); 2 → unified if disposition(runner-up, apparatus) ≥ 0 else split; ≤1 → split unless Stage-1 OW → unified → closed`. No contender → `regency` (no leader bonuses; retry next Accounting; three empty contests → collapse). Simultaneous contests resolve in descending pre-loss Mandate.

**PL-10.02 Split.** Creates polity `f'` (status national, name `"<Leader>'s <f>"` or directional): provinces — `f` keeps the capital province and each contested province goes to the nearer contender by settlement-graph distance to their seat; settlements follow provinces except those whose governor has `disposition ≥ +3` to a specific contender; `Influence` 60/40 floored, `Wealth` 70/30 floored, remainder burns; units by `disposition(commander, contender) + discipline`, ties disband; `Stability: f −1, f' := 2`; NPCs by disposition, others by residence. Reunification is a `reunification` treaty requiring both `Mandate ≥ 3`.

**PL-10.03 Löwenritter Autonomy.** Single instance; evaluated each PH-10 with D-10.05; effects D-10.06 applied on entry; Split and Coup terminal except by reconquest of Ehrenfeld (Coup: Crown resumes under the installed heir).

**PL-10.04 Insurgency.** `substrate (Uncontrolled provinces) --D-10.07--> formed (polity created with D-10.08; ctl(p) := f ∀ p ∈ P) --D-10.09--> promoted (status national; parliamentary flag) ; formed|promoted --D-10.10--> dissolved (provinces → ∅ or by agreement) | persist`. Insurgencies use the ordinary action table (Legionary, Consul; no Senator motions).

**PL-10.05 Latent RM.** `background (Stage 1: each arc, ∀ p with PT_p > 0 ∧ ctl(p) ≠ Church ∧ inquisitors(p) = 0: chance = min(0.8, 0.35·(1 + (arc − 1))) + 0.1·[Varfell adjacent ∧ Varfell.Influence ≥ 4]; draw < chance → one settlement's PT −1) --D-10.11--> latent (once per season: Organizing, Grassroots (Influence vs D(2) → presence +1 in a PT ≤ 2 province), passive +2 difficulty on Church seizures in PT ≤ 2 provinces; WR −2 once) --suppressed--> background`.

**PL-10.06 Crown succession.** Triggers: Crown leader lost (PL-10.01 with contenders Torben (blood), Löwenritter (institutional, if Autonomy ≥ Autonomous), Hafenmark (external-institutional if `baralta_stake.active ∧ Mandate(Hafenmark) ≥ 4`), Church (if `CI ≥ 40`)); Deposition (D-09.14) → same with the incumbent excluded. Outcomes: Torben → Crown continues; Löwenritter → Coup branch; Hafenmark → Consecration (D-10.14), Hafenmark persists under an institutional successor (Option B) and the PC Recognition Ceremony fires if `pc.standing[Hafenmark] = 7`; Church → theocratic regency (`CI +10`; all polities stability check D(2); secular rank privileges subordinated).

**PL-10.07 Reconstitution.** City-state → national: Declaration as D-10.13. Löwenritter after Split at `PI = 0`: Senator Inward, `Influence` vs D(3), `OW → PI := 2; S → PI := 1; P/F → Stability −1 (F also Church L +1 in Church settlements)`.

**Transitions out of SET-10.** New/removed polities → SET-06; control → SET-05; PI/CI/MS deltas → SET-07; contest scenes → SET-11 (mandatory slate, PC contender path); Split cards → SET-12.

---

### SET-11 — Personal Agency & Rank

```
 pc.convictions[3] ──▶ Scene Slate (Steps 1–7, pruned) ◀── Duty ◀── faction posture stack
        │                     │ 3–5 scene actions
        ▼                     ▼
   Momentum, Renown      scenes resolve (pool mode) ──Domain Echo (S +1 / OW +2, cap ±2)──▶ EffectQueue
 pc.standing[f] 0–7 (ladders as data) · sub-office standings · Renown · Shadow Renown · Resources · caste
 death/retirement ──▶ Generational Transition partition + Lineage Act
```

**Primitives**

| ID | Primitive | Type / domain | Owner | Writer | Lineage |
|---|---|---|---|---|---|
| P-11.01 | `pc.convictions[3]` | `{text, matches[] (NPCs, polities, provinces, keywords, roles), strain 0–3, state ∈ {active, fulfilled, failed, transformed, unresolved}, actions_taken}` | player | PH-12 (review), scenes | `player_agency §2` |
| P-11.02 | `pc.duty` | `{type ∈ {Initiation, Investigate, Diplomacy, Governance, Protection, Reconnaissance, Subversion, Thread, Escort}, target, success_pred, season}` | player | PH-03 | `player_agency §3` |
| P-11.03 | `pc.standing[f]` | `Clamped<−1,7>` (−1 = Dismissed-with-Dishonour) per polity; `pc.branch[f]`; `pc.sub_standing[ladder]` | player | commit | `faction_politics §1.0–1.4, Part 2`; `player_agency §5.1` |
| P-11.04 | `pc.renown`, `pc.shadow_renown` | `Clamped<0,10>` each, non-decaying, `+2/season` cap each | player | commit | `player_agency §5.4`; `faction_politics §2.2b` |
| P-11.05 | `pc.resources` 0–5, `pc.momentum` 0–5, `pc.coherence` 0–10, `pc.ts`, `pc.certainty`, `pc.wounds`, `pc.stamina` | Clamped | player | commit | `player_agency §9, §2.3`; `generational_transition` ◆ Coherence 0–10 |
| P-11.06 | `pc.caste` | `∈ {Northern, Central, Southern}` Fixed at creation; `pc.lifepath` seeds `ts ∈ {5, 10, 20}` | player | — | `faction_politics Part 3` ◆ TS seeds |
| P-11.07 | `pc.exposure[p]` | `Clamped<0,10>` per province | player | commit | `player_agency §1.6` |
| P-11.08 | `pc.at` | SettlementId | player | scenes | `settlement_layer §4.1` |
| P-11.09 | `pc.knots[]`, `pc.companions[]`, `pc.obligations[]` | refs | player | commit | `player_agency §6.2`; `generational_transition` |
| P-11.10 | NPC `standing`, `office`, `mentor_of` | on NPC records | NPC registry | commit | `faction_politics` (rank ladders apply to NPCs too) |
| P-11.11 | Rank ladder | Fixed rows per `(polity|ladder, standing)`: `{title, gate: Predicate, access[], obligations[], hall_tier, livery, mentor_rule, demotion: Predicate, magnitude}` | data | — | `faction_politics Part 1–2` |
| P-11.12 | Lineage | `{act ∈ {mentorship, succession, thread_legacy, none}, legacy_conviction}` | player | retirement | `player_agency §10–11` |

**Derivatives**

| ID | Derivative | Expression | Lineage |
|---|---|---|---|
| D-11.01 | Duty selection | highest posture row of `pc`'s polity whose `then` template has `capability_tags ∩ pc.tags ≠ ∅` (tags from skills: `investigate, diplomacy, governance, protection, recon, subversion, thread, escort`) and whose target is reachable (≤ 2 provinces); Standing 0 → Initiation Duty | `player_agency §3.2` ◆ tag match |
| D-11.02 | Slate | Steps 1–7 + 2b of `player_agency §4.2` as predicates over the snapshot; size `{Narrative 4–5, Normal 5–7, Hard 7–9}`; prune by `(step, internal_index)`; mandatory overflow → Witness Mode | `player_agency §4.2–4.3` |
| D-11.03 | Witness branch | the pre-scripted branch whose `conviction_tag` equals the highest-priority matched keyword of the PC's Convictions; default branch otherwise | ◆ (`player_agency §4.2`) |
| D-11.04 | Standing effects | `2: intelligence access; 3: council, branch, Town governor; 4: +1 scene, City/Fortress governor, sub-commands; 5: treaty standing, Seat governor; 6: inner-circle vote, +2 scene; 7: succession-eligible` | `player_agency §3.4, §5.1` |
| D-11.05 | Duty outcome | `success_pred → Standing +1 (+2 if exceeding: ◆ exceeding ⇔ the duty scene also produced a Renown-eligible event); failure → Standing −1 (floor 1 once initiated)` | `player_agency §3.4` |
| D-11.06 | Renown sources | `+1` per: Conviction fulfilled/transformed, Duty exceeded, Domain Echo, NPC scar caused, Complex investigation, mass battle present, Accord improved under governance, Knot formed; governance stakes `−1` per Accord drop / Treasury 0 / battle lost in governed settlement (cap −2); Southern Einhir: public gains halved outside `{Grauwald, Stillhelm, Oastad}` | `player_agency §5.4`; `faction_politics §3.3` |
| D-11.07 | Renown effects | `3+: neutral NPCs start +1; 5+: +1 point Impress; 7+: independent Domain Action with strength ⌊Renown/2⌋; 9+: Grand Contest at will` | `player_agency §5.4` |
| D-11.08 | Caste modifiers | Initiation difficulty `+2 points` for Southern Einhir in Crown/Hafenmark/Church/Guilds; inner-circle default dispositions per `faction_politics §3.5` (Central +1, Northern +2); gated ranks as ladder-gate predicates | `faction_politics Part 3` |
| D-11.09 | Demotion magnitude | `default 1; scandal 2 (min 1); heresy tribunal 2 (5+ → 3); defection max(3, →1); excommunication/treason/framework shift → 0 or −1` | `faction_politics §1.0a` |
| D-11.10 | Leadership | `standing = 7 ∧ leader lost → offered`; `standing ≥ 4 → challenge (social contest vs leader, council adjudicates); F → standing := 2, disposition(leader) −4` | `player_agency §5.2` |
| D-11.11 | Domain Echo | scene degree with Sufficient Scope (◆ scope ⇔ the scene's target is a polity office-holder, a settlement stat, or a clock-relevant NPC): `S → +1, OW → +2` on the echo target, cap `±2/season` | `stats › Domain Action Resolution` (Echo unchanged); `faction_behavior §5.2` |
| D-11.12 | Deniability Debt | accrual/reduction/thresholds exactly per `faction_politics §2.2b.ii`; witness rule ◆ `P = 0.1·count(resident NPCs with Standing ≥ 3 not in the operation)` | `faction_politics §2.2b` |

**Pipelines**

**PL-11.01 PC season.** `PH-03: duty (D-11.01), slate (D-11.02)` → `PH-04: spend scene actions; each scene resolves in pool mode; Momentum +1 per Conviction-pursuing action; echoes queued` → `PH-11: duty outcome (D-11.05), Renown (D-11.06), Standing obligations/demotion predicates evaluated, Conviction strain review` → `PH-12: Conviction states; Portrait Retirement offered if ≥ 2 of 3 starting Convictions resolved`.

**PL-11.02 Rank ladder.** `standing n --gate(n+1) holds ∧ (n+1 = 3 → Recognition scene; n+1 = 6 → Wing slot available ∨ Prince-in-Waiting) --> n+1`; `demotion(n) holds → n − magnitude`; `−1 → forfeited (re-entry only via a different branch)`. Facility slot capacity per settlement type gates Standing 6+ (`settlement_layer §1.4`).

**PL-11.03 Conviction.** `active --3 strains--> must transform or abandon; --fulfilled (≥2 actions, world aligned)--> fulfilled (+2 Momentum, Renown +1); --failed--> failed (+1 Momentum); --transformed--> transformed (new slot for a season)`; all three `unresolved` → drift warning.

**PL-11.04 Generational Transition.** On death or Portrait Retirement: PRESERVE all world state; TRANSFORM one Conviction (Legacy) and `Resources := ⌊old/2⌋ + start`; RESET Standing 0, Coherence 10, TS/Certainty by lifepath, Wounds/Stamina/Momentum/Exposure/skills; BREAK Knots (rupture strain to Knotted NPCs) and companions (return at disposition-to-leader); TRANSFER obligations, `Renown := [old ≥ 7]`; apply the chosen Lineage Act (Mentorship: skills 60%, org membership, one Knot at −2; Succession: titles, estates, governorships; Thread Legacy: `WR/2`, an embedded Knot POI at Evidence 3).

**Transitions out of SET-11.** Echoes → every set through the queue; governance verbs → SET-04; Standing 7/challenge → SET-10; PC diplomacy → SET-09 regard; Renown ≥ 7 → SET-06 independent actions; Investigation → SET-08 attention, SET-04 brokers; Lineage → SET-04 (governorship transfer).

---

### SET-12 — Campaign Arc & Decks

```
 setup: seed registry friction · draw 1 Tensions card · fuse(target, fire ∈ U{8..12})
 decks (one schema): settlement · peninsula (band crossings) · tensions · named-character
     card {family, triggers[], weight, cooldown, excludes[], ask, responses{verb → effects}, follow_on[]}
 revelation: MS band ∨ five triggers ──▶ mandatory slate scene · RM crisis branch
 warden paths A–E ──▶ Wardens enter the emergence pipeline
 terminal: victory(f) = sustained(score(f) ≥ 11, 2) · rupture = MS 0
```

**Primitives**

| ID | Primitive | Type / domain | Owner | Writer | Lineage |
|---|---|---|---|---|---|
| P-12.01 | `w.tensions` | `{card ∈ {RoyalCrisis, FeldmarkFamine, CardinalIndependence, GuildFracture, EinhirIncident, MinistryCrisis}, target?, fire_season, averted: bool, fired: bool}` | world | setup, PH-10 | `conflict_architecture › Tensions Deck`; `phases › Game Setup` |
| P-12.02 | Deck | Fixed card rows per deck; per-card runtime `{last_fired, active_chain}` | data / world | PH-02, PH-09 | `governance_play_redesign §2.2`; `worldbuilding §10` |
| P-12.03 | `w.revelation` | `{level 0–4, triggers_fired[], rm_branch ∈ {∅, embrace, denial, schism}}` | world | PH-10 | `campaign_architecture §4, §2.3` |
| P-12.04 | `w.victor`, `w.rupture` | `PolityId?`, bool | world | PH-12 | reconciliation (GD-1; MS 0) |
| P-12.05 | Friction registry | Fixed initial `presence`/church-axis rows: `Valorsplatz: cathedral, bishop-eligible; Gransol: presence[Guilds] 3; Ehrenfeld: presence[Löwenritter] 3; Grauwald: presence[RM] 1 (covert); Oastad: presence[RM] 2 (overt); Ministry presence 1 at Valorsplatz, Kronmark, Feldmark, Ehrenfeld; Guilds presence 1 at Halvardshelm, Gransol, Lowenskyst, Valorsplatz, Himmelenger` | data | — | `conflict_architecture › Starting Friction Points`; `ministry › AP/CP-Token Starting Positions` |

**Derivatives**

| ID | Derivative | Expression | Lineage |
|---|---|---|---|
| D-12.01 | Card eligible | `∀ trigger ∈ card.triggers: trigger(snapshot) ∧ season − last_fired ≥ cooldown ∧ ¬∃ active excluded card` | `governance_play_redesign §2.2` |
| D-12.02 | Card weight | `base × family_band_multiplier(Π) × Π_{tag ∈ card.tag_mods} (1 + ledger_count(tag))`; draw without replacement by weight from the stream | `governance_play_redesign §2.2, §2.4` |
| D-12.03 | Peninsula draw | one card per `band_crossing` this season whose `triggers` name that crossing | `phases` step 8 |
| D-12.04 | Named-character triggers | `Jarnstal Independence: ambition(Jarnstal) matured ∨ competence(Defense) = 0 ∧ Church.Stability ≤ 2`; `Olafsson Exposure: Intel OW vs Church in a settlement with a Broker`; `Prudence Crisis: Church.Wealth ≤ 2`; `Lions' Table Mutiny: Löwenritter.Military ≤ 2 ∧ Ehrenwall removed`; `Guild Schism: Guilds.Stability ≤ 2`; `Guild Forum Revolt: Crown taxation policy ∧ Guilds.Stability ≤ 3`; `Constitutional Crisis: Mandate(Crown) ≤ 1 ∨ Crown lost ≥ 3 provinces this season`; `Ministry Collapse: Crown.Stability ≤ 2` (◆ the affected Ministry is the lowest-competence one) | `worldbuilding §10` ◆ completed triggers |
| D-12.05 | Fuse signals | seasons 1–7: one Intrigue card per two seasons in the target's settlement; `averted ⇔ PC investigation reaches Evidence 5 in that chain before fire_season` | `conflict_architecture › Royal Assassination` |
| D-12.06 | Revelation level | `max(MS band index, count of triggers fired)`; triggers: public threadwork by an NPC/PC with `Renown ≥ 7` (◆), Threadcut being in a settlement, visible Mending, Thread op in a mass battle, RM node = site discovery | `campaign_architecture §4.3` |
| D-12.07 | Warden paths | `A: WR ≥ 3 → Wardens join Varfell as institution`; `B: rm_branch = embrace ∧ regard[RM][Wardens] ≥ 2 → alliance`; `C: WR ≥ 3 ∧ pc.founded_org → PC's movement`; `D: elske_loyalty ≥ 5 ∧ Schoenland treaty → Crown institution`; `E: MS ≤ 20 → Wardens declare (movement; Sanctuaries = presence)` | `campaign_architecture §6.2` |
| D-12.08 | Victory score | `score(f) = Σ_{p controllable} [Accord(p) ≥ 2] · share(f,p)/base_PV(p) + Σ_{g: sovereignty treaty g→f} score_own(g)`; `victory(f) ⇔ status(f) = national ∧ sustained(score(f) ≥ 11, 2)`; rupture `⇔ MS = 0` (checked first) | reconciliation; `core › Accord`; `insurgency §7.1` |

**Pipelines**

**PL-12.01 Setup.** Seed registries (D-04.15, P-12.05) → seed L/PS from `f.seed` → draw Tensions card (`rng(0, setup, tensions)`) → if RoyalCrisis: target `~ U{Lenneth, Torben, Almud}`, `fire_season ~ U{8..12}` → Autonomy := Loyal → derive snapshot → season 1.

**PL-12.02 Fuse.** `armed --each PH-10 with season < fire_season--> signalling (D-12.05) --averted--> defused (investigation reveals the sponsor's regard −2) | --season = fire_season--> fired: target killed; branches: Lenneth → Almud revenge (Crown actions +2 difficulty for 4 seasons, RM presence +1 in southern provinces); Torben → Elske retrieval (Crown must move a unit through Grauwald: CB Varfell → Crown; IP +5); Almud → Lenneth queen (Crown mission shifts to authored 'Einhir accommodation'; CI +3; Autonomy → Restless)`.

**PL-12.03 Card life.** `eligible → drawn (PH-02 settlement / PH-09 peninsula) → presented (slate or directive) → responded (PH-05: chosen response's effects queued; `ignore` applies `pressure_if_ignored`) → follow-ons armed → cooldown`.

**PL-12.04 RM crisis.** `folklore --revelation level ≥ 2 ∨ node-site discovery--> crisis scene: branch by player influence: embrace (RM may sponsor Thread Weaving; Warden path B opens) | denial (RM Organizing +1 difficulty in revealed provinces) | schism (RM splits per PL-10.02 into rationalist RM and a Thread-aware movement)`.

**PL-12.05 End.** At PH-12: `MS = 0 → rupture (all lose)`; else `∃ f: victory(f) → victor := f` (ties: highest score, then Mandate, then stable key).

**Transitions out of SET-12.** Cards → SET-04 (settlement effects), SET-06/07 (polity/clock deltas); fuse → SET-10 (succession), SET-09 (CB), SET-07 (IP); revelation → SET-11 (mandatory scenes), SET-10 (RM branch); victory ← SET-05 (shares, Accord), SET-09 (sovereignty treaties), SET-06 (status).

---

## 3. The unified graph

### 3.1 The tick — what the engine does each season, in order

One season is one pass through twelve phases. Each phase names what it reads and what it writes. Writes before PH-07 are *only* appends to the Effect Queue; PH-07 is the single commit for action effects; PH-08 onward are Accounting phases that apply their own effects at the end of each phase through the same commit routine. Every phase is deterministic given the snapshot and the seeded stream for `(season, phase, key)`.

| Phase | Name | Reads | Writes | Corpus lineage |
|---|---|---|---|---|
| **PH-01** | **Open** | season, seed | `season_flags {year_end, arc_boundary}`, budgets reset (`ap`, `scene`, card availability from cooling), radiation rows into the snapshot, `p.hostile_free_seasons` carried, unit `budget_left` refilled | `phases` step 13; `clocks › MS Effects` |
| **PH-02** | **World stroke** (settlement) | every settlement's snapshot, NPC ambitions, ledgers, decks | `s.needs` opened (D-04.12), `s.pressure` (D-04.10), `s.directive` (D-04.13), NPC `ambition.progress`, settlement cards drawn (D-04.11), matured ambitions → Ambition cards | `governance_play_redesign §4.2`; `settlement_layer §4.3` |
| **PH-03** | **Orders** | polity posture stacks, PC state, snapshot | `ActionInstances` declared for every polity (cards) and PC (duty, slate), pledges, treaty dissolutions, Mass-Seizure declaration, Diplomatic Alignment, Policy declaration; input log appended | `phases › Phase 1`; `player_agency §7.2 (1a–1b)`; `parliament › PP-515` |
| **PH-04** | **Personal** | slate, PC, NPCs at the scene settlement | scenes resolved in pool mode; `Momentum`, `Exposure`, dispositions, Evidence tracks; Domain Echo effects queued | `player_agency §4.4`; `strategic_layer §9.8 step 1` |
| **PH-05** | **Settlement** | directives, AP, drawn cards, governor | directive responses; governance verbs; card responses; bishop appointments / pastoral assumptions; building upgrades; subnational grant/revoke — all as queued effects (control changes are read back immediately for this phase's later actions) | `phases › Three-Scale Resolution 1`; `governance_play_redesign §1` |
| **PH-06** | **Province** | declared card actions ordered by D-02.03 | tier 1 Intel (reveals into `known_state`); tier 2 Military: marches (PL-03.01), assaults/sieges (PL-03.02–03), Vanguard contact; tier 3 Domain: Govern/Trade/Muster/Fortify/Survey/Consolidation/Levy-as-Directive; tier 4 Social: motions with votes (PL-09.03), Manoeuvre, Policy (PL-09.04), Suppress, Assert, treaties, Crown Treaty, Diplomacy; tier 5 Thread ops; tier 6 Unique (Decree, Excommunication, Private Collection, Economic Leverage, Sovereign Authority, Reformed Settlement, Mass Seizure per-province rolls); tier 7 Projects. Battle casualties and captures are read back within the phase; everything else is queued | `phases › Phase 4 Resolution Priority Order`; `strategic_layer › P-18` |
| **PH-07** | **Commit** | Effect Queue | all queued action effects applied in `(scale, path, key)` order with source-class sub-caps and net `±2` faction clip; `state.changed` events; attribute-loss tally | `phases › Phase 5` step 1; `stats › PP-242` |
| **PH-08** | **Derive up** | settlements | the derived snapshot: `ctl(p)`, `Accord`, `fractional`, `PV shares`, `Mandate`, `aggregate L/PS`, `Prominence`, cascade aggregates (damped), strictness, capabilities; **no writes to primitives** | `phases › Three-Scale 2`; `settlement_layer §1.3, §1.8`; `phases` 4b |
| **PH-09** | **Peninsula** | snapshot, this season's events (battles, revolts, eliminations, seizures, treaties) | clocks in order Turmoil → CI → IP → PI → MS (PL-07.01); band crossings; milestones; peninsula event cards drawn (D-12.03); temperament drift; Turmoil-band stat effects queued; radiation Surge | `phases › Phase 5` steps 4, 4d, 4e, 6, 8; `ci_seizure`; `tracks › Turmoil` |
| **PH-10** | **Pipelines** | snapshot, events | every state machine steps once, in registry order `(scale, pipeline_id, subject_key)`: Fragmentation Checks, Consolidation responses, Vacuum lifts, Autonomy, Succession Contests, Splits, Insurgency form/promote/dissolve, Latent RM, Emergence/collapse status, Invasion phases, Vanguard advance, Warden tracks, Expedition stages, Fuse, Revelation, Suspicion, Office vacancies, NPC ambition acts | `phases › Phase 5` steps 9–10b; every `_v30` pipeline doc |
| **PH-11** | **Settle** | tallies, snapshot | Stability checks and Consolidation recovery; cooldowns −1; PC duty/renown/standing; L/PS feedback (PL-05.05) and recovery; settlement drift (PL-04.03); Attention → Inquisitor placements, then Attention reset; Thread Debt ageing; pledge honour/breach; CB expiry and event-driven CB creation; ledger tag expiry; Π releases for served needs | `phases › Phase 5` steps 2, 3, 4c, 5, 6, 7; `player_agency §7.2 (3)` |
| **PH-12** | **Check & advance** | snapshot | eliminations (`Stability = 0`), Vacuum entry, revolts (PL-05.04, PL-04.05), sustained counters, Conviction states, Portrait offer; **rupture, then victory** (PL-12.05); if `year_end`: treaty lapse (D-09.07) before all else, then RM Stage-1 decay, arc CB refresh, Year-End hooks (Wealth from Prosperity, Legislative Record, Nomination, Cardinal appointments, Levies, Loyalty modifiers, Generational Shift, CI-80 PT drift, Mass-Seizure failure test); `season += 1`; derive snapshot; state hash | `phases › Phase 5` steps 12–13, `› Year-End`; `treaty_expiration §1.1` ("before any other arc-boundary processing") |

**Why this order and not the corpus's.** The corpus has the settlement resolve first and the peninsula last (`phases › Three-Scale Resolution Model`), and separately has a 13-step Accounting whose first step applies pending changes. Both survive: PH-02..06 *are* settlement-then-province, and PH-07..12 *are* Accounting. What the corpus never said is where the peninsula's *actions* go (Mass Seizure, Vanguard, invasion) — here they are province-phase actions whose *consequences* are peninsula-phase clock updates, which is what "the peninsula is the consequence layer" means. The only reorderings versus `phases › Phase 5`: Cooldown moves after Stability checks (no effect either way — nothing reads cooldown in between); Attention resolution moves after Inquisitor placement so placements are computed from a full season's pool; victory follows rupture explicitly (the corpus said "shared loss checked first").

### 3.2 Scale composition

**Upward is derivation; downward is effect.** No stored quantity exists at two scales.

```
 ┌───────────────── PENINSULA (consequence layer) ──────────────────────────────────────────────┐
 │  MS · CI · IP · PI · Turmoil · WC/WR · Loyalties · Generational · invasion phase · victor      │
 │        ▲ clocks are functions of events + previous clock         │ bands/milestones            │
 │        │ (battles, revolts, eliminations, seizures, treaties,     │ ⇒ advantage rows on actions │
 │        │  Prominence·PT·SW, Accord counts, occupied provinces)    │ ⇒ Turmoil-band Order effects│
 │        │                                                          │ ⇒ event cards ⇒ Effects     │
 ├────────┼──────────── PROVINCE (contest layer) ───────────────────▼──────────────────────────────┤
 │  ctl(p) = ctl(seat) · Accord = ⌊mean Order⌋ · PV shares ∝ Prosperity · fractional · Prominence │
 │  Mandate(f) = sat(Σ W_s·q_s) · aggregate L/PS                                                  │
 │        ▲ pure functions of settlement primitives                  │ Fragmentation ⇒ Order −1   │
 │        │                                                          │ Mandate ⇒ L/PS feedback     │
 │        │                                                          │ Directives ⇒ settlement     │
 ├────────┼──────────── SETTLEMENT (engine layer) ───────────────────▼──────────────────────────────┤
 │  Prosperity · Defense · Order · L · PS · PT · Tier · controller · governor · church axes ·      │
 │  presence[inst] · Π · ledger · needs · local actors · ambitions                                 │
 │        ▲ governance verbs, cards, appointments, battles, sieges, Thread ops (Effects)           │
 ├────────┼──────────── PERSONAL (scene layer) ─────────────────────────────────────────────────────┤
 │  PC · NPC dispositions · scenes in pool mode ── Domain Echo (cap ±2) ──▶ settlement/polity paths │
 └───────────────────────────────────────────────────────────────────────────────────────────────┘
```

- **Settlement → Province.** `Accord`, `PV share`, `fractional`, `Provincial Authority` are computed from members every PH-08 and PH-12. A province stores only what has no settlement analogue: stabilisation and vacuum windows, Attention, Thread Debt, the trade-route token, temperament drift.
- **Settlement → Polity.** `Mandate`, `aggregate L/PS`, `Treasury` (display) are computed from controlled settlements. A polity stores its five stats, its hand, its mission and its offices — things that are *about the institution*, not about acceptance in a place.
- **Province → Peninsula.** Clock deltas are functions of counted province facts (`count(Accord ≤ 1)`, `count(Prominent)`, battles per province, occupied provinces). The peninsula stores only clocks and campaign-arc state.
- **Peninsula → Province → Settlement (pressure).** A clock band is not applied "globally"; it becomes advantage rows keyed by `(band, proximity(p))` and Turmoil-band effects that target `Order` in specific seats (lowest-Accord first). A band crossing draws a peninsula card whose responses are Effects with settlement or polity targets. Nothing at the peninsula writes a settlement primitive directly; it emits Effects that commit does.
- **Personal → everything.** A scene's degree, when it has Sufficient Scope, becomes at most `±2` of Effect on one path. The personal layer never reads a clock; it reads the snapshot's *radiation row* and *slate*.

### 3.3 Where the graphs were fighting, and how the unified version resolves it

- **Two resolution systems** (`stats_1_7_scale` resolver vs every `pool vs Ob` rule) → one kernel with two modes and one advantage unit; the legacy Ob mapping is the bridge, applied everywhere.
- **Two degree tables** (PP-179 vs Ob+1) → PP-179 for pool mode; margin mode has its own bands; nothing else survives.
- **Prosperity at two grains** → settlement is stored; province is `Σ`; the geography table's numbers become the primary settlement's seed.
- **L/PS at faction vs settlement** → settlement only; Mandate is derived; the authored faction Mandate table becomes a calibration target for `K`.
- **Fracturing in two documents** (`fractional_province_ownership` vs `valoria_political_hierarchy §2.3–2.4`) → PV shares + Fragmentation + Consolidation kept; sub-province naming kept as a label rule; the unification-bonus scalar becomes the rights-of-the-Seat-holder.
- **Accord change rules written against provinces** (`tracks`, `phases 4c`) vs Accord derived from Order → every Accord-modifying rule is rewritten to target `Order` in the named settlements (seat, lowest, all non-capital).
- **Four phase schemes** → one twelve-phase tick.
- **Three-scale order vs Phase-4 tiers** → scales are phases; tiers order actions within PH-06.
- **Cascade Depth Cap vs batching** → batching alone; effects never fire effects inside a phase, so depth cannot run away.
- **Standing (rank) vs Standing (tokens) vs Standing (reputation)** → rank stays `pc.standing`; the other two are `rel.regard`.
- **Presence markers / CP-tokens / AP-tokens / Guild Favour / Church Favour** → `s.presence[inst]` and Church Prominence.
- **Turmoil vs Public Instability** → one clock.
- **TT vs MS** → `TT = 100 − MS`.
- **RM Community Weaving vs Organizing** → two action rows (reconciled); RM is a `movement` polity with a partial sheet, not a statless special case.
- **Battle → IP +2** (`phases 4e`) vs struck (`ci_political §4.4`) → struck; IP advances from Accord counts, Crown weakness, Torben, occupation.
- **CI freeze at 75 / seizure at 75 / seizure at 80** (`clocks`, `strategic_layer P-23`, `institutions`) → none; CI runs to 100, Mass Seizure at 60+, one-shot.
- **Victory as faction-specific paths / co-victory / hollow victory** (`phases` step 12, `strategic_layer`) → the sole universal score; deeds, hollow totals and milestone bonuses are removed with nothing lost, because every "path" is now a strategy toward the same 11.
- **Ministry "Accounting Step 11"** → a posture row that fires in PH-06 and a PI rule in PH-09.
- **Coup Counter vs Graduated Autonomy** → autonomy; the counter's increments become Autonomy transition predicates.
- **Niflhel as faction vs dissolved** → dissolved: black markets, brokers and sites are derivations; the Niflhel ladder in `faction_politics §2.6` survives only as sub-office Standing data for a PC in the shadow economy.
- **GM decisions** (~36) → each is a predicate or a draw in the tables above; none remains.

### 3.4 Conservation properties

**Bounded.** Every stored numeric path has a declared range and is clamped at commit; every clock additionally has a seasonal cap (`CI ±5/±3`, `PI +2`, faction stats `±2`, settlement stats `±1` per source class, PT `±1` from actions, Renown/Shadow `+2`). Margin `M` is unbounded but the kernel's probabilities are floored at 0.05 and capped at 0.90 — no outcome is ever certain or impossible except by prerequisite.

**Monotone.** `season`; `w.mass_seizure_used`; `w.repelled`; `wr_ever_past_1`; Dishonoured (Standing −1); Insurgency stages 3 → 4 (never back); Löwenritter `Split` (only reconquest reverses it, which is a new state, not a transition back); Renown and Shadow Renown never decay; Precedent tags never expire (Grudge and Debt do); `Generational Shift`; `revelation.level`; treaties are memoryless (no aging), which is a *non*-monotone guarantee the design keeps on purpose.

**Sums.** `Σ_f share(f, p) = base_PV(p)` for every province (or the equal-split guard); `Σ_p base_PV(p)` over controllable provinces is the victory denominator's mass; `|hand| + |cooling| = |authored hand|` per polity; `count(units of f) ≤ Military(f)`; `Σ_s presence[inst] ≤ 3 · |settlements|`; on a split, `Influence' + Influence'' ≤ Influence` and `Wealth' + Wealth'' ≤ Wealth` (the remainder burns — legitimacy is destroyed, not moved); `Σ votes for + against + abstain = Σ Mandate(parliamentary) + CI weights`; per season `Σ Δ MS = −battles − year_end − debt + mending + WC` exactly (fractions carried in one accumulator, never rounded twice).

**Round-trips.** *Derivations:* every D-value is recomputable from primitives; the snapshot is a cache and must equal a fresh computation (asserted after every PH-08/PH-12). *Replay:* `state₀ + seed + input_log → state_N` with identical per-phase hashes. *Control:* `ctl(p) = ctl(seat_p)` always; a settlement controller change is the only way a province changes hands. *Accord:* `Accord(p) = ⌊weighted mean Order⌋` always — the starting registry reproduces the authored capitals-3/home-2 table exactly (D-04.15), and every "Accord −1" rule in the corpus round-trips through Order. *Cards:* a card leaves the hand only by play and returns only by cooldown. *Effects:* every state change has a `source_ref`; the season's change log is the sum of committed Effects and nothing else.

**Complementarity — what each scale does that the others cannot.** The settlement is the only place where *people* act (governors, NPCs, the player), so it is the only place where new state is *created* rather than *recomputed* — acceptance (L/PS), order, prosperity, piety, presence. The province is the only place where *control is contested* — battles, transfers, seizures, fragmentation — and it does so by moving settlement controllers, never by writing settlement stats. The peninsula is the only place where *the whole* is measured — clocks are counts over provinces — and it acts back only by changing the odds (advantage rows) and by drawing cards. A quantity is therefore never owned twice: the peninsula does not own "Church presence" (that is settlement axes summed through Prominence), the province does not own "legitimacy" (that is settlement L/PS aggregated), and the settlement does not own "war" (that is province-phase contact between units).

---

## 4. The idealized code shape

Not a file listing — the architecture. Declarations are written in a typed pseudocode (TypeScript-flavoured for records and unions; `Clamped<lo, hi>` is an integer with clamp-on-write; `Frac` is an integer part plus a carried fraction). Anything marked `data` is authored content loaded at start; anything marked `code` is mechanism. The target is Godot, but nothing below depends on the engine: the model is a pure state machine over plain records, and the scene tree is a view of it.

### 4.1 Core types (T-nn) and why each exists

```ts
// ── Identity and numbers ──────────────────────────────────────────────────────
type SettlementId = string; type ProvinceId = string; type PolityId = string;
type NpcId = string; type UnitId = string; type PcId = string;            // T-01
type Clamped<lo, hi> = number;   // integer, clamped on commit             // T-02
type Frac = { int: number; frac: number };   // exact carry, never double-rounded

// ── The kernel ────────────────────────────────────────────────────────────────
type Degree = "F" | "P" | "S" | "OW";                                     // T-03
type Advantage = { points: number; reason: string };                      // +1 = +1 die = +1 M
type Check = {                                                            // T-04
  mode: "margin" | "pool";
  strength: number;             // actor stat (+ authored base) in margin mode; pool size in pool mode
  difficulty: number;           // margin mode: target stat or D(Ob); pool mode: Ob
  advantages: Advantage[];
  stream: RngKey;               // (season, phase, subject key)
};
// Why: one place where a contested thing is decided. Nothing else draws a random number to decide an outcome.

// ── Effects: the only write path ──────────────────────────────────────────────
type Path = string;             // "s:S-018.Order", "f:Church.Stability", "w.CI", "rel.regard[Crown][Church]"
type Effect = {                                                           // T-05
  path: Path; op: "add" | "set" | "max" | "min"; amount: number;
  sourceClass: "action" | "accounting" | "pipeline" | "card" | "echo";
  sourceRef: string;            // ActionInstance id, pipeline id, card id …
  key: string;                  // stable ordering key
};
type EffectQueue = Effect[];                                              // T-06
// Why: state has one writer (commit). Caps, clamps, ordering, logging and events live in one routine.

// ── Predicates and expressions (data can say "when") ──────────────────────────
type Predicate = Expr;          // boolean Expr over the snapshot                // T-07
type Expr =
  | { lit: number | boolean | string }
  | { path: Path }                                  // read a primitive or derived value
  | { op: "+"|"-"|"*"|"/"|"floor"|"min"|"max"|"clamp"|"count"|"sum"|"mean"|"cos"|"sign"|"abs"; args: Expr[] }
  | { cmp: "="|"≠"|"<"|"≤"|">"|"≥"; a: Expr; b: Expr }
  | { and: Expr[] } | { or: Expr[] } | { not: Expr }
  | { quant: "exists"|"forall"|"count"; over: Selector; where: Predicate }
  | { sustained: Predicate; seasons: number }       // reads the sustained-counter registry
  | { fn: string; args: Expr[] };                   // a registered pure derivation (D-nn.mm)
type Selector = { kind: "settlement"|"province"|"polity"|"npc"|"unit"; filter?: Predicate; rel?: "members"|"adjacent"|"controlled_by"|"resident" };
// Why: every branch predicate in the corpus is evaluable by this grammar; no rule needs code to be added.

// ── Actions: one schema for ~30 faction actions, 8 governance verbs, fieldwork, and auto-checks ──
type Budget = { kind: "card"; card: CardType } | { kind: "ap"; cost: number } | { kind: "scene" } | { kind: "none" };
type ActionDef = {                                                        // T-08
  id: string;
  scale: "settlement" | "province" | "peninsula" | "personal";
  actorKind: ("polity" | "governor" | "pc" | "auto")[];
  budget: Budget;
  targetKind: "none" | "settlement" | "province" | "polity" | "npc" | "unit";
  prerequisites: Predicate[];
  strength: Expr;               // e.g. {path:"actor.Influence"}
  difficulty: Expr;             // e.g. {fn:"D_ob", args:[{op:"+",args:[{op:"floor",args:[{path:"target.Prosperity"},{lit:2}]},{lit:1}]}]}
  contested: boolean;           // difficulty is the target's stat expression
  modifiers: string[];          // ids of Modifier rows consulted (identity, expertise, terrain, CI, regard …)
  effects: Partial<Record<Degree, Effect[]>>;   // missing band → next lower present band
  casusBelli?: { toTarget: boolean; source: string };
  convictionProfile: number[];  // 13-vector, for D-06.09
  category: string;             // da.public_governance | da.covert_betrayal | … (Mission alignment)
  tags: string[];               // suppress_L, self_improve, military, …
};
type ActionInstance = { id: string; def: string; actor: PolityId|NpcId|PcId; target?: string; params: Record<string,unknown>; degree?: Degree; season: number };  // T-09
type Modifier = { id: string; when: Predicate; points: Expr; appliesTo: Predicate };  // an advantage row

// ── Pipelines: state machines as data ─────────────────────────────────────────
type Pipeline = {                                                         // T-10
  id: string;
  subject: Selector;                       // one instance per matching subject
  states: string[];
  initial: string | Expr;
  transitions: { from: string; to: string; when: Predicate; effects: Effect[]; check?: string /* ActionDef id, auto */ ; degreeRoute?: Partial<Record<Degree,string>> }[];
  onEnter: Record<string, Effect[]>;
  phase: "PH-10";                          // every pipeline steps once, here
  terminal: string[];
};
type PipelineInstance = { pipeline: string; subject: string; state: string; enteredSeason: number; counters: Record<string, number> };

// ── Cards and decks: one schema for four decks ────────────────────────────────
type Card = {                                                             // T-11
  id: string; deck: "settlement" | "peninsula" | "tensions" | "named";
  family: "Petition"|"Friction"|"Opportunity"|"Crisis"|"Intrigue"|"Ambition"|"Thread"|"Fuse"|"Named";
  triggers: Predicate[]; weight: Expr; cooldown: number; excludes: string[];
  ask: { text: string; pressureIfIgnored: number };
  responses: { verb: string; requires?: Predicate; effects: Effect[]; release: number; scene?: string }[];
  followOn: { when: Predicate; unlock: string }[];
};

// ── The world ─────────────────────────────────────────────────────────────────
type Settlement = {                                                       // T-12
  id: SettlementId; province: ProvinceId; type: SettlementType; role: "primary"|"spoke"; xy: [number,number]; districts: District[];   // fixed
  Prosperity: Clamped<0,6>; Defense: Clamped<0,5>; Order: Clamped<0,5>; L: Clamped<0,7>; PS: Clamped<0,7>; PT: Clamped<0,5>;
  FacilityTier: Clamped<0,3>; controller: PolityId | null; governor: NpcId | PcId | PolityId | null;
  church: { building: "none"|"chapel"|"church"|"cathedral"; templar: boolean; inquisitor: boolean };
  presence: Record<"RM"|"Guilds"|"Ministry"|"Löwenritter"|"Wardens", Clamped<0,3>>;
  pressure: Clamped<0,10>; suspicion: Clamped<0,5>;
  ledger: LedgerTag[]; needs: Need[]; directive: Directive | null; ap: { capacity: number; spent: number };
};
type Province = {                                                         // T-13 (mostly a view)
  id: ProvinceId; duchy: string|null; seat: SettlementId; members: SettlementId[]; fort: Clamped<0,4>; proximity: Clamped<0,5>;
  SW: Clamped<0,5>; temperament: Temperament; basePV: Clamped<0,5>; controllable: boolean; capitalOf: PolityId|null;   // fixed
  stabilisedUntil: number; vacuumUntil: number; attention: Clamped<0,10>; threadDebt: { age: number; serviced: boolean }[];
  tradeRoute: { holder: PolityId; linked: ProvinceId|null } | null; temperamentDrift: number; hostileFreeSeasons: number;
  consolidation: { by: PolityId; pending: Record<SettlementId, "Submit"|"Resist"|null> } | null;
};
type Polity = {                                                           // T-14 — factions AND institutions
  id: PolityId; status: "national"|"institution"|"movement"|"insurgency"|"city_state"|"foreign"; extraParliamentary: boolean;
  role: Role; seed: { L: number; PS: number }; successionStat: string; expertise: CardType; capital: ProvinceId|null;   // fixed-ish
  Influence: Clamped<1,7>; Wealth: Clamped<0,7>; Military: Clamped<0,7>; Intel: Clamped<0,7>; Stability: Clamped<0,7>;
  hand: CardType[]; cooling: { card: CardType; left: number }[];
  mission: Mission; leader: NpcId|null; cascadeRoots: NpcId[]; institutionalCulture: number;
  offices: Office[]; posture: PostureRow[];                              // posture is data
  tracks: Partial<{ rdt: Clamped<0,5>; td: Clamped<0,5>; deniabilityDebt: Clamped<0,7>; awareness: Clamped<0,7>; massSeizureUsed: boolean }>;
  sponsor?: PolityId; originProvinces?: ProvinceId[];                    // insurgencies
};
type Npc = {                                                              // T-15
  id: NpcId; polity: PolityId|null; at: SettlementId; role: string; standing: Clamped<-1,7>; supervisor: NpcId|null;
  convictions: number[]; effective: number[]; scars: Clamped<0,5>; selfOther: number;
  disposition: Record<string, Clamped<-5,5>>;                              // toward polities, NPCs, the PC
  ambition: { goal: string; method: "lawful"|"factional"|"violent"|"covert"; timeline: number; progress: number } | null;
  leverage: { wants: string[]; fears: string[]; secret: string|null }; office: string|null; alive: boolean;
};
type Unit = { id: UnitId; polity: PolityId; at: SettlementId; kind: UnitKind; discipline: Clamped<1,5>; budgetLeft: number; siege: SettlementId|null };  // T-16
type Clocks = {                                                           // T-17
  MS: Frac; CI: Frac; IP: Clamped<0,100>; PI: Clamped<0,20>; Turmoil: Clamped<0,10>;
  WC: Clamped<0,3>; WR: Clamped<0,4>; torbenLoyalty: Clamped<0,7>; elskeLoyalty: Clamped<0,7>; generationalShift: Clamped<0,10>;
  invasionPhase: 0|1|2|3; repelled: boolean; freezeUntil: number; wardenEmergence: boolean; edeyjaContact: boolean;
};
type LedgerTag = { kind: "Precedent"|"Grudge"|"Debt"|"Reputation"; subject: string; weight: number; expires: number|null; obShift?: number };  // T-18
type Relations = {                                                        // T-19
  regard: Record<PolityId, Record<PolityId, Clamped<-3,3>>>;
  casusBelli: { holder: PolityId; target: PolityId; source: string; modeClass: string[]; created: number; expires: number }[];
  treaties: { a: PolityId; b: PolityId; kind: "formal"|"non_aggression"|"sovereignty"|"reunification"; bound: number; guarantor?: PolityId }[];
  pledges: Pledge[];
};
type PlayerCharacter = {                                                  // T-20
  id: PcId; at: SettlementId; caste: "Northern"|"Central"|"Southern"; convictions: Conviction[]; duty: Duty|null;
  standing: Record<PolityId, Clamped<-1,7>>; branch: Record<PolityId, string>; subStanding: Record<string, Clamped<0,7>>;
  renown: Clamped<0,10>; shadowRenown: Clamped<0,10>; resources: Clamped<0,5>; momentum: Clamped<0,5>; coherence: Clamped<0,10>;
  ts: number; certainty: number; wounds: number; stamina: number; exposure: Record<ProvinceId, Clamped<0,10>>;
  knots: NpcId[]; companions: NpcId[]; obligations: Obligation[]; budget: { capacity: number; spent: number };
};
type Event = { type: string; season: number; phase: string; payload: Record<string, unknown>; key: string };   // T-21
type Trigger = { id: string; on: string /* event type glob */; when: Predicate; emit: Effect[]; enqueueAction?: string };  // data
type RngKey = { season: number; phase: string; subject: string; seq: number };  // T-22

type GameState = {                                                        // T-23
  seed: bigint; season: number; phase: string;
  settlements: Record<SettlementId, Settlement>; provinces: Record<ProvinceId, Province>; polities: Record<PolityId, Polity>;
  npcs: Record<NpcId, Npc>; units: Record<UnitId, Unit>; clocks: Clocks; rel: Relations; pcs: Record<PcId, PlayerCharacter>;
  pipelines: Record<string, PipelineInstance>; campaign: { tensions: Tensions; fuse: Fuse|null; revelation: Revelation; victor: PolityId|null; rupture: boolean };
  queue: EffectQueue; inputLog: Input[]; sustained: Record<string, number>; oncePerYear: string[]; cardRuntime: Record<string, { lastFired: number }>;
};
// Derived (never stored, never saved): Snapshot = { accord, ctl, fractional, shares, mandate, aggL, aggPS, prominence,
//   cascadeAgg, strictness, capabilities, radiationRow, blackMarket, broker, site, vision, ... }                // T-24
```

Why each exists, in one line each: **Effect/EffectQueue** so there is one write path; **Check/Degree** so there is one decision; **Predicate/Expr** so data can express every branch the corpus left to a referee; **ActionDef** so the thirtieth action costs a row, not a function; **Pipeline** so the fifteenth multi-season process costs a table; **Card** so four decks are one engine; **Polity** so institutions, movements, insurgencies and factions are not five special cases; **Settlement/Province** so acceptance lives where people live and control lives where it is contested; **Relations** so every "token", "standing" and "accord" between polities is one ledger; **Trigger** so no subsystem names another; **GameState + Snapshot** so save is small and replay is exact.

### 4.2 Who owns what, and the single write path

| Quantity family | Owner record | Only writer | Read by |
|---|---|---|---|
| Settlement stats, controller, governor, church axes, presence, ledger, needs, directive, Π, suspicion | `Settlement` | `commit()` (Effects) — Π and directives are written by PH-02's world-stroke routine through the same commit | derive (Accord, shares, Mandate, Prominence), actions, cards, slate |
| Province windows, attention, thread debt, trade route, drift, consolidation | `Province` | `commit()` | pipelines, CI, Inquisitor placement |
| Polity stats, hand, cooling, mission, offices, tracks, status | `Polity` | `commit()`; `status` only via the emergence pipeline's Effects | kernel strengths, posture, votes, capabilities |
| Clocks | `Clocks` | `commit()` from PH-09's clock routine and pipelines | bands → modifiers, cards, victory |
| Regard, CB, treaties, pledges | `Relations` | `commit()` | vote sides, treaty strength, war entry, seizure cost |
| NPC dispositions, convictions, scars, ambition, standing, office | `Npc` | `commit()`; ambition progress by PH-02 through commit | cascade, slate, ambition cards, succession |
| Units | `Unit` registry | `commit()`; marches and battles write through commit with immediate read-back inside PH-06 | contact, garrison, supply |
| PC record | `PlayerCharacter` | `commit()`; scene results through commit | slate, standing, renown |
| Pipeline states | `PipelineInstance` | the pipeline runner, through commit | everything that asks "what stage is X in" |
| Derived values | Snapshot | **nobody** — recomputed | everybody |

`commit(queue, phase)` is the entire write surface: sort by `(scaleRank, path, key)`; apply source-class sub-caps then per-path net caps for the season; clamp; write; append to the change log; emit `state.changed`; update tallies. The routine is ~200 lines and is the one place cap policy lives. A rule that wants to write state and is not an Effect is a bug by construction.

### 4.3 The resolution kernel and how every subsystem reaches it

```ts
function resolve(c: Check): Degree {                       // code — the only decision procedure
  const adv = c.advantages.reduce((a, x) => a + x.points, 0);
  if (c.mode === "margin") {
    const M = c.strength + adv - c.difficulty;
    const Ps = clamp(0.5 + 0.1 * M, 0.05, 0.90);
    const Pow = clamp(Ps - 0.35, 0, 0.55);
    const Pp = clamp(Ps + 0.20, Ps, 0.97);
    const r = rng(c.stream).uniform();
    return r < Pow ? "OW" : r < Ps ? "S" : r < Pp ? "P" : "F";
  } else {                                                  // pool
    const dice = max(1, c.strength + adv), ob = max(1, c.difficulty);
    let net = 0; for (let i = 0; i < dice; i++) { const f = rng(c.stream).d10(); net += f === 1 ? -1 : f >= 10 ? 2 : f >= 7 ? 1 : 0; }
    if (ob >= 10) return net >= 10 ? "S" : net >= 5 ? "P" : "F";
    return (net >= 2 * ob && net >= 3) ? "OW" : net >= ob ? "S" : net > 0 ? "P" : "F";
  }
}
```

Who calls it, and how they build the `Check`:

- **A declared action** (`ActionInstance`): `strength := eval(def.strength)`, `difficulty := def.contested ? eval(def.difficulty on target) : eval(def.difficulty)`, `advantages := Modifier rows whose when holds`, `mode := def.scale === "personal" ? "pool" : "margin"`. Then `effects[degree]` (next-lower fallback) are enqueued, `casusBelli` granted, D-01.08 applied.
- **A battle**: the `assault` ActionDef with `contested: true`; both strength and difficulty are expressions over attacker, defender, edge, settlement type, Accord and garrison (D-03.04–05). There is no separate battle resolver; opposed dice are one margin.
- **A pipeline transition with a `check`**: the runner declares an `auto` ActionInstance for the subject (Fragmentation Check, Stability Check, Forgetting Check, Consecration is *not* a check — it is a predicate) and routes on the degree through `degreeRoute`.
- **A vote**: is not a check (tally is deterministic); the motion's *effect* check is (Transfer, Censure).
- **Succession Stage 1**: contested check between the two strongest contenders, `strength := contender strength` from D-10.03.
- **AI declaration probability** (Mass Seizure) and **decks**: use the stream directly through `rng(key).uniform()`; they are draws, not contests, and are the only non-kernel randomness. Both are logged with their key.

Every advantage anywhere in the game is a `Modifier` row: Domain Expertise (`+1` when the played card type equals `actor.expertise`), identity (D-01.06), coalition (D-01.07), CI weight (D-07.06), radiation (D-03.09), edge/type/Accord (D-03.04–05), regard, Ministry presence, RDT/TD ladders, Turmoil bands, black market, Inquisitor surveillance, Latent RM, caste. Adding a modifier is adding a row. The corpus's ~90 scattered "+1 Ob / −1D / +2D" clauses are, in this shape, ~90 rows in one file.

### 4.4 Pipelines as data — adding one is authoring, not coding

The runner is generic: for each `Pipeline`, for each subject matched by its selector, evaluate transitions from the current state in listed order, take the first whose `when` holds (or whose `check` degree routes), apply `onEnter` effects and the transition's effects through the queue, update counters. It runs once per season at PH-10 in `(scaleRank, pipeline.id, subject)` order. Sustained conditions are the `sustained` Expr, backed by the counter registry that PH-12 maintains.

```yaml
# data/pipelines/lowenritter_autonomy.yaml  — lineage: conflict_architecture › Graduated Löwenritter Autonomy
id: lowenritter_autonomy
subject: { kind: polity, filter: { cmp: "=", a: { path: "id" }, b: { lit: "Löwenritter" } } }
states: [Loyal, Restless, Autonomous, Split, Coup]
initial: Loyal
terminal: [Split, Coup]
transitions:
  - from: Loyal
    to: Restless
    when: { or: [ { cmp: "≤", a: { path: "f:Crown.Stability" }, b: { lit: 3 } },
                  { cmp: "≥", a: { path: "counter.seasons_since_crown_military" }, b: { lit: 4 } },
                  { path: "event.crown_lost_province_this_season" } ] }
  - from: Restless
    to: Loyal
    when: { and: [ { cmp: "≥", a: { path: "f:Crown.Stability" }, b: { lit: 4 } },
                   { or: [ { path: "event.crown_military_action_this_season" },
                           { cmp: "≥", a: { path: "n:Ehrenwall.disposition[Almud]" }, b: { lit: 1 } } ] } ] }
  - from: Restless
    to: Autonomous
    when: { or: [ { cmp: "≤", a: { path: "f:Crown.Stability" }, b: { lit: 2 } },
                  { cmp: "<", a: { path: "n:Ehrenwall.disposition[Almud]" }, b: { lit: 0 } },
                  { sustained: { cmp: "=", a: { path: "self.state" }, b: { lit: "Restless" } }, seasons: 4 } ] }
  - from: Autonomous
    to: Coup
    when: { and: [ { cmp: "≤", a: { path: "n:Ehrenwall.disposition[monarch]" }, b: { lit: -2 } },
                   { quant: "exists", over: { kind: npc, filter: { fn: "coup_candidate", args: [] } }, where: { lit: true } } ] }
  - from: Autonomous
    to: Split
    when: { or: [ { path: "event.crown_assaulted_lowenritter_settlement" },
                  { path: "event.crown_eliminated" },
                  { sustained: { cmp: "=", a: { path: "self.state" }, b: { lit: "Autonomous" } }, seasons: 4 } ] }
onEnter:
  Restless:   [ { path: "modifier:lowenritter_restless.active", op: set, amount: 1 } ]
  Autonomous: [ { path: "w.PI", op: add, amount: -1 }, { path: "modifier:lowenritter_autonomous.active", op: set, amount: 1 } ]
  Split:      [ { path: "f:Löwenritter.status", op: set, amount: national }, { path: "s:S-014.controller", op: set, amount: Löwenritter },
                { path: "w.PI", op: add, amount: -3 }, { path: "f:Crown.Military", op: min, amount: 2 } ]
```

The Insurgency pipeline, the Succession Contest, the Invasion phases, the Fuse, the Expedition, Suspicion, Emergence/collapse, the Fragmentation cycle, the Vanguard and the RM crisis are the same file shape. The succession contest's contender enrolment and asset split are the only two places that need a registered `fn` (a pure function over the snapshot) rather than plain expressions; both are listed in the derivation registry and are themselves data-parameterised (60/40, 70/30, tie rule).

### 4.5 Events and consequences across scales, without one subsystem naming another

`commit()` emits `state.changed`; phase routines and the kernel emit typed domain events: `battle.resolved`, `control.transferred`, `settlement.revolted`, `polity.eliminated`, `clock.band_crossed`, `treaty.voided`, `seizure.attempted`, `succession.opened`, `card.responded`, `expedition.entered`, `mission.shifted`, `scene.resolved`. Events are values on a per-season bus, keyed and ordered. Subscribers are `Trigger` rows — data — each with `on`, `when`, and Effects to enqueue (or an `auto` action to declare). The subscriber knows the event's payload schema, not the module that produced it; the producer knows nothing about subscribers.

```yaml
# data/triggers/battle_consequences.yaml — lineage: campaign_architecture §3.1; tracks › Turmoil; strategic_layer › PP-647
- id: battle_ms
  on: battle.resolved
  emit: [ { path: "w.MS", op: add, amount: -1, sourceClass: accounting } ]
- id: battle_turmoil_once_per_season
  on: battle.resolved
  when: { not: { path: "event.turmoil_battle_flag_set_this_season" } }
  emit: [ { path: "w.Turmoil", op: add, amount: 1 }, { path: "w.turmoil_battle_flag_set_this_season", op: set, amount: 1 } ]
- id: battle_order_loss_at_settlement
  on: battle.resolved
  when: { cmp: "≠", a: { path: "event.degree" }, b: { lit: "OW" } }
  emit: [ { path: "s:{event.settlement}.Order", op: add, amount: -1 } ]
- id: conquest_pins_order
  on: control.transferred
  when: { cmp: "=", a: { path: "event.class" }, b: { lit: "military" } }
  emit: [ { path: "s:{event.settlement}.Order", op: min, amount: 1 } ]
- id: adjacent_instability_cb
  on: arc.boundary
  emit: []            # declares the auto action "grant_adjacent_instability_cb" whose effects enqueue CB rows per D-09.06
  enqueueAction: grant_adjacent_instability_cb
```

Downward pressure is the same mechanism with a selector: `clock.band_crossed(MS, 59–40 → 39–20)` → a trigger that enqueues `Order −1` on `{ kind: settlement, filter: proximity ≤ 1 }` and draws a peninsula card. Upward composition needs no events at all — it is derivation. The bus is therefore small: about forty event types, about a hundred trigger rows, and no module imports another.

### 4.6 Data versus code — the boundary

| **Data (authored content)** | **Code (mechanism)** |
|---|---|
| Province registry (17), settlement registry (37) with seeds, districts, coordinates, friction rows; edge list (56); proximity, SW, temperament, base PV | Derivation registry: ~45 pure functions (`Accord`, `shares`, `Mandate`, `Prominence`, `W`, `q`, `radiationRow`, `cascade`, `strictness`, `votes`, `score`, …) |
| Polity definitions: roles, missions, hands, expertise, seeds, succession stat, posture stacks (as rows), office lists, role templates (13-vectors), institutional culture | `resolve()` — the kernel (both modes) |
| The action table (~60 rows: 30 faction, 8 governance verbs, ~12 unique/Church/Hafenmark/Varfell/Guild, ~10 auto-checks, personal fieldwork) | `commit()` — caps, clamps, ordering, change log, events |
| Modifier rows (~90) | The tick sequencer (PH-01..12) and the twelve phase routines (world stroke, order collection, scene runner, settlement/province action runners, clock routine, pipeline runner, settle, check) |
| Pipelines (~15 files) | The predicate/expression evaluator |
| Triggers (~100 rows) | The pipeline runner (generic) |
| Cards: settlement deck (60–100), peninsula deck, Tensions (6), Named-character (8) | The deck engine (eligibility, weighting, draw, chains) |
| Rank ladders (4 primary × 8, 7 sub-office), caste rows, conviction taxonomy, Duty types, slate step rules, scene scripts, Witness branches | The posture evaluator (`first row whose when holds`) — shared by polity AI, NPC governors, NPC ambitions, Directive generation and Duty selection |
| Clock band tables, milestone tables, Turmoil bands, PI bands, radiation matrix, Mender tiers, tier(PT) | Save/replay: canonical serialisation, hashing, `SplitMix64` keyed streams, input log |
| Constants (K = 6, lapse 0.90, caps, AP base 2, Π decay 1, CB life 3, supply radius 4, thresholds 3/5) — one file, every ◆ listed | Scene-scale engines (combat, social contest, fieldwork) that emit degrees into the same effect path — out of this corpus's scope but bound by the same contract |

**The test for the boundary:** if changing it changes *which world* this is (names, numbers, thresholds, decks, ladders, who starts where), it is data; if changing it changes *what a season is* (how a check resolves, how a write happens, what order things occur in), it is code. A rule that names a specific polity, province or outcome — "Church cannot seize Gransol at TD 5", "Feldmark +1 Prosperity uncontested", "Ehrenfeld hosts Löwenritter" — is authored as a *row whose predicate mentions that entity*, never as a branch in code. That is how `settlement_layer §4.3`'s eight hard-coded events became a deck, and it is the rule for everything else.

### 4.7 Determinism, save, replay

- **One seed, many streams.** `rng(key)` derives an independent `SplitMix64` stream from `hash(seed, season, phase, subject, seq)`. Two subjects never share a stream, so adding a settlement or reordering an unrelated action does not perturb an existing draw. Every draw is logged with its key.
- **AI is a function.** Posture stacks, NPC governors, ambitions, Directive generation and the Ministry are `first row whose predicate holds` over the snapshot, with ties by stable key. No AI reads the RNG except through declared draws (Mass Seizure declaration, deck weights).
- **Player input is data.** Every choice — card, target, directive response, verb, method, scene action, response to a card, Consolidation reply, pledge, treaty acceptance, Lineage Act — is an `Input` appended to the log at the phase it occurs. The engine never accepts a choice outside its phase.
- **Save = primitives.** A save is `GameState` minus the queue (always empty at a phase boundary) minus derived values. It is small: 37 settlements, 17 provinces, ~14 polities, ~200 NPCs, ~30 units, ledgers, pipeline instances, clocks, the input log.
- **Replay = fold.** `load(seed, inputLog) = fold(tick, setup(seed), inputLog)`; after every phase the state hash must match the recorded hash. A mismatch is a defect in a phase routine, and the offending phase is named by the first divergent hash. Rollback is free: reload and replay to season N.
- **Snapshots are recomputed, then asserted.** After PH-08 and PH-12 the derived cache is rebuilt and compared to a fresh computation of every registered derivation; inequality is a defect in a derivation's purity.
- **Caps are exact.** Fractions (MS, CI, Order from chapels, tithes, harvests) are carried in `Frac` accumulators and floored once per season; two half-points never round to two.

### 4.8 Worked examples

**Example 1 — Settlement scale: the war levy at Gransol (`governance_play_redesign §4.4`).**
Season 7, Gransol (S-018, City, controller Hafenmark, governor = the PC at Standing 4, Prosperity 5, Order 3, PS 4, Π 4, `presence[Guilds] 3`). PH-02: Hafenmark's posture stack top row is `Defend` (a Varfell unit is adjacent to Spartfell), so D-04.13 issues `Directive{Extract, 1 unit}`; D-04.12 opens no justice Need (Order is 3); but the Magistrate NPC's ambition (parliamentary seat, timeline 4, progress 2) is in motion (+1); D-04.10: `Π = clamp(4 + 0 + 0 + 1 + 0 − 0 − 1, 0, 10) = 4`; draw `1 + ⌊4/3⌋ = 2` cards; the weighted draw yields `EVT-S042 Petition: the miller's son was conscripted` (triggers: `directive.kind = Extract`) and an Opportunity. PH-05: the player Defies (`suspicion 0 → 1`, `PS +1`, local actors `disposition +1`, directive void → Hafenmark gets no unit), spends 1 AP on Hold Court ruling for the Magistrate (`disposition(Magistrate) +1`, `disposition(Garrison captain) −1`, tag `Precedent{only_sons_exempt, obShift −2 on conscription cards}`, release 2), 2 AP on Fortify by Militia (the governor is the PC, so `mode = pool`: pool `Military-relevant stat + history = 5` vs Ob `⌊Defense 1/2⌋ + 1 = 1` → S → `Defense +1`, `PS +1`, tag `militia` — an armed populace the faction did not raise; Develop was declined because Gransol's Prosperity 5 is the City ceiling, 6 being reserved for the capital). PH-07 commits: `Order` unchanged; the two `PS +1` (Defy, Militia) clip to one under the settlement-stat cap of `±1` per source class per season — `PS 4 → 5` — and the Effect log records the clip; `Defense 1 → 2`. PH-08: `W_s = 3 + 5 + 2 = 10`, `q_s = (4 + 5)/2 = 4.5`; Hafenmark's `T` rises; Mandate recomputed. PH-11: Π release 2 → next season's Π starts from 2. Season 8, PH-02: `suspicion 1` is below 3, but the Garrison captain's Grudge (weight 1) and the Magistrate's matured ambition (progress 4 = timeline) push Π to `2 + 1 + 1 = 4` and an Ambition card fires: *the Magistrate offers an alliance* — the PC's organisation now has an officer at disposition +3, one of the two D-10.13 needs for Stage 2 → 3.

**Example 2 — Settlement → Province: a bishop in Feldmark (`conflict_architecture › Church Expansion`, `fractional_province_ownership`).**
Feldmark province (Crown; seat S-009 Feldmark Town, spokes S-010, S-011). S-009 has `church.building = church` (built over two arcs), governor absent since the last Directive-driven recall. PH-05: Church declares `ecclesiastical_appointment` (Consul Outward): prerequisite D-04.08 holds; kernel margin `Influence 6 − D(1) = 6 − 1 = 5` → `P_s = 0.9` → S. Effects: `s:S-009.controller := Church`, `governor := Church`; PL-05.01: administrative class → `Order := min(Order, 2)`, and because `PT_s = 3 ≥ 3` no extra Order loss; `L, PS := Church.seed (5, 5)`. No CB (the row has `casusBelli` absent). PH-08: `ctl(Feldmark) = ctl(seat) = Church` — the *primary* changed hands, so the province transfers rather than fractionalising in Crown's favour: `control.transferred(Feldmark, Crown, Church)` fires; Feldmark's base PV is 1 (`ci_political §1`), so Crown's share falls from 1.0 to `1 · (1+1)/(5+1+1) = 0.29` (the two Villages it still holds) and the Church gains `0.71`; the province is now fractional in the *Church's* favour and it is the Church that rolls the Fragmentation Check; Crown's Mandate recomputes without S-009's `W = 8`. Had the Church appointed at spoke S-010 instead, the province would be *fractional*: PH-10 next season runs the Fragmentation Check for Crown — strength `Influence 5`, difficulty `D(2 + 1) = 4`, `M = 1`, `P_s = 0.6`; on F the Church (national) may secede S-010 into an independent holding — but D-05.11 gives Crown a Consolidation at `share = 6/7 ≥ 0.75`: strength 5 vs `D(⌈2·(1/7)·1⌉) = D(1) = 1` → `M = 4`, near-certain; Church's AI resists iff `Defense + garrison ≥ 2` (a Village: no) → Submit, `Order −2`. The Geneva trap is now legible as arithmetic: accepting a church for `Order +1` created a bishop-eligible settlement whose capture costs the Church one Consul card and the Crown one Fragmentation cycle to undo.

**Example 3 — Province scale: Hafenmark assaults Halvardshelm (`settlement_adjacency`, `march_layer`, `settlement_layer §5.1`).**
PH-03: Hafenmark plays Legionary (March). Unit `u` (professional, discipline 3) at Spartfell Fortress (S-021); `Military 3 → ⌊3/2⌋ = 1` edge of budget. The only edge into Halvardshelm is the hub-to-hub `pass` (cost 2), so the march is not traversable this season (D-03.02); the posture stack re-plans to Muster. A season later, `Military 4 → 2` edges: PH-06 tier 2, ordered with Crown's Legionary by `(tier 2, Stability 4 = 4)` — a two-way tie, so the two marches resolve simultaneously against pre-state. Traversal: entering Varfell's province without treaty → `cb(Varfell → Hafenmark, trespass)`, `regard[Varfell][Hafenmark] −1`. Contact at S-028 (Town, Defense 0, controller Varfell, garrison ∅): D-03.03 no forced engagement; Hafenmark declares Assault: strength `4 + ⌊3/2⌋ − 1 (pass) = 4`, difficulty `4 (Varfell Military) + 0 (fort) + 0 + 0 + 0 + 0 = 4` (Accord 2 → no defender bonus) → `M = 0`, `P_s = 0.5, P_ow = 0.15` → draw 0.42 → S. Effects: `S-028.controller := Hafenmark` (military class → `Order := min(Order, 1)`), `Prosperity −1`, attacker `discipline −1`; events `battle.resolved`, `control.transferred`. Triggers: `w.MS −1`, `w.Turmoil +1` (once), CB consumed (none held — trespass CB is Varfell's). PH-08: Halvardshelm is fractional (seat S-028 *is* the primary → this is a transfer of the Seat: `ctl(Halvardshelm) = Hafenmark`; spokes S-029/S-030 remain Varfell → *fractional in Hafenmark's favour*); shares: Hafenmark `1 · 4/(4+1+1) = 0.67` of base PV 1, Varfell 0.33. PH-09: Turmoil 0 → 1 (Peace); IP: no Accord ≤ 1 provinces yet (Accord(Halvardshelm) = ⌊(1 + 2 + 2 + 1)/4⌋ = 1 — yes, one) → `+⌊1/3⌋ = 0`. PH-12: Varfell's posture next season reads `Defend` (enemy unit adjacent to ungarrisoned territory) and `Counter-threat` — and holds a trespass CB it may spend on a Parliamentary Transfer in Adversarial mode, which is the corpus's whole point: the military move bought a settlement and handed the victim a political weapon.

**Example 4 — Peninsula scale: a CI season and the Mass Seizure decision (`ci_seizure`, `ci_political §2`).**
Season 21, CI 63.4 (`Frac{63, 0.4}`). PH-08 snapshot: Church Prominent in Himmelenger (SW 5, PT 5), Gransol (SW 3, PT 3), Ehrenfeld (SW 3, PT 3). PH-09 D-07.04 in order: (1) `count(Prominent) = 3 ≥ 2 → +1`; (2) Piety Yield `1.0·1 + 0.25·0.6 + 0.25·0.6 = 1.30`, plus carried `0.4` → `1.70` → floor 1, carry 0.70; (3) Church spent 2 Wealth on charity → `+1`; (4) one Templar unit at Ehrenfeld with Prominence → `+1`; (5) Assert (Senator) resolved S in PH-06 → `+1`; (6) Hafenmark Suppress resolved F → no cancel (and Hafenmark took `Stability −1` in PH-07); (7) `Mandate(Hafenmark) = 4 ≥ 4 → −1`; Himmelenger control `+1`. Sum `+5`, action-sourced portion (Assert `+1`, charity `+1`) `= 2 ≤ 3`; total `≤ 5` → CI `63 → 68`, carry 0.70. Band crossing: milestone 65 *Dominant* enters `w.milestones_fired` → `clock.band_crossed(CI, 55–64, 65–79)` → the peninsula deck draws the card whose trigger names that crossing (*Secular Alarm*: every national polity's posture gains a `Counter-threat` row). PH-03 next season: Church is NPC; D-08.03: `CI 68 ≥ 60 ∧ ¬used ∧ Mandate(Church) 5 ≥ 4`; `P = ((68−60)/40)^3.3 = 0.2^3.3 ≈ 0.005`; `rng(22, PH-03, "Church.mass_seizure").uniform() = 0.31` → not declared. At CI 90 the same draw would face `P ≈ 0.39`; at 100 it is mandatory. When declared: emergency season (free Senator-class motion for every other polity), then PH-06 tier 6 resolves each target province through the kernel — Himmelenger is its own; Ehrenfeld: `Ob = 10 − 3 − infra(6: cathedral 2 + templar 1 + inquisitor 1 + governor 2) = 1 → D = 1`, strength `6 + ⌊90/15⌋ = 12` → capped 0.90 — but Ehrenfeld's seat is garrisoned by Löwenritter, so an assault comes first, and if the Autonomy pipeline is at *Autonomous* the garrison is not Crown's to lose: the Church fights the Order, and the Crown watches its fortress change hands twice in one season without lifting a card.

**Example 5 — Cross-scale: Vaynard dies at the Battle of Oastad (`faction_succession_split §3`, `settlement_layer §6.3`, `insurgency_pipeline`).**
PH-06 season 12: Crown's assault on S-034 Oastad resolves OW; the defending commander NPC is Vaynard (present per unit record) → `npc.alive := false`, event `leader.lost(Varfell)`. PH-10: PL-10.01 — D-10.02: Maret Uln is canonical heir but `disposition(apparatus) = +2 < 3` → contest. Contenders: Uln (blood: `Mandate 4 + Influence 4 = 8`), the Tribune Captain (institutional: `Influence 4 + Intel 4 = 8`), RM-backed candidate (external, backer RM played a Praetor card this season: `3 + 2 = 5`). Tie at 8 → `succession_stat(Varfell) = Intel` → the institutional candidate is top1. Stage 1: contested `M = 8 − 8 = 0` → draw 0.62 → S → Captain leads. Stage 2: `G = 0 ≤ 1` → split, unless Stage 1 was OW (it was not). PL-10.02: Varfell keeps Sigurdshelm (capital) and Oastad's remaining settlement; Halvardshelm and Grauwald go to "Uln's Varfell" (nearer her seat by graph distance); `Influence 4 → 2/1` (remainder burns), `Wealth 4 → 2/1`; units by `disposition + discipline`; `Stability: 3 / 2`. PH-08: two polities, two Mandates, each derived from the settlements it now controls — no special rule computed either. PH-12: Oastad's seat is Crown's, Order pinned 1; Accord(Oastad) = 1 → IP counts it. Season 14: Crown, over-extended, lets Oastad's garrison go; PH-12 season 15: Accord 0 → Revolt → `ctl(Oastad) := ∅`; season 17: Grauwald under Uln's weak Stability hits 0 → eliminated → Vacuum → Uncontrolled; Oastad and Grauwald are *not* adjacent (T4–T13 are not edge-connected), so D-10.07's contiguity fails and no insurgency forms — until Stillhelm revolts in season 19, giving Oastad–Stillhelm contiguity and, two seasons later, an Insurgency polity with `Military = clamp(count(Order ≥ 2), 1, 3)`. Its mean PT is 1 → on promotion it will be extra-parliamentary, RM-flavoured, and — because `regard[Varfell][RM] ≤ −2` has held since the split — Latent RM is already active with `WR −2` applied, which is the Wardens quietly noting whom Varfell abandoned. Nothing in this chain named Varfell, Oastad or the RM in code; every step was a row, a derivation, or a transition.

---

## Appendix — the constants this design chose (◆), in one place

| Constant | Value | Where used |
|---|---|---|
| Advantage unit | `+1 point = +1 die = +1 M`; Ob ±1 = ∓2 points | SET-01 |
| Mandate saturation `K` | 6 (corpus); authored starting Mandates are the calibration target | D-05.08 |
| AP | `2 + FacilityTier + [Standing ≥ 5]` | D-01.11 |
| Π terms | Need weight 1–3 by type; Grudge 1; ambition-in-motion 1 (`progress ≥ ⌈timeline/2⌉`); shock = Accord fall 1 + battle 2 + Turmoil ≥ 7 1 + card deltas; release per card response (Hold Court 2, default 1) + 1 per served Need; decay 1 when no Need is open; seed Π 2 | D-04.10 |
| Suspicion | 0–5; recall at 3; replacement at 5 unless `q_s ≥ Mandate + 1` (emergence offered) | PL-04.02 |
| Seed state | Prosperity/Defense/Order/Tier by type and role as D-04.15; reproduces authored Accord exactly | D-04.15 |
| Piety Yield tier | `{0:0, 1:0, 2:0.1, 3:0.25, 4:0.5, 5:1.0}`; summed then floored with carried fraction | D-07.04 |
| IP advancement | `+⌊count(Accord ≤ 1)/3⌋ + 2[Crown.Stability ≤ 2] + [Torben ≤ 3] + occupied − 1[none unstable ∧ IP > 20]` | D-07.07 |
| PI bands 11–20 | Ascendant 11–14, Supreme 15–19, Deposition 20 | D-07.09 |
| Turmoil | absorbs Public Instability | P-07.05 |
| TT | `100 − MS` | D-07.15 |
| CB life | 3 seasons | P-09.02 |
| Vote side | `sign(regard[voter][proposer] − regard[voter][holder])` | D-09.02 |
| Treaty pool | `Influence + regard[target][actor]` vs target Stability | D-09.08 |
| Forced-breach exemption | hostile unit entered the pledged province this season and was not adjacent at PH-01 | D-09.11 |
| Confessor concurrence | `regard[Church][Crown] ≤ −1 ∨ CI ≥ 65` | D-09.15 |
| Comparable Standing | within 1 | D-10.02 |
| Succession tie | by authored `succession_stat` | D-10.04 |
| Coup predicate | `disposition(Ehrenwall, monarch) ≤ −2 ∧ ∃ candidate` | D-10.05 |
| Insurgency Military | `clamp(count(Order ≥ 2), 1, 3)` | D-10.08 |
| Promotion Accord floor | mean Accord ≥ 2 (0–3 ladder) | D-10.09 |
| Sponsor loss | deterministic on sponsor collapse / renouncing treaty / last province lost | D-10.10 |
| `EINHIR_I_GATE` | 4 | PL-10.05 |
| Consecration override | Himlensendt `scars ≥ 3` → consecrates | D-10.14 |
| Schism selection | lowest Dicastery competence, then lowest Disposition to Confessor | D-08.11 |
| Bishop appointment Order | pin 2; −1 more if `PT_s ≤ 2` | PL-08.03 |
| Supply radius | 4 edges | D-03.07 |
| March | `⌊Military/2⌋ (min 1) + cavalry + skirmish`, cap `+2` | D-03.01 |
| Trespass | CB + regard −1 (no IP change) | PL-03.01 |
| Consolidation AI reply | Resist iff `Defense + garrison ≥ 2` | PL-05.03 |
| Secession AI accept | `Order ≥ 3 ∧ Defense + garrison ≥ 1` | PL-05.02 |
| Greater/Lesser naming | centroid offset from seat; Outer if both offsets < 25% of extent | D-05.13 |
| Cascade functions | attribution = mean degree score × alignment × self-other; cascade alignment cosine ±0.3; expectation deviation `round(2(1 − fidelity))`; shock `0.5·tri(−1,0,1)` only when targeted | D-06.09–13 |
| Temperament drift → α | `α_eff = clamp(α + 0.2·drift, 0.1, 0.9)` | D-05.15 |
| Consolidation recovery | `+1 Stability` on a season with no stat loss, below 5 | PL-06.01 |
| Duty capability match | tag intersection | D-11.01 |
| Exceeding | duty scene also yields a Renown-eligible event | D-11.05 |
| Sufficient Scope | target is an office-holder, a settlement stat, or a clock-relevant NPC | D-11.11 |
| Witness probability | `0.1 × resident NPCs with Standing ≥ 3 not in the operation` | D-11.12 |
| TS lifepath seeds | Northern 5, Central 10, Southern 20; Almud's discovery TS 12 | P-11.06 |
| Coherence | 0–10 | P-11.05 |
| Southernmost Awareness seeds | Varfell 3, Church 2, RM 2, Crown 1, Hafenmark 1; Ritual named *the Closing*; Codex POI *the Askeheim Codex* | SET-07 |
| Fuse | target `U{Lenneth, Torben, Almud}`, season `U{8..12}`; averted at Evidence 5 | PL-12.02 |
| Revelation Renown threshold | 7 | D-12.06 |
| Ministry Collapse card | lowest-competence Ministry | D-12.04 |
| Elske Year-End | `+1` Crown Senator Outward S toward Altonia this year; `−1` IP rose ≥ 10 | D-07.13 |
| Named-character triggers | as completed in D-12.04 | SET-12 |
| Uncontested | no hostile unit in province and no military CB against the holder | D-05.14 |
| Rebased MS bands | 100–73 / 72–60 / 59–40 / 39–20 / 19–1 / 0 | D-07.01 |
