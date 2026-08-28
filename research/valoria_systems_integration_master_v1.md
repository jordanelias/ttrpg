# Valoria Systems Integration Master — Part 1: Collation and Slices

## Status: PROPOSED (2026-08-28)
## Version: v1.0
## Lane: IN (cross-cutting) · reads FA, SE, WR, PC, SC, FI, MB, GO
## Parts: this file · `_part2` (within-system analysis) · `_part3` (cross-category comparison and integration proposals)

**Reading order:** [Part 1 · Collation and Slices](valoria_systems_integration_master_v1.md) → [Part 2 · Flatten, the Personal Half](valoria_systems_integration_master_v1_part2.md) → [Part 3 · Within-System Analysis](valoria_systems_integration_master_v1_part3.md) → [Part 4 · Cross-Category Comparison and Proposals](valoria_systems_integration_master_v1_part4.md)


**What this is.** A single collation of every faction, personnel, settlement, governance, territory,
NPC and political mechanic in the repository — from `proposals/`, `research/`, `audit/2026-07-12-governance-compendium/`,
`systems/`, and the live code — sorted by gameplay system, sliced by kind, flattened, analysed
within and across systems, and resolved into four rival integration proposals.

**What it is not.** It is not canon and does not ratify anything. Under `CLAUDE.md` §0.05 this
document is *reference*: the code is the mechanism. Every `status` below was measured against the
working tree, not against a document's own header — that distinction is load-bearing and it is the
single most common error this collation corrects.

---

## §1 COLLATION — the corpus, and how it was sorted

### 1.1 Sources read

Eleven parallel harvest lanes read the corpus and emitted **1,079 structured records**. The lanes
and their beats:

| lane | beat |
|---|---|
| H1 | `research/` — cross-scale action catalogue, personnel/muster integration master (the PR #336 baseline) |
| H2 | `proposals/` — social contest consolidation, throughlines and precedent, conflict architecture |
| H3 | `systems/_architecture/` — propagation spec, derived stats, player agency, key substrate, holonic doctrine |
| H4 | `audit/2026-07-12-governance-compendium/` — all 10 files, including `_workings_joined.md` |
| H5 | `systems/factions/` — 18 design docs + `sim/` (17 modules, 2,747 lines) read in full |
| H6 | `systems/settlements/` + `systems/world/` — settlement layer, scale hierarchy, insurgency, strain |
| H7A/H7B | `systems/_architecture/scale_transitions_v30.md`, `engine/cross_scale/`, `engine/substrate/` |
| H8A/H8B | `research/` roster and historical-precedent corpus; `research/governance/` |
| H9 | `engine/` core — `game_state`, `dice_engine`, `sigma_leverage`, `victory`, `mc_v18` |

### 1.2 Two coverage limits, stated rather than papered over

1. **`systems/fieldwork/` (21 documents) and `systems/social_contest/` (6 documents plus ~18 Python
   modules) appeared on no lane's manifest.** The five records tagged `fieldwork-investigation` are
   mistagged knot and faction facts. Their absence from the flatten is a coverage hole, **not a
   finding that they are thin.** Where they cross into another system they appear there; nowhere else.
2. **Code citations from six of eleven lanes are advisory.** H1, H2, H3, H4, H8B and H9 emitted
   code-level `status_evidence` without opening a code file; H5 and H6 read their modules in full.
   That split correlates near-perfectly with the adversarial gate's error rate (H5/H6: 1 citation
   failure in 34 sampled; H3/H4: 7 in 14). Every code claim reproduced in this document was
   re-verified against disk before inclusion; claims that could not be re-verified were dropped.

### 1.3 The correction that mattered most

The adversarial gate on §2 confirmed **six overturns**, and their root cause was a single date
window: the harvest's design-doc sources are dated 2026-08-15 through 08-19, and thirteen commits
landed between 08-22 and 08-27. Corrected here and carried into every later section:

- `Faction.adjust` now reads per-stat bounds from `descriptors.faction_bounds` (2026-08-22/23), so
  "unbounded stats" is false for the six declared stats — but **true for `Faction.standing`**, which
  is a bare int outside that registry.
- `roll_pool` now **refuses** any TN but 7 (`_require_tn7`, ED-IN-0196, 2026-08-25).
- `mass_seizure.py:296` now writes `t.accord = ACCORD_MAP[starting_accord]` (ED-FA-0037) with four
  regression tests.
- The conviction roster has a single owner (`descriptors.CONVICTIONS`) as of 2026-08-24.
- The mass-battle canon engine was ported over Tree A on 2026-08-24; `massbattle.py` is now a
  146-line adapter, not the 1,905-line engine. Every record describing Tree A as live is closed.

