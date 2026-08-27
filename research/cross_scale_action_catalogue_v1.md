# Valoria — Cross-Scale Action Catalogue (v1)

## Status: FILED — reference, not canon (CLAUDE.md §0.05: code is the mechanism, prose is reference)
## Date: 2026-08-27 · Lane: IN (cross-cutting: FA, SE, MB, PC, SC, FI, WR)
## Scope: every action available at every scale of play; build status per action; the formula that
## governs it (or should); and whether it resolves opposed or unopposed.
## Method: read from the working tree at `f567c13`. Every row cites the module or doc it was read
## from. Where code and canon disagree, the code is recorded as the mechanism and the disagreement
## is flagged — never silently reconciled.

---

## 0. The one resolution kernel

Every scale in Valoria resolves through the same primitive. This is not a stylistic claim; it is
enforced by single-owner modules and a guard test.

| Element | Value | Owner |
|---|---|---|
| Die | d10 | `engine/autoload/dice_engine.py` |
| Target Number | **7. Always.** A varying difficulty is an Ob, never a TN. | `dice_engine._require_tn7` — the owner *refuses* any other value (Jordan, 2026-08-25, ED-IN-0196) |
| Per-die EV | μ = 0.40 successes, σ = 0.800 | `dice_engine._MU_PER_DIE` / `_SIGMA_PER_DIE` |
| Roll | continuous: `Normal(μ·N, σ·√N)`, pool floor 1.0, **fractional pools legal** | `sigma_leverage.roll_net_continuous` |
| Obstacle | `Ob`, integer or fractional, floor 1 | `sigma_leverage.OB_MIN` |
| Margin | `margin = net − Ob` | `dice_engine.degree_from_net` |
| Degrees | `margin ≥ 3` Overwhelming · `≥ 1` Success · `[0,1)` Partial · `< 0` Failure | same |
| Modifiers | **d+σ**: a modifier is a σ-space μ-shift on the roll, *not* an Ob shift. Soft-capped at `M_MAX = 1.5σ`; `σ_N = 0.8·√Pool` | `sigma_leverage.net_boost` / `soft_cap` |

**Pool construction is uniform across scales:** `Pool = (Primary Attribute × 2) + History bonus`,
where History bonus = relevant History points + 3, capped +3D. Confirmed identical in combat
(PP-615), contest (PP-234) and fieldwork (`fieldwork_v30 §2`). Threadwork substitutes
`(Spirit × 2) + History + TPS` where `TPS = floor(TS/10)` (PP-619/624). Personal combat instead
uses `resolution_pool(history) = max(5, History + 6)` — agility-independent, ED-901.

### 0.1 One degree ladder — with one declared hold

`tests/valoria/test_degree_ladder_single_owner.py` enrols every ladder in the tree. Eight of nine
have migrated to the owner. **One is deliberately HELD: `combat_engine_v1/core.py:degree`**, which
still uses the pre-2026-08-14 bands (`net ≥ 2·Ob AND net ≥ 2.5` for Overwhelming, ER-2 continuity
shift, fixed `DECISIVE_OB = 3`). Migrating it moves the Failure edge by two whole successes and
breaks a ratified armour-participation invariant; the collision is Jordan's to resolve. **Personal
combat therefore grades on a different ladder from every other scale today.**

### 0.2 Opposed vs unopposed — the governing ruling, and its execution gap

Jordan ruled 2026-08-14: *"an obstacle rolled against a character or faction is their corresponding
score/2 plus whatever specific modifiers exist for them in that instance."*

**That derivation is implemented at exactly one site in the tree.** `dice_engine.degree_from_net`'s
own docstring flags it: *"⚠ THAT DERIVATION IS IMPLEMENTED NOWHERE — every call site in the tree
still passes a hand-set Ob."* `registers/handoffs/HANDOFF_FA.md` measured the FA lane and found the
three opposed sites **disagree with each other**:

| Site | Derivation | Against the ruling |
|---|---|---|
| `crown_initiative.coronation_renewal_ob` | `floor(church.L / 2) + 1` | **matches** |
| `tribunal.py:116-122` | `round(accused.L × 0.5)` with formal grounds, `round(accused.L)` without | **half the time** |
| `parliamentary_transfer.py:257` | `holder.L + 2` — the full score | **contradicts**, and its own doc states this as canon |

Half B of M1 juncture 1 is **SUSPENDED** on this: wiring `score/2` uniformly would overwrite
ratified canon (`parliamentary_transfer_v30.md:30`) and would collapse the Tribunal's deliberate
two-tier formal-grounds halving. `tests/valoria/test_faction_obstacle_conventions.py` pins all
three so none drifts while it is suspended.

**Consequence for this catalogue:** Valoria has *four* structural resolution shapes, and only two of
them are "opposed" in the dice-rolling sense. Every action below is tagged with one:

| Tag | Shape | Example |
|---|---|---|
| **U** — Unopposed | One roll vs an Ob derived from world/terrain/self state | Muster (Ob 1), Govern (Ob 2), Threadwork Depth Ob |
| **SO** — Statically opposed | One roll vs an Ob derived from the *target's* score. No second roll. | Coronation Renewal, Excommunication Tribunal, Parliamentary Transfer, most Fieldwork social actions |
| **DO** — Dynamically opposed | The opponent **rolls**, and their result becomes the Ob or subtracts from yours | Contested Investigation (Concealment Ob), Social-contest `rebut` |
| **BI** — Bilateral model | No Ob at all; both sides' state enters a differential model that resolves the exchange | Personal combat (σ-differential), Mass battle (both sides roll pools per exchange), Conquest (delegates to the battle engine) |

**Dynamically opposed rolls are rare — two mechanisms in the entire tree.** Almost everything the
game calls "opposed" is actually SO or BI.

---

## 1. Faction / political scale

**Live driver:** `engine/mc_v18.py` → `systems/factions/sim/faction_action.py::faction_take_action`,
one action per faction per season.

### 1.1 The selection model (BUILT)

GD-2 mandatory-before-stochastic. Four buckets with prior weights re-weighted by faction state, then
renormalised and drawn once:

```
w_unique   = 0.30
w_conquest = 0.35 × (1 + 0.5·has_target + 0.5·mil_advantage)
w_muster   = 0.20 × (1 + threat_signal)
w_govern   = 0.15 × (1 + undergoverned_share)
```

In a neutral state this degenerates exactly to the retired fixed 30/35/20/15 vector. Grounding:
Levy 1983 (high-war baseline is period-correct), Blainey 1973 (war onset tracks perceived relative
power), Olson 1993 (stationary-bandit incentive to govern held land). ED-FA-0012. Signals consume
no RNG; the only draw is `rng.random()`.

Dispatch falls through: unique → Conquest → Muster → Govern (Govern is the unconditional fallback).

### 1.2 The four generic actions

| Action | Status | Pool | Ob | Shape | Effects |
|---|---|---|---|---|---|
| **Conquest** | **BUILT** | — | — | **BI** | Delegates to `resolve_mass_battle`. On attacker win: territory transfers, loser `L −10`, garrison set, `battle_count++`. Forks **Terms** (defender not routed, degree Success) → Accord −10, seeds new settlement `L = 3` (Joyeuse Entrée) vs **Storm** (routed, Overwhelming) → Accord −25. Grotius III / Parker 1994. Emits `scene.battle_concluded` Key (telemetry only, no `apply=`). |
| **Muster** | **BUILT** | `Mil + floor(W/2)` | 1 | **U** | Costs `W −1` **up front, always** — the military enterpriser is paid regardless of outcome (Redlich 1964, Tilly 1990). Overwhelming `Mil +5`, Success `Mil +3`. No extra failure penalty (the up-front cost prices it). ED-FA-0009. |
| **Govern** | **BUILT** | `Influence` | 2 | **U** | Overwhelming Accord +15, Success +10, Failure `Sta −5`. |
| **Faction-unique** | partial — see below | varies | varies | varies | Routes by `faction.name`; falls back to Parliamentary Censure. |

Note the `CONQUEST_MIN_MIL = 3.0` gate is **DELETED** (Jordan, 2026-08-14): *"that minimum military
score needing to be 3 to attack is wrong and must be deleted."* A faction that wants to attack may.

### 1.3 Faction-unique actions

