## LANE I — NPC COMPREHENSIVE AUDIT & CHARACTER AUDITS

### COVERAGE
files_assigned: 8 | files_opened: 8 | files_read_closely: 8 (npc-comprehensive-audit read via targeted extraction, not linearly)
skipped: Within the 1.26M-char comprehensive audit, I did not read the ~370 of 449 findings that are pure per-NPC data contradictions (wrong TS number, wrong gender, wrong surname) with no structural content — I read all 449 finding titles/index entries and closely read ~90 (the 9 system-level/taxonomy units: Convictions taxonomy integrity, Resonant-styles & P-08 gating, Stat-scale sweep, Behavior priority-trees, Relational-graph integrity, Ethical-frameworks supersession, Companion specification, Foils coherence, Naming contamination). Estimated coverage of that one file: ~20% by finding-count, but a much higher share of its structural/mechanism content, since the skipped 80% is individual-NPC bookkeeping (gender mixups, duplicate surnames, stray TS digits) that the brief's exclusions rule out as low-value. self-audit-cascade and meta-audit-immersion are about *game design methodology* (per-decision cognitive load, presentation-layer vs mechanical soundness), not repo process — kept, condensed.

### FINDINGS (ranked most valuable first)

**F-I-1 — Faction and character are explicitly "rightly asymmetric," with one shared substrate and named bridge mechanics**
- SOURCE: designs/audit/2026-05-08-comparative-audit-faction-vs-character.md §2–§4, §8
- CATEGORY: ontology
- SUBSTANCE: A dedicated comparative audit concludes the two frameworks should NOT be forced into parallel structure. What they share is one substrate — the 13-Conviction taxonomy (PP-684) — and a small set of named bridge mechanics: cascade aggregation, Self-Other→Popular-Support attribution, Standing, Domain Echo, and `effective_convictions`. Everything else (Resonant Style, Beliefs, Knots, Disposition vs. Mission, Legitimacy, Stability triggers, Political Axes) exists at only one scale and has no analog at the other. A structural-analog table explicitly warns against treating Coherence≈Stability or Belief≈Mission as equivalent — "a reader who thinks 'character Coherence = faction Stability' will make wrong predictions."
- WHY IT MAY STILL MATTER: This is a direct, reasoned answer to "should NPCs and factions be modelled the same way" — with a worked argument for why forcing symmetry actively distorts play. Any current design that treats faction and character sheets as interchangeable should confront this document's counter-case first.
- STATUS IN DOC: PROVISIONAL analytical document (header)
- REDISCOVERED IN: single source, but its underlying claim (that Ethical-Framework/Ob mechanics differ from Conviction mechanics) is corroborated independently by the comprehensive audit's Ethical-frameworks-supersession unit.

**F-I-2 — Cascade math: the actual formal bridge from personal Conviction to faction Conviction**
- SOURCE: designs/audit/2026-05-08-comparative-audit-faction-vs-character.md §6.2
- CATEGORY: mechanism
- SUBSTANCE: NPC personal Convictions aggregate into faction state via `effective = α × personal + (1−α) × supervisor's effective` (hierarchy-blended cascade, PP-686 §3.2). Leader self-interest dampens credit for faction outcomes: `attributed_outcome = raw × (1 − 0.5 × max(0, leader.self_other))`. When a leader's Scar count ≥ 3, cascade damping is suspended and new Convictions propagate immediately — "produces visible institutional instability" as a deliberate effect, not a bug. Faction→NPC runs the other way: Stability ≤1 collapses all member NPCs' Convictions to Liberty; faction collapse (Stability=0) strips affiliation but *NPCs keep their Conviction/Beliefs/Disposition and become recruitable by other factions*.
- WHY IT MAY STILL MATTER: This is a concrete, numerically specified two-scale derivation — exactly the kind of "formula, not gloss" the brief wants — and the "NPCs survive faction collapse as free agents, poachable by rivals" mechanic is a distinctive, reusable idea regardless of whether the taxonomy underneath it changes.
- STATUS IN DOC: none stated (PP-686 v2 cited as source)
- REDISCOVERED IN: the faction Stability≤1→Liberty-collapse trigger is independently confirmed inside the comprehensive audit's arc-state-machine findings (AUD-NPC2-086).

