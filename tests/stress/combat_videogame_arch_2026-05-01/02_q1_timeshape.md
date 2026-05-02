# Combat Stress Test — Chunk 3/7
## NERS-all-directions framework + Q1 worked example: time-shape

**Brief:** test many combat ideas many ways using canonical engine + rules as basis. Videogame medium opens up possibilities the TTRPG zone abstraction hid. Moving scene combat onto real space forces reconsideration of mass battle too.
**Method:** NERS-all-directions — each candidate answer to a design question is evaluated through 6 directional lenses with N/E/R/S scored per lens.

---

## The framework

### NERS — the four criteria (project-canonical)

| | Question |
|---|---|
| **N** Necessary | Is this present, complete, doing required work? |
| **E** Elegant | Logically simple, clear, intuitable from simple choices? |
| **R** Robust | Strategic depth, customization, emergent narrative, complete error-free mechanics? |
| **S** Smooth | Integrates without friction, scales up/down, sequences/transitions cleanly, consistent calculation methodology? |

### All-directions — the six lenses (project-canonical)

| Direction | Lens — what's being tested |
|---|---|
| **Top-down** | Whole-game philosophy → this idea. Does the idea cohere with the game's overall design intent (positive feedback loop player ↔ mechanics, emergent narrative)? Does it fit the videogame medium? |
| **Bottom-up** | Atomic mechanics → this idea. Does the idea compose cleanly from canonical primitives (Combat Pool, weapon TN, damage formula, Wound Interval, Stamina) without forking math? |
| **Vertical** | Scale traversal — personal ↔ settlement ↔ territory ↔ peninsula. Does the idea zoom up/down across scales without breaking? Where does it sit, and does the boundary work? |
| **Diagonal** | Cross-system interaction — combat ↔ fieldwork, combat ↔ thread, combat ↔ social contest, combat ↔ mass battle. Does the idea play well with adjacent systems? |
| **Lateral** | Same-scale parallel — at personal scale: combat ↔ social contest ↔ fieldwork investigation. Do they share substrate cleanly, or do they fork? |
| **Horizontal** | Time/campaign progression — same idea repeated across many encounters and many sessions. Does pacing hold up? Does narrative weight accumulate? |

### Scoring

Per cell: ✓ pass · ⚠ partial / has tension · ✗ fail · — N/A

The full grid per idea = 6 directions × 4 NERS criteria = 24 cells. Compact reporting uses one row per direction with NERS in columns.

---

## Q1 — What is the time-shape of scene combat?

Canonical baseline: phase-locked simultaneous declaration with priority resolution (combat_v30 §2). Round = 6–10s narrative.

The videogame medium permits: continuous time, perfect-info turn, hybrid models, animation-driven beat. The TTRPG zone abstraction hid the fact that real-time options were never on the table; in a videogame, they are.

### Candidates

| ID | Time-shape | Source reference |
|---|---|---|
| T1 | Strict turn-based per-actor | BG3, XCOM 2 |
| T2 | Phase-locked simultaneous (canonical) | Frozen Synapse, combat_v30 §2 |
| T3 | RTwP (real-time with pause) | Pillars 2, Pathfinder: WotR |
| T4 | Active-time gauge with interrupt window | Grandia IP, FF IV/IX |
| T5 | Pure real-time deflect/timing | Sekiro, Souls duels |
| T6 | Perfect-information turn | Into the Breach |
| T7 | Hybrid: command-turn + real-time-execute | Valkyria Chronicles BLiTZ |
| T8 | Pirates!-stance real-time (slow tempo) | Sid Meier's Pirates! |

### NERS per direction — by candidate

#### T1 — Strict turn-based per-actor

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ⚠ | ⚠ | Common, legible, but cedes the simultaneity flavor canonical §2 emphasizes |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Canonical pool split, weapon TN, damage all compose cleanly |
| Vertical | ✓ | ✓ | ⚠ | ⚠ | Mass battle is phased not per-actor; mass↔personal boundary requires explicit mode-switch |
| Diagonal | ✓ | ⚠ | ⚠ | ⚠ | Fieldwork is continuous; turn-based combat freezes the continuous layer abruptly on transition |
| Lateral | ✓ | ✓ | ✓ | ✓ | Social contest and investigation are also turn/phase canonically — system reuse high |
| Horizontal | ⚠ | ✓ | ⚠ | ⚠ | Long encounters bog down across a campaign; pacing tax accumulates |

**Verdict:** Safe choice with friction at vertical (mass interface) and diagonal (fieldwork integration) and pacing tax horizontally.

