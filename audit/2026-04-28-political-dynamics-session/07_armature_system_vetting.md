<!-- [PROVISIONAL: 2026-04-28 session — d964fd13158349fa] -->
<!-- STATUS: PROVISIONAL — design exploration, not canonical mechanic -->
<!-- TITLE: Armature System: Comprehensive Vetting -->
<!-- POSITION IN ARC: see designs/audit/2026-04-28-political-dynamics-session/00_session_index.md -->
<!-- VETTING: see 07_armature_system_vetting.md for canonical framework assessment -->

# Comprehensive Audit: Armature-Based NPC Autonomous Actor System

Applied per `references/throughlines_meta.md` canonical vetting protocol. Class A (new subsystem). Full vetting required: N → Ω → Μ → М → Τ → Q.

System scope: NPC inner-state architecture (Identity, State, Concerns, Projects, Opinions, Memories, Knowledge), five engine procedures, weighted-armature interpretive mechanism replacing template library, integration with existing Valoria systems.

---

## §1 N — NECESSITY

**Renaissance-era political-leadership dynamic modeled:** Courts in which advisors interpret the prince's actions through their own ideological frames, generate independent conclusions (often wrong), pursue personal projects beyond the prince's direction, form opinions of each other, and act on those opinions in ways that constrain the prince's effective political capacity.

**Subject-matter grounding (load-bearing in source material):**

- **Italian city-states (Medici, Sforza, Visconti):** Court factions interpreted ducal decisions through their own positional interests; the same act was read as wisdom or error depending on the courtier's frame. Machiavelli's *Discorsi* explicitly treats this as the central problem of governance.
- **Tudor Privy Council:** Cecil, Walsingham, Leicester, and others held distinct interpretive frames (pragmatic statecraft vs. Protestant militancy vs. dynastic-marriage-strategy). They formed conclusions about Elizabeth's intentions that diverged from her actual reasoning; their actions on those conclusions shaped policy outcomes.
- **Papal curia:** Cardinals interpreted theological-political events through Conviction frames so divergent that the same papal action could be read as sanctity or corruption. The Schism of 1378 emerged from divergent conclusions about Urban VI from cardinals operating under the same observed events.
- **Ottoman court:** Viziers, Valide Sultans, and devshirme administrators operated through different interpretive frames; the same sultan's action triggered different reactions across factions, and those reactions shaped subsequent court politics.

**Existing-mechanic coverage check:** The current Valoria system has Conviction taxonomy, Beliefs, Conviction Scars, Resonant Style, and arc states. These provide *static* interpretive frames — the NPC's Conviction tells you their values. They do not provide *dynamic frame-driven interpretation* — the mechanism by which a Conviction-aligned NPC produces specific conclusions about specific events.

**What is lost without this system:** The throughline T-27 (Effects Real, Explanation Wrong) is canonically present but mechanically underspecified. Without armature, the engine cannot produce institutionally-coherent-but-wrong explanations consistently — it can only flag NPCs as "Faith-aligned" and have authored content reflect that. T-27 reduces to authored events rather than emergent dynamics.

**N failure mode check:**
- *Fantasy imposition:* No. Directly grounded in repeatable historical pattern across multiple Renaissance-era court systems.
- *Duplicate coverage:* No. Current Conviction system provides static frames; armature provides the dynamic interpretation step that makes those frames behaviorally consequential.
- *Edge case mechanic:* No. Court interpretation dynamics are central to the genre, not peripheral.
- *Abstractable:* Partial — could be abstracted further via more sophisticated AI priority trees, but that abstraction would be more rule-heavy than the armature, not lighter. The armature *is* the abstraction.

**Verdict: N PASSES.** Subject-grounded, load-bearing, gap in existing coverage.

---

## §2 Ω — INTENT

Four-clause assessment:

| Clause | Assessment |
|---|---|
| **Ω-a** Strategic actions produce cross-scale traceable-but-unanticipatable consequences | **Strong.** Player promotion → displaced NPC's Concern generation → Project shift → off-screen coalition formation → Domain Action obstruction → settlement governance friction. Player can trace; cannot fully anticipate due to Conviction-shaped interpretation producing unexpected conclusions. |
| **Ω-b** Personal-layer confrontation transforms character through substrate | **Adjacent.** System produces personal-scale political moments (Outreach scenes, social Contests, Knot interactions) that engage existing substrate-transformation mechanics (Coherence, TS, Certainty). Doesn't directly produce substrate transformation — that's the Threadwork system's job. Correct division of labor. |
| **Ω-c** Autonomous agents generate consequential events independent of player | **Defining characteristic.** Procedures A–E run regardless of player presence; NPCs autonomously generate Concerns, advance Projects, drift Opinions, share Knowledge, form Coalitions. This is the system's core claim. |
| **Ω-d** No strategy produces dominance — every action pays what it buys | **Strong.** Relationship investment costs scene actions; political choices empower some NPCs and alienate others; Factional Exposure scales with cross-faction depth; Standing advancement creates obligations. Tradeoffs are structural, not optional. |

