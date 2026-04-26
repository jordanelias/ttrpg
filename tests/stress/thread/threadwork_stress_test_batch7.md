# THREADWORK STRESS TEST — BATCH 7
## Session: d8b924fb834a398c | Date: 2026-04-16 | Effort: MAX
## No repeats from Batches 1–6.

---

# 1. TS HARD CAP 100 — OVERWHELMING LEAP BONUS BECOMES DEAD

## 1.1 What Happens to +1 TS at Maximum TS? [ELEGANT — GAP]

Params_threadwork: "Thread Sensitivity (TS): 0–100 (hard cap)." Overwhelming Leap: "Practitioner gains 1 Thread Sensitivity." At TS 100, this bonus has nowhere to go.

**No fallback is defined.** The bonus is not converted, transferred, or replaced. It simply disappears. Every Overwhelming Leap at TS 100 awards a bonus that the practitioner cannot receive — which means every Leap at maximum TS rewards Overwhelming less than Success (Success preserves contact normally; Overwhelming also preserves contact normally AND wastes the TS gain). This inverts the normal value hierarchy of degrees at cap.

**[ELEGANT — GAP]** Required: a TS-cap Overwhelming conversion rule. Proposed: "At TS 100, Overwhelming Leap instead grants: next Thread operation's Ob reduced by 2 (not 1 as the standard Overwhelming Ob reduction benefit). The perceptual depth that cannot grow outward turns inward — greater precision, not greater range." This gives TS 100 Overwhelming a functional benefit while acknowledging the cap.

---

# 2. THREAD-READ DURING MASS BATTLE — CONTRADICTORY SYSTEM PLACEMENT

## 2.1 Thread-Read Is Simultaneously Suspended and Permitted [SMOOTH — FAILS]

Fieldwork_v30 (from fetched text): "Mass battle suspends fieldwork. Evidence Tracks freeze. Thread-Read during mass battle: resolves in Phase 4 window, classified as intelligence (not offensive). Co-movement fires. May advance an Evidence Track if the Thread-Read targets an investigation question."

This is self-contradicting: Evidence Tracks are **frozen** during mass battle, but Thread-Read **may advance** an Evidence Track during mass battle. The same sentence establishes both.

**[SMOOTH — FAILS — INTERNAL CONTRADICTION]** Required ruling: "Thread-Read during mass battle is a Thread operation (Phase 4), not a fieldwork action. Its Evidence Track contributions apply at Accounting (end of season), not immediately — consistent with the mass battle fieldwork freeze. Evidence Track state at battle start is preserved; Thread-Read evidence is banked and applied at battle end." This resolves the contradiction while preserving both the Thread operation timing and the fieldwork suspension.

---

# 3. POOL FLOOR CONFLICT: 1D (PARAMS_CORE) VS 5D (R-57 THREAD)

## 3.1 Two Canonical Pool Floors, Same System [CONFLICT — CRITICAL]

params_core.md: "No penalty may reduce a pool below 1D. Ob penalties still apply at 1D."

R-57 (threadwork_v30): "Minimum 5 dice before rolling any Pull. Below 5D (from wounds, degradation, low stats): Apply to §2.4 Pulling, eligibility section."

R-57 establishes a 5D floor specifically for Pull operations — five times the params_core 1D floor. These are both canonical. A heavily wounded practitioner (3 Wounds = −3D) with Spirit 3, TPS 3, History +3D = 12D base − 3D = 9D: above 5D, no conflict. A practitioner with Spirit 1, TPS 1, History +3D = 6D − 3D (wounds) = 3D: below 5D threshold. Params_core says: 3D is fine (above 1D). R-57 says: Pull is not eligible at 3D.

**Which floor applies where?**
- Params_core 1D floor: applies to all rolls universally.
- R-57 5D floor: applies specifically to Pull operations.
- Combined reading: all rolls can go as low as 1D except Pull, which requires 5D minimum.

**[CONFLICT — CRITICAL]** Does the 5D floor apply to ALL Thread operations or only Pull? R-57 references "rolling any Pull" — it is Pull-specific. A practitioner at 3D can still attempt a Weave, Mend, or Leap (params_core 1D floor applies). They cannot attempt a Pull (R-57 5D floor applies). This is logically consistent but creates an asymmetry: Pull is the only operation with a hard eligibility threshold above 1D.

