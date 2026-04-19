# Valoria Campaign Simulation — Full Rebuild Workplan

**Status:** proposed 2026-04-19
**Scope:** rebuild `tests/sim_framework/engine_v3.py` from the canonical game systems rather than from abstract faction stat comparisons
**Goal:** a simulation that runs the *actual game's mechanics* — not a proxy — and produces campaign outcomes that reflect the factional identities and geographic constraints documented in canon

---

## Guiding principle

The current engine (v3.6) is structurally wrong: it models factions as stat-comparison loops that expand by rolling dice against abstract Ob numbers. The real game has geography, settlements, fortresses, terrain, mass battles, Thread operations, institutional presence, and political manipulation. Every "balance tuning" attempt on the current engine is polish on the wrong shape.

The rebuild follows one rule: **every mechanic in the simulation must map to a canonical system already specified in the repo.** No invented modifiers. No placeholder dice bonuses. If a system isn't canonical, it isn't in the simulation — it becomes a flagged gap for editorial resolution.

---

## Phase 0 — Canon audit (prerequisite, not part of the build)

Read to full depth. Note any gaps as `[GAP: ...]` flags for editorial resolution before Phase 1 begins.

Required reads:

- `designs/provincial/mass_battle_v30.md` — the actual battle system (Part B is BG/sim-relevant)
- `designs/territory/settlement_layer_v30.md` — the 36-settlement substrate + dual-authority governance
- `designs/world/geography_v30.md` — adjacency + fortresses (already read)
- `designs/world/calamity_radiation_v30.md` — RS band × node distance matrix
- `designs/world/southernmost_v30.md` — T15 movement rules + expedition procedures
- `designs/provincial/faction_layer_v30.md` — Stability triggers, occupation, treaties, CI formula §9
- `designs/provincial/factions_personal_v30.md` — per-faction mechanical toolkits (§8.2–§8.9)
- `designs/provincial/faction_politics_v30.md` — rank ladders (useful for subnational faction behavior)
- `designs/npcs/npc_character_analyses_v30.md` — ruler identities (already read for Almud, Baralta; need full)
- `designs/npcs/npc_behavior_v30.md` — priority trees
- `params/bg/*.md` — all BG params (phases, faction_actions, npc_priority_trees, military, ministry, parliament, institutions, clocks, tracks, ci_seizure, victory, core)
- `canon/00_philosophical_foundations.md` — P-01 through P-15 principles (Thread mechanics sit on these)
- `designs/threadwork/threadwork_v30.md` — Thread operations as game actions

Output: `tests/sim_framework/canon_audit.md` listing every system the simulation will implement, its canonical source, and every gap flagged.

---

## Phase 1 — Substrate (the map and its contents)

**1.1 Territory graph with adjacency.**
17 territories as nodes. Canonical adjacency from `geography_v30.md`. Each territory carries: name, PV, SW (Spiritual Weight), PR (Proximity Rating, = node distance from T15), Fort level, Fort max, subtype tag, current controller, Accord, PT. This replaces the flat TERRITORIES dict in the current engine.

**1.2 Settlement sublayer.**
Each territory contains 1–4 settlements per `settlement_layer_v30.md §2.1`. Settlements are independent nodes with their own type (Capital / Major / Minor / Rural), their own Church infrastructure (Chapel / Church / Cathedral / none), Templar station (bool), Inquisitor station (bool), Church Governor (bool), and their own controller (may differ from territory controller — this is the dual-authority model canonical §3.1).

This is what makes Church infrastructure-before-Seizure work: Church owns settlements across the peninsula while Crown/Hafenmark/Varfell own the provinces those settlements sit in. Mass Seizure is the moment the settlement-layer control is formalized at territory layer.

**1.3 Calamity radiation state.**
Node distance per territory (from `geography_v30.md`). RS band × node distance effects from `calamity_radiation_v30.md`. Applied each Accounting: territories in bands where Calamity effects activate get mechanical consequences (Accord drops, Anomaly POI activate, forced Survey checks).

**1.4 Fortresses as movement constraints.**
T3 Lowenskyst (Fort 3, max 4), T14 Ehrenfeld (Fort 3, max 4), T10 Spartfell (Fort 2), T9 Himmelenger (Fort 2), T1 Valorsplatz (Fort 2), T8 Gransol (Fort 1), T12 Sigurdshelm (Fort 1), T16 Schoenland (Fort 1). Mass battles into fortified territories add Fort level to defender Ob. This is where Varfell's geographic containment becomes real.

