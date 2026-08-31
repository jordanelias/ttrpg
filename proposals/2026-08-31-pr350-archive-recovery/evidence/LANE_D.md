## LANE D — NPC Modelling, Attributes, NERS & Investigation (archives/audit)

### COVERAGE
files_assigned: 40 | files_opened: 26 | files_read_closely: 17

skipped: 12 raw JSON graph/token files under `2026-04-30-terminology-vector-audit/data/` — the four prose reports (`00_workplan`, `01_methodology`, `02_weakness_register`, `03_validation_report`) already surface every finding these encode. `2026-06-11-threadwork-resolution-diagnostic/{ners_alldirections,resolution_diagnostic,sigma_results,threadwork_crosssystem_mapping,threadwork_flattened_spec}_2026-06-11.md` — grepped for faction/NPC/settlement/governance terms rather than read cover-to-cover; threadwork's own dice/pool mechanics are out of scope and the master analysis + grep hits captured every in-scope cross-reference. Two `.mermaid` diagrams (threadwork) — restate state machines already in the prose master analysis. `ledger_candidates_jsonl_ready.jsonl` (investigation lane) beyond its first two rows — verified by sampling that it restates `00_MASTER.md` findings in ledger schema, nothing new.

### FINDINGS (ranked most valuable first)

**F-D-1 — Disposition has no canonical home, and that absence is *why* it forked three ways**
- SOURCE: `2026-04-30-terminology-vector-audit/02_weakness_register.md:195,203` (§6 Mode D); `2026-06-10-investigation-exploration-diagnostic/00_MASTER.md:25-39` (P1-1)
- CATEGORY: ontology
- SUBSTANCE: A pure citation-graph audit (2026-04-30) found "Disposition" is a 391-citation cascade terminal with **no first-class doc** — it exists only inside `alias_registry` as `category: stat`, buried across NPC Behavior + faction docs. Six weeks later, a full-depth mechanics audit found the predicted consequence: master `fieldwork_v30`, `params/fieldwork.md`, and `investigation_systems_v30` each state a **different** Disposition range/ceiling/Ob-formula (−3..+5 stepped-Ob vs −4..Bonds direct-subtraction vs −4..⌊Bonds/2⌋+1), and the master's own rupture rule resets Disposition to −4, below its own stated −3 floor.
- WHY IT MAY STILL MATTER: a general lesson independent of Valoria's specifics — a mechanic cited everywhere but *owned* nowhere will drift, and a citation-graph sweep can predict exactly which concepts are about to fork before anyone reads the prose closely enough to catch it.
- STATUS IN DOC: none (both are audit findings, not ratified)
- REDISCOVERED IN: two independently-produced audits, six weeks apart, that plainly did not read each other — the strongest rediscovery signal in this lane.

**F-D-2 — A failed investigation deliberately produces a false belief the player cannot distinguish from a true one**
- SOURCE: `2026-06-10-investigation-exploration-diagnostic/resolution_diagnostic_fieldwork.md:39` (RD-7); `system_map_fieldwork_investigation.md:175-180` (state graph)
- CATEGORY: mechanism
- SUBSTANCE: Reconstruct-at-threshold Failure yields a **false conclusion**, explicitly GM-concealed ("GM does not reveal the error"), only reopenable if later evidence contradicts it. This is audited and confirmed *design-explicit*, not a bug — "knowledge" in this system is not a monotonic truth-accumulator; it includes indistinguishable false positives with their own recovery path.
- WHY IT MAY STILL MATTER: directly answers the lane's knowledge-representation question — a per-character "belief" state must model confident wrongness, not just accumulated fact, or the mechanic degenerates into a disguised binary.
- STATUS IN DOC: "intent-gated PASS" (audit verdict, not canon status)
- REDISCOVERED IN: single source

