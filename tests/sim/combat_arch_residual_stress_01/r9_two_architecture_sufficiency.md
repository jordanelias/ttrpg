# R9 — Two-Architecture Sufficiency (A + C)
## Module 9 of combat_arch_residual_stress_01

**Date:** 2026-05-10
**Mode:** A coverage
**Source question:** *"Chunk 6 Q5 dropped B (slot formation) on grounds that S7-hybrid subsumes it. Decision needed: is Jordan willing to commit to A+C only, or should B remain available as an opt-in for routine encounters where S7-hybrid feels too heavy?"*

**Decision shape:** A+C sufficient / restore B for [specific encounter shapes]

---

## 1. Verification ledger entries

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| R9-L01 | three_architectures_baseline | Chunks 1-2: A (map+move), B (slot formation), C (duel) | tests/stress/combat_videogame_arch_2026-05-01/05_q4_q5_q6.md | Q5 brief | "Chunks 1–2 establish **A (map+move), B (slot formation), C (duel)** as three architectures." |
| R9-L02 | s7_hybrid_collapses_a_b | S7-hybrid collapses A and B into the same spatial substrate | tests/stress/combat_videogame_arch_2026-05-01/05_q4_q5_q6.md | Q5 | "Chunk 4 favors S7-hybrid which collapses A and B into the same spatial substrate (continuous within a zone). C remains specialized." |
| R9-L03 | b_dropped_recommendation | Drop B as a distinct architecture | tests/stress/combat_videogame_arch_2026-05-01/05_q4_q5_q6.md | Q5 verdict | "**Drop B as a distinct architecture.** Use A (S7-hybrid) for all general combat — adjust *zone size, encounter density, animation speed* to span the use cases B would have served" |
| R9-L04 | c_trigger_six_conditions | C fires on six discriminable conditions | tests/stress/combat_videogame_arch_2026-05-01/05_q4_q5_q6.md | Q5 trigger | "C fires on six discriminable conditions, all canon-adjacent. Default is A." |
| R9-L05 | combat_pool_formula | (Agility × 2) + Relevant History + 3 (minimum 5) | designs/scene/combat_v30.md | §1 | "Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)" |
| R9-L06 | zone_terminology | Close zone = Melee range; Far zone = Ranged distance | designs/scene/combat_v30.md | §5 PP-268 (R7-L03 cross-ref) | "**Zone terminology (PP-268):** Close zone renamed **Melee range**; Far zone renamed **Ranged distance** throughout." |

---

## 2. Coverage analysis — what shapes did B serve?

The original three-architecture model assigned distinct roles:

| Arch | Original scope | Encounter shapes it served |
|---|---|---|
| **A** | Map + move (continuous spatial) | Open-field, multi-zone, ranged + melee mix |
| **B** | Slot formation (DD-style fixed positions, adjacency-only reach) | Corridor ambush, dungeon-room fixed positioning, tavern brawl confined space |
| **C** | Duel (1v1, specialized vocabulary) | T-Wager, T-Cultural, T-Boss, T-Thread, T-Hero-Officer, T-Honor-call (R9-L04) |

**Synthesis claim (R9-L02, R9-L03):** A under S7-hybrid (continuous-position-within-zone, with zone-size as parameter) covers all B shapes via parameter adjustment:

| Encounter shape | Original B mapping | A+S7-hybrid mapping | Adequate? |
|---|---|---|---|
| Corridor ambush (4 actors, narrow space) | Slot formation, adjacency reach | Small zone, melee-range adjacency, sparse Stunt vocabulary | ✓ — small zone IS the slot formation |
| Dungeon room (5 actors around objective) | Fixed-position slot grid | Small zone with environmental anchors (objective fixture as positional fixture) | ✓ |
| Tavern brawl (8 actors, mid space) | Slot formation with environmental hazards | Medium zone with Stunt-eligible environmental features | ✓ |
| Field battle (12 actors, large space) | Was assigned to A | Large zone with multi-zone subdivision | ✓ (canonical A) |
| Hero vs lieutenant + 6 mooks | A territory | Large zone, mooks via Fibonacci pile-on (R6-L01 cap +5) | ✓ |

**The B shapes are entirely replicable by A+S7-hybrid via zone-size + actor-density parameters.**

---

## 3. Candidates