**Verdict: Ω PASSES.** Three strong, one adjacent (correct boundary).

---

## §3 Μ — MODES

| Mode | Service | Notes |
|---|---|---|
| **Μ-α** Pressure as engagement driver | **Primary** | NPCs continuously generate Outreach scenes, Concerns, Demands; political environment never resolves to equilibrium; player cannot rest from engagement |
| **Μ-β** Autonomous agent composition | **Primary (defining)** | Off-screen interactions produce events no agent predicts; coalition formation, Knowledge propagation, Opinion drift all run independent of player |
| **Μ-γ** Substrate ontology | **Adjacent** | Armature interprets substrate events through Conviction frames, but system itself is interpersonal/political, not substrate-grounded. Supports Μ-γ via integration with existing substrate systems |
| **Μ-δ** Cross-scale consequence | **Primary** | Settlement Signal (Passive→Active), Knowledge propagation (personal→faction), Outreach generation (faction→personal). Multiple cross-scale paths |

**Primary Μ served:** Μ-β, Μ-α, Μ-δ. Μ-γ supported via integration.

**No Μ undermined.**

---

## §4 М — META-THROUGHLINES

Working through all 11:

| М | Pattern | Rating | Notes |
|---|---|---|---|
| М-1 | Pressure is continuous | **+ extends** | New pressure source: NPC autonomous Outreach generation; Concerns persist across seasons; courts don't quiet between events |
| М-2 | Geography holds pressure | ○ | System is interpersonal, not geographic |
| М-3 | Substrate grounds all | ✓ | Armature interprets substrate events through Conviction; consistent with pattern, not extending |
| М-4 | Institutions stake substrate-postures | ✓ | Faction substrate-postures become behaviorally visible — Faith-aligned armature consistently produces Faith-conviction interpretations even when wrong |
| М-5 | Scales connect through substrate | **+ extends** | Three new scale-bridges: Settlement Signal aggregation, Knowledge propagation, Outreach generation cascade |
| М-6 | Choice is forced | ✓ | Outreach displacement costs, Project vs. institutional duty conflicts, Concern-driven scene attendance |
| М-7 | Borrowings as composite assembly | ✓ | Armature itself is composite: Conviction × Personality × Project × Scar modulation |
| М-8 | Access is vertical-position gated | **+ extends** | New gate type: interpretive-frame access. Same Knowledge fact interpreted differently by different Conviction frames; player must access via the holder's frame |
| М-9 | Ontological inversion | ○ | Pattern concerns Thread phenomena; armature does not engage |
| М-10 | Environment as constitutive medium | ○ | Geographic pattern; not applicable |
| М-11 | Voluntary/involuntary capacity duality | ✓ | NPC voluntary action (Projects, decisions) coexists with involuntary state (Mood, Concerns generated without consent, Opinion drift under accumulated evidence) |

**Summary:** 3 extends, 5 satisfies, 3 not-applicable, **0 violations**.

The М-5 extension is structurally significant. The system creates new scale-bridging mechanisms that didn't exist in the previous architecture. The М-8 extension adds interpretive-frame as a gating dimension alongside the existing position-based gating — this is a refinement of how access works in Valoria.

---

## §5 Τ — THROUGHLINES

Walking through directly affected throughlines:

| T | Effect | Justification |
|---|---|---|
| T-12 Practitioner Arc | Preserves | NPC armature interprets Thread events; doesn't alter practitioner experience |
| T-13 Certainty Journey | Preserves | NPC Certainty modulates armature interpretation but Certainty mechanic unchanged |
| T-14 Conviction Architecture | **Extends** | Armature mechanizes how Conviction structures interpretation — was implicit in existing Scar system, now explicit |
| T-15 Player Progression | Preserves + slight extension | Standing advancement produces NPC-side reactions (Memories, Opinion shifts); ladder mechanic unchanged |
| T-16 Knot Propagation | Preserves | Knot extensions (Patch 2.2: guaranteed Observable behavior, automatic Concern surfacing) preserve substrate mechanic |
| T-22 Belief Lattice | Preserves | NPC Beliefs continue to gate cooperation; armature determines formation/revision but lattice unchanged |
| T-23 NPC Arc Emergence | **Extends** | Armature provides internal mechanism for arc emergence — Concerns generate, resolve, accumulate; Scar count modifies armature; arcs emerge from armature transformation |
| T-25 Generational Arc | **Extends** | Succession dynamics operate through armature: NPC Projects shift toward succession positioning; Opinions of potential successors form and drift |
| T-27 Effects Real, Explanation Wrong | **Extends powerfully** | The Concern resolution mechanism (Conviction-weighted seeking + Memory matching) is the engine of this throughline. Previously underspecified; now mechanized |
| T-30 Information Asymmetry | **Extends** | Knowledge structure + interpretive-frame access (М-8 extension) produces deeper asymmetry. Same Knowledge interpreted differently by different Convictions |

