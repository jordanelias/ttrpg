<!-- Analysis / survey document — NOT a ratification. Cites existing EDs; rules nothing new. -->
# World-State Primitive Registry — writers, readers, and module I/O

## Status: ANALYSIS (survey only — no canon change; flags existing open items, rules nothing)
## Created: 2026-07-19 · Lane: IN (cross-cutting)
## Sources: `references/module_contracts.yaml` (I/O spine), `references/descriptor_registry.yaml` (pointer roster), `designs/provincial/clock_registry_v30.md` (clocks/tracks), `systems/_architecture/key_type_registry_v30.md` (the 49-type shared-outcome bus), and each subsystem's current head per `CURRENT.md`.

---

## 0. Purpose — fighting complexity/opacity by transposing chains into primitives

The corpus already documents how the game works, but almost entirely as **chains**: module A
emits event X, module B consumes X (that is exactly what `module_contracts.yaml` and
`key_type_registry_v30.md` encode). Chains are how the engine *runs*, but they are the wrong index
for *understanding state*: a single primitive like **Mandate** or **MS** is touched by a dozen
different chains, so its full behaviour is smeared across the whole corpus and never visible in one
place. That is the opacity.

This document is the **transpose**. The organizing unit is the **primitive** — one named state
variable — and for each one it gathers, in a single row:

- **← Writers (what is digested into it):** every module + action + event that *modifies* the value.
- **→ Readers (what is exported from it):** every module, gate, or derived value that *depends on* it.

If you want to know "what is influencing and managing the state of the game world," Part A is the
answer: it *is* the world state, enumerated, with its full write/read surface. Parts B–D keep the
older lenses (module I/O, chains, the shared bus) as cross-references.

**Bucket taxonomy** (from `descriptor_registry.yaml`): `[A]`ttribute (base 1–7 input) ·
`[D]`erived (computed, write-protected) · `[T]`rack (bounded, bidirectional) · `[C]`lock (bounded,
threshold-gated) · `[P]`ool (spent per action). A **primitive** = a pointer that should resolve
through the descriptor registry (Key-substrate A17), never a hardcoded literal.

---

# PART A — THE PRIMITIVE REGISTRY (organized by primitive, not by chain)

Grouped by scale band. Within each row: **Owner** = the one module that may write it authoritatively;
**← Writers** = everything that digests into it; **→ Readers** = everything that exports/derives from it.

---

## A1 · PENINSULA / WORLD primitives (the top-level state everyone radiates from)

| Primitive | Owner | Bucket · Range | ← Writers (digested in) | → Readers (exported out) |
|---|---|---|---|---|
| **Mending Stability (MS)** | ⚠️ *ownerless* (multi-writer) | `[C]` 0–100, start 60 | threadwork ops (Weaving ±1/−2, Pulling −1/−2, POP −3, Locking −1/−3, Dissolution −3/−8, **Mending +1/+2**); mass_battle Substrate Fracture −1; Calamity drift — canon flags MS *unowned* (victory reads it as an "unowned clock"; threadwork `state[]` omits it) | victory (MS=0 Post-Calamity, ≤5 Second Calamity, →20 recovery); territorial_piety CV drift; threadwork op Ob scaling; scene_slate Thread-State scenes; articulation |
| **Institutional Pressure (IP)** | peninsular_strain | `[C]` 0–100, start 20 | peninsular_strain accounting (rises from low-Accord territories); mass_battle deferred IP advance; **Crown "Diplomatic Outreach to Schoenland" reduces** | victory (IP=100 Occupation P1; ≥85/≥80 for 3s → P2/P3; <85/<75 stalls); Trade Ob (+1 if IP≥30) |
| **Turmoil** | peninsular_strain | `[C]` 0–10, start 0 | peninsular_strain accounting; battle aftermath (Campaign/War) | victory era reads; articulation (replaces retired Parliament Integrity) |
| **Church Influence (CI)** | territorial_piety | `[C]` 0–100, start 28 | territorial_piety generation (Piety Spread, CV); faction **Assert +1**, **Suppress negates gain**; seasonal cap | ci_political (Political Pool = f(Mandate,CI)); victory; Parliamentary Stay (gated CI<55); Theocracy Unification at CI=100 |
| **Season counter** | engine_clock | `[C]` | engine_clock tick | **all** (accounting cadence) |

---

## A2 · FACTION / PROVINCIAL primitives (the strategic-layer state)