| ID | Name | Description |
|---|---|---|
| **C9.1** | A+C only (synthesis recommendation) | Drop B. Use A under S7-hybrid for all non-duel combat; C for duel triggers per R9-L04. Single combat substrate; zone-size/actor-count parameters span B's prior shapes. |
| **C9.2** | Restore B (three-architecture) | Keep all three. B as opt-in for "feels-too-heavy" routine encounters. |
| **C9.3** | A+C primary, B-shaped opt-in for fixed-position-set-piece encounters | Default A+C; allow GM/engine to flag specific encounter shapes (corridor ambush, dungeon room around objective) for "B-mode" presentation (e.g., simplified UI, no continuous positioning) without restoring B as a distinct architecture. |

---

## 4. NERS at full grain

### C9.1 — A+C only

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Two systems; clear architecture boundary; C trigger logic well-defined R9-L04. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Combat Pool math (R9-L05) unified; zone substrate unified per S7-hybrid. |
| Vertical | ✓ | ✓ | ✓ | ✓ | A scales to mass via Effective Pool (R3-L03); C is scene-only. No B mid-tier orphan. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Threadwork integrates with both A and C cleanly; no B-specific cross-system rules to maintain. |
| Lateral | ✓ | ✓ | ✓ | ✓ | UI/UX: player learns one combat idiom (A) + one set-piece (C); cleaner mental model. |
| Horizontal | ✓ | ✓ | ✓ | ⚠ | ⚠ Horizontal: some videogames use multiple combat modes for variety (Witcher 3 has ranged minigame; Yakuza has tonal mode-switches). Variety-via-architecture is a design surface forfeited. Mitigated by: variety-via-zone-parameters, S7-hybrid encoding, scenes (set pieces). |

**Verdict C9.1:** 23/24 ✓, 1 ⚠ on Horizontal (variety-via-architecture forfeit, mitigated). Strong PASS.

### C9.2 — Restore B (three-architecture)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ⚠ | ⚠ | ⚠ | Three combat systems = three UI languages, three trigger boundaries, three sets of cross-system rules. ⚠ E: design surface tripled. |
| Bottom-up | ✓ | ⚠ | ✓ | ⚠ | All three compose canonical math, but B's slot abstraction is structurally simpler than A's continuous positioning. ⚠ S: B's "slot" doesn't smoothly compose with A's zones at boundary cases (mid-encounter zoom-out from corridor to open). |
| Vertical | ⚠ | ✗ | ⚠ | ⚠ | **E ✗:** B doesn't extend to mass scale per Q5 NERS table (B is "an island"). Need separate logic for "mass battle with B-shape sub-encounter." |
| Diagonal | ⚠ | ⚠ | ⚠ | ⚠ | Threadwork in B: does Leap work in slot-formation? Stunt eligible? Spec gap. |
| Lateral | ⚠ | ⚠ | ⚠ | ⚠ | Three combat UIs increase player mental load; mode-switch friction. |
| Horizontal | ⚠ | ⚠ | ✓ | ⚠ | Variety-via-architecture preserved at substantial complexity cost. |

**Verdict C9.2:** N=⚠ on 5, E=✗ on 1 + ⚠ on 5, R=⚠ on 4, S=⚠ on 6. **MARGINAL — high cost, mostly redundant with A+S7-hybrid coverage.**

### C9.3 — A+C primary with B-shaped opt-in presentation

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ⚠ | ✓ | ✓ | Encoder/UI flag for "B-shape" (simplified UI, no continuous positioning), not a separate mechanical architecture. ⚠ E: presentation complexity but mechanical simplicity. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Mechanically still A; UI is a presentation choice. |
| Vertical | ✓ | ✓ | ✓ | ✓ | No new mass-scale spec; B-shape is presentation-only. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Threadwork etc. operate as A; presentation flag doesn't change mechanics. |
| Lateral | ✓ | ⚠ | ✓ | ✓ | Two presentations of one mechanic — modest UX work; players learn one mechanic-set with two presentations. |
| Horizontal | ✓ | ⚠ | ✓ | ✓ | Variety preserved without architecture proliferation. |

**Verdict C9.3:** 22/24 ✓, 2 ⚠ on E (presentation work). **PASS — preserves variety value of B without B's mechanical cost.**

### Cross-candidate summary

