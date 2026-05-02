# Combat Stress Test — Chunk 7/7
## Synthesis · Canon impact · Godot path · Residual risks

**Closing chunk.** Six prior chunks tested the design space. This chunk consolidates: the stack of decisions, the canonical refactor cost, a phased Godot implementation path, and the residual risks that should be flagged for Jordan's review before any of this becomes canon.

---

## 1. The composite design stack — what the stress test produced

| Layer | Decision | Source chunk |
|---|---|---|
| **Time-shape** | T2+T4: phase-locked simultaneous declaration *visualized* as Grandia-style IP gauge. Same clock for scene + mass actors. | Ch3 |
| **Spatial substrate** | S7-hybrid: world is canonically zoned (mass + fieldwork + scene share the zone primitive), sub-zone continuous space at scene scale. | Ch4 |
| **Scene↔mass interface** | Three-tier ship path: I1 (modal zoom, MVP) → I4 (parallel scenes, v0.2) → I2 (continuous-zoom, v1.0). Each tier is a complete game. | Ch5 |
| **Combat architectures** | Two: A (general scene combat on S7-hybrid) + C (specialized duel). B (DD-slot) dropped — S7-hybrid + variable zone size subsumes it. | Ch6 Q5 |
| **C trigger logic** | C fires on six 2-participant conditions: Wager / Cultural / Boss / Thread / Hero-Officer / Honor-call. Default is A. | Ch6 Q5 |
| **Action economy** | Canonical pool split + Stamina (E1) baseline. Stamina-banking for Heavy attack (E6) added universally. Posture-as-yield (E7) in C only. | Ch6 Q4 |
| **Fieldwork bridge** | F2+F3: same-map continuous with stealth-graduated Exposure ramp. Combat is a state of the map, not a separate scene. | Ch6 Q6 |
| **C duel system** | Pirates!-style stance UI + Sekiro-posture endgame + arena-tagged Stunt opportunities + audience for Reputation. | Ch2 |

### Why this composes

- **Same time-shape** (T2+T4) lets scene and mass tick on one clock. The mass-battle phase mode-switch (canonical §A.7) becomes redundant.
- **Same spatial substrate** (S7-hybrid) means scaling between mass / fieldwork / scene is *granularity*, not *mode*. Camera-driven zoom (I2) IS the scale-traversal mechanism.
- **Same map** (F2+F3) means combat is a state of the existing map, not a separate scene. Investigation, combat, mass battle, fieldwork all happen on the same persistent geography.
- **Two architectures (A + C)** keep the design surface small. C's specialized presentation is justified by narrative weight (set-piece duels), not by mechanical necessity.
- **Canonical math is preserved everywhere.** Combat Pool, weapon TN matrix, damage formula, Wound Interval, Stamina, Threadwork all run unchanged at every scale and architecture. The videogame medium changes presentation, time-shape visualization, and spatial substrate — not resolution math.

### Why this is a single coherent move, not seven separate decisions

The TTRPG zone abstraction was a single cognitive scaffolding decision that propagated through every other layer of canon: it forced phase-mode-switching between scales (because zones at scene and zones at mass were qualitatively different), forced modal transitions between fieldwork and combat (because zones were the wrong granularity for fieldwork), forced the three-architecture split (because zones-at-scene needed more spatial detail than zones gave). **Removing the scaffolding collapses all of these subsidiary frictions.**

The composite stack is what the canon looks like when zone abstraction is replaced by canonical-zones-at-mass + continuous-within-zone-at-scene, with the videogame medium making the spatial substrate continuously presentable. Each individual decision in the stack is a consequence of that single substrate move, not an independent choice.

---

## 2. Canon impact — what files change, how much

Categorized by impact severity. Reference: `designs/scene/combat_v30.md`, `designs/scene/derived_stats_v30.md`, `designs/provincial/mass_battle_v30.md`, `designs/provincial/fieldwork_v30.md`.

### Major rewrite (substantial section overhaul)

| File / section | Change | Reason |
|---|---|---|
| `combat_v30 §2` Phase round structure | Add IP-gauge visualization spec; clarify same-clock-as-mass. Existing phase rules retained. | T2+T4 unification |
| `combat_v30 §5` Reach / Zone / Cover | Add sub-zone continuous-position spec. Convert zone reach (Melee/Ranged) to threshold distances within sub-zone. | S7-hybrid |
| `combat_v30 §11.5` Combat ↔ Fieldwork | Replace modal-transition language with same-map continuous bridge. Add stealth-graduated Exposure ramp (F3). | F2+F3 |
| `mass_battle_v30 §A.7` Battle Turn Structure | Replace distinct mass-phase model with unified IP-gauge ticking on same clock as scene actors. Cascade Phase steps retained but rendered as IP-driven. | T2+T4 unification |
| `mass_battle_v30 §B.5` Hybrid Handoff | Generalize from board-game-flavored zoom to videogame-medium continuous-zoom (or modal handoff for I1 MVP). | I1/I2 interface |
| `mass_battle_v30` Three-mode framing | Reframe: TTRPG mode deprecated; Hybrid mode = videogame default; Board-Game mode = abstract off-screen battle resolution. | I7 use case |