| Primitive | Owner | Bucket · Range | ← Writers (digested in) | → Readers (exported out) |
|---|---|---|---|---|
| **Mandate** | faction_state | `[D]` 0–7 (derived) | **settlement L/PS aggregate** `clamp(7T/(T+6),0,7)`; social_contest Domain Echo (±); parliamentary Sanctions (Censure −1, Outlawry −2, Recognition-Challenge, Combined −1) | settlement_layer drift feedback (±1/settlement/season); ci_political Political Pool; victory (all-dissolved→Anarchy); Treaty ratification `M=Mandate−2`; Resistance Check; DA Obs; Faction-Legitimacy `Mandate·20` |
| **Treasury** | faction_state | `[D]` (×100) | **Σ settlement Prosperity·10**; DA economic outcomes; Ransom (−2/general); Fiscal Stance (PROPOSED) | DA affordability; Ransom; upkeep |
| **Influence** | faction_state | `[A]` 1–7 (floor 1) | DA outcomes; accounting derived-value-at-0→stat−1; battle/political effects | Treaty/Diplomacy/Parliamentary Obs (floor Inf/2); Resistance Check `M=Inf−…`; pools |
| **Wealth** | faction_state | `[A]` 0–7 | Trade/economic DA; Embargo −1/s, Blockade −2/s; Subsidy +1 | Govern/Trade Obs; Levies; upkeep |
| **Military** | faction_state | `[A]` 0–7 | Muster; battle losses; War-Auth | Blockade gate (Mil 3); Martial-Governance; Commander bonus `floor(Mil/2)`; Levies |
| **Intel** | faction_state | `[A]` 0–7 | Spy/Investigate outcomes; Intel-Advancement Counter (resets +1 at 4) | Spy Ob (floor target Intel/2); Counter-Intelligence; Intelligence-Holdings buffer |
| **Stability** | faction_state | `[A]` 0–7 (0=eliminated) | Censure −1, Blockade −1, Outlawry −2; Suppress-fail −1; Ransom-refuse −1; env shocks | Faction-Discipline `Stability·10`; Diplomacy Ob (floor Sta/2); succession; victory |
| **Faction rank Standing** | faction_politics | `[T]` 0–7 ⚠️ | promotion/demotion/succession/exile; magnitude 1–3 | player action gates; sub-office ladders; `state.standing_change` — ⚠️ BG faction/political Standing is **0–5** (P-15): open scale divergence |
| **Faction Legitimacy (buffer)** | faction_state | `[D]` 0–140 `Mandate·20` | Mandate | Mandate-loss absorption buffer — distinct from settlement `set.legitimacy` (0–7) |
| **Faction Discipline (buffer)** | faction_state | `[D]` 0–70 `Stability·10` | Stability | Stability-loss buffer — distinct from unit Discipline (1–7) |
| **Levies Available** | faction_state | `[D]` | Wealth / Military | Muster ceiling |
| **Intelligence Holdings** | faction_state | `[D]` | Intel | Spy / counter-intel reserve |
| **Reputation** | faction_state | `[T]` 0–5 (BG, P-14) | conduct | Rep≥3 → +1 starting Disposition (fieldwork §5) |
| **Casus Belli** | faction_state | `[C]` per-faction (cap 1/target) | seizure; Outlawry rider; parliament/treaty breach | −1 Ob to a Military action (consumed on use) |
| **Thread Debt** | faction_state | `[C]` per-token (territory) | thread-op token issuance | tokens >1 season old → MS/RS −1/token |
| **CI Political Pool** | ci_political | `[P]` | Church `Mandate+floor(CI/20)`; opp `max(0,Mandate−floor(CI/30))` | Parliamentary vote resolution |
| **Faction-specific tracks** | faction_state | `[T]` | per-track (Torben/Elske Loyalty, Löwenritter Autonomy, Popular Will, Warden Coop/Recognition, Intel-Advancement, Guild Favour, Cardinal Influence, Ministry tokens) | faction behaviour, victory paths, unique cards |

---

## A3 · SETTLEMENT / TERRITORY primitives (the base of faction power)

| Primitive | Owner | Bucket · Range | ← Writers (digested in) | → Readers (exported out) |
|---|---|---|---|---|
| **Legitimacy (L)** | settlement_layer | `[T]` 0–7 (per-settlement) | Keep-Order(force −PS), Levy −L, §1.8a grain events, Directive-Defy +PS, **Mandate drift feedback ±1** | Mandate formula `q_s=0.5L+0.5PS`; governance/treaty Obs (floor L/2) |
| **Popular Support (PS)** | settlement_layer | `[T]` 0–7 | Fortify-militia +PS, Keep-Order-consent +PS/force −PS, Levy −PS, Directive-Defy +PS, Mandate drift ±1 | Mandate formula (paired with L) |
| **Prosperity** | settlement_layer | `[T]` 0–5 | **Develop +1**; da.economic_intervention; env.disaster/population_change − | Local Economy `Pros·50`; **Treasury `ΣPros·10`**; Mandate weight `W_s`; Govern/Develop Obs |
| **Defense** | settlement_layer | `[T]` 0–5 | **Fortify +1** (garrison/militia/walls) | Garrison Strength `Def·20+Fort·30`; auto-capture gate (Def=0) |
| **Order** | settlement_layer | `[T]` 0–5 | **Pacify/Keep-Order +1**; battle defender −1; Levy −1; Bind-Cells +1 | Public Order `Order·20`; **revolt gate (Order=0)**; province Accord `floor(mean Order)`; IP/Strain feed |
| **Facility Tier** | settlement_layer | `[A]` 0–3 | development/investment | Mandate weight `W_s`; Administration Points `AP=2+FacilityTier` |
| **Fort Level** | territory_stats | `[A]` 0–4 | Fortify (territory); geography seed | Garrison Strength `+Fort·30`; occupy Ob `2+Fort` |
| **Accord** | peninsular_strain (per-territory) | `[T]` 0–3 | conquest→1; governance; battle defender Order−1 | revolt eligibility (0); IP/Strain advance; victory; Duty Governance |
| **Piety Track (PT/CV)** | territorial_piety | `[T]` 0–5 (per-territory) | Piety-Spread +1; Cultural Reclamation −1; thread/Calamity drift | **CI generation**; temperaments; Church victory |
| **Administration Points** (admin-AP) | settlement_layer (redesign) | `[P]` 2–5 | `=2+FacilityTier`; Retain-Clerks +1/Clerk | governance verb budget/season — ⚠️ acronym "AP" collides with Church Attention Pool below |
| **Church Attention Pool** (AP) | territorial_piety / Church | `[C]` 0–10 per-territory | failed deep Survey; Niflhel / heresy activity; Active Inquisition | First Inquisitor at AP≥3; second at AP≥6 |
| **Guild Favour** | settlement_layer | `[T]` 1–7 | Guild contracts/Ordenanza | Guild contract access; player Resources |
| *derived (ro):* **Local Economy** `Pros·50` · **Garrison Strength** `Def·20+Fort·30` · **Public Order** `Order·20` · **province Accord** `floor(mean Order)` · **Settlement Weight** `W_s` — writers = their inputs above; readers = income, defense math, riot gate, Mandate | | | | |