A seventh correction is **mine**, and it is the sharpest methodological lesson in the exercise. I
reported the ledger tag family `Compact` as an open six-lane convergence. It is not open: ED-IN-0046
D3 **ruled it on 2026-07-13** — *"Compact models as a recurring Debt subtype, not a 6th
ledger.TAG_KINDS family"* — and the live enum's fifth member is `Leverage`. Six lanes agreed with
each other because all six were reading prose descended from one pre-ruling source, **including my
own merged baseline at `research/cross_scale_action_catalogue_v1.md` §2.4, which is the strongest
surviving carrier of the error.** Convergence measured agreement, not truth. That document needs a
separate correcting edit; it is named here so the error does not propagate again.

### 1.4 The twelve systems

Records were sorted into a closed set of twelve gameplay systems. The set is closed so that a record
cannot be filed under a category invented to hold it.

| system | records | one-line beat |
|---|---|---|
| faction-strategy | 276 | What a faction is, and the one action it takes per season |
| settlement-governance | 230 | The civic unit, its officers, budget, memory and events |
| npc-social | 124 | Who a person is — convictions, disposition, relational edges, memory |
| territory-world | 109 | The map, its clocks, insurgency, victory |
| cross-scale-plumbing | 97 | The Key substrate and the eight scale handoffs |
| personnel-roster | 97 | What a person holds — rank, office, power base, the climb |
| parliament-politics | 51 | The chamber, its motions and its sanctions |
| mass-battle-seam | 32 | Where faction scale meets the battle engine |
| economy-accounting | 24 | Wealth, treasury, yield, the season's books |
| resolution-kernel | 20 | Dice, obstacle, degree — seams only; the kernel itself is settled |
| social-contest | — | **coverage hole** (see §1.2) |
| fieldwork-investigation | 5 (mistagged) | **coverage hole** (see §1.2) |

`personnel-roster` and `npc-social` are flattened as one system in §3, because the corpus's live
vocabulary collision runs *between* them rather than inside either: **npc-social owns who a person
is; personnel-roster owns what a person holds**, and a person object satisfying one would not
satisfy the other.

---

## §2 SLICES — the eight kinds of thing

Every record carries exactly one slice. The set is closed, and the distinctions are mechanical rather
than editorial — each one answers a different question about where a thing can break.

| slice | definition | the question it answers |
|---|---|---|
| **primitive** | Stores state. A field, a track, an entity. | *Where does this live between seasons?* |
| **derivative** | Computed from primitives; stores nothing. | *What happens when its inputs move?* |
| **formula** | The expression itself, independent of who evaluates it. | *Is this arithmetic the same everywhere it appears?* |
| **mechanic** | One resolution event with an input, a roll or check, and an output. | *What does the player do, once?* |
| **process** | Several mechanics in a fixed order, usually on a clock. | *What happens every season whether or not anyone acts?* |
| **ruling** | A Jordan decision, with or without execution. | *Is this still open?* |
| **content** | Named instances — the 46 characters, the 37 settlements, the 17 provinces. | *Is there anything to populate this with?* |
| **gap** | A measured absence or a contradiction between two live surfaces. | *What is missing, and is it missing in the strong sense?* |

### 2.1 Status, and why the vocabulary is measured rather than declared

`status` is the axis on which this corpus most often lies to itself, so it is defined against
execution, per `CLAUDE.md` §0.2:

| status | means |
|---|---|
| **BUILT** | The code exists and a production path reaches it in a seeded campaign. |
| **INERT** | The code exists and is correct, and **nothing calls it.** |
| **DESIGNED** | Authored in canon, with a `## Status:` line, and no code. |
| **PROPOSED** | In `proposals/`, `research/` or `audit/`; not canon. |
| **RULED-UNEXECUTED** | Jordan decided it; the code does not reflect the decision. |
| **SUPERSEDED** | A later ruling or commit replaced it. |

**INERT is the finding.** It is not a synonym for unbuilt. Across the twelve systems, the corpus's
characteristic failure is not missing design and not broken code — it is **finished, correct
machinery with no caller.** §5 counts them.

One vocabulary warning, because it cost real analysis time: `npc_relational_graph_v30.md` §7 and §8
carry the header **"BUILT 2026-06-09, ED-1000"** for the Defection Cascade. There is no code — a
tree-wide grep for `relational_edges`, `defection_cascade`, `sworn_bond`, `liege_vassal` and
`hop_distance` across `engine/` and `systems/` returns zero Python hits. In that document's internal
vocabulary "BUILT" meant *a design decision was finalised*. That usage is defensible internally and
reads, to everyone else, as a claim about the engine. It is the clearest instance in the corpus of
why §0.05 exists.

### 2.2 Shape, for anything that resolves

Records that roll carry a contest shape, inherited from the PR #336 baseline:

