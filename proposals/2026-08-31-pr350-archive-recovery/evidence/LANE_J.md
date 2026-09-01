## LANE J — Cross-System Syntheses, Bridges & Throughlines

### COVERAGE
files_assigned: 33 | files_opened: 33 | files_read_closely: 25

skipped (out-of-scope subject or low marginal yield, headers/structure only checked):
- `rigorous_audit_synthesis_s1_s7_v3_1.md`, `gameplay_assessment_2026_04_21.md`, `mechanical_implications_revised_2026_04_21.md`, `mechanical_implementation_revised_2026_04_21.md`, `editorial_ein_sof_gradient_2026_04_21.md` — all Thread/metaphysical-ontology throughlines (T-26..T-41, М-7..М-11); brief's five subjects are NPCs/world/factions/settlements/governance, and these touch none directly.
- `simulation_review_2026-04-15.md`, `ecosystem_workplan_v2_2026-04-30.md` — test-inventory and repo-tooling workplans respectively, content is process not design.
- `valoria_how_to_play.md` — procedural walkthrough; its season-cycle structure is fully subsumed by `settlement_bridge_unification_2026-04-16.md` §2.3, already extracted.
- `label_audit_2026-04-19.md` (read in full) and `ecosystem_workplan_2026-04-30.md`'s content-findings table (read in full) — both are file-hygiene/repo-tooling; zero yield for the five subjects.

---

### FINDINGS (ranked)

**F-J-1 — The two-layer diagnosis: World Physics vs. Player Physics**
- SOURCE: `player_world_bridge_2026-04-16.md`:9-22
- CATEGORY: ontology
- SUBSTANCE: "Valoria has two complete, internally excellent design layers. They are not connected." Layer 1 (faction stats, clocks, NPC priority trees, territory ecology) runs on its own logic and "does not care about the player"; Layer 2 (player agency, fieldwork, combat, contests) describes only what the player does. The translation layer existed only "in fragmentary form across six documents written in parallel, never unified, and partially contradictory," with three named bridge mechanisms (Domain Echo, Scene Slate, Dialogue Lattice) each specified at different completeness levels.
- WHY IT MAY STILL MATTER: This is the exact "how does personal action reach the strategic layer, and vice versa" question the brief asks about, stated as a first-principles diagnosis before any patching — a clean frame for auditing whatever the current design does today.
- STATUS IN DOC: "WORKING DOCUMENT — launchpad for revision work"
- REDISCOVERED IN: single source (subsequent bridge docs build on it rather than re-deriving it)

**F-J-2 — Province Accord becomes a derived value, never set directly**
- SOURCE: `settlement_bridge_unification_2026-04-16.md` C-02, §2.1
- CATEGORY: derivation
- SUBSTANCE: Before settlements, Accord (0-4) was a per-territory stat that Domain Echo and player actions modified directly. The unification changes this: all personal-scale Accord pathways now target **settlement Order** instead, and "Province Accord updates automatically at Accounting via the floor(mean(Order)) formula... Province Accord is always derived — never set directly by personal action." Concrete edge-case rule: ties broken by giving the Seat settlement's Order +1 weight (`gap_resolution_2026-04-19.md` ED-SETT-03).
- WHY IT MAY STILL MATTER: Textbook instance of the brief's "X must be derived, never stored" pattern — a genuine architectural improvement (single source of truth, no desync) independent of whether "settlements" survive as a layer.
- STATUS IN DOC: "ADOPTED" (editorial resolution, authority explicitly granted)
- REDISCOVERED IN: single source, but the propagation *failure* of this exact change is independently flagged later (see F-J-9)

