# §3 FLATTEN — "faction-strategy"

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

# §4 WITHIN-SYSTEM ANALYSIS — "faction-strategy"

### What playing this system is actually like right now

Each season, four factions each take exactly one action. The choice is one dice throw against a re-weighted probability vector: roughly a third of the time the faction reaches for its unique action, a third for conquest, a fifth for muster, the rest govern. The signals that bend those odds are real and legible — a faction with an adjacent weaker neighbour becomes more likely to attack, one with ungoverned territory more likely to govern — but they bend probabilities only. Nothing is ever *decided*. A faction with an obvious conquest opportunity may spend the season mustering; the docstrings in three separate modules claim a "mandatory threat-response before stochastic selection" that the code does not implement.

Two of the four factions have interior lives. Crown picks between three initiative modes; Church runs a fixed three-step priority chain. Hafenmark and Varfell have no branch: they fall straight through to the universal Parliamentary Censure fallback, and their six stub modules are typed no-ops. Rename them in the starting table and nothing changes.

What the player would feel, if there were a player: a slow drift in five numbers. Wealth only ever goes down — its four write sites in the whole engine are all costs, and one of them (Muster) is scaled wrong and charges a hundredth of a point. Legitimacy oscillates as votes and censures land on it. Territories change hands. Nobody remembers anything. A faction that censured you last season has no record of it, and will pick the same target next season by the same arithmetic, because targeting reads the highest-Legitimacy rival and nothing else.

### The load-bearing conflicts

**1. `Faction.L` is doing two jobs, and one of them is ratified out of existence.** The code writes and reads `L` as Mandate at every site. LPS-1 ratifies Mandate as a *derived* aggregate over per-settlement Legitimacy and Popular Support, neither of which exists in code, and a 2026-08-23 ruling makes `fac.legitimacy` a declared *base* descriptor — a different quantity. This does not resolve on faction-lane work: it blocks on the settlement layer. Jordan's call, and it is upstream of most of this table.

**2. Faction stats have no setter — except at all 31 sites where they do.** `propagation_spec_v1 §IV.2`, ratified, says every write terminates at a settlement/territory cell or a Key-log entry. The engine writes `adjust()` directly everywhere. Deciding this decides whether faction actions are *causes* or *readouts*, which changes what the strategic layer is. The code has already voted; the ruling has not been withdrawn.

**3. The canon §9 unique-action table describes a game that was never built.** Royal Decree, Sovereign Authority Doctrine, The Private Collection, Economic Leverage — none exist under those names or formulas. Under §0.05 the code wins, which means half the table is not "unimplemented" but *retracted*, and someone has to say so before another session builds toward it.

**4. Two action economies, neither superseding the other.** `ci_political_v30 §5`'s card-hand-plus-cooldown model and `faction_action.py`'s single weighted draw are categorically different architectures. Neither document mentions the other. The AI threat-priority posture stack is a third.

**5. `Faction.standing` is two things with one name.** The bare int in the dataclass and the designed 0-7 officer ladder share nothing but a word. The int also escapes the registry clamps at every one of its eleven write sites and feeds pools that write it back. Code-resolvable: a one-line clamp, plus a rename.

### What this system needs from others

It reads **settlement-governance** hardest and gets nothing back: `Settlement.legitimacy` and `popular_support` are declared and inert, so LPS-1 Mandate, the compliance-scaled tax yield, the Faction Emergence stage gates and the settlement-drift feedback all sit on absent substrate. The settlement layer must be built before the faction Mandate question is even askable.

It reads **territory-world** for `Territory.accord`, `pt` and `owner`, and writes all three — with two uncoordinated write models for provincial Accord that `accounting.py` measures and refuses to reconcile.

It reads **resolution-kernel** correctly and more than anyone else: sixteen of eighteen files in `systems/factions/sim/` import `engine.*`, and all seven obstacle-bearing production rolls in the tree live here. This is the one lane using the dice owner as intended.

