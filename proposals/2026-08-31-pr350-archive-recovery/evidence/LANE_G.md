## LANE G — GOVERNANCE, FACTIONS & THE STRATEGIC LAYER

### COVERAGE
files_assigned: 69 (42 provincial/ + 27 architecture/) | files_opened: 40 | files_read_closely: 26

skipped: `mass_battle_v30`(+index+infill), `mass_battle_integration_v30`, `military_layer_v30`(+index) — out of scope per brief, no faction/governance-write seam found worth reporting beyond what §1.2 Trigger 5 and §6 (faction_layer) already cover. `key_type_registry_v30.md` — full type catalogue skipped; summary table lifted from `key_substrate_v30` §3 instead. `strategic_layer_v30` (55K) — an early v0.6 audit doc whose dice/Ob corrections are superseded by the resolver system in `faction_layer_v30`; skimmed for gaps only. `hybrid_gaps_v30`, `campaign_modes_v30`, `videogame_mode_spec`, `canonical_registry`, `complete_systems_reference`, `early_game_ignition_analysis` — headings only, content overlaps material already covered closely elsewhere. All `_index.md`/`_infill.md` companion files skimmed or skipped where the skeleton doc's own body already carried the substance. Explicitly excluded per brief: `cogload_moderate_target`(+index), `companion_app_design_note`, `session_a_spec_patches`, `tensions_pair_validation`, and `/proposals/`.

### FINDINGS (ranked)

**F-G-1 — A faction is not an independent agent; its conduct is a derived aggregate of its people's convictions**
- SOURCE: `designs/architecture/../provincial/faction_behavior_v30.md` §1, §3.2; `provincial/faction_canon_v30.md` §3.2
- CATEGORY: ontology
- SUBSTANCE: PP-686 v2 defines faction behavior as four components: **Mission** (authored telos), **Cascade** (derived, not authored — `effective_convictions(npc) = α·personal_convictions(npc) + (1−α)·effective_convictions(supervisor(npc))`, then Standing-weighted and normalized up the hierarchy), **Public Expectation** (role template vs. Mission consistency), and **Legitimacy+Popular Support** (per-settlement, not faction-level). Ob modifiers on Domain Actions come from a triadic sum of mission/cascade/expectation alignment, clamped ±2.
- WHY IT MAY STILL MATTER: Directly answers "does a faction act as an agent or only through people?" — mechanically it answers **through people**: a faction has no independent personality; swap the leader and NPC roster and the faction's behavior changes via the cascade formula, not via a hand-authored faction "AI."
- STATUS IN DOC: CANONICAL (promoted after Stage 10 sim PASS 12/14 battery); faction_canon_v30's consolidation is PROVISIONAL pending ratification.
- REDISCOVERED IN: single source (faction_behavior_v30), consumed verbatim by faction_canon_v30.

**F-G-2 — Mandate is explicitly DERIVED, never stored; correcting a real defect where it wasn't**
- SOURCE: `provincial/faction_behavior_v30.md` §4, §2 (schema comment); `provincial/faction_canon_v30.md` §5.1
- CATEGORY: derivation
- SUBSTANCE: `Mandate(faction) = clamp(round(7·T/(T+K)),0,7)`, `T = Σ_s W_s·(0.5·L_s+0.5·PS_s)/7`, `K=6` — a size-weighted, saturating aggregate of **per-settlement** Legitimacy/Popular Support. The schema literally comments `# DERIVED`. This replaced an earlier "7-stat" faction lineup where L/PS were faction-level scalars — which broke on the concrete case "perfect L/PS but one province computes the same Mandate as a peninsula-spanning faction." Jordan ruling LPS-1→LPS-2e (2026-05-30) fixed it by moving L/PS to settlements and making Mandate the weighted aggregate.
- WHY IT MAY STILL MATTER: A clean worked example of "X must be derived, never stored" catching a real design bug before it shipped.
- STATUS IN DOC: CANONICAL (LPS-2e resolution).
- REDISCOVERED IN: faction_state_authoring_v30 §8, franchise_v30 (independently converges on per-territory weighting for a different stat — National Influence).