**F-I-3 — `effective_convictions` / `role_acting`: an NPC's psychology bifurcates between "acting as themselves" and "acting as office-holder"**
- SOURCE: designs/audit/2026-05-08-comparative-audit-faction-vs-character.md §6.2, §6.5
- CATEGORY: mechanism
- SUBSTANCE: `role_acting = true` swaps an NPC's raw `personal_convictions` for the cascade-derived `effective_convictions` for the duration of an institutional act; `role_acting = false` reverts to the personal vector. This value is explicitly a "cross-scale singleton" — authored by neither the character schema nor the faction schema alone, computed at the junction. Domain Action Ob modifier = `mission + cascade + expectation`, clamped ±2 (the "triadic Ob calc," PP-686 §3.7) — this is the mechanic that later superseded the old per-NPC "Ethical Framework" Ob modifiers (see F-I-6).
- WHY IT MAY STILL MATTER: A structurally clean answer to "does a duke act the same in council as at dinner" — an NPC-as-office-holder vs NPC-as-person distinction with a computed, not authored, value for the former.
- STATUS IN DOC: none
- REDISCOVERED IN: single source

**F-I-4 — Scars are the sole mechanism by which tactical Contest outcomes become permanent narrative-arc change**
- SOURCE: designs/audit/npc_faction_arc_interdependency_2026-04-18.md Part IV §4.2; designs/audit/2026-05-08-character-mechanics-critical-audit.md §2.2 item (8)
- CATEGORY: mechanism
- SUBSTANCE: A Scar × Arc-state map for 7 named NPCs shows Scar 0→3+ escalation reliably shifting which Conviction is primary, which behaviors become available, and eventually collapsing the NPC's decision table into "unpredictable"/"crisis." The critical audit independently calls this the "arc-emergence engine" and flags a real gap: the crisis table is a flat d6 roll that doesn't check which Convictions the character actually holds weight on — "a 3-Scar character with no Faith weight should never roll 'Faith intercedes.'"
- WHY IT MAY STILL MATTER: Names the exact mechanism (Scars) that converts a won/lost social Contest into permanent character transformation, plus a specific, still-live calibration defect in it.
- STATUS IN DOC: none (flagged as open calibration question, never resolved in these docs)
- REDISCOVERED IN: independently named as load-bearing in both the interdependency matrix and the mechanics audit — two documents from different dates that plainly didn't read each other.

**F-I-5 — Conviction as political topology: alliance-compatibility is a computable property of the Conviction+Resonant-Style graph, not authored per-relationship**
- SOURCE: designs/audit/npc_faction_arc_interdependency_2026-04-18.md Part V, Throughline 8
- CATEGORY: derivation
- SUBSTANCE: The doc derives which faction-leader pairs are naturally compatible or incompatible purely from their Conviction primary/secondary and which Resonant Style can reach them — e.g., "Almud (Order/Reason) + Vaynard (Reason/Autonomy): shared Reason but Almud's Order contradicts Vaynard's Autonomy" is an *incompatibility trap*, while "Almud + Edeyja: Evidence can work on Almud because his Reason is secondary" is a *compatibility path*. This reframes the entire cast's diplomatic possibility-space as a derivable graph rather than a set of hand-authored relationship flags.
- WHY IT MAY STILL MATTER: A generative technique — alliance/conflict potential falls out of two existing per-NPC stats instead of needing to be separately authored for every pair, which scales far better than hand-written relationship matrices.
- STATUS IN DOC: none — but uses the pre-PP-684 7-Conviction labels (Order/Reason/Faith/Precedent/Autonomy/Equity/Continuity), so the specific example pairs are stale; the *method* is not.
- REDISCOVERED IN: single source

