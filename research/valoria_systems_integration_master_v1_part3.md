# Valoria Systems Integration Master — Part 3: Within-System Analysis

## Status: PROPOSED (2026-08-28)
## Version: v1.0
## Reads: Parts 1–2 (collation, slices, flatten)

**Reading order:** [Part 1 · Collation and Slices](valoria_systems_integration_master_v1.md) → [Part 2 · Flatten, the Personal Half](valoria_systems_integration_master_v1_part2.md) → [Part 3 · Within-System Analysis](valoria_systems_integration_master_v1_part3.md) → [Part 4 · Cross-Category Comparison and Proposals](valoria_systems_integration_master_v1_part4.md)


Deliverable §4. For each system, in order: **what playing it is actually like right now** ·
**the load-bearing conflicts**, each with a note on *what decides it* (the code · a ruling that has
already been made and not executed · a genuine Jordan call) · **what this system needs from others** ·
**the cheapest change that would make it playable.**

The last of those four is the one to read if you read only one thing. Eight independent lanes were
asked for it without being told what the others said, and §5 in `_part4` shows what they converged on.

### WITHIN-SYSTEM ANALYSIS — "faction-strategy"

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

---

### WITHIN-SYSTEM ANALYSIS — "parliament-politics"

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

---

### WITHIN-SYSTEM ANALYSIS — "economy-accounting"

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

---

### WITHIN-SYSTEM ANALYSIS — "settlement-governance"

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

---

### WITHIN-SYSTEM ANALYSIS — "territory-world"

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

---

### WITHIN-SYSTEM ANALYSIS — "People"

### What playing this system is actually like right now

Nothing. Not "thin" — **empty**. In every seeded campaign, `world.npcs` is an empty dictionary, and the population of Valoria is zero people. There is no one to meet, no one to recruit, no one to betray you, no one whose opinion of you is stored anywhere. The forty-six authored characters — Edeyja, Baralta, Konrad Ems, Hedda Vorn, the whole cast, each with convictions, arc trajectories, secrets and historical parallels — exist as a YAML file with no reader. Deleting that file would change nothing the engine does.

One NPC mechanic runs every season: pairwise stance convergence, which walks `world.npcs` looking for same-territory pairs who share a conviction and disagree by exactly one step, and nudges them toward each other. It runs, correctly, over an empty dict, and the caller throws away what it returns. That is the whole of the personal layer's live behaviour.

The strange part is how much of the machinery is *finished*. `generate_npc` is a complete two-tier generator: it reads a territory's ecology, biases the new person 60% toward the controlling faction, then rolls a d6 and flips one axis to the opposite extreme so that populations are not uniform. It has no call site. `apply_conviction_scar` correctly implements the per-conviction crisis ladder that PP-718 ratified. Its only caller is itself unreachable. `succeed_governor` correctly replaces a governor and writes a durable ledger row. Zero callers. `npc_ai.py`, the module named for NPC decision-making, contains two typed no-ops that nothing calls, and its docstring declares a dependency pointing the wrong way.

So the felt experience of this system is a strategic layer where factions fight, settlements tick and battles resolve, and no human being is present at any point. The game currently resolves a war between four spreadsheets.

### The load-bearing conflicts

**1. Identity is authored; capability is not — and the two halves do not fit together.** The registry gives `role`, `faction` and `convictions` on 46 of 46 characters, and `stats` on 1 of 46 (whose `social` value is the string `"3–4"`, not an integer). The runtime `NPC` dataclass wants stance, worldview, affiliation, compromise and volatility. **The two field sets share exactly two names — `faction` and `territory` — and those are the two with the worst data.** 20 distinct faction strings map to 4 factions in code; 7 of 46 carry a territory, written `"T15 (Southernmost)"` against a live map keyed on bare `T1`…`T15`, `T17`, and one names `T16`, which is not in the map at all. Two more entries are silently truncated by an unquoted `#` in the YAML. This is not "a loader is missing." **The destination type does not exist yet.** What decides it is a design call — is a character a bundle of five behavioural axes, or a named person with a role and a history? — and until that is answered, no loader can be written, only guessed at.