**F-G-3 — Universal Key substrate: one update rule, all state as typed append-only records**
- SOURCE: `architecture/key_substrate_v30.md` §1, §4.1, §3
- CATEGORY: ontology / mechanism
- SUBSTANCE: Every consequential event is a `Key` (uuid, type, source_actor, causes[], targets[] with role+impact_vector, scale_signature, symbolic_dimensions on a 4-axis Conviction space, visibility, permanence). One `on_key_emitted()` function validates, appends to an immutable log, resolves observers, has each interpret via their "armature," propagates to subscribing systems, and updates a sparse causal graph. Save state = initial conditions + Key log; replay = deterministic re-execution. 7 type families (scene_event, da_outcome, mechanical_event, state_transition, environmental, scene_outcome, system_meta).
- WHY IT MAY STILL MATTER: This is the substrate every other governance mechanism (Domain Echo, Cascade, Mission-shift) composes on. If any of it survived, it's the single highest-leverage piece — it is the actual answer to "who emits, who consumes."
- STATUS IN DOC: CANONICAL (Stage 10 sim PASS); doc header says PROVISIONAL pending final ratification.
- REDISCOVERED IN: single source; consumed by faction_behavior_v30 §5, political_dynamics_keys_migration_v30 (NPC memory), scale_transitions_v30 §12.

**F-G-4 — Stability redesigned as five named, historically-grounded shock triggers, not a broad failed-action tax**
- SOURCE: `provincial/faction_layer_v30.md` §1.1–§1.2 (esp. line 43–52, Trigger 1–5 tables)
- CATEGORY: mechanism
- SUBSTANCE: PP-403 (Stability −1 on any failed Domain Action) was repealed; Stability now changes only via 5 named triggers — Territorial Occupation/Loss, Unfavourable Treaty Terms, Antagonistic Parliamentary Vote, Major Subterfuge, and a 3-condition-gated Failed Military Engagement (committed force ≥4 AND clear defeat AND severity threshold). The infill's rationale is explicit: Venice lost battles constantly yet was one of history's most stable polities — ordinary reverses shouldn't destabilize a state; only structurally visible shocks should.
- WHY IT MAY STILL MATTER: A crisp worked distinction between "failure" and "shock" for any stability/legitimacy meter — avoids the death-by-a-thousand-cuts failure mode.
- STATUS IN DOC: CANONICAL.
- REDISCOVERED IN: single source, consumed in faction_canon_v30 §8, ci_political_v30 §4.4.

**F-G-5 — Faction Collapse is a 6-step procedure, plus a fix for a mathematically non-functional death-spiral floor**
- SOURCE: `provincial/faction_layer_v30.md` §1.5 (line 207–232), §1.4 line 203 (FSS-LOOP-1)
- CATEGORY: mechanism
- SUBSTANCE: Collapse at Stability 0: Mandate→0, territories→Uncontrolled (Accord→0/Revolt), units→Masterless (claimable), officers→Independent (recruitable), PC loses faction bonuses (3 paths: join/reconstitute/stay independent), Parliamentary seat lost, victory conditions close. Separately: the original "Stability ≤2 treated as Ob 4" anti-death-spiral floor was measured non-functional (a 2-die pool vs Ob 4 succeeds ~1% of the time) — replaced by a deterministic floor: the Accounting check simply *cannot reduce* Stability at ≤2 (min result Partial). Collapse remains reachable only via active pressure (the 5 triggers), never passive dice decay.
- WHY IT MAY STILL MATTER: The floor fix is a good worked example of "a rule that looks protective but is mathematically inert" — worth checking wherever a probability floor is used defensively.
- STATUS IN DOC: CANONICAL; FSS-LOOP-1 explicitly supersedes and subsumes the older Survival Exception check-path protection.
- REDISCOVERED IN: independently confirmed in factions_personal_v30 §8.12 ("[SUPERSEDED-BY FSS-LOOP-1]" annotation) — a genuine independent-rediscovery signal since factions_personal predates the fix and was patched to point at it.