| shape | meaning |
|---|---|
| **U** | Unopposed — pool against a fixed or state-derived obstacle |
| **SO** | Statically opposed — obstacle derived from a target's score, target does not roll |
| **DO** | Dynamically opposed — both sides roll |
| **BI** | Bilateral — both sides roll and both sides' outcomes bind |

Measured across the tree: **all seven obstacle-bearing production rolls live in `systems/factions/sim/`.**
Six of the seven other resolving subsystems derive their obstacle locally and pass a bare pool to the
roller, which is why the obstacle has no owner. That fact drives a proposal in `_part3`.

---

## §3 FLATTEN — the strategic half

Each system is flattened into four tables (primitives · derivatives and formulae · mechanics ·
processes) with a `status` measured against the working tree. `where it lives` is a file and line,
or the word *absent*.

The remaining four systems — **People**, **cross-scale-plumbing**, **resolution-kernel** and
**mass-battle-seam** — are flattened in `_part2`. Two are flattened seam-only (kernel, mass battle)
because their interiors are settled and only their edges are in scope; two are not flattened at all
(**social-contest**, **fieldwork-investigation**) per the coverage limit in §1.2.

### FLATTEN — "faction-strategy"

*Parliament rows are held back for the parliament-politics sub-cluster below. Of the 51 records tagged `parliament-politics`, about half were genuinely parliamentary; the rest were treaty machinery, officer-ladder content, Casus Belli plumbing and Church-tribunal formulas parked there by term association and are re-homed into this table.*

## Primitives

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| `Faction` | primitive | The whole faction model: `name`, `parliamentary`, six stats, a `territories` list, four turn-tracking booleans. Nothing else. | BUILT | `engine/autoload/game_state.py:109-140` |
| `Faction.L` (Legitimacy / Mandate) | primitive | The load-bearing scalar. Gates Censure, Excommunication, Absolution; is the pool for Great Work, Tribunal, Council, and every parliamentary vote; is the obstacle for Transfer and Tribunal. 20 of 31 `adjust` calls target it. | BUILT | `game_state.py:112`; `MULTS['L']=20` at `:74` |
| `Faction.Sta / W / I / Mil` | primitive | Four scalars clamped by `descriptors.faction_bounds(stat)` — all six declared stats floor 0, ceiling 7 (2026-08-23 ruling). | BUILT | `game_state.py:113-117`, `adjust` at `:154-197` |
| `Faction.intel` | primitive | Declared at `0.0`. No `MULTS['intel']` row, so `adjust('intel', …)` raises `KeyError` before any bound is consulted. Never read, never written. | INERT | `game_state.py:118-124` |
| `Faction.standing` | primitive | A bare unbounded `int`, mutated by `+=`/`-=` at eleven sites, never through `adjust()`, so it never sees the registry clamps. Feeds two dice pools whose outcomes write it back — two undamped positive-feedback loops. | BUILT | `game_state.py:129`; `crown_initiative.py:81,98,116,119,167,177,254,267,270`; `absolution.py:86`; `parliamentary_transfer.py:379` |
| Standing 0-7 officer ladder | primitive | A **different quantity** sharing the name: eight rungs per ladder across four primary and seven sub-office ladders, each rung carrying an entry gate and a demotion cell. No rung executes in either direction. | DESIGNED | `systems/factions/faction_politics_v30.md:38` |
| `Faction.territories` | primitive | A list of territory ids — the only field that represents faction power beyond the six stats. No people, no holdings model, no tier. | BUILT | `game_state.py:126` |
| The live faction roster | content | Four instances: Crown, Church, Hafenmark, Varfell. Canon names six to eight; Guilds, Restoration Movement and Löwenritter have no instance. | BUILT | `STARTING_STATS` via `references/world_initial_state.yaml` |
| Faction personality | primitive | Implemented as `if faction.name == 'Crown'` / `elif == 'Church'`. Hafenmark and Varfell have no branch — swap their names in the starting table and the campaign is unchanged. | BUILT | `faction_action.py:308,324,346` |
| `world.casus_belli` | primitive | An optional duck-typed dict read for every CB source except Crown's auto-refreshing restoration clause. Zero writers anywhere. Every other CB source is unreachable in a fresh campaign. | INERT | `parliamentary_transfer.py:111-121,331-335` |
| `world.treaties` | primitive | A real serialized per-campaign dict of `TreatyRecord`. No module owns it; nothing creates or ends an entry. | INERT | `game_state.py`; `treaty.py:120-160` |
| Shadow Renown 0-10 / Deniability Debt 0-7 | primitive | Riskbreaker covert tracks with a 7-step ladder to mandatory demotion. No field, no key type; three registries mark Deniability Debt deprecated while the source says retained. | DESIGNED | `faction_politics_v30.md:432,462` |
| Faction card-hand + cooldown economy | primitive | Per-faction typed 6-card hands gating which Domain Actions may be played, 1-2 season cooldowns. A structurally different action economy from the one that runs; neither document acknowledges the other. | DESIGNED | `ci_political_v30.md:263-316` |
| `aims` / `redLines` / `threat` / `patience` | primitive | Proposed opposition-memory fields so a faction can obstruct across seasons and concede. None exist. | PROPOSED | `proposals/social_contest_consolidation_integration_v1.md:374` |
| Faction tier (local / provincial / national) | primitive | Ruled independent — a faction holds people, not necessarily territory. No tier field, no population-held field. | RULED-UNEXECUTED | `systems/settlements/scale_hierarchy_v1.md:81,102` |