**2. "Officer," "governor," and "companion" are three roles that legitimately compose on one person, and only one document says so.** Mass battle owns "officer" (auto-generated unit commander, the `officer_deaths` key type). Settlements own "governor." Personal scale owns "companion." The rise-to-power research reaches for "officer" for the *political rank* concept in about 20 of its 96 catalogued cases and must not — its own proposed resolution is to name that system **Ascendancy** and its role-holders Retainer / Patron / Advisor / Conduit / Favorite / Gatekeeper. `companion_specification_v30.md:22` is the one place in the corpus that names the collision explicitly instead of pattern-matching it away, and it is right: the same NPC can be your travelling companion, your faction's recruited asset, and the governor of a settlement, and each of those has its own eligibility, tracking and loss consequence. This is decided by Jordan or by whoever writes the roster canon — but it must be decided *before* the person object is typed, because it determines whether "role" is one field or three.

**3. A design document saying BUILT is not a mechanism, and this system contains the corpus's clearest case.** `npc_relational_graph_v30.md` §7 and §8 carry the header "BUILT 2026-06-09, ED-1000" for the Defection Cascade and its faction integration. There is no code. In that document's vocabulary "BUILT" meant *a design decision was finalised* — a defensible internal usage that reads, to anyone else, as a claim about the engine. The same document's own later section calls parts of §7 "hook only, full mechanics deferred." Decided by the code: there is none, and the six authored edge types have no data file either.

**4. Renown, Standing and Caste are load-bearing in canon and absent from the runtime.** Renown gates pool sizing, Disposition floors and faction emergence, and has no key type, no owned-state row and no contract module. Caste gates advancement across twelve ladders and is absent even from the registry's own required/optional field list — you cannot *author* a character's caste, let alone read it. These are not partially built; they are entirely uncommitted, and each is a ruling away from being either a first-class primitive or dropped.

**5. Weighted convictions have nowhere to land.** The taxonomy ruling settled the roster at thirteen and gave it a single owner — that part is genuinely fixed, and an unknown conviction name now raises loudly instead of scoring zero silently. But canon's structured-concentration model says convictions are *weighted*, the registry carries 81 weighted primaries, and `ConvictionState` stores scars, crisis flags and a log with no weight field anywhere. Decided by the code: add the field, or accept that authored weight is flavour text.

### What this system needs from others

It reads more than it writes, and almost all of what it reads is owned elsewhere and half-built.

From **territory-world**: the territory key space. `world.npcs` is territory-keyed and the live map has 16 bare `T*` keys with no `T16`. Any person placement is blocked on reconciling that against the registry's seven parenthesised strings. From **settlement-governance**: a settlement-grain home. `Settlement.npc_ids` exists and has no writer, and because the registry's only locational field is per-territory while territories hold one to three settlements, *which settlement* a person is in is a separate unanswered question from *which territory*. From **faction-strategy**: the faction identity space (4 in code, 20 strings authored) and the Mandate stat that recruitment debits. From the **resolution kernel**: obstacles. Every People mechanic that rolls — recruitment Approach, the Prince-in-Waiting maintenance check, Knot-mediated extraction — derives its Ob from a person's score, and the score/2 derivation has no single owner. From **cross-scale-plumbing**: the Key substrate is the only mechanism by which a person's history would ever become queryable — `Key.causes[]` is the chain, and Valoria has the chain and not the individual.

Writing outward, it owes: `Settlement.governor_id` and `npc_ids` to settlements; Standing changes and affiliation transitions to factions (neither has a mutator or a key type); and the sub-scale `targets[]` population that four emitter families — domain actions, faction politics, peninsular strain, scenario authoring — already declare `npc_behavior` as a consumer of and never fill in.

Ordering: **territory key reconciliation and the faction-string map must land before any person can be placed at all.** Everything else can follow.

### The cheapest thing that would make this system playable