**F-G-6 — Succession is a two-stage resolver: "who leads" and "does it split" are decoupled**
- SOURCE: `provincial/faction_succession_split_v30.md` §2.2–§2.3
- CATEGORY: mechanism / governance
- SUBSTANCE: On leader loss, contender strength is deterministic (Mandate+Influence for blood heirs, etc.). Stage 1 (dice, contested resolver) decides *who leads*; Stage 2 (deterministic strength gap G) decides *whether the realm fragments* — G≥3 unified, G=2 unified-but-fractious (disposition check), G≤1 splits ~60/40. This replaced a prior single-roll model where "margin <2 → split" let dice alone decide fragmentation, fragmenting ~50% of near-peer successions regardless of actual power balance.
- WHY IT MAY STILL MATTER: Clean structural insight — a single roll conflating two different questions (who wins vs. how decisively) produces wrong variance; splitting them fixes it without adding complexity.
- STATUS IN DOC: PROVISIONAL (approved mechanical design, pending smoke-test).
- REDISCOVERED IN: single source; explicitly generalizes and supersedes the earlier faction-specific `baralta_crown_claim_v30` §2 contest.

**F-G-7 — Fractional Province Ownership: provinces split Greater/Lesser proportional to settlement prosperity, not binary**
- SOURCE: `provincial/fractional_province_ownership_v30.md` §2
- CATEGORY: mechanism / settlement
- SUBSTANCE: A province with a mixed-controller settlement (but Seat-holder unchanged) becomes fractional; each settlement's PV share = its Prosperity fraction of the province total. Renamed "Greater X" (Seat-holder) / directional "Northern/Eastern X" (others). A holder of ≥75% PV share may declare Consolidation (Influence roll, target chooses Submit or Resist). Below 75%, each Accounting rolls a Fragmentation Check; on Failure the minority holder may declare Secession — a permanent fracture.
- WHY IT MAY STILL MATTER: Answers "when Hafenmark seizes one settlement from Varfell, is the whole province now Hafenmark's?" with a real intermediate state instead of binary flip — a genuinely underused wargame mechanic (explicit CK3/ROTK precedent cited).
- STATUS IN DOC: PROVISIONAL (approved 2026-04-19, pending smoke-test).
- REDISCOVERED IN: single source; consumed by victory_v30's PV counting and faction_layer's occupation rules.

**F-G-8 — Franchise: parliamentary weight is per-territory, structurally unequal, and tied to caste**
- SOURCE: `provincial/franchise_v30.md` §2–§4
- CATEGORY: governance
- SUBSTANCE: Franchise (0–5 per territory) measures a territory's political weight independent of its economic output — driven by war-coalition history, Church penetration, and caste stigma (southern Einhir territories score 1–2 vs. capital's 5). National Influence (replacing the old flat Influence stat) = Franchise-weighted mean of per-faction Territory Influence. Worked numbers: Crown starts ~5 National Influence from prestige territories; Varfell, holding equally-controlled but low-Franchise territories, is structurally capped lower — "even with total control of their territories, the caste system mutes their parliamentary voice." This is the mechanical answer to "who is enfranchised."
- WHY IT MAY STILL MATTER: A concrete, numeric expression of structural political inequality that a player can act against (Franchise rises +1 after 4 stable seasons, or via an unauthored "caste reform" hook) — ties personal-scale caste-reform play to strategic-layer power.
- STATUS IN DOC: DRAFT — awaiting Jordan review (never promoted).
- REDISCOVERED IN: single source; explicitly fills a gap flagged in faction_politics_v30 §3.