It reaches **mass-battle-seam** through `resolve_mass_battle` for conquest, and needs an officer/garrison model that neither side owns.

It needs **personnel-roster** for everything interesting it has designed — succession, the Standing ladder, officer demotion, Duties, Hostage-Kin — and personnel-roster does not exist. `Faction` has no leader field, so the succession resolver in `contest/faction.py` is unreachable by construction.

From **npc-social** it needs the thing `parliamentary_action.py:68-69` says in its own comment is missing: *"No grudge / hostility / inter-faction-relationship stat exists in game_state.Faction."* That single sentence is the honest summary of this system. **A faction in this game currently has no memory, no relationships, and no people.** Its personality is a string comparison; its enmity is recomputed from scratch each season as "whoever has the highest Legitimacy"; its history is a stat delta with no provenance.

### The cheapest thing that would make this system playable

**Give `Faction` one field: a `grudge` dict keyed by faction name, written by the outcomes that already fire.** Censure passing, Excommunication landing, a conquest taking a territory, a transfer succeeding — all four already run every campaign and already know both parties. Have each add to the target's counter against the actor and decay it slowly.

Then change one function. `select_censure_target` is currently a documented placeholder that picks the highest-Legitimacy rival *because no relationship signal exists*; its own docstring says so. Point it at `grudge` instead. Do the same for `select_excommunication_target`.

That is one dataclass field, four one-line writes at sites that already fire, and two changed sort keys — and it converts every faction action from an isolated dice throw into a move in an ongoing quarrel. A faction that censured you comes back for you. A faction you conquered from turns on you. The strategic layer starts having a *plot* rather than a drift, and it does it without a new subsystem, a new resolver, or the settlement layer.

---

# §3 FLATTEN — "parliament-politics"

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

# §4 WITHIN-SYSTEM ANALYSIS — "parliament-politics"

### What playing this system is actually like right now

There is no chamber. Every season the engine finds the lowest-Stability faction with territory, finds the highest-Legitimacy other one, and puts them on opposite sides of a motion with no subject — `motion_id = "parl_s7"`, genre pair fixed, no text, no object, no consequence beyond the roll. Each side's dice pool is the sum of its Legitimacy. Both roll. The difference moves a track from 5. If the track lands at 7 or above the motion passes; at 9 or above someone loses a permanent point of Legitimacy that the code believes it is lending for one season.

The only *authored* motion in the game is Censure, and it arrives sideways: a faction whose unique-action slot comes up empty proposes one, always against whoever is currently strongest, always with exactly two voices declared and everyone else abstaining. There is no debate, no amendment, no whipping, no order of business, no vote to schedule the vote. The one lever an uninvolved faction has is to be stable enough (`Sta ≥ 6`) that its silence counts as resistance.

A player would experience Parliament as weather. It fires every season, it costs nothing, it cannot be entered, joined, blocked, delayed or spoken in, and the only thing it produces is a slow bleed on whoever is winning. Ironically that bleed is the strongest negative-feedback loop in the strategic layer — it is genuinely doing balance work — but it does it invisibly and by accident.

### The load-bearing conflicts

**1. Parliament has no state, and everything designed for it needs state.** Five ongoing Sanction statuses, two durable constructive-motion outcomes, seat tenure, agenda, session slots, a Recognition Challenge's persistent −1 TCV — none has a field anywhere, in Parliament or in `victory`'s own state block. Every design in this cluster is blocked on the same missing object. Decidable by architecture: either Parliament becomes an entity or the ladder stops.

**2. The "one-season" Mandate penalty is permanent.** The comment says one thing, `season_manager` provides no mechanism for it, and the penalty compounds across a fifty-season campaign against whichever faction keeps leading. This is a code fix, not a ruling — but which way it is fixed (restore the point, or ratify permanence) changes the balance profile of the whole layer, because this is currently the game's main anti-runaway force.

**3. Censure composes to −2 and nobody decided that.** The module flags it honestly: the §10 rider and the §5.4 effect stack, the golden pins the *current* composition rather than an intent. Jordan's, and small.