---

## A4 · PERSONAL — character state primitives

| Primitive | Owner | Bucket · Range | ← Writers (digested in) | → Readers (exported out) |
|---|---|---|---|---|
| **Attributes** (Str/End/Agi/Foc/Acu/Will·Spi/Att/Cha/Bonds) | actor substrate | `[A]` 1–7 | character build; legacy/growth | every personal pool + derived value |
| **Health** | personal_combat | `[D]` (ro) | ⚠️ **canonical = combat_engine_v1** `round(WI·(MW+1)+0.25·Str·End) − cumulative_damage`, `WI=round(End+4+0.4·Spi)` (module_contracts §827-838). The v30 `(End+6)(MW+1)` 13–55 form is SUPERSEDED; range itself diverges in canon (13–55 clock_registry / 14–48 core.md / sigma engine) — flagged | felling gate (Health=0→`scene.combat_felled`) |
| **cumulative_damage** | personal_combat | `[T]` | combat_hit accrual (the substrate every Health delta lands on — **F1 guard**, never write Health directly) | Health derivation; Wounds `min(floor(cum/WI),MW+1)` |
| **Wound Interval / Max Wounds** | personal_combat | `[D]` | `WI=round(End+4+0.4·Spi)`; `MW=min(floor(End/2)+1,3)` | Health formula; Wounds cap |
| **Wounds** | personal_combat | `[T]` 0–max `floor(End/2)+1` | combat_hit accrual | bilateral-Ob penalty (+0.15 atk/+0.25 def, ED-1041) |
| **Initiative (Vor/Nach)** | personal_combat | `[T]` (continuous, decaying) | disposition lean; hit-gains; Indes steals | exchange-order; who acts first |
| **Poise / structure (kuzushi)** | personal_combat | `[T]` (per-beat) | overcommit/bind/hit degrade −; per-beat regen + | structure-break; mode availability |
| **Stamina** | personal_combat | `[P]` 5–47 `3·End+2·Spi` | exertion; Take-a-Breath +End | combat action economy |
| **Resolve** | actor substrate | `[D]` 1–7 (`Spirit`) | Spirit | **Inspiration** pool ceiling (core.md §Resolve) |
| **Inspiration** | actor substrate | `[P]` 0–Resolve | narrative earn | spendable re-roll/boost (fieldwork Inspiration Spend) |
| **Composure** | actor substrate | `[D]` 3–21 `Cha·3` | knot_ruptured −5; contest strain | contest survival; Rattled marks |
| **Concentration** | social_contest | `[P]` 5–35 `3·Foc+2·Spi` | −5/exchange, +5 loss | Spent gate (0→−2D self) |
| **Momentum** | actor substrate | `[T]` 0–4 | Rescue +2; contest wins | spendable bonus dice |
| **Coherence** | threadwork | `[T]` 0–10 | thread ops (−0/−1/−2 by scale, FR surcharge); Knot-Anchoring +1; Dissolution Residue −1 | thread op eligibility; practitioner weaving |
| **Thread Fatigue** | threadwork | `[C]` 0→Spi·5 | thread ops (Leap 3, Mending 4/r, Pulling 5/r, Locking 7/r, Dissolution 10/r) | contact-break threshold |
| **Thread Sensitivity (TS)** | actor substrate | `[A]` 0–100 | growth | TPS `floor(TS/10)`; op eligibility (TS≥30/50); Concealing Ob |
| **Truth** (formerly Certainty) | conviction_track | `[T]` 0–5 | metaphysical-stance events (ED-IN-0075; consolidates retired piety meter) | qualitative bands (player-visible); Solmund/Thread pole |
| **Conviction Scars** | conviction_track | `[C]` per-conviction (indelible) | witnessed events at thresholds (thread/violence/betrayal) | Scars=2 Resonant-Style; ≥3 crisis→arc; npc/faction reaction; Renown |
| **Convictions** (13-vector) | actor substrate | by-ref (0–1 weight) | background templates; legacy | armature dot-product (significance); contest style; NPC decisions |

---

## A5 · PERSONAL — relationship / investigation / progression primitives

