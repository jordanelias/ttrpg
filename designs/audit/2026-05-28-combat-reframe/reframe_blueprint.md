# Combat v31 — Reframe Blueprint

**Purpose:** restructure combat_v31 around Jordan's top-down vision (2026-05-28): a **probability-weighted state graph** with **front-end strategy** (weapon / school / loadout / setup), where the **bout is the 6–10s engagement round** that resolves and disengages, and **facing direction sets field of view**. This blueprint specifies the new models concretely; the proposal revision (subsequent turns) implements them.

**What this reframe resolves:** the diagnostic's central tension (combat_v31 at the expressive-R-maximal corner, failing E and correctness-R). The vision dissolves it on two axes — see §2.

---

## 1. The state-graph model (the container)

Combat is a **probability-weighted state graph**. Combat alternates between two tiers:

### 1.1 Setup tier (deterministic player choice — the front-end strategy)

Between engagements the fighter is at **Measure** (out of contact). Here the player constructs their approach through deterministic choices under uncertainty about the opponent:

- **Stance** (§6.1) — sets perception bias, available reactions, Signal
- **Position** (§4.3) — sets commit options, Signal
- **Approach** (§4.4) — *one opposed roll* determines bout-entry state (Out-of-contact vs Closing) and relative facing
- **Reading peak** (§4.5) — sets the modifiers carried into the bout (gated by perception, §4)
- **Commit** (§4.6) — chooses action class + depth, which weights the bout's opening transition

These map to current phases 1–5. They are **choices, not random** — the player's strategic layer.

### 1.2 Bout tier (probabilistic state subgraph — the 6–10s engagement)

The **bout** is the engagement round: a probability-weighted traversal of engagement states, ~6–10 seconds in-fiction, ending in disengagement or a terminal outcome.

```
            ┌──────────────┐
   enter →  │ Out-of-contact│ ──probe/close──┐
            └──────┬───────┘                 │
                   │                          ▼
            ┌──────▼───────┐         ┌────────────────┐
            │   Closing    │ ◄─────► │    In-bind     │
            └──────┬───────┘         └───────┬────────┘
                   │                         │
                   └────────► Breaking ◄─────┘
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                    ▼
        [Disengaged]         [Wounded]            [Felled]
         → Setup           → continue or         → terminal
                            → Breaking
```

**Transition probabilities** at each bout state are set by opposed Pool rolls, weighted by:
- **stats** → Pool size (Agi/Str × 2 + History + proficiency)
- **equipment** → weapon modifiers (TN, damage, phase-strength, handling §5)
- **choices** → sub-action selection + setup-derived modifiers (state-gated, §4 below)
- **chance** → the dice

This is *exactly* the vision's "effectiveness influenced by stats, equipment, interactions between choices and chance." The bout is where setup choices resolve probabilistically.

**Player intervention** during the bout fires only at decision nodes (opponent depth crosses threshold, bind-state transition, perception reveal, resource-critical, Thread-available — current §4.7 triggers). Otherwise the **Conditional Logic Profile** auto-resolves transitions. This keeps in-bout per-moment load low.

### 1.3 Phase regrouping

The eight phases survive but regroup under the state-graph frame:

| Old phase | New role |
|---|---|
| 1 Stance / 2 Position / 3 Approach / 4 Reading / 5 Commit | **SETUP tier** (deterministic choice) |
| 6 Bout | **BOUT tier** (probabilistic subgraph) |
| 7 Disengage / 8 Return | **RESET** (back to Setup/Measure, with recovery) |

One **round of engagement** = one SETUP → BOUT → RESET cycle. The bout is the 6–10s engagement.

---

## 2. Front-end strategy principle (resolves F6 + correctness-R)

**Strategic depth is front-loaded; the bout resolves probabilistically.**

The diagnostic found combat_v31 failing E (too complex per-moment) and correctness-R (uncapped modifier stacking). The vision resolves both:

- **E resolution:** complexity lives in *setup* (weapon choice, school training, skill loadout, stance/approach/reading/commit) — where the player *wants* to think. The *bout* resolves that setup probabilistically with low per-moment load (CLP auto-resolution + intervention only at key nodes). Complexity front-loaded into build/loadout is E-acceptable; complexity smeared across in-bout micromanagement is not. The reframe moves it to the right place.
- **Correctness-R resolution:** in a state graph, modifiers attach to *states and transitions*, not globally. State-gating (Lever B) becomes structural — each bout state's transitions use only that state's relevant modifiers. This bounds F2 (compound Ob stacking) at the source: fewer modifiers are ever simultaneously live.