Load the forty-six authored characters into `world.npcs` at world-gen — but **give the NPC layer its own RNG substream first, and treat that as the actual prerequisite.**

The loader is the obvious move and it is the right one: `world.convictions`, `world.beliefs`, `world.knots`, `world.npcs` and `Settlement.npc_ids` are all already declared, routed and serialised, so one loader would put occupants into several stores that are already ticking. `registry.py::populate_from_geography` is the in-tree pattern to copy — deterministic, no RNG draw, every field mapping cited, illegal values raised.

What the controlled experiment showed is that the analogy does not carry. Loading two NPC objects directly into `world.npcs` left all three population guards green — because every one of them observes `world.npc_counter`, which only `generate_npc` increments, and a loader constructing `NPC` objects directly never touches it — and **moved the seed-42 campaign winner from Crown to Hafenmark.** The channel is `simulate_npc_actions`: it draws `world.rng`, the shared campaign stream, once per qualifying same-territory pair per season. Zero people, zero draws. Two people, up to one draw a season. Every downstream consumer — faction actions, battles, settlement events — re-phases behind it. Neutering the drift function reproduced the unmodified baseline byte-exact, which isolates the cause.

So `populate_from_geography` is golden-safe only because settlements have no per-season RNG-drawing consumer. `world.npcs` has one. The sequencing that follows: **derive a dedicated `random.Random` for the NPE from the campaign seed, so that population size cannot re-phase anything else, and land that on its own — a change with no behavioural delta and a golden that proves it.** Then the loader is a real single-variable experiment, its golden movement is attributable, and the three guards should be re-pointed at `world.npcs` rather than the counter, since as written they cannot see the very change they exist to catch.

---

---

### WITHIN-SYSTEM ANALYSIS — "Cross-Scale Plumbing"

### What playing this system is actually like right now

The pipes are real, the water is not. Valoria has a genuinely good event substrate: every consequential event is a typed, validated, append-only `Key`; save state is initial conditions plus the log; the deferred-apply channel lets a Key be logged live and cause-linked at emission while its state write lands at the accounting boundary, so same-tick causal chaining survives. That is a better foundation than most games this size have.

What actually flows through it, per campaign, is five Key types out of fifty-five declared, from four call sites. Three of those write state. Thirteen callbacks are subscribed on the bus and every one is a typed no-op. Eleven of the thirteen subscribed types are never emitted by anyone; of the five emitted, two are subscribed, and `scene.contest_resolved` — one of the three that changes the world — is subscribed by nobody. Subscription and emission were wired independently and barely overlap.

The player-facing consequence: **scale transitions are almost entirely one-directional and mostly absent.** Eight handoffs are specified and one is reachable, via a dispatch dict with two entries that both point at the same pair. Eight mandatory zoom-in triggers are specified and one — Stability Crisis — can be evaluated; it fires an emergency council debate in which both sides of the argument are derived from the *same faction's own aggregate stats*, one side scoring `round(L)` and the other `round(7 − Sta)`. So the single working personal↔strategic crossing in the game is a faction arguing with itself, and it works precisely because it needs no person in the room.

Faction→Personal is worse: the bridge builds a combat actor from one rounded integer, is behind a default-off flag, and has no producer that would queue the scene even with the flag on. Personal→Settlement is the most painful, because it is *finished*: `scene.accord_echo` is the one fully closed Key-driven state-write loop in the engine — scene resolves, Key emitted with honest `causes[]`, `stat_deltas` applied at the boundary, `Settlement.order` written — and it never fires, because nothing in the campaign loop declares `echo['scene_outcome']`, and the classifier correctly refuses to guess one from the scene type.

Keys flow **out** and essentially never **in**. Across fifteen traced subsystem flow skeletons, Key-typed inputs were 7 of 165, and six of those seven were substrate self-construction or a callback receiving its own emission. Subsystems are shaped by caller arguments and direct world-state reads. That is why nothing loops: events are emitted and never read back into the things they happened to.

### The load-bearing conflicts