**F-I-6 — Ethical Framework labels were the original mechanical Ob driver, then formally superseded by a "triadic Ob" calc — and the supersession never propagated**
- SOURCE: designs/audit/2026-06-22-npc-comprehensive-audit.md:1974–2001 (AUD-NPC2-198–201); designs/audit/2026-05-08-character-generation-audit.md P6 (lines 165–179)
- CATEGORY: mechanism
- SUBSTANCE: Every Tier-1 NPC originally carried an "Ethical Framework" label (Virtue, Faith, Categorical Imperative, Utility-driven Pragmatism, Martial Honour, Equity Social Contract, Moral Relativism, Administrative Proceduralism) that directly applied Ob modifiers (−1/+1/+2) to that NPC's actions. PP-686 §3.7 replaced this with the mission+cascade+expectation triadic calc (clamped ±2) and formally retired the framework labels as *descriptive-only* tags. Both audits independently found the old labels still live and still driving Ob math in the source docs, with zero `[SUPERSEDED]` annotation — "simultaneously canonically retired AND mechanically active." The comprehensive audit's own verifier later downgrades severity because the annotation requirement was scoped to an unbuilt "Part B" of character_canon and the source doc was *deliberately* left unedited pending a "separate propagation cycle."
- WHY IT MAY STILL MATTER: A clean case study in a mechanic that was correctly redesigned (personality-driven Ob → triadic institutional Ob) but whose old implementation was never actually removed — worth checking whether any current implementation still keys off the framework labels rather than the triad.
- STATUS IN DOC: SUPERSEDED (per PP-684 §6 / PP-686 §3.7), but downstream files never updated
- REDISCOVERED IN: independently found by two audits five weeks apart (2026-05-08 and 2026-06-22), neither citing the other — strong signal.

**F-I-7 — The NPC metaphysical stat stack: TS/Coherence/Certainty/Framework-Drift, with concrete bands and capability floors**
- SOURCE: designs/audit/2026-06-22-npc-comprehensive-audit.md:951–971, 1129–1156, 3079–3099, 3709–3715 (findings 51–53, 76–78, 356, 446)
- CATEGORY: mechanism
- SUBSTANCE: Thread Sensitivity (TS) is a 0–100+ scale banded Hidden(10–19)/Dormant(20–29)/practitioner threshold at 30 ("Stirring")/Active(30–49)/Deep(50–69)/Apex(70+), with hard capability floors: Thread-Read at 30+, Locking/Dissolution/Mending at 50+, Past-Oriented Pulling at 70+. Coherence is 0–10 (self-rendering integrity, floors at 0 = "Conversion"). Certainty is 0–5 (cosmological-framework fit). Framework Drift is bounded [1,7]. Self-Other is bounded [−1,+1] with damping constant κ=0.03. Resonant-style/positional dice stacking is hard-capped at +5D, pool-minimum 1D.
- WHY IT MAY STILL MATTER: This is the fully specified numeric substrate underlying every NPC's metaphysical state — reusable regardless of what happens to the narrative layer above it.
- STATUS IN DOC: none contested in this pass ("dimension (a)/(b) essentially clean" per finding 446)
- REDISCOVERED IN: single source (internally cross-verified across dozens of individual NPC checks)