### Net-new content (chapters / files needed)

| File / section | Content | Reason |
|---|---|---|
| `combat_v30 §B` (new) — Duel architecture | Full C spec: stance UI, Pirates!-style commit-and-tell, posture-as-yield, arena tags, audience-for-Reputation | Ch2, Ch6 Q5 |
| `combat_v30 §X` (new) — Architecture selector | Trigger logic: when C fires vs A. Six trigger conditions. | Ch6 Q5 |
| `combat_v30 §Y` (new) — Wager system | Stake types (Conviction / Renown / item / life), accept/refuse rules, Reputation/Conviction tags | Ch6 Q5 |
| `combat_v30 §7` extension — Stamina banking | Pre-commit rule for Heavy attack via banked Stamina (≤1.5× max) | Ch6 Q4 |
| Cross-cutting — Cultural-refusal table | Reputation/Conviction tags for refusing T-Cultural / T-Honor-call duels | Ch6 Q5 |
| Cross-cutting — Stealth detection spec | Visibility cones, sound radius, Exposure tier engine, silent-elimination rule | Ch6 Q6 |
| Cross-cutting — Pursuit-as-scene | When mass-battle rout becomes a personal-scale chase scene | Ch5 §A.12 |
| Cross-cutting — Officer-assassination spec | T-Hero-Officer trigger, mid-battle isolation rules | Ch5 §D.2 |

### Minor extension (additions to existing rules)

| File / section | Change |
|---|---|
| `combat_v30 §4` Stunt | Add: substrate-aware Stunt determination (geometry-driven in continuous, tag-driven in zones, arena-driven in C). Cap +5 retained. |
| `combat_v30 §5` Cover | Add: LoS-aware sub-zone cover variant. Preserves Soft/Hard DR values. |
| `combat_v30 §8` Fibonacci | Add: explicit proximity radius (count attackers within Long reach of target). Numeric values intact. |
| `mass_battle_v30 §D.1` Post-battle scenes | No change. Already videogame-friendly. |
| `mass_battle_v30 §A.10` Threadwork | Add: cross-scale fire is now real-time (same clock); §10.3 Cross-System Fire timing simplifies. |

### Unchanged (preserves canon as-is)

- All Combat Pool math (Agi×2 + Hist + 3)
- Weapon TN matrix (Short/Long, Light/Heavy, Blade/Blunt)
- Damage formula (net hits + STR + weapon mod − DR)
- Wound Interval, −1D per Wound, incapacitation stages
- Stamina formula and per-action costs (banking is pre-commit only)
- Threadwork Leap mechanics (+1 Ob per Wound, full-pool defence)
- Faction unit rosters (mass §11)
- Death Cascade (§13.3) — preserved verbatim
- Reputation Cascade (§13.2) — preserved verbatim
- Conviction Track interactions

**Net canon footprint:** ~6 major rewrites, ~8 net-new sections, ~5 minor extensions, ~10 unchanged anchors. The canonical resolution math is **fully preserved**. The rework is in presentation, time-shape visualization, spatial substrate, and inter-system bridges — not in the dice or the damage tables.

---

## 3. Godot implementation path — phased

### Phase 0 — Spike & vertical slice (weeks 1–4)

**Goal:** prove the substrate decision in code before committing canon.

| Deliverable | Notes |
|---|---|
| Single zone with 4 actors on continuous-position substrate | S7-hybrid sub-zone test |
| Canonical Combat Pool math implemented | Bottom-up canon test |
| IP gauge UI (T4) running for the 4 actors | Time-shape test |
| One C duel scene with stance UI and Sekiro-posture | Architecture test |

**Decision gate:** does the spike feel like Valoria? If S7-hybrid + IP gauge + canonical math gives the right mood, proceed. If it feels arcade-y or loses the canonical strategic depth, reconsider the substrate decision.

### Phase 1 — MVP (months 1–6)

**Goal:** ship a complete game using **I1 (modal zoom)** for scene↔mass interface — the lowest-cost interface tier.