| Action | Faction | Status | Pool | Ob | Shape | Notes |
|---|---|---|---|---|---|---|
| **Royal Progress** | Crown | **BUILT** (PROVISIONAL) | `Influence + standing` | `max(2, floor(accord_gap / 2))` where `gap = 7·n_owned − Σaccord` | **U** (Ob from own territory) | `W −2`. ED-840 closure formula. |
| **Great Work** | Crown | **BUILT**, simplified | `Mandate (L)` | 4 | **U** | Multi-season Open Pledge tracking **deferred to PP-515** — currently instant-resolution only. |
| **Coronation Renewal** | Crown | **BUILT** | `Influence` | `floor(church.L / 2) + 1` | **SO** | The one site matching the `score/2` ruling. Lifts Excommunication on success (§6.4, Q-11). |
| **Excommunication** | Church | **BUILT** (PROVISIONAL) | `church.L` (+1 on formal grounds) | `round(accused.L)`, **halved** with formal grounds (`CI ≥ 40 ∧ Church.L ≥ 4`) | **SO** | Single-roll abstraction of the §7.1 Tribunal. Target `L −1` (−2 with formal grounds), `CI +3`. On failure Church `L −1`, target `L +1` (sympathy). |
| **Council of Solmund** | Church | **BUILT** (PROVISIONAL) | `church.L` | `floor(CI / 30) + 2` | **U** (Ob from world clock) | 1/arc cooldown. Cardinal Focus effect logged but **not state-mutating** — the track isn't in the v18 schema. |
| **Absolution** | Church | **BUILT** (PROVISIONAL) | `church.I` | 3 | **U** | Costs Church `L −1`; target `Sta +1`. Ob 3 is `M6_ASSUMPTION_ONE`, **not ratified**. Gated on `Church.L ≥ 4` to protect the Excomm prereq. |
| **Mass Seizure** | Church | **BUILT** | `Influence + floor(CI/15)` | `max(1, 10 − PT + infra_mod)` | **U** | Declaration is probabilistic: `P = ((CI−60)/40)^3.3`, one-shot lifetime, forced at CI 100. Per-territory resolution against every territory with Chapel+. GD-1: produces no victory directly. |
| **Parliamentary Censure** | any parliamentary | **BUILT** | see §1.4 | — | vote | The universal unique-slot fallback (ED-FA-0012). Only the *mildest* Sanction tier is built. |
| **Charter of Liberties** | Hafenmark | **STUB** (`stubwire`) | — | — | — | `attempt_charter` is a typed no-op. |
| **Hafenmark Equipment** | Hafenmark | **STUB** | — | — | — | |
| **Varfell Mandate Action** | Varfell | **STUB** | — | — | — | Pass 2d BLOCKED. |
| **Varfell Territorial Acquisition** | Varfell | **STUB** | — | — | — | Pass 2e BLOCKED. |
| **Home Sanctuary (T9)** | Church | **STUB** | — | — | — | Jordan directive exists (invasion Ob +4 for 12 seasons; ends on Church PT<3 / L<2.5 / any CB vs Church) — unimplemented. |
| **Infrastructure Reclamation** | — | **STUB** | — | — | — | |
| **Generic Tribunal (§7 Asymmetric Proceeding)** | — | **STUB** | — | — | — | Only the Excommunication specialisation resolves. |
| **Treaty proposal** | Crown | **STUB** — `propose_treaty` raises | — | — | — | Only `process_treaty_expirations` (90–95%/arc lapse) and `register_treaty` scaffolding work. |

**So: 8 of the 16 rows above execute; 8 are typed no-ops** (Treaty is half-alive — expiration and
registration work, proposal raises), **and 1 of the 8 that execute (Great Work) does so in a reduced
form.** Varfell and Hafenmark have *no working unique action at all* and reach the board only
through the Censure fallback.

### 1.4 Parliament

`systems/social_contest/sim/parliamentary_vote.py` + `systems/factions/sim/parliamentary_action.py`.

Votes: each faction contributes votes = current Mandate; the target does not vote. Majority > 50%;
Supermajority ≥ 60%. Church contributes `Mandate + floor(CI/20)`; a faction voting against Church on
a Church-targeting motion contributes `max(0, Mandate − floor(CI/30))`. Church **Sacred Veto**: once
per 4 consecutive seasons, `Mandate −1` if used against a motion that would have passed, `−1` again
if self-interested.

**The Sanction ladder — one parameterised action at five severity tiers (ED-FA-0006 DISTILL):**

| Tier | Proposer min | Vote | Target effect | Proposer cost | Duration | Built? |
|---|---|---|---|---|---|---|
| Censure | Mandate 2 | Majority | `Sta −1; Mandate −1` | none | one-time | **YES** |
| Embargo | Mandate 3 | Majority | `W −1/season` | `W −1/season` | until lifted | **NO** |
| Blockade | Mil 3, Mandate 3 | Majority | `W −2/season; Sta −1` | `Mil −1` | until lifted | **NO** |
| Combined | both | Supermajority | `W −2, Sta −1/season, Mandate −1` | `W −1 + Mil −1` | until lifted | **NO** |
| Outlawry | Mandate 5 | Supermajority | `Mandate −2, Sta −2, CB to all` | `Mandate −1` | permanent until petitioned | **NO** |

**Constructive motions — all five UNBUILT:** Subsidy (Mandate 2 / Majority / recipient `W+1`),
War Authorisation (Mil 2 / Majority / free first advance + CB), Treaty Ratification (any signatory /
Majority), Recognition Challenge (Mandate 4 / Supermajority / `−1 TCV`), Succession Endorsement
(Mandate 3 / Majority / succession Ob −1).

**Target Rebuttal** (design only): `M = Mandate − 2` (Censure) or `Mandate − 3` (Outlawry). Failure →
vote unmodified; Partial → Stability cost halved; Success → Stability negated, Mandate halved;
Overwhelming → both negated + proposer `Mandate −1` + target `Sta +1`.

**Parliamentary Territorial Transfer** (`parliamentary_transfer.py`, **BUILT**): wraps the §10 vote,
then `Pool = max(0, Influence + pool_mod)` where `pool_mod = ±1` by vote outcome,
`Ob = holder.L + 2` — **SO**, and the site that contradicts the `score/2` ruling. Four CB-required
modes; §10.1 stay hook available post-roll.

### 1.5 The Domain Action catalogue (board-game surface)

Captured verbatim in `engine/engine_params/params_tables.yaml` §"Standard Action Ob Reference"
(P-21). **⚠ This is a byte-frozen 2026-08 capture of evacuated prose. Under §0.05 it is reference;
where it disagrees with code, the code wins.** The card slot vocabulary is
Legionary / Consul / Senator / Tribune / Pontifex / Praetor / Diplomat / Colonist / Prefect / Recess.

| Domain Action (card slot) | Default Ob | Shape | Built? |
|---|---|---|---|
| Muster (Legionary Inward) | 2 | U | **YES** (as faction Muster, Ob 1 in code — *code and capture disagree*) |
| March (Legionary Outward) | no roll; contested entry = Battle | BI | via Conquest |
| Govern (Consul Inward) | `floor(Prosperity/2) + 1` | U | **YES** (Ob 2 in code — *disagrees with capture*) |
| Trade (Consul Outward) | `floor(Prosperity/2) + 1`; +1 at IP≥30, +1 in T2 | U | **NO** |
| Diplomacy vs NPC (Senator Outward) | `floor(NPC Stability/2) + 1` | **SO** | **NO** |
| Formal Crown Treaty (Senator Outward) | `floor(target L/2) + 1` | **SO** | **NO** (`propose_treaty` raises) |
| Thread Operation (Pontifex/Weaver) | 2 base | U | **YES** — single-sourced to the TW lane, not re-catalogued here |
| Investigate/Intel (Tribune) | 2; +2 in Church territory with Inquisitor | U | **NO** |
| Spy (Tribune Outward) | `floor(target Intel/2) + 1` | **SO** | **NO**. Failure now specified (ED-FA-0006): target learns it was probed, gains +1D on its next Intel action against you |
| Survey (Consul Inward) | `(5 − Proximity Rating) + 1`, min 1; Pool: Influence | U | **NO**. Reveals 1 POI; failure at Depth ≥3 → +1 Church Attention Pool |
| Parliamentary Manoeuvre (Hafenmark) | `floor(opponent Influence/2) + 1` | **SO** | **NO** |
| Community Organising (Restoration) | 2; Pool `1D + 1D per adjacent RM Presence` | U | **NO** |
| Community Weaving (Restoration) | `ceil((100−MS)/20)`, min 1; −1 per Presence marker | U | **NO** |
| Dynastic Proclamation (Hafenmark) | `floor(target Stability/2) + 1` | **SO** | **NO** |
| Martial Governance (Löwenritter) | `floor(Prosperity/2) + 2`; Military pool; Accord +1 cap 2 | U | **NO** |
| Fortify | `Fort level + 1` | U | **NO** |
| Cultural Reformation (Varfell) | **STRUCK** CR-STRIKE-2026-04-19 (VTM-dependent) | — | superseded by Cultural Reclamation |
| Diplomacy between players | **DISTILLED away** (ED-FA-0006) — it *is* Treaty's Concession step | — | — |