**1. The Key is the wrong shape for half of what the game tracks — and this is the deepest one.** A Key is a typed, targeted, one-shot emission. That is exactly right for a flag: a coup attempted, a standing changed, a battle concluded. It is structurally wrong for a *continuous* value. Legitimacy, Popular Support, settlement pressure Π, Mending Stability and Accord do not emit; they *are*, continuously, between emissions, and they decay. There is no named primitive for a persistent, scale-tagged, continuously-read value that Keys deposit deltas into. The consequence is visible in the state taxonomy, which is `{pool, derived_value, track, clock}` — defined only for single-owner scalars — which is why every relational primitive in the tree (treaties, casus belli, NPC edges, settlement footholds) is stored as an untyped dict. What decides it: an architecture ruling on whether a Field/Gauge primitive is added. Both options are defensible and they lead to materially different engines.

**2. Five scale vocabularies are live and none of them agree.** The runtime hard-enforces four (`personal`, `settlement`, `territory`, `peninsula`) and raises on a fifth. The key registry's enum, `module_contracts.yaml`'s implicit seven-value field, the ratified Country > Duchy > Province > Territory > Settlement ladder, and `scale_transitions_v30`'s Object / Personal / Relational / Territorial / Structural set all differ. Only "Personal" appears in all of them, and one registry entry uses a singleton token no sibling uses. This is held at ED-IN-0103 fork 1, and it is not a naming cleanup: the honest reading is that two different concepts — *what size of thing this event is about* and *what administrative tier owns it* — have been forced into one field.

**3. The no-GM ruling is ratified and unexecuted in the document that defines the crossings.** `videogame_mode_spec.md` rules that there is no GM and every "GM decides" phrase must resolve to one of five types. `scale_transitions_v30.md`, its canonical companion and the source of all eight handoffs, still says "GM adjudication" in its mode table and "GM recognises faction scope" in §3.2. Worse, §3.3 and §8 are empty headings whose only specified content sits in an unmerged 2026-04-13 infill file — and that content is itself GM-dependent ("GM makes final scope determination"). So the two empty crossings are not empty for lack of design; they are empty because the design that exists was written under a model that has since been overruled. Decided by: authoring deterministic replacements. The dispatcher already refuses to execute the placeholder, which is the right posture.

**4. Auto-resolution's calibration tolerance is unruled, and it is a live exploit.** Every Slate event can be Played, Witnessed or Auto-resolved by the same kernel. If the outcome distributions differ on matched inputs, the player mode-shops — picking whichever fidelity yields the better strategic consequence. The stated lean is that unbiased mean is a hard constraint and variance may be looser for auto, but the number is deferred to a parity harness that does not exist, which also makes it the acceptance gate for the zoom-in expansion work. This is a genuine Jordan call: how much variance divergence is tolerable is a taste question about how much the player should feel rewarded for playing scenes out.

**5. A default-off bridge is silently equivalent to the seam not existing.** `DISPATCH_COMBAT_BRIDGE` ships OFF and has no producer even when flipped ON. No surveyed precedent defends a cross-scale seam whose default state is indistinguishable from its absence — every comparable game either has no such seam or ships an explicit, imperfect one. The right half of the current implementation is that `derive_parties` returns `None` on a derivation gap rather than inventing an actor; that behaviour should survive any repair.

### What this system needs from others

Almost everything, and the dependency is unusually asymmetric: the plumbing needs *producers*, not consumers.

From **People**: the entire missing input. Six of the seven Sufficient Scope conditions require a person — a named leader, an office-holding NPC, a Disposition reading. The four emitter families that declare `npc_behavior` as a consumer and populate no `targets[]` are blocked on there being an NPC to target. `Key.causes[]` is the machinery by which a person's history becomes queryable; the chain exists and the individual does not. From **social contest and personal combat**: a producer that declares `echo['scene_outcome']`. This is the single field standing between the finished accord-echo loop and it actually running, and it belongs to the scene-resolving lane, not here. From **settlement-governance**: `Settlement.order`, the one state field a Key currently writes, and the Π homeostat the proposed event deck draws against. From **faction-strategy**: `Faction.L` and `Faction.Sta`, which the one working crossing reads, and the Mandate channel Domain Echoes target. From the **resolution kernel**: the degree, which every Echo magnitude table keys on.