## Derivatives and formulae

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| Action-selection policy | formula | Base priors 0.30 unique / 0.35 conquest / 0.20 muster / 0.15 govern, re-weighted by three RNG-free state signals (target-exists + military advantage, undergoverned share, proximate threat), renormalised, then **one** `rng.random()` draw against cumulative thresholds. This is the only action-selection mechanism that runs. | BUILT | `faction_action.py:55-58,208-273` |
| Muster | formula | `pool = Mil + floor(W/2)`; `Ob = 1`; Wealth charged up front unconditionally; Overwhelming +5 / Success +3 granular Military; no failure penalty. | BUILT | `faction_action.py:531-559` |
| Muster's Wealth cost, at scale | formula | `adjust('W', -1)` passes a *granular* delta that `adjust` divides by `MULTS['W']=100`, so one muster costs **0.01 Wealth**, not 1. The three sibling cost sites in `crown_initiative.py` multiply by 100 first and charge full points. Verified by execution. | BUILT (defect) | `faction_action.py:77,546` vs `crown_initiative.py:91,161,246` |
| Govern | formula | `pool = I`; `Ob = 2` fixed; Overwhelming Accord +15 / Success +10 / Failure `Sta -5` granular. | BUILT | `faction_action.py:562-581` |
| Govern — three rival formulas | gap | Code uses Influence vs flat Ob 2. `ci_political_v30 §4.2` uses Mandate vs `floor(Prosperity/2)+1`. `military_layer` / `parliamentary_transfer_v30` corroborate the Prosperity form. Different pool *stat* and different obstacle *shape*. | — | `faction_action.py:562-580`; `ci_political_v30.md:219-231` |
| Royal Progress | formula | `Ob = max(2, floor((7·n_owned − Σaccord)/2))`; `Pool = int(I) + standing`; `W −2` regardless of outcome. | BUILT | `crown_initiative.py:39-122` |
| Great Work | formula | `Pool = int(L)`; `Ob = 4`; pays all three seasons' Wealth (−3) up front. Multi-season pledge tracking deferred. | BUILT | `crown_initiative.py:127-181` |
| Coronation Renewal | formula | `Ob = floor(Church.L/2) + 1`; `Pool = Crown.I`; `W −2`. Lifts Excommunication. | BUILT | `crown_initiative.py:189-273` |
| Council of Solmund | formula | `Ob = floor(CI/30) + 2`; `Pool = int(Church.L)`; 1/arc. | BUILT | `council_solmund.py:30-33,49-92` |
| Absolution | formula | `Pool = int(Church.I)`; `Ob = 3`, self-flagged `[M6_ASSUMPTION_ONE]` — not ratified; `Church.L −1` regardless of outcome; Failure decrements `Church.standing`, not `L`. | BUILT | `absolution.py:33-107` |
| Excommunication Tribunal | formula | `Pool = int(church.L)` +1D on formal grounds; `Ob = max(1, round(accused.L))`, halved on formal grounds (CI≥40 and Church.L≥4). | BUILT | `tribunal.py:95-140` |
| Excommunication — three rival formulas | gap | Code as above; `faction_canon_v30 §9` says `M = Mandate − target Mandate` with no halving concept; `factions_personal_v30 §8.3` gives a third. | — | `tribunal.py:113-121`; `faction_canon_v30.md:339` |
| Mass Seizure | formula | Declaration `P = ((CI−60)/40)^3.3`, forced at CI 100, gated on `Church.L ≥ 4`, one-shot lifetime. Per-territory `Pool = Church.I + floor(CI/15)`; `Ob = max(1, 10 − canonical_pt − infra_mod)`. | INERT | `mass_seizure.py:141-298` |
| Seizure Ob modifier stack | formula | Chapel 0, Church −1, Cathedral −2, Templar −1, Inquisitor −1, Church Governor −2; capped −4 per settlement. | BUILT (unreached) | `systems/settlements/sim/infrastructure.py:236` |
| Conquest | formula | Delegates to `resolve_mass_battle`; on attacker win, territory moves, loser takes `adjust('L', −10)` granular (= −0.5 points), garrison set. | BUILT | `faction_action.py:432-528` |
| Terms / Storm fork | formula | Defender not routed (Success) → Accord Terms + an `entry_terms_l_seed` nothing reads; routed (Overwhelming) → Storm baseline. AI always takes Terms when available. | BUILT | `faction_action.py:508-524` |
| LPS-1 Mandate aggregate | formula | `Mandate = clamp(round(7T/(T+6)), 0, 7)` over per-settlement Legitimacy and Popular Support. Ratified; no per-settlement L or PS exists, so this is a counterfactual about unbuilt code while `Faction.L` is written directly as if it were Mandate. | RULED-UNEXECUTED | `settlement_layer_v30.md:165` |
| Faction derived values | derivative | Legitimacy = Mandate×20, Treasury = Wealth×100, Levies = Military×2, Reputation = Influence×15, Discipline = Stability×10, with the rule that no event may touch a 1-7 stat except through derived-value depletion or a named structural event. | DESIGNED | `systems/_architecture/derived_stats_v30.md:295-320` |
| Aggregate-Up Transform | ruling | Ratified 2026-07-02: `faction_stat[s]` has **no setter** — it equals an aggregate over holdings plus decaying event modifiers. Every one of the 31 direct `adjust` sites violates this. | RULED-UNEXECUTED | `systems/_architecture/propagation_spec_v1.md:145` |