**F-G-9 — Treaty Expiration: 90%/arc lapse rate is a deliberate, self-admittedly "narratively extreme" Crown-nerf**
- SOURCE: `provincial/treaty_expiration_v30.md` §1, §4
- CATEGORY: mechanism / balance
- SUBSTANCE: Every Crown Treaty independently rolls for lapse at each 4-season arc boundary at 90% probability, memoryless (a 3-arc-old treaty has the same lapse chance as a new one). Without it, Crown compounds treaty-hegemony to 55-90% win rate at N=1000; with it, all factions land in a 22-29% band. Renewal costs a full Senator Outward action + Wealth −2 per treaty per arc. The doc's own §4 quotes the balance-audit source verbatim: "90-95% lapse rate is mechanically functional but narratively extreme. Almost every Treaty breaks every arc."
- WHY IT MAY STILL MATTER: A rare case of a design doc admitting its own mechanic is narratively broken while keeping it for balance reasons — flags a real unresolved tension (mechanical necessity vs. fictional plausibility) worth resolving explicitly if this is ever revived, rather than silently re-deriving 90% from nothing.
- STATUS IN DOC: CANONICAL (Pass 2h) with 3 explicit PROVISIONAL sub-items awaiting "Pass 2k" ratification that this lane found no evidence ever happened.
- REDISCOVERED IN: single source; cited as CB source by parliamentary_transfer_v30.

**F-G-10 — Parliamentary Territory Transfer: a formal, CB-gated, vote-weighted mechanism to move territory without battle**
- SOURCE: `provincial/parliamentary_transfer_v30.md` §1–§4
- CATEGORY: mechanism / governance
- SUBSTANCE: Requires standing Casus Belli (8 distinct sources, faction-pair-scoped ledger). Roll = proposer Influence vs. holder Legitimacy+2, wrapped in a Parliamentary Vote contest that shifts the pool ±1D by bloc majority. Four narrative "modes" (Adversarial/Consensual/Punishment/Appeasement) gate which CB sources qualify and adjust outcome framing (e.g., Appeasement grants +2 Accord instead of +1). Last-territory and self-transfer protections built in.
- WHY IT MAY STILL MATTER: A genuinely rich non-military territorial-transfer mechanism, balance-validated at N=1000 as one of three levers that broke Crown's dominance.
- STATUS IN DOC: CANONICAL (Pass 2h), core mechanic Tier-0 validated; mode-specific and vote-modifier details flagged PROVISIONAL pending unresolved Pass 2k.
- REDISCOVERED IN: single source.