**1.5 T15 Askeheim — special movement.**
Per `southernmost_v30.md`: entering T15 requires Expedition Procedure. Non-Varfell factions face additional Ob. Calamity exposure effects apply. Movement through T15 as a transit route requires separate roll.

**Phase 1 output:** `engine_v4.py` skeleton with substrate only. No AI, no actions. A state-of-the-world that matches canon.

---

## Phase 2 — Action layer (what factions can do per season)

Each faction has a canonical action list from `factions_personal_v30 §8.x` and `params/bg/faction_actions.md`. The simulation implements these as functions operating on the substrate, not as stat-bonus triggers.

**2.1 Universal actions (all factions).**
- Govern (Consul Inward) — Accord management in own territories
- Expand (Consul Outward) — infrastructure or claim in another territory
- March (Legionary Outward) — military movement + mass battle
- Defend (Legionary Inward) — Fort garrison, Accord support
- Senate (Senator) — diplomatic actions, treaties
- Pass (Recess) — bank Standing or +1D next season

**2.2 Crown-specific.**
- **Royal Decree** (Prefect card) — PP-435 canonical: redirect resources or suppress a rival's action. Not stat-boost.
- **Crown Treaty** (Senator) — victory_v30 §3.1 degree table. Submission or cession negotiation.
- **Ministry deployment** (per `params/bg/ministry.md`) — Ministry of Law, Taxation, Guilds, Water/Granaries. Each provides conditional bonuses. Crown is the only faction with Ministries at game start.
- **Altonian relations** — Elske marriage, Torben tutoring decision (IP 30 event), Schoenland trade. These are not routine actions but event-driven.

**2.3 Church-specific.**
- **Assert** (CI generation step — `params/bg/ci_seizure.md §3.6`) — Influence vs Ob 2 for +1 CI
- **Piety Expand** — upgrade settlement Church infrastructure (Chapel → Church → Cathedral). Canonical Ob and pool per `settlement_layer_v30 §1.4`. Fires at settlement level, not territory.
- **Templar Deploy** — place Templar in settlement with Church building ≥ 2. Military presence.
- **Inquisitor Deploy** — place Inquisitor in settlement with Church building ≥ 1. Investigation + suppression capability.
- **Heresy Investigation** — target Thread-active NPC or faction leader. Per `npc_priority_trees Church P2`.
- **Excommunication** — formal ban, grants Casus Belli to other factions vs target.
- **Mass Seizure** — one-shot, current canonical curve `P=((CI-60)/40)^3.3`, Ob = `10 - PT + church_infra_modifier` (floor 1), targets ALL settlements where Church is prominent.

**2.4 Hafenmark-specific.**
- **Parliamentary Manoeuvre** (per `params/bg/parliament.md`) — Baralta's structural lever. Not implemented in v3 engine.
- **Dynastic Proclamation** (Diplomat card, PP-649) — diplomatic territory claim. Ob = `floor(target Stability/2) + 1`.
- **Mine Income** — Wealth income from mineral territories (T17 Halvarshelm especially). Canonical rate TBD (flag as `[GAP: mine income rate]`).
- **Equipment Bonus** — Hafenmark Military actions get +1D from mining-funded equipment. Canonical in `faction_politics_v30` §1.2 Hafenmark ladder.
- **Food Vulnerability** — Hafenmark territories are highlands (T7, T8, T10, T17), not breadbaskets. If Hafenmark loses access to Feldmark (T5) or Kronmark (T2) trade, Wealth drops. Flag for canonical rate.

**2.5 Varfell-specific.**
- **Tribune Investigation** (per `npc_priority_trees Varfell P2/P3`) — reveals enemy hidden stats. Not a combat bonus.
- **Thread Operations** (per `threadwork_v30.md`) — practitioner-led actions. Costs Coherence + RS. Available to Varfell first (southern baseline TS + RM proximity).
- **RM Alliance** — if RM activates as subnational faction (`factions_personal §8.8`), Varfell can coordinate with them. Shared territory operations.
- **March through Askeheim** — the alternate route to Crown territory. Thread exposure, RS cost, but bypasses T14 fortress.