**Required:** Explicit statement of scope: "R-57's 5D minimum applies to Pull operations only. All other Thread operations use the params_core 1D floor. This is intentional — Pulling (opening configurations) requires sufficient intentional depth; below 5D, the practitioner's perceptual engagement is insufficient to meaningfully open a thread configuration."

---

# 4. COMMUNITY WEAVING × 4 IN FOCUS 5 WINDOW — OA STACKING

## 4.1 Four Sequential Community Weavings of the Same Community [EXPLOIT — INTERNAL]

Community Weaving: "One Community Weave per contact window round; replaces another op that round." Focus 5 = 4 operation rounds. A practitioner performs Community Weaving every round:
- Round 2: Community Weave Ob 3 (base Relational). Success → RS +1.
- Round 3: Same community configuration → OA active (+1 Ob) = Ob 4. Success → RS +1.
- Round 4: OA persists (same contact window) + Overweave (+1 Ob cumulative for ops 2+) = Ob 5. Success → RS +1.
- Round 5: OA + Overweave cumulative = Ob 6. Success → RS +1.

Total RS from four successful Community Weavings: +4. Coherence: −1 (Relational, only at ≥Relational scale, so each Weave costs −1) × 4 = Coherence −4. From Coherence 10: ends at Coherence 6 (Dissonant band).

**The overweaving collapse risk by Round 5 (Ob 6):** At 17D TN7 Ob6: P(≥6) ≈ 79%. P(failure) ≈ 12% per round by Round 5. Collapsed overweave at Round 5: RS −3, Shifting Object risk, ejection. If this fires: Round 5 Community Weave failure costs RS −3 vs RS +1 success = a 4× swing on the round. Expected RS from Round 5: (0.79 × 1) + (0.12 × −3) = 0.79 − 0.36 = **+0.43** net. Marginal. 

**[EMERGENT+ — NOT EXPLOIT]** Four Community Weavings in one Focus 5 window is not an exploit — Coherence −4 and increasing Ob make it a high-risk, diminishing-returns gamble. The mechanic is self-regulating. Good design. Surface as a design note: "Community Weaving x4 in a single Focus 5 window produces RS +4 at Coherence −4 cost, with a ~12% catastrophic collapse risk on the final weave. This is the maximum RS restoration achievable in a single contact window via Community Weaving."

---

# 5. COHERENCE 0 FOR AN NPC COMPANION — DOUBLE NPC STATUS

## 5.1 What Is a "Companion" at Coherence 0? [SMOOTH — GAP]

Params_core PP-261: "At Coherence 0: character becomes NPC (100% functional, player agency ends)."

Companion spec: "A companion is a named NPC who travels with the player character." Companions are already NPCs (GM-run). If a practitioner companion reaches Coherence 0: "character becomes NPC." But the companion IS already an NPC.

**The Coherence 0 rule means something specific:** the player loses agency over the companion. For a companion, the player never had mechanical agency (GM runs companions per npc_behavior_v30). So Coherence 0 on a companion NPC means: the GM's control of the companion is now governed by the Coherence 0 protocol (released Coherence 0 characters contribute to world-state from co-authored Belief/Inspiration material) rather than the companion's normal Stance Triangle behavior.

**Practical impact:** A companion at Coherence 0 transitions from: acting per Conviction + Resonant Style (normal NPC behavior) → acting from the Rendering Crisis framework (contributing to world-state, GM-rendered, not relationship-bound). This ends the companion relationship mechanically. The player no longer has a companion — they have a world-state contributor who used to be their companion.

**[SMOOTH — GAP]** The companion departure rules (§3) don't list Coherence 0 as a departure condition, because Coherence 0 isn't departure — it's ontological transition. The companion doesn't leave; they become something else while remaining present. Required addition to companion spec §3: "A companion who reaches Coherence 0 undergoes Rendering Crisis transition. This is not a departure in the conventional sense — the NPC remains in the world but can no longer function as a companion (the relationship-governed behavior that defines companionship has dissolved). The player loses the companion slot immediately. The companion NPC persists as a world-state actor per Coherence 0 rules."

---

# 6. DISSONANCE FACTOR FOR LOCKED ZONES — MISSING FROM TABLE

