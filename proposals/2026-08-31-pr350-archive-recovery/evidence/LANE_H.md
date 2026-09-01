## LANE H — Political Dynamics Session & Territory Audits

### COVERAGE
files_assigned: 36 (political-dynamics-session) + 6 (geography-audit) + 3 (findings/ratified docs) = 45
files_opened: 15
files_read_closely: 13 (00_session_index, 01_interpersonal_audit, 04_autonomous_actors_philosophical_reframe, 12_development_specification [full 1876 lines], HANDOFF_session_chain, 24_promotion_checklist_evaluation, 25/26/27_integration_*, 22_NERS_and_bloat_assessment [partial], 00_audit_report [geography], 04_workplan_reconciliation [geography], territory-settlement-audit/findings.md, pt-treaty-build-readiness/findings.md, contest-redesign RATIFIED)

skipped: 02, 03, 05–11, 13–17, 19, 21, 23 (political-dynamics-session) — stage docs explicitly marked superseded by doc 12 or by the v1.1/v1.2 revision docs; their content is carried forward and summarized inside `HANDOFF_session_chain.md` and `00_session_index.md`, which I read in full. SIM_A through SIM_H + SIM_narrative_arc_pass (9 files, ~3,400 lines) — not opened directly; their scenario-by-scenario findings, invariants, and gaps are fully enumerated in `HANDOFF_session_chain.md`'s per-session notes, which name every gap ID and resolution. `00_phase2_workplan.md` / `01_phase2_workplan.md` / `01_coord_transform.py` / `02_sample_data.yaml` (geography audit) — mechanical/spatial detail out of this lane's scope (mass-battle terrain, march budgets); the reconciliation memo I read captures the decisions that matter.

### FINDINGS (ranked most valuable first)

**F-H-1 — NPCs reframed as autonomous actors, not computed entities**
- SOURCE: `04_autonomous_actors_philosophical_reframe.md:9-17`
- CATEGORY: ontology
- SUBSTANCE: Explicit pivot away from "RP balances, Alignment Scores, AI priority trees" toward NPCs as persons with Concerns (active questions), Projects (multi-season personal agendas), Opinions (characterized, not numeric, assessments of others), Mood (short-term emotional weather), and Memories (5-10 high-salience records). The player is "one actor in a political environment," not the protagonist of NPC lives.
- WHY IT MAY STILL MATTER: This is the governing ontological choice underneath the entire mechanism built in doc 12 — any future political-dynamics work has to decide whether it accepts or rejects this framing before touching the mechanics built on it.
- STATUS IN DOC: "Foundational" (00_session_index.md)
- REDISCOVERED IN: single source, but load-bearing for every later doc in the session (04→05→…→12).

**F-H-2 — The Armature: political interpretation is derived, never authored per-event**
- SOURCE: `12_development_specification.md:414-513` (§3.1-3.2)
- CATEGORY: derivation
- SUBSTANCE: NPCs interpret every event through a 3-dimension weighted armature (Agency/Intent/Mechanism) computed additively from Conviction + Personality + Scar count + active Projects + active Concerns, then per-dimension normalized to a probability distribution. No event gets a hand-authored NPC reaction; the reaction is *computed* from standing state. "Wrong resolution is intrinsic, not flagged" — a Faith-aligned NPC misreading a strategic-calculation event through Faith-shaped seeking-tags is explicitly the design, not a bug.
- WHY IT MAY STILL MATTER: This is a concrete, worked answer to "how do NPCs interpret political events without per-event authoring" — a genuinely reusable derivation pattern regardless of whether this exact spec survives.
- STATUS IN DOC: v1.2.2, "CURRENT SOURCE OF TRUTH" as of the frozen snapshot (PROVISIONAL, never promoted to canonical — see F-H-19).
- REDISCOVERED IN: single source.