## Mechanics

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| Crown Initiative | mechanic | Crown's unique slot: a heuristic picks Royal Progress, Great Work, or Coronation Renewal (the last only while excommunicated). | BUILT | `crown_initiative.py:294-317` |
| Excommunication | mechanic | Church strips a rival's Legitimacy via a single-roll abstraction of the Tribunal; sets `target.excommunicated`; Failure costs Church `L −1` and grants the target sympathy `L +1`. | BUILT | `excommunication.py:78-193` |
| Church priority chain | mechanic | Excommunication → Council → Absolution, in that fixed order, each with its own gate. Mass Seizure is **not** in the chain. | BUILT | `faction_action.py:324-344` |
| Mass Seizure | mechanic | Fully implemented one-shot Church territorial conversion with **zero production callers** anywhere in `engine/` or `systems/` — confirmed by grep; its only invocation is `tests/valoria/test_mass_seizure_accord_write.py`. | INERT | `mass_seizure.py` (whole module) |
| The six faction stubs | mechanic | `charter_liberties`, `hafenmark_equipment`, `home_sanctuary`, `infrastructure_reclamation`, `varfell_mandate_action`, `varfell_territorial_acquisition` are all typed `stubwire.stub_resolve` no-ops with no logic. | INERT | the six modules, each at its single `def` |
| Canon §9 unique-action table | mechanic | Names Royal Decree (Crown, Mandate vs Ob 2), Sovereign Authority Doctrine (Hafenmark, Mandate vs Ob 4), The Private Collection (Varfell, Intel vs Ob 2), Economic Leverage (Guilds, Wealth vs target Wealth). The code implements **none of these under those names or those formulas**; Hafenmark, Varfell and the Guilds have no faction-specific action at all. | DESIGNED | `faction_canon_v30.md:336-345` |
| Treaty | mechanic | `propose_treaty` is a typed no-op; `register_treaty` is a test helper keyed by tuple against a frozenset-documented store; `process_treaty_expirations` is fully implemented at a flat 0.90 hazard. All three have zero production callers, and with no RNG the fallback roll is fixed at 0.95, so `0.95 < 0.90` makes lapse impossible on that path. | INERT | `treaty.py:99-160` |
| Faction Collapse Exit Procedure | process | Six steps at Stability 0: Mandate→0, territories→Uncontrolled, officers→Independent, seat lost, victory closed, Reconstitution at 50% frozen stats. No collapse detection exists. | DESIGNED | `faction_layer_v30.md:207` |
| Universal Succession Contest | process | Two stages — who leads (resolver), then whether the realm fragments (deterministic strength gap G). Subsumes the Crown-specific Baralta mechanic. No code implements succession for any faction; `Faction` has no leader field. | DESIGNED | `faction_succession_split_v30.md:22` |
| Stability Trigger system | process | Stability may change only from five named triggers plus the Accounting cascade. The live code adjusts Stability ad hoc from inside individual action modules with no trigger registry. | DESIGNED | `faction_layer_v30.md:49` |
| Duty system | mechanic | Eight Duty types generated from the leader's AI priority stack, moving the player's 0-7 Standing (+1 / +2 / −1, floored at 1 once initiated) with fixed per-rank unlocks. | DESIGNED | `systems/_architecture/player_agency_v30.md:120,147` |
| Löwenritter Graduated Autonomy | mechanic | Loyal → Restless → Autonomous → Split, each stage with named triggers; stages 1-3 reversible. | DESIGNED | `conflict_architecture_proposal.md:68` |
| Royal Assassination Fuse / Tensions Deck | mechanic | One assassination fires at a randomised S8-S12 unless investigated during a visible S1-S7 fuse; a 6-card deck drawn once sets fuses on five friction points. | DESIGNED | `conflict_architecture_proposal.md:85,119` |
| Altonian invasion | mechanic | Three IP-gated escalation phases with a Governorate stat block, and three named permanent repulsion paths. | DESIGNED | `campaign_architecture_v30.md:153,165` |
| Faction Emergence / Collapse (scale) | process | Cell → Organization → Movement → Faction → Hegemon bottom-up, and national → city-state → dissolved downward. No key type announces a faction coming into or going out of existence. | DESIGNED | `settlement_layer_v30.md:1027,1065` |
| AI threat-priority posture stack | process | A six-tier stack (Existential → Defend → Consolidate → Counter-threat → Expand → Opportunistic) evaluated in order each season, replacing the probability model above. | DESIGNED | `ci_political_v30.md:321` |
| Fail Forward complications | process | Every Domain Action gains a mandatory failure complication and a player-chosen minor complication on Partial. | PROPOSED | `fail_forward_pp177.md:17` |
| Historical governance-mode catalogue | mechanic | ~40 grounded proposals — sequential-veto chambers, sortition-plus-scrutiny, mask-vs-substance governance modes, two-signal deposition, recognition-fission, regency interregnum, coercion-vs-capital Muster asymmetry, the Sforza Gambit. All ED-IN-0064-provenanced; none authored into canon. | PROPOSED | `research/governance/*.md`, `research/fa_se_historical_precedent_research_v1.md` |