#### T2 — Phase-locked simultaneous (canonical)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ⚠ | ✓ | ✓ | Preserves canon; but blind-declare UI is conceptually elegant yet hard to make legible |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | All canonical primitives assume this — Feint mind-games, initiative transfer, declare-then-resolve |
| Vertical | ✓ | ✓ | ✓ | ✓ | Mass battle (mass_battle_v30 §A.7) is also phased — vertical alignment is native |
| Diagonal | ✓ | ⚠ | ✓ | ⚠ | Social contest is canonically phased — aligns. Fieldwork is continuous — transition has cost. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Phase model shared with social contest, miraculous events — high reuse |
| Horizontal | ✓ | ⚠ | ✓ | ⚠ | Phase rhythm is consistent over a campaign but each round has the same UX cost — risk of repetition fatigue without animation variety |

**Verdict:** Strong on canonical fidelity and lateral/vertical reuse. UX tax on legibility (blind-declare) is the main friction. Frozen Synapse is the proof-of-concept that this can work.

#### T3 — RTwP (real-time with pause)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Mature CRPG idiom; player can choose tempo; cohesive with player-agency design intent |
| Bottom-up | ⚠ | ⚠ | ✓ | ⚠ | Canonical phase order requires fudging — actions resolve as their recovery timers complete; "blind simultaneous declare" becomes "everyone queues, animation order = priority order" |
| Vertical | ⚠ | ⚠ | ⚠ | ✗ | Mass battle is phased — RTwP doesn't extend to army scale without a different time-shape — mass↔personal is two modes |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Fieldwork is continuous — RTwP combat is the same time-shape, transition is seamless |
| Lateral | ⚠ | ⚠ | ⚠ | ⚠ | Social contest is phased canonically — mismatched time-shape with combat means two different UX modes at the same scale |
| Horizontal | ✓ | ✓ | ⚠ | ✓ | Tempo can compress for routine encounters; campaign pacing flexible |

**Verdict:** Strong diagonal (fieldwork) and horizontal (pacing) at the cost of vertical (mass mismatch) and lateral (social contest mismatch). Mode-switch tax.

#### T4 — Active-time gauge with interrupt window (Grandia IP)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Preserves declare-then-resolve flavor with continuous time; cohesive with videogame medium |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | IP gauge IS canonical priority resolution made visible. Interrupt = canonical Feint pool reduction surfaced as gameplay |
| Vertical | ⚠ | ⚠ | ✓ | ⚠ | Mass battle could borrow the IP-gauge metaphor at unit scale (each unit acts when its IP fills) — feasible but requires mass spec rework |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Continuous gauge bridges fieldwork's continuous time and combat's phased declarations |
| Lateral | ⚠ | ✓ | ✓ | ⚠ | Social contest could also use IP-gauge — would unify all phased systems under continuous-tempo UI; net-new lateral spec |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Compresses well for routine combat (gauges fill faster); slows for set-pieces |

**Verdict:** Highest-fit time-shape. Visualizes canonical priority resolution as gameplay. Vertical reuse (mass) and lateral reuse (social) plausible but require rework. **Standout candidate.**

#### T5 — Pure real-time deflect/timing (Sekiro)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ✓ | ⚠ | ✗ | High-skill action genre; mismatches game's strategic depth intent at non-duel scales |
| Bottom-up | ⚠ | ✗ | ⚠ | ✗ | Canonical pool split, weapon TN, damage all need translation; Combat Pool dice abstraction breaks if every input matters |
| Vertical | ✗ | — | — | ✗ | No path to mass battle |
| Diagonal | ⚠ | ⚠ | ⚠ | ⚠ | Fieldwork transition is fine in time-shape; but skill-gating combat detaches it from canonical stat-driven resolution |
| Lateral | ✗ | — | — | ✗ | Social contest and investigation cannot use this paradigm |
| Horizontal | ✓ | ✓ | ⚠ | ⚠ | High-engagement per encounter but exhausting across a long campaign |

**Verdict:** Reject as primary. Viable only as **C duel architecture's optional skill layer** — does not generalize to A or B.

#### T6 — Perfect-information turn (Into the Breach)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ✓ | ⚠ | ⚠ | Excellent legibility but kills the simultaneity surprise canonical Feint depends on |
| Bottom-up | ✗ | — | ✗ | ✗ | Canonical "blind simultaneous declare" inverted — Feint becomes deterministic puzzle |
| Vertical | — | — | — | — | Mass battle untouched; mass not perfect-info anyway |
| Diagonal | ⚠ | ✓ | ⚠ | ⚠ | Fieldwork is partial-info — combat being full-info inverts the information gradient |
| Lateral | ✗ | — | ✗ | ✗ | Social contest depends on hidden intent — perfect-info would break social mechanics if extended laterally |
| Horizontal | ⚠ | ✓ | ⚠ | ✓ | Solvable-puzzle feel reduces emergent narrative variance over campaign |

**Verdict:** Reject as primary. Possible **accessibility/tutorial mode** showing predicted enemy intent.