| Deliverable | Notes |
|---|---|
| A architecture (general scene combat) on S7-hybrid | Single zone, ≤8 actors |
| C architecture (duel) with Pirates!-style stance UI | Triggered on the six conditions |
| F2 same-map fieldwork bridge | Combat is a state of the fieldwork map |
| F3 stealth-graduated Exposure ramp | Pre-combat detection |
| Mass battle in canonical Part B abstract resolution mode (Board-Game mode) | I7 use case — off-screen and on-screen abstract |
| I1 modal scene-zoom for hero-vs-officer mid-battle moments | Canonical Hybrid Handoff |
| Action economy: E1 + E6 (Stamina-banking) + E7 (posture in C) | All ready |

**Cut:** continuous-zoom (I2), parallel scenes (I4), continuous mass-battle simulation. Mass battle resolves abstractly; player participates via I1 zoom-in moments.

**Why this ships:** All canonical resolution math runs. Scene combat is rich (S7-hybrid). Duels are cinematic (C). Fieldwork integrates seamlessly (F2). Mass battles work via canonical Board-Game mode plus authored I1 zoom moments. The game is complete.

### Phase 2 — v0.2 (months 7–12)

**Goal:** upgrade scene↔mass interface to **I4 (parallel scenes)**.

| Deliverable | Notes |
|---|---|
| Mass-battle layer running concurrent unit-scale simulation | Same time-shape (T2+T4) — IP gauge ticks for units too |
| I4 hero-detached parallel scenes | Hero plays scene-scale on a sub-region while units act at mass scale |
| End-of-round merger logic | Hero outcomes affect adjacent units; unit outcomes affect hero |
| Mass-battle Threadwork at unit scale | Canonical §A.10 cross-scale fire fully supported |
| Officer-assassination as scene event | T-Hero-Officer trigger fires |
| Pursuit-as-scene for routing units | Canonical §A.12 in personal scale |

**Cut from this phase:** continuous-zoom rendering (intermediate zoom levels with units composed of individuals).

### Phase 3 — v1.0 (months 13–24)

**Goal:** reach **I2 (continuous-zoom)** — the full Bannerlord/Three Kingdoms experience.

| Deliverable | Notes |
|---|---|
| Multi-resolution simulation: units always tick; individuals spawn at zoom threshold | Engineering project |
| Camera-driven scale traversal: army view ↔ unit view ↔ individual view | UX project |
| Threadwork at any zoom on the same clock | Canonical realization |
| Officer hunt mid-battle in continuous zoom | Drama maximized |
| Optional skill-input layer for C (Sekiro-deflect window) | E5 inspiration retained as toggleable |

### Phase 4 — refinements (ongoing)

- Hex grid (S3) toggle for tactics-genre players (low priority — niche audience)
- Elevation (S8) for fortress / cathedral / tower scenes (medium priority — high payoff per scene)
- Tactic-card pre-combat tap-in linking BG-layer cards to scene combat (low-medium priority)

### Cost estimate

| Phase | Engineering scope | Calendar |
|---|---|---|
| 0 spike | 1 engineer × 1 month | 1 month |
| 1 MVP | 2–3 engineers × 6 months | 6 months |
| 2 v0.2 | 2–3 engineers × 6 months | 6 months |
| 3 v1.0 | 4–5 engineers × 12 months | 12 months |

[CONFIDENCE: low — engineering estimates without knowing team size or Godot familiarity]. Provided as relative shape, not commitment.

---

## 4. Residual risks — flag for Jordan

These are decisions or tensions that the stress test surfaced but **did not resolve**. They need explicit Jordan judgment before canonical adoption.

### R1 — Wound permanence vs canonical recovery

**Tension:** canonical §4 says Wounds clear at end of session. Wildermyth pattern (Chunk 2 §3) suggests permanent-consequence Wounds for narrative weight. The composite stack doesn't take a position. **Decision needed:** do some Wounds (catastrophic — limb loss, blind eye) become permanent for narrative payoff, with normal Wounds clearing canonically?

### R2 — Skill input layer in C

**Tension:** canonical math is dice-driven. Pirates! / Sekiro / For Honor reference systems involve real-time player skill (timing windows, deflect windows, animation reads). Chunk 6 Q4 adopted E5 as "C-only inspiration" without specifying mechanic. **Decision needed:** does C add a skill-timing layer that modifies dice (cap +1 net hit), or does C remain pure dice with stance-UI as visualization only?

### R3 — Mass-battle three-mode reframe

**Tension:** canonical `mass_battle_v30` Parts A (TTRPG), B (Board), D (World Bridge) coexist. Chunk 5 recommends deprecating Part A and reframing Part B as off-screen abstract resolution. **Decision needed:** is Jordan committed to this reframe, or does some TTRPG/board structure need preserving for design parallels with canonical fieldwork modes?