**F-H-3 — Faction "mind" is an aggregate of its inner circle, not a separate faction-level stat**
- SOURCE: `12_development_specification.md:930-989` (§5.3)
- CATEGORY: derivation / faction
- SUBSTANCE: `FactionMetaArmature` = Standing-weighted average of inner-circle NPC armatures (S7:1.0, S6:0.7, S5:0.5, S4:0.3, leader ×1.5, all further scaled by a Mood-dampening modifier — Distracted ×0.7, Grieving ×0.5) PLUS a single merged `institutional_stability` term (0.4 weight, decaying with accumulated inner-circle Scars) anchored to the faction's historical dominant Conviction. A reformist leader does not single-handedly shift faction behavior — the aggregate pulls back toward institutional character, which the doc calls out as the mechanism producing "the historically realistic dynamic where reformer rulers find their courts resisting their personal transformations."
- WHY IT MAY STILL MATTER: A concrete, numerically specified answer to "what does a faction's institutional opinion mean, mechanically" — factions are never a single stat block reacting monolithically; they are literally computed from named people.
- STATUS IN DOC: current in v1.2.2.
- REDISCOVERED IN: single source.

**F-H-4 — Settlement political sentiment is derived from governor tenure + Passive-NPC memory aggregate + institutional character, and decays across scale boundaries**
- SOURCE: `12_development_specification.md:765-929` (§5.1-5.2)
- CATEGORY: derivation / settlement
- SUBSTANCE: `SettlementMetaArmature` weight-blends governor_weight (0.1→0.4 scaling with tenure), passive_npc_aggregate_weight (inversely scaled), institutional_character_weight (fixed 0.2, e.g. Cathedral→Faith bias), and population_disposition_weight (0.1). `compute_settlement_signal()` aggregates recent Passive-NPC Memories into a single dominant-tag Signal, with explicit null-guards for settlements with no Passive NPCs (falls back to governor-only, half-weight) or no recent Memories (returns None — "sparse-settlement handling," not a crash). Signal salience is then decayed ×0.7 crossing into faction scale (Cascade Attenuation, §4.4).
- WHY IT MAY STILL MATTER: A settlement's political weather is explicitly NOT a stored scalar — it is recomputed from the people currently on-station there, with documented degenerate-input handling. This is a strong worked answer to "how does a settlement have a political mood without being a hand-tuned stat."
- STATUS IN DOC: current, with a real bug found and fixed in-corpus (see F-H-9 pattern note below) — the 0-5 vs 0-10 scale mismatch in `population_disposition`'s normalization formula (§3.9), corrected as v1.2.2 (`12_development_specification.md:16-25`).
- REDISCOVERED IN: single source for the mechanism; the bug was found independently by `27_integration_settlement_layer.md` cross-checking against `settlement_layer_v30`.

