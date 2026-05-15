# Engine NERS — All-Directions Audit

**Date:** 2026-05-15
**Scope:** Dice engine + derived score architecture + Ob/Pool channel design, audited as the unified mechanical substrate underneath all Valoria systems.
**Method:** Throughlines → NERS per throughline → six-direction audit → consolidated inconsistency map → unification proposals.
**Predecessors reviewed:** `tests/audit/all_directions_ners_v27.md` (weapon-system scope), `tests/audit/pp717_ners_all_directions.md` (PP-717 D1–D5 scope), `tests/audit/engine_audit_2026-04-18.md` (sim-code-vs-canon scope). This audit is **first engine-design NERS at the architectural level** — no prior coverage at this scope.

---

## §1 What the engine is

| Layer | Components | Canonical source |
|---|---|---|
| **Dice primitive** | d10, face values, TN bands, degree table, Ob scale, Pool floor, Momentum | `params/core.md` L10–L96, §Momentum |
| **Pool grammar** | `(Attr × 2) + History + K` (K=3 default; TPS for Thread); diminishing returns for combat above Agi 4 | `params/core.md` §Attributes; `params/combat.md` L14; `params/threadwork.md` L20 |
| **Attribute scale** | 1–7, creation max 5, advancement max 7 | `params/core.md` L100 |
| **Derived score architecture** | `derived = attribute × multiplier`; stats = capacity, derived = state | `derived_stats_v30.md` §1 |
| **Ob channel** | Environmental difficulty; 1–20 scale; reserved per PP-716 for non-actor-state effects | `params/core.md` L31; `derived_stats_v30.md` §4.1 |
| **Pool penalty channel** | Actor-state degradation (wounds, depletion); −1D unit; floor 1D | PP-716; `derived_stats_v30.md` §4.1 |
| **Track / clock / counter layer** | Piety, Disposition, Coherence, Certainty, TS, MS, CI, IP, Evidence, Saturation, etc. | Multiple |

The engine is the substrate everything else stands on. Every system (combat, thread, contest, fieldwork, mass combat, faction, knot) is a specific configuration of the layers above.

---

## §2 Throughlines

Five recurring principles that the engine currently expresses:

**TE-1 · The pool is the actor; the Ob is the world.** (PP-716 reservation.) Wound = −1D. Out of Breath = −2D. Cover = +Ob. Stunt = −Ob. Per-actor degradation never touches Ob; per-environment difficulty never touches Pool.

**TE-2 · One attribute, one role, in each system.** No multi-attribute pools. Thread = Spirit. Combat = Agility. Connect = Bonds. Argue = Primary (Cog or Cha by adjudicator). The engine does not average attributes; it elects one per resolution.

**TE-3 · Capacity (1–7) ≠ state (derived).** Stats are slow (advancement events); derived values are fast (per-action). The split exists because dice probability flattens above ~12D, so attributes must stay small; but state tracking needs granularity, so derived values use multipliers.

**TE-4 · Diminishing returns above the median.** PP-717 introduced this for combat (Agi above 4) and wounds (MW capped at 3 ≈ End 5+). The principle: a master is meaningfully better than competent, but not exponentially so. Other systems do not currently honor this principle.

**TE-5 · Degree resolution scales with Ob.** Overwhelming requires `net ≥ max(2·Ob, 3)`. So at Ob 1 everything has the full degree spread (F/P/S/OW); at Ob 13+ Overwhelming becomes structurally inaccessible. The system intentionally narrows the degree palette at high Ob.

---

## §3 NERS scorecard per throughline

| Throughline | N | E | R | S | Notes |
|---|---|---|---|---|---|
| TE-1 Pool=actor, Ob=world | ✓ | ✓ | ✓ | ~ | Rattled (social) breaks separation; Cover Ob is environmental but tied to actor positioning |
| TE-2 One attribute per role | ✓ | ✓ | ~ | ✓ | Spirit carries Thread Pool + Thread Fatigue + Resolve + Knot — concentrated weight on one attribute |
| TE-3 Capacity ≠ state | ✓ | ~ | ✓ | ~ | Multiplier values arbitrary across scales; §14 includes non-derived values (Coherence, Resolve) as derived |
| TE-4 DR above median | ~ | ~ | ✓ | ✗ | Only combat applies it; lateral inconsistency with Thread/Contest/Fieldwork |
| TE-5 Degree scales with Ob | ✓ | ✓ | ~ | ✓ | Foundational Thread ops (Ob 12–13) lose Overwhelming entirely — design intent but underdocumented |