**F-D-3 — The NPC decision substrate: a Genome + a five-stage deterministic response filter, not a roll**
- SOURCE: `2026-06-10-investigation-exploration-diagnostic/system_map_fieldwork_investigation.md:88-127` (§A2), `:301-305` (NPC Genome row), `00_MASTER.md:89-91` (NULL: Five-Filter Chain)
- CATEGORY: npc
- SUBSTANCE: An NPC's response to any utterance is decided by chaining five ordered filters — Information (Certainty+TS set interpretive frame), Conviction (wound state, may escalate to Contest or fire an Arc), Disposition (block/defensive/neutral/engaged/transparent bands), Compromise (does the offer match a Compromise Profile), Ethical Framework (style vs faction alignment) — over an NPC Genome of Stance-per-issue, Worldview (1-2 convictions from an 8-item list), hidden Affiliation, Compromise Profile, and Volatility. The chain is deterministic and pass/modify/block/escalate at every stage; dice only ever feed the *evidence clock*, never the disclosure decision itself.
- WHY IT MAY STILL MATTER: this is a validated ("examined, nothing found" — full-chain example traced end to end) template for NPC decision logic that is legible, ordered, and explicitly *not* a black-box roll — the answer to "how does an NPC decide" this lane was asked to find.
- STATUS IN DOC: none flagged as superseded; re-confirmed at full depth in this audit after surviving an earlier index-depth pass
- REDISCOVERED IN: single source, but corroborated by combat/social cross-references in `threadwork_crosssystem_mapping_2026-06-11.md:14,20`

**F-D-4 — NPC awareness is explicitly gated, not ambient: the model does not let an NPC read state it hasn't earned**
- SOURCE: `2026-06-10-investigation-exploration-diagnostic/system_map_fieldwork_investigation.md:135-165` (§B Exposure state graph)
- CATEGORY: npc / ontology
- SUBSTANCE: Per-territory Exposure only becomes NPC-visible in bands: at "Noticed," only NPCs already at Disposition ≤0 become aware; at "Watched," a dominant faction *may* respond; at "Compromised," all territory NPCs' Disposition drops and cover is blown. Reduction tools exist (concealment roll, cover identity, leaving) and the whole track resets each season. A separate §2.5 "NPC-learns-investigated" hook is cross-referenced but not itself expanded in this audit's read set.
- WHY IT MAY STILL MATTER: directly answers the brief's question about NPC omniscience — the audited design is a bounded, damped feedback loop (confirmed via Stage-4 loop attack in `ners_verdict_fieldwork.md:69`, "survived — intent-gated pass"), i.e. the corpus already contains a worked answer to "how do we stop NPCs from cheating."
- STATUS IN DOC: none
- REDISCOVERED IN: single source

**F-D-5 — Evidence is a persistent multi-threshold clock, and knowledge scope moves from per-character to shared at a named seam**
- SOURCE: `2026-06-10-investigation-exploration-diagnostic/system_map_fieldwork_investigation.md:406` (C5 Outputs table, "Map state" row); `00_MASTER.md:91` (NULL: Evidence Track)
- CATEGORY: derivation
- SUBSTANCE: Evidence accumulates on a 3/5/8 threshold clock that never decays and never regresses on its own (only Mode-1 Anomaly aging or Thread-verification explicitly halves it). The flattened-spec output table records map/site visibility explicitly as "**per character → party**," i.e. the corpus already draws the per-character-vs-global line the lane brief asked about, at the map-discovery layer specifically (not stated as general policy for all knowledge types).
- WHY IT MAY STILL MATTER: gives a concrete, audited precedent for "discovered by one PC, shared with the party" rather than a vague design intention — useful as a citation the next time this exact question is re-litigated.
- STATUS IN DOC: none
- REDISCOVERED IN: single source