**Design consequence:** the per-state decision is small (a handful of sub-actions, a handful of live modifiers), even though the *system* is large. Depth is in the front-end; resolution is clean.

---

## 3. Timescale recalibration

| Unit | In-fiction time | Content |
|---|---|---|
| **Setup** | ~2–4s (maneuvering to measure) | deterministic choices; player decision-time is here but in-fiction it's brief |
| **Bout** | **6–10s** | the engagement round — probabilistic state traversal |
| **Reset/Disengage** | ~1–2s | separation, recovery |
| **Round of engagement** | ~10–15s | one full Setup→Bout→Reset cycle |

Change from current proposal: the proposal labels the *pass* at 15–30s. The bout is the 6–10s engagement (matches vision); the full cycle is ~10–15s in-fiction. Recalibrate §4.1.

---

## 4. Perception system: facing direction → field of view

**The clarified mechanic (Jordan):** the direction a fighter faces sets their field of view; field of view gates what they can perceive, read, and react to.

### 4.1 Field of view from facing

Each fighter has a **facing** (relative angle to opponent). Facing defines a **field of view (FoV)** with a perception factor by the opponent's angular position:

| Opponent's position relative to your facing | Angle off-axis | FoV factor | Maps to §11.2 facing |
|---|---|---|---|
| Central cone | 0–45° | 1.0 (full) | Square |
| Near-peripheral | 45–90° | 0.6 (degraded) | Quarter |
| Far-peripheral | 90–135° | 0.3 (poor) | Flank |
| Blind rear | 135–180° | 0.0 (none) | Rear |

### 4.2 What FoV gates

**Reading** (perception of opponent X): `effective Reading Pool = base Reading Pool × FoV-factor(angle to X)`, then resolved vs X's Signal Level. FoV gates *whether* you can read; Signal sets *how hard*. Verified: a 12D Reading pool becomes 12 / 7.2 / 3.6 / 0 at Square/Quarter/Flank/Rear.

**Reactions** (in-bout defense): gated by FoV threshold —
- FoV ≥ 0.6 (central/near): all reactions available
- FoV 0.3 (far-peripheral): only fast/contact reactions (Hand-led, Pressing); **lose Body-led, Yielding, Voiding** — these need to *see* the commit develop
- FoV 0.0 (blind): no visual reaction; only Hand-led at penalty, and only if already in a tactile bind

This reproduces §11.2's reaction restrictions (Flank loses Body-led/Yielding/Voiding; Rear only Hand-led at penalty) — now *grounded* in perception, not authored.

### 4.3 Facing Ob modifiers become EMERGENT (a derive-from-primitives win)

**The proposal no longer carries authored Facing Ob modifiers.** The aggressor's advantage from flanking *emerges* from two compounding effects on the defender:
1. **Lost Reading** → defender doesn't read the aggressor → loses the defensive Reading-modifier they'd otherwise gain
2. **Lost reactions** → defender's reaction sub-action Pool is reduced/unavailable

These compound. At Square both are full (no advantage, 0 Ob). At Rear both are gone — lost read-bonus + lost reaction — compounding **super-linearly** to ~−2 aggressor Ob (verified: a linear FoV→Ob model gives −1.5 at Rear, but the compound lost-read + lost-reaction reaches the −2 the current table specifies). The §11.2 table becomes a **"typical emergent values" reference**, not a primitive.

