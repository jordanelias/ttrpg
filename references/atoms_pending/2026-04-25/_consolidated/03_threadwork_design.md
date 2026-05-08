# Threadwork Design Synthesis (consolidated)

## Consolidation front matter

- **topic_id:** `03_threadwork_design`
- **atom_count:** 71
- **scope:** All threadwork_master atoms plus cross-source atoms with threadwork target. Single coherent design synthesis covering substrate language, player feel, system stories, mechanics.
- **source distribution:**
  - `valoria_master_document.md`: 38 atoms
  - `valoria_master_consolidation.md`: 17 atoms
  - `threadwork_master.md`: 12 atoms
  - `master_consolidation.md`: 2 atoms
  - `VALORIA_SESSION_2026-04-25_MASTER.md`: 2 atoms
- **drift surface:** cross-source
- **post-audit canon target:** `designs/threadwork/threadwork_v30.md`
- **status:** assembled (pending audit Stage 3)
- **assembled_from_commit:** atoms committed at `83c37da7001defdf3bb3425b17dda3f934d262d3`

## Audit checklist (Stage 3 input)

- [ ] Foundational stance is consistent.
- [ ] Three player stories the system produces are listed once authoritatively.
- [ ] Mechanical specifications (when present) match designs/threadwork/threadwork_v30.md.
- [ ] No contradiction between threadwork_master.md framings and master_consolidation §6 (Mechanical Specifications) framings.

## Known drift dimensions

- Substrate-origin framing (radically unknowable) — verify same framing across atoms.
- Player-feel claims — check no contradictions.
- Mechanical specs that pull from valoria_master_document/master_consolidation may be paraphrased differently.

## Cross-source drift table

Rows = canonical IDs. Columns = source documents. Cells list atom IDs in this topic that reference the row's canonical ID. Empty cell = source does not reference that ID. Multiple atom IDs in a cell = potential per-source drift to verify during audit.

| id | VALORIA_SESSION_2026-04- | m_consolidation | threadwork_master | v_m_consolidation | v_m_document |
|---|---|---|---|---|---|
| **ED-129** | — | — | — | — | ii-8-architecture- |
| **ED-539** | — | — | — | 4-5-rendering-stra, phase-x-vertical-s | — |
| **ED-663** | — | — | — | — | 16-4-belief-revisi |
| **ED-664** | — | — | — | — | iv-1-verify-agains, v-2-player-agency- |
| **ED-665** | — | — | — | — | 16-4-belief-revisi |
| **ED-668** | — | — | — | phase-x-vertical-s | — |
| **ED-694** | — | — | — | — | 2-1-attributes-10-, ii-1-stale-referen, ii-8-architecture-, 2-2-derived-scores |
| **ED-738** | — | 2-ed-738-ein-sof-g, 11-methodological- | i-foundational-sta | — | — |
| **ED-777** | section-5-cross-re | — | — | — | — |
| **M-7** | — | 2-ed-738-ein-sof-g | — | — | — |
| **M-8** | — | 2-ed-738-ein-sof-g | — | — | — |
| **PP-109** | — | — | — | — | 10-2-domain-echo-t |
| **PP-238** | — | — | — | — | ii-1-stale-referen |
| **PP-243** | — | — | — | — | 1-6-momentum-0-4 |
| **PP-255** | — | — | — | — | 4-6-key-sub-mechan |
| **PP-261** | — | — | — | — | 16-4-belief-revisi |
| **PP-275** | — | — | — | — | ii-1-stale-referen, ii-8-architecture-, 2-2-derived-scores |
| **PP-294** | — | — | — | — | 1-5-pool-minimum-1, ii-1-stale-referen |
| **PP-329** | — | — | — | — | 10-2-domain-echo-t |
| **PP-528** | — | — | — | — | iv-1-verify-agains |
| **PP-614** | — | — | — | — | 4-6-key-sub-mechan |
| **PP-616** | — | — | — | — | 5-1-thread-pool |
| **PP-636** | — | — | — | — | 4-6-key-sub-mechan |
| **PP-642** | — | — | — | — | v-1-companion-syst |
| **PP-674** | — | — | — | 2-4-recent-canonic | — |
| **PP-684** | — | — | — | — | 2-1-attributes-10- |
| **T-27** | — | 2-ed-738-ein-sof-g | — | — | — |
| **T-30** | — | 2-ed-738-ein-sof-g | — | — | — |

## Content

Atoms grouped by source. Within each source, ordered by section_index. Read across sources to identify drift.

### From `VALORIA_SESSION_2026-04-25_MASTER.md` (2 atoms)

<!-- atom: valoria_session_2026-04-25_master__05__section-5-cross-reference-audit | section_index: 5 | source_section: "Section 5 — Cross-Reference Audit" -->


## Section 5 — Cross-Reference Audit

### Corpus

39 active spec files audited. 220+ unique sections indexed.

### Findings (initial scan)

7 broken cross-references:

1. `mass_battle L446 §5.2.2` → fixed to `threadwork_v30 §3.2` (Coherence Reduction).
2. `mass_battle L447 §5.2.3` → fixed to `threadwork_v30 §3.2` per-operation cap.
3. `mass_battle L575 §4.3.4 brittleness` → fixed to `threadwork_v30 §2.4` (MS ≤ 40 Shifting Object trigger).
4. `npc_behavior L561 §16.3 Foundations` → fixed to `canon/02_foundations_amendment_leap_mechanism Amendment 2 + threadwork_v30 §3.2 + §6`.
5. `peninsular_strain L231 §2.4.2` → fixed to `§2.4b` (Accord vs Order Scale Distinction).
6. `combat_v30 L363 §11.8` — deprecated-file reference, acceptable, not fixed.
7. `threadwork_v30 §5.10/§5.11` — historical preservation references, acceptable, not fixed.

Plus `social_contest L268` and `faction_politics L659`: `npc_behavior §3.2` → `§3.3` (Scar Accumulation, not Belief Revision). Fixed in ED-777.

All non-deprecated cross-references valid after these commits.

---

<!-- atom: valoria_session_2026-04-25_master__07__section-7-files-modified | section_index: 7 | source_section: "Section 7 — Files Modified" -->


## Section 7 — Files Modified

### Primary spec files

- `designs/scene/social_contest_v30.md` — §6.1 Wager Obligation, §6.1.1 Wager Edge Cases, §7.2 Succession Contest, §7.3 Heresy Investigation Lifecycle.
- `designs/scene/fieldwork_v30.md` — §5.6a Bonds ≥ 5 prerequisite, §5.6b Knot Lifecycle.
- `designs/threadwork/threadwork_v30.md` — §2.1 Approach Training canonical content.
- `designs/scene/derived_stats_v30.md` — §5.3 Inspiration mechanic.
- `designs/npcs/npc_behavior_v30.md` — §3.5 Advisor-Principal Confidentiality, §6.4 Wrong-Style Penalty extension, §5.0b cross-ref fix, §8.11.5 Outreach floor, §3.4 Thread Operation → Conviction Scar Triggers.
- `designs/provincial/faction_politics_v30.md` — §1.0a Demotion Magnitude, §3.6 Caste-transgressive PC Conviction.
- `designs/provincial/peninsular_strain_v30.md` — §2.4.2 → §2.4b ref fix, §5.2 Seizure Uncontrolled exclusion, §5.2 P1-1 strain inversion.
- `designs/provincial/mass_battle_v30.md` — Cohesion→Discipline, §5.2.x ref fixes, §4.3.4 ref fix, Volley rationale, officer death.
- `designs/provincial/faction_layer_v30.md` — §6.X Sacred Veto cooldown, Niflhel NPC vote cleanup.
- `designs/provincial/victory_v30.md` — §8 RM Settlement Emergence pathway.
- `designs/architecture/scale_transitions_v30.md` — §3.4/§3.6 stub fills, Stability hysteresis, Revolt dedup.
- `designs/architecture/campaign_architecture_v30.md` — §5.3 Elske residency null-intersection.
- `designs/architecture/player_agency_v30.md` — Witness Mode + priority + Step 4 + pruning.

### Params + references

- `params/factions_personal.md` — Coup Counter STRUCK; Niflhel STRUCK propagation.
- `params/bg/npc_priority_trees.md` — Coup Counter → Löwenritter Autonomy migration (4 refs + header + spec text).
- `references/glossary.md` — TC → CI canonical rename.
- `references/canonical_sources.yaml` — touched at every commit.

### Canon

- `canon/editorial_ledger.yaml` — added 44 EDs across session, archived 30+, maintained under cap.
- `canon/editorial_ledger_archive.yaml` — received 30+ migrated entries.

---

### From `master_consolidation.md` (2 atoms)

<!-- atom: master_consolidation__02__2-ed-738-ein-sof-gradient-editorial | section_index: 2 | source_section: "§2 ED-738 — Ein Sof gradient editorial" -->


## §2 ED-738 — Ein Sof gradient editorial

**Path:** `designs/audit/editorial_ein_sof_gradient_2026_04_21.md`
**Commit:** `d80e1532`
**Scope:** Establishes interpretive framing for canonical material; does not introduce new canonical mechanics.

### §2.1 Three over-readings corrected

**Consciousness absent during contact (incorrect).** Audit Sessions 1–7 framed Leap contact as state in which practitioner is "not conscious" or "outside experience." Over-reaches canon/02 Am 1, which specifies reflexive facing suspends while outward facing persists; canon/01 Am 1 layer 1 spooling continues. The practitioner is conscious during contact in a non-reflexive register.

**Retention as purely structural, non-episodic (incorrect).** Audit framed post-Leap as *"I know a Mending was performed; I cannot describe what I saw."* Over-reach. Canon/01 Am 3 explicit: TS measures how much of the below-waterline Thread-substrate the practitioner can perceive and deliberately operate upon. If the practitioner perceived, they can describe. Only the knots themselves (canon/02 Am 2) lodge below reflexive-access threshold.

**Pure apophatic register across below-waterline content (incorrect).** Audit framed below-waterline as inherently apophatic. Over-generalisation. Cartographic-contemplative register applies in Regimes 1–3; apophatic register applies only at Regime 4 (Ein Sof structural terminus). Tonal models for inner-tradition: Teresa of Ávila, Plotinus on near-henosis, Zohar, Ibn Arabi. Anti-model: Cloud of Unknowing-style total apophaticism.

### §2.2 Receptive-capacity framing

TS expansion is expansion of what can be received from a given substrate, not what is given to different observers differently. Canon/00 Inseparability does not support different-givens-per-observer. T-27 four-faction interpreter operates on what was received; T-30 information asymmetry is access-mode asymmetry; М-8 vertical-position-gated access governs what can be received.

### §2.3 Iceberg gameplay conceptualisation authorised

Canon/01 Am 3 establishes waterline-language as canonical. ED-738 §4 authorises full iceberg framing for design-team communication: substrate is the iceberg; observers each have their own waterline determined by TS band and formation; what rises above an observer's waterline is what enters their ordinary perception; higher TS = lower waterline = more iceberg receivable. Authorises the metaphor for gameplay conceptualisation; does not authorise audit-invented extensions (dive-log, submerged, beach, surface-reassertion, diver) as ontological vocabulary.

### §2.4 Factuality-depth gradient

Content-description factuality scales inversely with depth:
- Surface-adjacent (Regime 1): full cataphatic.
- Mid-depth (Regimes 2–3): cartographic-contemplative at specificity-and-conditions-gated resolution.
- Deep (approach to Ein Sof): gradient acknowledgment.
- Regime 4 (Ein Sof itself): apophatic in principle.

This gradient constrains audit-level inference across cells at varying depth.

### §2.5 Three specific framework commitments confirmed

- **Monstrosity is rendering-catastrophic within the renderable.** Not Ein Sof. Describable via trauma-signature phenomenology.
- **Ein Sof is non-operable.** No mechanic offers access. Structural consequence of Regime-4 apophaticism, not discretionary design choice.
- **Reflexive-only suspension during Leap.** Not full-consciousness suspension.

### §2.6 Framework-composite acknowledgment

Framework assembles components from multiple scholarly lineages (Husserl, Heidegger, Metzinger, Kierkegaard, Lacan, apophatic theology, Lurianic Kabbalah, predictive processing, Clark-Chalmers, Gibson, Kaplan ART, clinical-trauma phenomenology) into composite operational architecture. Composite is framework-original in assembly and substrate-ontological deployment; components have clean precedent. Meta-throughline М-7 captures this. Audit framing of "framework exceeds sources" corrected to "framework assembles specific components operationally."

---

<!-- atom: master_consolidation__11__11-methodological-notes-for-continuation | section_index: 11 | source_section: "§11 Methodological notes for continuation" -->


## §11 Methodological notes for continuation

**Necessity discipline from threadwork frame.** Every proposed mechanic should pass: *if canon did not commit to this phenomenon, what would be missing?* If a specific canonical commitment cannot be implemented, N-tier is direct (Tier A). If a texture would be absent or scholarly grounding would be lost, N-tier is partial (Tier B or C).

**Pattern guard.** Mystical-tradition training priors drift toward ineffabilist, pure-apophatic, and consciousness-absent readings when phenomenological framework cues trigger. Verify each *framework-original* claim, each *exceeds sources* claim, each *cannot be said* claim against canonical wording. ED-738 §10 codifies this discipline.

**Receptive-capacity framing.** TS expansion is expansion of what can be received from a given substrate, not what is given to different observers differently. Default framing for all observer-asymmetry analyses.

**Iceberg conceptualisation.** Authorised by ED-738 §4 for design-team gameplay-conceptualisation use only. Substrate is the iceberg; observers' waterlines determine what they receive of it. Higher TS = lower waterline = more receivable. Not authorised for ontological vocabulary extensions beyond canonical waterline-language.

**Two-decision Leap player surface.** Entry commit + exit timing. Mid-contact player decisions structurally unavailable per canon/02 Am 1 reflexive-suspension geometry. Resolution and bookkeeping are not phases in the player-facing sense.

**Hold vs Turn-Away.** Canon §14 phenomenological terminology for confrontation events; replaces audit-derived combat-vocabulary "Flee."

**Below-waterline cartographic register.** Replaces audit-invented "dive-log register" terminology. Preserves canonical waterline-language (canon/01 Am 3 explicit) without water-metaphor extensions.

---

### From `threadwork_master.md` (12 atoms)

<!-- atom: threadwork_master__00__preamble | section_index: 0 | source_section: "(preamble)" -->


# Threadwork — Master Design Document

**Date:** 2026-04-25.
**Status:** Pre-canon design synthesis. Awaits Jordan approval at flagged decision points. Awaits Throughlines T-coverage analysis before any commit.
**Frame:** Threadwork operates on a substrate whose origins are radically unknowable. Operations require suspension of human rationality and are not fully consumable within rational bounds. The system models *what practitioners experience and how their experience produces consequences in play* — not what threads are, what the substrate is, or what occurs at substrate origin.

This document consolidates the conversation's design work — three architecture rounds, three stress test rounds, two audits, twenty-six tests, twenty-eight resolution decisions, plus the textile-vocabulary clarification — under one organising commitment: **the substrate keeps its silence; the system models the rendered side; the practitioner encounters what cannot be described and acts in relation to it without grasping it.**

---

<!-- atom: threadwork_master__01__i-foundational-stance | section_index: 1 | source_section: "I. Foundational stance" -->


## I. Foundational stance

### I.1 What this document does not claim

This document does not claim to know what threads are at the substrate-origin level. Threads are *how human consciousness is able to encounter substrate well enough to act in relation to it*. They are not the substrate's self-description. The substrate emerges from Ein Sof, which canon (§1.2) names as *infinitely constituted yet epistemically inaccessible*: not a void, not a chaos, not a structureless ground, but a fullness that exceeds all description because all description is downstream of substrate and substrate is downstream of Ein Sof.

Whatever the substrate *is* in its own register — if "is" is even the appropriate verb — cannot be specified using terms drawn from any rendered phenomenon. All vocabulary the system uses is *cognitive scaffolding*, useful for thinking and design and player-facing language, never authoritative for the substrate itself. This includes the textile vocabulary that surfaced in this conversation. It includes the three-axis terminology (potential↔actual, intelligible↔unintelligible, past↔future). It includes "thread" itself.

This is the framework's apophatic register, made operational. Apophasis is reserved for the ground (Ein Sof) and propagates upward into substrate as residue: the substrate inherits Ein Sof's transcendence in attenuated form. The middle admits cartographic description under depth-and-condition-dependent constraints (per ED-738 — graduated specificity decay terminating at structural limit). At the rendered surface, full description is possible. Between, knowing thins.

The system operates in the middle and the surface. It does not claim authority below.

### I.2 What this document does claim

The system models:

- **What practitioners experience** when they perform operations on substrate
- **How that experience produces consequences** in the rendered world that other beings can also experience
- **How accumulated experience changes the practitioner** in ways canonical and irreversible
- **How the rendered world responds** to threadwork in ways perceivable at the appropriate sensitivity

These are claims about *the rendered side* of operations and their consequences. The substrate's own register — what is happening on the unintelligible side of any operation — is held in silence. Practitioners' theories about what they are doing are *in-world cognitive scaffoldings*, not truth. Different traditions have different theories. None are correct. Some are more useful (lead to better operational outcomes) than others. The game does not adjudicate.