**F-D-6 — Domain Action, the faction-resolution mechanism itself, is also a buried concept — and Mandate was ruled to be *derived*, never directly written**
- SOURCE: `2026-04-30-terminology-vector-audit/02_weakness_register.md:200,204`; `2026-06-19-ratification/ratification_decisions_2026-06-19.md:35` (#3, J-7)
- CATEGORY: governance / faction
- SUBSTANCE: "Domain Action" is a 346-citation cascade terminal with no canonical doc — the glossary only mentions it in passing under "Zoom In." Separately, Jordan ruled (2026-06-19) that **Mandate is derived from per-territory Legitimacy/Popular-Support**, not written directly — "stop direct +/-Mandate writes; route Echoes through dL/dPS aggregated over held territories" — queued as a faction-layer sweep, not yet executed at record time.
- WHY IT MAY STILL MATTER: a durable governance-architecture principle ("a legitimacy-like aggregate must be computed from its territorial inputs, never hand-set") that stands regardless of whether the specific sweep ever landed; worth re-checking if Mandate/legitimacy is ever touched again.
- STATUS IN DOC: ruling = "QUEUED (faction-layer sweep)"
- REDISCOVERED IN: single source

**F-D-7 — Domain Echo: one throttled writeback channel reused by three unrelated personal-scale systems**
- SOURCE: `2026-06-11-threadwork-resolution-diagnostic/threadwork_flattened_spec_2026-06-11.md:230` and `threadwork_master_analysis_2026-06-10.md:57` (§2.5); `2026-06-10-investigation-exploration-diagnostic/system_map_fieldwork_investigation.md:85,397` (XSYS)
- CATEGORY: seam / mechanism
- SUBSTANCE: Faction-scope Findings (investigation), faction-scope thread operations, and (per cross-reference) mass-battle outcomes all route personal-scale consequences into faction stats through the *same* named primitive — Domain Echo — capped at roughly ±1-2 per season with a 1/scene/faction throttle, queued to Accounting rather than applied instantly.
- WHY IT MAY STILL MATTER: a genuinely single-owned cross-scale primitive (the kind CLAUDE.md's "build bottom-up from primitives" now asks for) that three independently-audited subsystems converge on — worth preserving as the pattern for *any* personal-action-feeds-faction-stat bridge, rather than re-inventing per system.
- STATUS IN DOC: none
- REDISCOVERED IN: threadwork master analysis, threadwork flattened spec, and the investigation system map — three same-corpus documents citing the identical mechanism (ED-673) independently in their own domains.

**F-D-8 — NPC priority trees hardcode geography, and the mandatory-vs-stochastic action precedence is undocumented**
- SOURCE: `2026-05-20-npc-priority-trees/audit_findings.md:73-81` (S-7), `:99-103` (A-2), `:9-13` (D-1)
- CATEGORY: npc / problem-only
- SUBSTANCE: Crown's P4 priority row hardcodes a specific territory pair ("if T2 Kronmark ungarrisoned AND Varfell unit active in T4 → deploy garrison"), the only asymmetric faction-vs-faction rule of its kind, flagged as needing explicit canon backing before authoring it into `npc_ai.py`. Separately, the doc never states whether GD-2's mandatory-action pass (Muster/Govern) consumes a priority slot before the stochastic priority tree fires, or runs independently. (A structural dedup defect — the entire tree duplicated verbatim across two blocks — was also found and is purely mechanical.)
- WHY IT MAY STILL MATTER: a clean, still-live instance of exactly the "scripting drift" CLAUDE.md's §0 now names as a stop condition — special-casing one entity pair inside a general decision structure — worth citing as a worked example if that guardrail is ever explained to a new session.
- STATUS IN DOC: "Decision required" (open at time of audit, pre-implementation — consumer `npc_ai.py` was a stub)
- REDISCOVERED IN: single source

**F-D-9 — World-substrate collapse has a concrete, named governance-collapse mechanic**
- SOURCE: `2026-06-11-threadwork-resolution-diagnostic/threadwork_flattened_spec_2026-06-11.md:164`
- CATEGORY: governance / world-churn
- SUBSTANCE: At the MS ("Metaphysical/Rendering Stability," terminology later unified) Critical band (19-1), factions roll a Stability check each season; failure costs Mandate −1, and Mandate reaching 0 triggers **Faction Fracture**. The same band adds +1 to coup/succession triggers once MS ≤10. This is the concrete mechanical link between world-state decay and a faction's constitutional collapse.
- WHY IT MAY STILL MATTER: a specific, numbered answer to "how does world churn threaten governance" that a designer would otherwise have to re-derive from scratch.
- STATUS IN DOC: none flagged as struck; recorded as live canon at audit time
- REDISCOVERED IN: single source

**F-D-10 — Attribute-roster architecture (flat vs. grouped) was live-contradicted by the game's own data, not just undecided in prose**
- SOURCE: `2026-06-04-attributes-derived-ners/03_ADVERSARIAL.md:14-17` (A2); `02_COMPARATIVE.md:13-25` (Comparison 1)
- CATEGORY: ontology
- SUBSTANCE: A first pass called the Mind/Body/Spirit-vs-flat-~10 question "genuinely unresolved" from absence of a roster doc. The adversarial pass tested this against ground truth: the NPC Edeyja's stat block is stated flat ("Cognition: 5, Focus: 5, Endurance: 4"), matching the combat engine's flat fields — so the live system *is* flat, and the macro framing is vestigial, not a competing live option. A comparative pass independently confirms both flat (D&D/SPECIAL) and grouped (WoD 3×3, Disco Elysium 4-macro) are acclaimed-viable; the actual defect was carrying both framings labeled as canon simultaneously.
- WHY IT MAY STILL MATTER: a methodology lesson as much as a content one — "no roster doc" was treated as "undecided," when checking one NPC's stat block against the engine settled it in one grep.
- STATUS IN DOC: none formally struck at time of writing
- REDISCOVERED IN: single source (self-correction within the same audit)

**F-D-11 — Spirit/Recall is a documented "mandatory tax stat + dump stat" pair, validated against genre precedent**
- SOURCE: `2026-06-04-attributes-derived-ners/01_DIAGNOSTIC.md:44-53` (Mode C); `02_COMPARATIVE.md:51-58` (Comparison 5), `:27-34` (Comparison 2)
- CATEGORY: derivation
- SUBSTANCE: Post-two-ratifications (S1, ED-902), Spirit feeds five downstream values (Stamina, Concentration, Thread Fatigue, Inspiration cap, Sincerity Gate) — a cross-pillar "you want this whatever you play" stat, explicitly likened to D&D Con/Dex over-centralization. Recall feeds almost nothing live. The comparative pass adds nuance: Disco Elysium's *Encyclopedia* proves a thin-seeming knowledge stat can be excellent *if it gates rich content* — so Recall's actual defect is "nothing to gate," not "recall stats are bad."
- WHY IT MAY STILL MATTER: a reusable diagnostic pattern (downstream-load counting + genre precedent) for catching over/under-centralized stats before they ship, and a specific caution against folding Recall into Spirit (which would *worsen* the very asymmetry being fixed — caught by the adversarial pass).
- STATUS IN DOC: none (audit-only)
- REDISCOVERED IN: converges with the 2026-05-08 prior character-mechanics audit cited throughout `01_DIAGNOSTIC.md §A`

**F-D-12 — "Freshness" was proven not to imply mutual consistency, on exactly the mechanic that matters here**
- SOURCE: `2026-06-04-attributes-derived-ners/03_ADVERSARIAL.md:49-52` (B1, B4)
- CATEGORY: problem-only
- SUBSTANCE: `canonical_sources.yaml` listed both `params/contest.md` (Recall/Bonds attribute model) and `social_contest_v30.md` (Composure/Conviction model) as canonical with equally fresh SHAs — two incompatible attribute models for the same social-contest engine, both passing the corpus's own staleness check. "All 114 sources fresh" gave false comfort because SHA-freshness verifies staleness-of-a-file, not agreement-between-files.
- WHY IT MAY STILL MATTER: a load-bearing methodology gap that will recur for any future "freshness gate" unless a mutual-consistency check is added alongside it.
- STATUS IN DOC: "B1 [P1, durable]"
- REDISCOVERED IN: single source

**F-D-13 — A designed doom-loop that was deliberately left unbuilt, and why**
- SOURCE: `2026-06-11-threadwork-resolution-diagnostic/threadwork_master_analysis_2026-06-10.md:57` (§2.5); `resolution_diagnostic_threadwork_2026-06-11.md:78` (L5)
- CATEGORY: seam / world-churn
- SUBSTANCE: World-substrate collapse (MS Critical) causes Mandate loss and Faction Fracture (F-D-9), but no canonical mechanism makes a *fractured* faction perform more Thread operations in return — the audit explicitly checked for this return edge, found none, and flagged it "to keep it that way," pointing at the NPC-AI-doctrine integration point (ED-679) as the intended (not-yet-built) place such a coupling would live if ever added.
- WHY IT MAY STILL MATTER: a rare case of an audit recommending an absence be preserved rather than filled — evidence that the missing mechanism is a deliberate firebreak against a runaway world-collapse spiral, not an oversight, and should not be "completed" reflexively.
- STATUS IN DOC: "[UNGROUNDED return edge]", flagged deliberate
- REDISCOVERED IN: single source

**F-D-14 — Knot (bonded-relationship) lifecycle: a mature, verified five-state machine reusable beyond its own subsystem**
- SOURCE: `2026-06-10-investigation-exploration-diagnostic/system_map_fieldwork_investigation.md:222-254` (§B KNOT); `00_MASTER.md:93`
- CATEGORY: npc / mechanism
- SUBSTANCE: NoKnot → EligibleScene → Distant/Close → {Broken, Ruptured, Dissolved, Memory} with explicit strain accrual (six named sources), decay, and break-at-Accounting timing. Verified via a stress test at 22/24 NERS cells, with two pre-known low-Bonds lockout edge cases.
- WHY IT MAY STILL MATTER: a genuinely load-tested template for any PC-NPC bonded relationship system (companions, rivals, political allies) independent of the specific Thread-magic dressing.
- STATUS IN DOC: "mature" (audit verdict); the underlying *values* (strain caps, formation formula) are separately forked — see open questions below
- REDISCOVERED IN: single source

**F-D-15 — Ratified governance decisions that had not yet reached the corpus body at record time**
- SOURCE: `2026-06-19-ratification/ratification_decisions_2026-06-19.md:33-50` (§1, rows #1, #3, #5, #14)
- CATEGORY: governance
- SUBSTANCE: Four rulings landed as *decisions* but explicitly deferred as *propagation*: victory threshold = all 15 territories (not 11+), Mandate-derivation sweep (F-D-6), unify TT/RS/Metaphysical naming into "MS," and strike the Niflhel faction outright (canon/03 row + Viability Matrix + LA-13 sweep).
- WHY IT MAY STILL MATTER: a dated snapshot of exactly which governance/faction rulings were "decided but not yet true in the files" — useful for anyone reconstructing when a given rule actually took effect versus when it was merely ruled.
- STATUS IN DOC: "QUEUED" for all four
- REDISCOVERED IN: single source

**F-D-16 — A named faction (Niflhel) was struck by ruling, yet its content kept resurfacing across unrelated subsystems for months**
- SOURCE: `2026-05-20-npc-priority-trees/audit_findings.md:59-65` (S-5, Varfell/Warden Recognition tangle); `2026-06-10-investigation-exploration-diagnostic/00_MASTER.md:60` (P2-4); `2026-04-30-terminology-vector-audit/02_weakness_register.md:29,54,66`
- CATEGORY: problem-only
- SUBSTANCE: Niflhel-as-faction was struck (ED-764) yet its Social Toolkit and exposure bonus remained live in `fieldwork_v30 §5.8/§6.3` as of 2026-06-10, and 10 of 23 corpus mentions were still concentrated (unresolved) in two files as of the 2026-04-30 terminology audit. A related VTM/Warden-Recognition strike left the npc-priority-trees doc unable to tell whether an adjacent mechanic (Warden Recognition) survived the same strike.
- WHY IT MAY STILL MATTER: this is not one bug but a recurring pattern across this whole corpus (also true of VTM, Cultural Reformation, Coup Counter, Cohesion per the same terminology audit) — a ruling and a landed edit are different events, and nothing here closed that gap automatically.
- STATUS IN DOC: "STRUCK" (ED-764) at ledger level; "live" in multiple prose bodies
- REDISCOVERED IN: independently flagged by the npc-priority-trees audit, the investigation-diagnostic audit, and the terminology-vector-audit — three separate sessions.

**F-D-17 — Contested investigation: an active adversarial-concealment roll, not a static gate**
- SOURCE: `2026-06-10-investigation-exploration-diagnostic/system_map_fieldwork_investigation.md:41` (OBC), `:318` (C2 #5), `:375` (C4 #7)
- CATEGORY: mechanism
- SUBSTANCE: When a concealer (NPC or faction agent) is present, they roll `Cognition×2+History`; net successes become *added* Ob for the investigator, applied per-scene — a genuine two-sided information contest layered on top of the static perception/depth gates, with an institutional variant (Church Tribunal Heresy Investigation, +1D/+2 Ob).
- WHY IT MAY STILL MATTER: a concrete worked example of "an NPC actively resists being investigated" distinct from passive concealment stats — useful precedent for any future adversarial-knowledge design.
- STATUS IN DOC: none
- REDISCOVERED IN: single source

**F-D-18 — Self-correcting audit methodology: over-stated verdicts narrowed by a mandatory adversarial re-pass**
- SOURCE: `2026-06-04-attributes-derived-ners/03_ADVERSARIAL.md` (Part A, A1-A5)
- CATEGORY: problem-only
- SUBSTANCE: The diagnostic-stage verdict ("Recall = clean fold," "R/S: FAIL broadly," "structure genuinely unresolved") was walked back point-by-point in the next stage using primary evidence the first pass hadn't checked (contest.md's actual Recall usages, Edeyja's stat block, today's own edit-lag). The corrected verdict is narrower and more defensible on every walked-back point.
- WHY IT MAY STILL MATTER: a worked demonstration, from this project's own history, that a single-pass audit self-confirms and a mandated adversarial second pass is what catches it — direct precedent for CLAUDE.md §0's current adversarial-pass requirement.
- STATUS IN DOC: none (methodology narrative)
- REDISCOVERED IN: single source

### DEAD ENDS
- **"Recall is a near-orphan, fold it"** (`01_DIAGNOSTIC.md:114`) — retracted by `03_ADVERSARIAL.md:9-12` (A1): the premise missed that `params/contest.md`, itself still declared canonical, gives Recall ~5 live roles. Reduced to a 3-path, Jordan-contingent decision.
- **"§1: one attribute × multiplier, no combinations" as a real defect when violated** (`01_DIAGNOSTIC.md:38`) — reversed by `02_COMPARATIVE.md:45-49`: acclaimed games (D&D HP, Battle Brothers fatigue) routinely combine attributes; the *rule* was the defect, not the ratified multi-attribute formulas that broke it.
- **"Fold Recall into Spirit/Mind"** (`01_DIAGNOSTIC.md:102`) — self-contradicted per `03_ADVERSARIAL.md:24-26` (A4): folding into the already-overloaded Spirit worsens the exact asymmetry the audit flagged. Corrected target: Cognition.
- **"Combat's stat-economics diverging from siblings is a lateral S-failure"** (`01_DIAGNOSTIC.md:83`) — softened by `02_COMPARATIVE.md:60-64` to a documentation gap; the divergence itself (skill-driven pool + attribute-as-leverage) is acclaimed-normal (Mount & Blade, Battle Brothers).

### OPEN QUESTIONS NEVER ANSWERED
- Which social-contest attribute model is canonical: `contest.md` (Recall/Bonds), `social_contest_v30` (Composure/Conviction), or the 2026-06-03 groundup (pisteis+Standing)? Blocks Recall's fate. (`04_RECONCILED_MASTER.md` F-CONTEST)
- Disposition→Ob rule: stepped table vs. `max(1, base−Disposition)` direct subtraction — never resolved in this lane's files. (`00_MASTER.md §6` item 1)
- Disposition floor: −3 or −4? (`00_MASTER.md §6` item 2)
- Knot formation model: strain (ED-773, Spirit×2+History) vs. tier-cost (PP-632, Bonds-based) — open in two independent lanes (fieldwork's `00_MASTER.md §6` item 4 *and* threadwork's N9), never reconciled between them.
- Whether Spirit's five-way downstream load should be reduced, given it may be *deliberate* per two separate ratifications (S1, ED-902) — explicitly left "[OPEN TRADE-OFF]." (`04_RECONCILED_MASTER.md §4` item 5)
- What happens to a practitioner who hits Coherence 0 with no Close Knot available — entirely unstated. (`resolution_diagnostic_threadwork_2026-06-11.md` RD-3)
- Whether the missing "inbound Coherence drift for connected non-practitioners" (P-12) should be designed or the philosophical claim declared already satisfied by Knot strain pacing. (`threadwork_master_analysis_2026-06-10.md` N14)
- Six named npc-priority-tree mechanics (Royal Decree, Löwenritter Autonomy track, Crown's IP-trigger, Warden Recognition, the Church "Cardinal" mechanic, post-founding RM behavior) each flagged "confirm canonical source" with no resolution anywhere in this lane's files. (`2026-05-20-npc-priority-trees/audit_findings.md` S-2, S-3, S-4, S-5, S-6, S-8)
- Whether the 10 concentrated Niflhel-faction references in two files are genuine missed strikes or legitimate place-name references mis-flagged by the audit's regex — sampling was recommended, never performed in these files. (`02_weakness_register.md:66`)