#### T7 — Hybrid command-turn + real-time-execute (BLiTZ)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ⚠ | ✓ | ⚠ | Off-genre (3rd-person shooter origin); doesn't fit Valoria's stat-driven tone |
| Bottom-up | ⚠ | ⚠ | ⚠ | ⚠ | Real-time aim layer adds skill input that bypasses canonical TN |
| Vertical | ⚠ | — | — | ⚠ | Doesn't generalize to mass |
| Diagonal | ⚠ | ⚠ | ⚠ | ⚠ | Two-mode combat creates more transition surface |
| Lateral | ✗ | — | — | ✗ | No social/investigation analog |
| Horizontal | ⚠ | ✓ | ⚠ | ⚠ | High-engagement; off-tone |

**Verdict:** Reject. Off-genre.

#### T8 — Pirates!-stance real-time (slow tempo)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ⚠ | Excellent for set-piece duels; doesn't generalize to group combat |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Stance = pool split commit; footwork = Establish Distance — direct canonical mapping (see Chunk 2 §1) |
| Vertical | ✗ | — | — | ✗ | Cannot scale up to mass |
| Diagonal | ⚠ | ✓ | ✓ | ⚠ | Fieldwork transition fine; cannot host social contest analog |
| Lateral | ✗ | — | — | ✗ | Single-purpose architecture |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Set-piece weight scales narratively across campaign |

**Verdict:** Strong fit for **C only**. Same conclusion as Chunk 2 — Pirates! is the duel-architecture flagship.

---

### Aggregate read on Q1

| Candidate | Best for | Worst at | Recommendation |
|---|---|---|---|
| T1 strict turn | Routine combat legibility | Mass↔personal vertical mismatch; campaign pacing | Backup if T2/T4 fail |
| T2 phase-locked sim (canonical) | Vertical+lateral reuse, canon fidelity | UI legibility (blind-declare) | **Default for canonical respect** — adopt with Grandia-IP visualization |
| T3 RTwP | Diagonal fieldwork bridge | Vertical (mass) mismatch; lateral (social) mismatch | Dual-mode (RTwP combat + phased social) is a real cost |
| **T4 active-time gauge** | All directions ✓ or ⚠ | Mass requires rework | **Standout — combine with T2 to surface canonical phases as IP gauge** |
| T5 pure real-time | Duel-only | Everything else | Optional C skill layer |
| T6 perfect-info turn | Accessibility | Canonical Feint loop dies | Tutorial mode only |
| T7 BLiTZ hybrid | None | Off-genre | Reject |
| T8 Pirates! stance RT | C duel | Generalization | C-only flagship |

**Composite recommendation:** **T2 + T4 hybrid as default** — canonical phase-locked simultaneous declaration *visualized* as Grandia-IP gauge so players see the canonical priority order play out. Specialize T8 (Pirates! real-time) for C duel set-pieces. Optional T1 for strict-turn accessibility / tactical-pause mode. Reject T5/T6/T7 as primaries.

This single decision sets up Q2 (spatial substrate) — the IP gauge runs on continuous time, which means real-space continuous movement is also viable, which is what unlocks the move away from zone abstraction.

---

## Mass-battle implication of Q1 decision

If scene combat adopts T2+T4 (canonical phase-locked simultaneous, IP-gauge visualized), mass battle inherits the same time-shape pattern:
- Each unit acts when its IP fills (Discipline + Speed → IP rate)
- Engagements within mass battle resolve via canonical Combat Pool math at unit scale (Power dice pool)
- Hero participation in mass battle: hero's IP gauge ticks alongside units; hero acts on individual canonical resolution within the unit-scale frame

This **eliminates the canonical phase-mode-switch (PP-089/PP-090, mass_battle §A.7)** as a hard transition — both scales are the same time-shape, just different actor granularity. Ratification cost: mass_battle_v30 §A.7 needs rework. Payoff: vertical scale-traversal becomes seamless rather than mode-gated.

This is the kind of opportunity the move away from zone abstraction surfaces.

---

## Canon gaps surfaced (Q1)

1. **Phase visualization spec.** Canonical §2 says "phase-based, simultaneous, blind" but specifies no UI. T4 (Grandia IP gauge) would fill this — net-new canon content.
2. **Mass-battle time-shape unification.** If T2+T4 is adopted at scene scale, mass_battle §A.7's distinct phase model becomes redundant. Decision needed: unify or maintain dual time-shapes.
3. **Skill-input layer for C.** Canonical math is dice-driven; T5/T8 add skill timing on top. Canon needs a rule for whether skill input adds dice (cap +1 net hit?) or modifies TN.
4. **Accessibility / tutorial mode.** T6 perfect-info turn as an opt-in mode — does canon allow opt-in time-shape variants per session?

End Chunk 3.