`✓` pass · `~` partial · `✗` fail. Three partials and one fail. The fail (TE-4 Smooth) is the v27 lateral flag promoted to engine-level: PP-717 DR is asserted as a system-wide design philosophy but implemented only in combat.

---

## §4 Six-direction audit

### §4.1 Top-down: engine intent → realization

Engine intent: *positive feedback loop between player decisions and mechanics that produces engaging gameplay with emergent narratives.*

The engine substrate supports this **well** at the personal scale: every decision (attribute allocation, weapon, action choice, resource spend) maps to dice outcomes with visible probabilistic consequences. The Pool/Ob channel separation is the right shape for it — actor agency lives in the Pool, world response lives in the Ob.

**Top-down inconsistencies:**

- **TD-1 · The "no change to the dice engine" claim is overstated.** `derived_stats_v30.md §1`: *"No change to the dice engine."* But PP-717 introduced a non-linear pool formula in combat (diminishing returns above Agi 4). That IS a change to the dice engine. **NERS: Smooth.** Source: `derived_stats_v30.md §1` L12 vs `params/combat.md` L14.

- **TD-2 · `derived_value = attribute × multiplier` rule broken by Health.** `derived_stats §1` asserts a universal multiplier formula; §4.1 gives Health as `(End+6) × (MW+1)` — a non-linear formula with a wound-count factor, not a multiplier. The rule's exception is bigger than the rule. **NERS: Elegant.** Source: `derived_stats_v30.md` §1 L14 vs §4.1.

### §4.2 Bottom-up: system mechanics → engine cohesion

| System | Honors TE-1? | Honors TE-2? | Honors TE-3? | Honors TE-4? |
|---|---|---|---|---|
| Combat | ✓ (wounds = −1D per PP-716) | ✓ (Agi) | ✓ | ✓ (PP-717) |
| Thread | ✓ | ✓ (Spi) | ✓ | ✗ |
| Contest | ✗ (Rattled = +Ob) | ✓ (Primary) | ✓ | ✗ |
| Fieldwork | ✓ | ✓ (per action) | ~ (Evidence is a clock, not derived) | ✗ |
| Mass Combat | ✓ (wound = −1D Command) | ✗ (pool uses Size AND Command) | ✓ | ~ (Command caps Size — DR-like) |
| Faction | n/a | ✓ (one stat per action) | ✓ | ✗ |
| Knot | ✓ | ✓ (Bonds) | ✓ | ✗ |

- **BU-1 · Mass Combat pool composition breaks TE-2.** `Pool = min(Size, Command) + Command` — uses two attributes. Defensible (unit + commander), but it is the only place TE-2 does not hold. Source: `params/mass_combat.md` L77.
- **BU-2 · Contest Rattled mechanic breaks TE-1.** Rattled adds Ob from actor state breakdown. Could be re-cast as Pool penalty (−1D/Rattled level) to honor PP-716 fully.
- **BU-3 · Mass Combat already has a DR-like structure.** Pool capping at `min(Size, Command) + Command` means Size above Command stops contributing — a form of DR. TE-4 is honored at unit scale via a different mechanism than at personal scale.

### §4.3 Lateral: peer systems consistency

| Function | Combat | Thread | Contest | Fieldwork | Note |
|---|---|---|---|---|---|
| Pool formula | `min(Agi,4)×2 + max(0,Agi−4) + H + 3` | `(Spi×2) + H + TPS` | `(Pri×2) + H + 3 + style` | `(Pri×2) + H + 3` | Combat alone has DR; Thread alone has track-based constant |
| Action economy resource | Stamina | Thread Fatigue | Concentration | (Cover, scenes) | Three different multipliers; one counts up |
| Survival resource | Health | Coherence | Composure | (Cover decay) | Three different formulas, three different directions |
| Wound/strain penalty | −1D / wound | −1D / wound | +1 Ob / Rattled level | −1D / wound | Contest is the outlier |
| Default TN | 7 (weapon-modified 5–8) | 7 (8/9 for some ops) | 7 | 7 | TN-as-difficulty in combat; Ob-as-difficulty elsewhere |

- **L-1 · Combat is the only personal-scale system with DR pool.** (Carries v27 P3 / engine-level F3.)
- **L-2 · Thread uses TPS as pool constant; everyone else uses +3.** Defensible; structural difference imposes cognitive load.
- **L-3 · Combat uses TN-as-difficulty (weapon TN 5–8); others use Ob-as-difficulty (TN locked at 7).** Two parallel difficulty channels with overlapping function.