| Candidate | N | E | R | S | Verdict |
|---|---|---|---|---|---|
| C9.1 A+C only | 6/6 | 6/6 | 6/6 | 5/6 (1⚠) | **PASS — synthesis-aligned, simplest** |
| C9.2 Restore B | 1/6 (5⚠) | 0/6 (1✗+5⚠) | 2/6 (4⚠) | 0/6 (6⚠) | **MARGINAL — high cost, low marginal value** |
| C9.3 A+C with B-shape presentation flag | 6/6 | 4/6 (2⚠) | 6/6 | 6/6 | **PASS — variety without architecture proliferation** |

---

## 5. Mode D — Edge cases (compressed)

### Boundary
**EC-D9.B-01 [P3] (C9.3):** "B-shape presentation" criteria need GM/engine spec — when does a small zone trigger simplified UI vs full S7-hybrid?

### Cascade
**EC-D9.C-01 [P3] (C9.2):** Mid-encounter mode-shift (B → A as scope expands) requires migration spec.

### Regression
**EC-D9.R-01 [P3] (C9.2):** Three architectures invite "always use the simplest" optimization — players may default to B for everything, eroding A's design value.

### Crunch cascade
**EC-D9.CR-01 [P2] (C9.2):** Three combat resolutions, three sets of edge-case rules, three sets of cross-system bridges.

### Ambiguity
**EC-D9.A-01 [P3] (C9.3):** Presentation-flag boundary undefined — a corridor-feel encounter at 8 actors borders B-shape but is mechanically A.

### Incoherence
**EC-D9.I-01 [P3] (C9.2):** B's "doesn't extend to mass" creates structural inconsistency at scale boundary.

### Optimal play
**EC-D9.O-01 [P3] (C9.1/C9.3):** Player optimal: lean into the simplicity. Single combat idiom is faster to internalize, more transfer between encounters.

---

## 6. Decision-shape findings

**Recommendation: C9.1 (A+C only — synthesis-aligned) primary; C9.3 (A+C with B-shape presentation flag) as a UX refinement if Jordan wants explicit corridor-ambush / dungeon-room presentation contrast.**

**Rationale:**

1. **C9.1 passes 23/24 NERS.** Synthesis Q5 analysis (R9-L02, R9-L03) is corroborated. A under S7-hybrid covers all B shapes via zone-size + actor-count + Stunt-vocabulary parameters (Section 2 mapping). The single ⚠ on Horizontal (variety-via-architecture forfeit) is mitigated by zone-parameter variety and scenes/set-pieces.

2. **C9.2 (restore B) is high cost for low marginal value.** Three architectures = three UIs, three sets of edge cases, B as orphan-mid-tier. Most encounter shapes B would serve are already coverable in A+S7-hybrid.

3. **C9.3 is a sensible refinement** if Jordan wants the genre-feel contrast between "tactical corridor ambush" UI and "open-field skirmish" UI without mechanical bifurcation. The B-shape flag is a presentation/UX choice, not a separate combat resolution path.

**Implementation under C9.1 (no new code beyond what S7-hybrid already implies):**

- Affirm `combat_v30 §1` Combat Pool (R9-L05) as single math basis for both A and C.
- Drop reference to "Architecture B / slot formation" in design docs; treat B-style encounter shapes as A under specific zone parameters.
- C trigger logic per R9-L04 with six conditions stands.

**Decision-shape statement for Jordan ratification:**

> Combat resolution uses two architectures: A (S7-hybrid scene combat, default) and C (duel, fires on T-Wager / T-Cultural / T-Boss / T-Thread / T-Hero-Officer / T-Honor-call per R9-L04). Architecture B (slot formation) is dropped as redundant with A+S7-hybrid: corridor ambush, dungeon-room fixed positioning, tavern brawl all map to A with appropriate zone-size and actor-count parameters. If Jordan desires UI contrast for tactical-feel encounters (e.g., "corridor mode"), this can be added as a presentation flag on top of A (C9.3) without creating a separate mechanical architecture.

**Open items:**

- Affirm C9.1 closes R9.
- Decide on C9.3 presentation flag — pursue, defer, or reject?

---

## 7. Module status

| Item | Status |
|---|---|
| Synthesis Q5 sources fetched at full depth | ✓ |
| Verification ledger (6 entries) | ✓ |
| Coverage map: B shapes → A+S7-hybrid mapping (Section 2) | ✓ |
| NERS full-grain analysis (72 cells) | ✓ |
| Mode D edge cases | ✓ |
| Decision-shape finding (C9.1 primary; C9.3 refinement option) | ✓ |

**Module 9 status: verified.**