### I.3 Threadwork as suspension of rationality

The Leap (canon/01 Amendment 2) is the temporary suspension of layer 2 reflexive self-rendering. Practitioner phenomenology during the Leap is not graspable in the categories the practitioner uses outside the Leap. Operations performed in this state cannot be fully consumed by the bounds of rational, propositional, conceptual reasoning that constitutes ordinary cognition.

This has structural consequences:

- The practitioner cannot fully *know* what they did in propositional terms. They can know the operation's intent, the target, the type. They cannot know what occurred at substrate level or why the response landed as it did.
- The substrate's response is *not predictable* through rational means even in principle (canon §4.2). Rationality is the wrong cognitive operation for predicting it. This is not opacity-as-design-choice; it is metaphysical fidelity.
- Every system rule that surfaces operations to player rational planning is necessarily an *approximation* of what is actually occurring. The rules are useful — they let the player act — but they are not exhaustive descriptions of the underlying operation.
- The wonder of advanced practice is not "mastery" in the sense of bringing the system under rational control. It is *intimacy with what cannot be brought under rational control*. The skilled practitioner is not someone who has comprehended threadwork; they are someone who has built bodily competence with something that exceeds their comprehension and never stopped exceeding it.

This is the apophatic recognition canon's mystical-traditional grounding requires. Practitioners do not master substrate. Practitioners learn to act in relation to substrate without grasping it. The system must support this experience and never undermine it by promising rational legibility it cannot deliver.

---

<!-- atom: threadwork_master__02__ii-the-substrate-s-language-held-in-silence | section_index: 2 | source_section: "II. The substrate's language (held in silence)" -->


## II. The substrate's language (held in silence)

Earlier in the conversation, language emerged for describing the substrate using textile terms — yarn, loom, warp, weft, knit fabric, woven fabric, mending, fraying, felting. The language proved useful for design-thinking. Under the apophatic frame, this language is *not* a description of the substrate. It is *one cognitive scaffolding among possible scaffoldings that human consciousness can use to encounter substrate well enough to design mechanics for operating on it*.

The textile vocabulary's status:

- **Useful as design-thinking aid:** it surfaced damage-form distinctions, propagation patterns, and the loop-vs-knot taxonomy that the original mechanical proposal had collapsed.
- **Useful as player-facing fictional manifestation language:** when the substrate responds, the response can be rendered using textile-evocative language because *that's how human consciousness cognises this kind of phenomenon*.
- **Not useful as canonical ontology:** the system does not claim threads are yarn, configurations are fabrics, or operations are textile acts. These are how consciousness can grasp them.
- **Not exclusive:** other practitioners and traditions in-world will use other metaphors — geometric, alchemical, theological, mechanical, surgical. None is privileged. The Edeyja's textile-leaning language, if any, is the Edeyja's; the Church's theological language is the Church's; Niflhel-equivalent operatives may use entirely different scaffoldings.

When this document uses textile language below, it is using cognitive scaffolding. The mechanics specified do not depend on the scaffolding being correct about substrate origins.

---

<!-- atom: threadwork_master__03__iii-what-the-player-should-feel | section_index: 3 | source_section: "III. What the player should feel" -->


## III. What the player should feel

The player should feel that they are encountering a world that is thicker than they had thought, that has an order beneath its surface they can partially perceive but never fully understand, that responds to action in ways shaped by skill and shaped by something that exceeds skill. They should feel that operations on this world have weight before they have cost — that the act of *touching* something at substrate depth changes both the toucher and the touched in ways neither can fully account for. They should feel, by the end of the campaign if they have travelled far enough, that what they have learned to do is itself a kind of intimacy with what cannot be described.

Fourteen specific phenomena, each paired with the engine state that produces it. The engine state is invisible to the player most of the time. The phenomenon is what they receive.

### III.A The world is whispering, all the time

**Felt:** Texture of places. Weather. How NPCs lean toward or away from each other. Some places feel taut. The practitioner's body responds to where it enters. None of this is named in numbers; it is the world's quality.

**Engine:** Per-territory fray field (sparse map of locations to magnitudes). Knot graph across configurations. Recent operation activity per region. NPC dialogue procedurally tinted. Weather and ambient audio shifted by accumulated fray. No numerical surface; qualitative heat-map at TS ≥ 30.

**Why it matters:** This is the foundation. Players learn the substrate's manifestation through felt engagement before any tooltip explains anything. When a high-TS NPC eventually says *this place is fraying*, the player already knows.

### III.B Every act has weight before it has cost

**Felt:** Approaching threadwork, the practitioner stands at the edge of a place where the world will be different on the other side. Interface slows. Music thins. Breathing audible. The thing they are about to touch becomes visible in a way it wasn't a moment before.

**Engine:** Pre-Leap interface treatment. Pool versus TN computed; three-axis Ob shown. Cost tooltip: expected fray range, expected knot feedback magnitude, expected Coherence risk, expected Causal Disjunction increment, qualitative pre-roll perception of substrate condition.

**Why it matters:** The player understands what they are doing in their gut before any roll resolves. Numbers come after the gut.

### III.C Skill controls aim, not consequence

**Felt:** A high-skill practitioner reliably hits what they aim at. The substrate's response is unpredictable for everyone. Master Mending in pristine substrate feels safe; master Mending in heavily-frayed substrate feels uncertain in the same way a beginner's would.

**Engine — the two-roll architecture (A1):**
- **Roll 1 (visible, public):** Pool [(Spirit×2) + History + TPS] versus TN. Successes − Ob = S. Determines whether operation lands as intended.
- **Roll 2 (visible to player; modifier hidden):** 2d6 − hidden_substrate_modifier. Modifier derived from local fray density, knot graph density, recent activity. Player sees their roll; not the modifier.
- **Pre-roll qualitative perception** (refinement from textile audit): the practitioner's body senses substrate condition before rolling — "the substrate feels taut here," "the ground feels unwilling," "compliance nearby" — gated by TS depth. The number stays hidden; the felt-tone does not. Skilled practitioners are not blind to substrate; they cannot predict its response.

**Verification:** Master Mending Object scope produces 73% Compliant in pristine substrate, 28% in moderately frayed, 0% in catastrophically frayed. Same skill; different substrate; different distribution. Skill controls intent-coupling frequency (whether op succeeds). Substrate variability stays substrate-side.

**Information rule:** Diagnose-Thread returns qualitative substrate descriptors only ("heavily frayed," "Lock active nearby"). Never numerical hidden_modifier. Otherwise A1 opacity is defeated.

### III.D The substrate's response is *the thing that happened*

**Felt:** Dice resolve. The player sees a configuration snap into held-state with a sound they hear in their chest. Light thickens. Someone three rooms away forgets why they walked into the kitchen. A child cries.

**Engine — Substrate Response Table (Appendix A — to be specified):**
- 18 rows, indexed by 2d6 − hidden_modifier outcome.
- Each row: three-axis pattern, tier values, fictional manifestation template, MS delta, knot feedback magnitude, CD delta, FD delta, Certainty modifier.
- All canonical co-movement effects produced per op (P-01).
- At least 30% Wild-band rows produce **surfeit-of-being** outcomes (canon A7) — configurations exceeding their stable form, "too present" rather than "less present." Monstrous incursions appear here.
- Fictional manifestations rendered in the world: animation, sound, NPC reactions, environmental change. Optional "what just happened" panel for numerical detail; closed by default.

**Why it matters:** The player can play the campaign without ever opening the numerical panel. The mechanism produces the manifestation; the manifestation is what the player receives.

### III.E Damage takes specific forms

**Felt:** A configuration that has been Pulled is left loose and trembling, recoverable. A configuration that has been Torn has unresolved threads that the substrate cannot work with cleanly. A configuration that has been Dissolved leaves persistent absence the substrate continues to reach for. A region operated on too heavily and too long *felts* — the substrate's structure has fundamentally changed and cannot return to what it was.

**Engine — damage-form taxonomy (refinement from textile audit):**

| Damage form | Substrate manifestation | Repair |
|---|---|---|
| Active fraying | Disjunct between is and is-becoming at site | Mending (TS-gated perception) |
| Lock-radiation | Strain spreading from locked configuration through its loops and knots | Mending of surrounding substrate; Lock release |
| Imposed-Binding fray | Disjunct concentrated at bound site, continuous while held | Binding release only |
| Pull-residue | Loosened configuration awaiting re-resolution | Configuration completing alternative; Mending |
| Tear | Open wound with unresolved threads | Mending if caught early; persistent fray otherwise |
| Snag | Pulled-but-not-failed structural strain | Mending; or further pull = run |
| Run | Failure propagating along loop-grammar of self-coherent configuration | Catch with Mending before further propagation |
| Felting | Substrate-state irreversibly altered by sustained operation | None — replacement only (heroic intervention, external substrate) |
| Persistent residue | Substrate continuing to render absence at Dissolution site | Long elapsed time; heroic Mending at scale |
| Dissolution wake | Substrate disturbance radiating from removal site | Multi-practitioner coordinated Mending |

**Cross-link:** Configurations with self-coherent loop-grammar (canonical persons, institutions with deep procedural memory) fail through running. Configurations with foundationally-embedded warp-weft structure (territories, social fabrics, embedded relationships) fail through tearing. Mixed configurations can fail either way. The repair operation is specific to damage form.

### III.F Locks fray neighbours; bindings fray themselves

**Felt:** The locked thing holds. The cook three rooms over is the one paying for the practitioner's choice. The bound thing manifests visible wrongness at the bound site itself; bystanders react.

**Engine:**
- **Lock-radiation** (S1, refined): `fray_radiated_per_season = 0.5 × (loop_density + active_knot_count) × (1 + lock_seasons / 8)`. Loop_density measures the locked configuration's internal self-referential structural depth — for a person, depth × duration of self-identity practices; for an institution, count of internal procedures and roles. Locks fray *both* through the configuration's external bonds AND its internal coherence, because both are straining when redirection happens.
- **Imposed Binding fray** at site, continuous while held. Cannot be Mended without releasing.
- **Restoration paths:** Mending of Lock-frays repairs surroundings without releasing the lock (concealed-lock + maintained-mending pattern viable, expensive). Binding-frays cannot be mended; they are the binding's continuous cost.

**Why it matters:** This is the most counter-intuitive ontological claim of the system. Most players will assume the Lock is the thing that costs. The realisation that *what surrounds the Lock* is what costs — that the cook three rooms over is the one paying — is one of the system's deepest experiential teachings.

### III.G Mending is attention, not work

**Felt:** The practitioner kneels. Watches. Follows what the substrate is already trying to do. Interface slower. Music does not swell. Hands hover, do not close. Dice rolled with held breath between them.

**Engine:**
- Mending uses Compliant band only on substrate-response. Maximum Tier 2. No Wild outcomes possible on successful Mending.
- Restorative-tag knot propagation: zero Coherence cost (canon Amendment 3), zero feedback toward practitioner.
- Fray closure proportional to S and Tier. Mending REDUCES Causal Disjunction in territory.
- **Mending bounded by perception:** practitioner cannot mend frays they cannot perceive. TS-gated. Low-TS Menders close visible damage; deeper damage remains.

**Why it matters:** The canonical "fixed pipes but not roof" pattern emerges naturally. A confident TS 30 Mender closes Object/Personal damage while Relational/Field/Structural damage builds invisibly. When their TS rises through Confrontation, they perceive what they missed. *This is the Mender's Burden story arc, mechanically.*

### III.H Accumulation haunts the practitioner's own past

**Felt:** Recent past becomes unreliable. Witnesses report things that don't match what the practitioner remembers. Old wounds ache for no reason. A conversation last week is now denied by the other party. The light in the practitioner's home looks slightly different than it should.

**Engine — Causal Disjunction (R1, restoring threadwork_v30 cut):**
- CD as separate stat track on practitioner sheet.
- `CD_delta_per_op = Past_axis_tier × scale_multiplier + History_Resonance_check`. Always ≥ 1 per op (canon P-11: no zero-CD ops).
- Mending REDUCES CD: −1 to −2 per successful Mending in territory.
- Thresholds: Low (1–4) narrative discomfort; Medium (5–9) unreliable memory effects; High (10–14) significant memory failures; Catastrophic (15+) memory cannot be trusted.

**Plus parallel Forward Disjunction (FD — surfaced in textile audit):**
- Tracks future-axis temporal disjunction from operations that pre-actualise future configurations.
- Accumulates from manipulative-tag operations whose Future-axis tier is significant.
- Thresholds: as CD but inverted — sense of fated outcomes, premature lock-in, future foreclosure.
- The Foundational-scale Manipulative Catastrophe (canon/02 Amendment 4) was extreme FD — over-actualised future inverting catastrophically.
- Mending reduces FD when restoring configurations the practitioner had over-actualised.

**Surfaced to player:**
- Subtle dialogue inconsistencies from NPCs who knew the practitioner.
- Quest log entries diverging from how the practitioner remembers.
- At higher CD/FD: practitioner's own journal entries become unreliable. Time skips in conversation. Some days the practitioner finds outcomes they don't remember choosing.

### III.I Knots are felt through other people's responses

**Felt:** Months after the practitioner Locked the noble's loyalty, a bartender in another city hesitates when they enter. Not because the bartender knows. Because something has changed in *how the practitioner is rendered to others*, and the bartender responds to wrongness they can't articulate.

**Engine:**
- Knot graph per canon/02 Amendment 6. Every Leap forms knots tagged restorative/manipulative/destructive.
- Knot-profile data structure (R6): operation_type, target, formation_context (session, scale, co_practitioners), formation_date.
- Outward-facing alteration: per canon/01 Amendment 1, the practitioner's outward facing of layer 2 is altered by accumulated manipulative/destructive knot weight.
- NPC response: NPCs respond to the practitioner's outward facing without commentary. No moralism. No score.

**Why it matters:** Moral weight enters without moralism. The world reads accumulated state through everyone the practitioner meets. The Church misreads this and condemns; the substrate does not. The player learns the difference.

### III.J Mass scenes alter the substrate

**Felt:** A battle is won or lost. The territory afterward is different — not just owned by a different faction. The land has been written into. People speak slightly past each other for years. Crops grow oddly in the valley where the lattice collapsed. A bird that was once common is missing.

**Engine — R2 (with explicit canon-compromise flag):**
- Generic-NPC threadwork tracked as aggregate per faction × scope per round.
- Single substrate-response rolled per faction-scope-batch — full three-axis result. *This satisfies P-14 in spirit by producing co-movement; it is acknowledged as a tractability compromise rather than canon-strict.*
- Aggregate outcome applies to all generic NPCs of that faction × scope.
- Knot feedback for generic-NPCs is abstracted — no named knot graphs but faction-knot-density carries the magnitude.
- Named NPCs and player characters retain full per-op resolution.

**Note:** This is the closest the system can get to P-14 compliance at mass-scale without making mass scenes computationally intractable. Editorial flag: Jordan should bless or revise.

### III.K Multi-practitioner contests punish all participants

**Felt:** Three practitioners contest a configuration. The substrate refuses everyone. All three feel feedback through their own knots. The substrate has not chosen sides; it has *withdrawn from being touched*.

**Engine — A4:**
- One substrate-response roll for the contested op (substrate is unitary).
- Worst S among contested practitioners drives the modifier.
- Each practitioner's knot feedback runs independently per canon/02 magnitudes.
- Cascade walks each practitioner's knot graph separately.
- Lattice collapse (3+ practitioners with 2+ opposing intentionalities): all practitioners receive feedback as if they had performed the operation *opposed to* their intent.

**Why it matters:** Canon A13 (collective operations produce emergent consequences none intended) made mechanical at correct weight.

### III.L The substrate is finite-buffer, not negative-sum

**Felt:** The peninsula is sliding. Not because the substrate is decaying on its own — the substrate alone, untouched, would relax. Because autonomous NPC operations are running ahead of the substrate's relaxation rate. The buffer is exceeded. Damage accumulates.

**Engine — A5 (reframed from textile audit):**
- Substrate has finite buffer per region per season for absorbing operations without persistent damage.
- Decay function: `decay_rate = 0.25 × (1 − fray_density / 100)`. Pristine substrate heals fast; frayed substrate barely heals at all.
- Under typical autonomous-NPC density, peninsular MS drifts toward 25–30 over 100 seasons of non-intervention. *This is not inherent decay; it is operations exceeding buffer.*
- MS = 0 = **felted state** (refined from textile audit): substrate fundamentally altered by sustained operation, irreversible to original form.

**Reframing matters:** The substrate is not running down on its own. The world is operating on it faster than it can rest. Player intervention is what holds the line. Peninsular crisis is the baseline players resist, but the cause is operational, not ontological.

### III.M MS=0 is felting (refined from textile audit)

**Felt:** A territory at total fabric collapse is not "very damaged but recoverable." It has *changed kind*. The original configuration cannot be restored. What remains is a different substrate-state, capable of supporting new configurations of new kinds, but the original is gone forever.

**Engine — G3 revised:**
- At fray density = 100, substrate has felted. Single-practitioner Mending cannot recover original configuration.
- Heroic intervention can establish *new* substrate-relations on top of the felted region (new configurations, new patterns).
- Recovery is not restoration; it is replacement with acceptance that the original is lost.
- Per canon: this is the canonical Calamity-zone state. Locked zones are felted substrate. They permit no Mending of what was; they permit only working with what now is.