| Primitive | Owner | Bucket · Range | ← Writers (digested in) | → Readers (exported out) |
|---|---|---|---|---|
| **Disposition** | fieldwork | `[T]` −5..+5 (per-NPC-per-PC) | Converse/Connect/Impress/Gift/Negotiate +; knot_ruptured −3; Demand-refuse −1; decline-outreach −1; Sincerity-fail | Interview depth gate (+3); NPC Outreach (≥+2); Demand (≤−2); Knot formation (+5); Hold-Court |
| **Bonds** | fieldwork | `[T]` (capacity) | Connect | Knot eligibility (≥5); Knot Count `floor(Bonds/2)+1` |
| **Knot Strain** | fieldwork | `[C]` −5..+5 | knot use +1/each; decay −1 (Disposition≥+3, no new strain) | Knot Break (>capacity / +5) |
| **Evidence Track** | fieldwork | `[C]` 0–threshold (3/5/8) | Examine/Interview/Research/Surveil/Thread-Read +0..+3 | Reconstruct→Finding; Investigate-Duty threshold; Pre-Contest citation +1D |
| **Exposure** | fieldwork | `[C]` 0–10+ | failed rolls, Thread-Read, Surveil +2, hostile-time; − concealment/leave/season | Cover thresholds (Noticed/Watched/Compromised); Subversion risk |
| **Cover** (derived) | fieldwork | `[D]` 2–14 `Acuity+History` | attributes | Exposure threshold scaling |
| **Persuasion Track** | social_contest | `[C]` 0–10 (per-contest) | CLASH/REINFORCE/CROSS margins; Regroup/Concede +1; Doubt-Marker | resolution (≥7/≤3 terminal, ≥9/≤1 Total); Obligation clocks |
| **Face** | social_contest | `[D]` `Cha·3` (Standing-scaled) | contest strain accrual; CR5 backfire | Rattled marks; contest standing buffer |
| **Doubt Marker** | social_contest | flag | Obscuring win | −2 opponent next margin / terminal apply |
| **Standing** (player) | player_agency | `[T]` 0–7 (faction) | Duty success/exceed; leadership-challenge; promotion/demotion | player action gates (Std 2–7); Face; `state.standing_change` |
| **Renown** | player_agency | `[T]` 0–10 | Renown actions +1 (cap +2/s: Conviction resolved, Duty exceeded, Domain Echo, Scar caused, Investigation, Battle, Accord+, Knot) | Independent DA pool (≥7 `floor(Renown/2)`); Grand Contest (≥9) |
| **Resources** | player_agency | `[T]` 0–5 | Guild contracts +1..+3 | Equipment/Bribe/Hire/Upgrade/Leverage costs (1/1/2/3/3) |
| **Obligation clocks** | social_contest | `[C]` per-obligation | Decisive Formal/Grand win | binding cross-season commitment; violation trigger |

---

## A6 · MASS-BATTLE unit primitives (scene-scale, per-sub-unit)

| Primitive | Owner | Bucket · Range | ← Writers (digested in) | → Readers (exported out) |
|---|---|---|---|---|
| **Command** | mass_battle | `[A]` 1–7 (general-derived) | general's Cha/Cog | sub-unit limit; Discipline ceiling; Morale start/floor; tactic Obs |
| **Discipline** | mass_battle | `[T]` 1–7 (per-sub-unit) | own Size-loss over threshold − ; Reinforce-Discipline/Reform + | Effective Power penalty; formation-hold; Discipline checks |
| **Morale** | mass_battle | `[T]` 1–7 (per-sub-unit) | Size-loss/flank/idle/general-down −; Rally/Reform + | **Rout gate (0)** |
| **Size / TroopCount** | mass_battle | `[D]` | engagement damage | **Destroyed gate (0)**; Effective Pool |
| **Tactic-card hand** | mass_battle | `[T]` 6/faction | draw/play | BG battle resolution |

---

## A7 · What this transpose reveals (the opacity payoff)

Reading the tables by **fan-in / fan-out** surfaces the coupling that the chain view hides:

- **Highest write-fan-in (most things digest into it):** `Order` (governance + battle + levy + strain),
  `Stability` (5 sanction tiers + shocks), `Disposition` (7 social verbs + knot + demand), `MS`
  (every thread op + battle), `Mandate` (settlement aggregate + echo + 4 sanctions).
- **Highest read-fan-out (most things export from it):** `Mandate` (→ 7 consumers), `MS` (→ victory,
  piety, threadwork, slate), `CI` (→ ci_political, victory, stay, theocracy), `Prosperity` (→ economy,
  treasury, mandate-weight, 3 Obs), `Order` (→ public-order, revolt, accord).
- **Derived-value chokepoints (write-protected, but everything downstream depends on them):**
  `Mandate`, `Treasury`, `Health`, `Local Economy`, `Garrison Strength`, `Public Order`, `Cover`,
  `Composure`, `Face`. These are the values you must never let a Godot port hand-write (F1 guard).
- **Cross-scale couplers (a primitive whose writer and reader sit at different scales):**
  `L/PS ↔ Mandate` (settlement ↔ faction), `Prosperity → Treasury` (settlement → faction),
  `CV → CI` (territory → provincial), `MS` (personal thread-ops → peninsula), `Accord → IP` (territory
  → peninsula). These five are where the whole model's cross-scale behaviour lives.

---

# PART B — MODULE I/O (what each module digests vs exports)

The complementary lens: per module, the surface the primitives above flow through. (Full contract
detail with resolver/loops/gates is in `module_contracts.yaml`; this is the digest.)

