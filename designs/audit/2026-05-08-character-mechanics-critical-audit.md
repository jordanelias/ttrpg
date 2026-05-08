# Critical Audit — All Character Mechanics

**Date:** 2026-05-08 · **Status:** PROVISIONAL audit document. Not commit-ready.
**Scope:** Every mechanical surface attached to a character (PC or NPC) in current canon, plus all proposals from the last four conversational turns. Foundational mechanics (Beliefs, Inspirations, Convictions) audited with the same scrutiny as the newest proposals. No mechanic exempt by pedigree.
**Methodology:** NERS per mechanic; interaction map; per-decision load test; coverage-gap analysis. Findings ranked: load-bearing / valuable / audit-flag / cut-or-fold.
**Stance:** academic rigour, enthusiast fervour, snob criticality. The point is to surface the truth, not to defend prior decisions.

---

## §0 — Thesis

The character system has three primary layers and four supporting ones:

1. **Personality** (interior gate) — Convictions, Beliefs, Self-Other, Resonant Style, cultural template, Conviction Track.
2. **Competence** (exterior gate) — Lifepath histories, Skills, Sparking, attribute pools, Recall.
3. **Metaphysical** (substrate layer) — TS, Coherence, Spirit, Certainty, Substrate-Posture.
4. *Relational* — Knots, Disposition, Foils, Standing, Caste, Renown.
5. *Behavioral/temporal* — Tier system, Behavioral AI flaw, Priority Trees, Arc state machine, Stance triangles, Decision Forks.
6. *Narrative* — Inspirations, Articulation Layer, Forgetting.
7. *Specialized* — Shadow Renown, Deniability Debt, Companion specification.

**Headline finding:** the system is **architecturally sound but accreted.** The personality layer is genuinely well-designed and integrates elegantly with the metaphysical and relational layers. The competence layer is sound but underused (histories are not yet content-bearing). The accretion is in the relational and behavioral categories — at least four mechanics overlap or duplicate (Standing/Renown, Stance triangles/Resonant Style, Decision Forks/Conviction Track effects, NPC Belief/PC Belief). The biggest single coverage gap is **PC interiority** — voiced inner life of the player character.

**My own proposals from the last four turns: ~30% earn their place; ~50% are scoped-down keepers; ~20% should be cut.** This document does the cuts.

---

## §1 — Inventory (52 mechanics, 9 categories)