**The single biggest structural gap in the faction layer:** `references/module_contracts.yaml`
declares a module `domain_actions` with `resolver: d_sigma` and **`doc: null`** — it has no home
design doc. The catalogue above lives only in a frozen prose capture. This is the missing
foundation the faction-management ask needs (see §9).

---

## 2. Settlement governance

**Live head:** `systems/settlements/settlement_layer_v30.md` (CANONICAL).
**In proposal:** `systems/settlements/governance_play_redesign_v1.md` (PROPOSAL, 2026-06-22).
**Sim:** `systems/settlements/sim/` — registry, adjacency, ledger, infrastructure, temperaments.
**No governance-verb resolver exists in code.** Every verb below is design-only.

### 2.1 The old menu (`settlement_layer_v30 §3.2`) — superseded in proposal

Four verbs: Develop / Fortify / Pacify / Administer, one free governance action per season. The
redesign's own diagnosis: *"a player-governor's mechanically-distinct verbs are four stat-pumps …
governing collapses toward 'roll one die a season and watch numbers'."*

### 2.2 The proposed menu — the Governor's Turn

**Action economy:** `AP = 2 + FacilityTier_s` (0–3) → 2–5 AP/season; Standing-5 governors +1;
AP do not carry over. Companion-governors get a flat 2 AP.

Season order: **Directive (mandatory) → Governance Phase (spend AP) → Personal Phase.**