This is the opposite of the Stance Counter result (Piece 1): Facing *does* derive cleanly from one mechanic (perception), because the facing penalty has a single physical cause (you can't see the attack). Stance Counter resisted because its hard counters are independent design choices.

### 4.4 The spatial tactical loop

- **Footwork** (Curvilinear, Triangular, Drawing) changes your facing → reorients your FoV
- **Approach angles** (Angled approach) change relative facing → can place you in the opponent's periphery while keeping them in your central cone
- **Core loop:** maneuver to keep the opponent in *your* FoV (so you read them) while getting into *their* periphery/blind (so they can't read you). Winning the perceptual-positioning battle → Reading advantage → transition-probability advantage in the bout.

This integrates the vision's cluster — **footwork + field-of-view + angles/directions + reading/anticipation** — into one spatial-perceptual system. Intent Reading (§10) operates within FoV like other channels (you cannot read the intent of someone you cannot see).

---

## 5. Weapon ease-of-use (handling)

Each weapon class gains a **handling rating** shaping the proficiency→effectiveness curve. This is the vision's "ease of use" dimension (beyond the existing STR-min gate).

| Handling | Weapon-contribution to Pool (by Aspect Proficiency P) | Character |
|---|---|---|
| **Forgiving** | `min(P + 1, 3)` | competent immediately, low ceiling (spear, short sword) |
| **Standard** | `min(P, 4)` | linear (longsword) |
| **Demanding** | `max(P − 1, 0)`, reaches 5 at P=6 | punishing at low skill, high ceiling (rapier, paired short) |

Crossover ~P=4: below it, forgiving weapons outperform; above it, demanding weapons pull ahead. (At P=2: Forgiving 3 > Standard 2 > Demanding 1. At P=6: Demanding 5 > Standard 4 > Forgiving 3.)

**Front-end consequence:** a build choice — pick an easy weapon for immediate competence and a lower skill ceiling, or invest in a demanding weapon for higher mastery payoff. Pairs with school training (a demanding weapon in a school that teaches it well mitigates the floor penalty).

Provisional handling assignments: Long thrust-primary = Demanding; Curved cut-primary = Standard; Long cut-and-thrust = Standard; Long pole = Forgiving; Paired short = Demanding; Single short = Forgiving. (Sim-tunable.)

---

## 6. Equip-skills loadout + named sets

The vision's "learn skills from each school, equip across schools, set bonuses" becomes an explicit **loadout layer** — replacing the implicit aspect-pair coherence math with a legible front-end system. This folds Piece 1's coherence result (clusters + exceptions).

### 6.1 Trained pool vs equipped loadout

- **Trained pool:** every aspect specialization + technique the character has learned across all their schools (Traditions). Grows through play.
- **Equipped loadout:** the active subset brought to a fight. Structure: 1 Stance, 1 primary Footwork, Grip (weapon-constrained), 1 each of Approach/Reading/Anticipation/Reaction/Commitment/Disengage emphasis, + a slate of equipped techniques (slot-budgeted).
- The player **re-equips between fights** (front-end strategy) but not mid-bout.

### 6.2 Named sets (from Piece 1 coherence clusters)

Piece 1 showed the 36-pair coherence matrix reduces to **2–3 synergistic clusters + a short exception list**. These clusters become **named equippable sets** with set bonuses when fully equipped:

| Set (cluster from Piece 1) | Components | Set bonus (draft) |
|---|---|---|
| **Thrust Duelist** | Forward-point + Linear + Standard grip + Direct/Explosive + Temporal + Decisive + Clean | +0.5D to thrust-class bout transitions when ≥4/5 equipped; +1D at full |
| **Bind Fighter** | Centered/Raised + Half-grip + Tactile + Patterned + Yielding + Sustained + Defensive | +0.5D to in-bind sub-actions when ≥4 equipped; +1D at full |
| **Counter-time** | Centered/Side + Linear + Drawing + Temporal/Biomechanical + Reactive + Hand-led + Defensive | +0.5D to counter sub-actions on successful Reading; +1D at full |
| **Burst** | Bursting + Explosive + Burst + Sudden | +0.5D to opening commit; −cost on Explosive close |
| **Continuous-flow** | Side + Triangular + Paired + Angled + Rhythmic + Voiding + Sustained | +0.5D to flow sub-actions across multi-pass bouts |

The set bonus = legible front-end reward for a coherent loadout. The player sees "Thrust Duelist 4/5 — equip Clean Disengage to complete" rather than computing aspect-pair coherence.

### 6.3 Incompatibilities (the rare antagonisms)

Piece 1's 2 antagonistic pairs become explicit **loadout incompatibility warnings**:
- **Anticipation×Reaction** clash: equipping Predictive Anticipation + Reactive Reaction → −0.5D when both fire (contradictory mental model)
- **Commitment×Disengage** clash: Burst Commitment + Defensive Disengage → −0.5D (mismatched intensity)

The loadout UI flags these so the player chooses awkward builds knowingly.

---

## 7. How Pieces 1 & 2 fold into the reframe

| Piece | Result | Home in reframe |
|---|---|---|
| **1 Reaction matrix** | 2 params/reaction (baseline + depth-slope) | §7.2 → formula; reaction effectiveness vs commit-depth, applied at bout transitions |
| **1 Aspect coherence** | clusters + exceptions | §6.2 named sets (loadout layer) |
| **1 Stance Counter** | resists derivation; keep authored | §7.1 authored table, **state-gated** (applies only at Closing-state opening, not every sub-action) |
| **1 Facing** | derives from perception (this turn) | §4.3 emergent from FoV; remove authored Facing Ob table |
| **2 σ-space modifiers** | (next turn) | bout transition probabilities computed in σ-space for uniform impact |
| **2 soft cap** | (next turn) | saturating cap on per-transition modifier sum |
| **2 state-gating** | (next turn) | each bout state surfaces only its relevant modifiers — *native to the state graph* |

The reframe is the **container** that makes Piece 2 natural: σ-space + soft-cap + state-gating all attach to bout-state transitions, which the state graph now defines explicitly.

---

## 8. Cross-scale / cross-scope notes (per the all-scales directive)

- **Mass combat:** the perception=facing principle extends conceptually to units (unit facing → unit perceptual arc → flanking advantage). Mass combat already has flanking; the reframe makes personal and mass perception *consistent in principle* (both: facing gates perception gates reaction). Personal bout state-graph does NOT replace mass-combat resolution (canonical Martial/Discipline) — they remain distinct engines linked at transitions (§15.2 preserved).
- **Social contest:** the loadout layer is personal-combat-specific. Concentration shared-pool (F3) is unaffected by the reframe; handled separately (I-15 sim). Social contest could *optionally* adopt a parallel perception/loadout model later, but out of scope here.
- **Scope completeness:** the reframe touches personal-scale combat fully (engine framing, perception, weapons, loadout). It does not alter Thread integration (§14), World Bridge (§15.1), or mass combat (§15.2) beyond the consistency note above.

---

## 9. Implementation map + sequencing

### 9.1 Proposal sections that change

| Section | Change |
|---|---|
| §0 Disposition | Add state-graph framing + front-end-strategy principle |
| §1 Pillars | Revise Pillar 1 (loop → state graph); add Perception pillar; sharpen front-end-strategy pillar |
| §4 (engine) | Reframe as SETUP(1–5) → BOUT subgraph(6) → RESET(7–8); recalibrate timescale; bout as probability-weighted state graph |
| §5 / §6 | Add trained-pool vs equipped-loadout layer; aspects become trained + equipped |
| §6.2 (new) | Named sets (loadout); incompatibilities |
| §7.1 Stance Counter | Keep authored; mark state-gated (Closing-opening only) |
| §7.2 Reaction | Replace table with 2-param formula |
| §7.3 Coherence | Replace 36-pair matrix with named-set reference + exceptions |
| §8 Weapons | Add handling (ease-of-use) dimension + curves |
| §10 Intent | Note Intent reads within FoV (perception-gated) |
| §11.2 Facing | Replace with perception/FoV system; Facing Ob modifiers become emergent |
| §11 (new var) | Perception field as a derived state (facing → FoV) |
| §12.3 Ob composition | σ-space + soft-cap + state-gating (Piece 2) |

### 9.2 Sequencing (proposed)

1. **This turn:** blueprint (done)
2. **Next:** Piece 2 — σ-space + soft-cap + state-gating concrete spec, now that the bout subgraph (its container) is defined
3. **Then:** implement the full revision into the proposal — multi-turn, section by section per §9.1, folding Pieces 1 & 2 and this blueprint
4. **Then:** full review — triple-pass + directional NERS (all directions/scales/scopes) on the revised proposal
5. **Then:** re-run the resolution diagnostic on the reframed system to confirm the F-findings are resolved (F2 by state-gating + soft-cap; F6 by front-loading + loadout legibility + derivations; F1 by σ-space; F4 by definition; F7 by Reading consolidation; Facing now emergent)

---

## Verification log (this turn)

- Facing→FoV→Ob grounding tested: linear model fits Square/Quarter/Flank; Rear is super-linear (−2 vs linear −1.5), correctly emergent from compounding lost-read + lost-reaction. `[CONFIDENCE: high — numerically checked]`
- Weapon handling crossover verified: Forgiving > Standard > Demanding at low P; reverses above P≈4. `[CONFIDENCE: high]`
- Named sets sourced from Piece 1 coherence clusters (validated 86–92% reducible). `[CONFIDENCE: medium — cluster membership is interpretive; set-bonus magnitudes draft, sim-tunable]`
- `[SELF-AUTHORED — bias risk: this blueprint reframes my own proposal toward Jordan's vision; the perception-derives-Facing claim is the one new derive-from-primitives result and it was numerically checked, unlike the Stance Counter claim which I let fail]`