**F-J-3 — Faction design is deliberately "hybrid asymmetric," and this is named as the strongest architectural element**
- SOURCE: `2026-05-16-faction-ners-all-directions.md` §5.6 H-1
- CATEGORY: faction / ontology
- SUBSTANCE: A symmetric layer (seven-stat surface, four-component Mission/Cascade/Public-Expectation/Legitimacy+Support model, one Accounting cycle, one DA-Ob formula) is shared by all factions; an asymmetric layer (six distinct roles, one Unique Action per faction, distinct starting distributions, role-specific tracks like CI/VTM) differentiates them. Verdict: "pure symmetric... fails М-4 (reskinned attractor failure)... pure asymmetric... fails Q-smooth... Hybrid asymmetric → right," explicitly likened to how "the Medici, Papacy, French Crown, Hanseatic League all played the same game... but with deeply asymmetric mechanism access."
- WHY IT MAY STILL MATTER: A crisp, reusable design principle for any redesign of faction mechanics — names *why* the shared-stats-plus-unique-actions shape is correct rather than arbitrary.
- STATUS IN DOC: PROVISIONAL (audit output), verdict "ALIGNED with research... preserve"
- REDISCOVERED IN: single source

**F-J-4 — Five of six faction roles lack a "turn on you" failure mode**
- SOURCE: `2026-05-16-faction-ners-all-directions.md` §5.6 H-2, §8 A-4; unresolved per `2026-05-16-faction-audit-phase-1-verification-outcomes.md` §6 (A-4 "unchanged")
- CATEGORY: faction / problem-only
- SUBSTANCE: Only Löwenritter has an asymmetric-vulnerability mechanic (Martial Law / Coup Trigger — the tool that becomes the threat). Crown (bureaucracy-independence → coup), Church (CI-driven schism), Hafenmark (wealth-accumulation → oligarchic capture), Varfell (intel dominance → paranoid purges), and Restoration Movement (movement-success → institutional rigidity) have no analogous "your strength becomes your weakness" mechanic, despite this being a load-bearing Renaissance dynamic (T-7: "every tool can be turned against the user").
- WHY IT MAY STILL MATTER: A specific, still-open, evidence-grounded gap with a named shape for each of five factions — directly implementable if factions are revisited.
- STATUS IN DOC: P2 PROPOSE, confirmed still open as of the Phase-1 verification pass
- REDISCOVERED IN: single source

**F-J-5 — Regime-relative category mutation (private war → treason) is structurally absent**
- SOURCE: `2026-05-16-faction-ners-all-directions.md` T-3, A-7 / candidate М-12; unresolved per verification-outcomes §8 (D-2.1 "unchanged")
- CATEGORY: faction / governance / problem-only
- SUBSTANCE: Faction Mission-shift produces *within-faction* reinterpretation (a Domain Action can flip legitimate↔illegitimate as one faction's own Mission changes), but there is no mechanism for **cross-faction** legal reclassification — the largest identified Renaissance dynamic ("centralization rewrites what was lawful," e.g. a crown declaring private war treason as it consolidates) with no canonical home.
- WHY IT MAY STILL MATTER: Named explicitly as "the largest Renaissance dynamic structurally missing" and flagged to Jordan as an open decision that was never closed in this corpus — a genuine unsolved design problem with real value if governance/legitimacy mechanics are extended.
- STATUS IN DOC: flagged, decision pending ("admit candidate М-12 OR document scope-bound... OR scope-bound deliberately")
- REDISCOVERED IN: single source

**F-J-6 — Intelligence stat: struck, diagnosed as broken, restored with concrete formulas**
- SOURCE: `faction_stats_renaissance_review.md` (2026-04-28); confirmed adopted per `2026-05-16-faction-ners-all-directions.md` §1 ("Intel restored per PP-686 v2... per faction_stats_renaissance_review.md recommendations")
- CATEGORY: mechanism / derivation
- SUBSTANCE: Striking Intel broke the Spy Ob formula (`floor(target Intel/2)+1` referenced a dead stat) and flattened Varfell's identity to 4/4/4/4/4. The review specifies restoration with concrete mechanics: defensive counter-espionage roll, Intel-driven offensive pool, a strategic-fog rule ("without successful Intel action, enemy faction stats are hidden"), and per-faction starting values (Crown 3, Church 4, Hafenmark 3, Varfell 5, Löwenritter 2, Guilds 4).
- WHY IT MAY STILL MATTER: A worked example of a design regression being diagnosed with root-cause precision (a live formula bug, not just "feels wrong") and a recommendation that was later actually adopted — rare in this corpus.
- STATUS IN DOC: recommendation, later confirmed executed
- REDISCOVERED IN: single source (citation trail, not independent)

**F-J-7 — The R6 "death spirals" were simulation artifacts of an uncommitted branch, not canon defects**
- SOURCE: `2026-05-25-r6-death-spiral-reconciliation/findings.md` F1-F4
- CATEGORY: derivation / mechanism
- SUBSTANCE: A prior session reported two "death spirals" (Hafenmark Military, Tension band L) from an unpushed branch. Reconciliation against main HEAD found: main's N=100 simulation matches canon target *exactly* (Crown 40.0/Church 5.0/Hafenmark 1.0/Varfell 54.0 vs. R6's drifted 37/11/0/52), and the specific drain locations the handoff cited (`faction_action.py:420/454`, "§4.3 Turmoil 3-4 drains L−0.25/season continuously") do not exist anywhere in the codebase — grep-verified absent. The real, still-unimplemented canon mechanics are named precisely: battle-loss Military −1 (§B.3), battle→MS drain capped at −3/season (§E.1/E.4), and a probabilistic Mandate-vs-Ob check at Turmoil 3-4 (§4.4, not a continuous L-drain) — closing any of which would require re-tuning main's calibrated balance from scratch.
- WHY IT MAY STILL MATTER: A model case for how to adjudicate a "the world feels broken" claim: reproduce against main, verify the claimed mechanism actually exists in code, and distinguish "unimplemented canon" from "buggy canon." The three named gaps (Mil drain, MS drain, Mandate-check) remain real backlog items.
- STATUS IN DOC: "Main is the canonical-baseline-of-record... No patches in this audit."
- REDISCOVERED IN: single source