What it must build before others can: the `targets[]`/`scale_signature`/`stat_deltas` population on the eight named down-seams, and `references/rendering_dispositions.yaml`, without which no new Key type may be appended — which currently blocks every proposed key in the register.

### The cheapest thing that would make this system playable

Have the contest branch of `scene_dispatch` set `echo['scene_outcome']` on the scene it already resolves.

The accord-echo loop is finished. A scene resolves, a Key is emitted with an honest `causes[]` chain, its `stat_deltas` are collected at emission and applied at the accounting boundary, and `Settlement.order` changes. Every part of it is built, tested and correct. It is dormant on exactly one missing declaration, and the classifier is deliberately strict about it — it will not infer an outcome category from `scene_type`, on the correct reasoning that a resolved combat is not automatically an act of violence against a settlement.

The emergency-council contest is the one scene the campaign actually queues and resolves. It already carries a `ctx['echo']` block. Giving it a declared `scene_outcome` — `destabilisation` is the honest reading of a faction whose Stability fell to 2 or below convening an emergency council — makes a personal-scale scene change settlement state, in a seeded campaign, through the Key substrate, for the first time. That is one field on one dict.

What it buys is out of proportion to its size: it converts the substrate from a write-only log into a loop with an observable output, it gives the eight down-seams a working template rather than a specification, and it produces the first execution artifact for a cross-scale juncture that is not a test. It will move the seeded goldens, because it writes state — so it wants the same treatment as any behaviour change: state the control, and re-pin deliberately.

---

---

### WITHIN-SYSTEM ANALYSIS — "Resolution Kernel"

**What playing it is like.** It works, and it is the only part of Group C that a player would actually feel functioning. Roll a pool of d10s against TN 7, subtract the obstacle, read the margin. Overwhelming at 3 or more, Success at 1 or more, a narrow Partial window for a near-miss-by-nothing, Failure below. It is legible, it is the same at every scale, and the code refuses to be told otherwise: pass any target number but 7 and it raises.

**The load-bearing conflicts, ranked.** First: **the obstacle has no owner while the ladder does.** The margin ladder is single-owned and guarded by a test that fails if a declared hold silently resolves. The obstacle is derived locally in six of seven resolving subsystems and arrives at the roller as a bare parameter. This is decided by ruling R1, and the structural point is the one worth carrying: *ruling the obstacle without also giving the roller an owner predicts the same fork recurring*, and the corpus already has the measured precedent — six private roll/degree implementations in production. Second: **quantisation.** Every obstacle-derivation site rounds or floors, against a ladder whose own docstring says both operands may be fractional; and `sigma_leverage.py:284` rounds the pool to an integer before the continuous engine sees it. Neither is blocked by the score/2 hold — both are code fixes decided by the code. Third: **the 27 probability gates in personal combat have never been scoped.** Thirty outcome-producing branches tree-wide resolve by comparing a random float to a computed probability rather than by rolling, and no ruling mentions whether the obstacle doctrine covers them. That is a genuine Jordan question: are those rolls in disguise, or a deliberately separate resolution mode?

**What it needs from others.** Almost nothing — which is why it works. It needs an obstacle from whoever is calling it, and it needs the systems that fork it (mass battle, contest, threadwork, combat) to stop. The dependency runs the other way: every other system in Group C needs *it*, and several reach it through a private copy.

**The cheapest thing.** Give the obstacle an owner in the same module that owns the roll — a `derive_ob(target_score, modifiers)` living next to `roll_pool`, with the score/2 shape it has already been ruled toward — and route the factions and threadwork call sites through it, since those are the only two lanes that pass an obstacle to the roller today. That is a small, non-behaviour-changing move (the arithmetic is unchanged) that converts the largest outstanding ruling from "a decision with nowhere to land" into "a one-line edit in one file," and it puts the fractional-obstacle fix in a single place instead of four.