**F-I-8 — P-08/P-10/P-12: three canon-level constraints on how NPC mechanism must behave**
- SOURCE: designs/audit/2026-06-22-npc-comprehensive-audit.md:938–943, 2338–2372 (P-08); 1890–1903, 3395–3401 (P-10); 2394–2407 (P-12)
- CATEGORY: derivation
- SUBSTANCE: P-08: Thread-level evidence is epistemically inert against any NPC below TS 30 (not just TS 0) — repeatedly mis-implemented as a "TS 0" gate, leaving the entire 1–29 band wrongly exploitable across multiple independent findings. P-10: Coherence/drift must never be framed morally (no "corruption," no sin-language) — largely honored structurally, only surface prose ("seduction," "madman") brushes the line. P-12 ("relational contagion"): drift must propagate through Knots tridimensionally (actuality/intelligibility/temporality), never collapsed to "a single generic strain value," and must be agent-neutral (either party's drift can strain the bond, not just PC→NPC).
- WHY IT MAY STILL MATTER: These are three explicit, reusable design constraints for any future NPC-psychology mechanism — a real gate boundary (30, not 0), a forbidden narrative register, and a ban on collapsing relational effects to a scalar.
- STATUS IN DOC: canon constraints (P-08/P-10/P-12), still live; the TS-0-vs-TS<30 miswording recurs across at least 4 independent findings and appears never fixed within this corpus.
- REDISCOVERED IN: the TS<30 boundary error is hit independently by findings 48, 49, 160, and 250 — the single strongest "independent rediscovery" signal in the whole corpus.

**F-I-9 — The relational graph: NPC bonds are typed edges over a settlement-adjacency BFS, with geographic distance multiplying relational strain**
- SOURCE: designs/audit/2026-06-22-npc-comprehensive-audit.md:1676–1719, 3016–3022 (findings 155–156, 347)
- CATEGORY: mechanism
- SUBSTANCE: `npc_relational_graph_v30` models NPC bonds as typed edges (symmetric SWORN-BOND, bidirectional rivalry) whose settlement-to-settlement BFS hop-count feeds a distance-scaling multiplier (×1.0/1.25/1.5/2.0) into strain math — i.e., a genuine spatial dimension to relational mechanics: NPCs physically far apart accrue Knot/relational strain differently than NPCs co-located. As designed, this was badly executed (worked-example hop counts don't match the actual BFS) and barely populated: only 3 of the roster's 13 supporting NPCs carry any edge at all, and 2 of the 3 headline "motivating ties" advertised in the doc's own scope section were never instantiated as edges.
- WHY IT MAY STILL MATTER: The *idea* — settlement distance mechanically modulating relational/Thread strain — is a real structural device worth keeping even though this specific implementation was never finished or verified.
- STATUS IN DOC: PROVISIONAL, self-acknowledged deferred ("B2, §12: 13+ named NPCs need their canonical edges authored")
- REDISCOVERED IN: single source

**F-I-10 — The per-NPC data model was fragmented across 5+ uncoordinated documents, and the fragmentation was a *known, deliberately deferred* state, not an oversight**
- SOURCE: designs/audit/2026-05-08-character-generation-audit.md P1–P2, §5 (V1–V4); designs/audit/2026-06-22-npc-comprehensive-audit.md:1223–1234, 2345–2372 (findings 90, 251–252)
- CATEGORY: ontology
- SUBSTANCE: A single NPC's canonical facts (Conviction, TS, Coherence, faction, framework) were independently authored in npc_roster, npc_behavior §2, npc_character_analyses, npc_foils, and the migration roster, with real numeric divergence for at least 3 shared NPCs (Maret Uln, Yrsa Vossen, Baralta). Critically, character_canon's own Decision Log (D1) explicitly instructs: "Do NOT silently regenerate npc_behavior §2 from migration roster — that's a separate propagation cycle" — meaning fragmentation was a deliberate, logged deferral, not a defect nobody noticed. The proposed fix (P1/P2, character-generation-audit): promote one canonical per-NPC sheet (identity, 13-Conviction vector, Self-Other, cultural label, Beliefs, Goals, Inspiration, arc map, physical signature, speech register) and make every existing file a *generated view* of it, which "dissolves both P1 and P2 simultaneously."
- WHY IT MAY STILL MATTER: This is exactly the single-owner-of-truth principle the current repo already espouses, independently arrived at for NPCs a year earlier — and never executed. A later state (`references/npc_registry.yaml`, cited repeatedly inside the comprehensive audit's verifier notes as "the declared source of truth for ALL named characters") shows this fix was eventually attempted.
- STATUS IN DOC: none stated as fixed; PROVISIONAL throughout
- REDISCOVERED IN: independently identified by two audits (2026-05-07/08 character-generation-audit and 2026-06-22 comprehensive audit) five weeks apart.

**F-I-11 — A 52-mechanic full inventory of the character/NPC system, with a "per-decision consultation count" load test**
- SOURCE: designs/audit/2026-05-08-character-mechanics-critical-audit.md §1, §5
- CATEGORY: mechanism
- SUBSTANCE: Enumerates every character-attached mechanic (52, in 9 categories) and stress-tests them against realistic decisions. Pre-cuts, a single dialogue decision required consulting 17 distinct systems (self-audit-cascade names the same 17). Post-cuts, three worked scenes (social, combat, Domain Action) each stay at a 4–7 consultation ceiling. The explicit design principle: "specificity earns its place by what the player consults during a decision, not by what the engine could in principle track."
- WHY IT MAY STILL MATTER: A concrete, numeric complexity-budget technique specific to NPC/character mechanism design, directly actionable for any future NPC system redesign, with a named target (≤7 strategic-scale, 3–4 personal-scale per the companion immersion audit).
- STATUS IN DOC: none — self-produced audit conclusion, apparently never re-verified after this pass
- REDISCOVERED IN: independently reached by both 2026-05-08-self-audit-cascade.md (17→7 count) and 2026-05-08-meta-audit-immersion.md (recommends tightening personal-scale further to 3–4) — three documents converging on the same metric.

**F-I-12 — Five real naming collisions where one term means two mechanically different things**
- SOURCE: designs/audit/2026-05-08-character-mechanics-critical-audit.md §3.2
- CATEGORY: ontology
- SUBSTANCE: "Belief" = NPC first-person truth-statement vs. PC engagement-counted aspiration. "Inspiration" = PC aspirational arc vs. NPC author-shorthand (historical parallel + in-character aspiration). "Spirit" = attribute-pool stat vs. metaphysical will-to-grip stat (both quantitative, worse than the others). "Stance" = composite triangle vs. simple ally/neutral/opposed positioning. "Goal" = implicit AI-prose field vs. faction Mission's `primary_objective`.
- WHY IT MAY STILL MATTER: Concrete, still-open naming defects in exactly the kind of vocabulary this repo's own conventions section cares about; each collision names a real fork in what the underlying mechanic should be called going forward.
- STATUS IN DOC: none — flagged, unresolved (F8–F10 in the same doc's open-question list)
- REDISCOVERED IN: single source

**F-I-13 — F1–F15: fifteen specific, still-open design questions Jordan was asked and (within this corpus) never answered**
- SOURCE: designs/audit/2026-05-08-character-mechanics-critical-audit.md §7
- CATEGORY: problem-only
- SUBSTANCE: Numbered, presumably-actionable questions including: is Recall load-bearing beyond gating Sparking (F1)? Are Cognition/Focus/Endurance/Charisma/Bonds sub-pools independent tracks or derived from Mind/Body/Spirit — i.e., is a character 3 stats or 8 (F2)? Is Renown mechanically distinct from per-faction Standing, or derivable from it (F3)? Is Caste an actual mechanical floor on Standing ladders, or narrative-only (F4)? Are Stance triangles still queried by the engine as a composite, or vestigial (F5)? Do 9–10 of the 13 Convictions ever get meaningfully engaged in a campaign, or are they "landscape" (F11)? Are anti-Convictions (active opposition, vs. merely low weight) modeled at all (F12)? Does Self-Other's single scalar need per-relationship targets, e.g. toward-this-specific-parent (F13)?
- WHY IT MAY STILL MATTER: These are exactly the kind of sharply-stated, never-resolved design problems the brief flags as high-value regardless of implementation status — several (F2, F11, F13) bear directly on whether the NPC stat model is over- or under-specified.
- STATUS IN DOC: "Awaiting Jordan response on F1–F15" — no resolution recorded anywhere in this lane's files.
- REDISCOVERED IN: single source

**F-I-14 — Faction↔NPC succession is actuarial: named leaders die by an annual percentage roll, and player investment does not carry over by default**
- SOURCE: designs/audit/npc_faction_arc_interdependency_2026-04-18.md Throughline 5, Part VI
- CATEGORY: faction
- SUBSTANCE: Named faction heads carry an explicit annual death probability (Almud 12%/yr, Himlensendt 6%/yr, Ehrenwall 12%/yr, Baralta 6%/yr) feeding four simultaneously-latent succession crises (Crown/Church/Löwenritter/Hafenmark) that can converge in a single accounting period. Rule: "NPC Longevity death → succession fires; prior NPC investment does not transfer except where specified." A named open item (§8, PP-660) records that the original Generational Shift timeline (40 seasons) was corrected to ~10 seasons specifically so succession becomes mechanically reachable within campaign scope — without the fix, successions were functionally unreachable.
- WHY IT MAY STILL MATTER: A concrete mechanism for mortality-driven political churn, plus a documented instance of a numeric parameter (40→10 seasons) being tuned purely to make a designed system actually fire during play — a worked balance-correction case.
- STATUS IN DOC: "confirmed §8 correction" (design verdict marked resolved for the timeline fix; the "investment doesn't transfer" rule itself is stated as-is, not further justified)
- REDISCOVERED IN: single source

**F-I-15 — Obligation as a distributed, network-propagating consequence engine**
- SOURCE: designs/audit/npc_faction_arc_interdependency_2026-04-18.md Throughline 6
- CATEGORY: mechanism
- SUBSTANCE: Grand-Contest Obligations persist 4 seasons and, when violated, apply a network effect: "all NPCs Disposition ≥+1 with the violating faction: −1 Disposition" — i.e., breaking a promise doesn't just hurt the relationship with the counterparty, it degrades standing with every third party already favorably disposed toward you. Design verdict calls this "the most over-performing mechanic in the game... a 3-Obligation cascade produced 7 correctly targeted consequences with no conflicts."
- WHY IT MAY STILL MATTER: A named, specific propagation rule (through positive-Disposition edges) for how a single social/political act should ripple through an NPC relationship network — a reusable technique distinct from a simple point-to-point Disposition change.
- STATUS IN DOC: "confirmed ST-28" (design verdict, apparently validated against a simulation/playtest run)
- REDISCOVERED IN: single source

**F-I-16 — Character history (Lifepath) is simultaneously narrative content and mechanical output, structured to produce built-in biographical contradiction**
- SOURCE: designs/audit/character_histories_audit_2026-05-07.md STRUCT-1, STRUCT-2, "What's strong" §6
- CATEGORY: derivation
- SUBSTANCE: The 4-stage Origin/Formation/Vocation/Catalyst lifepath generator produces, per stage-choice, both prose *and* mechanical output (skills, Knots, starting Belief, Certainty modifiers) — never one without the other. The design's own stated principle: "a Crown Heartland Child with Practitioner Mentorship and a Church Vocation is a character whose biography is an argument with itself" — i.e., the generator is explicitly built to produce internally contradictory characters as a feature, with the contradiction driving later play tension. So "history" here is neither a raw event-list nor a pure derived-trait bundle — it's a small number of discrete authored life-stage choices, each dual-purposed as flavor text and as a mechanical unlock/Knot/Belief seed.
- WHY IT MAY STILL MATTER: A clean, general answer to "how should a character's past be represented" that avoids both extremes (free-text backstory vs. abstract trait sums) — worth preserving as a technique independent of Valoria's specific stage names.
- STATUS IN DOC: "The system is structurally sound" (explicit positive verdict) — but Stage 3 (Vocations) was entirely unwritten at time of audit (headers only, ~20–30 entries needed) and never confirmed filled within this lane's files.
- REDISCOVERED IN: single source; corroborated by character-mechanics-critical-audit's independent positive verdict on Lifepath ("KEEP... character creation chassis... 4 stages produces wide combinatorial space").

**F-I-17 — Caste-marked origin has explicit narrative weight but zero specified mechanical translation — flagged as a design gap, never closed**
- SOURCE: designs/audit/character_histories_audit_2026-05-07.md CASTE-1, CASTE-2, Editorial item ED-NEW-A (High severity)
- CATEGORY: problem-only
- SUBSTANCE: The Southern Einhir Descendant origin (245 years of Church suppression) is narratively precise but has no specified mechanical surface: does it set a different starting faction Standing, Social Contest Ob modifiers, a Renown floor/ceiling, or information-access gating? Same open question for Crown Heartland privilege and Himmelenger Church proximity. Explicitly logged as High-severity, unblocking player-facing character creation, with a proposed editorial item (ED-NEW-A) — no resolution recorded in this lane's material.
- WHY IT MAY STILL MATTER: A precise, still-open question about whether social/caste background should be pure flavor or should mechanically gate faction relationships and information access — directly relevant to any settlement/governance franchise or standing system.
- STATUS IN DOC: GAP (explicit), proposed but unresolved
- REDISCOVERED IN: single source

**F-I-18 — Personal-scale immersion requires the mechanism to become invisible; naming the mechanic to the player is itself a design failure mode**
- SOURCE: designs/audit/2026-05-08-meta-audit-immersion.md §3, §5
- CATEGORY: player-agency
- SUBSTANCE: Argues NERS-soundness and immersion are different, sometimes opposing, axes — a mechanically excellent system can still "surface too much of itself." Contrasts "Conviction weight exceeds salience threshold" (destroys immersion) with "my Faith is shaken" (preserves it) as the *same underlying mechanic*, differing only in presentation. Concludes every NPC-facing mechanic needs an explicit presentation-layer translation as a first-class design deliverable, not an afterthought, and that personal-scale scenes should target 3–4 consultations (vs. 7 for strategic scenes).
- WHY IT MAY STILL MATTER: A durable design principle specifically about how NPC psychological mechanism should surface to the player — distinct from, and complementary to, the raw mechanism design covered elsewhere in this lane.
- STATUS IN DOC: none — self-produced conclusion, not contested elsewhere in this lane
- REDISCOVERED IN: single source (game-design-process content, included per brief's allowance for material bearing on the game itself)

### DEAD ENDS
- **Legacy Conviction taxonomies (7-set and 9-set).** Explicitly superseded by the 13-Conviction taxonomy (PP-684), remapping Reason→Scholastic/Authority, Continuity→Warden, Autonomy→Liberty. `designs/audit/2026-06-22-npc-comprehensive-audit.md:652–693`; `designs/audit/2026-05-08-character-generation-audit.md` P1. Killed by PP-684; do not resurrect the 7/9-set labels or their example alliance/incompatibility pairs from F-I-5 without remapping.
- **"~87% degenerate win-share" balance claim** — not in this lane's files but cross-referenced from CLAUDE.md §5–7 restoration; not rediscovered independently in this lane, so no action needed here, only a caution that this lane's throughline "Design verdict: confirmed STXX" citations (F-I-14, F-I-15) are from a 2026-04-18 doc predating that retraction and should not be assumed still current without re-verification.
- **`values_master.yaml`-style free-text ethics tags as mechanical Ob drivers.** The Ethical Framework label system (F-I-6) is explicitly retired as a *mechanical* input; retaining it as *descriptive* flavor is the only surviving use. Any future NPC mechanism should not resurrect direct Ob-modifiers keyed to prose ethics labels.
- **Stance triangles as a queried composite object.** Flagged in `designs/audit/2026-05-08-character-mechanics-critical-audit.md` §2.6 (30) and §7 F5 as possibly vestigial post-PP-684 (its three components — Conviction, Resonant Style, Goal — now exist as independent fields). Never confirmed either way within this lane; treat as suspect, not load-bearing, until re-verified.

### OPEN QUESTIONS NEVER ANSWERED
- Do 9–10 of a character's 13 Convictions ever get meaningfully engaged across a campaign, or are they permanent "landscape"? (`2026-05-08-character-mechanics-critical-audit.md` F11)
- Are the 5 attribute sub-pools (Cognition/Focus/Endurance/Charisma/Bonds) independent tracks or derived from Mind/Body/Spirit — is a character mechanically 3 stats or 8? (same doc, F2)
- Is Renown mechanically distinct from per-faction Standing, or should it simply be derived (max or sum) from Standings? (same doc, F3)
- Does caste-marked origin (Southern Einhir, Crown Heartland, Church proximity) translate into any starting Faction Standing, Social Contest Ob, Renown, or information-access modifier — or is it pure narrative texture? (`character_histories_audit_2026-05-07.md` CASTE-1/2, ED-NEW-A)
- Should Self-Other be a single self↔collective scalar, or does it need per-relationship targets (toward this specific parent/lover/rival)? (`character_mechanics-critical-audit.md` F13)
- Are anti-Convictions (active opposition, not merely low weight) a real gap, or already covered implicitly by Beliefs? (same doc, F12)
- What are the ~20–30 Stage-3 Vocation entries (2 skills, faction relationship, Knot template per vocation) — the most mechanically dense part of character generation was entirely unwritten at last audit. (`character_histories_audit_2026-05-07.md` STRUCT-1)
- Is Caste actually functioning as a mechanical floor/ceiling on faction Standing ladders in play, or is it narrative-only? (`character_mechanics-critical-audit.md` F4)