| Category | Mechanics |
|---|---|
| **Foundational (earliest)** | (1) Inspirations · (2) Beliefs · (3) Goals |
| **Personality** | (4) Convictions [13D + cultural template] · (5) Cultural Background Templates [8] · (6) Self-Other orientation · (7) Resonant Style [4] · (8) Conviction Track [Scars] · (9) Belief revision mechanic |
| **Competence** | (10) Lifepath [4 stages] · (11) History-derived Skills · (12) Sparking · (13) Recall · (14) Attribute d-pools [Mind/Body/Spirit] · (15) Sub-pools [Cognition/Focus/Endurance/Charisma/Bonds] |
| **Metaphysical** | (16) Thread Sensitivity · (17) Coherence · (18) Spirit (metaphysical attribute, distinct from #14 Spirit pool) · (19) Certainty · (20) Substrate-Posture [T-15] |
| **Relational** | (21) Knots/Bonds · (22) Disposition · (23) Foil pairings/Ruler Diamond · (24) Standing per faction · (25) Renown · (26) Caste |
| **Behavioral/temporal** | (27) Tier system [1/2/3/Background] · (28) Behavioral AI flaw [Tier 2] · (29) Priority Trees [Tier 1] · (30) Stance triangles · (31) Arc state machine · (32) Per-NPC arc maps · (33) Decision Forks |
| **Narrative** | (34) Articulation Layer cut scenes [10 triggers] · (35) Per-Belief engagement count · (36) Forgetting · (37) Stance positioning |
| **Specialized** | (38) Shadow Renown · (39) Deniability Debt · (40) Companion specification |
| **Proposed (last 4 turns)** | (41) Conviction voices · (42) Reaction-shape library · (43) Conviction invocations · (44) History content-access · (45) History acquisition during play · (46) Per-NPC speech register · (47) Tier-3 texture floor · (48) Drift visualization · (49) Languages grid · (50) Knowledge domains grid · (51) Competencies grid · (52) Per-territory reputation |

That is 52 character-attached mechanics. The number itself is the first finding.

---

## §2 — Per-mechanic NERS audit

NERS = Necessary / Elegant / Robust / Smooth. Verdict column abbreviations: **KEEP** (load-bearing, no changes); **KEEP+** (load-bearing, but propagation/cleanup needed); **AUDIT** (interaction or scope question for Jordan); **SCOPE** (concept earns its place but proposed scope is too large); **FOLD** (fold into existing mechanic); **DEFER** (nice-to-have, not load-bearing); **CUT** (over-engineered or duplicate).

### §2.1 Foundational (Inspirations, Beliefs, Goals — the earliest)

**(1) Inspirations.** Two distinct mechanics share the name:
- **PC Inspirations** (`articulation_layer §2.4`): player-authored aspirational arcs with per-Belief-style engagement counts.
- **NPC Inspirations** (proposed by me, lifted from `npc_character_analyses_v30` literary framing): two facets — `historical_parallel` (author-side analytic anchor: Sorge, Luxemburg, Henry VIII) + `in_character_aspiration` (in-fiction model the NPC orients toward).

| Verdict | NERS | Note |
|---|---|---|
| **KEEP+** | N: high · E: low (naming collision) · R: high · S: mid | Two mechanics, same name. They do different work. Rename one. The PC version is closer to a Goal-type structure; the NPC version is part designer-shorthand part in-character motivation. **Snob finding:** `in_character_aspiration` may not be distinct from Goal — examine whether it earns separate field. |

**(2) Beliefs.** First-person quoted truth-statements. Drive Contests, revision, Scars, prose-writer voice anchors.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP+** | N: critical · E: mostly · R: high · S: mid | The single most foundational character-mechanic. **Snob findings:** (a) PC Beliefs (articulation_layer §2.4 — engagement-counted aspirations) and NPC Beliefs (npc_behavior §3 — first-person truth-statements) are different mechanics under one name; conflation is sloppy. (b) Belief revision requires three conjunctive conditions; in practice this means Beliefs are very stable. Calibration question: intended or accidental? (c) Beliefs are unranked — a character's three Beliefs all carry equal narrative weight. Should there be primary/secondary? (d) Belief Scars are permanent — great for arc weight, potential issue for replayability. |

**(3) Goals.** Implicit in Behavioral AI prose for Tier 2; explicit in Mission for factions; partially captured in arc maps for Tier 1.

| Verdict | NERS | Note |
|---|---|---|
| **AUDIT** | N: high · E: low · R: mid · S: low | Goals are scattered across implicit fields. Either author them as a first-class field per Tier 1+2 NPC, or fold into Inspiration's `in_character_aspiration` facet. Currently they exist without a clean home. |

### §2.2 Personality layer

**(4) Convictions [13D vector + cultural template].** PP-684 13-Conviction taxonomy. Primary 1–3 weighted to sum 0.6–0.8; cultural background fills 0.2–0.4.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP+** | N: critical · E: mid (13 is bloat-adjacent) · R: very high · S: mid (3-taxonomy succession debt persists) | The crown jewel. PP-684 §2 defends each Conviction with load-bearing Renaissance grounding. **Snob findings:** (a) 13 may be more than gameplay can engage with — if the player meaningfully engages with 3–4 of their character's Convictions across a campaign, the other 9–10 are scenery. Test by sim. (b) Convictions are positive-valence only; "anti-Faith" is implicit (low Faith weight) but not equivalent to active opposition. Possible gap. (c) Cultural template auto-fills 0.2–0.4 — if a player wants a non-template character (Crown courtier raised by Restoration, for example), the template system flexes how? Authoring needed. |

**(5) Cultural Background Templates [8].** `solmund_alpine`, `solmund_lowland_merchant`, `valorian_court`, `ecclesiastical`, `hafenmark_procedural`, `lowenritter_military`, `restoration_reformist`, `einhir_traditional`.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: mid · S: high | 8 covers main settings. No additions needed. |

**(6) Self-Other orientation.** Scalar [-1, +1], drifts under accumulated outcomes (κ = 0.03).

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: critical · E: very high · R: high · S: high | One of the most elegant pieces in the system. **Snob findings:** (a) binary toward-self vs toward-collective doesn't admit "toward this specific other" (parent, child, lover) — relational pluralism not modeled. (b) κ = 0.03 is calibration-pending — miscalibrated, drift is either sluggish (no Macbeth arc) or volatile (random-walk instability). |

**(7) Resonant Style [4].** Evidence / Consequence / Authority / Solidarity. Primary + secondary.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP+** | N: high · E: high · R: mid · S: mid | The shape of arguments that reach this person. **Snob findings:** (a) styles are not orthogonal — "Authority-via-Solidarity" is a real argument shape (a recognized leader appealing on shared bonds) that compresses poorly into one of the 4. (b) TS Gate restricts Evidence on TS-0 NPCs (perceptual prophylaxis) but no equivalent gate on Authority-from-Church-context for skeptics, etc. — inconsistent application of the same logic. (c) Wrong-Style Penalty is flat +1 Ob; should arguably differ by mismatch type. |

**(8) Conviction Track [Scars].** 0/1/2/3+ Scars structure. Crisis table at 3+. Source file uses stale 9-Conviction taxonomy (per audit D8).

| Verdict | NERS | Note |
|---|---|---|
| **KEEP+** | N: critical · E: high · R: very high · S: low (taxonomy debt) | THE arc-emergence engine. Crisis table d6 entry "5: Autonomy" → "Liberty" remap from PP-684 §6. Source file propagation pending. **Snob finding:** the crisis table is d6-flat — it doesn't account for *which* Convictions the character actually has weight on. A 3-Scar character with no Faith weight should never roll "Faith intercedes." Calibration. |

**(9) Belief revision mechanic.** Three conjunctive conditions: decisive Contest + Resonant Style match + specific Belief engagement.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: mid · S: high | See snob notes on (2). The conjunction is a deliberate stability lock. |

### §2.3 Competence layer

**(10) Lifepath [4 stages: Origin/Formation/Vocation/Catalyst].**

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: critical · E: high · R: very high · S: high | Character creation chassis. 4 stages produces wide combinatorial space. |

**(11) History-derived Skills.** Level 1–3. ★ unique per stage; § marked in spark list.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: mid · S: high | The granular competence layer. Levels 1–3 is appropriately tight. **Snob finding:** the ★/§ distinction adds an authoring overhead that produces marginal gameplay distinction. Could simplify. |

**(12) Sparking.** Spirit + floor(Recall/2) check after meaningful scene rolls Ob ≥ 2; cross-History hybrid sparks at Ob 2+ Success+ across 2+ histories.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: high · S: high | Skill-acquisition during play. SaGa-style. Works. |

**(13) Recall.** Stat used only as sparking gatekeeper.

| Verdict | NERS | Note |
|---|---|---|
| **AUDIT/FOLD** | N: low · E: low · R: low · S: low | Standalone stat for a single mechanic. **Snob finding:** Recall is BW-Wises heritage. In a videogame the engine tracks what the character has experienced; Recall as a player-tracked stat is overhead. Recommend folding into Mind or Spirit pool, or eliminating in favor of a fixed-Ob check. |

**(14) Attribute d-pools [Mind/Body/Spirit].** BW-style core attributes.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: high · S: high | Core resolution mechanism. Tight 3-attribute set. |

**(15) Sub-pools [Cognition/Focus/Endurance/Charisma/Bonds].** Visible in NPC stat blocks (Edeyja, etc.).

| Verdict | NERS | Note |
|---|---|---|
| **AUDIT** | N: ? · E: ? · R: ? · S: ? | I do not have full visibility into how sub-pools relate to Mind/Body/Spirit. Are sub-pools derived from main pools, or independent stats? If independent, that's 8 attribute tracks per character which is starting to get crunchy. Need clarification. |

### §2.4 Metaphysical / substrate layer

**(16) Thread Sensitivity (TS, 0–100).** Substrate-perception axis. Bands: Foreclosed → Latent → Hidden → Dormant → Stirring → Active → Deep → Apex.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: critical · E: high · R: very high · S: high | The substrate-perception axis. Setting-defining. |

**(17) Coherence [0–10].** Self-rendering integrity. Bands: Stable → Dissonant → Fragmented → Fractured → Severed → Conversion. MS Override at MS≤20 for Warden NPCs.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: critical · E: high · R: high · S: high | Distinct from TS. Distinct from Spirit. Earns place. |

**(18) Spirit (metaphysical attribute) [1–7].** Distinct from #14 Spirit *pool*. Whether will continues to grip when rendering fails (Beckett vs Lispector textures).

| Verdict | NERS | Note |
|---|---|---|
| **KEEP+** | N: high · E: low (naming collision with Spirit pool) · R: high · S: low (collision) | **Snob finding:** Spirit-the-pool and Spirit-the-metaphysical-attribute are different things with the same name. This is a worse naming collision than Belief/Belief or Inspiration/Inspiration because both Spirits are quantitative. Rename one. Candidate: rename the metaphysical attribute "Will" or "Vital Spirit" — Beckett texture is about will-to-grip, not spirit-the-pool. |

**(19) Certainty [0–5].** Cosmological framework alignment with Solmundan orthodoxy.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: high · S: high | Distinct from Conviction (moral) and from Coherence (self-render). Tracks framework-fit. Earns place. |

**(20) Substrate-Posture [T-15 series].** Faction-level (Hafenmark T-15a, Löwenritter T-15b, RM T-15c). Four other factions un-authored.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP+** | N: high · E: mid · R: high · S: low (gaps) | Earned for the three authored factions. Crown / Church / Varfell / Guilds gaps acknowledged. **Snob finding:** is this a *character* mechanic or a *faction* mechanic? It's filtered through the leader's POV, so both. Inelegant categorization. |

### §2.5 Relational layer

**(21) Knots/Bonds.** Distant / Acquaintance / Close / Intimate. 3 Close max.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: critical · E: high · R: high · S: high | Necessary for Solidarity Resonant Style; gates intimate scenes; produces Knot strain on transformation. |

**(22) Disposition.** Per-NPC tracker (-3 to +3 typical).

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: mid · S: high | Distinct from Knot (Disposition = like/dislike; Knot = closeness). |

**(23) Foil pairings / Ruler Diamond.** Cross-NPC structural relationships.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: high · S: high | Generates structural tension without scripted beats. Empty bodies in canon (~40% of pairings) acknowledged in audit. |

**(24) Standing per faction.** 0–7 reputation track per faction. 8 factions (currently 7 active + Niflhel struck).

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: critical · E: high · R: high · S: high | Faction reputation. |

**(25) Renown.** Public-facing reputation.

| Verdict | NERS | Note |
|---|---|---|
| **AUDIT/FOLD** | N: ? · E: low (overlap with Standing) · R: ? · S: low | **Snob finding:** Renown and Standing both track reputation. Renown is public-general, Standing is per-faction. Are they actually different in gameplay, or could Renown be derived from Standings (e.g., max-Standing-or-sum-of-Standings)? If derived, eliminate Renown as an authored stat. |

**(26) Caste.** Common / Skilled / Houseborn / Sworn / Noble. Sets Standing ladder floors per `faction_politics §3`.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high (Renaissance setting) · E: high · R: high · S: high | 5 castes; sets ceilings/floors on faction Standings. Period-appropriate. **Snob finding:** is Caste-as-mechanical-floor actually used in play, or is it narrative texture? If purely narrative, fold into Background. Likely actual use; verify with Jordan. |

### §2.6 Behavioral / temporal layer

**(27) Tier system [1/2/3/Background].** Roster Tracking Capacity.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: critical · E: high · R: high · S: high | Engine resource management. PP-661. |

**(28) Behavioral AI flaw [Tier 2].** Per-NPC mechanical flaw with consequence (e.g., Strand's flattery vulnerability).

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: high · S: high | Mechanical individuation for Tier 2. Single-flaw structure is tight. |

**(29) Priority Trees [Tier 1].** Behavioral AI for Tier 1 NPCs.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: high · S: high | Tier 1 needs more depth than Tier 2 flaw. Tree structure earns place. |

**(30) Stance triangles.** Conviction × Resonant Style × Personal Goal positioning.

| Verdict | NERS | Note |
|---|---|---|
| **AUDIT/FOLD** | N: ? · E: low · R: low · S: low | **Snob finding:** Stance triangles were the OLD positioning system pre-PP-684 cleanup. The three components (Conviction, Resonant Style, Personal Goal) all exist as independent fields now. The triangle as a *composite object* may be vestigial. If still queried by the engine, document the query path; if not, retire as a composite. |

**(31) Arc state machine.** Generic transition triggers.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: high · S: high | Generic triggers per `npc_behavior §5.1`. |

**(32) Per-NPC arc maps.** A/B/C minimum per Tier 1; some have D/E/F (royal-fuse arcs).

| Verdict | NERS | Note |
|---|---|---|
| **KEEP+** | N: high · E: high · R: high · S: low (empty bodies) | Vaynard Arc A and Arc B are empty bodies in `§5.2`. Acknowledged gap. |

**(33) Decision Forks.** Increase under Conviction Scars.

| Verdict | NERS | Note |
|---|---|---|
| **AUDIT/FOLD** | N: ? · E: low · R: low · S: ? | **Snob finding:** "Decision Forks increase" appears in the Scar accumulation table but isn't a separately tracked thing. Is this a tracked engine quantity or a documentary phrase? If documentary, fold into Conviction Track Scar effects (which already encode the increased internal-conflict behavior). |

### §2.7 Narrative layer

**(34) Articulation Layer cut scenes.** 10 trigger conditions; PP-688.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP+** | N: high · E: mid (10 triggers borderline) · R: high · S: mid | Moment-to-moment scene density. **Snob finding:** §2.4 (PC Beliefs/Inspirations) and §3.1 trigger #10 (NPC Beliefs surfaced) have the noted self-contradiction documented in original audit P7. Cleanup required. |

**(35) Per-Belief engagement count.** Articulation Layer §2.4 tracks how many scenes each Belief has been engaged in.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: high · S: high | The half-built Thought Cabinet substrate. |

**(36) Forgetting.** Cultural memory erosion (Southernmost / Einhir).

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: mid (scope-specific) · S: high | Specific narrative gear. Edeyja-relevant, RM-relevant. Earns place at scope. |

**(37) Stance positioning.** General stance reads (ally / neutral / opposed) toward issues.

| Verdict | NERS | Note |
|---|---|---|
| **AUDIT** | N: ? · E: ? | This may be subsumed by stance triangles (#30) and/or Disposition + Conviction. Verify. |

### §2.8 Specialized / sub-role

**(38) Shadow Renown [0–10].** Riskbreaker covert reputation.

| Verdict | NERS | Note |
|---|---|---|
| **AUDIT** | N: scope-limited · E: low (parallel system) · R: limited · S: low (parallel) | **Snob finding:** parallel reputation system for one sub-faction. If Riskbreaker gameplay is high-value (canonically yes — Torsvald arc, covert ops), keep. Otherwise fold into a "Covert Renown" extension of standard Renown. Pair with #39. |

**(39) Deniability Debt [0–7].** Riskbreaker covert-ops accumulated cost.

| Verdict | NERS | Note |
|---|---|---|
| **AUDIT** | Same as #38. | Same scope concern. Both or neither. |

**(40) Companion specification.** Companion-app NPC behavior layer.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: scope-specific · E: high · R: high · S: high | Companion-app subset of NPCs. Earned for companions. |

### §2.9 Proposed mechanics (last 4 turns)

**(41) Conviction voices.** Author per-Conviction characteristic-claim voice.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** (scoped to ~13 entries) | N: high (closes PC interiority gap) · E: high · R: high · S: high (with salience filter) | Single highest-leverage proposed addition. Author one line per Conviction. Engine surfaces 1–2 per scene, not all at once. |

**(42) Reaction-shape library.** Per-Conviction × per-event-archetype reactions.

| Verdict | NERS | Note |
|---|---|---|
| **SCOPE** (~25 entries, not 65) | N: high · E: mid · R: high · S: low if too large | Scope to ~5 event archetypes total (witnessed-violation / forced-against-ethos / kinship-claim / authority-clash / ontic-shock), not 5 per Conviction. |

**(43) Conviction invocations.** Darklands-saint-style power-move.

| Verdict | NERS | Note |
|---|---|---|
| **DEFER** | N: low · E: high (clean integration) · R: mid · S: mid | Cosmetic-but-pretty. Not load-bearing. Defer. |

**(44) History content-access.** Histories gate specific content (literacy, religious texts, court protocol, etc.).

| Verdict | NERS | Note |
|---|---|---|
| **KEEP+** (scoped to ~5 high-frequency unlocks per history) | N: high · E: high · R: high · S: high | The Darklands-derived exterior-gate move. Don't author 120 small unlocks; author 5 big ones (literacy, religious-text-access, court-protocol, military-command, Threadwork-formula-recognition) per history. ~5 × 57 histories = ~285 yes/no entries, but a single matrix. |

**(45) History acquisition during play.** Time-in-role + skill-cluster-threshold + catalyst event.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP+** (single tracker, not 3 systems) | N: high · E: low if 3 systems, high if unified · R: high · S: mid | Collapse to one acquisition tracker (engine notices conditions, offers History at threshold). |

**(46) Per-NPC speech register [Tier 1+2].** One-line voice descriptor per NPC.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: high · S: high | ~25 entries. Prose-writer input, not player surface. |

**(47) Tier-3 texture floor.** ≥1 Belief + ≥1 Goal + ≥1 Inspiration per Tier-3 NPC.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: high · S: high | ~14 NPCs × 3 fields. Closes the prose-feedstock deficit. |

**(48) Drift visualization.** UI showing Conviction-weight history and Self-Other history.

| Verdict | NERS | Note |
|---|---|---|
| **KEEP** | N: high · E: high · R: high · S: high | Legibility for an existing mechanic. Not a new mechanic. |

**(49) Languages grid [20 × R/S/W].**

| Verdict | NERS | Note |
|---|---|---|
| **CUT** | N: low · E: low · R: mid · S: low | Reduce to 4–5 binary languages, integrated into history content-access. No R/S/W tracking. |

**(50) Knowledge domains grid [15].**

| Verdict | NERS | Note |
|---|---|---|
| **CUT/FOLD** | N: low · E: low · R: mid · S: low | Reduce to ~5 major buckets; fold into history content-access. |

**(51) Competencies grid [25].**

| Verdict | NERS | Note |
|---|---|---|
| **CUT** | N: low (history-skills already do this) · E: low (parallel) · R: mid · S: low | Eliminate. History-derived skills are the granular layer; a parallel grid double-counts. |

**(52) Per-territory reputation grid.**

| Verdict | NERS | Note |
|---|---|---|
| **CUT** | N: mid · E: low (parallel to Standing) · R: mid · S: low | Extend Standing with optional per-territory modifier. Don't run two parallel reputation systems. |

**(53) Belief internalization (Thought Cabinet light).** From the DE-pivot turn — internalization stage at engagement-count threshold; bonus + lock.

| Verdict | NERS | Note |
|---|---|---|
| **AUDIT/RECONSIDER** | N: mid · E: high if used · R: mid · S: mid | Articulation Layer §2.4 already has engagement counts. The internalization stage adds a binding mechanic on top. Question: is the Belief revision mechanic (#9) already doing what internalization would do? **Snob finding:** yes — partially. Belief revision = forced change via Contest defeat. Internalization = chosen commitment via accumulated engagement. Different mechanics for different directions. *Earn place IF the system needs voluntary-commitment-with-binding;* otherwise the involuntary-revision path covers it. |

---

## §3 — Interaction audit

### §3.1 Smooth integrations (the system at its best)

These are the seams where the system genuinely works. Worth naming because they're the design's strongest claim:

- **Convictions ↔ Resonant Style ↔ Belief in Contests.** The argument-shape (Resonant Style) reaches the actor's Belief-or-Conviction; decisive defeat produces revision; revision produces Scar. *One mechanic feeding into the next, each at its appropriate scale.*
- **PP-686 v2 cascade math.** NPC `personal_convictions` → `effective_convictions` (cascade-blended) → faction `aggregate_effective_convictions` → matched against role template → Cascade Fidelity → modifies that NPC's Domain Action Ob. *Same vocabulary at both scales; clean derivation.*
- **TS Gate on Evidence Style.** TS-0 NPCs (theologically foreclosed) cannot be reached by Thread-level evidence, only by ontical evidence. *The metaphysical layer protects the personality layer in a way that is mechanically forced.*
- **Knot threshold → Solidarity Style activation.** Building a Close Knot makes Solidarity-style argument available. *The relational mechanic gates a personality mechanic.*
- **Self-Other drift + Conviction Scars + Belief revision = Macbeth arc.** Three distinct mechanics composing into emergent character development. *The system writes the arc.*
- **Lifepath → Skills → Sparking → cross-History hybrids.** The competence layer composes cleanly across stages.

These are real. They are why the system is worth defending.

### §3.2 Naming collisions and conflations

Five name conflations identified:

| Term | Use 1 | Use 2 | Recommendation |
|---|---|---|---|
| **Belief** | NPC first-person truth-statement (npc_behavior §3) | PC player-authored aspiration with engagement count (articulation_layer §2.4) | Rename PC version "Tenet" or "Aspiration" |
| **Inspiration** | PC aspirational arc (articulation_layer §2.4) | NPC author-shorthand (historical_parallel + in_character_aspiration) | Rename NPC version "Reference Figure" or split the two facets |
| **Spirit** | Attribute pool (#14, BW d10 pool) | Metaphysical attribute (#18, 1–7, Beckett/Lispector) | Rename metaphysical version "Will" or "Vital Spirit" |
| **Stance** | Stance triangle (#30, composite) | Stance positioning (#37, ally/neutral/opposed) | Verify if both exist; consolidate or rename |
| **Goal** | Implicit in Behavioral AI / arc map | Mission `primary_objective` (faction-side) | Author Goal as first-class field on NPCs |

Naming hygiene is a real audit finding.

### §3.3 Overlaps and duplications

| Mechanics | Overlap | Recommendation |
|---|---|---|
| Standing per faction (#24) ↔ Renown (#25) | Both reputation; Standing per-faction, Renown public-general | Test: is Renown derivable from Standings (max, sum)? If yes, eliminate as authored. |
| Stance triangles (#30) ↔ Resonant Style (#7) + Conviction (#4) + Goal (#3) | Triangle is composite of three independent fields | If engine queries triangle as composite, document; if not, retire |
| Decision Forks (#33) ↔ Conviction Track Scar effects (#8) | Forks "increase under Scars" but isn't separately tracked | Fold into Scar effects |
| Substrate-Posture (#20) — character or faction? | Filtered through leader's POV | Document categorization explicitly |
| Per-territory reputation (proposed #52) ↔ Standing (#24) | Two reputation systems | Cut #52; extend #24 |
| Languages grid (proposed #49) ↔ History content-access (proposed #44) | Languages are content-gates | Fold #49 into #44 |
| Knowledge domains (proposed #50) ↔ History content-access (proposed #44) | Knowledge is content | Fold #50 into #44 |
| Competencies grid (proposed #51) ↔ History-derived skills (#11) | Two granular skill grids | Cut #51 |

### §3.4 Friction points (real design issues)

1. **L+PS scope problem** (Jordan flag, faction §5.2 in faction_canon). Mandate-derived calculation doesn't capture territorial scope. Cross-cuts character mechanics because PC's faction-Mandate gates their action capacity.
2. **3-taxonomy supersession debt** (7 / 9 / 13 Convictions). Mostly cleaned but persistent in `npc_behavior §2` stance triangles and `conviction_track_v1`. Source-file propagation is a pending commit cycle.
3. **Tier-3 prose-feedstock deficit.** Acknowledged. Texture floor proposal closes it.
4. **Empty-body sections.** Vaynard Arc A/B; ~40% of foil pairings; ~5 character_analyses entries. Acknowledged in audit; surface-don't-fabricate is the policy.

---

## §4 — Coverage gap analysis (what isn't modeled)

These are not over-engineering proposals. These are genuine gaps where a load-bearing element of character-experience has no mechanical home.

### §4.1 PC interiority — the largest single gap

NPCs have rich interior: Convictions speak (after my proposed addition), Beliefs are quoted in voice, Resonant Style determines what reaches them, arc maps trace transformation, Behavioral AI flaws make them mechanically distinct.

PCs have: Lifepath history, starting Beliefs, Standing, attributes, skills, TS/Coherence/Spirit/Certainty.

**The PC's voiced inner life is structurally absent.** This is the gap the entire DE-pivot conversation has been trying to address. Conviction voices (#41) is the most important single move toward closing it.

### §4.2 Sensory anchors / physical signature

Edeyja has a Thread injury that "renders unusually" (gold standard). Most NPCs — even Tier 1 — have no comparable anchor. Almud, Vaynard, Baralta, Himlensendt: ethical and political detail, no physical detail.

This is not a mechanic to add; it's authoring on existing schema. Per-Tier-1 sensory anchor field (1–2 lines).

### §4.3 Class-coded speech

Currently offloaded to prose-writer's coherence-tier author-weighting. The synthesis renders all NPCs through the same eight-author lens. Per-NPC speech register (#46) closes Tier 1+2; Tier 3 remains generic.

### §4.4 Wants distinct from Beliefs and Goals

A character's *life want* — what they'd give everything to have — is implicit in Inspiration's `in_character_aspiration` facet but isn't a first-class field. Beliefs are what they assert as true; Goals are situational (this season, this scene); Wants are the deep current.

This may not need a separate mechanic; it may be that Inspiration + Belief together cover it. But the question is worth surfacing.

### §4.5 Fears

The inverse of Want. What the character would do anything to *avoid*. Distinct from Conviction (Conviction = what you value; Fear = what you flee). Currently unmodeled. **Snob finding:** classical drama runs on Want + Fear simultaneously. Valoria runs on Conviction + Belief, which captures different ground. May or may not earn a separate field; worth thinking about.

### §4.6 Habits and tics

DE's NPCs are recognizable by tics: Cuno's third-person speech, Klaasje's French phrases, Kim's notebook. These are partially encoded in the proposed speech register field (#46), but tics are non-linguistic too — gestures, gait, room-arrival patterns. Currently unmodeled.

### §4.7 Aging / lifespan

Darklands tracks character age; characters retire. Valoria has campaign seasons but characters don't age. For long campaigns this creates an immortal-cast problem.

**Snob finding:** probably not worth the overhead. Renaissance-political games typically span 5–15 years of in-game time, within a single generation. Skip unless campaign scale calls for it.

### §4.8 Trauma history (vs current Scars)

Conviction Track Scars are accumulated *during* play. NPCs canonically have backstory trauma (Edeyja's Thread injury, Ehrenwall's lost knights, Vaynard's complicit-in-erasure act) but this isn't represented as authored Scars. Recommend: NPCs can begin play with N authored Scars from backstory, modeled identically to play-acquired Scars.

This is small — adds nothing to the mechanic, just allows authoring use of an existing track.

---

## §5 — Per-decision load test

Three scenes modeled. Count = number of distinct mechanics consulted per *single* decision.

### §5.1 Scene A — Conversation with Hafenmark merchant

**Pre-cuts (system as I had been proposing it):** 17 consultations. Unplayable. (Last turn's analysis.)

**Post-cuts (this audit's recommendations):**

1. Conviction voice intrusion (1–2 surface, salience-filtered)
2. History gate (yes/no — do I have what I need)
3. Resonant Style of merchant (engine displays)
4. Belief engagement / Scar risk (binary indicator)
5. Pool to roll (one number)
6. Standing or Disposition modifier (one number)
7. Outcome

**Seven consultations.** At ceiling, but tractable. Each consultation maps to a decision the player actually has agency over.

### §5.2 Scene B — Combat round

Combat handled by `combat_design_v1`, largely independent of personality system. Per-round:

1. Action choice (attack / defend / move / use skill)
2. Pool composition (Body or Mind, plus weapon skill)
3. Tactical state (terrain, cover, ally position)
4. Resource cost (fatigue, momentum)

Four consultations. Combat is appropriately lighter on personality-mechanic surface.

### §5.3 Scene C — Domain Action (faction-scale)

1. Faction Mission alignment (PP-686 mission_alignment_modifier)
2. Cascade Fidelity (faction-side; engine-computed)
3. Public Expectation strictness (engine-computed)
4. Stat pool (Influence/Wealth/Military/etc.)
5. Standing of acting character + faction
6. Target faction's defensive stat (Ob source)
7. Outcome

Seven consultations. Strategic-layer ceiling. Tractable.

**Verdict:** with the cuts in §2.9, the system stays under a 7-consultation per-decision ceiling. Without the cuts, it spilled to 17.

---

## §6 — Cumulative verdict

### §6.1 Load-bearing — keep, no cuts

(2) Beliefs · (4) Convictions · (5) Cultural Templates · (6) Self-Other · (7) Resonant Style · (8) Conviction Track · (9) Belief revision · (10) Lifepath · (11) Skills · (12) Sparking · (14) Attribute pools · (16) TS · (17) Coherence · (18) Spirit (metaphysical) · (19) Certainty · (21) Knots · (22) Disposition · (23) Foils · (24) Standing · (26) Caste · (27) Tier system · (28) Behavioral AI flaw · (29) Priority Trees · (31) Arc state machine · (32) Per-NPC arc maps · (34) Articulation Layer · (35) Engagement count · (36) Forgetting · (40) Companion spec.

29 mechanics, all earn their place.

### §6.2 Keep with propagation/cleanup needed

(1) Inspirations [naming collision] · (8) Conviction Track [taxonomy debt] · (18) Spirit [naming collision] · (20) Substrate-Posture [authored gaps + categorization] · (32) Per-NPC arc maps [empty bodies] · (34) Articulation Layer [§2.4 vs §3.1 conflict].

### §6.3 Audit-flag — needs Jordan input

- (3) Goals — author as first-class field, or fold into Inspiration?
- (13) Recall — fold into Mind/Spirit pool?
- (15) Sub-pools — relationship to main pools? Independent?
- (25) Renown — derivable from Standings?
- (26) Caste — mechanical-floor used in play, or narrative texture?
- (30) Stance triangles — vestigial composite?
- (33) Decision Forks — separately tracked or documentary?
- (37) Stance positioning — distinct from #30?
- (38) Shadow Renown + (39) Deniability Debt — keep both for Riskbreakers, or fold?

Nine items.

### §6.4 Keep, propose scope reduction

(41) Conviction voices [13 entries] · (42) Reaction-shape library [~25 entries, not 65] · (44) History content-access [~5 high-frequency per history] · (45) History acquisition [single tracker, not 3 systems] · (46) Per-NPC speech register [Tier 1+2] · (47) Tier-3 texture floor · (48) Drift visualization.

Seven proposed additions, all scope-reduced.

### §6.5 Defer or cut

**Defer:** (43) Conviction invocations — neat, not load-bearing. (53) Belief internalization — needs Belief revision (#9) audit first.

**Cut:** (49) Languages grid · (50) Knowledge domains grid · (51) Competencies grid · (52) Per-territory reputation grid.

### §6.6 Coverage gaps to fill (authoring, not new mechanics)

- PC interiority (closed by Conviction voices #41)
- Sensory anchors per Tier 1 NPC (~10 NPCs × 1–2 lines)
- Per-NPC speech register Tier 1+2 (~25 NPCs × 1 line)
- Tier-3 texture floor (~14 NPCs × 3 fields)
- (Optional) Authored backstory Scars per Tier 1 NPC

Four authoring tasks. ~50 author-decisions total.

---

## §7 — Open audit flags for Jordan (numbered for response)

**F1 — Recall.** Is Recall actually used outside sparking? If only sparking, recommend folding into Mind or Spirit pool for the gateway check (e.g., Spirit alone, or Spirit + Mind/2). **Decision:** keep / fold / eliminate?

**F2 — Sub-pools (Cognition / Focus / Endurance / Charisma / Bonds).** Are these independent attribute tracks, or derived from Mind/Body/Spirit? If independent: 8 tracks per character is starting to crunch. If derived: document the derivation. **Decision:** clarify relationship?

**F3 — Renown vs Standing.** Are these mechanically distinct in current canon? If Renown is derivable (e.g., max-Standing or sum-of-positive-Standings), eliminate as authored. **Decision:** keep / derive / eliminate?

**F4 — Caste-as-floor.** Is Caste actually setting Standing ladder ceilings/floors in current play, or is it narrative texture only? **Decision:** load-bearing / narrative-only?

**F5 — Stance triangles.** Are these queried by the engine as a composite object, or are the three components (Conviction, Resonant Style, Goal) queried independently? If independent, retire the triangle as a composite. **Decision:** active / vestigial?

**F6 — Decision Forks.** Tracked engine quantity, or documentary phrase in the Scar accumulation table? **Decision:** track separately / fold into Scar effects?

**F7 — Shadow Renown + Deniability Debt.** Do Riskbreakers earn parallel reputation systems (current canon), or fold into Renown/Standing extensions? **Decision:** keep parallel / fold?

**F8 — Belief naming.** The PC Belief (articulation_layer §2.4) and NPC Belief (npc_behavior §3) are different mechanics under the same name. **Decision:** rename one (e.g., PC → "Tenet"), or accept the conflation as semantic kinship?

**F9 — Spirit naming.** Spirit-the-pool (#14) and Spirit-the-metaphysical-attribute (#18) are different things with the same name. **Decision:** rename one (e.g., metaphysical → "Will" or "Vital Spirit")?

**F10 — Inspiration naming.** PC Inspiration (aspirational arc) and NPC Inspiration (designer shorthand + in-character aspiration) are different mechanics. **Decision:** rename / split / accept?

**F11 — 13 Convictions.** Defended structurally per PP-684 §2 with Renaissance grounding. But experientially — does the player meaningfully engage with 3–4 of their character's Convictions in a campaign? If so, the other 9–10 are landscape. **Decision:** sim test / accept / reduce?

**F12 — Anti-Convictions.** Currently positive-valence only. Active opposition to a Conviction (e.g., active anti-Faith) is implicit (low Faith weight). Is this a gap, or are anti-Convictions modeled via Beliefs? **Decision:** explicit anti-Convictions / status quo?

**F13 — Self-Other relational pluralism.** Single scalar toward-self vs toward-collective. Doesn't admit "toward this specific person." Is this a gap, or is it modeled via Knot? **Decision:** add relational targets / status quo?

**F14 — Belief revision conjunction.** Three conjunctive conditions for revision. Calibration: intended high-stability or accidentally too-restrictive? **Decision:** sim test?

**F15 — Want and Fear as first-class fields.** Implicit in current schema. Earn place as separate fields, or covered by Inspiration + Conviction? **Decision:** add / status quo?

---

## §8 — What this means for the consolidation framework

The character_canon framework I built (PART A, §§1–11) needs three changes:

1. **Schema additions** (§2): add `Histories`, `Content Access`, `Speech Register`, `Sensory Anchor`, `Goal` as explicit fields. Resolves naming collisions and folds proposed mechanics in cleanly.
2. **Decision log additions** (§11): D9–D14 covering the audit findings — naming-collision policy, vestigial-mechanic policy (e.g., Stance triangle retirement if confirmed), and the F1–F15 question handling.
3. **Coverage-gap acknowledgment** (§10 Voice Anchors): explicit that PC interiority is closed by Conviction voices, that sensory anchors are an authoring task, that Tier 3 texture floor is foundational not optional.

The faction_canon framework needs one change:

1. **Substrate-Posture clarification** (§5 or §10): explicit that Substrate-Posture is filtered through leader POV but is a faction-level mechanic. Reduce categorization ambiguity.

Neither file needs structural revision. The audit changes priorities and decisions, not architecture.

---

## §9 — Synthesis

The character system is, in net, **stronger than I had been treating it.** Most of the foundational mechanics (Beliefs, Convictions, Self-Other, Resonant Style, Lifepath, Knots, TS/Coherence/Spirit/Certainty) are well-designed and earn their place under the harshest audit. The system has *real elegance* in the cascade math and in how the personality, metaphysical, and relational layers compose into emergent character development.

The system is **also more cluttered than it needs to be.** Naming collisions (Belief, Spirit, Inspiration, Stance, Goal), parallel reputation systems (Standing/Renown), and possibly-vestigial composites (Stance triangles, Decision Forks) accumulate without being audited. My recent proposals would have piled four more layers on top.

The path forward is **clean what exists before adding.** The cuts in §6.5 free authoring budget for the gaps in §6.6. The naming hygiene in §3.2 reduces friction without changing mechanics. The F1–F15 questions, once answered, retire vestigial overhead.

The single most important addition remains **Conviction voices.** It closes the PC interiority gap. It is small (13 entries). It composes cleanly with everything else. It is what changes what playing Valoria *feels like.*

Everything else — including most of what I proposed across the last four turns — is supporting work to that single move.

---

**End of audit. Awaiting Jordan response on F1–F15.**
