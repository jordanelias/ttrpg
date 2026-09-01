## LANE L — THE SCENE AND THE SEASON ECONOMY

### COVERAGE
files_assigned: cross-cutting search, no fixed subset (whole 819-file snapshot in scope) | files_opened: ~26 | files_read_closely: 12
skipped: `designs/arcs/*` (arc content, no scene-economy numbers) — grepped, none hit; `designs/provincial/faction_*` beyond `npc_behavior_v30.md` §8 — faction *stats* are other lanes' subject, I only pulled the NPC action-economy seam; the 51-scenario `19_v1_1_validation_report.md` and `21_v1_2_specification_revisions.md` (2026-04-28 session) — opened via grep only, their content is downstream of the R-39 stress test I already extracted; UI docs (`valoria_ui_ux_v4*`) — grepped for citations only, they're presentation not mechanism.

### NUMBERS TABLE (every number found, with citation and stated justification)

| # | Number | What it governs | Citation | Stated justification |
|---|---|---|---|---|
| 1 | **3 / 4 / 5** scene actions per season, by difficulty (Hard/Normal/Narrative) | Player's per-season action budget | `designs/architecture/player_agency_v30.md` §6.1 (table, L440-444) | "Narrative is about comfort... Hard is about triage... the game's tension scales with the gap between opportunities and actions" |
| 2 | **7-9 / 5-7 / 4-5** opportunities per Scene Slate, by difficulty (inverse of #1) | Slate size, always exceeds the budget | same, §4.3 (L297-302) and §6.1 table | "The surplus is the point" — unpursued opportunities resolve via NPC AI (L304) |
| 3 | **+1** scene action at Standing 4-5 (Lieutenant/Senior); **+2** at Standing 6-7 (Inner Circle+) | Stature-based budget modifier | §6.2 (L450-451); also §5.1 table L369,371 | reward for institutional stature |
| 4 | **+1** scene action in a Knotted NPC's territory | modifier | §6.2 (L452) | "the relationship opens doors that save time" |
| 5 | **-1** if Stamina 0 (Out of Breath); **-1** if 2+ Wounds | modifier | §6.2 (L453-454) | physical/injury logic, unexplained further |
| 6 | **1-3** mechanical interactions per scene; extended scenes cost **2** scene actions | scene↔action granularity | §6.3 (L456-458) | efficiency-dependent |
| 7 | Scene **time budget = 3** (within a single scene), adjustable by Stamina/Wounds; **1** time unit per node interaction | nested sub-budget inside investigation-graph scenes | `designs/scene/investigation_systems_v30.md` L158 | "not a new resource — it is the scene action budget expressed spatially" |
| 8 | **4-5 / 6-7 / 8-9** nodes per investigation scene-graph, by threshold (Simple/Complex/Structural) | internal structure of a scene | same, L152-154 | scales with investigation complexity |
| 9 | Max **3** Conviction-generated (Step 4) slate entries | slate-generation cap | `player_agency_v30.md` L275 | prevents over-triggering from ~25 keyword matches |
| 10 | Max **3** NPC Outreach entries/season; max **2** Demand entries/season | slate-generation cap | `player_agency_v30.md` §4.2 Step 5 / `designs/npcs/npc_behavior_v30.md` §8.11.5 (L946, L950) | "prevents inbox overload"; 1 of the 3 reserved cross-faction (ED-755) |
| 11 | Max **1** Thread-State scene per Slate | slate-generation cap | `player_agency_v30.md` L241 | — |
| 12 | **20-30** total Zoom-In trigger / scene-graph templates | authored-content target | `investigation_systems_v30.md` L199-211 | required to close ED-545 ("only 5 Zoom In triggers") |
| 13 | **±2** per faction attribute per season (seasonal cap, shared across modes) | interacts with, but distinct from, scene budget | `designs/architecture/campaign_modes_v30.md` L151 | "prevents hybrid mode from doubling attribute velocity" |
| 14 | **+2** Renown per season, cap | separate player-progress track | `player_agency_v30.md` §5.4 (L417) | — |
| 15 | **1** faction-level Domain Action per season, per NPC faction (top-firing branch of a 7-level priority tree) | the entire **NPC** "action economy" — categorically unlike the player's | `npc_behavior_v30.md` §8.1 (L770-782) | universal 7-level template; "Survival... Overrides all" |
| 16 | Post-mass-battle aftermath scene and the "Where Were You?" retrospective scene both cost **0** scene actions | explicit exceptions to the budget | `designs/provincial/mass_battle_v30.md` L867; `scale_transitions_v30.md` L156 | "it is the aftermath, and it is always worth experiencing" / "a free narrative moment" |
| 17 | **R-39 stress test:** 5 mandatory/Concern-driven scenes = **100%** of a 5-action budget, **0** discretionary actions left | budget-saturation failure mode, found and patched at the design stage | `designs/audit/2026-04-28-political-dynamics-session/15_stress_tests_batch3.md`, R-39 | flagged as a Robust/Smooth violation; patch downgrades Concern-Outreach from mandatory to deferrable |
| 18 | PCs grant **+1D**, once per season, to their faction's Domain Action in their physical territory | cross-scale presence bonus | `scale_transitions_v30.md` L278 | "mechanical expression of PC presence in the BG layer" |

### FINDINGS (ranked)

**F-L-1 — The Scene Slate is the whole answer to "why does a scene exist and how many do you get"**
- SOURCE: `designs/architecture/player_agency_v30.md` §4.1-4.3 (L173-302)
- CATEGORY: mechanism
- SUBSTANCE: At the start of each season's Personal Phase the engine deterministically generates a **Scene Slate** — 4-9 scene opportunities (by difficulty) drawn from seven priority-ordered generation steps (Mandatory Crisis → Crisis Events → Thread-State → Duty-Aligned → Conviction-Aligned → NPC Outreach → Territorial → Ambient), each entry carrying an NPC, a location, a one-sentence description, a generating tag, and a priority. The player has 3-5 scene actions (also by difficulty) to spend against that slate; a deterministic cross-step pruning algorithm (§4.3, step-by-step tie-break rules per generation step) trims the raw entry set down to slate size before the player ever sees it.
- WHY IT MAY STILL MATTER: This is the literal, load-bearing prior art for Jordan's "~5 playable scenes / ~5 actions" ruling — it already specifies the number, the generation algorithm, and the *reason* for triage (deliberate scarcity vs. surplus).
- STATUS IN DOC: `## Status: CANONICAL — approved 2026-04-17 (editorial batch acceptance)`
- REDISCOVERED IN: independently corroborated by `designs/audit/player_world_bridge_2026-04-16.md` §3.1 (dated one day *before* approval — this is the origin document), `designs/audit/settlement_bridge_unification_2026-04-16.md` §2.3, `designs/audit/valoria_workplan_final.md` L325-339, and `designs/ui/valoria_ui_ux_v4_1.md` L87-89 — five independently-authored docs converge on the identical 3-5 actions / 4-9 opportunities figures.

**F-L-2 — A scene is a container, not the atomic action; the action is "pursue this opportunity"**
- SOURCE: `player_agency_v30.md` §6.3 (L456-458), §4.4 (L326-336)
- CATEGORY: ontology
- SUBSTANCE: "One scene action = one scene opportunity pursued. A scene contains 1-3 mechanical interactions (a fieldwork action, a social roll, a combat exchange, a Thread operation)." A scene has no fixed internal turn structure of its own beyond that — resolution just chains existing subsystem actions (Read→Connect→Interview is the worked example) until the scene concludes. Scenes needing extended engagement cost 2 scene actions instead of 1.
- WHY IT MAY STILL MATTER: Directly answers the brief's ontology question — a scene is neither purely a pacing wrapper nor an atomic action; it's a variable-cost container whose *cost* (in the season-level currency) is what the player manages, while its *contents* are handled by whatever subsystem the scene invokes.
- STATUS IN DOC: CANONICAL (as above)
- REDISCOVERED IN: single source at the top-level, but the identical framing recurs fractally inside `investigation_systems_v30.md` (F-L-3, below), so the *pattern* is doubly attested even though the top-level number lives in one place.

**F-L-3 — The scene-action budget recurs one level down as a "scene time budget," and the doc says outright it is the same resource expressed spatially**
- SOURCE: `designs/scene/investigation_systems_v30.md` §"Traversal Economy" (L156-160), integration table L219
- CATEGORY: mechanism
- SUBSTANCE: Inside an investigation scene, the scene is a node-graph (4-9 nodes depending on Simple/Complex/Structural threshold). The player has a scene time budget of 3 (adjustable by Stamina/Wounds — the same modifiers as the season-level budget), and each node interaction costs 1 unit. The doc is explicit: "Moving between nodes costs time (not a new resource — it is the scene action budget expressed spatially)."
- WHY IT MAY STILL MATTER: This is a genuine structural insight independent of any one number: the corpus designed the season/scene/action hierarchy *fractally* — the same triage-under-scarcity shape repeats at the season level (slate vs. budget) and the scene level (node graph vs. time budget), deliberately reusing one mechanic rather than inventing a second currency.
- STATUS IN DOC: `## Status: CANONICAL — approved 2026-04-17`
- REDISCOVERED IN: single source, but explicitly cross-referenced to `player_agency_v30 §6` by name.

**F-L-4 — NPCs do not have a symmetric action economy — the player's per-season multi-slot budget has no NPC counterpart**
- SOURCE: `designs/npcs/npc_behavior_v30.md` §8.1 (L770-782), §7.9 (L1175)
- CATEGORY: ontology / npc
- SUBSTANCE: Every NPC *faction* runs exactly one action per season: a 7-level priority tree (Survival → Conviction-critical → Framework-opportunity → Institutional default → Conviction-secondary → Reactive → Pass) evaluated top-down, and whichever level fires first is the faction's *entire* action for the season. There is no "faction gets N actions, chooses among M options" structure — it is deterministic, one-shot, and the same 7-level template for every faction. A named individual NPC has no action-slot economy at all; their behavior is either subsumed in their faction's single roll, or (§8.11) they may *generate a Scene Slate entry* that costs the **player's** budget, not their own.
- WHY IT MAY STILL MATTER: This is the critical asymmetry finding the lane brief asked for. The budget was never stated as universal — it is explicitly player-only. NPCs are resolved by formula/priority-tree at the faction scale; only named NPCs "reaching out" ever touch the player's action economy, and even then it costs the player, not the NPC.
- STATUS IN DOC: CANONICAL
- REDISCOVERED IN: `designs/audit/2026-04-28-political-dynamics-session/06_iterative_test_audit_patch_critique.md` L290 independently calls this "NPCs have seasonal scene action budgets (Priority tree determines what actions they take)" while probing a *different, never-promoted* extension (individual NPC "Projects" gated on faction priority-tree "discretionary capacity") — i.e., a later session tried to give individual NPCs a real, player-like action economy and it never reached canon (see Dead Ends).

**F-L-5 — A live stress test found the exact number Jordan cited (5) can saturate to zero discretionary play**
- SOURCE: `designs/audit/2026-04-28-political-dynamics-session/15_stress_tests_batch3.md`, test R-39 ("Scene Slate Discretionary Budget — Does the Player Get Any?")
- CATEGORY: problem-only
- SUBSTANCE: Probing a mid-campaign (Year 4) season with 5 scene actions, the auditors found mandatory content alone (1 leader-crisis scene, 1 heresy-investigation scene, 3 Concern-driven NPC-Outreach scenes) consumes the *entire* 5-action budget, leaving **zero** left for investigation, Knot maintenance, Standing advancement, or any player-initiated agenda. The failure is filed as a Robust/Smooth violation ("NPCs always have the initiative — the player reacts... rather than directing their own political agenda"), with a proposed patch: demote Concern-driven Outreach from mandatory-feeling to explicitly deferrable, so missing it is "a deferred conversation," not a lost consequence.
- WHY IT MAY STILL MATTER: This is a direct, already-executed stress test of the number the current proposal is built around. It shows 5 is not automatically safe — the failure mode is specifically that *stacking* Priority 1-3 generation sources (mandatory + Concern-outreach) can crowd out all discretionary play, and that the fix that was found is a slate-generation policy change, not a budget-size change.
- STATUS IN DOC: filed as `## ROBUST` issue R-39-A/B in a document whose overall chain (`24_promotion_checklist_evaluation.md`) is `PROVISIONAL — BLOCKED ON JORDAN`, never promoted.
- REDISCOVERED IN: single source, but the underlying mechanism it stress-tested (NPC Outreach at Priority 3, capped at 3/season) *did* reach canon per F-L-6, so the failure mode is live against the current design even though the stress-test's own patch never was formally ratified.

**F-L-6 — Named NPCs are the World→Player bridge; they generate slate entries, they never spend player-like actions themselves**
- SOURCE: `npc_behavior_v30.md` §8.11 (L895-961)
- CATEGORY: mechanism / npc
- SUBSTANCE: "Each season, after the NPC priority tree fires its faction-level action, each named NPC evaluates whether to generate a personal-level Scene Slate entry for the player. This is the World→Player bridge... the world's actors do not wait to be approached." Outreach fires at Disposition ≥+2 + relevant active Conviction + a priority-tree action this season that "could benefit from player involvement"; Demand fires the mirror-negative condition. Capped at 3 Outreach / 2 Demand per season, with a cross-faction floor reserving at least 1 Outreach slot so player-faction NPCs can't monopolize the surface (ED-755).
- WHY IT MAY STILL MATTER: Establishes explicitly that "the world doesn't wait" is implemented as *slate generation pressure on the player's budget*, not as any independent NPC action currency — reinforcing F-L-4's asymmetry as intentional design, not an oversight.
- STATUS IN DOC: CANONICAL, marked "(NEW — feeds player_agency_v30 §4.2 Step 5)"
- REDISCOVERED IN: precedent-critiqued and proposed nearly verbatim in `designs/audit/player_world_bridge_2026-04-16.md` §1.8 (L167-178, one day earlier) — "NPC Outreach system... NPC demands... NPC independent action visibility" — a clean case of a critique doc's proposal being canonized essentially as written the next day.

**F-L-7 — Mandatory-overflow is handled by "Witness Mode," not by silently dropping content**
- SOURCE: `player_agency_v30.md` §4.2 Step 1 (L207-218); `scale_transitions_v30.md` §4.3.2 (L140)
- CATEGORY: mechanism
- SUBSTANCE: When mandatory scene count exceeds the scene-action budget, the player picks which to attend personally; the rest resolve in Witness Mode — a free (0 scene-action cost) Read/Appraise roll at Ob 1 (not auto-success), one narrative-input opportunity at resolution, mechanical resolution via NPC AI as if declined, and explicitly **no** Domain Echo and **no** Momentum/Coherence change. `12_development_specification.md` L1546 adds a companion detail: Witness Mode caps information at "max 3 Read results per Accounting"; beyond that, narrative summary only.
- WHY IT MAY STILL MATTER: Gives a concrete existing answer for what happens when a chosen action-count (e.g. 5) is insufficient for a crisis-heavy season — the corpus already solved "not enough actions" without simply forbidding overflow or inflating the budget.
- STATUS IN DOC: CANONICAL (`ED-745` cites this as newly defined in the 2026-04-24 audit)
- REDISCOVERED IN: `designs/audit/bridge_part1_revisions.md` L73 restates the same rule near-verbatim.

**F-L-8 — Season structure is a fixed 5-6 phase sequence, independently reconstructed by at least four documents**
- SOURCE: `player_agency_v30.md` §7.2 (L484-491); `player_world_bridge_2026-04-16.md` §3.1 (L262-278); `settlement_bridge_unification_2026-04-16.md` §2.3 (L276-291); `valoria_workplan_final.md` L325-339
- CATEGORY: ontology
- SUBSTANCE: Phase 0 Briefing (3-5 top world changes) → Phase 1a Duty Assignment → Phase 1b Scene Slate Generation → [Phase 1c Governor Action, settlement-layer addition only] → Phase 1c/1d Personal Phase (3-5 scene actions) → Phase 2 Strategic Phase (Domain Actions) → Phase 3 Accounting (clocks, Domain Echo, Standing, Belief/Conviction review, Renown) → Phase 4 Aftermath (free companion conversation, 0 action cost).
- WHY IT MAY STILL MATTER: This is the season "container" the ruling's "~5 scenes per season" sits inside — a season is not an unstructured pool of time, it's phase-gated, and the scene-action budget applies to exactly one phase (Personal Phase) sandwiched between world-generation (Slate) and world-reaction (Strategic Phase, Accounting).
- STATUS IN DOC: `player_agency_v30.md` CANONICAL; the other three are audit/workplan docs (no independent status line) that converge on the identical structure without visibly citing each other for the numbers.
- REDISCOVERED IN: four-way independent convergence, the strongest rediscovery signal in this lane.

**F-L-9 — "Scene Slate" and "Season Slate" are the same mechanism under two different names**
- SOURCE: `designs/architecture/videogame_mode_spec.md` L18, L104 ("Season Slate"); `player_agency_v30.md` §4 title ("Scene Slate")
- CATEGORY: seam
- SUBSTANCE: The videogame-mode collapse document — the doc whose entire job is to be the single reference the Godot implementer reads — twice calls the identical mechanism "Season Slate" while citing `player_agency_v30 §4`, which itself is titled "Scene Slate." `integration_proposal_v30.md` L274 uses "Season Slate" too.
- WHY IT MAY STILL MATTER: Minor but concrete terminology drift on the exact mechanism this lane is about — worth flagging so a re-derivation of the concept doesn't treat these as two different systems.
- STATUS IN DOC: none marked; simply inconsistent naming across otherwise-canonical docs.
- REDISCOVERED IN: independently in both `videogame_mode_spec.md` and `integration_proposal_v30.md`.

**F-L-10 — Every mechanical subsystem has its own within-scene resource; the scene-action budget is deliberately the *only* between-scene resource**
- SOURCE: `designs/architecture/integration_proposal_v30.md` L202-204
- CATEGORY: derivation
- SUBSTANCE: Responding to a critique proposing a new "Acuity" resource for investigation, the doc states the design is already complete and symmetric: Combat→Wounds/Stamina, Contest→Composure/Concentration, Thread→Coherence, Fieldwork→Exposure — each is a *within*-scene depletion resource — while "the scene action budget handles the between-scene resource limit" uniformly across all of them. Explicitly rejects adding a second between-scene resource: "Introducing Acuity... would double-penalize investigation — once through the scene action budget and once through the Acuity drain."
- WHY IT MAY STILL MATTER: A clean architectural rule for anyone re-deriving the scene economy today: exactly one currency governs "how many scenes," and each subsystem is free to have its own currency for "how deep can I go once I'm in one" — conflating the two was explicitly considered and rejected.
- STATUS IN DOC: no explicit status marker (design-proposal doc), but the resolution is stated as settling a named prior critique (the "RSE critique").
- REDISCOVERED IN: single source.

**F-L-11 — The scene action budget is explicitly named as the resolution of two open editorial items (ED-545, ED-547)**
- SOURCE: `player_agency_v30.md` §8 (L513-527), §7.4 (L497-501)
- CATEGORY: derivation
- SUBSTANCE: The Scene Slate is stated to structurally solve ED-545 ("only 5 Zoom In triggers" — "any game state change that would be interesting to experience personally becomes a scene opportunity"), and the scene action budget is stated to resolve ED-547 ("Fieldwork resource cost" — "each investigation scene costs a scene action that could have been spent elsewhere. Scene action budget IS the fieldwork cost").
- WHY IT MAY STILL MATTER: Shows the scene-action number wasn't picked in a vacuum — it was explicitly load-bearing on closing two other named design debts simultaneously. Any redesign of the number needs to re-check both.
- STATUS IN DOC: CANONICAL
- REDISCOVERED IN: single source (self-referential across its own §7 and §8).

**F-L-12 — Companions explicitly do NOT consume the player's scene-action budget**
- SOURCE: `designs/audit/integration_audit_v1_2026-04-15.md` L84; `integration_audit_v2_2026-04-16.md` L85
- CATEGORY: derivation
- SUBSTANCE: "The critical design question is: do companions consume the player's scene action budget? The answer must be no... A companion contributes to scenes as a distinct actor within the scene's time budget." Companions instead assist per fieldwork_v30 §3.2 (Ob+1 assist roll, success adds +1 net success, failure adds +1 Exposure for both).
- WHY IT MAY STILL MATTER: A clean precedent if the current proposal needs to decide whether party members/allies eat into the same 5-action pool as the protagonist — this corpus already answered no, and gave a specific mechanical alternative rather than just asserting it.
- STATUS IN DOC: resolved across two audit passes, second one explicitly closing "the redundancy identified in the critique" from the first.
- REDISCOVERED IN: two-document convergence within the same audit lineage (v1→v2, same author chain, still counts as the question being independently re-litigated and re-confirmed).

### DEAD ENDS
- **NPC "Projects" / individual discretionary-action-capacity economy** (`designs/audit/2026-04-28-political-dynamics-session/`, "doc 12" v1.2.1, commit `52fb1292`): a fully-vetted (68 stress-test issues, 51 simulation scenarios, 39 patches) proposal to give *individual* named NPCs a player-like action economy gated by their faction's priority-tree "discretionary capacity." Its promotion-checklist evaluation (`24_promotion_checklist_evaluation.md`) records the verdict explicitly: **3 PASS, 2 BLOCKED ON JORDAN, 1 FORMAT GAP, 1 NOT DONE — never promoted to canonical.** Only the narrower "NPC Personal Outreach Generation" slice of this work (§8.11) made it into `npc_behavior_v30.md`; the deeper individual-NPC-agency model did not. Anyone building an NPC-side action economy today is not starting from zero — this is the closest attempt, and it stalled on two Jordan-only design calls that were never made.
- **R-39's own proposed patch** (demote Concern-Outreach from mandatory-feeling to deferrable) was written inside the same never-promoted "doc 12" chain — so while the *problem* it found (budget saturation at 5 actions) is real and reproducible against canon, its specific *fix* was never ratified either.

### OPEN QUESTIONS NEVER ANSWERED
- **Whether Belief/Conviction-text keyword scanning for Scene Slate Step 4 needs structured tags or free-text NLP.** `designs/audit/comprehensive_system_audit_2026-04-15.md` §1.2 (CS-1) flags free-text scanning as fragile for a videogame and proposes mandatory tag fields at Belief-authoring time; the final `player_agency_v30.md` §4.2 Step 4 ships a ~25-keyword free-text scan with a capitalization-based validator instead — it's not clear from this lane's files whether that was a deliberate rejection of the tag-field proposal or the proposal simply never got reconciled back into the doc.
- **Whether the 3/4/5 difficulty-scaled budget survives contact with a single fixed videogame difficulty**, i.e. whether "Normal=4" or some other rung is what a shipped, non-adjustable-difficulty game would actually use — none of the files in this lane state a single canonical default outside the three-difficulty table.
- **NPC Standing mobility** (`15_stress_tests_batch3.md` R-40): whether individual named NPCs' institutional Standing can rise or fall during a campaign is flagged as unspecified and patched only inside the never-promoted "doc 12" chain — the live `npc_behavior_v30.md` has no NPC-standing-mobility rule, only the player's.