| Module | Digests (inputs) | Exports (outputs) | Writes which primitives |
|---|---|---|---|
| **engine_clock** | — | `season_change`, `accounting` | season counter |
| **personal_combat** | `combat_strike`, `combat_hit` | `combat_hit/felled/resolved` | Health, Wounds, Stamina, Initiative, Poise |
| **threadwork** | (reads Spi/TS/Coherence/MS) | `thread_operation`, `thread_woven` | Coherence, Thread Fatigue, **MS** |
| **fieldwork** | Memory-Query (`*`) | `knot_formed/ruptured`, `gift`, `belief_revised` | Disposition, Bonds, Knot Strain, Evidence, Exposure |
| **social_contest** | `opinion_revised` | `contest_resolved`, `dialogue`, `insult`, `threat` | Persuasion Track, Face, Concentration, Obligations |
| **mass_battle** | (reads Command/units; transitions) | `battle_concluded` (+auto MS/Accord/Order/IP) | Discipline, Morale, Size; **pushes MS/Accord/Order** |
| **npc_behavior** | ~20 types (nearly whole bus) | `opinion_revised`, `concern_resolved`, `belief_revised`, project/interaction/gossip/witness/displacement | beliefs, concerns, projects, arc-state |
| **conviction_track** | scene.* / da.* / meta.* witnessables | `scar_acquired` | Conviction Scars, Truth |
| **scene_slate / game_director** | slate rules, NPC outreach | scene.* / scene_entered/exited/skipped | (none — dispatcher) |
| **player_agency** | reads Standing/Renown/Resources | Renown grants, Domain-Echo eligibility | Standing, Renown, Resources, Duties |
| **settlement_layer** | `disaster`, `strain_shock`, `population_change`, `economic_intervention` | `population_change`; **pushes Mandate + Treasury** | Prosperity, Defense, Order, L, PS, Facility Tier |
| **territorial_piety** | (thread/Calamity drift — unkeyed) | (CI unkeyed) | CV/PT, **CI** |
| **faction_state / politics** | all `da.*`, `env.*`, `scene.*`, `state.*`, `accounting` | `standing_change`, `succession`, `coup_attempted`, `investigation_resolved`, `cascade_resolution`, `mission_shift` | Influence/Wealth/Military/Intel/Stability, rank Standing |
| **domain_actions** | `draft_da` | `da.*` (×5 buckets) | (none — outcome-tag taxonomy) |
| **peninsular_strain** | (accounting; low-Accord) | `crisis`, `disaster`, `strain_shock`, `population_change` | **Turmoil, IP** |
| **ci_political** | (reads CI) | political effects | political pool, card hands |
| **victory** | reads MS/IP/CI/Turmoil/Accord/Mandate/PT | era transitions (**unkeyed**) | (none — pure reader) |
| **articulation** | `*` (whole bus) | `cascade_cluster_event` | (none — renderer) |
| **miraculous_event** | (gated) | `miraculous_event` | (none — emitter) |

---

# PART C — VERTICAL STACKS (the chains, now indexed to the primitives they move)

The chains from the old lens, retained as the *propagation* view — but each is labelled with the
**primitive** it moves so you can jump from Part A to the chain and back.

- **B1 · Survival→reputation** *(moves Health→Standing)*: `combat_strike → combat_hit(Health δ) →
  combat_felled →` npc_behavior (memory) / conviction (Scar) / faction (officer death→`standing_change`).
- **B2 · Persuasion→power** *(moves Persuasion→Mandate)*: `social_contest.contest_resolved →` Domain
  Echo `→ faction Mandate/Standing`; 2-cycle back via `opinion_revised` (bounded).
- **B3 · Settlement⇄faction loop** *(moves L/PS↔Mandate, Prosperity→Treasury)*: `L/PS →` Mandate
  `7T/(T+6) →` drift `±1 →` L/PS. The one proven-bounded feedback loop.
- **B4 · Witness→arc** *(moves →Conviction Scars)*: any witnessable Key → `scar_acquired` → arc / Renown.
- **B5 · Church power** *(moves CV→CI→Theocracy)*: thread/Calamity drift → CV → CI → ci_political /
  victory. ⚠️ **unkeyed end-to-end**.
- **B6 · Strain→occupation** *(moves Turmoil/IP)*: `strain_shock/disaster/population_change →`
  settlement/faction/npc; `IP=100 →` occupation; fed upward by battle aftermath + Accord erosion.
- **B7 · Relationship→cognition** *(moves Disposition→belief→opinion)*: Connect → Disposition →
  `knot_formed`; Interview → Evidence → `belief_revised` → npc opinion → social_contest input.
- **B8 · DA fan-out** *(moves faction stats + settlement Prosperity + Scars)*: faction action →
  `da.* ` bucket → faction/npc/settlement/conviction/articulation.

---

# PART D — SHARED BUS + STATE-GRAPH GAPS

**The 49-type Key bus** is the shared-outcome layer (full table in `key_type_registry_v30.md`).
Two modules are universal sinks — **articulation** and **npc_behavior** consume nearly everything;
**faction_state** is the strategic hub. But three critical state channels **bypass the bus** and are
hand-wired: `L/PS→Mandate`, `Prosperity→Treasury`, `CV→CI`. These are the drift-risk seams for Godot.

**Loose seams a whole-state view must know about:**
1. **`doc: null` state-managers (9):** engine_clock (time!), domain_actions, scene_slate,
   game_director, npc_memory, settlement_economy, scenario_authoring, scene_timer, audit. engine_clock
   is the temporal spine — ED-1051 open.