## 6.1 Locked Zone Dissonance Factor Undefined [GAP]

Dissonance Factor table (params_threadwork):
- Thread operation nearby (brief): 1
- Thread operation nearby (significant): 2
- POP affecting character's own memories: 3
- Entering Field-scale Gap: 2
- Entering Structural-scale Gap: 3
- Extended time in Foundational zone: 4

**Locked Zone is not listed.** A Locked Zone is phenomenologically distinct from a Gap: a Gap is substrate absence; a Locked Zone is substrate frozen. Characters entering a Locked Zone are entering a space where the Thread configuration is permanently immobilized. The phenomenological effect on a non-practitioner: everything feels fixed, immovable, unchangeable — the texture of frozen becoming. This should produce Dissonance.

**[GAP]** Proposed Locked Zone Dissonance Factor based on Lock duration:
| Locked Zone age | Dissonance Factor |
|---|---|
| < 4 seasons (reversible) | 1 |
| 4+ seasons (Permanent, substrate adapted) | 2 |
| Einhir Catastrophe site (centuries) | 3 |

T15 Askeheim is an Einhir Catastrophe site — characters entering Askeheim should make Dissonance checks at Factor 3 (same as entering a Structural Gap), reflecting the profound substrate immobility at the epicenter. This is distinct from Calamity radiation (which affects Ob on rolls) — Dissonance Factor addresses ontological disruption to characters' Spirit tracks.

---

# 7. FOCUS 3 HALVED TO 1 → ZERO OPERATIONS — HIDDEN DEAD ZONE

## 7.1 Focus 2 Gets One Operation; Focus 3 Gets Zero After Halving [ELEGANT — FAILS]

P-11 Focus Halving: "Focus 3 halved = 1 = zero operations. Focus 5 halved = 2 = one operation."

The halving rule produces a non-monotonic result:
| Focus | Halved (round down) | Operations after halving |
|---|---|---|
| 1 | 0 | 0 |
| 2 | 1 | 0 |
| 3 | 1 | 0 |
| 4 | 2 | 1 |
| 5 | 2 | 1 |
| 6 | 3 | 2 |
| 7 | 3 | 2 |

Focus 2 and Focus 3 produce the same result after halving: 0 operations. Focus 3 is a higher investment (attribute point cost) that provides zero additional benefit in halved-duration environments. This creates a "dead zone": Focus 3 in any environment with halved contact duration is mechanically equivalent to Focus 2 — a wasted investment.

**[ELEGANT — FAILS]** Focus 3 should not be equivalent to Focus 2 in any scenario. Proposed fix: "Halved duration: round up rather than down for the purposes of operation count. Focus 3 halved = ceil(3/2) = 2 = one operation." This eliminates the dead zone. Alternatively: "Halving applies to contact rounds only, not operation count. Focus 3 = 3 contact rounds; halved contact = 1.5 rounds → 1 contact round → 0 operations (round 1 is Leap). Focus 4 = 2 contact rounds → 1 op." Same result but mechanically cleaner. The dead zone persists either way with floor rounding; the fix requires ceiling rounding for the operation conversion.

---

# 8. THREAD OPERATION AS DUTY SUBSTITUTE — UNDEFINED

## 8.1 Can Thread Work Satisfy a Factional Duty? [ROBUST — GAP]

Player_agency_v30 (from prior batches): Duties are faction-assigned objectives. Examples inferred: "Govern this settlement," "Recruit officers in T4," "Suppress CI activity in T9."

A player with Duty "Govern S-015 Gransol Parliament" could either: (a) use the Governance action (mundane, pool = Cognition + relevant History, Ob = floor(Prosperity/2)+1), or (b) use a Relational Weave on the Parliament's institutional bonds (Thread operation, per Batch 1 ruling).

**Does the Thread operation satisfy the Duty?** The Duty specifies a governance objective — increasing Order or maintaining institutional stability. If Thread achieves the mechanical outcome (Order +1 via proposed ruling), it has fulfilled the Duty's intent. But the Duty system tracks Duty completion as a factional performance metric — the faction assigned this Duty expects a mundane governance process, not Thread manipulation.