**4. Only Censure exists, so the severity dial has one setting.** ED-FA-0006 established that the five punitive tiers are one parameterised action differing in {proposer min, vote bar, magnitude, duration} plus two riders. Three of those four parameters need machinery the vote resolver lacks: a Supermajority bar, per-season recurring effects, and a rescission path. Building the parameterisation *is* building that machinery.

**5. Score/2 obstacle derivation is suspended, not unexecuted.** Three built sites disagree: `coronation_renewal_ob` halves exactly, `tribunal.py` halves conditionally, `parliamentary_transfer.py` uses full score +2. A test pins all three because Jordan explicitly suspended reconciliation. Do not touch this.

### What this system needs from others

Almost nothing, which is why it runs. It reads `Faction.L`, `Faction.Sta` and `Faction.parliamentary` from **faction-strategy** and writes `L` and `Sta` back. It borrows the Persuasion Track thresholds from **social-contest**'s `contest` module as shared constants — the one real seam, and a clean one. It reads `world.season` for the motion id and `world.clocks['CI']` for the (unbuilt) Church weighting. Transfer additionally reads and writes `Territory.owner` and `Territory.accord` in **territory-world**, and reads the `world.casus_belli` ledger that nothing writes.

What it *would* need is sharper. A real Parliament needs **personnel-roster** — seats are held by people, and the corpus has authored seat tenure, court attendance, recognition forks and 74 ladder rungs against a roster that does not exist. It needs **settlement-governance** for the political-value computation that would make seat weight mean something other than raw Legitimacy. And it needs a topic source: a motion needs identity, a raising condition and a retirement rule, which means reading the world for grievances — which means the grudge state faction-strategy also needs. The two clusters want the same missing primitive.

### The cheapest thing that would make this system playable

**Give the motion a subject by re-pointing Censure's target selection and the bridge's topic derivation at the same source.** Concretely: `_derive_vote` currently picks a proposer and a defender and stops. Have it also pick the *territory or action* the proposer is aggrieved about — it already has `world.territories` and the faction that lost one last season — and put that in the motion id and the result string.

The vote's arithmetic does not change at all. What changes is that the season log stops reading `parl_s7: Crown loses 1 Mandate` and starts reading `Motion on the seizure of Feldmark: Crown loses 1 Mandate`. The same roll becomes a legible event with a cause, and the identical-contest-forever problem — a low-Stability faction replaying the same motion before the same bench until the campaign ends — dissolves, because the subject changes even when the parties do not.

That is one function, no new state, and it is a precondition for every richer thing here: a motion you can name is a motion a Sanction tier can be aimed at, a player can lobby on, and a Recognition Challenge can attach to.

---

# §3 FLATTEN — "economy-accounting"

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

# §4 WITHIN-SYSTEM ANALYSIS — "economy-accounting"

### What playing this system is actually like right now

There is no economy. `Faction.W` is a number between 0 and 7 that four code sites decrement and nothing ever increments. A faction begins with 4 or 5 Wealth and, over fifty seasons, spends it down — except that the drain is negligible, because the one action that would drain it most often, Muster, charges a hundredth of a point per attempt while the three Crown initiatives charge full points. So in practice Wealth is a near-constant, and its only mechanical job is to add `floor(W/2)` dice to a Muster pool.

`run_accounting` runs every season and touches nothing fiscal. It advances the Church Influence clock, decays a world track once a year, checks whether an insurgency emerged, drifts some NPC stances, and measures an Accord divergence it is forbidden to fix. Its own module banner states plainly that it has no Mandate aggregation and no Treasury accrual step.

So a player would not experience an economy at all. There is no income to allocate, no upkeep to meet, no bankruptcy, no budget, and no season in which money is the constraint. Treasury — agreed by three separate surfaces as `Wealth × 100` — is not a field. The one live seasonal-budget primitive anywhere in the tree is settlement Administration Points, `AP = 2 + facility_tier`, and it belongs to a different system.

