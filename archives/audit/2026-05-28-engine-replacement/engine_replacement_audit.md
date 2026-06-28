# Engine Replacement Audit — Should the d10 / TN / Ob Core Engine Be Replaced?

**Date:** 2026-05-28
**Task type:** audit (bootstrap token b1141a77…; `task_gate('audit')` passed)
**Scope:** The core resolution engine (d10 dice pool, per-die TN, success-count vs Ob, degree table) evaluated *as the substrate under every Valoria gameplay system*, against the scope/scales/variety the project now spans. For each system: is the engine flexible enough to meet that system's demands across its sliding scale? With acclaimed precedent-game comparison per system.
**Method:** Bottom-up. Each system's canonical mechanics read from GitHub first (no pattern-matching), then assessed for engine-flexibility-across-scale, then compared to acclaimed precedent games researched per system. Six-direction lens (top-down / bottom-up / lateral / vertical / diagonal / horizontal) folded into the per-system and synthesis sections.
**Predecessors:** `tests/audit/engine_ners_2026-05-15.md` (engine internal-consistency NERS — different question, see §1.3), `tests/audit/engine_audit_2026-04-18.md` (sim-vs-canon scope). This audit asks the question those did not: is the *paradigm* right for the scope, not is the engine internally consistent.
**Decision ownership:** Jordan specifies; this audit informs. It does not prescribe a redesign. Two genuinely open design calls (personal-combat substrate; faction-scale resolver) are explicitly left to Jordan and flagged, not pushed (§8). The scene-combat redesign reserved under handoff `2026-05-17-scene-combat-redesign-exploration` is treated as input only.

---

## §0 — Executive Verdict

**The evidence does not support replacing the core engine. It supports (a) keeping the degree-of-magnitude resolver where it does the most work, (b) two scale-localized resolver decisions, and (c) recognising that the engine is already not a single thing.**

Four findings drive this:

1. **There is no single "core engine" to replace.** Resolution is already scale-fragmented by design: a 5–17D pool at personal scale; a composite/summed pool at unit scale; a bare 1–7D pool at faction scale; deterministic clocks-and-accounting at peninsula scale; and a deterministic filter-chain (not dice) at the investigation/dialogue layer. The d10 pool is fully expressed only at personal scale. (`derived_stats_v30.md` §14.4–14.5; `videogame_mode_spec.md` §0; GD-2.)

2. **For the videogame, the engine is already abstracted away from dice.** Decision E (ED-833/836, `params/core.md` §Continuous Engine) makes the *continuous Normal-distribution* engine canonical for Godot; `videogame_mode_spec.md` §4 explicitly discards literal dice ("Dice → engine resolution with visual feedback"). The audited "d10/TN/Ob" is the TTRPG-mode skin of a continuous degree-of-magnitude gauge.

3. **The genuine weaknesses are scale-local and fixable in place, not paradigm-level.** Bare-stat faction dice (1–7D) is statistically degenerate and is also where the continuous-engine equivalence is *unvalidated* (the spec itself flags the small-pool boundary). These are the strongest "replace at this scale" arguments — and the deterministic+stochastic model GD-2 already mandates for faction AI is the in-place fix, mirroring how acclaimed grand strategy resolves the same scale.

4. **Where the engine is the primary resolver (personal combat, social contest, thread operations) it is demonstrably flexible across its sliding scale** — social contest is the proof case — and replacing it wholesale would discard a validated substrate, force re-derivation of the 13 game-design principles, and break the degree-of-success interface that the entire cross-scale machinery (Domain Echo, co-movement, Persuasion/Evidence/MS clocks) consumes.

**The combat question is real but mis-attributed to the engine.** The five combat properties the project wants (initiative-as-state, weapon-changes-engagement, the bind, asymmetric commitment, reading the opponent) are deliverable in turn-based, single-roll combat — *Battle Brothers* delivers most of them with one d100 roll and no real-time. They come from combat-layer design (tracked states, weapon kits, positioning), not from the resolver's dice type. Replacing the engine would not add them; the current engine does not block them.

**Bottom line:** *Repair-and-keep* dominates *replace* at the level of "the core resolution architecture." The only places where "replace at this scale" is independently defensible are (i) faction/strategic resolution and (ii) — separately and at Jordan's discretion — the personal-combat substrate if the target feel is real-time HEMA. Neither is a reason to replace the substrate everywhere.

---

## §1 — What the Engine Actually Is

### 1.1 The substrate (`params/core.md`)

- **Die rule:** d10; face 1 = −1 success, 2–6 = 0, 7–9 = +1, 10 = +2 (no chain). Net successes = sum, may be negative.
- **Two difficulty channels:** per-die **TN** (6 controlled / 7 standard / 8 desperate) sets success probability per die; **Ob** (1–20) sets successes required. PP-716 reserves the channels: Pool = actor state, Ob = world difficulty.
- **Degree table:** Overwhelming (net ≥ 2·Ob and ≥ 3) / Success (net ≥ Ob) / Partial (0 < net < Ob) / Failure (net ≤ 0). Degree narrows at high Ob by design.
- **Pool grammar:** `(Attribute × 2) + History + K` (K = 3 default), floor 1D.
- **Momentum** (0–4) buys auto-successes.