**[ROBUST — GAP]** Two possible design positions:
1. **Thread can satisfy Duties** (outcome-based): if the Thread operation achieves the Duty's mechanical target, the Duty is complete. Encourages creative Thread use.
2. **Thread cannot satisfy Duties** (process-based): Duties require the stated action type. Thread manipulation is a separate act. This preserves Duty as a mundane governance track separate from Thread capability.

Position 2 is more robust: it creates two parallel capability tracks (mundane governance vs Thread manipulation) with different costs and benefits. A practitioner who Thread-Weaves governance simultaneously performs their Duty separately — they are doing more than required, with Thread as surplus action. Required explicit statement in both the Duty system and Thread→settlement interface.

---

# 9. SOLIDARITY RESONANT STYLE + STRAINED KNOT — COLLISION COURSE

## 9.1 The Attack That Destroys Its Own Tool [EMERGENT+ — DESIGN DEPTH]

npc_behavior_v30 §1.3: Solidarity Resonant Style requires "an active Knot with the NPC." The attack is: "Appeals grounded in relational obligation — debts, shared history, personal bonds."

A practitioner who has used Knot-mediated Thread-Read repeatedly on their Close Knot (Batch 2 §4.2 finding: +1 strain per use; threshold undefined) has accumulated Knot strain. If they then attempt a Solidarity attack on an NPC where this Knot is the operative relationship:

The Solidarity attack invokes the relational bond as rhetorical leverage ("you owe me, we share this history, our bond demands this"). The Knot strain accumulation represents the bond being taxed. Using the Knot as a rhetorical tool (Solidarity) while it's already strained from Thread-Read use could be the final strain event that triggers rupture.

**The Solidarity attack itself could rupture the Knot it requires.** Ruling: "Each Solidarity attack that invokes a specific Knot as its rhetorical basis adds +1 strain to that Knot (the relational obligation is called upon, incrementally depleting the bond's resilience). A Solidarity attack against a Knot already at strain threshold triggers rupture after the exchange resolves — the appeal succeeded in drawing on the bond, but the bond breaks under the weight of the appeal." This is mechanically coherent and thematically devastating — the practitioner who wins through Solidarity loses the relationship that enabled it.

---

# 10. FRACTURED FALLOUT "HISTORY UNCERTAIN" — MECHANICAL AMBIGUITY

## 10.1 Is the History Point Mechanically Suspended? [ELEGANT — GAP]

Fractured Fallout (d6=2): "Your most recent History advancement feels uncertain — borrowed, not learned."

Two interpretations:
(a) **Purely narrative**: the character experiences doubt about their competence, but the History point functions normally.
(b) **Mechanically suspended**: the History point cannot be applied as a bonus die this scene — "feels borrowed" = not available.

Under (b): a practitioner who just advanced "Einhir Scholar" cannot use it for Thread ops this scene. This is a significant mechanical penalty — potentially −3D on Thread operations if the History is worth 3 points. Under (a): it costs nothing mechanically.

**[ELEGANT — GAP]** The Fragmented Fallout table is described as firing "on entering this band" — one-time, not per-scene. If (b) is correct: the one-time penalty is limited to the current scene, making it temporary and bounded. If (a): it's flavor text with no mechanical weight, which seems too light for a Coherence crisis consequence. 

**Required ruling:** Interpretation (b) applies, scene-scoped. "Fractured Fallout History uncertain: the most recently advanced History cannot contribute bonus dice this scene (its points are temporarily inaccessible). At scene end, the History functions normally." This makes Fallout tables feel mechanically meaningful without permanently penalizing character advancement.

---

# 11. ISOLATION AS PREREQUISITE FOR FOUNDATIONAL MENDING — IS IT A THREAD OP?

## 11.1 Gap Network Isolation: Undefined Action Type [GAP — CRITICAL FOR ENDGAME]

PP-609: "Edeyja must isolate individual Foundational gaps from network, Mend at Ob 12." Isolation separates one Foundational gap from the interconnected network before Mending can hold. Without isolation: the gap's connection to the rest of the network means Mending one gap immediately stresses adjacent gaps.