**F-J-8 — "Every institution has a face, every consequence has a scene, every actor has a tempo"**
- SOURCE: `integration_audit_v2_2026-04-16.md` Part 1 (Three Presence Rules)
- CATEGORY: governance / ontology
- SUBSTANCE: Three load-bearing premises stated as the test any proposed governance/NPC mechanic must satisfy: no Domain Action or clock advances "without a person attached to it in the player's experience"; every stat change is anchored to either a witnessed scene or a human-terms report ("Baralta used the evidence you delivered. Himlensendt's motion failed."); every institutional actor (Ministry officer, Warden, trader) has a discoverable seasonal/cyclical schedule that is itself investigative information.
- WHY IT MAY STILL MATTER: A compact, reusable acceptance test for "is this institution mechanically alive or just a stat modifier" — directly answers the brief's NPC/governance framing question and is explicitly self-described as "the document's most important design insight," originally buried, promoted to first position in the revision.
- STATUS IN DOC: none (design principle, not flagged provisional)
- REDISCOVERED IN: single source

**F-J-9 — Non-standard institutional actors need named engagement doors, not faction membership**
- SOURCE: `integration_audit_v1_2026-04-15.md` Part 4 (§4.2-4.6); protocol format standardized in `integration_audit_v2_2026-04-16.md` Part 3
- CATEGORY: governance / npc
- SUBSTANCE: Five institutional actors named in canon but with no player-engagement pathway are given full protocols: the **Ministry** (public-records access with no faction gate, restricted access gated by faction Mandate weight, a reform-pressure arc); **Guild individual leaders** (five domain leaders, each with a Conviction and a "Guild Favour" token that decays −1/2 seasons if not renewed); **Niflhel** as an information economy accessible to *any* player via a three-tier access ladder (Rumour → Brokerage → named Arm Leader), with the explicit shadow-cost that "using it means being in it" — a buyer becomes a recorded entry in Niflhel's own intelligence file; **Wardens**, whose two undefined tracks (WR "recognition," WC "cooperation") are given concrete thresholds (WR 0-5, WC 0-3, WC capped at ≤ WR); and **Restoration Movement** as a leaderless faction accessed only through Community Weaving.
- WHY IT MAY STILL MATTER: This is a full worked answer to "how does a non-faction-aligned player still touch governance" — the corpus's most systematic attempt to make every institution "reachable... through some path of genuine engagement" (Part 9's own summary).
- STATUS IN DOC: PROPOSAL, "requires explicit approval before integration into canonical documents"
- REDISCOVERED IN: single source (v1's protocols corrected and reformatted, not independently re-derived, in v2)

**F-J-10 — Founded Organization: the mechanism for player-formed factions, deliberately capped**
- SOURCE: `integration_audit_v2_2026-04-16.md` §2.2-2.3; ceiling question in §2.3 and `integration_audit_v1_2026-04-15.md` Appendix
- CATEGORY: governance / faction / mechanism
- SUBSTANCE: A three-stage progression — Companion (Knot-bonded) → recognized Network (2+ companions, 2+ other NPCs at Disposition ≥+2, shared Conviction theme) → Founded Organization, which requires **all three** of Evidence (a Structural-threshold investigation on the founding theme), Territory (≥3 network NPCs at Disposition ≥+2 in one place), and Duration (3 consecutive seasons of Network status) simultaneously. A Founded Organization gets one Domain Action/season keyed to its founding Conviction and a Mandate track (0-3) derived from summed member Disposition. Whether it can ever reach Universal Victory is explicitly left as an open design call: "leave it possible and not advertise it — an easter egg... not a designed primary path."
- WHY IT MAY STILL MATTER: Directly answers "can players form their own factions" with a concrete, gated mechanism rather than a yes/no, and the deliberate non-resolution of the victory-ceiling question is itself a durable open design fork.
- STATUS IN DOC: PROPOSAL
- REDISCOVERED IN: single source

**F-J-11 — Restoration Movement should be generated, not authored, as a faction**
- SOURCE: `comprehensive_system_audit_2026-04-15.md` §7.3; `valoria_holistic_audit.md` Part 4.5; `integration_audit_v1_2026-04-15.md` §4.6 (all same-day, likely one session cluster)
- CATEGORY: faction / ontology
- SUBSTANCE: RM has victory conditions but no card hand or priority tree in board-game mode. The proposed resolution: RM formalizes from an "NPE Coalition embryo" mechanic — territory-level Stance convergence around Thread/Piety issues crosses a size threshold and RM gains formal faction status (Mandate, Community Weaving as its Domain Action). Framed explicitly: "RM is the only faction that is generated rather than given... the cultural memory layer becoming organizational, not an institutional actor" (P-15 grounding).
- WHY IT MAY STILL MATTER: A structural claim of the brief's exact form — "this should never have been a designed object, it should emerge from primitives already in the engine" — and it's still unresolved (Jordan decision J-3, explicitly deferred "until videogame playtesting reveals whether latent-faction works").
- STATUS IN DOC: recommendation across three docs, decision deferred (J-3)
- REDISCOVERED IN: same-day cluster of three docs; not confirmed independent (likely one working session), but the convergence itself indicates the finding was considered obviously correct across passes

**F-J-12 — NPC Behavior is the system with the highest coupling risk in the whole architecture**
- SOURCE: `valoria_complete_system_audit.md` §4 (Interdependency Matrix), "Dependency Risk"
- CATEGORY: ontology / seam
- SUBSTANCE: An 18×18 read/write matrix across every major system shows NPC Behavior with the highest fan-in (read by 14 of 17 other systems) **and** highest fan-out (reads from 14 others), with bidirectional (R,W) coupling to Fieldwork, Contest, Threadwork, and Player Agency specifically. Conclusion stated directly: "A bug or design error in NPC Behavior propagates to 14 other systems. This is architecturally appropriate... but means NPC Behavior requires the highest test coverage and the most conservative change management."
- WHY IT MAY STILL MATTER: A structural map of *where* the NPC subsystem sits in the whole design — useful independent of whether the specific 18 systems named still exist, because it identifies NPC state as the connective tissue any redesign must treat conservatively.
- STATUS IN DOC: none (audit finding)
- REDISCOVERED IN: single source

**F-J-13 — The Accord-propagation gap: settlement Order derivation was never retrofitted into downstream consumers**
- SOURCE: `throughlines_transitions_hierarchy.md` Part 9 ("Accord propagation," P1); recorded again (same content, same flag ID) in `valoria_complete_system_audit.md` Consolidated Flags AUD-SET-02
- CATEGORY: seam / problem-only
- SUBSTANCE: After the settlement-bridge unification made province Accord a *derived* value (F-J-2), "all existing docs that reference 'Accord ±N' haven't been updated to route through settlement Order changes... downstream consumers still use the old direct-modification model." Named a P1 gap.
- WHY IT MAY STILL MATTER: A concrete, still-open instance of exactly the kind of "coupling failure that was never closed" the brief asks about — a real architectural migration left half-done, with the seam (old direct-Accord writes vs. new derived-Accord reads) explicitly named.
- STATUS IN DOC: P1, unresolved (not re-verified as closed in any later doc I read)
- REDISCOVERED IN: same finding recorded twice under the same flag ID (AUD-SET-02) — a compiled duplicate, not independent, but never marked resolved in either instance

**F-J-14 — A single revolted settlement can cap an entire province's Accord (degenerate averaging)**
- SOURCE: `valoria_complete_system_audit.md` Consolidated Flags, AUD-SET-01
- CATEGORY: settlement / mechanism / problem-only
- SUBSTANCE: Because province Accord = floor(mean(settlement Order)) (F-J-2), one settlement at Order 0 (Revolt) can mathematically drag a whole province's Accord down regardless of how well-governed its other settlements are — flagged tersely as "Order averaging → one revolt caps Accord."
- WHY IT MAY STILL MATTER: This is a real dynamics-failure risk of exactly the death-spiral family the brief asks about — a single local failure cascading into an aggregate that gates the victory condition — but flagged, not diagnosed or fixed, in this corpus.
- STATUS IN DOC: P2, unresolved
- REDISCOVERED IN: single source

**F-J-15 — Standing (institutional trust) has no coupling to Disposition with the faction leader**
- SOURCE: `integration_audit_v3_2026-04-16.md` GAP-09
- CATEGORY: governance / problem-only
- SUBSTANCE: Standing (0-5) advances/degrades purely on Duty completion/failure. A player can systematically antagonize their own faction leader in social contests — winning arguments against them, publicly contradicting faction priorities, driving their Disposition to −3 — "without losing a single Standing point, because their Duties are still being completed." Disposition tracks the relational cost but the two systems are never formally linked.
- WHY IT MAY STILL MATTER: A precise governance-legitimacy modeling gap — institutional trust and personal relationship are supposed to be the same underlying thing, and the mechanics currently let them diverge arbitrarily. Directly relevant to any "governance/legitimacy" rebuild.
- STATUS IN DOC: unresolved gap, no later doc in this lane records a fix
- REDISCOVERED IN: single source

**F-J-16 — Multiplayer Domain Echo has an unbounded faction-stat-stacking exploit**
- SOURCE: `integration_audit_v3_2026-04-16.md` GAP-07
- CATEGORY: faction / seam / problem-only
- SUBSTANCE: The ±2/season/stat Domain Echo cap is enforced **per character**, not per faction. In board-game multiplayer, N characters serving one faction can each independently hit the cap on the same stat in the same season — "3 characters can produce ±6... enough to move Stability from 3 to max in one season" — with no faction-level ceiling specified anywhere.
- WHY IT MAY STILL MATTER: A concrete balance hole in the exact mechanism (Domain Echo) that is the corpus's primary answer to "how personal action reaches the strategic layer" — the cap's stated purpose ("personal actions shouldn't dominate the faction layer") is defeated by coordination.
- STATUS IN DOC: unresolved gap
- REDISCOVERED IN: single source

**F-J-17 — Concrete Wealth-generation formula for Mine settlements**
- SOURCE: `gap_resolution_2026-04-19.md` §1.1
- CATEGORY: settlement / mechanism
- SUBSTANCE: Each Mine-type settlement generates `floor(Prosperity/2)` Wealth for its controlling faction **at Year-End Accounting only** (explicitly not per season, "because ore processing is slow"). Guild subnational management and a Trade Network token each add +1/year and stack; per-mine ceiling is 4 Wealth/year (Prosperity 5 base 2 + Guild 1 + Trade 1).
- WHY IT MAY STILL MATTER: One of the few places in this lane's material where a previously-flagged "gap" (mine income unspecified) was closed with an actual numeric formula rather than left as narrative texture — a template for how the corpus resolves this class of gap.
- STATUS IN DOC: CANONICAL, patch PP-667
- REDISCOVERED IN: single source

**F-J-18 — "Value proliferation": ~50-100+ tracked values is a named structural risk, independently flagged twice**
- SOURCE: `valoria_rse_critique.md` S06 ("100+ values... unwieldy at a table"); `player_world_bridge_2026-04-16.md` §2.1 ("The Legibility Problem," ~50 tracked values)
- CATEGORY: problem-only
- SUBSTANCE: The RSE critique (2026-04-15) computes the tracked-value count directly (5 stats × 4 factions + 4 tracks × 15 territories + peninsula clocks + faction-specific tracks ≈ 100+) and calls it the system's "Key problem." The bridge overview (2026-04-16), working independently on a presentation problem rather than a complexity audit, separately names "~50 tracked values" as "the game's greatest risk" per its own cognitive-load framing, and proposes a generated natural-language season briefing as the fix rather than reducing the count.
- WHY IT MAY STILL MATTER: Two different sessions, different vocabulary ("value proliferation" vs. "Legibility Problem"), same underlying diagnosis from different angles — a genuinely convergent, durable finding about UI/information-architecture debt that is independent of any single subsystem's fate.
- STATUS IN DOC: none (both are audit-native findings)
- REDISCOVERED IN: `valoria_rse_critique.md` and `player_world_bridge_2026-04-16.md` — genuinely independent framings

**F-J-19 — Accord ≥ 2 as universal-victory gate is the single best balance mechanic**
- SOURCE: `valoria_rse_critique.md` S07
- CATEGORY: governance / mechanism
- SUBSTANCE: Universal victory requires all territories at Accord ≥ 2; military conquest sets Accord to 1 on capture. This makes conquest self-defeating without any explicit "you can't attack" rule — a conqueror must then govern to ever win, "creating a natural pacing brake" as an emergent consequence of the stat system rather than a special-cased rule.
- WHY IT MAY STILL MATTER: A durable example of the brief's "mechanism that was designed... and still has value" — elegant because the constraint is structural, not scripted; worth preserving in any governance/victory redesign even if the specific numbers change.
- STATUS IN DOC: none ("Possibly the most elegant system at its scale")
- REDISCOVERED IN: single source

**F-J-20 — Löwenritter's internal Five Arms structure, and Community Projects — flagged uncertain provenance**
- SOURCE: `cross_conversation_review_2026-04-15.md` §2.1-2.2
- CATEGORY: faction / governance
- SUBSTANCE: Löwenritter has a differentiated five-arm internal structure (Lions' Table, Lions' Helm, Knights of the Peace, Royal Investigators, Riskbreakers), each with distinct stat and domain — notably, "Riskbreakers loyal to Valoria the concept, not the institutions" is named as a deliberate structural fault line the Coup arc exploits. A separate multi-season Community Projects system (Community Weave, Einhir Memory Recovery, Restoration Network, Fortification, Diplomatic Mission — each with duration/effect/disruption rules) is also recorded. Both are explicitly self-flagged: "may be from an earlier iteration... should be cross-checked against current design docs."
- WHY IT MAY STILL MATTER: The Riskbreakers-as-fault-line idea (an institution's own sub-faction being loyal to the abstraction over the institution) is a genuinely reusable governance-legitimacy device even if the specific five-arm table is stale; the Community Projects duration-mechanic is a template worth checking against whatever multi-season system exists now.
- STATUS IN DOC: self-flagged uncertain/possibly superseded, never resolved within this corpus
- REDISCOVERED IN: single source

---

### DEAD ENDS

- **The R6 handoff's specific claimed drain locations** (`faction_action.py:420`/`454`; "§4.3 Turmoil 3-4 drains L−0.25/season continuously") — explicitly refuted by grep against main HEAD: the file is 228 lines with no such call, and the actual section is §4.4 with a probabilistic Mandate check, not an L-drain. Killed by `2026-05-25-r6-death-spiral-reconciliation/findings.md` F2. Do not resurrect the numeric claim.
- **Pass-3 "outside-reviewer" findings A-15 (Wealth-generation absent), A-16 (Church-as-territorial-power absent), A-17 (offstage pressure absent)** — all three added by surface reasoning without file-fetch confirmation; all three CLOSED on first verification (`2026-05-16-faction-audit-phase-1-verification-outcomes.md` §2, §5): wealth flow exists in `ci_political_v30 §4`, Church territorial power is "comprehensive" across four+ sections, and Altonia/IP already models offstage pressure. Explicit lesson recorded: "Pass 3 outside-reviewer-pass over-found... 3 of 3 additions closed on first verification."
- **A-6, coalition cost as an ongoing resource drain** — reframed and closed: coalition is structural (co-victory territory partition), not an accounting-style upkeep cost (`...verification-outcomes.md` V-1.2).
- **A-11, post-victory-impossibility persistence as a gap** — closed: `victory_v30 §5` World-State Transitions (Post-Calamity Era / Phased Occupation / Anarchy) plus Mission-shift trigger 3 already cover it; the original finding was based on an incomplete read.
- **Territory Accord as a directly-set 0-4 stat** — this whole model (from `clock_registry_staleness_report.md` Category 3, item 10) is superseded by the settlement layer's derived Accord = floor(mean(Order)) (F-J-2). Any citation of the old "Accord set by domain action, capitals start 4" model is pre-settlement and stale.

---

### OPEN QUESTIONS NEVER ANSWERED

- **Is a Domain Action a Thread operation under P-01/P-14?** If yes, three-dimensional inseparability auto-effects (temporal/epistemic/actualized) must fire on every DA and currently don't — a flagged P1-candidate canon-constraint violation. Never resolved (`2026-05-16-faction-ners-all-directions.md` A-9; still "unchanged" per verification-outcomes §8 D-2.3).
- **Should regime-relative category mutation (candidate М-12) and recognition-as-substrate-state (candidate М-13) be admitted as formal meta-throughlines?** Both flagged, both explicitly deferred to Jordan, neither resolved anywhere in this lane's material (F-J-5; verification-outcomes D-2.1/D-2.2).
- **Can a Founded Organization ever reach Universal Victory?** Deliberately left open with a stated preference (not advertise, don't design toward it) rather than a decision (F-J-10).
- **Should the Restoration Movement be a permanent minor faction or purely emergent from NPE Coalition?** J-3, explicitly deferred pending videogame playtesting that this corpus never records happening (F-J-11).
- **The territory-scale range conflict (0-4 vs 0-5)** — flagged "must resolve" in `valoria_holistic_audit.md` Part 12 (J-7) and independently in `clock_registry_staleness_report.md` Category 4; no resolution recorded in any document in this lane.
- **Community Weaving's three mutually conflicting specifications (ED-139)** — named as a live contradiction in `systematic_critique_2026-04-04.md` §2.2 ("These aren't edge cases — they're core mechanics"); no reconciliation found anywhere in this lane's corpus, despite Community Weaving recurring as the load-bearing mechanic for both the settlement Thread bridge (Throughline 1) and the Restoration Movement's entire faction identity.