## Processes

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| `faction_take_action` | process | The season loop's faction step: signals → re-weight → one draw → dispatch through four **non-`elif`** buckets. A bucket returning the `'invalid'` sentinel falls through to the terminal unconditional `_try_govern`, whose return the caller discards. | BUILT | `faction_action.py:208-273`; `engine/mc_v18.py:130-145` |
| Emergency Council | process | The one executing intra-faction two-sided contest, fired by the Stability Crisis trigger. Both sides are derived from the *same* faction's aggregate stats — `side_a = max(1, round(L))`, `side_b = max(1, round(7 − Sta))` — both run the identical default policy, and the echo returns to the faction it came from. | BUILT | `engine/cross_scale/scene_dispatch.py:120-139` |
| `run_accounting` | process | CI, MS year-end decay, insurgency triggers and promotions, NPC ecology, an accord drift probe. **No faction step at all** — no Mandate aggregation, no Treasury accrual, no upkeep, no Stability check. | BUILT | `systems/overview/sim/accounting.py:96-143` |

---

---

### FLATTEN — "parliament-politics"

*This is a sub-cluster of faction-strategy, not a separate system, and the most interesting fact about it is structural: there is no `systems/parliament/`, no `Parliament` class anywhere in `engine/` or `systems/`, no seat, no roster, no agenda, no session, no clock. The vote resolves directly on `Faction.L` and `Faction.Sta` and writes back to `world.factions`. Parliament has no state of its own. Fourteen real things, not twenty-five — the count is honest, not padded.*

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| Parliament (the entity) | primitive | Does not exist. Membership is the `Faction.parliamentary` boolean; there is nothing else. | — | absent (`grep` for `class Parliament` returns nothing) |
| `Faction.parliamentary` | primitive | One boolean. It is the entire franchise model, and it enforces GD-3 at both proposal and ballot. | BUILT | `game_state.py:111`; `parliamentary_vote.py:139-144` |
| Persuasion Track | primitive | The vote's only state: an integer 1-10 starting at 5, existing for the duration of one call. | BUILT | `parliamentary_vote.py:130,161-205` |
| The §10 vote resolver | mechanic | Per-side pool = **sum of `int(L)`** across declaring factions, +1D genre match, +1D audience match; roll TN 7; each side moves `max(0, net − resistance)`; track ≥7 passes, ≤3 fails, else committee. | BUILT | `parliamentary_vote.py:165-205` |
| Abstainer resistance | formula | +1 per abstaining faction at `Sta ≥ 6`, capped +2. This is the only way a non-declaring faction affects a vote. | BUILT | `parliamentary_vote.py:154-159` |
| Total Victory rider | formula | Track ≥9 or ≤1 strips `L −1` (20 granular) from the losing coalition's highest-Legitimacy faction. | BUILT | `parliamentary_vote.py:207-219` |
| The permanent "one-season" penalty | gap | That rider's own note reads *"[one-season penalty; temporary-modifier restoration deferred to season_manager]"*. `season_manager` defines two functions and has no temporary-modifier facility. The penalty is permanent and compounds. | BUILT (defect) | `parliamentary_vote.py:216-218` |
| Parliamentary Censure | mechanic | Proposer self-gates on GD-3 plus `L ≥ 2`; target chosen as highest-`L` rival; two voices declared, everyone else abstains; on pass, target takes `Sta −1` and `L −1`. Reached every campaign as the universal fallback in the faction-unique slot. | BUILT | `parliamentary_action.py:97-160`; `faction_action.py:295-299` |
| Censure stacking | formula | On a Total Victory pass the §10 rider and the §5.4 effect compose to **−2 Mandate** on the target. The module flags this as an unratified emergent composition, not a design decision. | BUILT | `parliamentary_action.py:154-160` (its own SEED/NEEDS-JORDAN note) |
| Sanction ladder — Censure tier | formula | Proposer Mandate 2; Majority; target `Sta −1`, `L −1`; no proposer cost; one-time. | BUILT | `faction_layer_v30.md:457` |
| Sanction ladder — Embargo / Blockade / Combined / Outlawry | formula | Four ascending tiers with proposer minimums 3/3+Mil3/both/5, per-season durations, rescission bars, and Outlawry's CB-to-all rider. **Prose only** — the module's own TODO names all four as unbuilt. | DESIGNED | `faction_layer_v30.md:458-461`; `parliamentary_action.py:163-172` |
| Constructive motions | mechanic | Subsidy, War Authorisation, Treaty Ratification, Recognition Challenge, Succession Endorsement — genuinely distinct actions, explicitly *not* part of the Sanction parameterisation. None built; two have durable outcomes with no state field to land in. | DESIGNED | `faction_layer_v30.md:462-468` |
| Parliamentary Territory Transfer | mechanic | `Pool = max(0, I + vote_mod[−1,0,+1])`; `Ob = holder.L + 2`; four narrative modes; 1/arc/faction via `parl_transfer_used_this_arc`; last-territory and self-transfer guards. Partial grants a retry CB. | BUILT | `parliamentary_transfer.py:248-386` |
| Casus Belli gate | mechanic | Eight canonized CB sources gate the four Transfer modes. Only `crown_constitutional_restoration` is ever populated, and it maps to `adversarial` alone — so in a fresh campaign the other three modes and seven sources are unreachable. Two "canonical" enumerations of the eight disagree on five names. | INERT | `parliamentary_transfer.py:76-121`; `faction_systems_overview_v30.md:175-186` |
| Parliamentary bridge | process | Runs every season by default: lowest-Stability eligible faction proposes on Projection, highest-Mandate defends on Memory, `motion_id = f"parl_s{season}"`. Derives *who*, never *what* — the identical contentless motion fires every season. | BUILT | `engine/cross_scale/parliamentary_bridge.py:88-107`; `engine/mc_v18.py:152-158` |
| Motion of No Confidence | mechanic | Two-step Crown deposal: Influence vs Crown Mandate, then Holy See concurrence, giving the Church a structural veto over Crown regime change. Zero code. | DESIGNED | `systems/world/worldbuilding_v30.md:179` |
| CI institutional weight | formula | Church vote contribution `Mandate + floor(CI/20)`; a faction voting against Church contributes `max(0, Mandate − floor(CI/30))`. | DESIGNED | `faction_layer_v30.md:450` |
| "Sanction" naming collision | gap | The collision database prescribes renaming the Authority pressure point to "Sanction" — which collides head-on with the live five-tier Parliamentary Sanction ladder. A vocabulary fix that manufactures a second collision. | — | `references/name_collision_database.yaml:421-425` |