**Is isolation itself a Thread operation?** The available text doesn't describe isolation as a specific Thread operation type. Candidates:
- **Lock on the gap's network connections**: Locking the relational bonds between the specific gap and its adjacent network nodes. This prevents the Mended gap from re-feeding destabilization to the network. Ob: Relational Lock on each connection node (4+ connections at T15) = multiple Lock operations. Chronic drift from each Lock: −1 RS/season. The isolation itself generates RS drain.
- **Structural-scale Pulling on the gap site**: Opening the gap's connection to the network, temporarily making it an isolated entity. Duration-limited (Pull duration: ends of session or seasonal Accounting). Mending must complete before Pull duration lapses.
- **Distinct procedure (not standard Thread op)**: Isolation is an Einhir-specific technique requiring the Einhir framework, not a standard Thread operation. This would make isolation itself Einhir-gated — practitioners without Einhir framework access cannot even attempt isolation.

**[GAP — CRITICAL]** The endgame Thread recovery path (isolate → Mend → restore) is mechanically undefined at its first step. Required: explicit definition of isolation as either: (a) a series of Relational Locks on network connections (standard Thread ops, costs RS, duration-indefinite), (b) a structural Pull creating temporary isolation (time-limited, must complete Mending within Pull duration), or (c) an Einhir-framework exclusive technique (gated, not a standard Thread op).

Option (a) is most mechanical consistent with existing rules. Option (c) is most design-consistent with "Einhir framework = endgame Thread path."

---

# 12. HYBRID ZOOM-IN DURING MASS BATTLE — WHICH RS MULTIPLIER?

## 12.1 Zoom-In Practitioner Thread Ops: ×3 or Standard? [SMOOTH — GAP]

Mass battle RS ×3 multiplier (PP-192) applies to Thread ops "in mass battle." Scale Transitions §4.1: Zoom In allows a player to enter a personal scene from the Strategic Phase. The Mass → Personal transition (§3.7: General Duel) creates a personal combat context within a mass battle.

**A practitioner who Zooms In during a mass battle is simultaneously in Personal Phase (TTRPG rules apply) AND in a mass battle context (×3 RS multiplier context).** Which governs their Thread operations?

Three possible rulings:
1. **Zoom-in Thread ops are Personal Phase**: standard RS costs. The practitioner has zoomed in to personal scale; mass battle rules don't apply at personal scale.
2. **Zoom-in Thread ops use ×3**: the mass battle is still occurring; all Thread ops in that context use ×3 regardless of zoom level.
3. **Split by target scale**: Thread ops targeting personal-scale configurations (healing a wound, personal opposition) use standard RS. Thread ops targeting mass battle configurations (unit Discipline, mass cohesion) use ×3.

**[SMOOTH — GAP]** Option 3 is most elegant — it follows from the scale hierarchy (Thread op RS cost × multiplier based on what the op is targeting, not where the practitioner is standing). Required ruling: "Thread operations performed during a Zoom-In from mass battle context: RS costs are ×3 if the operation targets battlefield-scale or unit-scale configurations (Territorial/Field scale and above), and standard if the operation targets personal-scale configurations (Object/Personal/Relational targeting an individual)."

---

# 13. OVER-ACTUALISATION AT FOUNDATIONAL SCALE — UNDEFINED CONSEQUENCE

## 13.1 OA Consequence Table Stops at Structural [GAP — ENDGAME CRITICAL]

OA (Over-Actualisation) table:
| Scale | OA Consequence on Success |
|---|---|
| Object / Personal | None |
| Relational | Subsequent ops on same config: +1 Ob. Clears 1 season or after Pull. |
| Territorial | As Relational + Diagnosis +1 Ob. |
| Structural | As Territorial + +1 RS degradation per season it persists. |
| **Foundational** | **UNDEFINED** |

Any Weaving at Foundational scale (TS 90+, Ob 13, TN 7 — e.g., a practitioner attempting to cohere a Foundational substrate condition) produces OA on Success. What does Foundational OA look like?

By extrapolation from the Structural pattern: "As Structural, plus: additional RS degradation AND something worse." Structrual OA already causes +1 RS/season degradation from the over-actualized configuration. Foundational OA should cascade further — potentially: the entire substrate in the zone resists all Thread operations (not just operations targeting the specific config), generating a locked state approaching a Permanent Lock without the intentionality of a deliberate Lock.