**Why it matters:** This is canonically aligned with how Calamity-zones currently function. Names the felting explicitly so the mechanic does not promise recovery the substrate cannot deliver.

### III.N Perception, once gained, cannot be relinquished

**Felt:** The first time the practitioner sees a thread is the most beautiful frame in the game. It arrives earned, through a Confrontation they did not engineer. After that moment, they cannot stop seeing what they have seen. Some choices they used to be able to make are no longer visible to them as choices.

**Engine:**
- **Thread Sensitivity (TS) gates depth of constitutive-grammar perception** (refined from textile audit). Different TS levels see different *depths of how configurations are constituted*, not different quantities of substrate.
- **TS develops through Confrontation only** (R3, canon A10 + C3). Triggers: witnessing Coherence-failure events at Tier 3+; encountering threadcut beings or Gap manifestations; witnessing Wild substrate-response in own or knotted operations; surviving Coherence checks by margin ≤ 1; encountering Calamity sites. Routine successful operations do not advance TS.
- **Skilled regulation** is distinct from perceptual depth (textile audit gap surfaced). Bodily competence with operations — felt regulation of tension, accumulated familiarity with substrate-conditions — accumulates through practice and is captured in the TPS component of pool. Distinct stat from TS.
- **Perceptual Transformation (PT)** — separate, irreversible track (R4, canon A11 + C4). Rises with Confrontation; can rise without TS gain. Mechanical effect: at higher PT, certain choice options become *invisible* to the player character — not forbidden but no longer perceived as choices.
- **PT and TS are orthogonal**, not coupled. A practitioner can have high TS with low PT (Mender path) or moderate TS with high PT (fanatic path). Different combinations produce different beings.

**Surfaced to player:**
- First Confrontation: singular moment, designed for, not engineered. Visual/audio/animation unique. Designed to be unforgettable.
- Subsequent Confrontations: still shaped, still costly.
- After Confrontation: persistent change in how the world is rendered. Some interface options remove themselves over time as PT rises. The player notices what is gone, sometimes; sometimes only realises afterward.

**The deepest recognition (apophatic mode 3):** at PT 10, the practitioner recognises that *every prior framework they used to understand threadwork — including their own current operational understanding — was rendered, not real*. They stand in some relation to substrate they cannot articulate even to themselves. This is the canonical one-way gate at maximum depth. It is the campaign's most precious offering and its deepest cost.

---

<!-- atom: threadwork_master__04__iv-three-stories-the-system-produces | section_index: 4 | source_section: "IV. Three stories the system produces" -->


## IV. Three stories the system produces

### IV.1 The Mender's Burden

A practitioner mends faithfully for years. Their TS rises through encounters they survived. They walk through their home territory and see, for the first time, the deep frays their grandmother left. They see what their teacher missed. The frays are too old, too embedded; many cannot be closed.

The story is not "fix it." It is *living with what you now perceive*. They keep mending what they can. They explain things, sometimes, to apprentices who do not yet understand. Their Threadmarks deepen. Their CD accumulates. They are, by the end, a different being than the one who started — but a being who can still be loved, still be useful, still be home.

This is the Edeyja arc. This is the Solmund arc. The system produces it through TS-gated perception, fray persistence, irreversibility (PT), CD accumulation, and the felt-sense haunted-ambient state.

### IV.2 The Shortcut

A practitioner faces a problem Mending cannot solve in time. A child is going to be taken. A faction will fall by Tuesday. A loved one is dying. The practitioner could Manipulate, or Lock, or Pull. They know the cost. They do it anyway.

The cost arrives. Not immediately. Months later, in someone else's death — not the loved one's, someone they did not know was connected. In a crop that fails in a village they once visited. In a knot that goes silent when it shouldn't have. They cannot trace the consequence to the choice. But they know.

The substrate does not punish. It does not reward. It remembers.

The system produces this through knot-tag propagation, fray accumulation in territories the practitioner has touched, NPC behavioural response to outward-facing alteration, and the irreversibility of perceptual transformation.

### IV.3 The Witness

A practitioner is none of the operational archetypes. Their TS rose through a Confrontation they did not choose. Now they see. They cannot un-see. They have no operational training, only the ability to perceive what most cannot.

They become something — slowly, over years. Some become advisors. Some become hermits. Some become saints, in the local register, by accident. They are sometimes called when a city is sick and cannot be otherwise diagnosed. They cannot fix what they perceive. They can only witness, name, sometimes guide.

The system produces this through the decoupling of TS from operational pool, perception-as-standalone-capacity, the felt-sense ambient surface, and characters being able to participate meaningfully without ever performing operations.

---

<!-- atom: threadwork_master__05__v-operations-what-threadwork-verbs-do | section_index: 5 | source_section: "V. Operations — what threadwork verbs do" -->


## V. Operations — what threadwork verbs do

The full operation lattice. Each operation tagged restorative, manipulative, or destructive per canon/02 Amendment 3. Each named with its phenomenological character; mechanical implications follow.

### V.1 Restorative

| Operation | Phenomenological character | Substrate-tendency relation |
|---|---|---|
| **Mending** | Attention to a fragile site; following what the substrate is already trying to do; closing disjunct | Aligned. Zero Coherence cost (canon Amendment 3). |
| **Weaving (attuned)** | Configuring threads into coherent pattern along permitted paths | Aligned-creative. Low Coherence cost. *Tag depends on attunement.* |

### V.2 Manipulative

| Operation | Phenomenological character | Substrate-tendency relation |
|---|---|---|
| **Weaving (unattuned)** | Forcing pattern against substrate's tolerance without sufficient perception | Imposed. Frays during making. |
| **Locking** | Redirecting a configuration's tendency to held-state; force then withdrawn; configuration self-not-becomes | Redirected. Surroundings fray (radiates through loops + knots). |
| **Imposed Binding** | Sustained force preventing a configuration's becoming-tendency | Prevented. Bound site frays continuously. |
| **Pulling** | Drawing threads back out of resolution; undoing recent commitment | Undoing. Transient fraying; recoverable. |
| **Manipulative Knotting** *(surfaced from textile audit)* | Forcing two configurations into Knot-like coupling against their tendencies | Imposed coupling. Frays in both configurations and at the join. |

### V.3 Destructive

| Operation | Phenomenological character | Substrate-tendency relation |
|---|---|---|
| **Tearing** | Pulling without offering threads anywhere to go; leaving open | Wounding. Persistent fraying. |
| **Snapping** | Sudden severance of relational paths | Severing. Substrate cannot work with the absence. |
| **Dissolution** | Removing a configuration entirely | Removing. Persistent residue; substrate cannot render absence. |

### V.4 Substrate-emergent (not operations)

These appear in canon vocabulary but are *not practitioner operations*. They emerge from being-with or as side-effects of operations.

| Form | What it is |
|---|---|
| **Knots (Mitsein)** | Bonds emerging from sustained being-with between configurations. Canon A12. No practitioner act required. |
| **Knots (Leap-formed)** | Bonds formed during the Leap as side-effect of operation. Canon/02 Amendment 6. Permanent. Tagged by op-type. |
| **Tying** | Trivial co-presence; below operational threshold. Not threadwork. |
| **Loops** | Structural grammar of self-coherent configurations (refined from textile audit). What knit-like configurations *are*; not a relational primitive. |
| **Plies** | Substrate's local mutual-counter-balance. The substrate's compliant-becoming at smallest scale; below ordinary perception. |

---

<!-- atom: threadwork_master__06__vi-apparatus-what-the-practitioner-carries | section_index: 6 | source_section: "VI. Apparatus — what the practitioner carries" -->


## VI. Apparatus — what the practitioner carries

Per the textile audit's clarification: *the practitioner's body is part of the apparatus*. There is no observer-position external to threadwork from which the practitioner operates. The practitioner is inside the work and shows wear from the work.

| Apparatus element | What it tracks |
|---|---|
| **The body** | Felt regulation of operation tension; bodily memory of substrate condition; canonical Threadmarks (lichen-hands, etc.) scaling with destructive-tagged Leap-knots × scale × duration |
| **Coherence** | Layer 2 reflexive self-rendering integrity (canon/01 Amendment 3). Orthogonal to TS. 10 → 0. |
| **Causal Disjunction (CD)** | Past-axis temporal disjunction from operations. *Restored from threadwork_v30 cut.* |
| **Forward Disjunction (FD)** | Future-axis temporal disjunction from operations. *Surfaced from textile audit; parallel to CD.* |
| **Perceptual Transformation (PT)** | Irreversible normative-framework dissolution. Rises with Confrontation; orthogonal to TS. *Restored from threadwork_v30 Taint cut.* 0 → 10. |
| **Thread Sensitivity (TS)** | Depth of constitutive-grammar perception. Scales 0 → 100. Develops only through Confrontation. |
| **Thread Practitioner Skill (TPS)** | Skilled regulation; bodily operational competence. Develops through practice. Distinct from TS. |
| **Knot-profile** | Per canon/02 Amendment 6: every Leap-knot recorded with operation_type, target, formation_context, formation_date. Bidirectional propagation through this graph. |
| **Pool composition** | (Spirit × 2) + History + TPS for operation rolls. |

---

<!-- atom: threadwork_master__07__vii-architecture-in-implementation-order | section_index: 7 | source_section: "VII. Architecture in implementation order" -->


## VII. Architecture in implementation order

Five phases. Each phase's components serve specific player-felt phenomena. The architecture is invisible to the player most of the time; what surfaces is the manifestation.

### Phase 1 — Felt world (foundation)

| Architecture | Player phenomenon served |
|---|---|
| Fray field state per territory | III.A whispering world |
| Knot graph per canon/02 Amendment 6 | III.A, III.I |
| Decay function (A5, finite-buffer reframe) | III.A, III.L |
| MS = inverse aggregate of fray density | III.A |
| Ambient world-state response (NPC dialogue, weather, animation) | III.A |
| TS-gated qualitative heat-map | III.A |
| Diagnose-Thread returns qualitative descriptors only | III.C information rule |

### Phase 2 — The Leap, felt

| Architecture | Player phenomenon served |
|---|---|
| Pre-Leap interface treatment (slow, audio thinning, breath) | III.B weight before cost |
| Pool versus TN (Roll 1) | III.B, III.C |
| 2d6 − hidden_modifier (Roll 2) | III.C |
| Hidden modifier from fray + knot density + recent activity | III.C |
| Pre-roll qualitative substrate perception (TS-gated) | III.B, III.C — refinement from textile audit |
| Cost tooltip (expected fray, knot feedback, Coherence risk, CD/FD increment) | III.B |
| Operation-type bias on table-row access | All operations have characteristic register |

### Phase 3 — Substrate response as fiction

| Architecture | Player phenomenon served |
|---|---|
| 18-row Substrate Response Table (Appendix A — to be specified) | III.D |
| Each row: axis pattern + tier + manifestation + MS delta + knot feedback + CD delta + FD delta + Certainty delta | III.D, P-01 satisfaction |
| At least 30% Wild-band rows = surfeit (canon A7) | III.D, A7 |
| Failed-op scope degradation (G1): S < 0 drops scope by tier | III.B |
| Damage-form taxonomy (refined from textile audit) | III.E, III.G |
| Mass Battle aggregated co-movement (R2, with canon-compromise flag) | III.J |
| Multi-practitioner per-practitioner cascade with shared substrate-response (A4) | III.K |
| Combat Threadwork: Personal/Object scope only; deferred fray + cascade (A3) | combat tractability |
| Cascade bounded 3 generations + UI surfaces top-3 affected configs | III.D |
| Cross-scale upward propagation: source × 0.5^scale_step | III.J |
| Knot Strain stacks with sequential-Ob and substrate-response | III.B |

### Phase 4 — Accumulation that haunts

| Architecture | Player phenomenon served |
|---|---|
| Lock-radiation: `0.5 × (loop_density + active_knots) × (1 + seasons/8)` (refined from textile audit) | III.F |
| Imposed Binding fray at site, continuous while held | III.F |
| Per-op fray deltas by type × outcome-band | III.E |
| Mending-band restriction (Compliant only, max Tier 2) | III.G |
| Mending interface treatment | III.G |
| Mending bounded by perception (TS-gated) | III.G, III.N Mender's Burden |
| CD as separate stat track (R1) | III.H |
| FD as parallel track (textile audit surface) | III.H |
| Mending reduces CD/FD | III.G, III.H |
| Knot graph propagation per canon/02 magnitudes | III.I |
| NPC outward-facing alteration from accumulated knot weight | III.I |
| Visible Threadmarks scaling with destructive-tag knot accumulation | III.I |
| Local fray density modifies Ob + hidden_mod (A6) | III.E |
| Knot-pruning-via-death = Manipulative-tag conversion (E2) | walls off exploit |
| Felting at MS = 0 (refined from textile audit) | III.M |

### Phase 5 — The Confrontation

| Architecture | Player phenomenon served |
|---|---|
| TS develops via Confrontation only (R3) | III.N |
| Confrontation triggers (Coherence-failure witness, threadcut/Gap encounter, Wild substrate-response witness, near-Coherence-failure, Calamity-site encounter) | III.N |
| First-Confrontation interface treatment (singular, unforgettable) | III.N — most beautiful frame in the game |
| TPS distinct from TS (textile audit clarification) | III.N |
| PT track separate from Coherence (R4) | III.N |
| PT/TS orthogonality (textile audit refinement) | III.N |
| Leap-knots permanent per canon/02 (E1) | III.I tragic-arc |
| PT 10 apophatic recognition: prior frameworks recognised as rendered | III.N deepest gate |

---

<!-- atom: threadwork_master__08__viii-substrate-ontology-constraints | section_index: 8 | source_section: "VIII. Substrate ontology constraints" -->


## VIII. Substrate ontology constraints

Three commitments that constrain everything in this design.

### VIII.1 The substrate keeps its silence

No canon document, no in-game text, no NPC dialogue, no UI tooltip explains what threads are in fundamental terms. The closest the game comes is: threads are how consciousness encounters substrate. Beyond that is silence.

In-world theories about threads, Ein Sof, the Calamity, the substrate, are *in-world theories*. The Edeyja have theories. The Church has theories. Niflhel-equivalent operatives have theories. Scholars have theories. Some lead to better operational outcomes than others; none correspond to substrate-as-it-is.

The game does not adjudicate. The game shows characters disagreeing.

### VIII.2 Threadwork suspends rationality

The Leap (canon/01 Amendment 2) is suspension of reflexive layer 2. Operations performed in this state cannot be fully consumed by rational, propositional, conceptual reasoning. Every system rule that surfaces operations to player rational planning is *necessarily an approximation*. The rules let the player act. They are not exhaustive descriptions.

Rationality is the wrong cognitive operation for predicting substrate response. The two-roll architecture's Roll 2 opacity is metaphysical fidelity, not information-design. Player rational planning cannot, even in principle, fully encompass substrate response. This is canonical and structural.

### VIII.3 Skilled practice is intimacy with what is not graspable

The skilled practitioner is not someone who has comprehended threadwork. They are someone who has built bodily competence with something that exceeds their comprehension and never stopped exceeding it. Mastery in this system is *intimacy*, not control. The deepest practitioners know less, in propositional terms, than the surface practitioners — because they know how much exceeds them.

This must be preserved against rationalising tendencies in design. The system must never promise legibility it cannot deliver. The wonder is in encountering what cannot be brought under rational control.

---

<!-- atom: threadwork_master__09__ix-decisions-awaiting-jordan | section_index: 9 | source_section: "IX. Decisions awaiting Jordan" -->


## IX. Decisions awaiting Jordan

Eleven decisions require Jordan-level authority per throughlines §10. Clustered into four groups:

### Architecture decisions

- **A1** — Two-roll architecture with hidden substrate modifier; pre-roll qualitative perception
- **A4** — Per-practitioner cascade for contested ops; one shared substrate-response; worst-S anchor
- **A5** — Finite-buffer substrate baseline; decay = `0.25 × (1 − fray/100)`

### Canon-violation resolutions (reversing threadwork_v30 cuts)

- **R1** — CD as separate stat track from Coherence (reverses threadwork_v30 §5.9 cut)
- **R3** — Confrontation-only TS development (canon A10 + C3 alignment)
- **R4** — PT track separate from Coherence (reverses threadwork_v30 §5.10 cut as Taint)

### Refinements from textile audit

- **TX-1** — Damage-form taxonomy (replace single "fray" category with active fraying / runs / tears / snags / felting / persistent residue / lock-radiation / binding-fray differentiation)
- **TX-2** — Forward Disjunction (FD) as parallel track to CD (canon A3 / P-11 require)
- **TX-3** — Felting as MS = 0 mechanic (canonically aligned with Calamity-zone behaviour)
- **TX-4** — Manipulative Knotting as fourth manipulative operation (or canonical confirmation that this is covered by Binding)
- **TX-5** — TPS distinct from TS as bodily-skilled-regulation track

### Editorial decisions