| Verb | AP | Roll | Ob | Shape | Effect · the tradeoff |
|---|---|---|---|---|---|
| **Develop** | 2 | Cognition + Wealth-history | `floor(Prosperity/2) + 1` | U | Prosperity +1. Funding fork: Treasury (needs PA approval) · Guild charter (faster, Guild Influence +1 — a standing claimant) · Corvée (Order −1) |
| **Fortify** | 2 | Military + history | `floor(Defense/2) + 1` | U | Defense +1. Fork: Garrison (Löwenritter dependence↑) · Militia (PS +1, brittle, armed populace) · Walls (Treasury, slow) |
| **Keep Order** | 1–2 | varies by method | — | U | Order +1. Fork: Consent (Charisma, 2 AP, PS +1) · Force (Military, 1 AP, PS −1, Disposition −1, rebound) · Clergy (1 AP, Order +1 *and* Church infra creeps — the Geneva trap) |
| **Hold Court** | 1 | Charisma/Cognition + Governance-history | set by dispute | **SO** | Adjudicate a Local-Actor dispute. Writes a **Precedent** tag (±1 Ob on related events) |
| **Sponsor** | 1–2 | auto / Wealth | — | none | Durable +1 stat + Disposition; writes a **Debt** tag (skip next year → Disposition −2) |
| **Treat** | 1 | Influence + history vs subnational leader | social contest §7 | **BI** (contest) | Minor side-deal. Chit stored as a Debt tag, called in when a Friction card referencing it fires |
| **Levy** | 1 | auto | — | none | Extract troops/Treasury/intel. `L/PS −1` and/or Order −1 — the dual-authority squeeze made literal |
| **Investigate** | 1–2 | Cognition + relevant history | vs concealment | **DO** | **DISTILL:** reuses the fieldwork Investigation resolver. What is new is the four-way post-discovery fork: expose · expel · co-opt · shelter |
| **Retain Clerks** | 1 + `W −1` | auto, no roll | — | none | +1 effective AP per Clerk Capacity point (0–3), uncapped by FacilityTier. Silently increments a hidden **Clerk Corruption** counter raising Intrigue-card weight. Ming–Qing *muyou*/*shúlì*. ED-SE-0022 |
| **Survey** | 2 | Cognition + Governance-history | `floor(Prosperity/2) + 1`; ~8-season cooldown | U | Writes/refreshes an **Assessment** tag locking `assessed_base`. Toyotomi *Taikō Kenchi* / *kokudaka*. New failure mode: a stale-high Assessment strips a declined settlement below subsistence *by neglect*. ED-SE-0018 |
| **Negotiate Quota** (Levy method) | 2 | Charisma/Cognition + history vs Local Actors as a mass social contest | §7 | **BI** | Converts variable Levy into a fixed multi-season **Compact** (4–6 seasons). Castilian *encabezamiento*. Grants Local Actors one Petition per term the governor must Hold Court on. ED-SE-0019 |
| **Bind the Cells** (Keep Order method) | 1 | — | — | U | Partitions Local Actors into five-household cells with reporting leaders; Order +1. Any member's infraction stamps a **Collective Liability** tag on the whole cell. Three tags → "Cell Revolt" Crisis card. Hideyoshi 1597 / Tokugawa *goningumi*. ED-SE-0020 |
| **Ordenanza: Ratify / Reject / Amend** (Hold Court branch) | — | Amend: Charisma/Cognition vs Guild Master, Ob 2 | 2 | **SO** | **RATIFIED** ED-SE-0023. Ratify → guild bonus + Guild Influence +1; Reject → Disposition −2 + Grudge; Amend → half bonus, no Influence. Ratifying an entry-standard clause locks caste exclusion in as settlement policy. Spanish *gremios* |
| **Petition / Defy** (Directive response) | 0 AP | Bargain = social contest vs PA | — | **BI** | see below |

### 2.3 The Directive — the dual-authority engine

Each season the Provincial Authority issues **one** Directive: **Extract · Tax · Suppress · Install ·
Host · Cede.** The governor must respond:

| Response | Cost | Up-tier | Down-tier |
|---|---|---|---|
| Comply | — | faction Standing +, trust + | usually strains the settlement |
| Bargain | social contest vs PA (you as petitioner) | soften terms; mild suspicion | partial strain |
| Defy / Divert | — | Standing-debt, **suspicion +1**; at threshold → recall / audit / replacement | protects settlement; Local-Actor Disposition +, PS + |

Suspicion at threshold fires a **Recall scene** (a social contest) — or, with enough local L/PS,
seeds the player's own faction-emergence (§6.2). Independently, the settlement emits **Needs** from
its state; the Directive and the Needs routinely conflict and your AP cannot serve both.

### 2.4 The Ledger of Consequence — five tag families (P5)

**Precedent** (biases related events ±1 Ob) · **Grudge** (raises hostile-action weight, seeds
Intrigue cards) · **Debt** (fires once, when called in) · **Reputation** (Just/Harsh/Generous/Weak/
Hated — modifies Local-Actor starting Disposition) · **Compact** (fires *every season of its term*).
Tags persist across tenure and **survive succession**.

### 2.5 Other settlement actions (design-only)

Expand Institutional Capacity (Treasury −300, +1 Wing, cap +1/settlement/decade) · Grant/Revoke
Subnational Management (**FA-lane Domain Action**, Influence, Ob 1 to grant / `ceil(subnational
Influence / 2)` to revoke — **SO**) · Quo Warranto charter challenge · Church Governor install
(Ob 1 when settlement has a Chapel and no governor) · Consensus Delay waiver in RM settlements
(1 Mandate + 1 Presence marker).

---

## 3. Mass battle

**Live head:** `systems/mass_battle/mass_battle_v30.md`; **engine:** `systems/mass_battle/sim/`
(~8,400 lines). This is the most completely built strategic system in the tree — the `MECHANICS`
registry in `engine.py` lists **31 mechanics, every one `status: WIRED`.**

Resolution is **BI**: a battle is a tick loop, not an action with an Ob. Per tick, per side:
`check_orders → assign_targets → find_contacts → volley_phase → resolve_engagements (cascading) →
attrition → morale/rout → recovery`. Each engaged pair rolls a combat pool; degrees drive casualties.

### 3.1 The player's actual decision surface

The commander does not "take an action" — they **compose an army and queue conditional orders**.

**Stance** (`STANCE_SPEED_MOD`): `aggressive` (+1 speed) · `balanced` (0) · `hold` (−99: immediate
early-return, never advances) · `retreat` (0).

**Formation shapes:** Line · GappedLine · Arrowhead (Column shape declared but *not yet defined* —
Flanker currently placeholders to Line).

**Troop types and their gated role menus** (`config.TROOP_TYPE_ROLES` — flagged
"SCAFFOLD — data only; INERT until the instruction→primitive modulation lands"):

| Troop type | Roles | Power/Disc/Morale |
|---|---|---|
| levy | (any: Support, Reserve) | 1/1/2 |
| light_infantry | Skirmish, Screen, Pursue | 3/3/4 |
| heavy_infantry | ShieldWall, Hold, Anvil, Push | 4/4/5 |
| pike | ShieldWall, Hold, Anvil | 4/4/5 (mirrors heavy_infantry; **reach 0.3 is the sole differentiator** — §B.2 carries no pike row) |
| cavalry | Shock, Flanker, Feint, Screen, Pursue | 5/5/5 |
| archers | VolleyLine, Harass | 3/3/3 |
| crossbow / sling / artillery | — | 3/3/3 · 2/2/3 · 2/2/3 |
| mounted_archers | Kite, Harass, Feint | — (the research report's #1 troop type) |
| knights_templar | — | 5/6/6 |

**Role → shape + instruction package (`ROLE_SPEC`):** ShieldWall (Line: brace+hold) · Hold (Line:
hold) · Anvil (Line: brace+pin) · Push (Line: advance) · Skirmish (GappedLine: loose+harass) ·
Screen · Pursue · Shock (Arrowhead: charge) · Flanker (envelop) · Feint (lure) · VolleyLine
(volley+hold) · Harass (loose+shoot_move) · Kite (kite+shoot_move) · Support/Reserve (reserve).

**⚠ Only 7 of ~18 instruction tokens are actually consumed by the engine:** `hold`, `envelop`,
`sweep`, `brace`, `kite`, `reserve`, `shoot_move`. `pin`, `advance`, `loose`, `harass`, `screen`,
`pursue`, `charge`, `lure`, `volley` appear in `ROLE_SPEC` and are read by nothing. The config's own
comment says so: *"Instructions are the behaviour layer … Behaviour wiring + calibration is the next
step."*

**Conditional orders** (`hierarchy/units.Order`, **BUILT**) — the real tactical language:

| Trigger | Fires when |
|---|---|
| `immediate` | at construction |
| `tick:N` | `t ≥ N` |
| `enemy_range:D` | within D of nearest enemy cell |
| `ally_at:D` | within D of a named allied subunit's centroid |
| `own_strength:FRAC` | this subunit attrited to ≤ FRAC of spawn count (strictly 0<FRAC<1) |

An order sets fields restricted to `_ORDER_SAFE_FIELDS`: `stance, instructions, unit_type, role,
target_condition, target_delay_ticks, order_target_idx, escort_of, escort_offset,
escort_engage_on_contact, yielding`. Geometry/troop-accounting fields are *deliberately excluded* —
setting them mid-battle orphans troops or teleports cells.

**Targeting conditions:** `nearest` (default) · `weakest` · `in_range:N` · `direct` (by index), plus
`target_delay_ticks` for a held reserve.

**Prebuilt manoeuvres** (`engine.py`): `build_envelopment` (wings at `hold`, released at
`tick:release_tick` into `balanced` + `envelop` — Cannae) · `build_refused_flank` (refused wing
released on `enemy_range:D` — Leuctra).

### 3.2 Mass-battle gaps

| Item | Status |
|---|---|
| **Tactic cards** (`tactic_cards.py`) | **BLOCKED STUB** — `FACTION_TACTIC_CARD_POOL_MODIFIERS = {}`. Contents pending a contamination audit (Jordan diagnosis 2026-05-17: prior card-pool authoring may contain overreach). The canonical name is reserved; nothing else ships. |
| Instruction→primitive modulation | **INERT** — 11 of 18 instructions are dead tokens |
| Column formation shape | undefined; Flanker placeholders to Line |
| Kiting primitive | named as a gap in config; `Kite` role "blocked on the kiting primitive" |
| Terrain modifiers at the faction→battle seam | `terrain=None` hardcoded in `_try_conquest` — "[GAP: deferred to Phase 7 follow-on Steps 2-9]" |
| Armour DR / Endurance bridge | `TROOP_TYPE_STATS` deliberately omits `dr` and `stamina` — §B.2's Armour column maps to a vs-Piercing DR scale whose identity with `Subunit.dr` is unconfirmed |

---

## 4. Personal combat

**Live head:** `systems/combat/combat_engine_v1/` — the resolver package *is* the canon (the engine
wins over prose). ~5,850 lines. This is a **continuous physics engine, not an action menu.** There
is no "attack / parry / dodge" button list; there is a beat loop in which commitment depth, reads,
mode selection and measure emerge from weapon morphology, attributes, fatigue and tradition.

### 4.1 The state graph (`state_graph.py` — data, and tested)

```
FightInit → EngagementInit → {Approach | AwaitTempo}
Approach  → {Approach, AwaitTempo, Felled, Separation}      emits: approach, stophit
AwaitTempo→ {Exchange, AwaitTempo, Approach}
Exchange  → {Bind, Riposte, HitLanded, Contact, AwaitTempo, Felled, Separation}
                                                            emits: commit, read, mode, roll, outcome
Bind/Riposte/HitLanded → {AwaitTempo, Contact, Felled}
Contact   → {AwaitTempo, Separation}                        emits: contact   [BUILT, not activated — M-11]
Felled → Decided → UpsetCheck → FinalResult
Separation → InterTurn → {EngagementInit, Unresolved}
```

Separation reasons: `collapse` · `burst_ceiling` · `clean_defence` · `beat_exhaustion`.

### 4.2 Resolution shape — **BI**, not opposed rolls

There is **no Ob derived from the defender.** `core.resolve` rolls against a fixed `DECISIVE_OB = 3`
and carries the *entire* opposition in `net_sigma`, assembled from differential terms:

`assemble_net_sigma(attack_sigma, defence_sigma, reach_pen, adef, init_edge, …)`, where the terms
include `reach_sigma`, `bind_sigma`, `initiative_sigma`, `armor_defeat_sigma`, `mode_sigma`,
`stophit_sigma`, `pursuit_sigma`, `true_time_edge`, `tempo_pressure`, `charge/percussion_stagger`,
`overcommit_exposure`, `wound_impairment`. Sub-contests (`read_contest`, `bind_dominance_p`,
`counter_success_prob`, `disrupt_resist_p`, `grab_outcome`) resolve through a single-owner logistic
squash of a σ-differential — a probability, not a second roll.

Damage: `damage(deg, heft_units, head, strength, armor, gap, perc, …)` through
`coupling()` → the three damage modes `percussion / puncture / shear` against
materials `none / cloth / mail / plate`.

### 4.3 What the *player* actually chooses

| Decision | Node | Status |
|---|---|---|
| Weapon (51 in the roster) + grip + half-sword form | pre-fight | **BUILT** |
| Armour tier (`none/light/medium/heavy`) | pre-fight | **BUILT** |
| Tradition (german, italian, english, spanish, japanese, …) | pre-fight | **BUILT** |
| Ability investment levels (0–8.0 per technique) | pre-fight | **BUILT** |
| Commit depth (2–5, disposition-skewed) | `Exchange` | engine-chosen; the injection point exists |
| Defence mode (`parry`/`dodge`/`wind`) | `Exchange` | engine-chosen by `mode_sigma`; ordered tuple is part of the RNG contract |
| Grapple branch | `Contact` | **BUILT, NOT ACTIVATED** |

### 4.4 Capability gates (`capabilities.py`) — the hard affordances

Only four things are *gated*; everything else is continuous scaling.

| Capability | Node | Requires |
|---|---|---|
| `halfsword` | closed.form_switch | a long rigid blade grippable mid-stave |
| `gap_thrust` | closed.coupling | a real point — head in `{point, cut_thrust}` or a derived point (catches the poleaxe's spike) |
| `percussive_blow` | closed.coupling | a blunt head |
| `open_contact` | Contact | `head_len ≤ GRAB_SHORT_REACH_M` (dagger/unarmed class) — every other weapon needs a real prior opening this beat |

Armour-defeat *effectiveness* is explicitly **not** gated: a low-gap rapier bounces off plate by
degree, not by prohibition.

### 4.5 The grapple menu (`contact.py` — BUILT, unactivated)

`grab_available(actor, opponent, opening_created)` → dagger-class always; everything else needs a
bind / beaten-aside / deep-commit reopen. Then
`grab_sigma = GRAB_STR_K·Δstrength + GRAB_LEV_K·Δleverage − GRAB_EDGE_K·grab_hazard(opp.weapon)·max(0, 1−skill)·ability_factor('edge_grab')`.

`grab_outcome`: flat escape chance, then `p = logistic(gsig)`-skewed weights over
**disarm** (0.15+0.25p) · **throw** (0.15+0.20p) · **pin** (0.15+0.15p) · **control** (0.35−0.25p) ·
**foot_pin** (0.10) — Fiore's 2nd Remedy four-branch plus a foot-pin/escape pair.

### 4.6 Ability primitives (`ability_primitives.py`) — 7 authored, 3 levers bare

A tradition gates *access*; the invested level drives *efficacy*. Additive abilities scale
`value × level`; multiplicative scale `value ** level`; level 0 is inert.

| Ability | Tradition | Lever | Op | Value |
|---|---|---|---|---|
| `indes` | german | counter_success | + | 0.15 |
| `staerke_schwaeche` | german | leverage | × | 1.20 |
| `zwerchhau` | german | counter_select | × | 1.4 |
| `ringen_am_schwert` | german | edge_grab | × | 0.4 (a mitigator) |
| `mezzo_tempo` | italian | counter_select | × | 1.40 |
| `misura` | italian | measure | × | 1.15 |
| `true_times` | english | anti_overcommit | + | 0.25 |
| `atajo` | spanish | leverage | × | 1.18 |
| `shinogi` | japanese | spine_press | × | 1.6 |

**Bare levers awaiting grounded content (a declared honest gap, not invented privilege):**
`edge_read`, `choke_control`, `facing_regime`. **Dead lever:** `seize` — its pre-contact consumer was
cut 2026-06-05, so `vorschlag`/`sen_no_sen` do nothing when equipped; slated for retire-or-reroute.

**Honesty note carried from ED-PC-0023:** the abilities' *aggregate* win-rate edge is ~0 once
isolated from tradition membership. Their effect is **per-event** (a bind won, a grab de-hazarded),
which aggregate winrate cannot see.

### 4.7 Tradition injection points — the differences the graph can accept

Nine declared points where a tradition biases a generic branch: `approach.measure` ·
`reopen.measure` · `exchange.commit` · `exchange.read` · `exchange.mode` · `exchange.bind_entry` ·
`exchange.counter` · `burst.continuation` · `contact.axis`. Note the **feint-node absorb**: there is
deliberately no separate Feint state — feint/micro-read lives inside `Exchange.read`.

### 4.8 Open PC items

JD-2/3/5/6/7/8 remain open (`HANDOFF_PC.md`). The declared degree-ladder hold (§0.1). The
Contact node built-but-unactivated. Menu-weighting of the grapple outcome table by tradition is
"a FUTURE increment, not yet wired."

---

## 5. Social contest

**Live head:** `systems/social_contest/social_contest_v30.md`; **kernel:**
`systems/social_contest/sim/contest/` (~6,700 lines) — the most mechanically complete *personal*
system after combat. ⚠ A staged **contest_rebuild** is in flight (Stage 4 "four games" next), and a
2026-08 three-lens audit found **three resolution models under one name** — findings only, nothing
ratified. **ED-SC-0015 needs a Jordan ruling.**

### 5.1 The move menu — 7 kinds, all BUILT (`resolver.VALID_KINDS`)

| Move | Reserve cost | Shape | What it does |
|---|---|---|---|
| **advance** | 3 | **U** (reception roll) | The standard argument. Must be relevant to the live stasis or it is `arthantara` (evasion fault). Gain scales with degree. |
| **hard** | 5 | **U** + self-gate | An overreaching argument; must be *licensed* by relative standing (`SelfGating.licit`), else `barred` (`chala/jati`). |
| **shift** | 4 | none | Move the live stasis ground. Only *upward* on the ladder — a downward or null shift is `apasiddhanta` / `pratijna-hani` (contradiction). |
| **support** | 2 | none | Regroup + build ethos 1. |
| **evidence** | 3 | none (readiness-free) | Present the best unpresented *relevant* dossier item. `mag = min(weight × corroboration, EVIDENCE_CAP)`. **Hard proof: readiness-independent, builds nothing, value hidden.** Refunds if nothing relevant. |
| **rebut** | 3 | **DO** | Contest the opponent's case: on `deg ≥ 2`, erase up to `REBUT_CAP` from the *opponent's* advantage. Only where `venue.allow_rebuttal`; otherwise `arthantara`. **One of only two dynamically-opposed mechanisms in the tree.** |
| **pass** | 0 | none | Yields (`ananubhasana`); regroups. |

### 5.2 The reception formula (the actual resolution)

```
pool  = Pool.size(faculty) + pool_bonus                     # pool_bonus = CR4's integer +1D
lev   = Leverage.net(faculty, on_ground=True) + dsigma_bonus  # armature δσ
net   = roll_net(pool) + net_boost(lev, pool)               # σ-leverage as μ-shift, Ob untouched
degree = degree_from_net(net, venue.base_ob, extension=degree_extension, pool=pool)

leak   = min(LEAK_CAP, Resonance.leak(adj.discipline, cred_frac) + public_pressure × PUBLIC_LEAK)
res    = max(RES_FLOOR, (1−leak)·venue.joint_weight(appeal, tense) + leak·adj.character[appeal])
rdy    = Readiness.of(cred_frac, room.frac(side))           # 1.0 for evidence
gain   = MERIT_SCALE · magnitude · res · rdy · U(1±JITTER) · bias(side)
```

Two **distinct additive channels** (CR6, judge-enforced): CR4's `+1D` enters the **pool**; the
armature's alignment enters as a **continuous δσ** in the leverage term. Neither multiplies `res`.

### 5.3 The three trackers (CR3 — Composure retired)

| Canonical name | Role | Kernel primitive |
|---|---|---|
| **Face** | contest-local ethos/standing (transient) | `Standing` (0–10, `START=5`, `BUILD/STRIP = 0.8`). `Face_max = Charisma × 3`; `Face_current = round(Standing/10 × Face_max)` |
| **Concentration** | per-exchange stamina | `Reserve` (`MAX = 12`, per-move cost, `REGAIN = 4`) |
| **Persuasion Track** | merits clock, 0–10 banded two-pole | `ContestState.adv` |

⚠ **Scope honesty from the kernel's own comment:** `Standing.strip()` is never called in the contest
kernel except through the CR5 backfire — **Face has no general strain channel and is monotonic-up.**
The v30-surface "strain → Rattled → −1D Argue pool" is *not realised*.

### 5.4 The Stasis ladder and the appeal axis

**Grounds (ordered; a shift may only go up):** `fact → definition → quality → jurisdiction →
consequence → feasibility`. Each carries an intrinsic tense: fact/definition = past,
quality/jurisdiction = present, consequence/feasibility = future (Aristotle *Rhet.* I.4–8).

**Appeals:** `ethos` (builds Face) · `pathos` (builds Room) · `logos` (neither).

**Styles = Genre × Orientation (4):** `precedent` · `suppression` · `vision` · `insinuation`.
Genre-of-chosen-style matching the live stasis's primary genre grants the CR4 `+1D`.

**CR5 self-backfire:** an Obscuring-style move that lands *nowhere* (`deg == 0`, a *nigrahasthāna*)
strips the mover's own Face by `min(2, own Face)` — bounded by your own standing. A landed obscuring
move, even a partial, costs nothing.

### 5.5 The eight proceedings (all BUILT)

| Proceeding | Exchanges | Roles | Resistance | Adjudicator | Tracker |
|---|---|---|---|---|---|
| Formal Contest | 3 | alternating | standard | Crowd | required |
| Grand Contest | 5 | alternating | standard | Crowd | required |
| Royal Audience | 3 | Crown objects | halved for petitioner | Expert Judge | required |
| Church Tribunal | 1–5 | Inquisitor proposes | halved for accused | Expert Judge | required (starts at 6; start_ground = FACT) |
| Guild Arbitration | 3 | symmetric | standard | **Panel** (ED-1059) | required |
| Casual Dispute | 1 | initiator proposes | n/a | none | none |
| Private Negotiation | 1–3 | symmetric | n/a | none | **optional** |
| Personal Appeal | 1 | appealer proposes | n/a | none | **optional** |

Adjudicator model: `learned` / `hostile` (feed self-gating) + `discipline` + a character weight over
{ethos, pathos, logos} (feed resonance). A `Panel` aggregates members behind the same interface.
`Pressure(toward, institutional, public)` is a thumb on the scale: institutional bias multiplies
gain, public pressure raises leak *and* biases.

### 5.6 Contest gaps

- **No in-kernel "Appraise the opponent's style" move.** The `agon_harness` documents this as
  WORKAROUND 1: a real "spend the beat to Appraise" mechanic is future kernel scope.
- Face strain/Rattled: unrealised (§5.3).
- The **two representations of Face** (Charisma×3 vs the 0–10 ethos scale) is an open decision.
- Three resolution models under one name (2026-08 audit) — unresolved.
- P0 docket ED-SC-0003/0004/0005 open.

---

## 6. Fieldwork & investigation

**Live heads:** `systems/fieldwork/fieldwork_v30.md` (DESIGN) +
`systems/fieldwork/investigation_systems_v30.md` (CANONICAL).

### ⚠ 6.0 The execution status, stated plainly

**`systems/fieldwork/sim/fieldwork.py` and `investigation.py` are entirely stub-wired.** All six
entry points — `run_fieldwork_scene`, `advance_disposition`, `advance_evidence`,
`resolve_npe_response`, `evaluate_dialogue_lattice`, `apply_response_matrix` — return
`stubwire.stub_resolve(...)`: typed no-ops, design-gated on ED-916 (*"zero continuous-engine
validation at fieldwork parameters"*). **The only fieldwork code that executes is `knots.py`.**

This is the largest design-to-code gap in the repo: a rich, canonical, three-mode action surface
with no resolver.

### 6.1 The core principle

**The Intelligibility Gradient.** Depth 1–5 with a perception gate and a base Ob per depth:

| Depth | Name | Perception gate | Base Ob |
|---|---|---|---|
| 1 | Surface | — | 1 |
| 2 | Hidden | — | 2 |
| 3 | Buried | TS ≥ 10 or Disposition/access | 3 |
| 4 | Anomaly | TS ≥ 30 | 5 |
| 5 | Unintelligible | TS ≥ 50; Coherence check Ob 2 on encounter | 8 |

**Cumulative Ob modifiers:** Calamity radiation +1 per MS band below 60 at current Proximity Rating ·
active Heresy Investigation +1 to Thread-adjacent actions · **physical wounds +0.15 Ob per wound**
(never −1D; Jordan 2026-07-08, ED-PC-0005, reversing PP-716) applied only to *physically exerting*
actions (Endurance-exploration, Surveil) · Rattled marks +1 Ob per mark to social fieldwork.
**Inspiration spend:** −1 Ob (min 1) before any roll. **Ob floor: 1.**

### 6.2 Investigation actions (design-only)

| Action | Attribute | Shape | Depth access |
|---|---|---|---|
| **Examine** | Cognition | U | to Hidden (2); Buried (3) at TS ≥ 10 |
| **Interview** | Attunement | U → **superseded** | to Hidden (2); Buried (3) at Disposition +3. **ED-FI-0004 MERGE:** folds into the Dialogue Lattice, which is its one home. The bare roll is retained as the current mechanical baseline only until ED-921 / ED-IN-0016 EP-8 reconcile |
| **Research** | Recall | U | to Hidden (2); Buried (3) at institutional access |
| **Surveil** | Cognition | U | to Hidden (2). **+2 Exposure** |
| **Thread-Read** | Spirit | U | Depth 3–5. TS ≥ 30. Pool `(Spirit×2) + History + TPS`. **Co-movement fires (P-01).** +1 Exposure |
| **Reconstruct** | Recall | U | any depth reached. **`Ob = threshold − current progress`, min 1.** Synthesises; gathers nothing new |

**Evidence progress by degree:** Failure `+0` Evidence, `+2` Exposure, may yield a *false lead the
investigator cannot distinguish* · Partial `+1`/`+1` · Success `+2`/`+0` · Overwhelming `+3`/`−1`
plus a bonus revelation and `+1 Momentum`.

**Contested Investigation — the tree's other true DO mechanism:** the concealing party rolls
`(Cognition × 2) + History` at TN 7; their net successes become a **Concealment Ob added to the base
Ob**, *per action, per scene*. If they are not present to conceal that scene, Concealment Ob is 0.
The Church's institutional form is the Heresy Investigation (+1D Investigate, +2 Ob for targets in
Church territory with an Inquisitor).

**Desperate Trail (fail-forward)** and **Thread-Read as Perceptive Leap** (§4.4/§4.5) are specified,
unbuilt.

### 6.3 Social actions, non-contest (design-only)

| Action | Attribute | Ob | Shape |
|---|---|---|---|
| **Read** | Attunement | 1 / 2 / 3 by depth | U |
| **Converse** | Charisma | `1 + Disposition modifier` | **SO** (target's Disposition) |
| **Connect** | Bonds | `2 + depth sought`; requires Disposition ≥ +1 | U |
| **Impress** | Charisma | `floor(NPC Cognition / 2) + 1` | **SO** — matches the `score/2` ruling |
| **Rumour** | Charisma | 1 (tavern/market) / 2 (hostile territory) | U |
| **Negotiate** | Attunement | `floor(NPC's highest relevant stat / 2) + 1` | **SO** — matches the ruling |
| **Gift/Bribe** | — | **no roll** | — | +1 starting Disposition, one per NPC per season; fails at Disposition ≤ −2 |

**Disposition shift by degree:** Failure `−1` + Exposure `+1` + action-type locked out for the scene ·
Partial `+0` · Success `+1` + one gated info item · Overwhelming `+2` + unsolicited volunteering
(+1 Momentum if Belief-aligned).

**The Disposition Track (−5..+5)** is a stepped Ob table, not a subtraction:
Hateful `+5 Ob` … Neutral `+0` … Warm/Friendly `−1` … Trusting/Devoted `−2` … Bonded `−3`, with an
information gate at each rung (Surface → Settled → Hidden → Private → Buried → Liminal).
**Information Gates** table gives multiple routes to the same fact at different costs —
Thread-Read a site (TS ≥ 30, Ob 3) instead of talking to the NPC, but pay co-movement + Exposure.

**Sincerity Gate:** Spirit, TN 7, Ob 1. **Contest Escalation boundary** at §5.7 defines when a
Negotiate becomes a formal Contest.

### 6.4 Exploration (design-only)

**Discovery Procedure:** Pool `(Primary Attribute × 2) + History`, TN 7, Ob per Depth table.
**Multi-character:** one leads; each assistant rolls at `Ob + 1`; each assisting Success adds `+1` to
the leader's net; each assistant failure adds `+1 Exposure` **for the whole party**; max 2 assistants.
**Movement:** adjacent territory = 1 scene of travel; travel through Calamity territory (PR ≤ 2, MS ≤
40) = Endurance check Ob 1 per territory or take 1 Exposure.
**Rendering Strain at Depth 3+:** at Depth 4 (Anomaly), Coherence check Ob 1; failure Coherence −1,
and **Truth −1** if Truth ≥ 3.

**POI types:** Resource (Prosperity +1 / Muster Ob −1 / Trade Ob −1) · Secret · Remnant · Anomaly.

### 6.5 Knots (`knots.py` — **BUILT**, the one live fieldwork module)

| Operation | Formula | Shape |
|---|---|---|
| `form_knot` | prereqs Disposition ≥ 5, Bonds ≥ 5, either party TS ≥ 30; **TN 7, Ob 2** | U |
| `sustain_knot` | strain delta accumulation | — |
| `check_knot_rupture` | at strain ≥ 5 (`RUPTURE_STRAIN`); tempered at `−5` | — |
| `apply_knot_loss` | break: Composure damage 4, Disposition −3 (floor −5); rupture: Disposition −3, Coherence −1, wound-dissolution 1 | — |

Tiers `Distant` / `Close`. **Knot-Mediated Remote Investigation:** standard Thread-Read pool, TN 7,
Ob 2 (Personal scale), **cost +1 Knot strain**; the Knotted party may detect it — Spirit check TN 7,
`Ob = floor(practitioner Cognition / 2)`, min 1 (**SO**, and it matches the ruling); on detection
Disposition −3. *The Knot itself never breaks — Knots are constitutive, not contractual.*

---

## 7. Threadwork (cross-cutting)

**Live head:** `systems/threadwork/threadwork_v30.md`; **sim:** `systems/threadwork/sim/`
(1,410 lines) — **BUILT**, except `rendering.py` (stub).

Pool: `(Spirit × 2) + min(3, History + 3) + TPS`, `TPS = floor(TS/10)`. TN 7 for **every** operation
(the old binding-8 / POP-8 / POP-binding-9 differential is superseded by ED-IN-0196).

**Three-Axis Ob system** — the Ob is composed, not looked up:

| Depth (Fibonacci) | Ob | TS minimum | Coherence cost |
|---|---|---|---|
| Object | 1 | 30 | 0 |
| Personal | 2 | 30 | 0 |
| Relational | 3 | 50 | −1 |
| Field | 5 | 50 | −1 |
| Territorial | — | — | −1 |
| Structural | 8 | 70 | −2 |
| Foundational | 13 | 90 | −2 |

**Breadth Ob:** Single 0 · Small group 1 · Formation 2 · Battlefield 3 · Regional 4.
**Distance Ob:** Contact/Close 0 · Near 1 · Distant 2 · Far 3.
**Mending Ob** is a *separate* scale: Relational 2 · Field 4 · Structural 7 · Foundational 12.

### The seven operations (all BUILT, all **U**)

| Operation | Ob | Coherence | Notes |
|---|---|---|---|
| **Leap** | `2` at TS 30–49, `1` at TS 50+ | 0 | Rendering-suspension; eligibility TS ≥ 30. Failure costs no Coherence |
| **Weaving** (things cohere) | Depth Ob | by scale | |
| **Pulling** (things open) | Depth Ob | by scale | |
| **Past-Oriented Pulling** | by recency: same_scene 3 · 1–2 seasons 4 · 3–5 5 · 6–10 6 · 10+ 7 | scale −1 (capped at −1 for Object/Personal) | Generational reach is near-impossible (<0.1%) |
| **Locking** (unable to become) | Depth Ob | scale + FR surcharge (−1, cap-exempt, PP-196) | |
| **Dissolution** (unable to be) | Depth Ob | scale + FR surcharge | |
| **Mending** | **Mending Ob** | **0 at every degree** | ED-871: operation *type*, not scale, determines Coherence risk. Never produces Scars |

**Inseparability (P-01/T-03) fires on every operation** — co-movement across temporal, epistemic and
actualised dimensions (`co_movement.py`, BUILT). This is the mechanic that prevents Thread from being
a power fantasy. `opposing.py`, `collective.py`, `coherence.py`, `threadcut.py` all BUILT;
`rendering.py` is a stub.

**Wounds do not cut Thread pools** (operations are consciousness-performed, P-03) — instead
`+1 Ob` to operations requiring a Leap.

---

## 8. Cross-scale plumbing — how an action at one scale reaches another

### 8.1 The Slate is the spine (`auto_manual_resolution_duality_v1.md`, RULED 2026-07-08)

Jordan, verbatim: *"faction parliament actions are the auto-resolve version of playing them out as a
scene, in parallel to Total War where you can play the battle or auto it."*

Three fidelities of **one** slate event:

| Fidelity | The player | Precedent |
|---|---|---|
| **Played** | resolves the scene interactively | watch the full match |
| **Witnessed** | present, one free Read/Appraise roll (Ob 1, **not** auto-success), no control | commentary-only |
| **Auto** | absent; NPC AI + clock advancement resolve it | instant result |

*"Opportunities not pursued do not wait — they resolve through NPC AI and clock advancement without
player input, often in ways the player would not have chosen."* (player_agency §4.2) — **that clause
is the auto-resolve.** Zoom in = play it out; zoom out = auto-resolve.

**Scene action budget: 3–5 per season.** There are always more opportunities than actions.
*Choosing what to attend is the gameplay.*

### 8.2 Scene Slate generation (design CANONICAL; `scene_slate.py` is a priority queue only)

Priority 0 **Mandatory** (cannot be declined): Accord-0 revolt in/adjacent to the player · player is
target of a Heresy Investigation · mass battle in the player's territory · faction leader
assassinated/overthrown. Priority ordering when several fire: Leader Removal → Heresy Target →
Stability Crisis → Mass Battle → Knot Partner in Crisis → Companion Arc → Settlement Revolt → Rank
Advancement. **Witness Mode** handles overflow (no Domain Echo, no Momentum/Coherence cost).

Priority 1 **Crisis Events** (presented, optional), then world-state and Conviction-biased entries.

### ⚠ 8.3 What actually fires in code

`scene_dispatch.evaluate_triggers` fires **exactly one** canonical trigger: Stability Crisis
(`Faction.Sta ≤ 2` → an emergency-council contest). **The other seven §4.3.2 mandatory triggers are
reported as `deferred`, not faked** — the aggregate World lacks the schema.

- **Contest scenes:** resolve through the promoted kernel (`build_contest`/`resolve_contest`) —
  **live**, routed via `guild_arbitration` as the emergency-council proceeding ([SEED]).
- **Combat scenes:** a bridge exists (`combat_bridge.py`) behind `DISPATCH_COMBAT_BRIDGE`,
  **default OFF**, and **no trigger anywhere in the tree queues a combat scene** — the bridge closes
  the *resolution* half of the gap, not the *trigger* half.
- **Outcome→echo mapping:** deliberately empty except emergency_council (Mandate channel) and the
  combat ON-branch (Mil channel). The scene phase is **side-effect-free on strategic state by
  default** — so wiring it in cannot regress the strategic loop.

### 8.4 The season tick (`engine_clock.py`, live 2026-08-27)

Three phases, one owner: `season_tick → action → accounting_boundary`. `_faction_actions_callback`
is the ACTION phase's body. The boundary crossing was previously miscounted, deferring every
accounting-phase settlement-locus Key by one tick — fixed at the phase re-siting.

---

## 9. The faction management system — what exists, what's missing

You are right that this is the hole. Here is the precise shape of it.

### 9.1 What exists

| Layer | State |
|---|---|
| Faction **stats** | Six, registry-clamped: Mandate/Legitimacy (L), Influence (I), Wealth (W), Military (Mil), Stability (Sta), plus `standing`. Jordan ruled "Legitimacy is a base"; `fac.legitimacy` is declared in `descriptor_registry.yaml`. **SETTLED.** |
| Faction **holdings** | `faction.territories` — a bare list of territory ids. `Territory` carries `owner`, `garrison`, `accord`. |
| Faction **action selection** | `faction_take_action` — state-conditioned, working, one action/season. |
| Faction **rank ladders** | `faction_politics_v30.md` (CANONICAL): Standing 0–7, sub-office ladders, caste system, four ladders (Crown Administrative, Church, Warden, Guild) with §1.0b Recognition Fork, §1.0c Court Attendance + hostage-kin, §1.0d Patron-Sponsored Performance Audit, §2.5a Guild entry/mastership. |
| Faction **politics** | Parliament (partially built), treaties (expiry only), CI track, occupation, casus belli. |

### 9.2 What is missing — five named gaps

1. **`domain_actions` has `doc: null`.** The module contract exists, `resolver: d_sigma` is declared,
   and there is **no home design document**. The action catalogue lives only in a frozen prose
   capture that §0.05 classifies as reference. *This is the foundation stone.*
2. **There is no officer/roster object.** A faction has territories and five scalars. It has no
   personnel: no appointable governors, no commanders, no ministers, no succession pool. The
   settlement layer's §3.2 Governor Assignment presupposes one; nothing supplies it.
3. **No holdings model below "a list of territory ids".** Facility tiers, Wings, Church's four
   infrastructure axes, and per-settlement L/PS are all designed (`settlement_layer_v30` §1.4–§1.8)
   and **PRE-LPS-1** in code: `faction_action.py` reads scalar `L` at territory grain, and
   ED-FA-0004 (the schema gap) is still open.
4. **No activity/queue model.** One action per faction per season, drawn stochastically. There is no
   multi-season project, no standing policy, no delegation — Great Work's Open Pledge was the one
   multi-season mechanic and it was simplified to instant-resolution (deferred to PP-515).
5. **Fiscal Stance is PROPOSED-only.** `faction_layer_v30 §5.9` (ED-FA-0008) specifies Light ×0.75 /
   Standard ×1.0 / Extraction ×1.5 with per-settlement PS consequences, grounded in Levi 1988
   (quasi-voluntary compliance), Scott 1976 (the subsistence ethic reads *invariance*, not level, as
   injustice) and Brewer 1989. **No Treasury sim coupling exists.**

### 9.3 The precedent research that already exists in this repo

Three research dockets bear directly on this and are **filed, partly executed, not canon**:

- **`research/rise_to_power_roster_system_research_v1.md`** — the officer/roster proposal, ~96
  historical cases distilled into **eight mechanisms**, each with its rise *and* its characteristic
  downfall baked into the same structure:

  | | Mechanism | Downfall shape |
  |---|---|---|
  | M1 | Patronage chains (clientelism) | collapses **top-down** when the patron falls |
  | M2 | Credentialed merit | capped for the un-tutored; reversible by rewriting the criteria |
  | M3 | Kinship / marriage alliance | **generational flip** or demographic lapse |
  | M4 | Court proximity / favouritism | **binary, not graduated** — loss of intimacy is total |
  | M5 | Bureaucratic chokepoint control | undone by a **single bypass channel** |
  | M6 | Purchased office (venality) | **no loyalty reserve** |
  | M7 | Armed retinue | **coalition purge** or subordinate-flip |
  | M8 | Ideological/moral authority | only **outcompeted in its own currency**, or purged covertly |

  Two cross-cutting findings: **power routinely detaches from formal rank** (Michinaga, Cosimo,
  Heshen) — so the system cannot be "climb the Standing ladder" alone; and **consolidation is
  self-limiting by construction** — every rise writes a legible vulnerability in the same field the
  rise reads. That symmetry is exactly Valoria's Ω-d non-dominance principle.

  It also flags a **naming collision that must be resolved before building**: mass battle already
  uses "officer". The political rank must be *household member* / *retinue* / *protégé seat* — one
  NPC legitimately holds both, and the fields must not collide.

- **`research/proactive_governance_scale_research_v1.md`** and the comparative-governance docket —
  44 proposals, ~15 already authored into `faction_politics_v30`/`settlement_layer_v30` as PROPOSED.
- **`research/historical_concerns_action_catalogue_v1.md`** — the event-deck crisis catalogue.

**Acclaimed-game precedent already cited in canon:** KOEI *Romance of the Three Kingdoms* (officer-
city assignment, development, provincial control) and *Crusader Kings III* (barony-county-duchy-
kingdom hierarchy, vassal governance, realm fragmentation) are the declared precedents at
`settlement_layer_v30`'s header. `player_agency_v30 §1` adds ROTK Officer Mode, CK3 Vassal Play,
Disco Elysium, Mount & Blade / Manor Lords, Pathologic 2 and Pentiment. The governance redesign
names the EU4-estate / Shadow Empire principal-agent friction as the model for its method-choice
tradeoffs, and Football Manager for the played/witnessed/auto fidelity ladder.

### 9.4 The build order this implies

1. **Author the `domain_actions` home doc** — it is the one `doc: null` module that gates the whole
   faction surface, and it already has a resolver grade (`d_sigma`) and a frozen action list to
   ratify or supersede.
2. **Rule the `score/2` obstacle question** (§0.2). It is suspended, not unresolved-by-neglect, and
   three built sites disagree today.
3. **Then** the roster: one object, `household_roster` + `upward_patron` edges on the existing Knots
   graph, `clientele_breadth` as a derived query (the research explicitly proposes no new storage).
4. **Then** the holdings model — LPS-1 (per-settlement L/PS), which closes ED-FA-0004 and unblocks
   Fiscal Stance, the Assessment/Compact tags and the Directive.

---

## 10. Summary — build status by scale

| Scale | Actions specified | Actions executing | The honest state |
|---|---|---|---|
| **Faction** | ~35 (4 generic + 16 unique + 10 parliamentary + Domain Action catalogue) | **~11** | Selection model and the four generic actions are solid. Varfell and Hafenmark have no working unique action. 5 of 5 constructive parliamentary motions and 4 of 5 sanction tiers unbuilt. Treaty proposal raises. |
| **Settlement governance** | ~14 verbs + 6 Directive types + 5 tag families | **0** | Entirely design-side. The richest *unbuilt* surface in the repo, and the one with the most historical grounding already done. |
| **Mass battle** | 31 mechanics, 15 roles, ~18 instructions, 5 order triggers | **31 mechanics; 7 of 18 instructions** | The most complete system. Tactic cards are a BLOCKED empty dict; role instructions are an inert scaffold; terrain is `None` at the faction seam. |
| **Personal combat** | a continuous model, not a menu | **the whole model** | Executes end to end. Contact/grapple node built but unactivated; 3 morphology levers bare; 1 lever dead; the degree ladder is a declared hold. |
| **Social contest** | 7 moves × 8 proceedings × 4 styles × 6 grounds × 3 appeals | **all of it** | Executes. Face has no strain channel; no Appraise move; three resolution models under one name (audit finding); ED-SC-0015 needs a ruling. |
| **Fieldwork / investigation** | 6 investigation + 7 social + exploration + 5-depth gradient | **knots only** | Six entry points are typed no-ops, design-gated on ED-916. The largest design-to-code gap in the tree. |
| **Threadwork** | 7 operations × 3-axis Ob | **7 of 7** | Executes, including co-movement. Only `rendering.py` is a stub. |
| **Cross-scale** | 8 mandatory triggers, 3 fidelities | **1 trigger; contest only** | Combat bridge default-OFF with no trigger to fire it. Echo mapping deliberately empty → scene phase is side-effect-free by default. |

### 10.1 Opposed/unopposed census

| Shape | Count of named actions | Where |
|---|---|---|
| **U** — unopposed vs world/self Ob | the large majority | Muster, Govern, Royal Progress, Great Work, Council, Absolution, Mass Seizure, all 7 Threadwork ops, all 6 Investigation actions, Read/Connect/Rumour, most governance verbs |
| **SO** — statically opposed (Ob from target's score) | ~12 | Coronation Renewal, Excommunication Tribunal, Parliamentary Transfer, Spy, Diplomacy vs NPC, Crown Treaty, Parliamentary Manoeuvre, Dynastic Proclamation, Impress, Negotiate, Converse, Knot-intrusion detection, Ordenanza Amend, Revoke Management, Hold Court |
| **DO** — dynamically opposed (opponent rolls) | **2** | Contested Investigation (Concealment Ob) · social-contest `rebut` |
| **BI** — bilateral model, no Ob | 4 | Personal combat, Mass battle, Conquest (delegates), the social-contest Bout as a whole |
| **No roll** | 4 | Gift/Bribe, Retain Clerks, Levy, March (contested entry = battle) |

**The design observation worth carrying:** Valoria has almost no true opposed rolls. Opposition is
carried either by *the target's score as an obstacle* (SO) or by *a differential model* (BI). The
`score/2` ruling is the attempt to make the SO family coherent, and it is the single highest-leverage
unexecuted decision in the tree — it touches every SO row above.

---

## Sources read

Code: `engine/autoload/{dice_engine,sigma_leverage,engine_clock,scene_slate,victory}.py` ·
`engine/cross_scale/{scene_dispatch,zoom_in_out,combat_bridge}.py` · `engine/mc_v18.py` ·
`references/module_contracts.yaml` · `systems/factions/sim/*.py` (17 modules) ·
`systems/settlements/sim/` · `systems/mass_battle/sim/**` · `systems/combat/combat_engine_v1/*.py` ·
`systems/social_contest/sim/contest/*.py` · `systems/fieldwork/sim/*.py` ·
`systems/threadwork/sim/operations.py` · `engine/engine_params/params_tables.yaml`.

Docs: `CURRENT.md` · `systems/settlements/{settlement_layer_v30,governance_play_redesign_v1}.md` ·
`systems/factions/faction_layer_v30.md` · `systems/fieldwork/fieldwork_v30.md` ·
`systems/_architecture/{auto_manual_resolution_duality_v1,player_agency_v30,throughlines_complete}.md` ·
`research/rise_to_power_roster_system_research_v1.md` · `registers/handoffs/HANDOFF_{FA,PC,SC}.md`.