---

---

### WITHIN-SYSTEM ANALYSIS — "Mass-Battle Seam"

**What playing it is like.** A faction declares a conquest. Its Military stat is rounded to an integer and becomes the `power` of a single line-infantry subunit at tier 2, standing at cell (8,12), facing forward, with command 4, discipline 5 and morale 5. The defender is built identically, from its own Military, at the same position, facing the same way — or, if the territory is uncontrolled, from a stub with `Mil=1.5`. An eighteen-tick battle runs on a genuinely sophisticated engine — troop types, equipment, formations, per-cell morale, Lanchester signatures, stamina, encirclement — and then the two survivor ratios are compared against three carried-over thresholds to produce a degree. A Key is emitted that nobody subscribes to.

So the engine underneath is rich and the seam above it is one number wide. Terrain is a parameter that the function never reads and the only caller passes as `None`. Command has a real derivation from Charisma and Cognition, and the flag enabling it now defaults on — but the adapter never sets either attribute, so on the campaign path it silently falls back to the hardcoded 4. **The one place in the game where a person's attributes would change a battle is dark for want of a person.**

**The load-bearing conflicts, ranked.** First: **what is a strategic army, in cells?** This is now the single open question at this seam, and the port did not answer it — the adapter's own header says so. The canon engine can express troop types, equipment, formations, multi-subunit hierarchies and orders of battle; the strategic layer offers one integer. Every default in `_faction_to_unit` is marked as inherited-with-a-recorded-gap rather than derived, which is the honest posture, and it means the question is open by declaration rather than by oversight. Decided by Jordan or by the MB lane, and it is a real design fork: an army as a faction stat is cheap and legible; an army as a composed order of battle is where the engine's whole capability lives.

Second: **two degree semantics for one event class.** The survivor-ratio map is a bespoke post-hoc classification maintained separately from the single-owned margin ladder, and it says so in its own comment. Self-disclosure is not a fix; it does the work of a guard and leaves the divergence in place. Decided by the code — but note it was carried over *deliberately*, so that the engine swap would be a single-variable experiment, which was the right call at the time and is now a debt with a due date.

Third: **personal-to-mass leverage has both failure modes coded, sixteen lines apart, and neither is decided.** PC incapacitation applies flat regardless of battle size, which dominates at small N; the Contested Figure wound is a flat Ob shift whose probability effect decays as `1/√N`, which evaporates at large N. Both are currently unreachable because nothing queues a personal scene from a battle. That is exactly the moment to fix the semantics — a personal-scale effect on a mass-scale outcome must scale as a fraction of unit size, and the guard belongs *before* the producer that would make these live, not after.

Fourth: **"officer" means two things and one of them is already load-bearing here.** Mass battle owns the unit commander and the `officer_deaths` key type. If the personnel lane authors a political ladder using the same word, the collision lands in this seam first, on the person who is both a court rank-holder and a battle commander.

**What it needs from others.** From **personnel**: a commander with Charisma and Cognition — that is the whole of what `derive_command` is waiting for, and it is a two-field write, not a system. From **territory-world**: terrain, which the signature already reserves. From **settlement-governance**: garrisons as a real entity rather than a bool, plus the assault/siege/bypass adjacency graph the design specifies and the code does not reach. From the **resolution kernel**: the margin ladder, once the survivor-ratio map is reconciled to it. It owes back, to faction-strategy, the conquest degree and the territorial outcome — which it already delivers.

**The cheapest thing.** Pass a commander's Charisma and Cognition through `_faction_to_unit`. The formula exists, is clamped, and the flag enabling it is already on by default; the guard fails only because both attributes are `None`. The moment any single named person can be attached to a conquest, a battle's outcome starts depending on *who is leading it* rather than only on how large the faction's Military stat is — which is the entire point of having a personnel layer sit above a battle engine. It is a strict superset of nothing: with no commander attached the value stays `None` and the path is byte-identical to today, so it can land ahead of the loader and light up the moment people exist.