**F-G-11 — Parliament: weighted majority votes, a cooldown-gated Sacred Veto, and CI as an asymmetric legitimacy modifier**
- SOURCE: `provincial/faction_layer_v30.md` §5.3–§5.4; `provincial/ci_political_v30.md` §3.2–§3.4
- CATEGORY: governance
- SUBSTANCE: Each faction votes with Mandate; targeted faction abstains. 10 named motion types (Censure, Embargo, Blockade, Outlawry, Subsidy, War Authorisation, Treaty Ratification, Recognition Challenge, Succession Endorsement) each with its own proposer threshold, vote type, and duration. Church holds a Sacred Veto (once per 4 seasons, costs Mandate if used against a motion that would've passed or in self-interest). Church's institutional weight adds ⌊CI/20⌋ to its own vote/margin, while opponents voting against Church lose ⌊CI/30⌋ from their own contribution (floored at 0) — explicitly modeled on papal political weight fluctuating with demonstrated authority (Julius II vs. Avignon papacy).
- WHY IT MAY STILL MATTER: A concrete, asymmetric "soft power" mechanic — institutional legitimacy that helps its holder AND penalizes opposition, rather than a flat vote-count bonus.
- STATUS IN DOC: CANONICAL.
- REDISCOVERED IN: single source (faction_layer + ci_political are companion docs by the same author pass).

**F-G-12 — Graduated Löwenritter Autonomy: a reversible 4-stage progression replaces a binary coup counter**
- SOURCE: `architecture/conflict_architecture_proposal.md` "Graduated Löwenritter Autonomy"
- CATEGORY: mechanism / problem-only-turned-solved
- SUBSTANCE: Loyal → Restless → Autonomous → Split, each stage triggered by named Crown-Stability/disposition/duration conditions, each reversible except the last. "Autonomous" is called out as the richest state — nominal loyalty with functional independence (explicit Teutonic-Order-in-Prussia parallel) that can persist indefinitely and forces every neighboring faction to decide how to treat the ambiguity.
- WHY IT MAY STILL MATTER: A strong template for "institutional loyalty as continuous state, not boolean" — directly reusable anywhere a subordinate power center might defect.
- STATUS IN DOC: CANONICAL.
- REDISCOVERED IN: single source; the underlying Coup Counter mechanic it replaces is independently visible in `clock_registry_v30` ("Löwenritter Autonomy: Loyal/Restless/Autonomous/Split") and baralta_crown_claim_v30 §7 — consistent across all three.

**F-G-13 — Clocks are pure passive counters, never agents — confirmed negative finding**
- SOURCE: `provincial/clock_registry_v30.md` (whole doc); `architecture/integration_proposal_v30.md` "The Faction Layer as the Game's Clock"
- CATEGORY: ontology
- SUBSTANCE: Every clock/track in the corpus (MS, CI, IP, Turmoil, per-faction stats, per-territory Accord/PT, personal tracks, contest clocks, Obligation clocks) is specified purely as {range, start, direction, source} with explicit derivation formulas where applicable — no clock has behavior, goals, or agency. Integration_proposal explicitly frames this as design intent: clocks should read as ambient environmental information ("the way sailors glance at the sky"), not urgent alerts, and "the game world IS the clock display."
- WHY IT MAY STILL MATTER: The brief flagged this as a design-smell risk; the corpus is clean on this axis — worth recording as a confirmed absence, not just a gap in what I found.
- STATUS IN DOC: CANONICAL (clock_registry).
- REDISCOVERED IN: independently stated in both clock_registry_v30 and integration_proposal_v30, which are different authoring passes.

**F-G-14 — Domain Echo: the one seam where personal scenes write to faction stats, deliberately capped against exploitation**
- SOURCE: `architecture/scale_transitions_v30.md` §5, §3.4
- CATEGORY: seam / mechanism
- SUBSTANCE: A personal scene that meets "Sufficient Scope" can push ±1/±2 to "the most relevant faction stat," capped at 1 Domain Echo per scene per faction (PP-329, closing an earlier compounding exploit ED-071). In full TTRPG it fires immediately; in BG/Hybrid it queues to seasonal Accounting specifically "to prevent real-time manipulation of BG stats from personal scenes." Separate Accord Domain Echo and Thread Domain Echo variants exist with their own caps.
- WHY IT MAY STILL MATTER: This is the canonical answer to "how does personal-scale play affect the strategic layer" — a deliberately narrow, capped, delayed channel rather than a wide-open one.
- STATUS IN DOC: CANONICAL.
- REDISCOVERED IN: independently named as "Mechanism 1" in integration_proposal_v30 Part 3, cross-checked against a formal reference table in that doc's Part 8.

**F-G-15 — Generational transition has a named five-way typology for what survives death**
- SOURCE: `architecture/generational_transition_v30.md` (whole doc)
- CATEGORY: mechanism / derivation
- SUBSTANCE: On PC death/retirement, every tracked value is classified: **PRESERVE** (world state: faction stats, clocks, NPC dispositions toward others, territory control), **TRANSFORM** (one Legacy Conviction + Resources at floor(prior/2)+new-starting), **RESET** (Disposition-toward-PC, Standing, Coherence, Skills — "new person, new relationships"), **BREAK** (Knots rupture, companion bonds end), **TRANSFER** (Obligations move to the new character's faction — "the institution remembers even if the individual doesn't"; Renown resets but predecessor's Renown≥7 grants a +1 head start).
- WHY IT MAY STILL MATTER: A clean, reusable taxonomy for "what does inheritance mean" that's more precise than a single "carries over / doesn't" binary — directly matches the brief's call-out for inheritance mechanics.
- STATUS IN DOC: no explicit status line (proposed §11 of player_agency_v30, per its own header) — functionally live given player_agency_v30 §10–11 cite and extend it.
- REDISCOVERED IN: single source; extended (not duplicated) by player_agency_v30 §10–11 Lineage Acts.

**F-G-16 — Two independent axes of player political power: faction-scoped Standing (0–7) and cross-faction Renown (0–10)**
- SOURCE: `architecture/player_agency_v30.md` §5.1, §5.3–§5.4
- CATEGORY: player-agency
- SUBSTANCE: Standing 0–7 gates faction-internal privilege (Petitioner→Regent-Designate; at 4+ can command NPC officers; at 7 succession-eligible). Renown is explicitly orthogonal — it persists across faction changes and even collapse, sourced from Conviction resolution, Domain Echoes, investigation, and governance success, capped +2/season. "Standing 5/Renown 3 = faction insider without cross-faction reputation. Standing 0/Renown 8 = independent operator with personal authority. Both are viable" — including a full independent-of-any-faction path (§5.3) that substitutes personal authority for institutional backing at Renown 7+.
- WHY IT MAY STILL MATTER: A precise, two-axis answer to "what may the player touch and what is refused" at the governance layer, including an explicit non-faction-aligned path.
- STATUS IN DOC: CANONICAL (approved 2026-04-17).
- REDISCOVERED IN: single source; cross-referenced by settlement_layer_v30 §6.1 (not in my lane) for governance-scope mapping.

**F-G-17 — The Ministry of the Peninsula: a non-faction institutional actor (no Mandate/Military/Wealth)**
- SOURCE: `provincial/factions_personal_v30.md` §8.9b; `provincial/faction_canon_v30.md` §11
- CATEGORY: ontology
- SUBSTANCE: An "institutional actor," not a faction — Influence 4/Stability 5 only, no Mandate/Military/Wealth/Intel. Administers roads, census, land records, and inter-territorial communication; predates the current faction structure and "prevents Valoria from collapsing into feudal anarchy." Has its own settlement-level priority tree and a Thread-artifact tie-in (the Deep Archives).
- WHY IT MAY STILL MATTER: Answers "does everything with political weight have to be a faction?" — no; this is a clean template for background administrative infrastructure that outlives any one faction's rise or fall.
- STATUS IN DOC: CANONICAL (factions_personal_v30 §8.9b is part of a CANONICAL doc).
- REDISCOVERED IN: named consistently in faction_canon_v30 §10–11 ("treated as institutional infrastructure, not a faction").

**F-G-18 — Catastrophic world-state failure produces a new chapter, never a game-over screen**
- SOURCE: `provincial/victory_v30.md` §5 (line 538–625)
- CATEGORY: world-churn / governance
- SUBSTANCE: "No shared loss. No fade to black. Every crisis becomes a new chapter." MS=0 (substrate tear) suspends faction acquisition 3 seasons but opens a personal-scale "Post-Calamity Era" where accumulated relationship/Thread capital outweighs broken institutions. IP=100 triggers a 3-phase, reversible Altonian invasion with named repulsion paths (military/diplomatic/resistance). All-factions-dissolved triggers an "Anarchy Era" with a defined re-formation path back to Parliament quorum.
- WHY IT MAY STILL MATTER: A strong structural principle for strategic-layer failure states generally — total system collapse is designed as a mode-shift, not a loss condition, which is unusual and reusable.
- STATUS IN DOC: Doc header flags most faction-specific §3 material SUPERSEDED-BY GD-1, but §5 (World-State Transitions) is not among the struck sections and is not itself marked superseded.
- REDISCOVERED IN: single source.

**F-G-19 — Fail Forward: complications are mandatory on Failure, player-chosen on Partial, and action-type-proportionate**
- SOURCE: `provincial/fail_forward_pp177.md` §1–§3, §7
- CATEGORY: mechanism / problem-only-turned-solved
- SUBSTANCE: Named gap: "Failure outcomes... produce only a wasted action slot — no complication, no state change." Fix: every Domain Action type gets a Partial complication (player picks 1 of 2 minor costs — preserving agency) and a Failure complication (mandatory, moderate). Explicit canon-compliance table ties this to "P-08 no null-outcome loops."
- WHY IT MAY STILL MATTER: A general-purpose pattern for preventing action-repetition stalemates in any resolution system with failure states.
- STATUS IN DOC: WORKING DESIGN — not yet committed.
- REDISCOVERED IN: single source; the same principle (no static repetition on failure) is independently visible in the resolver-migration rationale throughout faction_layer_v30 (ED-865/874 notes on removing "small-pool ratification walls").

**F-G-20 — Restoration Movement models an explicit alternative governance ontology: node-based consensus vs. hierarchy**
- SOURCE: `architecture/campaign_architecture_v30.md` §2.1–§2.3
- CATEGORY: ontology / faction
- SUBSTANCE: RM's political program is Einhir governance restoration: "node-based meritocratic consensus cells... utopian anarchism structured as a self-governing network," explicitly NOT hierarchical Standing-ladder governance, and RM itself disbelieves Threadwork is real even though its consensus-node sites are literal Threadweaving sites — a designed dramatic irony with a 3-branch resolution arc (Embrace/Denial/Schism) when the truth becomes public.
- WHY IT MAY STILL MATTER: The corpus's one deliberate counter-example to "faction = hierarchy," useful for checking whether any revived faction model can actually represent non-hierarchical governance.
- STATUS IN DOC: doc header CANONICAL (approved 2026-04-17); no internal supersession found within my lane's files, though Cultural Reformation (an RM mechanic named alongside it) was struck (see Dead Ends).
- REDISCOVERED IN: single source.

**F-G-21 — Consecration Crisis: legitimacy is a resolved variable, not a flag, contingent on a rival institution's own strength**
- SOURCE: `provincial/baralta_crown_claim_v30.md` §3–§4
- CATEGORY: governance
- SUBSTANCE: When Hafenmark wins a Crown Succession Contest, whether the new monarch is "legitimate" is resolved by checking Church Stability at that instant: ≥4 → refusal (unconsecrated rule, severe Mandate penalty, but validates permanently after 3 clean seasons); ≤3 → consecration under duress (Church subordinated, CI −5). The doc runs three simulated timing scenarios (early/mid/late-game) and concludes mid-game is the claimant's "optimal window" — legitimacy is a race condition against the rival institution's own decay curve, not a static check.
- WHY IT MAY STILL MATTER: A concrete worked model of contested legitimacy that ties two factions' internal states together rather than resolving unilaterally — directly useful if crown-claim/legitimacy mechanics are rebuilt.
- STATUS IN DOC: DESIGN (editorial decision, flagged for review) — never promoted to CANONICAL; generalized/subsumed by faction_succession_split_v30 (F-G-6) which is itself only PROVISIONAL.
- REDISCOVERED IN: single source; faction_succession_split_v30 explicitly names this as the special case it generalizes.

**F-G-22 — Three-scale bidirectional conflict architecture: Settlement is the "engine layer," Peninsula is the "consequence layer"**
- SOURCE: `architecture/conflict_architecture_proposal.md` "Core Insight," "The Three Scales"
- CATEGORY: ontology
- SUBSTANCE: Peninsula/Province/Settlement are named as consequence/contest/engine layers respectively, with an explicit stated resolution order each season (Settlement→Province→Peninsula) — infrastructure resolves first, so "the real game happened two resolution phases earlier" than what the peninsula map shows. The doc's diagnosis of a stalled early game: "The starting settlement map already contains five governance disputes. The game starts on fire. The design just didn't know it" — i.e., the fix wasn't a new system, it was recognizing latent friction already authored at the lowest scale.
- WHY IT MAY STILL MATTER: A useful structural claim about WHERE to look for governance drama (bottom scale, not top) that's easy to lose if a rebuild starts from the peninsula map down.
- STATUS IN DOC: CANONICAL.
- REDISCOVERED IN: single source; consistent with (not duplicating) scale_transitions_v30's "Domain Echo" bottom-up write path.

### DEAD ENDS

- **Peninsular Partition / Co-Victory Pairings** (`victory_v30.md` §0.1, §4) — entire alliance-stalemate co-victory system marked `[SUPERSEDED-BY: GD-1]`, struck 2026-05-17 by canon ruling GD-1 (peninsula-only victory). Content kept only as supersession-trail evidence.
- **Varfell Path B "Southernmost Dominion"** (`varfell_path_b_v30.md`, whole doc) — an entire alternate faction-specific victory path, struck absolutely by the same GD-1 ruling, "including all conditional and calamity-healed variants."
- **VTM (Vaynard Thread Mastery) + Cultural Reformation** — struck 2026-04-19 ("a placeholder mechanic with no canonical advancement rule"; Cultural Reformation "incompatible with Vaynard's identity" as a pure military conqueror). Independently rediscovered as struck across `faction_layer_v30` §1.5, `victory_v30`, `varfell_path_b_v30`, and `factions_personal_v30` — four separate documents patched to remove the same mechanic, a strong signal it was genuinely load-bearing before the strike.
- **Niflhel** (the "Shadow Network" faction) — dissolved per `CR-STRIKE-2026-04-19 + PP-DISSOLVE`, struck consistently across `faction_layer_v30` §4.1/§5.8, `faction_politics_v30` §2.6, `faction_state_authoring_v30` §9, and `victory_v30`. Residual influence redirected to a settlement-broker mechanic instead of a faction seat.
- **"7-stat" faction lineup with faction-level Legitimacy/Popular Support** — superseded 2026-05-30 (LPS-1→LPS-2e) once it was shown to produce nonsensical results for a small-but-loyal faction (see F-G-2). The stat schema conflict between `factions_personal_v30` (6-stat) and `stats_1_7_scale.md` (7-stat) is explicitly resolved in favor of 6-stat + per-settlement L/PS.
- **Old succession "split if roll-margin < 2"** — superseded by the two-stage deterministic-gap resolver (F-G-6) because it let a single dice swing decide realm fragmentation ~50% of the time regardless of actual power balance.
- **"Treated as Ob 4" Stability death-spiral floor** — measured non-functional (see F-G-5), replaced by a deterministic floor.

### OPEN QUESTIONS NEVER ANSWERED

- **Church stat discrepancy (BLOCKING):** `franchise_v30.md` §8 flags `stats_1_7_scale.md` (Church L=5/PS=5/W=5) against `ValoriaDataLibrary.gd` (L=4/PS=4/W=3) as three conflicting values, explicitly "needs Jordan decision before Godot implementation." No resolution found anywhere in my lane's files.
- **Treaty Expiration's own flagged items** (`treaty_expiration_v30.md` §8): violation-magnitude ratification, and whether the 90%/arc lapse rate should be replaced by an "active-maintenance" alternative — both explicitly deferred to "Pass 2k," which I found no evidence ever occurred in this lane.
- **Parliamentary Transfer's own flagged items** (`parliamentary_transfer_v30.md` §8): mode-specific narrative effects and the vote-bloc pool modifier are marked "Jordan ratify, revise, or strike" — same unresolved Pass 2k dependency.
- **Franchise's "caste reform event" hook** (`franchise_v30.md` §5.1, §8): a named +1-Franchise trigger for anti-caste play is left "TBD — requires Altonian hooks system design," never authored.
- **Balance smoke-tests never run:** `faction_layer_v30.md` §10 defers "Stability recovery pace" and "Blockade+Embargo Guilds/Hafenmark collapse rate" to an "engine_v4 smoke-test" — no evidence in this lane that engine_v4 or the test exists.
- **Player-led succession contender:** `faction_succession_split_v30.md` §6 flags that if the PC is a contender, "specific mechanics [are] deferred — scene-layer scope" — never resolved.
- **RM Settlement Emergence 4-season cooldown:** explicitly flagged as "smoke-test balance" unresolved in the same document — too slow risks suppression winning, too fast risks RM cascading, and no test result is recorded.
- **Multi-root cascade** (`faction_behavior_v30.md` §3.2.2): Crown/Church/Varfell's parallel institutional sub-hierarchies are specified but deferred to "Stage 10 sim observation" for whether multi-root should replace the single-root default — not found resolved anywhere in this lane.