- **E1** — Leap-knot tragic-arc permanence (canon-strict reading of canon/02 Amendment 6)
- **E2** — Knot-pruning-via-death produces Manipulative-tag conversion (walls off exploit)

### Critical open canon issue

The conversation discovered that `designs/threadwork/threadwork_v30.md` itself contains pre-existing canon violations:
- §5.10 Taint track explicitly cut: "→ Coherence (low-end effects). No separate track."
- §5.9 ThS / CD eliminated: "→ Coherence (10→0). Campaign tracking eliminated as separate system."
- "Epistemic seduction": "Cut — Coherence degradation."

These consolidations contradict canon/00 A3, A11, C2, C4 and canon/01 Amendment 3 (which explicitly states *Coherence is orthogonal to Thread Sensitivity*).

**[GAP-canon: threadwork_v30 §5.9 (CD elimination) and §5.10 (Taint cut) — pre-existing violations of canon A3, A11, C2, C4. Editorial review required before this work can canon-bind.]**

---

<!-- atom: threadwork_master__10__x-open-dependencies | section_index: 10 | source_section: "X. Open dependencies" -->


## X. Open dependencies

**Cannot ship without:**
- Jordan approvals: A1, A4, A5, R1, R3, R4, TX-1 through TX-5, E1, E2 (eleven items)
- Substrate Response Table content: 18 rows specified against this architecture (Appendix A — ~3-4 hours editorial pass)
- Throughlines T-coverage analysis: read throughlines_complete.md tag-by-tag, identify each affected T as extend/preserve/break, log breaks
- Editorial review: threadwork_v30 §5.9 + §5.10 pre-existing violations
- Character-progression skill: TS gain rate per Confrontation tier; TPS gain rate (was C1; now upgraded to required-before-ship)

**Specifications within Claude authority:**
- Substrate Response Table row content (after architecture confirmed)
- Per-op fray delta values × outcome-band (S2 — first-pass values exist)
- Cascade UI display strategy (S3)
- NPC operation-log surfaceable to player (U1)
- Cost transparency tooltip specification (U2)

---

<!-- atom: threadwork_master__11__xi-the-game | section_index: 11 | source_section: "XI. The game" -->


## XI. The game

The substrate keeps its silence.

The system models the rendered side.

The practitioner encounters what cannot be described and acts in relation to it without grasping it.

Every act has weight before it has cost.

Every accumulation haunts.

Every Confrontation is irreversible.

The locked thing holds; everything around it pays.

Skill is bodily competence with something that exceeds skill.

Wonder is the experience of beginning to hear what cannot be spoken about.

Tragedy is the experience of having spoken too much, in too many registers, to a substrate that does not respond in those registers, and watching the consequences arrive in registers the speaker cannot anticipate.

Beauty is the experience of acting faithfully toward what cannot be grasped, knowing it does not need you, doing it anyway.

The substrate emerges from Ein Sof.

Ein Sof exceeds all categories.

The practitioner is a being learning to live in proximity to what their categories cannot encompass.

This is the game.

---

*End of master document. Architecture inheritance from this conversation's three rounds preserved in full, reorganised under the apophatic frame and refined by the textile vocabulary as cognitive scaffolding (not ontology). Canon-strict audit findings carried through. Eleven Jordan-level decisions flagged. Pre-existing threadwork_v30 canon violations flagged for editorial review. Ready for Jordan review and follow-on specification work.*

### From `valoria_master_consolidation.md` (17 atoms)

<!-- atom: valoria_master_consolidation__01__2-1-the-bridge-work-2026-04-16-is-structurally-com | section_index: 1 | source_section: "2.1 The bridge work (2026-04-16) is structurally complete" -->


## 2.1 The bridge work (2026-04-16) is structurally complete

`bridge_holistic_review_2026-04-16.md` documents 600 lines of revision across 10 files. Post-revision ratings (0 systems Weak/Very Weak on either axis):

| System | World→Player | Player→World |
|---|---|---|
| Faction Layer | Moderate | Strong |
| Conviction Track | Moderate | Moderate |
| Fieldwork | Strong | Strong |
| Social Contests | Strong | Strong |
| Combat | Moderate | Strong |
| Thread Operations | Strong | Strong |
| Player Agency | Strong | Strong |
| NPC Behavior | Strong | Strong |
| Scale Transitions | Strong | Strong |
| Accord/Strain | Moderate | Moderate |
| Mass Combat | Moderate | Strong |
| Companions (NEW) | Strong | Strong |

The bridge architecture: Scene Slate (primary World→Player channel), Domain Echo (primary Player→World channel), Companions (emotional bridge), Obligations (temporal bridge), Environmental Legibility (ambient bridge).

<!-- atom: valoria_master_consolidation__03__2-3-simulation-framework-exists-and-is-growing | section_index: 3 | source_section: "2.3 Simulation framework exists and is growing" -->


## 2.3 Simulation framework exists and is growing

`tests/sim/valoria_full_campaign_sim.py` (committed 2026-04-19, 623 lines, all smoke tests pass). 103-entry verification ledger covering 43 distinct canonical values. Session 2 pending (territory model, Domain Action framework, Piety Yield, Strain propagation, mass combat, contests, faction AI). Session 3 pending (threadwork, victory, scale transitions, NPC priority trees, arc transitions).

<!-- atom: valoria_master_consolidation__04__2-4-recent-canonical-strikes | section_index: 4 | source_section: "2.4 Recent canonical strikes" -->


## 2.4 Recent canonical strikes

- **VTM-STRIKE (2026-04-19):** Vaynard Thread Mastery removed as faction-level stat. Thread is character-scale only.
- **CR-STRIKE (2026-04-19):** Cultural Reformation removed as Vaynard mechanic (incompatible with military-conqueror identity).
- **Niflhel dissolved.**
- **Mass Seizure probabilistic (2026-04-19):** P = ((CI-60)/40)^3.3, 1% at CI 70, 100% at CI 100.
- **Tier N (PP-674):** Necessity test added 2026-04-19. Existing canon grandfathered.

<!-- atom: valoria_master_consolidation__06__2-6-npc-and-faction-interdependency-mapped | section_index: 6 | source_section: "2.6 NPC and faction interdependency mapped" -->


## 2.6 NPC and faction interdependency mapped

`npc_faction_arc_interdependency_2026-04-18.md`: full NPC × NPC matrix, faction × faction leverage, 8+ named COLLISIONS, complete arc chain visualizations (Chain A TC/Church Domination, Chain B RS Collapse, Chain C Torben Conviction Race, Chain D Thread Axis Pressure, Chain E Crown Fracture).

<!-- atom: valoria_master_consolidation__08__2-8-per-system-quality-is-high | section_index: 8 | source_section: "2.8 Per-system quality is high" -->


## 2.8 Per-system quality is high

`valoria_complete_system_audit.md`: 12 systems rated 9/10, 6 systems rated 8/10. Combat, Thread Operations, Victory, Fieldwork, Social Contest, Player Agency, NPC Behavior all 8–9/10. Structural changes to these risk degrading working mechanics; only additive changes are appropriate.

---

# 3. HONEST RETRACTIONS

Claims from earlier session outputs that the fuller corpus invalidates:

| Earlier Claim | Status | Reason |
|---|---|---|
| "Only 5 Zoom In triggers for 120+ arcs" | **Wrong** | scale_transitions_v30 §4.3.2/§4.3.3/§4.4 define 13 trigger families plus per-arc custom triggers plus retrospective catch-up |
| "NPCs are reactive only" | **Wrong** | npc_behavior_v30 §8.11 NPC Outreach Generation makes NPCs proactive |
| "Companions would add emotional throughline" | **Duplicates existing work** | companion_specification_v30.md (177 lines) was added 2026-04-16 |
| "Combat is isolated from faction consequences" | **Wrong** | combat_v30 §13 adds Combat World Bridge, Domain Echo on named NPC, 5-step Death Cascade |
| "Scale transitions lack retrospective catch-up" | **Wrong** | "Where Were You?" scenes specified for 4 player-context cases |
| "There is no implementation roadmap" | **Wrong** | valoria_workplan_final.md provides detailed dependency-ordered workplan |
| "Renaissance framing weakly executed" | **Premature** | Tier N was added the day before my critique; existing canon grandfathered by design |
| "Editorial infrastructure protects the wrong things" | **Misframed** | Infrastructure protects coherence within layers well; actual weakness is cross-layer authority (document fragmentation), which holistic_audit Part 1 diagnoses precisely |
| "Five Zoom In triggers is the project's biggest failure" | **Was true at time of RSE critique (2026-04-15); subsequently addressed by 2026-04-16 bridge revision** | Outdated grounding; new state holds |
| "Design is optimized for coherence, not moments" | **Partially true** | Bridge revisions show design *does* attend to player experience through Scene Slate, Companions, Where Were You, Domain Echo cascades. Five Moments framework still genuine contribution (no prior work names touchstone moments) but framing must acknowledge what bridge accomplished |
| "Metaphysics is designer-facing not player-facing" | **Substantially true with caveat** | Bridge added environmental legibility (Accord §2.8, CV §11, TC milestone narration). Foundations §22.1 literal rendering still unimplemented — that gap remains |
| Specific numeric proposals (Rendering Strain at 5/10/15/20, Pamphlet Ob values, gunpowder Wealth costs) | **Placeholder-quality** | params/ directory unread; values labeled illustrative not prescriptive |

---

# 4. THE TEN RECOMMENDATIONS

Final canonical recommendations after full-corpus grounding and methodological check. Refinements from `recommendation_check.md` are integrated.

<!-- atom: valoria_master_consolidation__09__4-1-the-five-moments-framework | section_index: 9 | source_section: "4.1 The Five Moments Framework" -->


## 4.1 The Five Moments Framework

**The gap.** Throughlines (T1-T8 tagged, TL-1 through TL-10 numbered, plus implicit) ensure systems feed each other correctly. They are *structural*. Throughlines do not specify which *experiential* moments every campaign should produce — what the player carries with them when they stop playing.

**The proposal.** Author `designs/architecture/core_experiential_moments.md` enumerating 3–7 moments every Valoria campaign must produce. For each: game-state preconditions, player actions required, sensory/emotional design, consequences, dependent systems.