**Τ verdict: 0 breaks, 5 extensions (T-14, T-23, T-25, T-27, T-30), 5 preservations.** The system extends precisely the throughlines that needed mechanical specification — particularly T-27, which is canonically present but currently underspecified.

No supersession needed (no breaks). Add М-tag annotations to T-23, T-25, T-27 noting the armature mechanism per infill §3.1 update.

---

## §6 Q — QUALITY

### Q-robust

- **Three viable approaches per situation:** ✓
  - Cross-faction NPC contact: relationship-build / Insinuate operations / intermediary-mediated
  - Settlement governance: personal-invest / companion-delegation / formal-authority-only
  - Faction politics: direct-alliance / coalition-building / manipulation
- **Visible, traceable world-state change:** ✓ with caveat. Read actions reveal Mood + Observable behavior; Outreach reveals Concerns through dialogue; Gossip propagates relationship changes. Caveat: Opinion drift is invisible without Read action investment. Documented as intentional opacity per Iteration 2 Patch 2.6.
- **Player-independent firing:** ✓. Procedures A–E run regardless of player.
- **Dramatic legibility test:** ✓. Active NPCs have explicit Projects (what they want), explicit Mood + Concerns (current state), and propagation of consequences if no one intervenes. A designer can read game-state and answer the three legibility questions in one sentence each.

### Q-smooth

- **Methodology matches governing subsystem:** ✓. Armature uses Conviction (existing), Personality (new but minimal — 4 dimensions), Memory (extension of Belief/Scar system).
- **Scale-transition behavior specified:** ✓. Settlement Signal handles Passive→Active; Outreach generation handles Active→player; Knowledge propagation handles intra-tier.
- **Temporal behavior specified:** ✓ with note. Procedure ordering A→C→B→D→E at Accounting; Immediate Update for large events; Mood durations specified. Note: Mood updates batch at scene-resolution end (does not shift mid-scene); acceptable but flag for documentation.
- **Friction points:**
  1. Settlement Signal creates new data-flow path (Passive→Active scale) requiring new plumbing in the engine. Not contradiction with existing systems but new infrastructure.
  2. Off-screen interaction rate (60% ambient) does not currently scale with faction state. **Recommendation:** ambient rate halves when controlling faction is at Stability ≤ 2 (NPCs are too occupied with crisis for routine social contact). This is a smoothness fix.
  3. Immediate Update mechanism is a special case for large events. Per failure lexicon: special-cased risks Q-smooth violation. **Mitigation:** Implement standard ordering first; add Immediate Update only after base system passes simulation. Flagged as implementation-risk, not design-fail.

### Q-elegant

- **Core rule restatable after one reading:** ✓. "NPC Conviction + Personality form a weighted armature that interprets events into Concerns; Concerns drive behavior; Concerns resolve based on Memory; NPCs autonomously interact and form Opinions."
- **Second-order consequences predictable:** ✓ for the framework, contingent for specific outcomes. A Faith-aligned NPC encountering Reason-justified treaty produces Faith-frame Concerns predictably; specific resolution depends on Memory content (designed unpredictability).
- **Dependencies enumerated:** ✓. Existing Conviction, Belief, Scar, Disposition, Knot integrated; new Mood, Personality, Memory, Knowledge, Settlement Signal, Gossip introduced and explicitly listed.
- **"Except when X" cases flagged:** ✓. Immediate Update is the one special case; flagged in Iteration 3 final critique.

**Q verdict: PASS** with three smoothness recommendations (faction-state ambient scaling, Settlement Signal infrastructure note, Immediate Update implementation order).

---

## §7 Subjective Quality Assessment

### Necessity (project definition)