### R4 — Hero participation default

**Tension:** when the player is in a mass battle, is hero participation **default** (player plays hero scene-scale by default, can choose to step back to commander view) or **opt-in** (battle is mass-only by default, player steps in during scripted beats)? Influences pacing and player agency. **Decision needed.**

### R5 — Wager system stake range

**Tension:** Conviction / Renown / item / life stakes are canonical adjacencies but no canonical wager spec exists. The range from "honor stake" to "to-the-death" is wide. **Decision needed:** what stake types are canon, what are their numeric ranges, and how do they integrate with Conviction Track / Reputation Cascade?

### R6 — Fibonacci cap

**Tension:** canonical Fibonacci (§8) caps at 8+ attackers. In a 12-attacker continuous-substrate encounter, does the cap hold or extend? **Decision needed:** numeric cap or asymptote behavior at high N.

### R7 — Friendly fire and ranged in melee

**Tension:** S7-hybrid sub-zone continuous adds the question of whether ranged attackers can hit allies in melee with their target. Canonical "ranged at Close zone defends Def TN 8" handles ranged-into-melee but not friendly fire. **Decision needed:** is friendly fire a canonical mechanic, and if so under what conditions?

### R8 — Real-time fieldwork ↔ phased combat tempo shift

**Tension:** F2 same-map continuous bridge says combat begins on the existing fieldwork map with a tempo shift. The mechanism of the shift — does the world freeze for non-combatants? Do bystanders react in real-time? — is unspecified. **Decision needed.**

### R9 — Two-architecture sufficiency

**Tension:** Chunk 6 Q5 dropped B (slot formation) on grounds that S7-hybrid subsumes it. This is the most opinionated reduction in the stress test. **Decision needed:** is Jordan willing to commit to A+C only, or should B remain available as an opt-in for routine encounters where S7-hybrid feels too heavy?

### R10 — IP-gauge legibility tax

**Tension:** the stress test recommends T2+T4 (IP gauge visualizing canonical phase order). IP gauges are a known UX idiom but **add visual complexity at small scales** — when 12 actors are on screen, 12 gauges may be overwhelming. **Decision needed:** is there a per-scene-actor-count threshold above which the gauge is collapsed or hidden?

---

## 5. What the stress test does not cover

These are out of scope for this stress test but flagged for follow-up:

- **AI behavior in combat.** No AI temperament spec was tested — companion behavior, enemy tactical AI, NPC reaction to Stamina/Wounds.
- **Equipment loadout depth.** Only canonical weapon TN matrix tested. Not tested: armor crafting, weapon enchantment, Conviction-themed equipment.
- **Specific cultural duel codes.** Varfell single combat, Crown formal duel, Practitioner Thread duel were named but not specified beyond trigger conditions.
- **Multiplayer / save state at granularity.** Not in scope for single-player canonical design but may surface engineering questions later.
- **Accessibility specifics.** I6 (perfect-info turn) flagged as accessibility mode but not specified.
- **Difficulty / canonical variance.** No tested mechanic for scaling encounter difficulty without breaking canonical math.

---

## 6. Closing read — what this stress test produced

A stress test is supposed to find the system's breaking points. This one found that **the canonical resolution math doesn't break under any of the videogame-medium variants tested**. Combat Pool, weapon TN, damage formula, Wound Interval, Stamina, Threadwork — all survive.

What breaks is the **scaffolding around the math**: zone abstraction, modal transitions, three-architecture splits, separate phase models per scale. These are TTRPG/board-game artifacts that the videogame medium can replace with a continuous spatial substrate, a unified time-shape, and camera-driven scale traversal.

The composite stack (T2+T4, S7-hybrid, I2/I4/I1, A+C, E1+E6+E7, F2+F3) is **canon-respecting in math and canon-revising in structure**. The structural revision reduces complexity rather than adding it. The trade is canonical refactor cost (ten gaps, six rewrites, eight new sections) for sustained design coherence across all four game scales.

The set-piece duel architecture (C) earns its specialization by carrying narrative weight that the general substrate (A) cannot present cinematically. Pirates! + Sekiro + For Honor + Witcher 1 all converge on the same family of mechanics; canonical Combat Pool fits that family natively.

The single largest decision is dropping the TTRPG zone abstraction. Every other decision in this stress test is a consequence of that move. The decision is sound on every NERS-all-directions test it was put through. The follow-up Jordan judgment calls (R1–R10) are second-order tunings, not first-order tensions.

End Chunk 7. End stress test.