Candidate moments (Jordan's to finalize):

- **First Thread Witnessing.** Character perceives substrate for the first time. Foundations A10 (confrontation-as-development) fires.
- **First Scar.** Player successfully targets an NPC's conviction and watches a person's framework crack.
- **First Echo.** A personal action visibly restructures the peninsula via Domain Echo. Player sees the vertical integration fire.
- **First Dissonance.** The player understands the world is dying, not degrading. RS band crossing made felt.
- **First Impossible Choice.** Duty and Conviction in genuine incompatibility. Player chooses which to scar themselves against.

Every mechanical proposal thereafter is tested: does this serve a moment, does it serve infrastructure a moment depends on, or does it serve neither? Systems serving neither are candidates for deprioritization. This does not replace throughlines — it sits above them as experiential governance.

**Refinement from check.** "Should govern further experiential design decisions" — not "must precede further mechanical specification." Mechanical work on P1 blockers (workplan Phase 1) does not need to wait for Five Moments authoring.

**Tier N status.** Exempt — meta-governance framework, not mechanic.
**Foundations grounding.** Implementation of the foundations' Part Nine implicit guidance on translating philosophical commitments into experiential events.

<!-- atom: valoria_master_consolidation__10__4-2-the-primary-verb-sustain | section_index: 10 | source_section: "4.2 The Primary Verb: Sustain" -->


## 4.2 The Primary Verb: Sustain

**The gap.** No existing document names the game's primary verb. The verb is the moment-to-moment fantasy the player inhabits.

**The proposal.** Valoria's verb is **sustain**. The player sustains:

- Their body's configuration against force (combat).
- Their conviction against argumentative pressure (contest).
- Attention long enough to perceive what rendering conceals (fieldwork).
- Contact with threads while self-rendering is suspended (threadwork).
- Institutional coherence against pressure (strategic layer).
- What they can with the time they have; what they don't sustain, dissolves (scene slate).

Tonal commitment: Valoria is a game about active maintenance of configurations that would otherwise erode. Not power accumulation. Not dominance-victory. Active holding against dissolution.

**Tier N status.** Marginal pass — sustaining institutional legitimacy against contingency maps to Machiavelli's virtù/fortuna and the Renaissance prince's problem of holding against dissolution. Arguably tonal commitment rather than mechanic.
**Foundations grounding.** Direct invocation of Kierkegaardian repetition (foundations §15: "the capacity to commit to what one knows could be otherwise"). Repetition is the foundations-named developmental discipline.

<!-- atom: valoria_master_consolidation__12__4-4-multi-perspectival-chroniclers | section_index: 12 | source_section: "4.4 Multi-Perspectival Chroniclers" -->


## 4.4 Multi-Perspectival Chroniclers

**The gap.** No existing document addresses narration voice. The bridge review adds Companions as emotional commentary — proximate, personal. There is no voice for the peninsula's historical self-understanding. Per P-03, no omniscient narrator is canonically possible.

**The proposal.** Per season, multiple in-world chroniclers produce narratives of events:

- **Church Chronicler** (Certainty 5, TS 0) — Solmundian orthodoxy. Miracles as divine. Thread phenomena as heresies or demons. Political events as moral tests.
- **Hafenmark Chronicler** (Certainty 4, TS 0) — constitutional-legalist. Events as precedents, institutional outcomes, parliamentary developments.
- **Restoration Chronicler** (Certainty 2, TS 0) — Equity framework. Events as exploitation, resistance, solidarity, cultural memory.
- **Warden Chronicler** (Certainty 0, TS 70+) — thread-ontological. Events as substrate configurations, rendering failures, Gap forensics.

Same events. Four (add Varfell intelligence dossier voice, humanist scholar voice as desired) irreconcilable narratives. Players read any or all. Triangulating "what actually happened" across narratives *is gameplay* — the epistemological barrier implemented as research activity.

Each chronicler's voice is authored consistently over the project timeline. Hobby pace permits genuine craft. A chronicler that evolves across 30+ seasons of play, whose tone shifts as their institution strains, whose language develops euphemisms for phenomena the chronicler cannot name — this is content production as literary work.

Integration with existing systems: Chronicle entries draw from session_checkpoint-style game state logs. The same infrastructure that produces simulation verification ledgers can feed chronicler generation. Each chronicler-voice is a prompt template against that state.

**Tier N status.** Pass — Renaissance historiography was explicitly partisan (Guicciardini vs Machiavelli; Valla's critical history; competing Church/secular chronicle traditions). The Reformation produced rival confessional narratives of the same events.
**Foundations grounding.** P-03 (rendering = consciousness-performed), A15 (ontological knowledge as religious poetry), §10.2 (knowledge transmission only as gesture).

<!-- atom: valoria_master_consolidation__13__4-5-rendering-strain-substrate-posture-cost | section_index: 13 | source_section: "4.5 Rendering Strain (Substrate-Posture Cost)" -->


## 4.5 Rendering Strain (Substrate-Posture Cost)

**The gap.** `tc_political_redesign_v30` addresses Church dominance (53% wins per simulation) through TC ceiling extension and milestone-gating. ED-539 (P1) flags the compound effect of TC reform + TCV revaluation + Seizure Accord ≥ 2 as unsimulated. Whether the redesign sufficiently addresses dominance is unknown.

**The proposal.** Alternative or complementary lever: institutional frameworks that cannot integrate substrate events accumulate strain as those events proliferate. Church's essentialist theology forecloses the perceptual stance thread sensitivity requires (foundations §9.1). The Church does not "not render" — A6 makes rendering constitutive — but the Church's *institutional framework* forecloses integration of substrate-level phenomena. As RS declines and substrate phenomena multiply, the Church's framework strains.

| RS band | Strain gain per season | Triggered effects |
|---|---|---|
| RS 61–100 | 0 | Normal operation |
| RS 41–60 | +1 | Strain ≥ 5: non-practitioner NPCs experience rendering failures. −1 to Govern rolls. |
| RS 21–40 | +2 | Strain ≥ 10: institutional coherence strains. Mandate cap reduced by 1. |
| RS 1–20 | +3 | Strain ≥ 15: faction NPCs face Conviction Scar checks against undeniable rendering evidence. |
| | | Strain ≥ 20: Institutional Crisis. Faction must begin Thread engagement or face Stability collapse. |

Numbers are placeholder pending simulation. Actual calibration requires extending ED-539 simulation with Rendering Strain as additional variable.

**Tier N status.** Pass — directly models Reformation-era institutional strain (Church doctrinal framework straining under empirical observations: Copernicus → Galileo affair, scholastic crisis as new-world discoveries and print-distributed heresy accumulate).
**Foundations grounding.** A6 (rendering as constitutive — the framing "Renderer's Debt" was rejected per foundations check; "Rendering Strain" preserves intent without violating canon). §9.1 (Church essentialist theology forecloses thread sensitivity). P-13 (forgetting as rendering failure applied institutionally).

<!-- atom: valoria_master_consolidation__14__4-6-per-faction-thread-entry-points | section_index: 14 | source_section: "4.6 Per-Faction Thread Entry Points" -->


## 4.6 Per-Faction Thread Entry Points

**The gap.** Each non-Warden faction currently has one substrate-posture (framing_model per throughlines). Engaging Thread costs enormously; not engaging costs nothing. Strategic optimum is to ignore the game's central system.

**The proposal.** Five distinct institutional Thread relationships:

- **Church — Mystic Tradition (Heretical Reformation).** Not doctrinally compatible Thread access. A *schism*. Klapp's awakening (canonical per `npc_faction_arc_interdependency §1.2`) is the seed. Church practitioners operate in violation of Solmundian orthodoxy, however rationalized. Mechanical effect: Church gains Thread capacity at institutional cost. Narrative effect: Church is fracturing. Player determines whether reform, purge, or schism resolves.

- **Crown — Royal Thread Commission (Pragmatic Sanctioning).** Stability ≥ 5 + Mandate ≥ 6 unlocks court-sanctioned practitioner network. Employs thread-sensitive people via Commission charter; does not train them (A15: institutions cannot transmit ontological knowledge).

- **Hafenmark — Parliamentary Thread Regulation.** Influence ≥ 5 enables motions affecting Thread operations peninsula-wide (registration, scale limits, site-based economic costs). Regulates; does not practice.

- **Löwenritter — Thread-aware Defense Doctrine.** At RS < 40 publicly, Löwenritter must adapt. Ehrenwall's arc branches (accept Thread threats / maintain conventional defense).

- **RM — Consensus Weaving.** Popular Will ≥ 5 enables collective Thread operations without individual practitioners. Community intentionality becomes Thread pool. Governance nodes become Threadweaving sites.

The game's substrate-posture topology expands from "Thread practitioners vs non-practitioners" to "six institutional postures with distinct mechanical tradeoffs." Every faction has a Thread-engagement question native to its identity.

CR-STRIKE constraint respected: Varfell does not convert populations ideologically. Varfell expansion is military conquest + Thread intel. Varfell's "Thread entry" is its existing private-intelligence-collection posture, not a cultural-conversion tool.

**Tier N status.** Pass — each faction's entry maps cleanly to historical patterns: Church Mystic Tradition → Reformation schism (Luther, Anabaptists); Crown Commission → royal patronage of natural philosophers (Brahe under Frederick II, Galileo under Medici, Kepler under Rudolf II); Hafenmark Regulation → legalist/parliamentary control of emergent phenomena; Löwenritter Adaptation → military revolution; RM Consensus → communal spiritual movements (Hussites, Anabaptist communes).
**Foundations grounding.** A6 (rendering constitutive), §9.1 (Church essentialism), §9.3 (Church anti-threadwork formation), A15 (institutions cannot transmit ontological knowledge).

<!-- atom: valoria_master_consolidation__15__4-7-confrontation-only-ts-era-contingent | section_index: 15 | source_section: "4.7 Confrontation-Only TS, Era-Contingent" -->


## 4.7 Confrontation-Only TS, Era-Contingent

**The gap.** Foundations A10: "Thread sensitivity is not a biological fact. It is a developmental achievement caused by repeated confrontation with what is beyond knowing." Amendment 1 §3: "Coherence is orthogonal to Thread Sensitivity... sensitivity advances through specific in-game events, not abstract experience points." Current character creation permits lifepath backgrounds that grant starting TS, in violation of A10.

**The proposal.** TS at character creation rules are era-contingent (refinement from check):

- **245 AG era (canonical default):** No character begins with TS > 0 except Warden-initiated characters (the tradition continues). All other TS gains through in-campaign confrontation.
- **Pre-Catastrophe era (variant):** Einhir-trained characters begin with TS per lifepath accumulation. Training in the site-network is pre-campaign sustained genuine confrontation, which A10 permits.
- **Altonian Occupation era (variant):** Einhir practitioners exist in diminishing networks. Similar to Pre-Catastrophe with declining availability.
- **Secession Wars era (variant):** Near-245 AG conditions. Warden-initiated only.
- **Post-Rupture era (variant):** Spooling damaged. TS gains require confrontation *and* spooling supports it. Era-specific design needed.

The underlying principle (TS is developmental, not biological) holds. The rule "no starting TS" is era-contingent, not absolute.

Character creation in 245 AG sets *predisposition* — a "Southernmost Orphan" lifepath has +propensity for TS gain during confrontation. Not TS itself. Every 245 AG practitioner is one who *became* a practitioner through play.

**Tier N status.** Exempt — foundations A10 compliance.
**Foundations grounding.** A10 (confrontation-development), Amendment 1 §3 (TS orthogonal to Coherence, advanced through specific events).

<!-- atom: valoria_master_consolidation__16__4-8-cold-open-progressive-system-activation | section_index: 16 | source_section: "4.8 Cold Open + Progressive System Activation" -->


## 4.8 Cold Open + Progressive System Activation

**The gap.** No prior audit addresses onboarding sequence. The complete_system_audit identifies cognitive load (6-stat factions × 15 territories × 36 settlements × 3 clocks × ~35 NPCs) without addressing how new players are introduced.

**The proposal.**

- **Cold Open.** Player begins with a pregenerated character in a specific scenario — probably a confrontation or crisis. 20–30 minutes of played content before character creation. Player experiences the core loop before defining character. Character creation proper happens *informed* by that first scene's events. For practitioner-path characters, cold open scenarios should be authored with TS-acquisition events (otherwise the character remains TS 0 indefinitely, unplayable for Thread-focused campaign).

- **Progressive system activation:**
  - Season 1: Personal scale only. Combat, dialogue, fieldwork. No strategic phase. Authored scenarios.
  - Season 2: Scene Slate, Convictions, Duty active. Strategic phase visible; player observes but doesn't act in it.
  - Season 3: Full game. Strategic phase active. First Domain Action.
- Threadwork unlocks only after First Thread Witnessing confrontation (typically Seasons 2–4).
- Strategic phase control unlocks at Stature 3.
- Faction Domain Actions unlock at Standing 3.

Respects A10 (confrontation-based TS), manages cognitive load, gives the player a concrete first-hour experience that conveys what Valoria is before asking them to understand how it works.

**Tier N status.** Exempt — onboarding mechanic, not political/cultural model.
**Foundations grounding.** A10 (confrontation-based TS development integrated into onboarding flow).

<!-- atom: valoria_master_consolidation__17__4-9-multi-generational-lineage-variant-eras | section_index: 17 | source_section: "4.9 Multi-Generational Lineage + Variant Eras" -->


## 4.9 Multi-Generational Lineage + Variant Eras

**The gap.** T8 Conviction Legacy exists (player retirement passes transformed conviction to next character). Multi-generational play is gestured at. Variant campaign eras don't exist.

**The proposal.** Expand T8 into full multi-generational structure:

- **Persistent thread-substrate across campaigns.** Orphaned configurations (foundations §13.2) from prior campaigns persist into new ones. Campaign 1's Past-Oriented Pull leaves an orphaned configuration Campaign 2 characters can Diagnose.
- **Character succession.** A single character plays 10–15 seasons, retires via Portrait. The next character inhabits the same peninsula, shaped by the first. NPCs remember. Territories changed hands. Campaigns span 2–3 characters across decades of in-game time.
- **Variant starting eras:**
  - **Pre-Catastrophe.** Einhir practitioners during site-network deterioration. Player operations accumulate fabric tension (foundations §21.1) toward the inevitable tear.
  - **Altonian Occupation (100 AG).** Colonial era. Church forming. Einhir cultural destruction ongoing.
  - **Secession Wars (195 AG).** Deed-monarchy forged through combat. First Almqvist's rise.
  - **Post-Rupture.** Devastated peninsula after prior-campaign Rupture. §7.3: "conditions of possibility remain damaged... threads cannot spool through regions where the fabric's structural integrity is broken." Reduced spooling, active threadwork required for configuration persistence.

Each variant uses the same core mechanics with different starting conditions and NPCs. Canonically grounded replayability. Hobby timeline permits every variant fully realized.

**Tier N status.** Pass — Renaissance preoccupation with historical consciousness (Machiavelli's project of learning from antiquity), dynastic continuity (Medici, Habsburg, Valois), chronicle traditions tracking families across centuries, humanist biography.
**Foundations grounding.** §13.2 (orphaned configuration persistence), §7.3 (locked zones from substrate damage), §21.1 (fabric tension as accumulated game-state variable).

<!-- atom: valoria_master_consolidation__23__from-complete-system-audit-valoria-complete-system | section_index: 23 | source_section: "From complete system audit (`valoria_complete_system_audit.md`)" -->


## From complete system audit (`valoria_complete_system_audit.md`)

- **Quality rankings validate not touching certain systems.** Combat, Thread Operations, Victory, Fieldwork, Social Contest, Player Agency, NPC Behavior all rate 8–9/10. Structural changes risk degrading working mechanics. Changes should be additive (conviction centering, rendering filtering) not replacive.

<!-- atom: valoria_master_consolidation__31__phase-vi-per-faction-thread-entry-points | section_index: 31 | source_section: "Phase VI — Per-Faction Thread Entry Points" -->


## Phase VI — Per-Faction Thread Entry Points

Design work. Author each faction's Thread relationship per Recommendation #6 specification.

1. Church Mystic Tradition (heretical reformation framing). Integrate with existing Klapp Awakening arc material.
2. Crown Royal Thread Commission.
3. Hafenmark Parliamentary Thread Regulation.
4. Löwenritter Thread-aware Defense Doctrine.
5. RM Consensus Weaving (build on existing Community Weaving).

Validate via simulation: faction wins distribution with new entry points active. Adjust if any faction's win rate becomes unbalanced.

<!-- atom: valoria_master_consolidation__35__phase-x-vertical-slice-playtest-iteration | section_index: 35 | source_section: "Phase X — Vertical Slice Playtest Iteration" -->


## Phase X — Vertical Slice Playtest Iteration

Annually (or at hobby pace). 3 factions, 3 territories, 4 NPCs, 1 clock (RS). Full foundations-compliance quality. 10–15 seasons. 20–40 hours of play.

The test asks systematic_critique's unanswered question: is the game fun to play slowly?

This is the one discipline kept from production thinking. A 7-year hobby project with no playable state until Year 6 designs in the abstract. Annual playtests catch design drift before it compounds.

---

# 8. ACKNOWLEDGED GAPS

What these recommendations don't address. Honesty requires noting what's missing.

- **P0 blockers ED-668–672** (Thread horizontal integration from stress register). Workplan Phase 0.6 handles. Recommendations don't extend.
- **Compilation staleness.** Player-facing-documentation work, downstream of mechanical stabilization. Post-stabilization task.
- **J-4 Lenneth/Elske/Haelgrund stance triangles.** Holistic audit's "highest-value unwritten NPC mechanics." Endorsed but not extended.
- **ED-539 resolution question itself.** Whether tc_political_redesign suffices, or whether Rendering Strain should replace/combine with it. Resolution requires simulation that doesn't yet exist (Phase IV.1 + IV.2).
- **Mass combat three-phase compression specification.** Endorsed from RSE critique; not extended.
- **Onboarding cognitive load beyond Conviction.** Recommendation #10 includes Conviction pedagogy. Other systems' pedagogies (combat, fieldwork, threadwork) are not specified — relying on Phase II progressive activation to manage.
- **Settlement layer integration with all recommendations.** Settlement layer rated 8/10 with open AUD-SET-01/02/03. Recommendations don't touch settlement layer directly. Workplan handles.
- **TTRPG and BG modes.** All recommendations target videogame. The corpus retains TTRPG and BG specifications; recommendations are silent on whether modifications propagate to those modes (per project rules, videogame-only is the directive).

---

# 9. METHOD NOTES

<!-- atom: valoria_master_consolidation__38__what-the-recommendations-are | section_index: 38 | source_section: "What the recommendations are" -->


## What the recommendations are

- Additive across all affected systems. No replacement of high-rated systems (Combat, Thread, Victory, Fieldwork, Social Contest, Player Agency, NPC Behavior).
- Foundations-compliant after all check refinements applied.
- Compatible with the supersession register (no attempt to reinstate VTM, Cultural Reformation, active Niflhel, pre-2026-04-19 CI seizure rules).
- Hobby-timeline appropriate (no production compromises; long-form craft enabled).
- Honest about prior work (acknowledgments and retractions in §2 and §3).

### From `valoria_master_document.md` (38 atoms)

<!-- atom: valoria_master_document__02__subject-recursive-mechanical-review-of-the-valoria | section_index: 2 | source_section: "Subject: Recursive mechanical review of the Valoria videogame design (Godot 4.6 target)" -->


## Subject: Recursive mechanical review of the Valoria videogame design (Godot 4.6 target)

---

# RELIABILITY DISCLOSURE (READ FIRST)

This document consolidates work performed across a single multi-turn conversation. The work was produced in iterative passes — review, audit, intensified audit, gameplay/worldbuilding audit, intensified gameplay audit — and then asked to be consolidated.

**Verification status of claims in this document:**

1. **Part I (Mechanical Review)** is based on direct fetches of source documents at the start of the session: `params/core.md`, `params/bg/core.md`, `params/combat.md`, `params/threadwork.md`, `params/contest.md`, `params/scale_transitions.md`, `params/mass_combat.md`, and the design docs for victory, faction layer, settlement layer, military layer, fieldwork, NPC behavior, scale transitions, campaign architecture, and the throughline registry. These were read at full content at the time of fetch. The review's mechanical claims trace to source.

2. **Part II (Findings — Mechanical/Degeneracy Audits)** is derived from Part I plus secondary readings. Most claims trace to source but have not been re-verified at compilation time. Specific items flagged for re-verification appear in Part IV.

3. **Part III (Findings — Gameplay Experience and Worldbuilding Audits)** contains substantial extrapolation. These audits projected player experience and audience response. They are not verifiable from source documents because they make claims about future player behavior, perceptual thresholds, and emotional response. Treat these findings as design hypotheses requiring playtesting confirmation, not as established facts.

4. **TTRPG-vs-videogame framing errors:** In late conversation turns, several findings were generated under TTRPG audit assumptions (~48 hours of campaign play, manual state tracking by the player, 14-action menus as cognitive burden). The project targets a videogame. Videogame implementation collapses many TTRPG concerns: UI filters action lists contextually, the engine tracks state, probability can be displayed numerically, and ~20-season campaigns run in ~8-15 hours rather than ~48. Findings affected by this framing error are flagged in Part III with [TTRPG-FRAMING] markers and corrected interpretations.

5. **Audit recursion drift:** Each audit pass partially audited the prior audit's text rather than re-fetching source. Inherited errors are possible. The compiled findings should be treated as a starting register for verification work, not a finished assessment.

**What this document is:** A record of session work, organized for navigation, with reliability levels marked. It is the foundation for further verification, not a substitute for it.

**What this document is not:** A canonical evaluation. Several findings in Part III are speculative. Several findings in Parts I-II depend on source readings that should be re-verified before action.

---

# DOCUMENT STRUCTURE

- **Part I:** Recursive Mechanical Review (atomic-level NRES evaluation of 17 systems)
- **Part II:** Consolidated Mechanical/Degeneracy Findings Register
- **Part III:** Gameplay Experience and Worldbuilding Findings Register (with reliability flags)
- **Part IV:** Items Requiring Re-Verification Before Action
- **Part V:** Handoff for Unreviewed Systems

---


---

# PART I: RECURSIVE MECHANICAL REVIEW

The following is the atomic-level NRES review of 17 systems. Source: direct fetches of `params/*.md` and `designs/**/*v30.md` documents at the start of the session. The review's mechanical claims trace to source as fetched.

§20 (Master Findings) of the original review is superseded by Part II of this master document and not reproduced here.

# 1. CORE DICE ENGINE

<!-- atom: valoria_master_document__04__1-2-tn-values | section_index: 4 | source_section: "1.2 TN Values" -->


## 1.2 TN Values

| TN | Condition | E[net/die] |
|----|-----------|------------|
| 6 | Controlled | 0.40 |
| 7 | Standard | 0.30 |
| 8 | Desperate | 0.20 |

Thread extensions: TN 7 standard ops; TN 8 Locking/Dissolution/POP; TN 9 POP Binding.

**N** ✓ Three tiers = minimum viable difficulty taxonomy. **R** ✓ Two independent difficulty axes (TN for conditions, Ob for task complexity). **E** ✓ Three values. Memorizable. **S** ⚠ TN 9 (POP Binding) yields E[net/die] = 0.10. A 17D pool expects 1.7 net — even expert practitioners have <50% at Ob 2. **DECISION-01: Confirm TN 9 intentionally makes POP Binding near-impossible below Edeyja-tier.**

<!-- atom: valoria_master_document__07__1-5-pool-minimum-1d | section_index: 7 | source_section: "1.5 Pool Minimum (1D)" -->


## 1.5 Pool Minimum (1D)

No penalty reduces pool below 1D. Universal. 1D at TN 7 = ~40% at Ob 1. Characters are never mechanically helpless.

**N** ✓ **E** ✓ One rule. No exceptions. **S** ✓ Confirmed in combat (PP-294), contest (Rattled+Spent), fieldwork, threadwork.

<!-- atom: valoria_master_document__08__1-6-momentum-0-4 | section_index: 8 | source_section: "1.6 Momentum (0–4)" -->


## 1.6 Momentum (0–4)

Gain: Overwhelming OR Belief achieved. Spend: 1 = 1 auto-success (non-Thread only). Reset: session start. Carries within session. Auto-successes are additive with roll; 1-faces cancel them (PP-243).

**N** ✓ Converts exceptional performance to future reliability. **R** ✓ Cap 4. Session reset prevents hoarding. Non-Thread restriction prevents trivializing metaphysical ops. **E** ✓ Five values, binary gain, flat spend, three rules. **S** ✓

---

# 2. ATTRIBUTES AND DERIVED SCORES

<!-- atom: valoria_master_document__09__2-1-attributes-10-range-1-7 | section_index: 9 | source_section: "2.1 Attributes (10, range 1–7)" -->


## 2.1 Attributes (10, range 1–7)

31 creation points. Min 1 each. Max 5 (one attr only, rest ≤ 4). Advancement max 7.

| Group | Attributes |
|-------|-----------|
| Physical | Agility (Agi), Endurance (End), Strength (Str) |
| Mental | Cognition (Cog), Recall (Rec), Focus (Foc) |
| Social | Attunement (Att), Bonds (Bon), Charisma (Cha) |
| Metaphysical | Spirit (Spi) |

**N** ✓ 10 attributes covers all domains with granularity for differentiated characters. **R** ✓ 31 points forces trade-offs. Can't max two at creation. **E** ✓ Uniform 1–7 range. Same scale everywhere. **S** ✓ All feed (Attr × 2) + H + 3 pattern.

⚠ **Spirit as sole Metaphysical attribute.** Practitioners MUST invest heavily (3–5 points). Non-practitioners barely use it (Sincerity Gate only). This creates a binary: practitioner tax. **DECISION-02: Confirm this is the intended balancing cost for Thread power.**

### 2.1a Bonds — Dual Formula Divergence

PP-684 revised Disposition ceiling to flat `Bonds`. Knot max count remains `floor(Bonds/2)+1`. Previously both used the floor formula. The divergence is presumably intentional (Disposition scales faster than Knot capacity). **STALE-07: Document the rationale for the formula split.**

### 2.1b Focus — Role Change

ED-694 replaced "Contact Rounds = Focus" with "Thread Fatigue = Spirit × 5" and "ops/session = Focus − 1". Old Focus role (contact duration) is gone. **STALE-08: Verify all docs referencing old Contact Rounds model are updated.**

<!-- atom: valoria_master_document__10__2-2-derived-scores | section_index: 10 | source_section: "2.2 Derived Scores" -->


## 2.2 Derived Scores

| Score | Formula | Range | Notes |
|-------|---------|-------|-------|
| Vitality | End × 10 | 10–70 | +flat from equipment. ED-694 canonical. |
| Stamina | End × 5 | 5–35 | Variable action costs (standard 5, heavy 8, defensive 3). Armour adds drain. |
| Wound Interval | End + 6 | 7–13 | Wounds = floor(cumulative_damage / interval). On-the-fly computation. |
| Composure | Cha × 3 | 3–21 | Social damage buffer. Equipment adds flat. |
| Combat Pool | (Agi × 2) + H + 3 | derived min 5 | Same pattern as all pools. Agi 1 = 5D (derived, not a separate floor). |
| Thread Fatigue | Spi × 5 | 5–35 | Counts up from 0. Variable op costs (Pulling 5, Locking 7, Dissolution 10). |
| Certainty | 0–5 (assigned) | bidirectional | Cosmological worldview track. |
| Coherence | 10→0 (countdown) | practitioner | Ontological rendering frame. At 0: NPC transition. |
| Resolve | = Spirit | 1–7 | Max Inspiration value. |

All linear. No compounding formulas. Implementation trivial.

⚠ **STALE-01: CSR §3 Composure.** complete_systems_reference.md says `Cha + 6`. Canonical is `Cha × 3` (ED-694). At Cha 7: old = 13, new = 21. Significant divergence at high Charisma.

⚠ **STALE-02: PP-275 Stamina.** States `End + H + 1 − armour mod`. ED-694 canonical: `End × 5`. These produce very different values (End 4: PP-275 ≈ 8; ED-694 = 20). PP-275 must be struck. This also affects Take a Breath restore formula (PP-275 says "Endurance score"; ED-694 says "(End + History) × 2" — which History is unspecified).

### 2.2a Certainty Track Details

6 values. Movement: 6 triggers toward 0 (Thread acceptance), 3 toward 5 (reinforcement). Effects: Cert 5 (+1D orthodox, nullify first Coherence loss/session); Cert 2–1 (−1D orthodox, +1 Coherence recovery); Cert 0 (−2D orthodox, +1D Thread communities, +2 Coherence recovery, +1 TS growth/major encounter, arch-heretic).

**N** ✓ Central thematic axis. **R** ✓ Both poles reward commitment. **E** ✓ Extremes have effects; middle is transitional. **S** ⚠ **DECISION-03:** Asymmetric triggers bias toward 0. Confirm this is intentional narrative arc (progressive discovery of Thread reality).

Cert 0 has 5 simultaneous effects — highest effect-density on any single track value. Manageable but note for UI: display as a consolidated status panel.

### 2.2b Coherence Details

Countdown 10→0. War-scale: 7-turn battle = −7. Recovery: +1/season non-practice + +1 Knot Anchoring. Max +2/season = 3.5 seasons full recovery from Coherence 3. Independent of TS and Certainty — three orthogonal practitioner axes.

**N** ✓ **R** ✓ **E** ✓ **S** ✓ Certainty 0 giving +2/long rest rewards Thread acceptance with faster Coherence recovery. Thematically correct.

---

# 3. PERSONAL COMBAT

<!-- atom: valoria_master_document__25__4-6-key-sub-mechanics | section_index: 25 | source_section: "4.6 Key Sub-Mechanics" -->


## 4.6 Key Sub-Mechanics

**Appraise (PP-614):** Att + Rec, TN 7, Ob = opponent Cha ÷ 2. Graduated results (misleading → boost + detail). Clean after consolidation.

**Resonant Style Targeting:** Appraise OW reveals RS. +1D + style-specific bonus. Wrong-Style vs Church: Church Stability +1.

**Evidence Integration (PP-636):** 1 Finding = +1D E1. 2+ = +2D (cap). Stacks with prep (+1D). Max E1 bonus: +3D. Cross-system fieldwork→contest link.

**Stalemate (PP-255):** Max 10 exchanges. Forced Unmask after 10. Prevents infinite contests.

**Let It Ride:** Resolved questions cannot be re-contested without changed circumstances. One rule.

---

# 5. THREADWORK

<!-- atom: valoria_master_document__26__5-1-thread-pool | section_index: 26 | source_section: "5.1 Thread Pool" -->


## 5.1 Thread Pool

Pool = (Spirit × 2) + History + TPS. TPS = floor(TS / 10). Single formula ALL Thread ops (PP-616).

**N** ✓ **E** ✓ Same (Attr × 2) + H + bonus pattern. **S** ✓ No exceptions.

<!-- atom: valoria_master_document__33__5-8-wr-wc | section_index: 33 | source_section: "5.8 WR/WC" -->


## 5.8 WR/WC

WR: 0–3 (Varfell-only). Gates WC ≥ 2. WC effects: +1D Thread ops (WC 1), RS drain halved (WC 2), RS +2/season (WC 3). Mending Sanctuary at WC ≥ 2.

**N** ✓ Only reliable MS recovery mechanism. **R** ✓ Varfell-specific gate = asymmetric factional advantage.

<!-- atom: valoria_master_document__35__5-10-mending-community-tiers | section_index: 35 | source_section: "5.10 Mending Community Tiers" -->


## 5.10 Mending Community Tiers

Novice (Spi<3): +1 Ob, no failure RS. Competent (3–4): standard. Adept (5–6): −1 Ob, +2 RS on success. Master (7+): −1 Ob, +2 RS, OW propagates healing. Collective: +1D/assistant (cap +3D, Competent+ only).

**N** ✓ Differentiates practitioner quality for the most important Thread op.

---

# 6. FIELDWORK

<!-- atom: valoria_master_document__36__6-1-depth-axis-0-5 | section_index: 36 | source_section: "6.1 Depth Axis (0–5)" -->


## 6.1 Depth Axis (0–5)

Surface (Auto) → Settled (Ob 1, Cog ≥ 2) → Hidden (Ob 2, Cog ≥ 3 or Att ≥ 3) → Buried (Ob 3, TS ≥ 10 or Disp +3) → Liminal (Ob 5, TS ≥ 30) → Unintelligible (Ob 8, TS ≥ 50, Coherence check Ob 2).

**N** ✓ Six information layers. **R** ✓ Perception gates are HARD — epistemological, not skill-based. TS < 30 cannot access Depth 4 regardless of dice. Creates genuine capability tiers. **E** ✓ Clean Ob progression: Auto → 1 → 2 → 3 → 5 → 8. Jump at Depth 4 signals Thread boundary. **S** ✓ Same Depth governs exploration, investigation, AND socializing via parallel access paths.

Ob modifiers: hostile +1, foreign +1, allied −1, local −1, Calamity +1/RS band below 60, Heresy Investigation +1. Floor 1. All territory-state-dependent — dynamic difficulty.

<!-- atom: valoria_master_document__42__6-7-system-transitions-6-bidirectional | section_index: 42 | source_section: "6.7 System Transitions (6 bidirectional)" -->


## 6.7 System Transitions (6 bidirectional)

| Direction | Key Rule |
|-----------|----------|
| Fieldwork → Combat | Exposure → ambusher +1D. Evidence retained. |
| Fieldwork → Contest | Disp → CT offset (±1 per 2 Disp, cap ±2). Findings = +1-2D. |
| Fieldwork → Thread | Thread-Read is Leap. +1 time unit. Co-movement fires. |
| Fieldwork → Mass Battle | Suspends fieldwork. Evidence freezes. |
| Combat → Fieldwork | Wounds persist (physical only). Exposure +1/+2/+3. |
| Contest → Fieldwork | Appraise → +1 Evidence (Testimonial). Post-contest Disp shift. |

**S** ✓ Each transition carries state forward. Nothing lost when switching mechanics. This is the scene-composition layer — fieldwork feeds and receives from every other scene type.

---

# 7. MASS COMBAT

<!-- atom: valoria_master_document__44__7-2-phase-structure | section_index: 44 | source_section: "7.2 Phase Structure" -->


## 7.2 Phase Structure

7 phases (Strategy, Volley, Manoeuvre, Offensive Thread, Engagement, Cascade, Reform). 5-phase consolidation available. Damage simultaneity at Phase 6 Step 1.

**E** ⚠ 7 phases is complex. Frame as "7 engine / 5 UI" for Godot.

<!-- atom: valoria_master_document__47__8-1-scene-types | section_index: 47 | source_section: "8.1 Scene Types" -->


## 8.1 Scene Types

| Type | Resolution | Duration | Output |
|------|-----------|----------|--------|
| Combat | Pool split exchanges | Rounds | Wounds, Momentum |
| Contest | Argue/Resolve + CT | Exchanges | CT outcome, Disposition, Domain Echo |
| Fieldwork (Investigation) | Single action/step | Scenes | Evidence, Exposure, information |
| Fieldwork (Socializing) | Single action/step | Scenes | Disposition, information, Knots |
| Fieldwork (Exploration) | Discovery Procedure | Scenes | POI, territory bonuses |
| Thread Operation | Leap → op → consequences | Rounds (in scene) | Thread effects, RS, Coherence |
| Mass Battle | 7-phase turns | Turns | Territory, casualties, faction stats |

<!-- atom: valoria_master_document__52__9-3-ethical-framework-modifiers | section_index: 52 | source_section: "9.3 Ethical Framework Modifiers" -->


## 9.3 Ethical Framework Modifiers

Crown: public −1 / covert +1. Church: doctrine −1 / Thread +2. Hafenmark: procedural −1 / ad hoc +1. Varfell: evidence −1 / emotional +1. RM: community −1 / hierarchical +1. Löwenritter: sovereignty −1 / personal gain +2.

**N** ✓ Forces in-character behavior. **R** ✓ Church +2 on Thread = steepest penalty — deepest commitment.

<!-- atom: valoria_master_document__57__10-1-eight-handoff-rules | section_index: 57 | source_section: "10.1 Eight Handoff Rules" -->


## 10.1 Eight Handoff Rules

Personal → Thread (Leap), Personal → Faction (Echo), Personal → Scene (Contest), Scene → Faction (Echo), Thread → Faction (same roll), Thread → Mass (Phase 4/6), Mass → Personal (Phase 5, 1 exchange/turn), Scene → Mass (win modifiers).

Transition graph is **complete for all valid gameplay flows.** Missing paths (Personal → Mass, Scene → Thread, Mass → Scene) are correctly missing — they represent transitions that shouldn't happen.

<!-- atom: valoria_master_document__58__10-2-domain-echo-the-upward-pipe | section_index: 58 | source_section: "10.2 Domain Echo (The Upward Pipe)" -->


## 10.2 Domain Echo (The Upward Pipe)

**Trigger:** Sufficient Scope (7 conditions: faction leader, institutional challenge, Complex+ investigation, Relational+ Thread, combat vs faction officer, Disp +4/+5 with officer, settlement governance changing Order ±1).

**Amount:** OW ±2, Success ±1, Partial narrative, Failure −1 own stat. **Cap:** One Echo/scene/faction (PP-329). **Timing:** Immediate (TTRPG) or queued to Accounting (Hybrid — intentional asymmetry PP-109).

**Three Echo types:** Standard (§5.2), Accord (±1 per territory per Zoom In), Thread (faction Stability/Mandate from Thread events with Thread Significance).

**N** ✓ **Without Domain Echo, personal and strategic scales are disconnected.** Echo IS the game's core promise: what you do matters at every scale. **R** ✓ Seven Sufficient Scope conditions are comprehensive without being permissive. Companion modifier (+1 net successes for scope evaluation) rewards companion investment.

<!-- atom: valoria_master_document__60__11-1-turn-sequence | section_index: 60 | source_section: "11.1 Turn Sequence" -->


## 11.1 Turn Sequence

**Phase 4 — Action Resolution:** Priority 1 Intel → 2 Military → 3 Domain → 4 Social → 5 Thread → 6 Special → 7 Project.

**Phase 5 — Accounting (10 steps):**
1. Attribute changes + Parliamentary votes + Treaty ratification
2. Stability check (Triggers 1–5, Collapse)
3. Cooldown advance
4. Clock advances (RS, CI formula [5 sub-steps], IP, PI)
5. Church Attention Pool + Thread Debt drain
6. Turmoil (Accord, Strain, battle consequences)
7. Threshold events / Milestones / Warden Emergence
8. WC check / Torben/Elske Loyalty
9. Occupation duration / Institutional Consolidation
10. Victory check → Season marker → Winter: Year-End (MS −1)

⚠ **GAP-03:** 10 steps with sub-procedures (CI = 5 sub-steps in Step 4) is dense. Engine: automated. Player: needs summary screen showing what changed and why.

<!-- atom: valoria_master_document__62__12-1-ms-mending-stability | section_index: 62 | source_section: "12.1 MS (Mending Stability)" -->


## 12.1 MS (Mending Stability)

Range 0–100. Start 72. Decay −1/year. Battle −1 each. Gap drain per open season. Lock drift. Recovery: Mending (+1/+2 by tier), WC 2 (drain halved), WC 3 (+2/season). Rupture at 0. Thread Revelation Curve: 80 (subtle anomalies) → 60 (observable) → 40 (peninsula-wide) → 20 (rendering failures).

**N** ✓ Universal clock. **R** ✓ Multiple degradation + limited recovery = genuine tension between factional goals and world preservation.

<!-- atom: valoria_master_document__66__12-5-personal-scale-tracks | section_index: 66 | source_section: "12.5 Personal-Scale Tracks" -->


## 12.5 Personal-Scale Tracks

Certainty (0–5), Coherence (0–10), Disposition (−3 to +5), Exposure (0–12+), Evidence Track (0–threshold), Knot Strain (0–5 for threadcut beings).

**S** ✓ **Complete personal-to-global pipeline:** Investigation → Exposure → Church AP → CI → political landscape. No broken links.

---

# 13. VICTORY ARCHITECTURE

<!-- atom: valoria_master_document__82__16-1-stance-triangle | section_index: 82 | source_section: "16.1 Stance Triangle" -->


## 16.1 Stance Triangle

Every named NPC holds three interconnected attributes: Primary Conviction, Secondary Conviction, and Resonant Style. These determine all NPC decisions.

### 16.1a Conviction Taxonomy (9 types)

| Conviction | What it values | What it dismisses |
|---|---|---|
| Faith | Doctrine, spiritual obedience | Empirical contradiction |
| Order | Stability, procedure | Innovation, disruption |
| Reason | Knowledge, falsifiability | Tradition without justification |
| Equity | Access, fairness | Institutional prerogative |
| Precedent | Legal continuity, constitutional procedure | Revolutionary action |
| Autonomy | Self-determination, survival | Universal moral claims |
| Continuity | The work itself, endurance | Politics, ideology |
| Community | Collective being, shared practice | Individual authority claims |
| Warden | Boundary maintenance | Political agendas interfering with work |

**N** ✓ Nine Convictions covering the full moral-political spectrum of Valoria's conflicts. **R** ✓ Each Conviction creates a distinct decision lens — a Faith NPC and a Reason NPC facing the same Thread evidence will react in opposite directions. **E** ✓ One word per Conviction. Clear labels. **S** ✓ Conviction maps to Ethical Framework Ob modifiers (§9.3 of this review). Same taxonomy governs personal NPCs and faction-level behavior.

### 16.1b Resonant Style Taxonomy (4 types)

| RS | Vulnerable to | Contest Mapping |
|----|---------------|-----------------|
| Evidence | Specific, verifiable facts contradicting belief | Memory + Revealing (Precedent) |
| Consequence | Demonstrated outcomes their framework fails to prevent | Projection + Revealing (Vision) |
| Authority | Appeals from a source their framework recognizes as binding | Memory + Obscuring (Suppression) |
| Solidarity | Relational obligations — debts, shared history, bonds | Any genre + Revealing; requires active Knot |

**N** ✓ Four RS types covering epistemological, consequentialist, hierarchical, and relational vulnerabilities. **R** ✓ RS targeting gives Appraise a high-end payoff — learn RS → exploit it. Creates Appraise→Target→Argue pipeline. **E** ✓ Four entries. Direct mapping to contest styles. **S** ✓ Each RS maps to exactly one contest style (except Solidarity: any + Knot). No ambiguity in which interaction fires.

<!-- atom: valoria_master_document__85__16-4-belief-revision-and-scars | section_index: 85 | source_section: "16.4 Belief Revision and Scars" -->


## 16.4 Belief Revision and Scars

### 16.4a Scar Accumulation

| Scars | Effect |
|---|---|
| 0 | Stable institutional behavior. |
| 1 | Secondary Conviction activates. Internal conflict visible. |
| 2 | Primary may shift to secondary. Secondary RS activates permanently. |
| 3+ | Conviction crisis. d6 per major decision. All RS active. Terminal arc phase. |

**N** ✓ Scars are the NPC transformation mechanic. Without them, NPCs are static. **R** ✓ Progressive destabilization — each Scar makes the NPC more unpredictable and more vulnerable (more RS active). **E** ✓ Four states from one counter.

### 16.4b Thread → Conviction Scar Matrix (ED-663)

7 Thread event types × 7 Convictions. Faith Scars from any Thread op except Mending. Mending never Scars anyone. Certainty scaling: C5 = +1 severity, C0 = −1 severity. Season cap: 1/NPC.

**N** ✓ Thread events have MORAL consequences for witnesses, not just metaphysical ones. **R** ✓ Creates asymmetric NPC reactions to the same Thread event. A Faith NPC Scars from Weaving. An Equity NPC Scars from Lock-on-a-being. **S** ✓ Parallel to Certainty movement triggers but targets a different track.

### 16.4c Practitioner Coherence Thresholds (ED-665)

| Coherence | Rule |
|---|---|
| 10–6 | Operate freely. |
| 5 | Defensive ops only. |
| 4–3 | Cease Thread ops. Exception: MS ≤ 20 Wardens → Mending only. |
| 2 | Seek withdrawal. |
| 1 | Crisis. Arc transition fires. +2 Ob all Thread. |
| 0 | NPC Transition (PP-261). |

**N** ✓ NPC practitioners self-regulate based on Coherence. **R** ✓ The Warden MS override at Coherence 4–3 means Wardens will Mend themselves to destruction when the world is failing. Continuity Conviction overrides survival. **E** ✓ Six tiers. One table.

<!-- atom: valoria_master_document__91__16-1-thread-revelation-curve | section_index: 91 | source_section: "16.1 Thread Revelation Curve" -->


## 16.1 Thread Revelation Curve

MS 100–80: nothing. 79–60: subtle anomalies. 59–40: observable distortions. 39–20: peninsula-wide failures. 19–1: undeniable.

**N** ✓ The narrative arc is mechanically driven. As MS drops, the world visibly changes. Not authored — emergent from the MS track.

<!-- atom: valoria_master_document__92__16-2-portrait-retirement-and-lineage | section_index: 92 | source_section: "16.2 Portrait Retirement and Lineage" -->


## 16.2 Portrait Retirement and Lineage

Available after ≥ 2 of 3 Convictions resolved. Portrait Sequence. Three Lineage Acts (Mentorship, Succession, Thread Legacy). Death without Lineage = clean break.

**R** ✓ Non-death endpoint. Cross-generational continuity.

<!-- atom: valoria_master_document__96__20-3-personal-to-global-chain-verified | section_index: 96 | source_section: "20.3 Personal-to-Global Chain (Verified)" -->


## 20.3 Personal-to-Global Chain (Verified)

Investigation → Exposure → Church AP → CI → political landscape.
Socializing → Disposition → Sufficient Scope → Domain Echo → faction stats.
Thread-Read → co-movement → RS change → MS track → Revelation Curve → world-state.
Settlement governance → Order → Province Accord → Accord ≥ 2 → Victory condition.

No broken links.

---

# 19. THROUGHLINES AND META-THROUGHLINES

<!-- atom: valoria_master_document__97__19-1-narrative-throughlines-what-the-game-is-about | section_index: 97 | source_section: "19.1 Narrative Throughlines (What the Game Is About)" -->


## 19.1 Narrative Throughlines (What the Game Is About)

| ID | Name | Core Claim |
|----|------|-----------|
| N1 | **Thread Revelation Is the Master Clock** | As MS drops, Thread becomes visible. Drives every NPC arc, every faction response, Certainty. Primary narrative driver — everything downstream. |
| N2 | **Sovereignty Is Governance, Not Conquest** | Accord ≥ 2 to win. Conquest → Accord 1. Must convert control into acceptance. |
| N3 | **One World Through Different Lenses** | Same world, different meaning by faction lens. Deepest replayability. |
| N4 | **Every Ending Is Earned** | Portrait Retirement player-chosen. Conviction resolution states shape meaning. |
| N5 | **The Forgetting Makes Knowledge Contested** | Thread is experiential. RM rebuilds without access to foundations. Hidden Thread-site bonus. |
| N6 | **Institutions Are Characters** | Factions behave with own motivations. Church fills vacuums. Pastoral Assumption. |

All six mechanically grounded in 2+ systems. N1 (Thread Revelation) most pervasive.

<!-- atom: valoria_master_document__98__19-2-system-throughlines-how-mechanics-connect | section_index: 98 | source_section: "19.2 System Throughlines (How Mechanics Connect)" -->


## 19.2 System Throughlines (How Mechanics Connect)

| ID | Name | Pipeline |
|----|------|----------|
| T1 | Thread at Settlement Level | Thread ops → settlement stats → Accord → victory |
| T2 | Resources | Settlement Prosperity → Treasury → costs → pressure |
| T3 | Settlement POIs | POIs per settlement → fieldwork → geography |
| T4 | Ministry & Bureaucracy | Haelgrund → census Thread data → intelligence |
| T5 | Martial Law | Löwenritter → Military governance → Accord |
| T6 | Altonian Invasion | IP from inter-faction battle → three-phase invasion → RM Underground |
| T7 | Local Actors | Non-faction NPCs → population will → governance feedback |
| T8 | Conviction Legacy | Convictions persist across Lineage → shape successor's world |
| T9 | **Church Pipeline** | Chapel → Cathedral + infrastructure → PT → CI → Mass Seizure. **Longest factional throughline (20+ seasons).** |
| T10 | Economic Pressure | Treasury drains from military → income from Prosperity → strategic decisions |
| T11 | **RM Identity Arc** | Consensus cells → Founding → Uprising → Governance Transition → Thread revelation → hidden bonus. **Most complex factional throughline.** |
| T12 | Morale-Legitimacy Cascade | Battle rout → Cohesion → Accord → governance failure |
| T13 | **Scale Transition Pipeline** | Character → settlement → territory → peninsula. **Most structurally load-bearing.** |
| T14 | Warden Emergence | Hermits → five paths to relevance → Mending Sanctuary |
| T15a | Hafenmark Sovereigntist | Shared theology, rejected monopoly. TS 0 = vulnerability |
| T15b | Löwenritter Protector | Military authority. Thread revelation: can't fight substrate decay |
| T15c | RM Heritage Reclaimer | Unknowing substrate inheritance. Vindication + crisis on revelation |

17 system throughlines, each traceable through 2+ documents.

<!-- atom: valoria_master_document__102__ii-1-stale-references-10-items | section_index: 102 | source_section: "II.1 Stale References (10 items)" -->


## II.1 Stale References (10 items)

| # | Location | Issue | Fix |
|---|----------|-------|-----|
| STALE-01 | CSR §3 | Composure = Cha + 6 | Update to Cha × 3 (ED-694) |
| STALE-02 | PP-275 | Stamina = End+H+1−armour | Strike. ED-694 (End × 5) is canonical |
| STALE-03 | PP-238 | Feint = full pool, Def = 0 | Strike. PP-294 (partial commitment) is canonical |
| STALE-04 | params/bg/core.md | Faction Assignment table duplicated | Remove duplicate |
| STALE-05 | params/core.md | Chain rule comment (exploding 10) | Strike or mark NON-CANONICAL |
| STALE-06 | PP-275 / ED-694 | Take a Breath restore formula conflict | Resolve formula and which History |
| STALE-07 | params/core.md | Bonds Disp ceiling vs Knot count divergence | Document rationale for formula split |
| STALE-08 | Multiple docs | Contact Rounds = Focus (old model) | Verify all updated to Thread Fatigue = Spi × 5 |
| STALE-09 | §3.3 of review | Unarmed conflated with weapon 3-axis system | Unarmed is separate category at TN 8 |
| STALE-10 | §3.3 header (FIXED in review) | Header read "warhammer/unarmed" | Already corrected |

<!-- atom: valoria_master_document__104__ii-3-gaps-11-items | section_index: 104 | source_section: "II.3 Gaps (11 items)" -->


## II.3 Gaps (11 items)

| # | Issue | Recommendation |
|---|-------|----------------|
| GAP-01 | Scene Lifecycle not formally codified | Create SceneLifecycle specification |
| GAP-02 | "Where Were You?" implementation thin | Define player actions, roll requirements |
| GAP-03 | Accounting 10-step density | Summary screen showing changes and causes |
| GAP-04 | Fieldwork-to-Echo split across two docs | Consolidate reference |
| GAP-05 | Companion system not atomically reviewed | Full NRES review needed |
| GAP-06 | Player Agency/Convictions/Standing/Renown not reviewed | Player progression framework needs review |
| GAP-07 | Derived Stats (Treasury/Legitimacy/Reputation/Cohesion) not reviewed | Economic throughline unverified |
| GAP-08 | Thread-Read Fatigue cost unspecified | Verify or assign cost |
| GAP-09 | "Session" undefined for videogame | Define session boundary (recommend: season-based) |
| GAP-10 | Accord derivation mapping incomplete | Map each legacy Accord input to settlement Order equivalent |
| GAP-11 | Tutorial pipeline missing | Design staged introduction for Godot |

<!-- atom: valoria_master_document__105__ii-4-provisional-items-17-total | section_index: 105 | source_section: "II.4 PROVISIONAL Items (17 total)" -->


## II.4 PROVISIONAL Items (17 total)

- **Mass combat: 14** (Volley TN, Lock phase, Discipline triggers, pool split default, crossbow reload, BG Partial threshold, Shield Wall scope, Thread-destroyed participation, general personal combat, mutual destruction, Command per sub-unit, Sling exception, Artillery Morale cap, Commander bonus)
- **Settlement: 2** (starting stats, governance Ob calibration)
- **TC: 1** (conditional passive thresholds)

Mass combat's 14 PROVISIONAL items mean the system is incomplete (S ✗). Needs canonicalization pass before Godot implementation.

<!-- atom: valoria_master_document__108__ii-7-architecture-strengths-mechanical | section_index: 108 | source_section: "II.7 Architecture Strengths (Mechanical)" -->


## II.7 Architecture Strengths (Mechanical)

1. One resolution engine at every scale — (Attr × 2) + H + 3, TN 6/7/8, Ob 1–20
2. Domain Echo as the personal→strategic pipe (mechanically — see Part III for experiential concerns)
3. Church Mass Seizure (one-shot, exponential declaration probability)
4. Settlement→Faction emergence (5-stage bottom-up progression)
5. Three-axis Thread Ob (Fibonacci depth + linear breadth/distance)
6. Weapon 3-axis matrix (3 bits → 8 archetypes → TN)
7. NPC Stance Triangle + Scar system (progressive AI destabilization)
8. Sincerity Gate (37% failure on instrumental relationships)
9. Post-Calamity continuation (MS=0 doesn't end the game)
10. Turmoil as anti-war counter (mechanically — see Part III)
11. Geneva Trap (Church infrastructure helps + creates dependency)
12. Thread→Conviction Scar Matrix (moral consequence for NPC witnesses)

<!-- atom: valoria_master_document__109__ii-8-architecture-weaknesses-mechanical | section_index: 109 | source_section: "II.8 Architecture Weaknesses (Mechanical)" -->


## II.8 Architecture Weaknesses (Mechanical)

1. **Contest CLASH stalls at median** — P1 blocker, not implementable as-is
2. **Mass combat incomplete** — 14 PROVISIONAL = S ✗
3. **Five+ unreviewed systems** — Companion, Player Agency, Derived Stats, Caste, Royal Assassination
4. **Ranged weapon dual taxonomy** — ED-129 open
5. **CI/Accounting density** — 7 nested in 10 steps (player-facing concern, see Part III)
6. **Thread-Read Fatigue cost unspecified** — potential degeneracy
7. **Stamina formula conflict** — PP-275 vs ED-694
8. **Domain Echo floor-function absorption** — ±1 Echo absorbed by floor(stat/2)+1 formulas (see Part III)
9. **Hafenmark Parliament mechanically thin** — single action type vs Church's multi-season pipeline

<!-- atom: valoria_master_document__111__ii-10-meta-throughlines-genuinely-emergent-vs-impo | section_index: 111 | source_section: "II.10 Meta-Throughlines (Genuinely Emergent vs. Imposed)" -->


## II.10 Meta-Throughlines (Genuinely Emergent vs. Imposed)

After audit, four meta-throughlines genuinely emerge from system intersections (each predicts gameplay outcomes from structural features):

- **M1: Knowledge-Power Disjunction** — No single faction has both metaphysical knowledge and political power. Predicted from victory conditions + NPC distribution.
- **M2: Institutional Trap** — Every institutional benefit has institutional cost. Predicted from Geneva Trap + Crown Treaty + Hafenmark procedure.
- **M3: Scale Recursion** — Same engine at every scale. Predicted from formula consistency.
- **M5: Dual Clock** — Sovereignty contest competes with survival contest. Predicted from MS budget vs. PV requirements.

Four "meta-throughlines" identified during the throughlines pass do not survive scrutiny:

- **M4: Asymmetric Information** — Standard asymmetric game design pattern. Not emergent.
- **M6: Moral Architecture of Thread** — Authored design intention, not emergent pattern.
- **M7: Bottom-Up Political Possibility** — A feature (settlement→faction emergence), not a meta-pattern.
- **M8: Relational Load-Bearing** — Overstated; Knots are necessary for practitioners at Coherence risk, optional otherwise.


---

# PART III: GAMEPLAY EXPERIENCE AND WORLDBUILDING FINDINGS REGISTER

This part consolidates findings from the gameplay experience and worldbuilding audits. **All findings in this part are extrapolations or design hypotheses, not verified facts.** Several are flagged [TTRPG-FRAMING] where the original analysis used wrong-medium assumptions.

<!-- atom: valoria_master_document__113__iii-2-findings-affected-by-ttrpg-vs-videogame-fram | section_index: 113 | source_section: "III.2 Findings Affected by TTRPG-vs-Videogame Framing Errors" -->


## III.2 Findings Affected by TTRPG-vs-Videogame Framing Errors

The following findings were generated using TTRPG audit assumptions and require recalibration:

**Cognitive load count (~9 values per combat turn):** In TTRPG, the player tracks state mentally. In videogame, the engine tracks state and the UI presents the relevant subset. Cognitive load becomes a UI design problem, not a rule-count problem. The 14-action combat menu is fine when contextually filtered to applicable actions.

**Engagement valley duration:** Calculated as ~15 hours of ~48-hour campaign (TTRPG pacing). Videogame pacing produces ~3-6 hours of valley in ~8-15 hour campaign. Smaller absolute risk.

**Mass combat investment-to-use ratio:** "20% documentation for 4% playtime" used TTRPG estimates. At videogame pacing, mass combat fires 5 times across ~8-15 hours = ~5-10% of playtime. The procedural complexity concern is also reducible by UI: 7 engine phases → 3 UI phases (Strategy, Thread commitment, Engagement decisions; auto-resolve Volley/Manoeuvre/Reform).

**Tie Up "is it worth a button?":** Videogames hide rarely-applicable actions contextually. Tie Up only appears when the situation supports it. Zero UI cost when inapplicable.

**Investigation pacing (no opposition):** The Church Attention Pool already advances during investigation (via Exposure feeding AP). Procedural opposition exists; I missed it because I was looking for table-visible mechanics.

**Domain Echo invisibility:** Partially solvable in videogame via immediate notification on Echo trigger. The remaining concern (floor function absorption in downstream formulas) is a math problem, not a presentation problem. That part stands.

<!-- atom: valoria_master_document__114__iii-3-claims-that-survive-recalibration | section_index: 114 | source_section: "III.3 Claims That Survive Recalibration" -->


## III.3 Claims That Survive Recalibration

Despite framing errors, these gameplay/worldbuilding findings remain valid in videogame context:

1. **Domain Echo floor-function absorption (GX-09 partial):** Math-level. Going from Mandate 4→5 produces no change in floor(5/2)+1. UI cannot display a difference that doesn't exist downstream. The Echo magnitude vs. consuming-formula granularity is a design mismatch.

2. **Power moments require staging (GX-12):** Overwhelming success, Mass Seizure, settlement Flourishing, Breach encounters — each requires presentation work to convert mechanical significance into experiential significance. This is a content-design requirement, not a mechanical flaw.

3. **Victory needs a ceremony (GX-14):** No mechanical victory presentation is specified. A videogame can implement one cheaply (cutscene, summary screen, world Portrait Sequence). The finding identifies the requirement.

4. **NPC personality requires voice (WB-12):** The Stance Triangle creates the AI. Whether NPCs FEEL like people depends on dialogue, recurring phrases, characteristic reactions — content layer, not mechanical layer.

5. **Thread geographic concentration (WB-13):** Northern factions (Crown, Hafenmark, Church) can play 10+ seasons before meaningful Thread engagement. The political/social systems must sustain that period independently.

6. **Hafenmark Parliament thinness (WB-16):** Single action type vs. Church's multi-season infrastructure pipeline. Asymmetry between factional mechanical depth.

<!-- atom: valoria_master_document__116__iv-1-verify-against-source | section_index: 116 | source_section: "IV.1 Verify Against Source" -->


## IV.1 Verify Against Source

| Finding | What to verify | Document to check |
|---------|----------------|-------------------|
| Thread-Read Fatigue cost (GAP-08) | Does the threadwork doc list a Fatigue cost for Thread-Read? | params/threadwork.md |
| Conviction taxonomy (DECISION-12) | Are Warden and Community truly faction-restricted? | designs/npcs/npc_behavior_v30.md §2 |
| Evidence/positional cap stacking (DECISION-14) | How are Evidence (+2D) and positional (+5D) caps related? | designs/scene/fieldwork_v30.md §2.5; designs/npcs/npc_behavior_v30.md §6.5 |
| Crown Treaty re-sign cooldown (DECISION-15) | Does PP-528 explicitly address lapse vs. refusal? | params/bg/core.md (or wherever PP-528 lives) |
| Spirit non-practitioner uses (DECISION-02) | I claimed 4 uses (Resolve, Sincerity Gate, Dissonance, ED-664). Verify all four exist. | params/core.md, params/threadwork.md, ED-664 |
| 14 PROVISIONAL items in mass combat | Re-list and verify count | params/mass_combat.md |
| Domain Echo floor-function math (GX-09) | Spot-check: which downstream formulas use floor(stat/2)+1 vs. linear stat? | params/bg/core.md Domain Action Ob formulas |
| Accord derivation legacy mappings (GAP-10) | Each old Accord rule needs settlement Order equivalent specified | designs/territory/settlement_layer_v30.md vs. designs/provincial/peninsular_strain_v30.md |

<!-- atom: valoria_master_document__119__v-1-companion-system-gap-05 | section_index: 119 | source_section: "V.1 Companion System (GAP-05)" -->


## V.1 Companion System (GAP-05)

**Why it matters:** Companions are the player's primary persistent agency tool. They serve as settlement governors (free governance action), mass combat officers (Command contribution), contest allies (Knot buffer), Thread anchors (Coherence stabilization), and personal-scene relationship targets.

**Sources to fetch:** `designs/npcs/companion_specification_v30.md` (referenced in NPC behavior doc).

**Review questions:**
- How are companions acquired? Disposition gates, recruitment procedure (PP-642), Standing thresholds?
- How do companions advance? Independent character sheets or attached to player?
- How does companion death/loss interact with Knots (Loss = Coherence −1)?
- What is the companion-generated scene rate? (Identified gap in gameplay audit GX-04.)

<!-- atom: valoria_master_document__120__v-2-player-agency-convictions-standing-renown-gap- | section_index: 120 | source_section: "V.2 Player Agency / Convictions / Standing / Renown (GAP-06)" -->


## V.2 Player Agency / Convictions / Standing / Renown (GAP-06)

**Why it matters:** This is the player's interface to all other systems. Convictions drive Portrait Retirement (campaign endpoint). Standing gates governance assignments. Renown gates scene types and faction access.

**Sources to fetch:** `designs/architecture/player_agency_v30_index.md` and full content.

**Review questions:**
- How are Convictions authored? Free-form vs. typed selection at character creation?
- What are the Conviction resolution mechanics? (Fulfilled/Failed/Transformed/Unresolved per Portrait Retirement.)
- What is the Standing 0–5 ladder? Specific thresholds for governance, scene access, NPC interaction?
- What is the Renown 0–10 progression? Earning rates, threshold effects?
- ED-664 player Conviction checks (Spirit TN 7 Ob 1 on Thread witnessing) — specifications?

## Provenance

Atom-by-atom inventory in source/section order:

| atom_id | source | section_index | source_section | lines |
|---|---|---|---|---|
| `valoria_session_2026-04-25_master__05__section-5-cross-reference-audit` | `VALORIA_SESSION_2026-04-25_MASTER.md` | 5 | Section 5 — Cross-Reference Audit | 24 |
| `valoria_session_2026-04-25_master__07__section-7-files-modified` | `VALORIA_SESSION_2026-04-25_MASTER.md` | 7 | Section 7 — Files Modified | 32 |
| `master_consolidation__02__2-ed-738-ein-sof-gradient-editorial` | `master_consolidation.md` | 2 | §2 ED-738 — Ein Sof gradient editorial | 44 |
| `master_consolidation__11__11-methodological-notes-for-continuation` | `master_consolidation.md` | 11 | §11 Methodological notes for continuation | 18 |
| `threadwork_master__00__preamble` | `threadwork_master.md` | 0 | (preamble) | 10 |
| `threadwork_master__01__i-foundational-stance` | `threadwork_master.md` | 1 | I. Foundational stance | 38 |
| `threadwork_master__02__ii-the-substrate-s-language-held-in-silence` | `threadwork_master.md` | 2 | II. The substrate's language (held in silence) | 15 |
| `threadwork_master__03__iii-what-the-player-should-feel` | `threadwork_master.md` | 3 | III. What the player should feel | 196 |
| `threadwork_master__04__iv-three-stories-the-system-produces` | `threadwork_master.md` | 4 | IV. Three stories the system produces | 30 |
| `threadwork_master__05__v-operations-what-threadwork-verbs-do` | `threadwork_master.md` | 5 | V. Operations — what threadwork verbs do | 43 |
| `threadwork_master__06__vi-apparatus-what-the-practitioner-carries` | `threadwork_master.md` | 6 | VI. Apparatus — what the practitioner carries | 18 |
| `threadwork_master__07__vii-architecture-in-implementation-order` | `threadwork_master.md` | 7 | VII. Architecture in implementation order | 79 |
| `threadwork_master__08__viii-substrate-ontology-constraints` | `threadwork_master.md` | 8 | VIII. Substrate ontology constraints | 26 |
| `threadwork_master__09__ix-decisions-awaiting-jordan` | `threadwork_master.md` | 9 | IX. Decisions awaiting Jordan | 42 |
| `threadwork_master__10__x-open-dependencies` | `threadwork_master.md` | 10 | X. Open dependencies | 18 |
| `threadwork_master__11__xi-the-game` | `threadwork_master.md` | 11 | XI. The game | 37 |
| `valoria_master_consolidation__01__2-1-the-bridge-work-2026-04-16-is-structurally-com` | `valoria_master_consolidation.md` | 1 | 2.1 The bridge work (2026-04-16) is structurally c | 21 |
| `valoria_master_consolidation__03__2-3-simulation-framework-exists-and-is-growing` | `valoria_master_consolidation.md` | 3 | 2.3 Simulation framework exists and is growing | 4 |
| `valoria_master_consolidation__04__2-4-recent-canonical-strikes` | `valoria_master_consolidation.md` | 4 | 2.4 Recent canonical strikes | 8 |
| `valoria_master_consolidation__06__2-6-npc-and-faction-interdependency-mapped` | `valoria_master_consolidation.md` | 6 | 2.6 NPC and faction interdependency mapped | 4 |
| `valoria_master_consolidation__08__2-8-per-system-quality-is-high` | `valoria_master_consolidation.md` | 8 | 2.8 Per-system quality is high | 31 |
| `valoria_master_consolidation__09__4-1-the-five-moments-framework` | `valoria_master_consolidation.md` | 9 | 4.1 The Five Moments Framework | 21 |
| `valoria_master_consolidation__10__4-2-the-primary-verb-sustain` | `valoria_master_consolidation.md` | 10 | 4.2 The Primary Verb: Sustain | 18 |
| `valoria_master_consolidation__12__4-4-multi-perspectival-chroniclers` | `valoria_master_consolidation.md` | 12 | 4.4 Multi-Perspectival Chroniclers | 20 |
| `valoria_master_consolidation__13__4-5-rendering-strain-substrate-posture-cost` | `valoria_master_consolidation.md` | 13 | 4.5 Rendering Strain (Substrate-Posture Cost) | 19 |
| `valoria_master_consolidation__14__4-6-per-faction-thread-entry-points` | `valoria_master_consolidation.md` | 14 | 4.6 Per-Faction Thread Entry Points | 23 |
| `valoria_master_consolidation__15__4-7-confrontation-only-ts-era-contingent` | `valoria_master_consolidation.md` | 15 | 4.7 Confrontation-Only TS, Era-Contingent | 19 |
| `valoria_master_consolidation__16__4-8-cold-open-progressive-system-activation` | `valoria_master_consolidation.md` | 16 | 4.8 Cold Open + Progressive System Activation | 21 |
| `valoria_master_consolidation__17__4-9-multi-generational-lineage-variant-eras` | `valoria_master_consolidation.md` | 17 | 4.9 Multi-Generational Lineage + Variant Eras | 19 |
| `valoria_master_consolidation__23__from-complete-system-audit-valoria-complete-system` | `valoria_master_consolidation.md` | 23 | From complete system audit (`valoria_complete_syst | 4 |
| `valoria_master_consolidation__31__phase-vi-per-faction-thread-entry-points` | `valoria_master_consolidation.md` | 31 | Phase VI — Per-Faction Thread Entry Points | 12 |
| `valoria_master_consolidation__35__phase-x-vertical-slice-playtest-iteration` | `valoria_master_consolidation.md` | 35 | Phase X — Vertical Slice Playtest Iteration | 27 |
| `valoria_master_consolidation__38__what-the-recommendations-are` | `valoria_master_consolidation.md` | 38 | What the recommendations are | 8 |
| `valoria_master_document__02__subject-recursive-mechanical-review-of-the-valoria` | `valoria_master_document.md` | 2 | Subject: Recursive mechanical review of the Valori | 47 |
| `valoria_master_document__04__1-2-tn-values` | `valoria_master_document.md` | 4 | 1.2 TN Values | 12 |
| `valoria_master_document__07__1-5-pool-minimum-1d` | `valoria_master_document.md` | 7 | 1.5 Pool Minimum (1D) | 6 |
| `valoria_master_document__08__1-6-momentum-0-4` | `valoria_master_document.md` | 8 | 1.6 Momentum (0–4) | 10 |
| `valoria_master_document__09__2-1-attributes-10-range-1-7` | `valoria_master_document.md` | 9 | 2.1 Attributes (10, range 1–7) | 23 |
| `valoria_master_document__10__2-2-derived-scores` | `valoria_master_document.md` | 10 | 2.2 Derived Scores | 38 |
| `valoria_master_document__25__4-6-key-sub-mechanics` | `valoria_master_document.md` | 25 | 4.6 Key Sub-Mechanics | 16 |
| `valoria_master_document__26__5-1-thread-pool` | `valoria_master_document.md` | 26 | 5.1 Thread Pool | 6 |
| `valoria_master_document__33__5-8-wr-wc` | `valoria_master_document.md` | 33 | 5.8 WR/WC | 6 |
| `valoria_master_document__35__5-10-mending-community-tiers` | `valoria_master_document.md` | 35 | 5.10 Mending Community Tiers | 10 |
| `valoria_master_document__36__6-1-depth-axis-0-5` | `valoria_master_document.md` | 36 | 6.1 Depth Axis (0–5) | 8 |
| `valoria_master_document__42__6-7-system-transitions-6-bidirectional` | `valoria_master_document.md` | 42 | 6.7 System Transitions (6 bidirectional) | 17 |
| `valoria_master_document__44__7-2-phase-structure` | `valoria_master_document.md` | 44 | 7.2 Phase Structure | 6 |
| `valoria_master_document__47__8-1-scene-types` | `valoria_master_document.md` | 47 | 8.1 Scene Types | 12 |
| `valoria_master_document__52__9-3-ethical-framework-modifiers` | `valoria_master_document.md` | 52 | 9.3 Ethical Framework Modifiers | 6 |
| `valoria_master_document__57__10-1-eight-handoff-rules` | `valoria_master_document.md` | 57 | 10.1 Eight Handoff Rules | 6 |
| `valoria_master_document__58__10-2-domain-echo-the-upward-pipe` | `valoria_master_document.md` | 58 | 10.2 Domain Echo (The Upward Pipe) | 10 |
| `valoria_master_document__60__11-1-turn-sequence` | `valoria_master_document.md` | 60 | 11.1 Turn Sequence | 18 |
| `valoria_master_document__62__12-1-ms-mending-stability` | `valoria_master_document.md` | 62 | 12.1 MS (Mending Stability) | 6 |
| `valoria_master_document__66__12-5-personal-scale-tracks` | `valoria_master_document.md` | 66 | 12.5 Personal-Scale Tracks | 10 |
| `valoria_master_document__82__16-1-stance-triangle` | `valoria_master_document.md` | 82 | 16.1 Stance Triangle | 31 |
| `valoria_master_document__85__16-4-belief-revision-and-scars` | `valoria_master_document.md` | 85 | 16.4 Belief Revision and Scars | 32 |
| `valoria_master_document__91__16-1-thread-revelation-curve` | `valoria_master_document.md` | 91 | 16.1 Thread Revelation Curve | 6 |
| `valoria_master_document__92__16-2-portrait-retirement-and-lineage` | `valoria_master_document.md` | 92 | 16.2 Portrait Retirement and Lineage | 6 |
| `valoria_master_document__96__20-3-personal-to-global-chain-verified` | `valoria_master_document.md` | 96 | 20.3 Personal-to-Global Chain (Verified) | 13 |
| `valoria_master_document__97__19-1-narrative-throughlines-what-the-game-is-about` | `valoria_master_document.md` | 97 | 19.1 Narrative Throughlines (What the Game Is Abou | 13 |
| `valoria_master_document__98__19-2-system-throughlines-how-mechanics-connect` | `valoria_master_document.md` | 98 | 19.2 System Throughlines (How Mechanics Connect) | 24 |
| `valoria_master_document__102__ii-1-stale-references-10-items` | `valoria_master_document.md` | 102 | II.1 Stale References (10 items) | 15 |
| `valoria_master_document__104__ii-3-gaps-11-items` | `valoria_master_document.md` | 104 | II.3 Gaps (11 items) | 16 |
| `valoria_master_document__105__ii-4-provisional-items-17-total` | `valoria_master_document.md` | 105 | II.4 PROVISIONAL Items (17 total) | 8 |
| `valoria_master_document__108__ii-7-architecture-strengths-mechanical` | `valoria_master_document.md` | 108 | II.7 Architecture Strengths (Mechanical) | 15 |
| `valoria_master_document__109__ii-8-architecture-weaknesses-mechanical` | `valoria_master_document.md` | 109 | II.8 Architecture Weaknesses (Mechanical) | 12 |
| `valoria_master_document__111__ii-10-meta-throughlines-genuinely-emergent-vs-impo` | `valoria_master_document.md` | 111 | II.10 Meta-Throughlines (Genuinely Emergent vs. Im | 23 |
| `valoria_master_document__113__iii-2-findings-affected-by-ttrpg-vs-videogame-fram` | `valoria_master_document.md` | 113 | III.2 Findings Affected by TTRPG-vs-Videogame Fram | 16 |
| `valoria_master_document__114__iii-3-claims-that-survive-recalibration` | `valoria_master_document.md` | 114 | III.3 Claims That Survive Recalibration | 16 |
| `valoria_master_document__116__iv-1-verify-against-source` | `valoria_master_document.md` | 116 | IV.1 Verify Against Source | 13 |
| `valoria_master_document__119__v-1-companion-system-gap-05` | `valoria_master_document.md` | 119 | V.1 Companion System (GAP-05) | 12 |
| `valoria_master_document__120__v-2-player-agency-convictions-standing-renown-gap-` | `valoria_master_document.md` | 120 | V.2 Player Agency / Convictions / Standing / Renow | 13 |