2. **Unkeyed CANONICAL primitives:** CV/CI and the victory-era transitions emit **no Key** —
   articulation/observers are blind to Church-power and era changes through the bus.
3. **Pointer disagreements:** Combat Pool (still 3 defs, CLAUDE.md §5); attribute roster `IN FLUX`; Health formula/range diverges (v30 13–55 vs core.md 14–48 vs the sigma engine). *(Coherence's former 3-way was resolved to `track` by PR #112 — no longer open.)*
4. **Name collisions:** personal Truth/"Piety" vs territory "Piety Track" vs Church "Piety Spread";
   faction "Legitimacy" (`Mandate·20`) vs settlement `set.legitimacy` (0–7); faction "Discipline"
   (`Stability·10`) vs unit Discipline (1–7).
5. **Phantom module:** settlement_economy owns no state (RECOMMEND RETIRE → fold into settlement Prosperity).
6. **da.* bucket assignment** is a directional first pass — 3 forks open (ED-FA-0006).
7. **Cross-module derived pushes bypass the Key bus** — the drift-risk concentration for the port (CLAUDE.md §5).

---

# PART E — SIM ↔ DESIGN RECONCILIATION (code truth: where the pointers actually live)

Parts A–D describe the *design* pointers. But the pointers that will actually drive Godot live in
the **Python sim** (`engine/`, `sim/`, `systems/*/sim/` — ~12.7k LOC, the 1:1 GDScript oracle). That
layer **diverges materially** from the design registry, and *that gap is the opacity*: a designer
reads "Mandate = 7T/(T+6) aggregate of settlement L/PS", but the running code holds a single flat
`Faction.L` scalar and no settlement L/PS at all. This part reconciles the two, per primitive.

**Sim-status flags:** `LIVE` (wired, read+written) · `DORMANT` (declared, never read) · `STUB`
(NotImplementedError / no field — the design primitive has *no* sim state) · `DIVERGENT` (name or
value mismatch) · `SIM-ONLY` (real code state with no design-registry row) · `SAVE-GAP` (real state
not serialized — lost on snapshot).

## E0 · The actual persistent container — `engine/autoload/game_state.py`

The whole live world state is one `World` dataclass: `factions: dict[str,Faction]`,
`territories: dict[str,Territory]`, `clocks: dict[str,float]`, `settlements: dict[str,Settlement]`,
`season`, `arc`, `winner`, plus **14 sub-registries** (`practitioners, insurgencies,
uncontrolled_streaks, npcs, treaties, convictions, beliefs, knots, territory_infrastructure,
npc_drift_state, threadcut_beings, comovement_deck, settlements, …`). Deltas are applied through the
**Key substrate** (`engine/substrate/keys.py`): a `Target.stat_deltas` dict (e.g. `{'L': +1}`) routed
via `Faction.adjust()` — the F1 guard is real in code.

## E1 · Faction (sim) — the PRE-LPS-1 model is what actually runs

| Design primitive | Sim field (game_state.py) | Status |
|---|---|---|
| **Mandate** *and* **Legitimacy** | `Faction.L` (float 0.5–7, `MULTS['L']=20`) | ⚠️ **DIVERGENT + CONFLATED** — one flat scalar read as *both* Mandate and faction-Legitimacy; self-flagged `[PRE-LPS-1 / PORT-BLOCKING — ED-FA-0004]`. The `×20` granular scale *is* the 0–140 Legitimacy buffer. **No `7T/(T+6)` aggregate, no per-settlement L/PS feed exists.** |
| Stability | `Faction.Sta` (`MULTS 10`) | LIVE |
| Wealth | `Faction.W` (`MULTS 100`) | LIVE |
| Influence | `Faction.I` (`MULTS 15`) | LIVE (mass_seizure reads it as Influence `[ASSUMPTION]`) |
| Military | `Faction.Mil` (`MULTS 10`) | LIVE |
| Intel | `Faction.intel` (0.0) | **DORMANT** — no `MULTS` entry, never read/written |
| Faction Standing | `Faction.standing` (int) | LIVE but **flat** (one per-faction int, not the per-officer ladder) |
| **Treasury** | *(none)* | **STUB** — no Treasury field; `ΣProsperity·10` unimplemented |
| **Reputation** | *(none)* | **STUB** |
| Casus Belli | `world.casus_belli` | **SIM-ONLY** duck-typed — not a schema field; only Crown-restoration CB is derivable |
| Excommunication | `Faction.excommunicated` | LIVE (sim-only flag; no registry row) |
| — | `Faction.consul_used`, `Faction.peaceful` | **DEAD** — `consul_used` is written at seasonal reset but read nowhere; `peaceful` is fully inert (default-only) |

The `MULTS` table `{L:20, Sta:10, W:100, I:15, Mil:10, accord:10, pt:10}` is the **actual numeric
backbone** — it, not the design tables, defines granular-delta magnitudes.

## E2 · Two coexisting settlement/territory models

The sim runs an **old `Territory`** model *and* a **new `Settlement`** model simultaneously:

| Design primitive | Sim field | Status |
|---|---|---|
| Accord | `Territory.accord` (float, `MULTS 10`, `ACCORD_MAP` **0–4** buckets) | LIVE — ⚠️ range diverges (registry says 0–3) |
| Piety (PT/CV) | `Territory.pt` (`MULTS 10`) | LIVE |
| Prosperity | `Territory.prosperity` **and** `Settlement.prosperity` | **DUAL** — two coexisting grains |
| Fort Level | `Territory.fort_level` **and** `Settlement.fort_level` | **DUAL** |
| Defense / Order | `Settlement.defense` / `.order` (0–5) | LIVE |
| **Legitimacy (L)** | `Settlement.legitimacy` (0–7) | ⚠️ **INERT** — declared, **zero read/write anywhere in sim/** (ED-FA-0004) |
| **Popular Support (PS)** | `Settlement.popular_support` (0–7) | ⚠️ **INERT** — same |
| Facility Tier / Admin Points | `Settlement.facility_tier` → `.ap` property | LIVE |
| Church Attention Pool | `Settlement.church_attention` | LIVE (undocumented in §1.3) |
| — | `Settlement.suspicion`, `Settlement.pressure` (Π, 4.0), `Settlement.governor_emergence` | **SIM-ONLY** (the Goldenfurt dossier/governance-deck subsystem — not in `settlement_layer_v30 §1.3`) |
| Ledger tags | `LedgerTag.kind ∈ {Precedent, Grudge, Debt, Reputation, Leverage}` | LIVE — ⚠️ **missing `Compact`** (the 5th family ratified ED-SE-0019); recurring-fire semantics unimplemented |
| Religious building (Axis 1) | `Settlement.religious_building` (sid-keyed) **and** `InfrastructureState.religious_building` (tid-keyed) | ⚠️ **DUAL-TRACKED**, no reconciliation code |
| Church infra (Axis 2–4) | `InfrastructureState.{templar_station, inquisitor_base, church_governor}` | LIVE, keyed per-territory (canon says per-settlement) |
| temperament_drift | `world.npc_drift_state` | LIVE — ⚠️ DIVERGENT name (canon: `territory.temperament_drift`) |
| Entry-Terms L seed | `Territory.entry_terms_l_seed` (dynamic attr) | **SIM-ONLY** inert placeholder, schema-undeclared |
| — | `ADJACENCY` graph | ⚠️ **code bug** — missing a `T16` (Schoenland) entry though `T1` names it |

## E3 · The `clocks` dict — most of it is dormant

`create_world()` seeds `{'CI':30.0, 'MS':60.0, 'IP':20.0, 'PI':0.0, 'Strain':0.0, 'Turmoil':0.0}`.

| Design clock | Sim key | Status |
|---|---|---|
| Church Influence | `clocks['CI']` | LIVE — ⚠️ start **30** in world-init vs **28** in `ci_track.CI_STARTING` (registry says 28) |
| Mending Stability | `clocks['MS']` | LIVE (start 60, matches) |
| Institutional Pressure | `clocks['IP']` | **DORMANT** — `ip_track.py` is a `NotImplementedError` stub; nothing reads it |
| Turmoil | `clocks['Turmoil']` | ⚠️ **DIVERGENT (3-way name)** — `victory.py` reads it as "Political Stability"; dormant in peninsular |
| — | `clocks['PI']` | **ORPHAN** — no registry row; leftover from retired `mc_v*` monoliths |
| Peninsular Strain | `clocks['Strain']` | **DORMANT** — no live reader |
| — | `clocks['MASS_SEIZURE_USED']` | **SIM-ONLY** — improvised one-shot flag on the generic dict |
| **RS track** (retired *Rendering*-Stability label) | `rs_track.py` | **STUB** + name-collides with MS — no `RS` clock key exists; threadwork Part 5's heading uses the retired RS label but its body is entirely Mending Stability |

## E4 · Personal / combat — a large SIM-ONLY continuous layer

The canonical resolver is `combat_engine_v1`; the old `sim/combat.py` (flat wounds, −1D penalty) is
**dead canon**. On the live `Combatant`:

| Design primitive | Sim field | Status |
|---|---|---|
| Combat Pool | `Combatant.pool = max(5, history+6)` | LIVE (matches R1 canon) |
| Health / cum-damage / Wounds / WI / MW | `WoundTracker.{cumulative_damage, wounds, wi, max_wounds, health_full, felled}` | LIVE (the sigma model, F1 substrate) |
| Stamina | `stamina_max = 3·End+2·Spi` | LIVE — ⚠️ DIVERGENT (doc still says `End×5`) |
| Concentration | `conc_max = 3·Foc+2·Spi` | LIVE |
| Initiative | `Combatant.initiative` (continuous sigma Vor/Nach/Indes) | ⚠️ **FALSE COGNATE** — a *different* mechanic from design's discrete PP-232 Initiative; all constants `[FIAT]`/`[SIM-CALIBRATE]` |
| — | `Combatant.poise` (kuzushi), `grip_position`, `lunge_depth`, `facing`, `range_avail`, `sel_*`, `disp` | **SIM-ONLY** — a whole continuous per-beat morphology layer (the 2026-07 closing-distance redesign) with **no design-registry pointers** |
| — | `Combatant.ready` | **DEAD** (shadowed by an engagement-local dict) |

Threadwork: `CoherenceState.coherence` LIVE · `ThreadcutState.{rendering_strain, deactualisation_round}`
LIVE · co-movement deck LIVE (**15 of 18 cards**). **`Thread Fatigue` = STUB (zero implementation
anywhere).** **Composure and Knot-Strain are computed in `opposing.py` but never persisted** —
return values dressed as consequences.

Conviction/belief: `ConvictionState.{scars, resonant_active, in_crisis, pending_belief_revisions,
last_scar_season}` LIVE · `Belief.{position, underlying_convictions, revision_pressure}` LIVE · **Truth**
= `CERTAINTY_SCALING` (sim keeps the old "certainty" identifier). ⚠️ **Three incompatible
`CONVICTIONS` taxonomies run at once** — `conviction.py` (9, mislabeled "13"), `npe.py` (8, different
set), vs canonical 13 (ED-1006 open). Non-listed convictions silently no-op when scarred.

Fieldwork: `Knot.{strain, tier, disposition, active}` LIVE (in `knots.py`) — but **`fieldwork.py` /
`investigation.py` are pure stubs**, so **Disposition, Evidence, Exposure, Cover have no sim state**
(Disposition exists only as a formation-time snapshot inside a Knot).

## E5 · Social-contest kernel — new primitives + duplicates

`Standing.v` **is** Face (literal Python alias; Composure retired) · `Reserve` = Concentration (an
abstract seed pool, not `3·Foc+2·Spi`) · `ContestState.adv` = Persuasion merits. **`ArmaturePosition`
(evidence / consequence / authority / insinuation)** is a new field carried alongside the frozen
adjudicator — its 3 first axes map to **CANONICAL** contest styles (`STYLE_AXIS`, citing
`npc_behavior_v30 §1.3`) and the 4th (`insinuation`) is a **RATIFIED** new axis (ED-1062); the
**continuous dot-product itself** is the sim-only construct (no design-registry row), not the axes. **Doubt Marker** is fully spec'd in
`dictionaries.py` but **UNIMPLEMENTED** as live state. **Persuasion Track and "resistance" are each
implemented twice** (resolver vs `parliamentary_vote`) with different math.

## E6 · Mass battle

`Unit.{power, command, discipline, morale, size, dr, h_per_size, speed, broken, routed}` LIVE. ⚠️
`Unit.hp/hp_max` **is** TroopCount (DIVERGENT name). **`quality`** (canon "unit quality") — **STUB**
(no field; pre-baked into power/morale_start). `Unit.stamina` — **SIM-ONLY** (self-flagged, no canon).
`stance` orders vocab — SIM-ONLY. **Per-sub-unit stats (ED-1018) — UNIMPLEMENTED** (Subunit has no
power/discipline/morale). **Tactic-card hand — STUB** (`FACTION_TACTIC_CARD_POOL_MODIFIERS = {}`).
`altonian_reinforcements` choice-lock — STUB.

## E7 · Stub inventory — design primitives with NO sim state

`Thread Fatigue` · `IP` track · `RS` / Calamity track · `Treasury` / `Reputation` (faction) · settlement
`Legitimacy`/`Popular Support` (inert) · Disposition/Evidence/Exposure/Cover (fieldwork stubs) ·
Doubt Marker · tactic cards · per-sub-unit stats · unit `quality` · miraculous_event ·
restoration_movement · home_sanctuary · companion · npc_ai · 5 faction modules (charter,
hafenmark-equipment, infrastructure-reclamation, both varfell actions) · `propose_treaty`.

## E8 · Save/restore gaps (real state lost on snapshot)

`Territory.uncontrolled_since` (declared but omitted from `serialize_world`/`restore_world`) · the
entire Key/Echo log (`world.key_log`, `echo_scheduler`, `_echo_key_seq`, attached via `setattr`) ·
`victory._qualifying_streak` (module global). *(NOT a save-gap: `world.convictions`/`world.beliefs`
ARE declared `World` fields and DO round-trip through serialize/restore — the module-level dicts are
only the `world=None` fallback. Corrected per the E-verification pass.)*

## E9 · The headline

1. **The live faction + settlement model is PRE-LPS-1** — `Faction.L` conflates Mandate/Legitimacy;
   settlement `L/PS` is inert. The ratified `7T/(T+6)` aggregate (Part A/B3) **is not implemented**.
   This is the single biggest port blocker (ED-FA-0004).
2. **A whole SIM-ONLY continuous layer exists with no design pointers** — combat morphology
   (poise/grip/lunge/facing) and the contest `ArmaturePosition` *continuous dot-product* (its axes
   are canonical, but the continuous vector primitive is not). These need design-registry rows
   *created*, or they will cross into Godot undocumented.
3. **A whole set of design pointers have no sim** — Thread Fatigue, IP, RS, Treasury, tactic cards,
   per-sub-unit stats, fieldwork Disposition/Evidence/Exposure, Doubt Marker. Porting these is
   blocked on *implementing the oracle first*.
4. **Silent divergences to reconcile before transcription** — CI start (30 vs 28), Stamina
   (`3·End+2·Spi` vs `End×5`), Accord range (0–4 vs 0–3), TroopCount↔`hp`, temperament_drift naming,
   3 conviction taxonomies, the missing `Compact` ledger family, dual-tracked religious building.

---

*Survey only. Establishes no canon; every flag points to an existing open ED / gap_note. Part E is a
code-truth census of the working tree (`engine/`, `sim/`, `systems/*/sim/`), compiled by a six-way
sim-extraction fan-out.*