This is an oWoD-family d10 dice pool (count successes vs a tunable TN, need Ob of them) carrying Burning-Wheel-family design principles (Let It Ride, Fail Forward, Beginner's Luck, Histories-as-pool, escalating-Ob wounds, Reach/Speed, phase combat — `valoria-mechanic-audit/SKILL.md` Mode E).

### 1.2 Decision E — the engine is already two specifications

`params/core.md` §Continuous Engine (Decision E, ED-833/836, 2026-05-15):

- **Discrete** (legacy/TTRPG): roll N d10, count.
- **Continuous** (videogame / "canonical for Godot implementation"): sample `net ~ Normal(μ·N, σ·√N)` with per-TN μ/σ. Outcome magnitude = `net − Ob`, surfaced as a gauge.
- Validated statistically equivalent at **combat parameters only** (pool 5–17D, TN 7; max deviation 0.029 mean / 0.022 std). The spec states the result is CLT-general "by construction" but explicitly warns that **faction-scale bare 1–7D pools sit at the small-pool boundary where the Normal approximation grows shaky and would benefit from dedicated sanity-check.**

`videogame_mode_spec.md` §4 formally discards physical dice for the videogame. So the literal "d10" is a TTRPG artifact; the product runs a continuous degree-of-magnitude resolver with visual feedback.

### 1.3 What the prior engine audit settled — and didn't

`engine_ners_2026-05-15.md` audited the engine for **internal consistency** and concluded its architecture is sound, with defects concentrated in (a) un-propagated recent revisions and (b) one or two open design-asymmetry decisions (2 P1, 8 P2, 11 P3 — all consistency defects, zero paradigm findings). It assumed the d10 substrate and checked coherence. **It did not ask whether the paradigm fits the scope.** Its most useful contribution here is its cross-scale evidence: personal ~17D, unit ~14D, faction 7D bare, peninsula 0–100 clocks (no dice) — the engine is already non-uniform across scales (its finding V-1, "pool size shock across scales").

### 1.4 The degree-of-success output is the cross-scale currency

The single most load-bearing architectural fact for the replacement question: **the engine's *graded* output is what every higher layer consumes.** Domain Echo maps degree → ±stat (`scale_transitions_v30.md` §5.2: Overwhelming ±2, Success ±1, Partial narrative-only, Failure −1 to own stat). Co-movement severity, the Persuasion Track, the Evidence Track, and MS shifts all read *magnitude*, not pass/fail. Any replacement engine must emit a graded magnitude to drive this machinery; a binary resolver or a pure-physics combat resolver would have to re-bolt a degree interface. The continuous engine already provides this as `net − Ob`.

---

## §2 — The Flexibility Lens

Jordan's test: *for each system, is the engine flexible enough to handle demands at an appropriate sliding scale?*

"Sliding scale" has two axes in Valoria, both real:

- **Intra-system intensity** — a quick aside vs a life-or-death duel; a casual remark vs a faction-defining grand debate; healing one wound vs restructuring a kingdom's substrate.
- **Inter-system scope** — the canonical scale ladder Object → Personal → Relational → Territorial → Structural → Foundational (`scale_transitions_v30.md` §2), with base Ob and Thread requirements rising by rung.

A flexible engine should: (a) express the system's decision space at each rung, (b) degrade gracefully as scope rises, and (c) hand outcomes to adjacent systems without an impedance mismatch. The per-system audit (§3) scores each on these.

Three engine properties determine flexibility:

- **Tunability** — TN and Ob are independent continuous-capable levers; degree is continuous (`net − Ob`). This gives fine difficulty/severity control at every rung. **Strength.**
- **Pool-size sensitivity** — outcome quality depends on pool size, which the same 1–7 stat scale maps to wildly differently across scales (17D → 7D → bare 1–7D). **The flexibility weak point.** Small pools (1–3D) are high-variance and non-Gaussian; the engine does its *worst* work at the faction scale, where stakes are highest.
- **Graded output** — drives all cross-scale propagation. **Structural strength and a constraint on any replacement.**

---

## §3 — System-by-System Audit

Each system: **(a)** what the engine does there + operating range; **(b)** flexibility-across-sliding-scale verdict; **(c)** acclaimed precedent comparison; **(d)** finding.

### 3.1 Personal Combat — `combat_v30.md`

**(a) Engine role & range.** Primary resolver. Combat Pool `(Agi×2)+History+3` (5–17D), split Offence/Defence per round; phase-based round (declare blind → resolve by action priority → simultaneous damage). Already carries a substantial tactical layer *on top of* the resolver: deterministic initiative that **transfers to the exchange winner** (a tracked state); asymmetric declaration (lower-initiative declares split first, higher responds — an information/reading element); a **weapon TN matrix** (3 binary axes Reach/Weight/Type → TN 5–8) plus reach rules, zones (Melee/Ranged), and weapon-vs-armour DR tables (weapon changes the engagement profile, not just damage); a **Feint** sub-game (versus roll, margin attrits the opponent's next-round pool — an asymmetric-commitment mini-game); Stamina action-economy with variable costs; and group scaling (Fibonacci outnumbering bonus, multi-engagement single-split, Rescue interception). Sliding scale: 1v1 duel → group melee → TTRPG-scale mass abstraction (§9), the last reusing the same engine via unit stat blocks.

**(b) Flexibility verdict: HIGH at expressing decisions; the limit is round-discrete vs real-time, which is an architecture choice above the engine.** The resolver already supports tracked initiative, weapon profiles, commitment sub-games, positioning, and graceful group scaling. What it does *not* natively express is continuous, moment-to-moment engagement geometry (a Hellish-Quart-style bind). That is a property of *round-based vs real-time resolution*, not of dice-pools — a continuous-engine or a single-roll engine would be equally round-bound or equally real-time depending on the *combat architecture* chosen.

**(c) Precedent.** Acclaimed personal combat splits cleanly into two paradigms. **Real-time / physics** (Hellish Quart, Bushido Blade, Sekiro, For Honor, Mount & Blade) use *no resolution dice at all* — combat is input + physics + timing; "initiative," "bind," "commitment," and "reading" are emergent from real-time play. **Turn-based / probabilistic** (Battle Brothers, XCOM, Wesnoth) use a *single* probability check (Battle Brothers: one d100 vs Melee Skill − Defense, cap 95%; not a pool) and deliver the same five properties *discretely*: Battle Brothers has initiative as a **dynamic state** (it drops as fatigue rises), weapon-specific skill kits (axe breaks shields, mace stuns, sword riposte), zone-of-control + surround positioning, and five discrete **morale states** with contagious panic. Disco Elysium resolves person-to-person stakes with 2d6 + skill vs DC, most checks deterministic passives.

**Implication.** The five desired combat properties are demonstrably achievable in **turn-based, single-roll** combat (Battle Brothers proves it) — they are *combat-layer* features (tracked states + weapon kits + positioning), not a function of the resolver's dice type or its real-time-ness. Valoria's combat already implements partial analogues of all five. Whether to keep round-discrete resolution or move to real-time is the genuine open question, and it is **orthogonal to the dice engine**: real-time would mean abandoning *turn resolution* (the round), not specifically the d10.

**(d) Finding — ER-4 (P2, Robust).** Combat-feel gaps are mis-attributed to the engine. Replacing d10→anything does not add initiative-as-state / bind / reading; deepening the combat *layer* (or moving to real-time, a separate architecture decision) does. The engine neither supplies nor blocks them.

---

### 3.2 Social Contest — `social_contest_v30.md`

**(a) Engine role & range.** Primary resolver, and the **best demonstration of engine flexibility in the project.** Argue Pool `(Primary×2)+History`, where the *primary attribute itself shifts with adjudicator type* (Cognition for an expert judge, Charisma for a crowd, Attunement for no-adjudicator). Exchanges feed a **Persuasion Track** clock (0–10; win ≥7 / ≤3, compromise 4–6) — multi-exchange attrition, not a single roll. A genre×orientation interaction layer (Memory/Projection × Revealing/Obscuring) gives CLASH/REINFORCE/CROSS/TIE resolution — a rock-paper-scissors atop the dice. Composure (Cha×3) = social HP, Concentration (Foc×3) = action economy, Rattled/Spent depletion states — structurally identical to combat. The system *explicitly* flexes by context ("FORMAT FOLLOWS CONTEXT"): Casual Dispute (1 exchange) → Private Negotiation (1–3) → Formal Contest (3) → Grand Contest (5) → asymmetric Tribunal/Royal Audience (biased starting track, halved resistance, non-alternating roles) → **BG Parliamentary Vote** where the pool basis swaps from a personal attribute to **summed faction Mandate** → Hybrid Contest (BG offset feeding TTRPG resolution).

**(b) Flexibility verdict: VERY HIGH.** This is the engine sliding across nearly the full scope ladder (one person → coalition → multi-faction parliament) on one substrate, by varying exchange count, adjudicator-attribute, asymmetry, and pool basis. Graceful degradation and clean cross-scale handoff are both demonstrated (Domain Echo, Obligations as persistent clocks). No paradigm strain.

**(c) Precedent.** Acclaimed social/persuasion systems are *lighter* than Valoria's, not heavier. Disco Elysium: a single 2d6 + skill check, the *majority* of checks deterministic passives (skill + 6 vs DC, no roll) — a deliberate blend of light-stochastic and deterministic. Pentiment: no dice at all — reputation, time pressure, and choice. Citizen Sleeper: a die from a pool feeds a clock (closely parallel to the Persuasion Track). None uses a multi-channel degree-counting pool for dialogue.

**Implication.** Valoria's social engine is *more* mechanically elaborate than the acclaimed baseline. That is a depth/legibility trade-off, not a fitness problem — but it suggests the videogame should lean on the **continuous gauge + passive-check** presentation (à la Disco Elysium passives) so the multi-channel machinery stays invisible. The substrate is not the constraint; presentation is.

**(d) Finding — ER-7 (P3, Elegant).** Social resolution is heavier than acclaimed precedent; consider DE-style deterministic passives for low-stakes exchanges to reduce surfaced complexity. Not an engine defect — a presentation/calibration note. Strong evidence *for* engine flexibility.

---

### 3.3 Fieldwork: Investigation & Dialogue — `fieldwork_v30.md`, `investigation_systems_v30.md`

**(a) Engine role & range.** **Feeder, not resolver — by design.** The Fieldwork Pool `(Primary×2)+History` rolls feed an **Evidence Track** clock (3/5/8 thresholds); but the *conversational/deductive resolution* runs on non-dice machinery: Scene-as-Graph traversal, a Dialogue Lattice of gate types, a **Case Board**, and a deterministic **Five-Filter Response Matrix** (Information → Conviction → Disposition → Compromise → Ethical-Framework). The investigation doc states the filter chain's purpose explicitly: "Without the filter chain, this would be a binary roll. With it, the resolution reflects the specific character of this specific NPC at this specific arc point." Disposition is a per-NPC table; conviction wound-count routes responses deterministically.

**(b) Flexibility verdict: N/A in the right way — the engine is correctly demoted here.** The dice contribute the *accumulation* (Evidence) and the *gate* (can you perceive a Thread-Read at Depth ≥ 4), while character-driven deduction is deterministic. This is the engine flexing *down* to a feeder role, which is exactly right for the domain.

**(c) Precedent.** The acclaimed investigation standard is **deduction with zero RNG**: Return of the Obra Dinn, The Case of the Golden Idol, Her Story, Outer Wilds, Pentiment — clue-gathering + case-board verification, "minimally guided deduction." Disco Elysium is the outlier that *does* roll for investigation beats, but even it makes most checks passive/deterministic.

**Implication.** Valoria's investigation is well-aligned with the acclaimed standard and *already keeps dice out of the deductive core*. This is a model for the rest of the project: the engine as feeder where graded accumulation matters, deterministic systems where character/deduction matters.

**(d) Finding — no defect.** Positive anchor: the investigation layer is the project's clearest example of correct engine scoping (graded feeder + deterministic resolution). It also demonstrates the engine is *not* load-bearing everywhere — weakening the "replace the engine" premise further.

---

### 3.4 Threadwork — `threadwork_v30.md`

**(a) Engine role & range.** Resolver for *operations*, with the heavy lifting in consequence tables and tracks. The Leap roll and each operation (Weaving / Pulling / Locking / Dissolution / Mending) is a Pool/Ob check `(Spi×2)+History+TPS`; Opposing Operations is a contested roll. But the *system's identity* lives in: tridimensional **co-movement** (Version C: temporal + epistemic auto-effects + a d6/card actualized table — mandated by Foundations P-01/P-11), the personal **Coherence** track (10→0), and the world **Mending Stability** clock (0–100). Sliding scale is explicit and well-handled: the §2 scale table raises base Ob and TS requirement by rung (Object Ob 1 → Structural Ob 5+), and Coherence auto-cost scales with scope (0 / −1 / −2).

**(b) Flexibility verdict: HIGH for operation resolution; the system is mostly non-dice.** Ob-scaling cleanly expresses the Object→Structural ladder, and degree drives co-movement severity and MS cost. The engine is a trigger; the consequence architecture is the system.

**(c) Precedent.** The closest paradigm is **Mage: the Ascension's Paradox** family: magic against consensus reality accrues escalating cost; *witnesses worsen the backlash*; thresholds trigger Backlash; a corruption track persists. Valoria's threadwork is recognisably this lineage rendered in its own ontology (MS degradation = consensus strain; visibility → Certainty Scars / Church attention = witness penalty; Coherence = corruption track). Videogame magic-with-cost analogues (Dishonored's Chaos meter, Black Book, Soulslike resource risk) confirm the pattern's reach.

**Implication.** The dice are incidental to threadwork's value, which is its consequence machinery — and that machinery reads **degree** (see §1.4). Any replacement engine must still emit graded magnitude to drive co-movement severity and MS cost. This is a constraint on replacement, not an argument for it.

**(d) Finding — ER-8 (P3, Smooth).** Threadwork is consequence-architecture-first; the resolver choice barely matters *except* that it must remain graded. Reinforces the §1.4 cross-scale-currency constraint.

---

### 3.5 Mass Battle (Unit Scale) — `mass_battle_v30.md`, `military_layer_v30.md`

**(a) Engine role & range.** Resolver, scaled by aggregation. TTRPG-scale unit pool `min(Size, Command) + Command` (2–14D) — the *only* place the engine uses two attributes (breaks the one-attribute-per-roll throughline, but defensibly: unit + commander). BG-scale battle is a **margin system**: `Battle pool = Σ(Martial of engaged units) + floor(Military/2) + Fort dice`, attacker wins if net ≥ defender net + 2, partial within ±1, defender wins symmetrically; net successes distribute as unit damage. Phase-structured (6-phase Cascade) at the tactical rung; single margin roll at the strategic rung; **auto-resolve** (Part B) when the player does not zoom in.

**(b) Flexibility verdict: HIGH, and it mitigates the bare-stat problem.** Because the BG pool *sums unit Martials + commander*, faction battles roll healthy pools (9–14D), not the degenerate bare 1–7D of generic faction actions. The same engine flexes from a 6-phase tactical battle to a one-roll margin auto-resolve via the same Pool/Ob grammar and a pool-basis swap (Size-capped → unit-sum). Graceful.

**(c) Precedent.** Two acclaimed patterns, both present in Valoria. **Nested scale with auto-resolve:** Total War (strategic map ↔ real-time battle, weighted auto-resolve when not played) and Crusader Kings 3 (auto-resolved deterministic combat over phases: Maneuver / Early / Late / Retreat, Advantage from terrain + commander Martial) — Valoria's Part A zoom-in / Part B auto-resolve is exactly this validated pattern. **Turn-based tactical:** Battle Brothers' morale-state + positioning model is a strong reference for the 6-phase tactical rung.

**Implication.** Valoria's mass-battle architecture (zoom-in tactical OR margin auto-resolve) is well-precedented and the engine flexes across it cleanly. Note the divergence: Total War battles are real-time, CK3 combat is deterministic; Valoria's is turn/phase-based with dice. All three are acclaimed — paradigm is a feel choice, not a fitness gate, and Valoria's margin-and-aggregation approach is sound.

**(d) Finding — ER-9 (P3, Elegant).** Two-attribute unit pool is the one throughline break; defensible. The summed-pool design is a *model* for fixing the faction-scale degeneracy (§3.6): aggregate, don't roll bare stats.

---

### 3.6 Faction / Strategic Layer — `faction_layer_v30.md`, `strategic_layer_v30.md`, `ci_political_v30.md`, GD-2

**(a) Engine role & range.** Mixed and **weakest for the engine.** Discrete faction actions (Govern, Trade, Assert, Suppress, Parliamentary Vote, Diplomacy) resolve via a **bare faction-stat pool (1–7D) vs Ob** — the degenerate case. But most faction *state* moves through **deterministic accounting**, not dice: the CI economy is a fractional accumulation pipeline (conditional passive + piety yield + charity + templar + assert/suppress + cap, executed in fixed order — `ci_political_v30.md` §3.11 / `military_layer_v30.md` §3.11); Accord, PT, Turmoil, Treasury/Legitimacy/Reputation/Discipline are income/drain ledgers (`derived_stats_v30.md` §8). Actions are gated by a **card-hand + cooldown economy** (PP-177). Faction AI runs **deterministic posture/priority trees + GD-2's mandatory-then-stochastic** action selection.

**(b) Flexibility verdict: LOW where the engine resolves; the layer already routes around it.** The bare 1–7D pool is high-variance (a 1D roll at TN 7 ≈ 40% with enormous relative spread) and is precisely the small-pool regime where the continuous-engine equivalence is unvalidated (§1.2). The "intentional" scale-shift note (`derived_stats_v30.md` §14.5) concedes that numerically identical stats yield non-comparable dice at this scale. Crucially, the layer's *important* dynamics are already deterministic accounting + AI; the dice are a thin, statistically weak overlay on the parts that are most consequential (who wins parliament, whether a seizure lands).

**(c) Precedent.** The premier acclaimed faction/grand-strategy games **do not use dice pools** at this scale. Crusader Kings 3: deterministic combat simulation + **capped percentage** schemes (≤90%, pre-rolled) + **weighted-random (MTTH) events**. Total War / Stellaris / Europa Universalis: deterministic formulas + weighted events. King of Dragon Pass / Six Ages (the closest structural cousin — clan management + authored event scenes + simulation): skill-gated advisor advice + deep simulation driving scene appearance/outcome, combat abstracted. None resolves faction decisions with a bare-stat success-count pool.

**Implication.** Valoria is the outlier in using dice pools at faction scale — and its own GD-2 already mandates the acclaimed pattern (deterministic threat-response, then stochastic candidate generation). The in-place fix is to extend that: resolve faction actions via the **summed/derived-value** approach the mass-battle layer already uses (§3.5) or a CK3-style capped-probability/weighted model, reserving the dice engine for personal-scale where pools are healthy. **This is "replace the resolver at this scale," not "replace the core engine."**

**(d) Findings — ER-1 (P2, Robust/Smooth):** bare 1–7D faction pool is degenerate where stakes are highest. **ER-2 (P1, Smooth):** continuous-engine equivalence is unvalidated at this small-pool regime — the Godot-canonical engine is only proven equivalent at personal scale. Both are fixable in place and are the strongest scale-local case for change.

---

### 3.7 Settlement Layer — `settlement_layer_v30.md`

**(a) Engine role & range.** Largely unspecified for resolution. Settlement stats (Prosperity / Defense / Order, 1–7) and governance exist; but the derived-value multipliers are **PENDING** (`derived_stats_v30.md` §9), and no settlement-specific resolver is defined. By default it would inherit either bare-stat dice (sharing the §3.6 degeneracy) or deterministic accounting.

**(b) Flexibility verdict: UNDETERMINED — a hole between a healthy rung (personal) and a degenerate one (faction).** The engine *could* fit here cleanly if settlement resolution aggregates (like mass battle) or runs as accounting (like CI), or degenerate if it copies bare-stat faction dice.

**(c) Precedent.** The doc itself cites KOEI Romance of the Three Kingdoms (officer-city assignment, development, provincial control) and Crusader Kings III (barony→county→duchy→kingdom holdings, vassal governance, realm fragmentation). Manor Lords / Songs of Syx / Banished add deterministic city-simulation references. All resolve settlement state via **deterministic simulation + officer/governor modifiers**, not dice.

**Implication.** Settlement should be specified as deterministic accounting + governor-skill modifiers (ROTK/CK3 pattern), *not* as bare-stat dice. Doing so avoids importing the §3.6 degeneracy and keeps the engine where it belongs (feeding graded outcomes when a governance *scene* is played personally).

**(d) Finding — ER-6 (P2, Robust).** Settlement resolution is an open hole; specify it as deterministic-simulation-first to avoid bare-stat dice degeneracy. Any engine verdict is partial until this rung is designed.

---

### 3.8 Peninsula Clocks & Victory — `peninsular_strain_v30.md`, `victory_v30.md`, GD-1

**(a) Engine role & range.** **The engine is correctly absent.** MS / CI / IP are 0–100 clocks moved by deterministic accounting; Accord (0–3) and Turmoil are per-territory counters; PT is a 0–3+ territory clock. Victory (GD-1) is a deterministic check: control 11/15 territories (treaties counting), Accord ≥ 2, Political Stability ≤ 6, sustained 2 consecutive seasons. No dice.

**(b) Flexibility verdict: N/A — correctly deterministic.** World-state at this scope should be legible and non-stochastic; it is. The engine's job here is upstream (graded outcomes feed the clocks), not at the clock itself.

**(c) Precedent.** Universal among acclaimed grand strategy: world/era state and victory are deterministic thresholds + accumulators (CK3, EU, Stellaris, Total War). Valoria matches the standard exactly.

**(d) Finding — no defect.** Confirms the engine is appropriately *not* the resolver at the top of the scope ladder.

---

### 3.9 Scale Transitions — the glue — `scale_transitions_v30.md`

**(a) Engine role & range.** The zoom system (mandatory + elective triggers, stack-based container transitions, max depth 3) is deterministic. The engine's **degree output is the cross-scale currency**: Domain Echo converts a personal scene's degree into ±faction-stat (§5.2), gated by Sufficient Scope (§7); BG-degree biases the personal scene's Ob on zoom-in (§4.1). Co-movement, Accord Echo, Thread Echo all read degree.

**(b) Flexibility verdict: HIGH and structurally central.** This is where the engine's graded output earns its keep — it is the common interface that lets personal-scale play move strategic-scale state. A binary or non-graded resolver would break this; the continuous gauge strengthens it (finer Domain Echo possible).

**(c) Precedent.** Nested-scale handoff is well-precedented: Total War and Mount & Blade (campaign ↔ battle), King of Dragon Pass / Six Ages (saga ↔ event scene), Battle Brothers (worldmap ↔ tactical). What is distinctive in Valoria — outcomes from the *low* scale propagating *graded* consequences *up* to faction/world state — is closest to KoDP/Six Ages' simulation-driven scene consequences, and is a genuine strength.

**(d) Finding — structural strength + constraint.** The degree interface is a reason to *keep* a graded resolver and a hard constraint on any replacement (§1.4).

---

## §4 — Consolidated Findings Register

Severity: P1 (blocks/structural), P2 (architectural), P3 (polish/clarity). NERS axis per `valoria-mechanic-audit` convention.

| # | Finding | Sev | NERS | System | Source |
|---|---|---|---|---|---|
| ER-1 | Bare-stat faction pool (1–7D) is statistically degenerate where stakes are highest | P2 | Robust/Smooth | Faction | `derived_stats §14.4–14.5` |
| ER-2 | Continuous-engine equivalence unvalidated at small-pool (faction) regime; Godot-canonical engine proven equivalent only at personal scale | P1 | Smooth | Faction / core | `params/core.md` §Continuous Engine (WS-D-1/ED-836) |
| ER-3 | Cross-scale pool-size shock (17D→7D→clocks); same 1–7 stat ≠ comparable dice across scales | P2 | Smooth/Vertical | Cross-scale | `engine_ners` V-1; `derived_stats §14.5` |
| ER-4 | Combat-feel gaps mis-attributed to engine; they are combat-layer / real-time-vs-turn decisions | P2 | Robust | Combat | `combat_v30 §1–8`; handoff #1; Battle Brothers precedent |
| ER-5 | Two parallel difficulty channels (TN-as-difficulty in combat, Ob-as-difficulty elsewhere) | P3 | Elegant | Combat vs others | `engine_ners` L-3; `params/core.md` TN table |
| ER-6 | Settlement resolver unspecified (PENDING); risks importing bare-stat degeneracy | P2 | Robust | Settlement | `derived_stats §9`; `settlement_layer` |
| ER-7 | Social resolution heavier than acclaimed precedent; lean on deterministic passives for low-stakes | P3 | Elegant | Social | `social_contest §4`; Disco Elysium precedent |
| ER-8 | Threadwork is consequence-architecture-first; resolver must remain graded | P3 | Smooth | Threadwork | `threadwork_v30 §2–5`; Mage Paradox precedent |
| ER-9 | Mass-battle unit pool uses two attributes (throughline break); summed-pool is a model for fixing ER-1 | P3 | Elegant | Mass battle | `mass_battle §B.3`; `military_layer §2` |

**Distribution:** 1 P1 (ER-2, validation gap), 4 P2 (ER-1, ER-3, ER-4, ER-6), 4 P3. **None is a "the paradigm is wrong" finding.** Every P1/P2 is either scale-local (ER-1/2/6), a known cross-scale calibration (ER-3), or a mis-attribution (ER-4).

---

## §5 — Flexibility Synthesis: Where the Engine Fits, Strains, and Is Correctly Absent

| Rung / system | Engine role | Pool regime | Flexibility | Verdict |
|---|---|---|---|---|
| Personal combat | Primary resolver | 5–17D | High (decisions); limited only by round-vs-realtime | **Fits.** Gap is combat-layer/architecture, not engine. |
| Social contest | Primary resolver | 5–18D | Very high (slides 1-person → parliament) | **Best fit.** Proof of flexibility. |
| Thread operations | Resolver (trigger) | 5–17D+ | High; system is mostly tracks/tables | **Fits**, must stay graded. |
| Investigation / dialogue | Feeder only | n/a (feeds Evidence) | Correct demotion | **Correctly scoped.** Deduction is deterministic. |
| Mass battle | Resolver (aggregated) | 9–14D (summed) | High; summed pool avoids degeneracy | **Fits.** Model for ER-1 fix. |
| Faction / strategic | Thin overlay on accounting+AI | **1–7D bare** | **Low** where dice resolve | **Strains.** Replace *resolver at this scale*. |
| Settlement | Unspecified | PENDING | Undetermined | **Hole.** Specify deterministic-first. |
| Peninsula / victory | Absent (deterministic) | n/a | Correct | **Correctly absent.** |
| Scale transitions | Degree = cross-scale currency | n/a | High; structurally central | **Keep graded resolver.** |

**Pattern.** The engine *fits well wherever pools are healthy and a graded contested outcome is wanted* (personal combat, social, thread, aggregated mass battle), is *correctly demoted or absent wherever deduction or world-accounting dominates* (investigation, peninsula, victory), and *strains only at the faction scale* where it rolls bare stats — the one place it is both statistically weakest and unvalidated. The fit/strain map is scale-shaped, not paradigm-shaped.

---

## §6 — Precedent Summary

| System | Acclaimed precedents | Their resolution paradigm | Implication for Valoria |
|---|---|---|---|
| Personal combat (real-time) | Hellish Quart, Bushido Blade, Sekiro, For Honor, Mount & Blade | Input + physics + timing; no resolution dice | Five combat properties are emergent from real-time; a *combat-architecture* path, not an engine swap |
| Personal combat (turn-based) | Battle Brothers, XCOM, Wesnoth | Single probability check (e.g., one d100); discrete states (initiative, morale), positioning, weapon kits | Five properties achievable turn-based with one roll — combat-layer, not dice-type |
| Social / dialogue | Disco Elysium, Pentiment, Citizen Sleeper | 2d6+skill (mostly passive/deterministic); choice/reputation; die→clock | Valoria's is heavier; lean on passives/gauge for presentation |
| Investigation | Obra Dinn, Golden Idol, Her Story, Outer Wilds, Pentiment | Deduction, zero RNG; case-board verification | Valoria already aligned; keep dice out of deduction |
| Threadwork | Mage: the Ascension (Paradox); Dishonored Chaos | Escalating consequence/backlash + corruption track; witnesses worsen | Valoria is this lineage; consequence tables are the system, resolver incidental but must stay graded |
| Mass battle / nesting | Total War, Crusader Kings 3, Mount & Blade | Real-time or deterministic battle + weighted auto-resolve; campaign↔battle nesting | Valoria's zoom/auto-resolve is well-precedented and sound |
| Faction / grand strategy | Crusader Kings 3, EU, Stellaris, King of Dragon Pass / Six Ages | Deterministic formulas + capped % + weighted (MTTH) events + simulation; **no dice pools** | Valoria's bare-stat dice is the outlier; GD-2 already points to the standard fix |
| Settlement | KOEI ROTK, Crusader Kings 3, Manor Lords | Deterministic simulation + governor/officer modifiers | Specify settlement deterministic-first, not bare-stat dice |
| Dice-in-videogame proof | **Citizen Sleeper** (acclaimed 2022) | d6 pool → feeds clocks; pool shrinks with damaged condition | Dice pools *can* headline an acclaimed videogame; Valoria's pool→clock pattern is the same — validates keeping the engine where it fits |
| Closest structural cousin | **King of Dragon Pass / Six Ages** | Clan management + authored event scenes + simulation + skill-gated advice | Validates Valoria's strategic↔personal nesting; resolution is sim + skill + authored content, not one unified dice engine |

**Two precedent takeaways stand out.** (1) *Citizen Sleeper* proves a dice-pool-feeding-clocks resolver can anchor an acclaimed videogame — and it is structurally Valoria's own pattern (pool feeds Persuasion/Evidence/MS clocks; wounds shrink the pool). This is direct evidence *against* "dice don't belong in the videogame." (2) Across every other scale, acclaimed games **stop using dice as scope rises** — deduction and world-state go deterministic; faction goes deterministic+weighted. Valoria already does this *except* at the faction action rung (ER-1).

---

## §7 — Replace vs Repair: The Decision, Both Cases

### 7.1 The case FOR replacement (stated at full strength)

- **If the target personal-combat feel is real-time HEMA** (the project's own references), a round-resolved degree-of-success system is the wrong *architecture* for combat specifically. The acclaimed exemplars use no resolution dice. This is the one place a genuine engine-class change (for combat) has a real argument — but it is confined to combat and is an architecture decision, not a substrate-everywhere decision.
- **A unified engine is a TTRPG value, not a videogame requirement.** Videogames routinely run scale-native resolvers (tactics ≠ strategy). Valoria is already drifting there (clocks at peninsula, deterministic+stochastic at faction, deterministic filters at investigation). "Replace the engine" may really mean "stop treating one substrate as universal and formalise scale-native resolution."
- **ER-1/ER-2 independently justify replacing the resolver *at faction scale*** with the deterministic+stochastic model GD-2 already mandates and CK3/EU/KoDP exemplify.

### 7.2 The case AGAINST wholesale replacement

- It discards a **validated** personal-scale resolver (validated exactly where it does most work) and the continuous abstraction already built for Godot (Decision E).
- It forces **re-derivation of all 13 game-design principles** (Mode E) and re-checking against the **immutable Foundations P-01–P-15**. Note the Foundations are largely *engine-agnostic* (they mandate tridimensional co-movement, the track/clock layer, and a graded actualized table) — so they don't force d10, **but any replacement must still emit graded magnitude** (§1.4) to drive co-movement, Domain Echo, and the clocks.
- It does **not** fix ER-4 (combat-layer), ER-3 (cross-scale shock recurs under any substrate), or ER-6 (settlement hole). It addresses only ER-1/ER-2, both fixable in place.
- *Citizen Sleeper* demonstrates the existing pool→clock pattern is videogame-viable and acclaimed.

### 7.3 Constraints any replacement engine must satisfy

1. **Graded magnitude output** (`net − Ob` or equivalent) — non-negotiable; the entire cross-scale machinery reads it.
2. **Two independent difficulty levers** (actor-state vs world-difficulty) — PP-716 channel separation is load-bearing across systems.
3. **Tridimensional co-movement compatibility** (Foundations P-01/P-11/P-14) — every operation must be able to fire temporal + epistemic + actualized auto-effects.
4. **The 13 design principles** (Let It Ride, Fail Forward, Beginner's Luck, escalating-Ob wounds, etc.) must survive or be deliberately retired.
5. **Healthy resolution at the scale used** — the lesson of ER-1: do not roll bare small pools at high-stakes scales.

### 7.4 Net

At the level of *the core resolution architecture for the whole game*, **repair-and-keep strictly dominates replace**: keep the (continuous) graded resolver where pools are healthy and graded contest is wanted; fix the faction-scale resolver in place (aggregate or go deterministic+weighted, per GD-2/CK3); specify settlement deterministic-first; treat combat feel as a separate, layer/architecture decision. Wholesale replacement buys only ER-1/ER-2 (fixable in place) at the cost of the validated substrate, the 13 principles, and the degree interface.

---

## §8 — The Decisions That Are Jordan's (not pushed here)

Two design calls are genuinely open; this audit supplies inputs, not a direction.

1. **Personal-combat substrate / architecture.** Keep round-resolved degree combat vs move to real-time (the reserved scene-combat exploration). *Engine-audit input:* the dice substrate is adequate and flexible for combat decisions, but it is not *aimed* at the real-time HEMA feel the project keeps citing; that feel is an architecture choice (turn vs real-time) largely independent of the dice. Battle Brothers shows the five desired properties are reachable turn-based; Hellish Quart shows the real-time path drops resolution dice entirely.

2. **Faction / strategic resolver.** Keep bare-stat dice vs adopt the deterministic+stochastic model GD-2 already mandates (CK3/EU/KoDP pattern), or the summed/derived-value approach mass battle already uses. *Engine-audit input:* ER-1 (degeneracy) + ER-2 (unvalidated) make "replace at this scale" defensible on its own merits, and the project's own GD-2 already points the way.

Neither call is a reason to replace the substrate at personal scale, where it fits and is validated.

---

## §9 — Open Items, Limits, and Findings to File

- **Not committed.** No repo writes this session: branch protection (finding B6) blocks PAT commits to `main`, and the editorial ledger is mid-consolidation (active handoff `2026-05-XX-editorial-ledger-consolidation`). Filing now would conflict. **[DRIFT: audit-skill "P1 → editorial_ledger.yaml" not executed — reason B6 + ledger consolidation in flight.]** ER-2 (P1) and ER-1/ER-3/ER-6 (P2) are staged here for Jordan to file in a dedicated ledger session.
- **Validation debt (closes ER-2):** run a small-pool (1–7D) sim to test discrete-vs-continuous equivalence at faction scale before relying on the continuous engine there; the spec's CLT claim is untested below pool 5.
- **Did not cover:** NPC behavior AI internals, conviction/knot mechanics, arc/throughline systems, economy/treasury balance — out of engine-resolution scope. Settlement resolver is unspecified (ER-6), so its verdict is provisional.
- **Precedent caveat:** precedent resolution paradigms are summarised from public documentation of each game; treat exact numbers as indicative, not authoritative.
- **Confidence:** High on §0 verdict and ER-1/ER-2/ER-4 (trace to cited canon + the spec's own admissions). Medium on settlement (ER-6, unspecified rung).

**One-line answer to the brief:** *Do not replace the core engine. It is already a continuous, graded resolver that fits well wherever pools are healthy and is correctly demoted or absent elsewhere; repair the one scale where it strains (faction, bare-stat) using the deterministic+stochastic pattern the project already mandates and acclaimed grand strategy already uses — and treat combat feel as a separate architecture decision, not an engine swap.*
