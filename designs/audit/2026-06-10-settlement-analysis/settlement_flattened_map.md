# Settlement Layer — Flattened System Map
**Session 2026-06-09 · companion to `settlement_flowchart.mermaid` + `settlement_state_graph.mermaid`**
**Sources:** `settlement_layer_v30.md` (post-LPS-2e), `valoria_political_hierarchy_v30.md` (PP-726), `settlement_adjacency_v30.md`, `derived_stats_v30.md`, `territory_temperaments_v30.md`, `valoria_geography_v30.yaml`, canonical_sources LPS annotations. Section references are to `settlement_layer_v30` unless prefixed.
**Status tags:** `[C]` canonical · `[P]` provisional · `[PEND]` pending/not canonicalized · `[TBD]` structure canonical, values unset · `[SUP]` superseded text still standing · `[GAP]` hole surfaced by this flattening.

---

## 0. State register (the operands)

| Variable | Range / domain | Tier | Source | Status |
|---|---|---|---|---|
| Type | Seat, City, Town, Fortress, Port, Cathedral, Mine, Outpost (+ registry-extant Village, Fortress-City, Cathedral-City) | settlement | §1.2, §2.1 | [C] table / [GAP] 3 registry types undefined in §1.2 |
| Prosperity, Defense, Order | 0–5 each | settlement | §1.3 | [C]; starting values [P] per ED-SETT-01 |
| Legitimacy (L), Popular Support (PS) | 0–7 each, keyed to controlling faction | settlement | §1.8 | [C] (Jordan ruling 2026-05-30) |
| FacilityTier | 0–3 (Billets/Chambers/Suites/Wings highest built) | settlement | §1.8, §1.4 | [C] |
| Facility slots | per-type Wing/Suite/Chamber/Billet caps | settlement | §1.4.1 | [C]; no Village / Fortress-City rows [GAP] |
| Church axes | Building {None, Chapel, Church, Cathedral}; Templar 0/1; Inquisitor 0/1; Church Governor 0/1 | settlement | §1.5 | [C] |
| Governor slot | vacant / NPC / PC / subnational / Bishop / Church (Pastoral) | settlement | §3 | [C] |
| Garrison | 0–1 military unit (Discipline feeds defense) | settlement | §5.2 | [C] |
| Sub-features | per-feature registry effects | settlement | §2.2 | [C] |
| Local Actors | 0–2 NPCs, Disposition each | settlement | §4.5 | [C]; Village count undefined [GAP] |
| Fieldwork Depth | 0–3+ per settlement (Exposure stays per province) | settlement | §4.1 | [C] |
| Emergent flags | BlackMarket, IntelBroker, ThreadSite | settlement | §4.7–4.9 | [C] |
| Geographic | coords, terrain, radiation band, march edges | settlement | geography YAML | [C] for old 36 IDs; **21 new spokes have no entries** [GAP] |
| Weight W_s | 1–11 (derived) | settlement | §1.8 | [C] |
| Accord | 0–5 (derived) | province | §1.3 | [C] |
| Fracture state | Unified / Fractured (named sub-provinces) | province | hierarchy §2.3 | [C] rule; triggers [TBD] |
| Temperament | α/β pair, 5 typologies | province | temperaments §2 | [P]; settlement grain deferred Stage 6b |
| Mandate | 0–7 (derived) | faction | §1.8 | [C] |
| Treasury | 0 – Wealth×100 | faction | derived_stats §8 | [C] |

---

## I. Inputs

### I.A Governor actions — 1 free per season (player Duty = governance; companion-governor: 1 free action, social OR governance, per C-04) `[C]` §3.2

| Action | Pool | Ob | Success effect |
|---|---|---|---|
| Develop | Cognition + Wealth-relevant History | floor(Prosperity/2) + 1 | Prosperity +1 (cap: type max) |
| Fortify | Military-relevant stat + History | floor(Defense/2) + 1 | Defense +1 (cap: type max) |
| Pacify | Charisma + local History | floor((3 − Order) + 1), min 1 | Order +1 (cap 5) |
| Administer | Attunement + Governance History | 2 | No Order decay this season; reveals one local NPC's active Conviction |