**F-H-5 — Domain Action selection is inner-circle competition scored by Conviction-domain alignment, with an anti-deadlock stall-escalator**
- SOURCE: `12_development_specification.md:1268-1307` (§6.2 `select_proposal()`)
- CATEGORY: mechanism / faction
- SUBSTANCE: When multiple inner-circle NPCs propose same-domain Projects in one Accounting, the faction picks a winner by score = (meta-armature's Conviction-weighted domain alignment) + (Standing×0.1 bonus) + (`0.05 × seasons_stalled` stall-escalator). Without the stall-escalator, simulation testing found unequal-Standing same-domain collisions produce **permanent winner-takes-all deadlocks** (SIM-B Scenario 8) — the escalator was added specifically to fix this and validated at 12-Year scale (SIM-G) as both anti-deadlock and anti-ossification.
- WHY IT MAY STILL MATTER: A concrete, simulation-tested formula for "how do competing political actors within one institution get resolved into one action per season" that explicitly guards against a real pathology (permanent exclusion of lower-Standing actors).
- STATUS IN DOC: current, v1.2.2.
- REDISCOVERED IN: single source (found via simulation SIM-B, confirmed at scale by SIM-E/SIM-G).

**F-H-6 — Single-writer invariant for Opinions: exactly one procedure may mutate NPC-NPC relationship state**
- SOURCE: `12_development_specification.md:1412-1417`, §0.1 change log
- CATEGORY: mechanism
- SUBSTANCE: Procedure D (Opinion Drift) is declared the *only* procedure allowed to mutate the NPC-NPC Opinion structure. Concern resolution (B) and Project completion (C) write Memories only; D consumes those Memories and applies the actual affect-axis change, with a hard clamp [-3,+3] on every write. This was a deliberate architectural correction (PATCH 1.4-1.6) made after an earlier draft had multiple procedures writing Opinions directly.
- WHY IT MAY STILL MATTER: A named, general pattern for avoiding double-counted or desynchronized relationship state in any system where several game-systems can independently claim to change "how NPC A feels about NPC B" — directly answers the brief's interest in "X must be derived, never stored"-style structural insights (here: X must have exactly one writer).
- STATUS IN DOC: current invariant, v1.1 onward.
- REDISCOVERED IN: single source.

**F-H-7 — Cascade Attenuation: a formalized decay law for political signal crossing personal→settlement→faction→peninsula scale boundaries**
- SOURCE: `12_development_specification.md:692-711` (§4.4)
- CATEGORY: mechanism
- SUBSTANCE: Signal magnitude decays ×0.7 per scale boundary crossed, with an explicit sub-threshold cutoff: salience <2 generates a Concern but does not influence Domain Action selection. Example given: a personal event at salience 5 becomes a faction-Concern at 2.45 and a peninsula-consequence at 1.7.
- WHY IT MAY STILL MATTER: This is the single mechanism preventing a lone tavern brawl from reshaping continental politics while still letting genuinely large events propagate — a reusable "scale-crossing decay constant + floor" pattern independent of anything else in the doc.
- STATUS IN DOC: current.
- REDISCOVERED IN: single source, but explicitly reused/extended by later patches (Settlement Signal cascade decay, event vertical propagation §15.4).

**F-H-8 — Knot Rupture: a fully specified "public political failure" mechanic, P1-critical gap that got real teeth**
- SOURCE: `12_development_specification.md:288-354` (§2.5.2)
- CATEGORY: mechanism
- SUBSTANCE: Trigger conditions (sustained disposition < -2 for 2+ seasons, OR a salience-5 betrayal Memory against a Belief held at confidence 4-5), mutual Disposition crash to -4 (beyond the normal floor), public salience-5 event visible to observers, permanent Founding-equivalent Memory, increased future-Knot-formation difficulty (+1 disposition threshold), and possible identity-level Belief revision ("I am trustworthy" → "I am inconstant"). Recovery requires 4+ seasons of sustained positive Memories and never fully erases the original event.
- WHY IT MAY STILL MATTER: A near-permanent, publicly-legible relational-collapse mechanic distinct from simple Disposition decay — the strongest "intimate-political" dramatic beat this session designed, and it was flagged as the engine's third P1-critical gap (SIM-H-G2) before being specified in full.
- STATUS IN DOC: current, PATCH v1.2-3, "featured behavior."
- REDISCOVERED IN: single source.

**F-H-9 — Faction Succession: tiered leader-designation algorithm, later extended for named-heir override**
- SOURCE: `12_development_specification.md:1026-1065` (§5.4.1); `25_integration_npc_behavior.md:108-134` (INT-1.6)
- CATEGORY: governance
- SUBSTANCE: On leader death/exit, `designate_new_leader()` picks the highest-Standing same-faction Active NPC, tie-breaking first by Conviction-alignment with the faction's dominant Conviction, then by NPC id. The npc_behavior integration pass then flagged this as insufficient for named canonical heirs (e.g. Prince Torben) and recommended adding an explicit `faction.explicit_heir` Tier-0 check before the algorithmic fallback.
- WHY IT MAY STILL MATTER: Succession-by-algorithm vs. succession-by-narrative-designation is a real, still-relevant tension; this corpus proposes a concrete two-tier resolution (explicit designation overrides, algorithm is the fallback) rather than picking one exclusively.
- STATUS IN DOC: adopted in v1.2 (algorithm) + recommended-not-yet-applied (explicit_heir override, INT-1.6, "recommended for canonical-promotion edit" — never confirmed applied in this snapshot).
- REDISCOVERED IN: single source for the algorithm; the heir-override gap was found by a separate integration pass (doc 25) cross-checking against the canonical named-NPC roster.

**F-H-10 — Standing recalculation must count *execution*, not *competition outcome*, or it self-reinforces inequality**
- SOURCE: `12_development_specification.md:1603-1636` (§8.1, PATCH v1.2-1); HANDOFF_session_chain.md:277
- CATEGORY: mechanism / problem-only-then-solved
- SUBSTANCE: Original spec counted "lost inner-circle competition" as a `failed_da_proposal`, decrementing Standing. Simulation flagged this as SIM-B-G8, a P1-critical gap: under that reading, lower-Standing NPCs lose competitions → lose Standing → lose more competitions, a runaway exclusion loop confirmed at scale (~8 percentage points of faction Order-share divergence over 3 years between the strict and liberal readings, SIM-E). Resolved: only an actual failed DA *roll* counts against Standing; a lost competition merely increments `seasons_stalled` (feeding the stall-escalator, F-H-5).
- WHY IT MAY STILL MATTER: A concrete, quantified example of how a plausible-looking "did they succeed" metric for political advancement can become a rich-get-richer trap, and the specific counter-definition that avoids it.
- STATUS IN DOC: resolved, PATCH v1.2-1, retained through v1.2.2.
- REDISCOVERED IN: single source (surfaced independently across SIM-B, SIM-D, and SIM-E before being fixed — three separate simulation passes converged on flagging the same defect, the strongest "independent rediscovery" signal within this lane).

**F-H-11 — The 8-gap interpersonal-to-political audit: vertical-only relationships, no NPC↔NPC modeling**
- SOURCE: `01_interpersonal_audit.md:98-236` (Parts 3, 6)
- CATEGORY: problem-only
- SUBSTANCE: Pre-reframe audit of the *existing* (pre-session) design found interpersonal mechanics were "overwhelmingly vertical: Player ↔ NPC" with NPC-to-NPC relationships, rivalry, and coalition formation "structurally unmodeled." Cataloged as 8 gaps (G1-G8): no NPC-NPC relationships, no Disposition gate on Standing promotion, no settlement-loyalty→faction feedback, no diplomatic-decision→NPC-disposition consequence, succession treated as event not structure, no internal consequence for cross-faction relationship discovery, no active "influence" tier of intelligence operations (only Information/Recruitment, missing the middle "manufactured grievance" tier), and no companion-governor Conviction→settlement drift.
- WHY IT MAY STILL MATTER: This is the sharply-stated diagnostic that everything else in the session (04, 05, 12) was built to answer. Even where the specific fixes proposed here were superseded by later mechanics, the gap statements themselves are durable design questions any governance rewrite has to re-answer.
- STATUS IN DOC: "Foundational — gaps still valid" (00_session_index.md).
- REDISCOVERED IN: single source, but G1 (horizontal relationships) and G5 (succession-as-structure) are directly what doc 12's Opinion architecture and Faction Succession mechanic (F-H-6, F-H-9) were built to answer.

**F-H-12 — Faction Crisis / "institutional autopilot" and its recovery paths**
- SOURCE: `12_development_specification.md:993-1024` (§5.4)
- CATEGORY: faction / mechanism
- SUBSTANCE: If ≥40% of inner-circle NPCs are simultaneously Distracted/Grieving, the faction enters institutional autopilot: only existing Priority 1-2 Domain Actions execute, no new Project proposals, no inner-circle competition. Three recovery paths are named (Mood recovery, succession clarity, external alliance); a crisis with none available is called "structurally degenerate" and flagged as needing engine-generated external pressure. A separate "anomaly detection" rule (≥3 inner-circle NPCs simultaneously showing negative Mood + low Disposition-with-leader, absent external cause) triggers faction-leader Loyalty Interviews — a mechanized paranoia/purge trigger.
- WHY IT MAY STILL MATTER: A concrete state-machine for "what does it mean for a faction to be politically incapacitated," with named recovery conditions rather than leaving crisis as an unresolvable dead state.
- STATUS IN DOC: current.
- REDISCOVERED IN: single source.

**F-H-13 — Two-Tier Authority Model and subnational-faction governance create routing complexity doc 12 initially missed**
- SOURCE: `27_integration_settlement_layer.md:57-140` (§2.2, 2.3, 2.6)
- CATEGORY: governance / settlement / seam
- SUBSTANCE: `settlement_layer_v30` (external canon, referenced not read directly) specifies a Two-Tier Authority Model (Provincial Authority = national faction vs. Settlement Governor = local), with governor able to be Player, Officer NPC, Subnational Faction, or Vacant. doc 12's Settlement-Signal routing logic (`route_signal_to_concern`) originally only handled the single-Officer-NPC case; the integration audit specifies the extension needed for Player-governor, subnational-faction-governor, and vacant cases.
- WHY IT MAY STILL MATTER: Governance authority at the settlement scale is explicitly NOT single-shaped (national vs local, and local itself can be four different kinds of actor) — any settlement-signal-routing or local-power mechanic needs to handle this branching, and this doc names exactly which cases were missed.
- STATUS IN DOC: PROVISIONAL, "recommended" patch — not confirmed applied.
- REDISCOVERED IN: single source.

**F-H-14 — Settlement-stat-derived events are the causal seed layer beneath political Signal aggregation**
- SOURCE: `27_integration_settlement_layer.md:103-122` (§2.4)
- CATEGORY: derivation / settlement
- SUBSTANCE: `settlement_layer_v30 §4.3` specifies stat-triggered local events (Prosperity 0→Famine+Order−1; Defense 0+hostile adjacency→Raid; Order 0→Local Revolt; Order 5+Prosperity 4+→Flourishing). doc 12's Settlement Signal (F-H-4) does not generate events itself — it aggregates NPC Memories *of* such events. The integration audit clarifies these are complementary layers: stat-conditions→events→NPC Memories→political Signal, a full causal chain from raw settlement numbers to faction-level political consequence.
- WHY IT MAY STILL MATTER: Establishes a clean layering principle — settlement mechanics generate the *content* of political life, political mechanics generate the *propagation*; conflating the two layers was an identified risk.
- STATUS IN DOC: recommended cross-reference, not yet applied to either doc.
- REDISCOVERED IN: single source.

**F-H-15 — Population Disposition is explicitly a *second*, independent derived value alongside Order — sentiment vs. institutional stability are different axes**
- SOURCE: `12_development_specification.md:797-828` (§5.1); `27_integration_settlement_layer.md:144-150` (§3)
- CATEGORY: derivation
- SUBSTANCE: `population_disposition[settlement,faction] = clamp(0.4·normalized_order + 0.4·normalized_prosperity + 0.2·recent_event_delta, -3,+5)`, where `recent_event_delta` sums faction-caused Disposition deltas over the last 4 seasons with exponential decay (×0.7^seasons_ago), tracked via a per-settlement capped event-history log (8 seasons). Explicitly not the same axis as Order: "Order tracks institutional governance stability; population_disposition tracks settlement-population sentiment toward each faction."
- WHY IT MAY STILL MATTER: A clean worked example of "two related-but-distinct derived quantities from the same substrate, kept separate on purpose" — directly the kind of structural insight the brief flags as durable independent of the doc.
- STATUS IN DOC: current, but shipped with a real scale-mismatch bug (0-10 vs 0-5 assumption) fixed as v1.2.2 — see F-H-4.
- REDISCOVERED IN: single source.

**F-H-16 — Parliamentary Transfer + Treaty Expiration: canon exists, substrate does not — a governance mechanism blocked on missing plumbing, not missing design**
- SOURCE: `2026-05-26-pt-treaty-build-readiness/findings.md:14-53` (F1-F6)
- CATEGORY: governance / seam
- SUBSTANCE: Both canon docs (`parliamentary_transfer_v30`, `treaty_expiration_v30`) are CANONICAL and clear, but: the Parliamentary Vote contest and Stay-handling are literal `NotImplementedError` stubs; the Casus Belli economy (8 named sources, pair-scoped, stacking/decrementing) has "zero substrate" — no `Faction.cb` field, no registry, and every CB source hooks into 5+ other systems, several themselves unbuilt; Cross-faction Standing (needed for vote-bloc computation) doesn't exist — `Faction.standing` is a single scalar, a gap independently flagged by a *different* module's own docstring (`crown_initiative.py`'s Coronation Renewal); the Crown's canonical treaty-renewal action ("Senator Outward") is entirely absent from the dispatch table, meaning as-built the Crown would only ever receive the treaty-lapse penalty with no compensating renewal loop; and treaty-violation is not auto-detected in the conquest code path at all.
- WHY IT MAY STILL MATTER: This is exactly the kind of "readiness assessment names blockers, and blockers are durable" finding the brief asks for — it demonstrates that a governance mechanism (parliamentary power transfer, binding treaties) can be fully designed at the canon layer and structurally unbuildable without first building casus-belli accounting, cross-faction Standing, and a vote-contest engine that don't yet exist anywhere in the codebase.
- STATUS IN DOC: PROVISIONAL, "awaiting Jordan ratification on two open decisions"; Pass A (annotation cleanup) landed, Passes B-F (the actual build) not started as of this doc.
- REDISCOVERED IN: cross-faction Standing gap independently named by `crown_initiative.py`'s own inline `[PROVISIONAL]` comment (F3), separate from this audit finding it.

**F-H-17 — The published faction-balance equilibrium is a five-mechanic figure; two of the five don't exist**
- SOURCE: `pt-treaty-build-readiness/findings.md:28` (F6)
- CATEGORY: problem-only
- SUBSTANCE: The canonical balance target (24.7/28.6/24.2/22.5 territory share) validates only with Parliamentary Transfer, Einhir Revival, Altonian Reinforcements, RM PT-decay, and Treaty Expiration *simultaneously* active; the live sim has none of the five, and two faction-unique action slots are explicitly `BLOCKED` pending an unrelated contamination audit. Building just PT+Treaty cannot reach the published number, and the doc explicitly warns against "tuning to hit v12c" under that condition.
- WHY IT MAY STILL MATTER: A durable caution against citing an equilibrium number as a target when the mechanisms that produced it are only partially built — directly relevant to any future faction-balance claim in this game.
- STATUS IN DOC: explicit open decision (§4.2, three options x/y/z, default (x) "accept and document," not ratified in this snapshot).
- REDISCOVERED IN: single source.

**F-H-18 — Settlement schema migration (PP-726) was half-applied, leaving governance-adjacent data structurally self-contradictory**
- SOURCE: `2026-06-22-territory-settlement-audit/findings.md:14-42` (Root cause, H2, M1)
- CATEGORY: seam / problem-only
- SUBSTANCE: A settlement re-cut from 36 entries to 37 (adding a "Village" type) migrated the settlement registry and adjacency map but left the geography YAML's `settlements:`/`provinces:` blocks, one doc section (§1.1), and a UI supplement on the stale 36-scheme — while the *same YAML file's* adjacency block already references the new 37th settlement (S-037/Schoenland) as an edge target that is never defined as a node. "Village" is used as a type for ~18 settlements but is undefined in the settlement-types table, facility-slot table, or local-actor table — those 18 settlements have no defined stats or facility slots.
- WHY IT MAY STILL MATTER: A concrete, still-live illustration of the corpus's recurring pattern — a schema change applied to the mechanically load-bearing surface (adjacency, used by pathing/faction_action code) but not to the descriptive/reference surfaces, leaving internally contradictory settlement counts across the same file.
- STATUS IN DOC: unresolved defects (H1-H3, M1-M7) as of 2026-06-22, no evidence of a later fix in this snapshot.
- REDISCOVERED IN: independent of the political-dynamics session — a separate audit, six weeks later, converging on the same class of defect (canon/data half-migration) that the pt-treaty-readiness doc also independently surfaces for a different subsystem (F-H-16). Three separate audits across three months (04-30 geography, 05-26 treaty, 06-22 territory) each independently found "the spec says one thing, the data/code says another, because a migration only touched the load-bearing half."

**F-H-19 — Promotion to canonical was blocked on a durable, never-resolved Jordan-decision inventory**
- SOURCE: `12_development_specification.md:1717-1851` (§11, §16); `24_promotion_checklist_evaluation.md:56-76, 144-157`
- CATEGORY: governance / problem-only
- SUBSTANCE: The entire political-dynamics architecture (doc 12) remained PROVISIONAL, blocked on: (1) whether to keep or cut the 210-entry Conviction×event symbolic-resonance table, (2) whether faction-top political behavior should be opaque or legible by design, (3) whether NPCs should introspect their own Standing/Conviction, (4) whether crisis-masking persists across Accountings, (5) whether to restore Intelligence as a 6th faction stat, (6) a LICENSE/GOV-08 status carryover, and (7) full vs. reduced (~1,190 vs ~700-800) content-authoring scope. None show as resolved anywhere in this corpus.
- WHY IT MAY STILL MATTER: These are still-live, still-relevant design forks (opacity vs. legibility of faction "AI" being the most consequential) that any future governance-mechanics work should check against before re-deciding from scratch.
- STATUS IN DOC: `[JORDAN-DECISION-PENDING-ED-755]`, explicitly unresolved through v1.2.2.
- REDISCOVERED IN: single source.

**F-H-20 — Face/Reputation/faction-Mandate pipeline (ratified, governance-adjacent corner of the contest redesign)**
- SOURCE: `2026-06-01-contest-redesign/RATIFIED_2026-06-01.md:13, 20` (CR3, omega vetting)
- CATEGORY: governance / seam
- SUBSTANCE: The ratified social-contest redesign splits the retired "Composure" into Concentration (shared stamina resource with combat) and a new **Face** tracker — an explicitly *transient*, contest-local ethos measure, distinct from persistent Disposition/Reputation. The omega-vetting block names an explicit intended pipeline: "Face → Reputation → faction Mandate," i.e., a formal-contest outcome is meant to eventually feed institutional legitimacy at the faction scale.
- WHY IT MAY STILL MATTER: This is a second, independently-ratified system gesturing at the same "personal-scale outcome → institutional-scale consequence" seam the political-dynamics session built (Domain Echo, F-H-5); the Face→Reputation→Mandate chain itself is flagged as not yet built ("propagation follow-through... not yet applied").
- STATUS IN DOC: "provisional canon-of-record as of 2026-06-01" (Jordan-ratified, but propagation into Reputation/Mandate explicitly deferred).
- REDISCOVERED IN: single source for this exact framing, but structurally the same seam-class as F-H-16/17.

**F-H-21 — Completionist bloat identified and deliberately cut from a political mechanic (coup, war-state, peace-treaty)**
- SOURCE: `22_NERS_and_bloat_assessment.md:27-54`
- CATEGORY: problem-only
- SUBSTANCE: A self-critical NERS pass on the finished v1.2 spec found the Leader Challenge/Coup mechanic and the Inter-Faction War State + Peace Treaty mechanic failed the "would the game break without this?" test — coup-by-living-peer is rare enough that emergent Memory-drift already covers precursor pressure, and War State/Peace Treaty were pure aggregation over Domain Actions the general framework already supports. Both were cut from v1.2.1, explicitly deferred to "v1.3."
- WHY IT MAY STILL MATTER: A documented example of scope-discipline being applied to a governance system specifically (not just naming the temptation, but naming what was cut and why) — useful precedent if this exact functionality (coups, formal war states) gets proposed again.
- STATUS IN DOC: "Cut from v1.2.1... Defer to v1.3 if Jordan wants it" — no evidence in this corpus that v1.3 happened.
- REDISCOVERED IN: single source.

**F-H-22 — Forgetting-zone-as-overlay ruling: a world/faction interaction explicitly made non-negotiable**
- SOURCE: `2026-04-30-geography-audit/04_workplan_reconciliation.md:90-96` (§2.2)
- CATEGORY: world-churn / governance seam
- SUBSTANCE: Deciding whether the Calamity "Forgetting" zone should be a terrain type or a polygon overlay was explicitly resolved as overlay-not-terrain specifically because making it a terrain type "would imply faction-property exemptions are mechanically possible" — i.e., a faction could someday be granted a stat/property that ignores Forgetting-zone cost. Per PP-703, faction-property exemptions from Forgetting are ruled *impossible*; the data-layer choice was made to prevent even accidentally enabling that at the schema level.
- WHY IT MAY STILL MATTER: A rare case of a purely spatial/data-modeling decision being driven by a governance-adjacent canon constraint (no faction can be exempt from a universal world-mechanic) — worth flagging for anyone touching either the geography layer or faction-property systems later.
- STATUS IN DOC: ratified decision in a reconciliation memo (PP-709 proposed / ED-779).
- REDISCOVERED IN: single source.

### DEAD ENDS
- **v1.0 "RP balance" / Alignment Score model** (`03_revision_directionality_emergence.md`, per `00_session_index.md:24`): explicitly superseded by the autonomous-actor reframe (F-H-1) same session; reasoning preserved but mechanism dead.
- **§5.4.2 Leader Challenge / Coup Mechanic** (PATCH v1.2-20): drafted in full, then cut in the v1.2.1 NERS pass (F-H-21) as "spec-completionist," deferred to an unrealized v1.3.
- **§8.2 Inter-Faction War State + §8.2.1 Peace Treaty** (PATCH v1.2-22/23): same fate as above — drafted, then cut as pure bookkeeping over the existing Domain Action framework.
- **valoria_map_v2.svg**: `2026-04-30-geography-audit/00_audit_report.md §3.C4` — found to use a completely different territory-numbering schema and faction-territory assignment than current canon; explicitly deprecated (kept for history, not usable).
- **Old 36-settlement scheme**: superseded by the 37-settlement PP-726 scheme, but per F-H-18 the supersession itself is only half-applied, so remnants of the dead scheme are still live in several files.

### OPEN QUESTIONS NEVER ANSWERED
- All six `[JORDAN-DECISION-PENDING-ED-755]` items (F-H-19): symbolic_effects table keep/cut, faction opacity-vs-legibility stance, NPC self-monitoring, crisis-masking persistence, Intelligence as 6th faction stat, LICENSE/GOV-08 — no resolution found anywhere in this corpus.
- Content-authoring scope for the political-dynamics system: full ~1,190 entries vs. reduced ~700-800 (`12_development_specification.md §11.2`) — never decided.
- Integration-patch adoption: 20 recommended patches across docs 25/26/27 (NPC behavior, player agency, settlement layer) — recommended, none confirmed adopted into the actual canonical docs they target.
- PT+Treaty: which ratification posture for provisional canon items (ratify-as-written / validated-core-only / mixed) and which balance target (accept-current / chase-full-v12c / interim) — both explicitly reserved to Jordan, unresolved in this snapshot (`pt-treaty-build-readiness/findings.md §4`).
- Territory audit Q1/Q2: whether sparse Seat coverage (3 of 36/37 settlements typed Seat) and single-settlement provinces are acceptable — flagged as needing a design ruling, not a defect, and not answered.
- The `Halvardshelm` (T11, Varfell) vs `Halvarshelm` (T17, Hafenmark) one-letter name collision — flagged as a legibility/mis-assignment hazard, no ruling found on whether to rename.