**2.6 Event-driven actions (non-routine).**
- Löwenritter Coup (Coup Counter ≥ 4)
- Altonian Vanguard (IP ≥ 50)
- Schoenland naval passage (IP ≥ 75)
- Klapp Awakening, Olafsson Exposure, Jarnstal Independence (Church event cards)
- Constitutional Crisis, Ministry Collapse (Crown event cards)
- Guild Schism, Guild Forum Revolt (Guild event cards)

**Phase 2 output:** action layer implemented. Each action uses canonical Ob, canonical pool, canonical effects. No fabricated modifiers.

---

## Phase 3 — Mass battle system

Replace the current `attempt_conquest` one-roll abstraction with `mass_battle_v30` Part B. Canonical phases:

1. **Declaration** — attacker commits force, defender responds
2. **Manoeuvre** — terrain advantage, position selection
3. **Offensive Thread phase** — only if attacker has practitioner with Thread ops prepped (this is where Varfell's Thread access matters mechanically)
4. **Engagement** — dice resolution with Size/Power/Discipline/Command stats
5. **Cascade** — casualty cascade, morale, breakthroughs
6. **Resolution** — territory transfer or defender hold

Canonical battle consequences (`mass_battle_v30 Part E`): RS cost (-1 to -2 depending on scale), Strain +1, IP +2, Accord drop in battle territory.

Each faction's battle capabilities per `params/bg/military.md` and `factions_personal §8.x`. Hafenmark gets Discipline +1 (equipment). Varfell gets Thread phase access first. Crown gets Ministry of Law bonus to Command. Church Templars provide defensive Size in Church-infrastructure settlements.

**Phase 3 output:** real battles. Size/Power/Discipline/Command stats tracked per army. Terrain matters. Thread operations in battle are available but rare.

---

## Phase 4 — Political layer (the actual game the factions are playing)

This is what the current engine lacks entirely. Factions don't expand abstractly — they pursue specific political goals.

**4.1 Almud's threat assessment AI.**
Each season, Crown AI ranks rivals by current threat level:
- Highest-Mandate rival → target with Heresy rumor / Church pressure
- Highest-territory rival → target with Crown Treaty negotiation or Parliamentary motion
- Highest-military rival → target with Altonian threat redirect (Crown tips off Altonia about Varfell border movements, etc.)
- Crown expansion is LAST priority. Crown wins by preventing any rival from reaching critical mass, then absorbing wreckage.

**4.2 Himlensendt's pastoral drift.**
Church AI prioritizes:
- Settlement infrastructure upgrade (Chapel → Church → Cathedral) in highest-PT territories
- Templar/Inquisitor deployment in settlements with infrastructure
- Heresy Investigation against visible Thread activity
- Mass Seizure declaration follows canonical curve — but now the Seizure targets *settlements* Church already infrastructure-owns, making it effective instead of ineffective
- Church does NOT military-conquer. Its expansion is pastoral.

**4.3 Baralta's constitutional campaign.**
Hafenmark AI:
- Parliamentary Manoeuvres against Crown each session Baralta has Mandate advantage
- Structural CI suppression (Mandate ≥ 4 = CI -1/season, per `params/bg/ci_seizure.md`)
- Military expansion via Dynastic Proclamation (diplomatic) first, force second
- Equipment-superior battles against weaker-army factions
- Food vulnerability: if Hafenmark territories disconnect from Crown breadbasket (T2, T5), Wealth decay

**4.4 Vaynard's revolutionary war.**
Varfell AI:
- Must break out of geographic containment. Three options:
  - North through T14 (Crown Fort 3) — frontal assault on fortress
  - North through T7 (Hafenmark Rendstad) — attack Hafenmark first
  - South through T15 (Askeheim) — Thread-exposure route to T6 Stillhelm
- Thread operations when available (Varfell has southern TS baseline — operations fire earlier than Church can counter)
- RM alliance if RM subnational faction activates
- Vaynard targets strongest remaining rival for climactic battle (once he's out)
- Heresy investigation against Vaynard is a persistent Church pressure — Varfell AI must defend against it

**4.5 Restoration Movement as subnational faction.**
Per `factions_personal §8.8`. RM can activate when conditions met (Lenneth's influence, Varfell support, Church overreach). Once active, it's a faction-like actor with Presence markers in territories. Lenneth's Crown-side Einhir revival programme interacts with RM (potentially aligns Crown and Varfell briefly through Lenneth).

**4.6 Caste as political pressure.**
Not just a lore note. Territories with high southern-Einhir populations have modified Accord behavior under the caste system. Church Heresy Investigations fall disproportionately on them. Crown's Einhir suppression action (canonical somewhere in `faction_politics_v30` — flag for verification) is available. Lenneth's revival programme contests this.

**Phase 4 output:** factions playing the actual game. Crown manipulating, Church drifting, Hafenmark campaigning, Varfell breaking out. Not four parallel copies of "expand until victory."

---

## Phase 5 — Integration and output

**5.1 Season cycle** per `params/bg/phases.md`.
**5.2 Accounting** per canonical Phase 5 steps (1–13).
**5.3 Victory check** per `victory_v30` — now functional because the political layer actually produces submissions, capitulations, and formal transfers.
**5.4 Shared loss** per RS ≤ 0 per `params/bg/clocks.md`.
**5.5 Event logging** — every faction action, battle, infrastructure change, political pressure. The log should be readable as a campaign narrative.

**5.6 Smoke test suite.**
- 20 seeds × 120 seasons — baseline balance check
- Scenarios: Early Altonian invasion, Lenneth gains Crown influence, Vaynard breaks out through T15, Baralta deposes Almud, Church Mass Seizure at CI 75 vs CI 95 (timing pressure), RS ≤ 40 forcing Warden emergence
- Output per run: winner/shared loss/stalemate, season count, RS/CI/Strain trajectories, major events

**5.7 Balance targets.**
Not uniform 25% — canonical factions are asymmetric by design. Realistic targets:
- Crown 30–35% (favored — most resources, best position, Almud's competence)
- Hafenmark 20–25% (strong but food-vulnerable)
- Varfell 15–20% (high-variance — either breaks out fast or collapses)
- Church 15–20% (slow buildup, Mass Seizure timing-dependent)
- Shared loss 5–10% (RS collapse from prolonged conflict)
- Stalemate <10% (endgame mechanics should force resolution)

**Phase 5 output:** a working simulation that produces canon-faithful campaign outcomes.

---

## Out of scope for this rebuild

- Player character (this is the NPC-only world simulation)
- Scene-layer resolution (combat, social contest, fieldwork, Threadwork as player actions)
- Godot implementation
- Hybrid handoff (TTRPG mode integration)
- Full 36-settlement POI discovery (use starting POI counts from `geography_v30` without implementing Survey action fully)

These are future work. The simulation's job is to produce a world state the player's scenes can hook into.

---

## Estimated work

Phase 0 (canon audit): 1 session, full read of listed docs, gap flagging
Phase 1 (substrate): 1 session, territory + settlement data structures + adjacency + radiation state
Phase 2 (action layer): 2 sessions, per-faction action implementation, canonical Obs and pools
Phase 3 (mass battle): 1 session, replacing `attempt_conquest` with full battle resolution
Phase 4 (political layer): 2 sessions, faction AI rewrite per canonical identity (one session per two factions)
Phase 5 (integration + smoke tests): 1 session, running seed sweeps, balance reporting

Total: **~8 focused sessions.** Each session produces a commit + coverage matrix update. Each session leaves the engine in a runnable (if incomplete) state for incremental testing.

---

## Session-one recommended starting point

Phase 0 canon audit. Produce `tests/sim_framework/canon_audit.md` with every system, its source file, its canonical details, and every `[GAP: ...]` flag. Do not touch the engine yet. The audit becomes the specification the rebuild is tested against.

After the audit, Phase 1 substrate becomes a clean build from known specifications rather than a rewrite under uncertainty.

---

## Known gaps that block the rebuild (flagged for editorial resolution)

These items do not have canonical mechanical specifications in what I've read so far. Each blocks at least one Phase 2–4 system.

- `[GAP: mine income rate — Hafenmark Wealth +/season from mineral territories not specified]`
- `[GAP: Hafenmark food vulnerability mechanic — canonically flagged ED-054 but unresolved]`
- `[GAP: Crown Einhir suppression action — referenced in `character_histories_v30` 1D but no canonical DA]`
- `[GAP: RM activation trigger conditions — `factions_personal §8.8` likely has this, needs full read]`
- `[GAP: Thread operations in mass battle — `mass_battle_v30` §Offensive Thread Phase needs full read for pool/Ob]`
- `[GAP: subnational faction emergence — `settlement_layer §3.3` referenced but not read]`

Phase 0 audit will confirm whether these are truly gaps or whether canon exists in sections I haven't reached yet.