Calibration `[P]` per ED-SETT-02 (proposed: pool = governor's primary stat; Ob 2 standard / 3 recovery / 4 crisis). NPC governor tree: Pacify → Develop → Fortify → Administer, faction-tree override at Stability ≤ 2 (ED-SETT-06).

### I.B Domain Actions `[C]`
- **Assign governor** — Duty system, Standing gate (see III.D).
- **Grant subnational management** — Influence, Ob 1.
- **Revoke subnational management** — Influence, Ob = subnational Influence ÷ 2 (round up); costs Order −1 + Disposition −2 with that faction (§3.3).
- **Expand Institutional Capacity** — Treasury −300, +1 Wing, ≤ 1 per settlement per decade (§1.4.3).
- **Ecclesiastical Appointment** — installs Bishop-Governor (Church NPC tree); province fractionalizes if settlement controller now differs from Seat holder (§3.2, PP-TBD).
- **Pastoral Assumption** — Church installs Church Governor at Ob 1 where settlement has no governor AND ≥ Chapel; Provincial Authority (tax/military/legal) unaffected; revocable per §3.3 rates (§1.7).

### I.C Military `[C]` §5, adjacency §1–3
- **March** — armies occupy one settlement; movement owned by `march_layer` (budget 100 px/season × Military point; cavalry ×1.5; skirmish ×1.3; A* over terrain costs; Casus Belli check on inter-faction edge crossing). Local "1 edge/season, Military÷2 edges" text in adjacency §1.3 `[SUP]` by ED-780 migration.
- **Assault** — Military vs Defense + garrison Discipline. Fail: repelled with casualties.
- **Siege** — requires Military ≥ Defense; no roll; defender Order −1/season → surrender at 0; attacker pinned while besieging.
- **Bypass** — requires Military > Defense + 2; bypassed garrison raids supply each season (Military vs Ob 1 → invader units in province −1 Discipline). Fortress: no bypass unless Military exceeds Defense by 3+.
- **Garrison placement** — one unit per settlement.
- **Auto-capture** — Defense 0 + ungarrisoned + hostile entry, no roll.

### I.D Church infrastructure `[C]` §1.5–1.6
Axis builds and their per-season emissions: Chapel +0.5 PT, Church +1 PT, Cathedral +2 PT (+0.5 PT adjacent territories); Templar +1 CI/season + rival-DA interrupt (+1 Ob, costs 1 CI); Inquisitor → practitioner Concealment test/season, RM governance +1 Ob, RM cultural presence → 1 Church Attention/season; Church Governor → settlement governs on Church stats (removal: Mass Battle, Mandate Challenge Ob 6+, or RM community action at OW). Parish Order bonuses: Chapel +0.5 Order/season (rounds: +1 every other season); Church +1 Order one-time; Cathedral +1 Order install + Order decay −1. Seizure-Ob modifiers (stacking, per settlement): Chapel −0 · Church −1 · Cathedral −2 · Templar −1 · Inquisitor −1 · Church Governor −2 · **cap −4**.

### I.E Thread operations (Relational+ scale; Object/Personal = no settlement effect) `[C]` §4.4 — cap ±1 per stat per season

| Operation | On success | On failure |
|---|---|---|
| Weaving | Order +1 | — |
| Pulling | — | Order −1 |
| Past-Oriented Pulling | — | Prosperity −1 |
| Dissolution | — | Defense −1 AND Order −1 |
| Mending | Prosperity +1 | — |
| Community Organizing | Order +1 AND Prosperity +1 (province PT ≤ 2) | — |
| Lock | Defense +1 | — |

### I.F Faction-political inputs `[C]` §1.8
- Mission outcomes (cascade-fidelity / procedural / violation ΔL, ΔPS) apply uniformly to the faction's held settlements, clamped 0–7, then re-aggregate.
- Mandate feedback drift each Accounting: q_s ≥ 1 **below** Mandate → L +1 (cap 7); q_s ≥ 1 **above** → PS −1 (floor 0); max ±1 per settlement per season, inside the ±2 faction seasonal cap. Negative (stabilizing) feedback, Stage-4 sim-verified bounded/convergent over 30 seasons.

### I.G Seasonal / clock inputs `[C]` §4.3, §7
- Event roll: 0–1 per settlement per season off the §4.3 trigger table (see II.D).
- Order decay: a baseline seasonal decay exists (Administer suppresses it; Ministry management and Cathedral set decay −1) — **rate unstated in read set** `[GAP]`.
- Unmanaged settlement: Order −1/season until governor assigned (§7.2).
- Clocks touching settlements: IP halved to +1/2 seasons; Generational Shift +1 per 5 years (thresholds 2/4/6 → leaders −1/−2/−3 highest attribute; Thread Sensitivity ≥ 50 exempt per P-15); MS, CI, Political Stability unchanged (§7.1).

### I.H Geographic constants `[C]` geography YAML
56-edge settlement adjacency (28 intra-province: 7 triangles + 7 singles; 28 inter-province incl. Valorsplatz↔Schoenland sea-edge + 3 resilience routes); ≥2-connection rule (Schoenland degree-1 foreign-exempt pending ED-055); province-tier adjacency retained for strategic routing; terrain cost matrix (mountain 999 impassable, pass 2.0, bridged crossing 1.0); radiation bands centered Askeheim; Forgetting-zone polygon; Altonian passes. Thread-Witnessed edges absent from the PP-726 graph — survives only as march_layer §3.4 scouting (no army transport).

---

## II. Calculations & mechanics

### II.A Aggregation pipeline (the load-bearing math) `[C]` §1.8, §1.3, derived_stats §8
```
W_s      = base(Type) + Prosperity_s + FacilityTier_s            # 1–11
           base: Seat 3 · City 3 · Cathedral 3 · Town 2 · Fortress 2 · Port 2
                 Village 1 · Mine 1 · Outpost 1
                 (Cathedral-City → 3 either reading; Fortress-City UNRESOLVED 2 vs 3 [GAP])
q_s      = 0.5·L_s + 0.5·PS_s                                    # 0–7
T        = Σ_held W_s · (q_s / 7)
Mandate  = clamp( round( 7·T / (T + K) ), 0, 7 ),  K = 6         # saturating → Lesson-5 bound
agg_L    = Σ W_s·L_s / Σ W_s ;  agg_PS = Σ W_s·PS_s / Σ W_s      # strictness consumers
Accord_p = floor( mean(Order over province settlements) )         # single → passthrough; Seat +1 tie-break (ED-SETT-03)
Income   = Σ_held Prosperity × 10 gold/season                     # derived_stats §8.1
LegMeter = Mandate × 20  (0–140; per-system buffer, no 0–100 master scale)
PolValue = Σ territory_value + Σ province_unification_bonus       # structure [C], scalars [TBD] (hierarchy §2.4)
EffDef   = Defense + garrison Discipline                          # §5.2
```
Degenerate cases `[C]`: zero holdings → Mandate 0; N=1 province computes normally; embedded faction N/A until it holds settlements; Restoration sums T over Presence localities (community grain, FSA §6 / PP-460).

### II.B Settlement derived values `[PEND]` — derived_stats §9 "not canonicalized"
Local Economy = Prosperity × 50 · Garrison Strength = Defense × 20 + Fort Level × 30 · Public Order = Order × 20. Stat-damage rule (stat −1 only when its derived value sits at 0 through Accounting, §1.3) is **gated on this pending layer** — until §9 canonizes, settlement stat damage has no operating substrate `[GAP]`. §1.3's gloss of ×50 as "income contribution" conflicts with the canonical ×10 rollup (prior-session finding C).

### II.C Modifier & trigger tables `[C]`
**Battle (adjacency §2.2):** traversed edge — River −1D attacker · Mountain Pass −1D attacker · Coastal strips Fort positioning · Road none. Settlement type — Fortress +Fort Level to defender Ob · Seat +1 defender Discipline · Port +1D defender if naval reinforcement · Cathedral attacker takes Church Casus Belli · Mine attacker captures Prosperity · Town/Outpost none. Consequences — settlement Order −1; Prosperity −1 on Partial-or-worse assault; MS/Strain/IP apply peninsula-wide unchanged.
**Events (§4.3):** Prosperity 0 → famine, Order −1 · Defense 0 + adjacent hostile → raid/siege, mandatory scene if player present · Order 0 → revolt, governor expelled unless garrison · Order 5 ∧ Prosperity 4+ → flourishing, +1 Disposition all local NPCs · RM control → Governance Transition (Disestablishment / Accommodation / Transformation, see state graph) · RM-governed emergency DA → Consensus Delay +1 season (waive: 1 Mandate + 1 Presence marker) · Cathedral + CV change → religious event · Mine ∧ Prosperity 3+ → Treasury +50/season · Fortress + hostile in province → mobilization, Defense pool vs Ob 2.
**Subnational management passives (§3.3):** Church (Cathedral) +1 Piety Influence/season · Guilds +1 Trade/season · Ministry Order decay −1 · Löwenritter Defense +1 passive · RM CV −1 potential/season (PT ≤ 2, covert option) · Wardens RS detected 1 band earlier · Niflhel covert infiltration +1D intel (detected at Evidence 3). RM cell resilience: ≥3 Presence settlements in province → +1 Ob on Church/Crown suppression there (stacks with Inquisitor's +1 Ob to organize).
**Local Actor Disposition drivers (§4.5):** governs well/Order up +1 · Order down −1 · sponsor event +1 · public combat −2 · defends vs invasion +2 · controller change → reset 0 · Conviction fulfilled +1.
**Emergent conditions (§4.7–4.9):** Black market — emerge at Order ≤ 1 ∨ no governor, vanish at Order ≥ 3; effects "Wealth +0.5 / Accord −0.5" (denominated in non-settlement stats — vocabulary drift, prior finding). Intel broker — Prosperity ≥ 3 ∧ (no governor ∨ governor Stability ≤ 2); sells/fabricates intel, can be killed/bought/turned. Thread exploitation site — Thread Proximity ≤ 2; harvest = RS −0.5/harvest/season, harvester Wealth +1; discovery via Investigation.
**Temperament (temperaments §2–4):** five typologies (α,β): pragmatic .7/.3 · traditional .3/.7 · balanced .5/.5 · principled .2/.8 · outcomes-only .9/.1; faction aggregate = population-weighted mean (uniform interim); drift += 0.1 × strain_delta, clamp ±1, toward outcomes-only.

### II.D Progression numbers `[C]` §6, §7.2
Declaration roll: Influence pool = Renown ÷ 2, Ob 3. Founded faction (ED-790): L 2 · PS 3 · Influence floor(Renown÷2) · Wealth 2 + (settlements − 1) cap 5 · Military 1 · Intel 2 · Stability 3. Cross-generational inheritance: protégé requires Disposition +4 ∧ Standing 4+; successor starts Standing 0 with Renown ÷ 2 (round down).

---

## III. Sequences & gates

### III.A Seasonal Accounting — firing set `[C]` items, ordering `[GAP]`
Fires each Accounting (canonical intra-Accounting **ordering is unspecified** across the read set): parish Order bonuses · baseline Order decay (rate unstated) unless Administer/Ministry/Cathedral · unmanaged −1 Order · siege tick −1 Order · Mandate↔L/PS mean-reverting drift (±1, inside ±2 faction cap) · faction income Σ P×10 (+ mine surplus +50) · settlement event roll 0–1 · black-market / broker emergence-disappearance checks · stat-damage check (derived value at 0 through Accounting — inert while §9 pending) · Consensus-Delay maturation · temperament drift recompute · Generational Shift on 5-year boundaries.

### III.B Invasion sequence `[C]` §5.1, adjacency §3
1. Army enters province **via the traversed edge** — engagement is path-constrained, no free choice of target.
2. At each settlement: declare **Assault / Siege / Bypass** (gates per I.C).
3. Mass battle resolves at the settlement node (mass_battle Part B) with edge + type modifiers.
4. **Seat captured → provincial control transfers.**
5. Non-Seat settlements with Order ≥ 3 may resist as holdouts (collapse variant adds governor Disposition ≥ +3); reduce individually or grant autonomy.

### III.C Governance sequences `[C]` §3
**Assignment gate:** Standing 0–2 none · 3 Town/Outpost · 4 City/Fortress/Mine · 5 Seat/Cathedral (+ leader approval). **Grant → manage → revoke/contest:** grant Ob 1 → subnational governor replaces faction governor (Provincial Authority retained) → revoke at Ob = Influence÷2 with Order −1 / Disp −2, or contested via asymmetric social contest (province as institutional authority). **Vacancy:** governed → unmanaged (Order −1/season) → reassignment, or Pastoral Assumption (Ob 1, Chapel+) → Church governance until revoked.

### III.D Capacity-pressure sequence `[C]` §1.4.3
Standing 6 reached, Wings full → (a) a holder departs (death/exile/Generational Shift), or (b) Expand Capacity (−300, +1 Wing, decade cap), or (c) Prince-in-Waiting: Std-6 privileges, seasonal Disposition contest vs Ob 2, failure reverts to Standing 5.

### III.E Hard gates (boolean) — consolidated
| Gate | Condition | Source |
|---|---|---|
| Auto-capture | Defense 0 ∧ no garrison ∧ hostile entry | §5.2 |
| Siege declarable | Military ≥ Defense | §5.1 |
| Bypass | Military > Defense + 2 (Fortress: > Defense + 3) | §5.1 |
| Province control flip | Seat captured | §5.1 |
| Holdout | Order ≥ 3 (∧ gov Disp ≥ +3 in collapse) | §5.1, §6.3 |
| Revolt | Order = 0 (garrison suppresses expulsion) | §4.3 |
| Black market on/off | Order ≤ 1 ∨ no governor / Order ≥ 3 | §4.7 |
| Pastoral Assumption | no governor ∧ Building ≥ Chapel | §1.7 |
| Wing advancement | free Wing slot at the Seat | §1.4.2 |
| Stage 2→3 | 2+ settlements ∧ Renown 5+ ∧ 2 officers Disp +3 | §6.2 |
| Stage 3→4 | 4+ settlements / 2+ provinces ∧ Renown 7+ ∧ 1 Seat ∧ Declaration Ob 3 | §6.2 |
| Stage 4→5 | 2+ Seats ∧ Renown 9+ ∧ Parliament seat | §6.2 |
| City-state survival | leader alive ∧ in personally held settlement | §6.3 |
| Dissolution | leader dead/captured ∧ no successor Std 4+ | §6.3 |
| Fracture / reunify | mixed faction alignment / common alignment restored (event triggers [TBD]) | hierarchy §2.3 |
| Victory (Accord leg) | Accord ≥ 2 in **all** provinces | §8.1 |
| Generational exemption | Thread Sensitivity ≥ 50 | §7.1 |

---

## IV. Outputs (by consumer)

| Output | Computed from | Consumer | Status |
|---|---|---|---|
| Province Accord | floor(mean Order) | victory gate (≥2 all provinces); peninsular_strain rules now act via settlement Order | [C] |
| Faction Mandate | saturating W-weighted L/PS aggregate | Parliament votes; Legitimacy meter ×20; d+σ resolver (resolution side, ED-865/874) | [C] |
| aggregate_L / aggregate_PS | W-weighted means | PE strictness = base + 0.5(L/7) − 0.3(PS/7) | [C] |
| Treasury income | Σ Prosperity × 10 (+ mine +50) | faction Treasury (cap Wealth×100; Treasury-0 path → Wealth −1) | [C] |
| Political value | Σ territory_value + unification bonus | parliamentary influence, Mandate-track inputs | [TBD] scalars |
| Battle parameters | EffDef, edge/type modifiers, Fort Level | mass_battle Part B at the node | [C] |
| Scene Slate entries | events (Priority 4), Local Actors (Priority 5), Slate anchoring | scene generation, player loop | [C] |
| Clock flows | PT (buildings), CI (Templar), CV (RM), RS (sites/harvest), Church Attention (Inquisitor), Trade (Guilds), Piety Influence (Cathedral mgmt) | church/threadwork/economy layers | [C] |
| Intel affordances | Niflhel +1D, brokers, Warden early RS detection, Watchtower vision | investigation / fog-of-war | [C] |
| Population feedback | Local Actor Disposition | governance legibility; Stage-2→3 recruitment pool | [C] |
| Settlement derived meters | ×50 / ×20+Fort×30 / ×20 | videogame UI layer | [PEND] |
| Temperament aggregate | pop-weighted province values | faction_behavior strictness/conduct weighting | [P] |

---

## V. Holes the flattening surfaced (beyond the prior session's A–G findings)

1. **Intra-Accounting ordering unspecified** — the III.A firing set has no canonical sequence; drift-before-income vs income-before-drift etc. is implementation-significant (e.g., siege tick vs revolt check vs parish bonus ordering decides whether a settlement surrenders or riots first). `[GAP — needs a ruling or an explicit "order-independent by design" statement]`
2. **Baseline Order decay rate unstated** — three mechanics modify "Order decay" (Administer, Ministry, Cathedral) but no read source states the base rate it modifies. `[GAP]`
3. **Stat-damage substrate inert** — §1.3's settlement stat-damage rule routes through derived values that derived_stats §9 marks PENDING; until canonized, settlement stats have no damage path other than direct effects. `[GAP]`
4. **Fortress-City Weight base unresolved** (2 vs 3) — Ehrenfeld is precisely where W matters. `[GAP]`
5. Carried from prior analysis: 21 spoke settlements without geographic/stat data (A); adjacency prose doc one PP behind (B); ×50/×10 gloss (C); old-ID residue in spine doc Parts 1, 3–7 (D); Village/Fortress-City/Cathedral-City absent from §1.2/§1.4.1/§4.5 (E); CI 75-cap vs CI-100 trigger tension (F); stale indices + empty infill (G).

*Map complete to the read set; nothing herein is asserted beyond the cited sources.*