**The system models a specific Renaissance-era dynamic that existing Valoria mechanics gesture toward but do not produce.** The current NPC system specifies that NPCs have Convictions and form Beliefs, but does not specify how those Convictions transform observed events into specific conclusions. The armature provides that transformation. Without it, T-27 (Effects Real, Explanation Wrong) cannot fire as a system property — only as authored content. The system earns its existence.

### Smoothness (project definition)

**Integrates without modifying any existing system.** The armature reads from existing Conviction, Belief, Scar, Disposition, Knot, Standing structures and adds new derived structures (Concerns, Projects, Opinions, Memories, Mood, Knowledge). Existing mechanics fire identically; new mechanics extend behavior.

Friction points (three identified above): (1) new data-flow infrastructure for Settlement Signal, (2) ambient interaction rate doesn't scale with faction crisis state, (3) Immediate Update is a special case. (1) is unavoidable for the system's function; (2) is fixable with a one-line modifier; (3) is mitigated by deferring implementation.

Scale transitions are specified (personal ↔ settlement ↔ faction). Temporal behavior is specified (Accounting sequence). Calculation methodology is consistent (Conviction-weighted selection + Memory filter mirrors the existing pool/Ob/degree pattern's structure: derive parameters → consult evidence → produce outcome).

### Robustness (project definition)

**Strategic depth:** Player decisions about whom to invest in, when to engage, which NPC's Project to support, how to manage Factional Exposure, all produce different political outcomes. Multiple viable strategies — high-Bonds relationship-builder, low-Bonds independent operator, faction loyalist, cross-faction broker, intelligence specialist.

**Customization:** Per-NPC armature derives from their specific Conviction × Personality × current Projects + Scars. ~35 Active NPCs each with distinct armature configurations. Player customization is *via the existing systems* (Bonds, Cha, Spirit, History, Standing) — the player builds a character whose social tools work better or worse with different NPC types.

**Variety:** Same event produces different reactions across NPCs (per Probe 3.1: Klapp's Project completion in two playthroughs produces categorically different political dynamics based on player relationship history). Different player choices produce different NPC Memories which produce different future Opinion drifts.

**Player importance:** Player actions generate Memories in observing NPCs; Memories shape Opinions; Opinions drive subsequent NPC behavior toward the player. The player is consequential at every scale.

**Emergent narratives:** Per Iteration 1 Test 7 (multiple stressors simultaneously) and Iteration 3 Probe 3.1 (different play histories produce different outcomes), the system produces genuinely emergent political situations not pre-scripted by any single proposal.

### Elegance (project definition)

**Logically simple core:** The armature concept replaces 630-template-library with weighted dimensions derived automatically from existing NPC characteristics. The reduction from authored-tables to characteristic-derived-weights is the elegance pivot.

**Clear approach:** A designer working on the system can predict an NPC's behavior trajectory from Conviction + Personality + active Projects. The system is intuitable.

**No unnecessary overhead:** State per NPC is necessary for behaviors. Concerns/Projects/Opinions/Memories/Mood are each load-bearing — none can be removed without losing mechanical capability.

**Player-intuitive complex outcomes from simple choices:** The player's social action (Read, Connect, Negotiate, Insinuate) consults a coherent set of inputs (Disposition, Bonds, Mood, NPC Personality if visible) and produces an outcome the player can reason about. The system surfaces complexity without exposing the engine state.

---

## §8 Throughline-Level Synthesis

The armature system is, at its core, the **mechanization of T-27 (Effects Real, Explanation Wrong)** — making explicit the engine by which institutionally-coherent-but-wrong explanations form across the political environment.

T-27 was previously implementation-deferred ("Conviction Scar targeting tied to specific effect/explanation mismatches" — pending). The armature delivers the targeting mechanism. Each NPC's Conviction-derived seeking-tag set is exactly the "Conviction Scar targeting" the throughline required.

This means: the system is not just adding a feature; it is **completing a structurally committed throughline**. The vetting framework's Τ assessment treats this as preservation/extension; the deeper assessment is that T-27 was previously unfinished and the armature finishes it.

Similarly:
- T-23 (NPC Arc Emergence) was specified as a state machine but the *internal mechanism* that drives transitions was implicit in Scar accumulation. The armature provides Concern→Memory→Belief Revision→Scar as an explicit chain.
- T-25 (Generational Arc) was specified at the demographic level (aging, succession) but the *court-political* dimension of succession (anticipatory positioning, faction internal repositioning, succession-anxiety effects on NPC behavior) was implicit. The armature operationalizes succession positioning as Project shifts and Opinion drift toward potential successors.

The system is therefore not a new throughline but a **structural completion** of three existing throughlines (T-14, T-23, T-25, T-27) that were previously load-bearing but mechanically incomplete.

---

## §9 Meta-Throughline-Level Synthesis

The М-5 extension (scales connect through substrate) is the architectural significance. The armature system creates three new scale-bridging mechanisms:

1. **Settlement Signal** (Passive→Active scale): aggregates lite-NPC Memories into faction-NPC Concerns
2. **Knowledge propagation** (intra-tier with cross-scale endpoints): individual-held facts move through the NPC network and surface to player or faction at appropriate Disposition gates
3. **Outreach generation cascade** (Active→player scale): NPC Concerns and Projects generate Scene Slate entries that pull the player into faction-level dynamics through personal-scale interactions

These three bridges — combined with existing scale-bridges (Domain Echo, Standing ladder, faction emergence) — produce a Valoria where information, pressure, and consequence move freely across personal/settlement/faction scales. М-5 was always the throughline that made Valoria's scale architecture distinctive; the armature deepens it.

The М-8 extension (interpretive-frame access gating) is more subtle but possibly more important. Existing Valoria gates information by position (Disposition, Standing, TS, Coherence, Certainty). The armature adds interpretive frame as a gate: even when the player has access to a Knowledge fact, they must understand the *holder's interpretive frame* to use it well. A Faith-aligned NPC tells the player about a Thread event; the player must recognize that the NPC's account is Faith-framed before treating it as evidence about the event. This is a Renaissance-realistic information dynamic (every account is framed; evaluating the frame is part of evaluating the information) and it's underspecified in current Valoria.

---

## §10 Vetting Block

Per §8.5 of the vetting framework:

```yaml
vetting:
  class: A
  necessity: pass
  omega: pass
  mu: [Μ-β, Μ-α, Μ-δ]
  m_ratings:
    M-1: "+"
    M-2: "○"
    M-3: "✓"
    M-4: "✓"
    M-5: "+"
    M-6: "✓"
    M-7: "✓"
    M-8: "+"
    M-9: "○"
    M-10: "○"
    M-11: "✓"
  q: pass
  q_notes:
    - "Faction-state ambient interaction scaling recommended (smoothness)"
    - "Settlement Signal infrastructure is new plumbing (acceptable)"
    - "Immediate Update implementation deferred until base system stable (smoothness)"
```

---

## §11 Outstanding Items

Items requiring Jordan decision before implementation:

1. **Personality dimension calibration:** four dimensions (risk_tolerance, social_warmth, intellectual_rigor, institutional_deference) need value assignments per Active NPC. ~140 values across 35 NPCs.
2. **Conviction → armature weight mappings:** 7 Conviction × 4 dimensions × ~5 options = ~140 weight assignments. One-time, shared by all NPCs of that Conviction.
3. **Event dimension profiles:** ~30 significant event types × ~3 active dimensions × ~3 options = ~270 entries. One-time, shared.
4. **Sentence frame templates:** ~20 frames covering Agency × Mechanism × Intent combinations.
5. **Wrong Belief Investigation interaction (Iteration 1 Patch G critique):** design decision required — Option A (forgiving: Investigations from wrong Beliefs pause pending player evidence submission) or Option B (harsh: Wrong Beliefs fire consequences at normal speed). Recommendation: Option B per Ω-d (no strategy produces dominance — wrong-Belief consequences are part of the political environment the player must manage).

Items deferred until simulation:

1. Computational budget profiling
2. Concern template within-Conviction variation (Alpha/Beta/Gamma) calibration via simulation runs
3. Ambient interaction rate validation (60% with dampening produces realistic court textures? — verify via simulation)
4. Knowledge propagation latency (one-degree per season — produces realistic information networks? — verify via simulation)

---

## §12 Verdict

**The armature-based NPC autonomous actor system passes full vetting (N → Ω → Μ → М → Τ → Q) with no failures, three meta-throughline extensions, five throughline extensions, and three minor smoothness recommendations.**

The system completes structural commitments in three throughlines (T-14, T-23, T-25) and makes T-27 mechanically functional for the first time. It extends М-5 with three new scale-bridging mechanisms and М-8 with interpretive-frame gating.

It is ready for content authorship (the ~370-entry weight/dimension/frame library) and simulation design. Implementation should begin with the base system; Immediate Update and Settlement Signal aggregation should be added in subsequent passes after base behavior is verified.

Per project definitions: the system is **necessary** (subject-grounded, completes underspecified throughlines), **smooth** (integrates without modifying existing systems, scale transitions specified, methodology consistent), **robust** (multiple strategies, customization via existing systems, emergent narratives demonstrated), and **elegant** (characteristic-derived rather than table-derived, restatable in one sentence, dependencies enumerated).