Meanwhile the corpus holds twenty-one deeply-researched fiscal mechanics: tax farming with a named farmer NPC who becomes a political actor, debasement ratchets with exactly one priced exit, environment-indexed levies, private guild embargoes, negotiated quota locks. All of them are excellent, all of them are prose, and several were adjudicated against a ledger tag family that turned out not to exist in code.

### The load-bearing conflicts

**1. Wealth has no source.** This is not a design disagreement; it is an absence that makes every fiscal proposal unbuildable, because they all move a quantity that never accrues. Decided by architecture, and it is the first move.

**2. Muster's cost is off by 100×.** `faction_action.py` passes an unscaled granular delta; its three sibling cost sites multiply by `MULTS['W']` first. Either the canonical "Wealth −1" means one point (and Muster is wrong) or Muster's constant is already granular (and the constant is misnamed and mis-commented, since its citation is ED-FA-0009's full-point cost). Code-resolvable, one line, but it moves the Muster/Conquest balance materially, so it needs a seeded control run and not a blind fix.

**3. `TAG_KINDS` is a closed five-member enum and at least six proposals assume an open sixth.** The shipped fifth member is Leverage; the proposals presume Compact. Encabezamiento was rated clean and "ratify as-is" on that false premise. Until the Compact-vs-Leverage question is settled, HRE-5, VEN-SE-2, VEN-SE-3, CHN-4, HRE-4 and HAB-5 cannot be safely authored. One ruling unblocks six items — the highest-leverage single decision in this system.

**4. Treasury is a missing field, not an open question.** Three surfaces already agree on the formula. It should not be on a ruling docket; it should be on a build list.

**5. The Capital-Posture consolidation is the right shape and nobody has taken it.** Nine of ten fiscal proposals independently reference the same tag family. Authoring it once turns nine separate mechanics into nine variants of one, which is exactly the primitive-first posture the rest of the tree asks for.

### What this system needs from others

From **faction-strategy**: `Faction.W` and the four sites that spend it, plus a Treasury field it does not have. Every yield formula in the proposal corpus terminates in a faction-scale accumulator that does not exist.

From **settlement-governance**, and this is the hard dependency: `Prosperity`, per-settlement `Legitimacy`, and `Settlement.ap`. The Fiscal Stance formula is `Prosperity × k × rate_mult × compliance(L)`, and both `Prosperity` and `L` are settlement-grain. Compliance-scaled taxation is the single most-referenced fiscal idea in the corpus and it is entirely downstream of the settlement layer being built. Until then no yield can be computed and no extraction rate means anything.

From **cross-scale-plumbing**: the `ledger.py` `TAG_KINDS` enum, which owns whether a durable fiscal claim can be represented at all, and the Directive Comply/Bargain/Defy pipeline, which is the resolution shape every proposed fiscal verb wants to reuse rather than reinvent.

From **territory-world**: `Territory.accord` and `pt`, and a resolution of the two uncoordinated provincial-Accord write models that `accounting.py` currently only measures.

### The cheapest thing that would make this system playable

**Add one line to `run_accounting`: seasonal Wealth income proportional to territories held.**

Not Treasury, not compliance, not Prosperity — those need the settlement layer. Just `faction.adjust('W', k * len(faction.territories) * MULTS['W'])` at the top of the accounting pass, with `k` tuned so a mid-size holding roughly covers one Royal Progress per two seasons.

This is the smallest change in this entire document and it does the most, because it closes the only open circuit in the strategic economy. Wealth stops being a slowly-draining battery and becomes a *flow*, which means holding territory pays, which means conquest and Govern have an economic return and not just a Legitimacy one, which means Muster's cost is finally a real trade-off against something. It makes losing territory hurt twice — once in victory scoring, once in the treasury — and it gives every one of the twenty-one authored fiscal mechanics a quantity to actually modulate.

It also makes the Muster scaling defect *visible*, because for the first time there will be a budget for it to fail to consume. Fix the income first; the defect surfaces itself.