### §4.4 Vertical: cross-scale consistency

| Scale | Pool | Default Ob | Resource pool basis | Direction |
|---|---|---|---|---|
| Personal | `Attr×2 + H + K` (5–17D typical) | 1–13 | Attr × small multiplier (3, 5, 10ish) | Drain |
| Unit (mass combat) | `min(Size, Command) + Command` (2–14D typical) | 1–3 | Size × block_size (10–5000) | Drain |
| Settlement | (pending) | (pending) | Prosperity × 50, Defense × 20 + Fort × 30 | (pending) |
| Faction | `Stat` bare (1–7D) | 1–4 | Stat × large multiplier (10–100) | Drain (mostly) |
| Peninsula (world clocks) | n/a | n/a | 0–100 ranges (MS, CI, IP) | Mixed |

- **V-1 · Pool sizes drop as scale rises.** Personal: ~17D max. Unit: ~14D. Faction: 7D. Same 1–7 attribute scale produces wildly different dice pool sizes across scales.
- **V-2 · Resource multipliers do not scale predictably with frequency.** §3 Multiplier Tiers describes the calibration intent but does not formalize it.
- **V-3 · Settlement layer is a hole.** `derived_stats §9` is `(PENDING)`.

### §4.5 Diagonal: cross-system × cross-scale chains

**Strongest chain:** Personal combat → Settlement defense → Faction derived value. Per `derived_stats §10.4`: closed loop, well-typed.

**Weak chain:** Personal social contest → political Disposition → faction Reputation. Slow propagation (next-season income), no fast-track.

- **D-1 · Fast/slow asymmetry undocumented.** Combat outcomes propagate fast; social outcomes propagate slow. Both correct for fiction; asymmetry not surfaced.
- **D-2 · Thread operations bypass cross-scale chains.** Globally consequential (peninsula clocks), locally invisible (no Disposition/Reputation shift).
- **D-3 · Inspiration documented in `derived_stats §5.3` but missing from §14 Complete Map.**

### §4.6 Horizontal: timescale consistency

| Timescale | What changes | Engine layer responding |
|---|---|---|
| Per-action | Pool penalties, Ob mods, Momentum spend | Pool, Ob, Momentum |
| Per-scene | Composure/Concentration deplete; Rattled accumulates; Saturation Counter resets | Derived values |
| Per-session | Momentum resets; Inspiration scene engagement; Disposition shifts | Tracks, Momentum |
| Per-arc | Certainty drift; TS growth; Coherence loss | Tracks |
| Per-campaign | MS baseline decay (−1/year); CI/IP movements; PT propagation | Peninsula clocks |

- **H-1 · Momentum reset is session-level.** Defensible but rationale unstated.
- **H-2 · MS baseline decay fires at Year-End only.** Engine_audit_2026-04-18 G-RS-01 flagged sim implementation as probabilistic — sim drift, not engine-design defect.
- **H-3 · Wound recovery binary at session end.** Carries within session, vanishes between sessions.

---

## §5 Consolidated inconsistency map

| # | Finding | Severity | NERS axis | Source |
|---|---|---|---|---|
| TD-1 | "No change to dice engine" violated by PP-717 DR | P2 | Smooth | `derived_stats §1` vs `params/combat L14` |
| TD-2 | `Attr × multiplier` rule broken by Health formula | P2 | Elegant | `derived_stats §1` vs §4.1 |
| F1 | `params/core L121` stale Vitality formula | P1 | Smooth | `params/core L121` vs `derived_stats §4.1` |
| F2 | `params/contest L107, L254` stale Concentration formula | P1 | Smooth | `params/contest` vs `derived_stats §5.2` |
| F4 | `derived_stats §3 + §14` still names Vitality | P2 | Smooth | internal to `derived_stats_v30.md` |
| F5 | `derived_stats §14` missing Intel; uses pre-PP-686 Mandate | P2 | Robust | `derived_stats §14` vs `stats_1_7_scale L3` |
| F7 | Coherence taxonomy conflict (derived vs track) | P2 | Elegant | `params/core L127` vs `derived_stats §6` |
| BU-1 | Mass Combat pool uses two attributes (breaks TE-2) | P3 | Elegant | `params/mass_combat L77` |
| BU-2 | Contest Rattled = +Ob breaks TE-1 channel separation | P3 | Smooth | `params/contest L111` vs PP-716 |
| L-1/F3 | Combat alone has DR pool (PP-717) | P2 | Smooth | `params/combat L14` vs peers |
| L-2 | Thread uses TPS as pool constant; others use +3 | P3 | Smooth | `params/threadwork L20` |
| L-3 | Combat uses TN-as-difficulty; others use Ob-as-difficulty | P3 | Elegant | `params/combat L24` vs others |
| V-1/F6 | Pool size shock across scales (17D→7D) | P2 | Smooth | `params/combat L14` vs `stats_1_7_scale L60` |
| V-2/F9 | Multiplier rationale not formalized | P3 | Elegant | `derived_stats §3` |
| V-3 | Settlement scale (pending) | P2 | Robust | `derived_stats §9` |
| D-1 | Fast/slow propagation asymmetry undocumented | P3 | Smooth | cross-system |
| D-2 | Thread cross-scale loop globally consequential but locally invisible | P3 | Robust | Thread + peninsula |
| D-3/F11 | Inspiration not in §14 derived map | P3 | Smooth | `derived_stats §5.3` vs §14 |
| H-3 | Session-boundary wound clearance — design weight | P3 | Robust | `params/combat L219` |
| F8 | Mass Combat pool shape distinct (no ×2, no H) | P2 | Smooth | `params/mass_combat L77` |
| F10 | Four directional state models (drain/up/ceiling/countdown) | P3 | Smooth | UI/legibility |