---

---

### FLATTEN — "economy-accounting"

*This system has fewer real things than the target range, and the shortfall is the finding. Twenty-one of its twenty-four records are historical-precedent proposals — Ottoman iltizam, Roman publicani, the Ferme Générale, John Law, the Salt Certificate, Encabezamiento — grounded, well-argued, and attached to nothing. The live accounting cascade is three rows.*

| thing | slice | what it does | status | where it lives |
|---|---|---|---|---|
| `Faction.W` (Wealth) | primitive | The only economic state a faction has. Registry-clamped 0-7. | BUILT | `game_state.py:114` |
| Treasury | derivative | `Treasury = Wealth × 100`. Agreed by three surfaces; **the field does not exist**. The gap is a missing field, not a design disagreement. | DESIGNED | `derived_stats_v30.md:298`; `descriptor_registry.yaml:192` |
| Wealth write sites | formula | Four in the entire engine, **all of them costs**: Muster up-front, Royal Progress −2, Great Work −3, Coronation Renewal −2. There is no income anywhere. Wealth is monotonically non-increasing across a campaign. | BUILT | `faction_action.py:546`; `crown_initiative.py:91,161,246` |
| Muster's cost, at scale | formula | `adjust('W', −1)` → `−1 / MULTS['W'](100)` = **−0.01 Wealth**, while the three Crown sites multiply by 100 first and charge full points. 100 musters cost 1 Wealth. Verified by execution. | BUILT (defect) | `faction_action.py:77,546` vs `crown_initiative.py:91` |
| Muster's Wealth-to-pool conversion | formula | `pool = Mil + floor(W/2)` — the one place Wealth buys anything. | BUILT | `faction_action.py:549` |
| `run_accounting` | process | CI seasonal calculation, MS year-end decay, insurgency triggers, insurgency promotions, NPC ecology, an accord-drift probe. **No Treasury accrual, no Mandate aggregation, no upkeep, no income, no Stability check.** The module's own banner says so. | BUILT | `systems/overview/sim/accounting.py:96-143` |
| Accord drift probe | process | Report-only telemetry comparing `registry.province_accord` against `Territory.accord`, measuring two uncoordinated write models for provincial Accord without reconciling them. | BUILT | `accounting.py:54-95` |
| Settlement AP | derivative | `AP = 2 + facility_tier`, +1 at a Seat or Cathedral. The only live seasonal-budget primitive in the tree, and the anchor several proposals resolve against. | BUILT | `systems/settlements/sim/registry.py:94-96` |
| Fiscal Stance | mechanic | Per-faction/province {Light, Standard, Extraction} with `yield = Prosperity × k × rate_mult × compliance(L)`, `compliance(L) = 0.5 + L/14`. Extraction trades 1.5× for `PS −1`/season. Proposed, no ratification; no per-settlement tax model exists to consume it. | PROPOSED | `faction_layer_v30.md:546` |
| Capital-Posture ledger family | primitive | One tag family (`:Speculative`, `:Debased`) that nine of ten fiscal proposals independently reference. `ledger.py`'s `TAG_KINDS` is a **closed five-member enum** whose fifth member is Leverage, not Compact — so multiple proposals were adjudicated against a family that does not exist. | PROPOSED | `historical_concerns_action_catalogue_v1.md:288` |
| Levy:Debase + Recoinage | mechanic | A one-way debasement ratchet plus its only exit, priced to grow costlier the longer it is deferred. | PROPOSED | `historical_concerns_action_catalogue_v1.md:288,290` |
| Farm the Revenues | mechanic | Immediate `W +2` against a 4-season term of ×0.75 yield and `PS −1`/season, spawning a named "Farmer" NPC as a leverage surface. Roman publicani / iltizam / Ferme Générale. | PROPOSED | `fa_se_historical_precedent_research_v1.md:204` |
| Gauge-Indexed Levy | mechanic | The one Levy method-fork that makes extraction auto-responsive to a tracked environmental stat without a per-season roll (the Nilometer model). The other three forks are timing parameters, not verbs. | PROPOSED | `historical_concerns_action_catalogue_v1.md:292` |
| Embargo as a Directive | mechanic | The one genuinely new Directive *shape*: every other Directive targets the settlement it is issued to; Embargo targets a rival **through** the issuing governor's own trade. Comply/Defy reads as "how much of my trade do I sacrifice for someone else's grudge." | PROPOSED | `historical_concerns_action_catalogue_v1.md:302` |
| Guild Withdrawal of Trade | mechanic | Guild-only private embargo — target's Port/City/Mine settlements take −50% Prosperity growth, costing the Guilds only exposure. Grounds the unbuilt "Economic Leverage" line. | PROPOSED | `fa_se_historical_precedent_research_v1.md:236` |
| Protected Tributary | mechanic | A second Tributary treaty row: `W −1/yr` and `W +1/yr` trade access (net zero) plus casus foederis, at zero Stability cost — a stable subordination equilibrium against the existing extortion spiral. | PROPOSED | `fa_se_historical_precedent_research_v1.md:230` |
| Encabezamiento / Salt Certificate / State Arsenal / Borrow | mechanic | Four fiscal proposals adjudicated against the phantom Compact tag family; the first was rated "ratify as-is" and must not be, until the tag schema is settled. | PROPOSED | `audit/2026-07-12-governance-compendium/_workings_joined.md:1782,2065,2471,2590` |
| Fiscal cascade chains (THR-01 · 03 · 07 · 09 · 10 · 12) | process | Six authored multi-step chains — debasement→famine→coup, siltation→merchant exodus→ladder capture, fixed quota→drought→outlawry — each naming the un-pulled lever that would have broken it. Not vetted against the live card corpus; every lever they name is unbuilt. | PROPOSED | `_workings_joined.md:1267-1517` |

---

---

### FLATTEN — "settlement-governance"

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

---

### FLATTEN — "territory-world"

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