**[GAP — ENDGAME CRITICAL]** Foundational-scale Weaving is the rarest and most powerful Thread operation. Its OA consequence is the most consequential undefined gap in the Thread rules. Required: "Foundational OA on Success: All Thread operations in the zone (not just targeting the specific config) receive +1 Ob. Diagnosis reveals the over-actualized configuration as a dangerous attractor — other configurations begin conforming to it. RS degradation: −2/season until the OA is Pulled or the configuration collapses. If not addressed within 3 seasons: the OA crystallizes into a Permanent Lock on the Foundational condition — the Einhir Catastrophe is replicated locally."

---

# 14. DISSOLUTION OF THREAD CONTACT ITSELF — ONTOLOGICAL EDGE

## 14.1 Can Thread Contact Be Dissolved? [EXPLOIT — METAPHYSICAL]

A practitioner's Thread contact window is a state: their rendering is suspended, they are in originary contact with the substrate. This state is ontologically a configuration — the practitioner's relational state with respect to the substrate during contact.

A hostile practitioner could target this contact-state:
- Target: the contact window as a relational configuration (the practitioner's suspension-of-rendering, actualized as an ongoing state).
- Operation type: Pull (opening the suspension, forcing rendering to reassert) or Dissolution (tearing the contact state, forcing abrupt re-rendering).

Pull on contact: Ob = Loosely/Normally actualized (the contact window is ephemeral, not firmly established) = Ob 1-2 + Relational depth (it is a relational state between practitioner and substrate) = Depth 3 + Ob 1-2 + Breadth 0 + Distance 0-1 = **Ob 4-6, TN 7**. On Success: contact is opened — the practitioner's rendering reasserts. Contact ends. This is a more reliable "interrupt Thread contact" action than dealing wounds (Spirit check Ob 1 to maintain contact on wounding; Pull at Ob 4-6 with 50-75% success rate is more reliable).

**[EXPLOIT — METAPHYSICAL]** This is a precision anti-practitioner technique. No wound required. No direct violence. Just Pull the practitioner's contact state and their Thread capability is terminated for the scene. Required ruling: "A practitioner's Thread contact window is not a Thread-targetable configuration. The contact window is not a relational bond between entities — it is the practitioner's own mode of being during the Leap. The only disruptions to contact are: wounds (Wound disruption check), incapacitation, and natural contact-round expiry. Thread operations cannot directly target another practitioner's contact state."

This ruling is philosophically grounded: the contact window is the practitioner's suspension of their own rendering — it belongs to their first-person experience. It cannot be accessed third-person via Thread any more than a practitioner can Dissolve someone else's consciousness directly.

---

# 15. INQUISITOR TS 30 TESTIMONY — PROSECUTORIAL EVIDENCE GAP

## 15.1 "I Sensed Something" Is Thin as Formal Evidence [SMOOTH — EMERGENT+]

A Church Inquisitor with TS 30 perceives: "Senses an operation in the scene; general direction identifiable." This is their perceptual testimony. Before a Church Tribunal: they can testify to sensing an operation. Not to the type, the target, the practitioner specifically, or the configuration. Just: "something happened, from that direction."

The accused practitioner (against Conviction orthodoxy): "I did nothing. You imagined it." The TS 30 perception is exactly what the Church's theology says doesn't exist — Thread perception. The Inquisitor's testimony is: "I used the perception our doctrine says is either non-existent or demonic to detect Thread practice I cannot specifically identify."

**The Church's prosecutorial system relies on Thread perception to detect Thread practice.** But Thread perception is itself theologically contentious. A skilled accused practitioner can argue that the Inquisitor's perception is itself evidence of Thread contamination — turning the prosecution's tool against them. This is a Reason Resonant Style attack on the theological framework underlying the investigation.

**[SMOOTH — EMERGENT+]** This creates a genuine social contest dynamic with Thread at its center. The Tribunal is a site where: the Inquisitor's Thread perception (real but theologically fraught) confronts the accused's knowledge that they were sensed (accurate but unprovable). A social contest in this space rewards a practitioner who understands both Thread mechanics AND Church theology — they can use the Inquisitor's perceptual testimony as evidence against the Inquisition's own theological premises. Surface as an explicit design note on the Church Tribunal proceeding type.

---

# SUMMARY TABLE — BATCH 7

| Item | Finding | Lens | Severity | Action Required |
|------|---------|------|----------|----------------|
| TS 100 Overwhelming | +1 TS bonus disappears at cap; Overwhelming = Success at TS 100 | **ELEGANT — GAP** | Moderate | Conversion rule: Ob −2 on next operation instead of +1 TS |
| Thread-Read mass battle | Evidence Track frozen AND Thread-Read may advance Evidence Track — self-contradiction | **SMOOTH — FAILS** | High | Rule: Thread-Read Evidence banked, applied at Accounting (battle end) |
| Pool floor conflict | params_core: 1D floor. R-57: 5D floor for Pull only. Two canonical floors | **CONFLICT — CRITICAL** | Critical | Clarify: 5D floor applies to Pull only; all other Thread ops use 1D floor |
| Community Weaving ×4 | Self-regulating via OA + Overweave; RS +4 at Coherence −4 cost; collapse risk by round 4 | **ELEGANT — EMERGENT+** | Low | Surface as max-efficiency design note |
| Coherence 0 companion NPC | Companion already an NPC; Coherence 0 = ontological transition, not departure | **SMOOTH — GAP** | Moderate | Add to companion spec §3: Coherence 0 = companion slot lost; NPC persists as world-state actor |
| Locked Zone Dissonance | Locked Zone not in Dissonance Factor table | **SMOOTH — GAP** | Moderate | Proposed table: 1/2/3 by Lock age; Askeheim = Factor 3 |
| Focus 3 dead zone | Focus 3 halved = same operation count as Focus 2; Focus 3 is wasted investment in halved environments | **ELEGANT — FAILS** | Moderate | Fix: use ceiling rounding for operation conversion after halving |
| Thread Duty substitution | Thread op achieving Duty outcome: does it satisfy the Duty? | **ROBUST — GAP** | Moderate | Rule: Thread does not substitute for Duty (preserves dual-track design) |
| Solidarity + strained Knot | Solidarity attack adds strain; at threshold, the attack ruptures the Knot it requires | **EMERGENT+ — ELEGANT** | Low | Surface as design note; rule: Solidarity adds +1 Knot strain per use |
| Fractured Fallout History | "Uncertain History" — mechanical or narrative? | **ELEGANT — GAP** | Moderate | Rule: scene-scoped mechanical suspension of the specified History points |
| Isolation before Foundational Mending | Isolation undefined as Thread operation type | **GAP — CRITICAL** | Critical | Define isolation: Relational Locks on network connections (Einhir-framework exclusive) |
| Hybrid zoom-in mass battle × 3 | Personal Phase Thread ops during Zoom-In from mass battle: ×3 or standard? | **SMOOTH — GAP** | High | Rule: ×3 for battlefield-scale targets; standard for personal-scale targets |
| OA at Foundational scale | OA consequence table ends at Structural; Foundational OA undefined | **GAP — ENDGAME CRITICAL** | Critical | Proposed: global zone Ob +1 + RS −2/season + crystallizes Permanent Lock after 3 seasons |
| Dissolution of Thread contact | Pull/Dissolution of another practitioner's contact window: metaphysically undefined | **EXPLOIT — METAPHYSICAL** | High | Rule: contact window is not Thread-targetable (first-person mode of being) |
| Inquisitor TS 30 testimony | Inquisitor's perceptual testimony is self-undermining within Church theology | **SMOOTH — EMERGENT+** | Low | Design note: practitioner can use Reason attack on Inquisitor's theological framework |

---

## NEW CRITICAL ITEMS FROM BATCH 7

26. **Pool floor conflict (1D vs 5D)** — two canonical documents specify different minimum pool sizes for Thread operations. This is a direct contradiction that affects every practitioner in a degraded state (wounded, low-Spirit). The 5D floor for Pull operations may be intentional; its scope must be explicitly stated.

27. **Isolation as prerequisite for Foundational Mending** — the endgame RS recovery path requires isolation of Foundational gaps before Mending can hold. Isolation is referenced but never defined as a Thread operation. Without this definition, the endgame recovery path has no first step.

28. **Foundational OA** — OA consequences are defined for Relational, Territorial, and Structural scales but not Foundational. If a practitioner successfully Weaves at Foundational scale, the OA consequence is undefined. Given that Foundational Weaving at Askeheim is a potential endgame action, this is a critical gap.

---

*End of document. Session d8b924fb834a398c.*