**Distribution:** 2 P1 (propagation defects), 8 P2 (architectural inconsistencies), 11 P3 (polish + design clarity).

---

## §6 Unification proposals

All proposals framed as options for Jordan's call.

### U-1 · Propagate PP-716/PP-717 to all stale files
**Targets:** `params/core L121` (Vitality → Health), `params/contest L107, L254` (Concentration formula), `derived_stats §3, §14` (rename Vitality, fix multiplier table).
**Effect:** closes F1, F2, F4. **Status: pure propagation; no design call.**

### U-2 · Decide on lateral DR propagation (TE-4 unification)
**Three options:** (a) propagate DR to Thread/Contest/Fieldwork; (b) document combat-only DR as intentional asymmetry; (c) revert PP-717 DR. **Needs design call.**

### U-3 · Convert Rattled from +Ob to −1D (TE-1 unification)
**Currently:** Rattled = +1 Ob per level. **Proposal:** Rattled = −1D Argue pool per level. Honors PP-716 channel separation fully. **Needs design call** — semantic shift from "the room is harder" to "I'm flustered."

### U-4 · Formalize the multiplier derivation
Document in `derived_stats §3` a formula relating interaction frequency to multiplier. **Needs design call** — could be light note rather than forced unification.

### U-5 · Clean up taxonomy: Derived Values vs Tracks vs Clocks vs Counters
Rewrite `params/core §Derived Scores` and `derived_stats §14` to use a single 4-bucket taxonomy:
- **Derived Values:** `Stat × multiplier`, actor state, drains/refills.
- **Tracks:** bounded oscillating counters representing relationship/character state.
- **Clocks:** world/scene progress, mostly monotonic.
- **Pools:** dice pools.

Closes F7 / D-3 / part of F10. **Needs design call** — ripples through tooltips, char sheets, vocabulary.

### U-6 · Decide TN-vs-Ob convention (L-3 unification)
(a) TN always circumstance; weapon difficulty becomes Ob. (b) Accept dual-channel; document the distinction. **Needs design call.**

### U-7 · Replace "counts up" Thread Fatigue with "Energy remaining" (F10)
UI-only change. **Needs design call** — minor.

### U-8 · Document settlement-scale interaction rules (V-3 closure)
Complete `derived_stats §9`. **Depends on settlement-layer design completion.**

### U-9 · Document fast-vs-slow propagation asymmetry (D-1 closure)
Tooltip-level documentation in `derived_stats §10`. **Light touch.**

---

## §7 Suggested next actions

**Immediate, no design call needed:**
1. **U-1** — propagate PP-716/PP-717 to stale files. Closes F1, F2, F4. Single commit.

**Needs Jordan call (sequenced by impact):**
2. **U-2** — DR lateral decision.
3. **U-5** — taxonomy cleanup.
4. **U-3** — Rattled channel reassignment.
5. **U-6** — TN-vs-Ob convention.

**Defer:**
6. **U-8** — settlement scale completion.
7. **U-4, U-7, U-9** — documentation polish.

The engine's architecture is sound; inconsistencies are concentrated in (a) recent revisions not yet propagated and (b) one or two design-asymmetry decisions still to be made.
