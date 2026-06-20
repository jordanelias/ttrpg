<!-- [DEPRECATED: 2026-06-19 — superseded by canonical combat_engine_v1; not canon, will not be ratified. Per Jordan ratification 2026-06-19 (ratification decision #17). Retained for historical reference only.] -->
<!-- PROPOSAL — PP-TBD; supersedes designs/scene/combat_v30.md §§1–4 on ratification -->
<!-- Source: combat_v31_proposal.md reframed per Jordan top-down vision (2026-05-28) -->
<!-- Architecture: engine replacement within d10/TN/Ob substrate; combat as probability-weighted state graph -->
<!-- Status: PROPOSAL — not canonical until editorial ratification -->

# VALORIA — Combat System Rewrite (Proposal)

## Date: 2026-05-28
## Version: combat_v32_proposal v1.0 (state-graph reframe of v31)
## Status: DEPRECATED (2026-06-19) — superseded by canonical combat_engine_v1; will NOT be ratified (Jordan ratification 2026-06-19)
## Scope: Personal-scale combat engine. Mass combat, Thread-in-combat (combat_v30 §10), Combat World Bridge (combat_v30 §13), Fieldwork transitions (combat_v30 §11.5) preserved by reference.
## Mode applicability: VIDEOGAME (Godot). Per VGMS §4, TTRPG-only mode struck — single mode in this proposal.
## Authority: canon/00_philosophical_foundations_rules.md → canon/02_canon_constraints.md → designs/architecture/videogame_mode_spec.md → this document → params/combat.md (pending refresh)
## Cross-references: params/core.md (attributes, dice engine, derived stats); designs/scene/derived_stats_v30.md (Health, Stamina, Concentration authoritative); designs/architecture/player_agency_v30.md (Convictions, Duties); designs/scene/combat_v30.md §§10, 13 (Thread, World Bridge); designs/scene/threadwork_v30.md (Thread operations); params/threadwork.md (TS, TPS, Thread Pool).
## Reframe basis: designs/audit/2026-05-28-combat-reframe/ — reframe_blueprint.md (state-graph + front-end-strategy + perception/FoV + weapon handling + equip-loadout), modifier_system_spec.md (σ-space + soft-cap + state-gating, F1/F2 fix), matchup_derivation_analysis.md (Reaction→params, coherence→sets, Stance Counter authored), derived_stats_audit.md (Command derivation, attribute-weight standard). Diagnostic: designs/audit/2026-05-28-resolution-diagnostic/.

---

## 0. DISPOSITION

This proposal **replaces** the canonical combat engine (combat_v30 §§1–4: Combat Pool framing, Round Structure, Initiative, Actions) with a **probability-weighted state graph**. The d10/TN/Ob resolution substrate (params/core.md continuous engine, PP-717 fractional Ob/TN) is **preserved and load-bearing** — all state transitions, sub-action resolutions, and matchup modifiers operate within canonical Pool/TN/Ob/degree grammar.

**The core model (v32 reframe).** Combat alternates between two tiers:
- **Setup tier** — deterministic player choice under uncertainty about the opponent: weapon and equipped skill loadout (front-end), then per-engagement stance, position, approach, reading, and commit. This is where strategic depth lives.
- **Bout tier** — a probability-weighted subgraph (states: out-of-contact / closing / in-bind / breaking → wounded / disengaged / felled), ~6–10 seconds, where the setup choices resolve. Transition probabilities are weighted by **stats** (Pool), **equipment** (weapon modifiers), **choices** (state-gated modifiers), and **chance** (dice).

One **round of engagement** = one Setup → Bout → Reset cycle; the bout is the 6–10s engagement that ends disengaged. The eight phases of v31 survive, regrouped as **SETUP (1–5) → BOUT (6) → RESET (7–8)** — see §4.

**Why the reframe.** v31 (the predecessor proposal, now checkpointed at designs/proposals/combat_v31_proposal.md) was diagnosed NON-COMPLIANT: it sat at the "expressive-R-maximal corner," failing Elegance (too much per-moment in-bout complexity) and correctness-Robustness (compound modifier stacking foreclosed outcomes at small Pool). The state-graph + front-end-strategy framing resolves both: complexity is **front-loaded into setup** (E-acceptable — players want depth there), and modifiers attach to **states** (correctness-R — state-gating bounds compound stacking). See designs/audit/2026-05-28-resolution-diagnostic and the reframe_blueprint.

**Preserved unchanged from canon:**
- 10-attribute character (Agi, End, Str, Cog, Rec, Foc, Att, Bon, Cha, Spi), 31-point creation, range 1–7
- Histories as progression backbone (audit principle #4: Histories not Skills; Recall caps History points)
- d10/TN/Ob resolution (continuous engine, fractional Ob/TN per PP-717)
- Health, Wound Interval, Max Wounds (per derived_stats §4.1, PP-716)
- Stamina = Endurance × 5 (per derived_stats §4.2, ED-694; action costs reweighted for the state graph)
- Coherence 10→0 with PP-261 NPC transition at 0; Coherence drift per P-10/P-12/P-15
- TS gates 30/50/70/90; Thread Pool = (Spirit × 2) + History + TPS per params/threadwork PP-616
- Convictions (3 player-authored statements, strain mechanic) per player_agency §2
- Duties (8 institutional types, Standing 0–7) per player_agency §3
- Combat World Bridge (combat_v30 §13): Domain Echo, Reputation Cascade, Settlement Consequences, Death Cascade
- Thread in Combat (combat_v30 §10): wound penalty propagation, TS-gated perception, cross-system fire

**Extended / added (v32):**
- Probability-weighted state-graph engine (replaces canonical action priority resolution)
- **Front-end strategy layer:** trained skill pool + equipped loadout with named set bonuses (§5–6)
- **Perception system:** facing direction sets field of view, which gates Reading and reactions (§4, §11) — Facing Ob modifiers become emergent, not authored
- **σ-space modifier system** with soft cap and state-gating (§12.3) — resolves v31's F1 (non-uniform impact) and F2 (compound foreclosure)
- **Weapon handling** (ease-of-use): per-weapon proficiency curve (§8)
- Combat Concentration as parallel mental resource (uses canonical Focus attribute)
- Reading sub-channels (consolidated set + Thread + Intent track) — combat sensory layer
- Intent Reading track (Tier 0–5 with specific abilities)

**Recalculated:**
- Combat resource economy: Stamina/Concentration drain rates for the state graph
- Wound display layer: 3 perceptual states over canonical 4-wound math (UI compression)

**Cut / superseded:**
- Canonical action priority resolution (Strike=1, Feint=2, etc. per combat_v30 §4) — replaced by state-gated sub-action option sets
- Canonical Round Structure (combat_v30 §2) — replaced by §4 state graph
- Strike as primary action — collapses into Bout sub-action chain (§4.6)
- Canonical Concentration as social-only — extended to combat
- **Authored Facing Ob modifiers** — replaced by emergent perception consequences (§4, §11.2)
- **Standalone matchup tables where derivable** — Reaction-aspect → 2-parameter formula; Aspect coherence → named loadout sets + exceptions (Stance Counter retained as authored, per matchup_derivation_analysis)

**Editorial ledger entries needed on ratification** (named here, drafted Pass 2c):
- Supersession of combat_v30 §§1–4
- New canonical combat engine ratification (state-graph model)
- Concentration combat extension; σ-space modifier methodology (combat-internal)
- Cross-system propagation: mass_battle_v30 Bout integration, fieldwork_v30 transition update, social_contest interaction (Concentration shared pool)

---

## 1. DESIGN PILLARS

Eight commitments. Where a design choice conflicts with a pillar, the pillar wins.

**Pillar 1 — Combat is a probability-weighted state graph.** Combat is a traversal of combat states; transitions carry probabilities weighted by stats, equipment, choices, and chance. The setup tier (stance/position/approach/reading/commit) is deterministic choice; the bout tier (out-of-contact / closing / in-bind / breaking → terminal) is the probabilistic subgraph. This replaces canonical "declare-and-resolve action priority." Single-action mechanics (Disarm, Tie Up, etc.) survive as bout sub-actions, not round-level alternatives.

**Pillar 2 — Strategic depth is front-loaded; the bout resolves probabilistically.** The player's strategy lives in *setup* — weapon choice (techniques/grip/distance/speed/handling), school training, equipped skill loadout with set bonuses, and per-engagement stance/approach/reading/commit. The *bout* resolves that setup with low per-moment decision load (Conditional Logic Profile auto-resolves; the player intervenes only at decision nodes). Complexity front-loaded into build/loadout is the source of depth *and* keeps the in-bout experience clean. This pillar is the v32 answer to v31's Elegance failure.

**Pillar 3 — The bout is the engagement round (~6–10s) and ends disengaged.** One round of engagement = one Setup → Bout → Reset cycle. The Bout (Phase 6) is the substantive resolution — a sub-action chain producing wounds, displacement, bind transitions, and termination. There is no separate "Strike"; what was canonical Strike is a depth-keyed Commit (Phase 5) that initiates the bout. The bout resolves to a terminal state (wounded / disengaged / felled) within ~6–10 seconds in-fiction.

**Pillar 4 — Two resource economies: physical and mental.** Stamina (Endurance × 5, canonical) is the physical reservoir; Combat Concentration (Focus × 3, combat extension; sim-tunable) is the mental reservoir. Both drain across the state graph (reading load, deep commits, sub-action chains, wound shock) and recover at Reset. Long fights become two-axis resource-management contests.

**Pillar 5 — Perception is facing-gated: the direction you face sets your field of view.** What a fighter can read, anticipate, and react to is bounded by their field of view, which is a function of facing direction (central cone / peripheral / blind rear). Reading Pool scales by the opponent's position in your FoV; reactions are gated by it. Positioning (footwork, approach angle) is the contest over who can perceive whom. The Facing Ob advantage is **emergent** from lost-reading + lost-reaction, not an authored modifier (§4, §11.2).

**Pillar 6 — Trained pool, equipped loadout; sets reward coherence.** A character trains aspect specializations and techniques across schools (Traditions) into a *trained pool*, then *equips* a subset as a combat loadout (re-equipped between fights, not mid-bout). Per-aspect Proficiency contributes to state-transition Pools. Coherent loadouts trigger named **set bonuses** (the synergistic clusters); a few cross-cluster combinations are flagged incompatible (§5–6). Aspect specializations remain sub-skills within Histories (audit principle #4); Recall caps History points.

**Pillar 7 — d10/TN/Ob with σ-space modifiers is the resolution substrate.** Every state transition operates within canonical params/core dice grammar. Modifiers are applied in **standard-deviation units (σ-space)** with a saturating soft cap and **state-gating** (only state-relevant modifiers are live per bout state). This delivers uniform modifier impact across Pool scale (resolves v31 F1) and bounds compound stacking (resolves v31 F2). σ-space is engine-internal; the player sees advantage *levels*, not σ (§12.3). Methodology may differ from other Valoria systems; attribute-weight equivalence is maintained per the σ-leverage standard (designs/audit/2026-05-28-combat-reframe/attribute_weight_standard.md).

**Pillar 8 — Constraints are mechanical, not flavor.** Honor codes (when present) filter the action space at specific states. Equipment forecloses options. Wound state forecloses options. Convictions modify available commit depths in specific contexts (cross-ref player_agency §3.5). Every constraint operates by removing or modifying decisions, not by adding narrative color.

---

## 2. CANONICAL SUBSTRATE CITED

This section enumerates canonical primitives the proposal builds on. The proposal does not restate canonical content; readers reference the canonical source.

### 2.1 Attributes (params/core.md §Attributes)

10 attributes, range 1–7, 31 points at creation, max 5 in any single attribute at creation:

| Group | Attributes |
|---|---|
| Physical | Agility (Agi), Endurance (End), Strength (Str) |
| Mental | Cognition (Cog), Recall (Rec), Focus (Foc) |
| Social | Attunement (Att), Bonds (Bon), Charisma (Cha) |
| Metaphysical | Spirit (Spi) |

**Combat-relevant attribute roles** (this proposal):
- **Agi**: Bout sub-action Pools (footwork, evasion, light strikes); approach Pool; disengage Pool
- **End**: Stamina_max, Wound Interval, Health
- **Str**: damage modifier, Bout grip/displacement sub-actions, heavy-strike commits
- **Cog**: Reading sub-channel Pools (Geometric, Intent); Anticipation
- **Rec**: caps History points per History (limits training depth)
- **Foc**: Concentration_max combat, sustained-commit duration, Intent Reading attention discipline
- **Att**: Reading sub-channel Pools (Tactile, Kinetic, Rhythmic, Thread); Initiative
- **Spi**: Thread-op commits in combat; Coherence interaction
- **Bon, Cha**: not combat-active by default; Bon factors into Death Cascade via Knot mechanics (combat_v30 §13.3 + threadwork Knot rules); Cha affects Composure (social fallback if combat de-escalates)

### 2.2 Dice engine (params/core.md §Die Rule, §Continuous Engine)

- d10 face rule: 1 = −1 success, 2–6 = 0, 7–9 = +1, 10 = +2; no chain
- TN values: 6 / 7 / 8 (controlled / standard / desperate)
- **Continuous engine canonical for Godot**: `net ~ Normal(μ·N, σ·√N)` with per-die statistics per TN
- **Fractional TN and Ob canonical** (PP-717 Fiore half-step TN ratified) — the σ-space modifier system (§12.3) resolves to Ob shifts on this fractional substrate
- Pool floor: 1D universal
- Degree of success: Failure (net ≤ 0) / Partial (0 < net < Ob) / Success (net ≥ Ob) / Overwhelming (net ≥ 2·Ob AND net ≥ 3)

### 2.3 Derived stats (derived_stats_v30.md §§4–6 authoritative)

| Stat | Formula | Range | Per |
|---|---|---|---|
| Health | `(End+6) × (MW+1)`; `MW = min(floor(End/2)+1, 3)`; WI = End+6 | 14–48 | §4.1 |
| Stamina | `Endurance × 5` | 5–35 | §4.2 |
| Concentration | `Focus × 3` (canonical: social contest only; **this proposal extends to combat — see §3.3**) | 3–21 | §5.2 |
| Composure | `Charisma × 3` | 3–21 | §5.1 (combat fallback if engagement de-escalates) |
| Thread Fatigue | `Spirit × 5` threshold (counts up) | 5–35 | §6.1 |
| Coherence | 10 → 0 countdown | 0–10 | params/core §Coherence; PP-261 NPC transition at 0 |

**Universal modifier:** −1D per Wound on all Pools (PP-716 / derived_stats §4.1).
**Wound clearance:** all wounds clear at session end (canonical).

### 2.4 Histories (audit principle #4)

Histories are the canonical character-progression backbone. Each History represents lived experience and grants point-based bonus to relevant Pools. Recall caps per-History points (`History points ≤ Recall`). Combat-relevant Histories include the Tradition catalog in §5.

### 2.5 Player agency (player_agency_v30.md §§2–3)

- **Convictions**: 3 player-authored worldview statements with strain mechanic (3 strains → transform/abandon). Drive scene generation, Momentum awards, Certainty shifts on resolution.
- **Duties**: 8 institutional types (Investigate / Diplomacy / Governance / Protection / Reconnaissance / Subversion / Thread Operation / Escort) assigned by faction leader per season. Advance Standing 0–7.
- **Duty vs Conviction tension** (player_agency §3.5) is the central player-decision tension; this proposal preserves it.

### 2.6 Thread and Coherence (canon/02 P-01, P-10, P-11, P-12, P-15)

- P-01 Inseparability: Thread operations produce three-dim co-movement. Applies in combat per combat_v30 §10.1 (Thread-op commits trigger full P-01 cascade)
- P-10, P-12, P-15: Coherence is layer-2 integrity; drifts under specific triggers; at Coherence 0, TS-gated branching (low-TS dissolution; high-TS forced layer-3 maintenance via Thread Fatigue cost)
- Thread perception in combat per combat_v30 §10.2 visibility table (TS 30+, 50+ thresholds)
- Cross-system fire from combat per combat_v30 §10.3 (Knot rupture on kill, Conviction Scar on witnesses, etc.)

---

## 3. PATCHES TO CANONICAL COMBAT_V30

This proposal supersedes combat_v30 §§1–4 in their entirety and patches three additional defects. Patches enter the editorial ledger on ratification.

### 3.1 P-C01 — Action declaration ambiguity (resolved by supersession)

**Canon issue:** combat_v30 §2 (Round Structure) declares actions "simultaneous, blind"; §3 (Initiative) says "lower initiative declares Offence/Defence split first, higher counter-declares." Contradiction.

**Resolution:** §§1–4 superseded by this proposal. The new engagement-loop has no Round Phase 3 simultaneous-blind action declaration. Phase-keyed commits (Phase 5) are sequenced by Initiative within each phase per §4 specification below.

### 3.2 P-C02 — First-round Initiative undefined (resolved)

**Canon issue:** combat_v30 §3 PP-232 covers subsequent rounds only.

**Resolution:** First-round Initiative = **`Att + Weapon Speed`**, where Weapon Speed is a per-weapon-class fractional value (see §6 weapon classes). Tiebreak: higher Cog, then higher Agi. Subsequent-round transfer preserved from canonical §3 (loop winner gains initiative).

**Weapon Speed values (draft, sim-tunable I-17):**
| Weapon class | Speed |
|---|---|
| Single short | +3 |
| Paired short | +2.5 |
| Curved cut-primary | +2 |
| Long thrust-primary | +1.5 |
| Long cut-and-thrust | +0.5 |
| Long pole | 0 |

### 3.3 P-C08 — Stunt mechanic adaptation (videogame)

**Canon issue:** combat_v30 §4 Stunt action: "Game Master sets N, max 5 dice."

**Resolution:** In videogame mode, Stunt opportunities are *Authored* per VGMS §3 ("GM Decides" Register). Scene metadata specifies environmental advantages available (e.g., elevation, terrain, lighting, props). Engine surfaces Stunt option during Phase 5 commit if scene-context supports it; Stunt magnitude (+N dice) is scene-authored.

### 3.4 P-C09 — Reach terminology unified

**Canon drift:** combat_v30 §5 (PP-268) uses "Melee range / Ranged distance"; params/core §Reach (PP-290) uses "Short Reach / Long Reach / Ranged."

**Resolution:** PP-290 wins. This proposal uses **Short Reach (≤1m) / Long Reach (≤3m) / Ranged** throughout. Editorial entry on ratification edits combat_v30 §5 to PP-290 vocabulary.

### 3.5 Concentration combat extension

**Canon issue:** derived_stats §5.2 specifies Concentration as social-contest resource only.

**Proposed extension:** Concentration formula `Focus × 3` is preserved. **Combat use is added** — Concentration drains during combat phases per §3.3 below. Social-contest Concentration mechanics (drain per exchange, Spent state) unchanged. The two use-contexts share a single pool: a character entering combat after a social contest carries reduced Concentration into combat.

This is the proposal's largest extension to canon outside the engine replacement. It requires editorial ratification.

---

## 4. THE ENGAGEMENT STATE GRAPH

This section replaces combat_v30 §§2–4 in their entirety.

### 4.1 Tier structure

Combat is a **probability-weighted state graph** traversed in **rounds of engagement**. Each round is one cycle through three tiers:

- **SETUP (Phases 1–5)** — deterministic player choice under uncertainty. The front-end strategy: the player has already chosen weapon + equipped loadout (§5–6) before the fight; per engagement they choose stance, position, approach, do their reading peak, and commit. These choices *weight* the bout's transition probabilities; they do not themselves resolve combat (except the Approach roll, which sets bout-entry state).
- **BOUT (Phase 6)** — the probabilistic engagement subgraph. ~6–10 seconds in-fiction. The setup choices resolve here as transitions between engagement states, weighted by stats (Pool), equipment (weapon modifiers), choices (state-gated σ-modifiers, §12.3), and chance (dice). This is the engagement round.
- **RESET (Phases 7–8)** — disengage and return to measure, with recovery. Leads back to SETUP for the next round (unless a terminal state was reached).

| Tier | Phase | Name | Primary mechanic | Initiative effect |
|---|---|---|---|---|
| SETUP | 1 | Stance | Player choice; sets Signal, Reading gating, Stance Counter, Concentration recovery, perception bias | Simultaneous |
| SETUP | 2 | Position | Player choice (stance-narrowed); sets Commit Pool/TN modifiers, Signal | Simultaneous |
| SETUP | 3 | Approach | Player choice (5 options); **opposed roll** sets bout-entry state (out-of-contact vs closing) and relative facing | Higher init first |
| SETUP | 4 | Reading peak | Player choice (attention split); Reading channels fire vs opponent Signal, **gated by field of view** (§4.5, §11.2) | Simultaneous |
| SETUP | 5 | Commit | Player choice (action class + depth); weights the bout's opening transition | Higher init first; clash if mutual full |
| BOUT | 6 | Bout | Probability-weighted state subgraph (§4.7); CLP auto-resolves; player intervenes at decision nodes | Simultaneous-declared per step |
| RESET | 7 | Disengage | Player choice (5 options); opposed roll when pursued | Higher init first |
| RESET | 8 | Return | Default + player choice (when wound filter narrows >1); recovery applies | Simultaneous |

**Timescale.** The **bout is the 6–10s engagement round**. Setup is brief in-fiction (a few seconds of maneuvering to measure); reset is ~1–2s. One full round of engagement ≈ **10–15 seconds in-fiction**. A 3-round duel resolves in well under a minute of in-fiction action. (Player decision-time concentrates in SETUP — the front-end strategy — while the bout largely auto-resolves with intervention at key nodes.)

**State-graph framing.** SETUP nodes are deterministic-choice; the BOUT is the probabilistic subgraph whose transition weights are set by SETUP. The player's leverage over the probabilistic bout is exercised *before and around* it (build, loadout, stance, approach, reading, commit, and in-bout intervention at decision nodes), not by micromanaging every transition. This is Pillar 2 in mechanical form.

### 4.2 Phase 1 — Stance

Player chooses a stable bodily configuration from trained Stance specializations (per §5 aspect catalog). Stance is sustained — it persists across the pass and affects subsequent phases.

**Mechanical effects:**
- Sets baseline **Signal Level** (low/medium/high — ambiguous stances reduce signal)
- Gates **Reading sub-channel bonuses** (each Stance favors specific channels)
- Sets **Stance Counter modifier** vs opponent's chosen Stance (per §7.1; σ-space, state-gated to the Closing state per §12.3)
- Sets **Concentration recovery rate** for this pass (sustained stances recover more)
- Sets available Position options for Phase 2

**Wound state filter:** Heavily wounded reduces available Stance set by ~50% (advanced stances require unimpaired body).

**No Pool roll.** Phase 1 is pure state-setting.

### 4.3 Phase 2 — Position

Player chooses where weapon and body move to as the attack prepares. Position telegraphs and gates Phase 5 commit options.

**Mechanical effects:**
- Signal Level adjustment (multi-attack-affording positions reduce signal; single-attack positions increase signal)
- Phase 5 Commit Pool TN modifier (fractional, draft ±0.5 per signal tier; sim-tunable I-17)
- Phase 5 action class availability (some Positions foreclose commits; some unlock advanced techniques per trained tradition)

**No Pool roll.** Phase 2 is pure state-setting.

### 4.4 Phase 3 — Approach

Player chooses how to close distance. Approach is committed — once moving forward, full reversal is expensive. Opponent's response begins during Approach.

**Options (canonical 5):**
- **Direct press**: straight-line close. Cost: 0 Stamina (canon: Standard movement equivalent)
- **Angled approach**: close from off-line, arrives with facing advantage (a perception edge — moves the opponent toward your central cone / yourself toward their periphery, §11.2). Cost: 1 Stamina; takes 2 zone transitions
- **Feinted approach**: appears to close, holds at threshold. Cost: 0 Stamina; opponent's Phase 5 Commit Pool at +1 Ob if they reacted
- **Drawing approach**: retreats first to pull opponent forward. Cost: 0 Stamina; opponent's Phase 3 fires at penalty next pass if they chase
- **Explosive close**: sudden close skipping intermediate zone. Cost: **3 Stamina** (canonical heavy-action cost reweighted); bypasses opponent's Phase 4 Reading peak

**Pool roll: opposed Approach Pool vs opponent's Reaction Pool**

```
Approach Pool = (Agility × 2) + Approach-aspect Proficiency + History modifier
Opponent's Reaction Pool = (Speed-or-Agility × 2) + Reaction-aspect Proficiency + History modifier
```

*Speed* here = Agility per canon (canon has no separate Speed attribute; Reaction defenders use Agi).

**Outcome:**

| Net successes (Approach − Reaction) | Effect |
|---|---|
| ≥ +3 | Zone arrival with facing advantage; opponent Phase 4 Reading at −1D this pass |
| +1 to +2 | Zone arrival, no advantage |
| 0 | Arrival at one zone short of intended |
| −1 to −2 | Arrival-tempo lost; opponent's Phase 5 Commit at +1D this pass |
| ≤ −3 | Approach fails; opponent gains free Phase 5 Commit at probe depth |

Feinted approach exception: rolls vs static TN 7 (not opposed); on success the Feint registers per option list.

### 4.5 Phase 4 — Reading peak

Reading is a continuous state variable that *peaks* immediately before Commit. Sensor channels fire vs opponent's Signal Level. Player allocates attention.

**Sensor channels:**

| Channel | Works at | Reveals | Pool composition |
|---|---|---|---|
| Tactile | In Bout (Phase 6) bind state | Pressure, intent through contact | `(Att × 2) + AspProf(Reading-Tactile) + History` |
| Kinetic | Measure → during opponent's Commit | Incoming attack: commitment-window timing + initiation order/type | `(Att × 2) + AspProf(Reading-Kinetic) + History` |
| Geometric | Stable Positions (Phase 1–2) | Positional vulnerabilities | `(Cog × 2) + AspProf(Reading-Geometric) + History` |
| Rhythmic | Multi-pass (after pass 2) | Opponent's cadence | `(Att × 2) + AspProf(Reading-Rhythmic) + History` |
| **Thread** | TS ≥ 30 (params/threadwork) | Opponent's thread state, Coherence integrity, Conviction strain | `(Spirit × 2) + History + TPS` per Thread Pool canon |
| **Intent** | At measure before Commit (Phase 4–5); higher tiers in Bout | Opponent's pre-motor state; tier-keyed abilities | `(Cog × 2) + Intent Reading track value` (see §6) |

**Channel set (F7 consolidation).** v31's five mundane channels over-split the reading role (diagnostic F7, Lesson 1). v32 merges the two intra-attack channels — *commitment timing* and *initiation order*, both Att-based reads of the incoming attack — into one **Kinetic** channel. The four remaining mundane channels carry distinct roles: Kinetic (incoming attack), Geometric (spatial/positional, Cog-based), Rhythmic (cross-round cadence — a distinct meta-temporal role), Tactile (contact/bind). This is a *minimal* Lesson-1 merge; further consolidation would risk collapsing genuinely distinct roles (Lesson-1 over-merge), and whether four is still over-split is a sim/playtest judgment.

**Field-of-view scaling (§11.2).** Each *sight-mediated* channel's Pool is scaled by the opponent's position in the reader's field of view (central 1.0 / near-peripheral 0.6 / far-peripheral 0.3 / blind 0.0). **Tactile is exempt** (contact-mediated — read through the bind regardless of gaze). This is how facing produces its effect: an opponent in your periphery is read at reduced Pool.

**Resolution:** channels roll vs opponent's Signal Level as fractional TN. Net successes produce a **Reading-modifier** that enters the §12.3 σ-space sum (state-gated) as a δσ contribution on Phase 5 Commit and Phase 6 Bout sub-actions — it is not added to Ob directly.

| Net successes | Read achieved | Reading-modifier (σ-space, §12.3) |
|---|---|---|
| 0 (failure) | none | +0 |
| 1 (partial) | class read (commit category visible) | Minor (δσ +0.25) |
| 2 (success) | class + depth read | Moderate (δσ +0.50) |
| 3+ (overwhelming) | full read | Strong (δσ +0.75); in Bout, sub-action options expanded by 1 (precognition surface) |

**Attention split mechanics:**
- **Full primary**: one channel at full Pool
- **70/30 split**: primary at Pool × 0.7 floor, secondary at Pool × 0.3 floor
- **Reserve**: 50% of pool fires Phase 4, 50% held for Phase 6 Bout sensor-read trigger

**Concentration cost:** 1 Conc per channel beyond primary; +1 Conc for Reserve.

**No Pool floor exception** — Reading rolls obey the 1D Pool floor (params/core §Pool Floor).

### 4.6 Phase 5 — Commit (initiates Bout)

The action chosen and launched. Player selects:
- **Action class** (light strike, heavy strike, thrust, displace, grip-change, Thread-op, etc. — class set varies by weapon and trained aspects)
- **Depth** (probe / preparatory / committed / deep / full — depth 1–5)

Higher Initiative fighter commits first within the phase. Lower fighter sees commit class+depth, then commits.

**Mutual-full clash exception:** if both fighters select depth 5 (full), commits resolve simultaneously per clash resolution (§4.7 Bout edge case).

**Depth structure:**

| Depth | Name | Stamina cost | Concentration cost | Bout chain length cap | Counter-window |
|---|---|---|---|---|---|
| 1 | Probe | 2 | 0 | 1 sub-action | 0.5s |
| 2 | Preparatory | 3 | 0 | 2 sub-actions | 1s |
| 3 | Committed | 5 | 1 | 4 sub-actions | 1.5s |
| 4 | Deep | 7 | 2 | 6 sub-actions | 2s |
| 5 | Full | 10 | 4 | unlimited (terminates only on wound/separation/resource) | 2.5s |

Stamina and Concentration costs are baseline; per-action-class costs may modify (see Bout sub-action costs §4.7).

**Depth ceiling per wound state:**
- Unwounded: depth cap 5
- Wounded (1 wound at low End; 1–2 at high End): cap 4
- Heavily wounded (≥(MW−1) wounds): cap 3

**Honor code filter** (if active): forbidden depths/classes are not surfaced (per §10 Authored codes).

**Thread-op alternative:** TS-sensitive practitioners (TS ≥ 30) may commit a Thread operation in place of a martial commit. Thread-op cost: per canonical Thread Fatigue table (Leap 3, Mend 4, Pull 5, Lock 7, Dissolve 10) + the proposal's Concentration cost per depth. Thread-op P-01 cascade fires per combat_v30 §10.1.

**Commit initiates Bout** (Phase 6). The opening sub-action of the bout chain is set by the commit's action class + depth, resolved through the **§12.3 σ-space modifier sum** (state-gated): Reading-modifier, Stance Counter (Closing), Reaction matchup, weapon phase-strength, set bonus, and the **emergent perception effect** (FoV consequences of relative facing, §11.2 — not a separate facing-Ob line) — passed through the soft cap, then converted to an Ob shift scaled to the Pool.

### 4.7 Phase 6 — Bout (the probability-weighted subgraph)

The engagement round. ~6–10 seconds in fiction. The bout is a **probability-weighted state subgraph**: fighters occupy an engagement state, each picks a sub-action (player or CLP), and the opposed resolution determines the transition to the next state (including terminal wound/disengage/felled states).

**Engagement states and their transitions** (the subgraph):

| State | Entered from | Sub-action options | Transitions to |
|---|---|---|---|
| **Out-of-contact** | commit miss; probe | Probe-cut / Probe-thrust / Step-around / Disengage→P7 | Closing, Breaking |
| **Closing** | commit land; approach | Cut / Thrust / Press-the-bind / Yield-to-bind / Void-and-counter | In-bind, Out-of-contact, Wounded, Breaking |
| **In-bind** | bind formed | Wind / Yield / Press / Displace / Break-bind / Grip-change (weapon-dependent) | Closing, Breaking, Wounded |
| **Breaking** | one fighter disengaging | Pursue / Release / Throw-strike | → Phase 7 (Disengaged), Wounded |
| *Wounded* (terminal-ish) | wound transition | — | continue or Breaking |
| *Disengaged* / *Felled* | terminal | — | exit to RESET / combat end |

**State-gating (§12.3).** Each state surfaces only its physically-relevant modifiers — Stance Counter lives at Closing, Tactile reading and Grip at In-bind, perception/facing at open states, etc. This bounds compound modifier stacking (the v31 F2 fix) and shrinks the per-state decision.

**Transition resolution.** Both fighters declare from the current state's option set (simultaneous-declared per step). Each declaration resolves as an opposed roll; the outcome sets the transition. Transition probability is weighted by:

```
Sub-action Pool = (relevant-attribute × 2) + AspProf(aspect) + History modifier
Relevant-attribute: Cut/Thrust = Agi(light)/Str(heavy); Press/Wind = Str;
  Yield/Void/Disengage/Probe = Agi; Displace/Grip-change = Str+Agi composite (sim-tunable)

Effective Ob = base Ob (1–3), adjusted by the STATE-GATED σ-space modifier sum (§12.3):
  net_σ = Σ(live state-gated modifiers in σ-units) — Stance Counter (Closing only),
          Reaction-aspect, Reading-modifier, set-bonus (loadout), weapon phase-strength,
          perception (emergent from facing/FoV, §11.2)
  effective_σ = M_max · tanh(net_σ / M_max)          [M_max = 1.5σ, soft cap]
  Effective Ob = base Ob − effective_σ · 0.8·√Pool
```

Perception/facing is **not** an authored Ob line — it enters as the Reading-modifier and reaction-availability consequences of field of view (§11.2). This is the v32 change: Facing's effect is emergent.

**Player intervention triggers** (engine pauses for player decision; otherwise CLP auto-resolves):
- (a) Opponent's commit depth crosses player's response threshold
- (b) Engagement-state transition (e.g., closing ↔ in-bind)
- (c) A Reading channel reveals previously-occluded information
- (d) Resource crosses critical threshold (Concentration <30%, Stamina <30%)
- (e) Thread-mediated sub-action becomes available (TS-gated)

**Termination conditions (transitions to terminal states):**
1. **Wound transition**: a sub-action lands at net successes ≥ Ob + (current wound count + 1) → Wounded; control passes to Phase 7.
2. **Both separate**: both declare Disengage → Phase 7 simultaneously.
3. **Concentration depletion**: either fighter <30% → depleted fighter forced to Phase 7.
4. **Stamina depletion**: either fighter <30% → depleted fighter forced to Phase 7.
5. **Chain cap reached**: depth-keyed cap (§4.6) → Phase 7.
6. **Mutual deep-commit clash**: both depth ≥4 collision → highest Pool net successes wins; chain ends.

**Edge case rulings:**
- **Mutual depth-5 (full) clash**: both Pools roll opposed; both apply wound consequences at net-successes magnitude. If tied, both heavily wounded. (Voluntary mutual full-commit; high resource cost; the soft cap (§12.3) ensures neither is foreclosed pre-roll.)
- **Mutual depth-5 with one Thread-op**: Thread-op resolves first per P-01 temporal-auto-effect ordering.
- **Chain-termination ambiguity** (multiple fire same step): priority 1, 5, 2, 6, 3, 4 (wound first; chain cap; mutual separation; clash; resource depletion).
- **Mutual disengage**: both succeed; both separate to Phase 7.

### 4.8 Phase 7 — Disengage

Separation. Player chooses how to separate.

**Options (canonical 5):**
- **Clean withdrawal**: full retreat to Ranged distance (canonical PP-290; beyond Long Reach). Cost: 1 Stamina. If opponent pursues, Phase 3 fires immediately next pass.
- **Pursuing disengage**: break only if opponent also disengages; otherwise press for next pass's Commit. Cost: 0. Conditional.
- **Defensive disengage**: separate with parry-ready guard. Cost: 2 Stamina; +2 Ob to opponent's pursuit attempt.
- **Drawing disengage**: withdraw with vulnerability bait. Cost: 0; opponent's pursuit next pass at +1 Ob (drawn-in penalty).
- **Sudden disengage**: abrupt break with unexpected vector. Cost: 3 Stamina + 1 Concentration; opponent's Phase 4 Reading peak next pass fails entirely.

**Resolution:**

If opponent does not pursue (their Phase 7 also disengages, or they're incapacitated): all options succeed automatically.

If opponent pursues: opposed Disengage Pool vs pursuer's Reaction Pool.

```
Disengage Pool = (Agi × 2) + AspProf(Disengage) + History
```

Outcome:

| Net successes (Disengager) | Effect |
|---|---|
| ≥ +2 | Clean break; pursuer ends pass at starting zone; no Phase 3 advantage next pass |
| 0 to +1 | Partial break; zone change succeeds; pursuer follows; Phase 3 next pass fires for pursuer at +1D |
| −1 to −2 | Bind held; engagement persists; Phase 6 resumes next pass (no Phase 1–5 reset) |
| ≤ −3 | Disengage failure with consequence; pursuer gains free Phase 5 Commit at probe depth immediately |

### 4.9 Phase 8 — Return to stance

The character returns to a stable configuration. Wound state filters available Stance options; if multiple available, player picks. If one available, default fires.

**Mechanical effects:**
- Reading state persists in part (Rhythmic channel reads accumulate; other channels reset per §5.5 Reading state-variable rules)
- **Stamina recovery**: `+(Endurance + History) × 2`, capped at max (canonical Take a Breath per derived_stats §4.2)
- **Concentration recovery**: `+Focus`, capped at max (new combat extension; sim-tunable I-15)
- **Coherence recovery**: +1 if no Thread-op this pass (per P-15)
- New Stance set for next pass

Pass ends. If neither fighter has met termination per §4.4, loop returns to Phase 1.

### 4.10 Combat termination conditions

| Condition | Trigger | Outcome |
|---|---|---|
| Felled (canonical) | Health ≤ 0 (MW+1 wounds accrued) | Per combat_v30 §4 Stage 1 (Down) → Stage 2 (Dying) cascade preserved |
| Stamina collapse | Stamina = 0 (Out of Breath, canonical) | −2D all rolls until recovery action; usually forces disengage |
| Concentration collapse | Combat Concentration = 0 | Engine forces Phase 7 disengage; combat continues if opponent permits |
| Voluntary withdrawal | Clean disengage with opponent not pursuing | Combat ends without resolution |
| Death (Stage 2 → Killed) | Stage 1 + 1+ net hit landed | Death Cascade fires per combat_v30 §13.3 |

---

## 5. COMBAT HISTORIES (TRADITION BUNDLES)

Combat-relevant Histories are organized as **Traditions** — coherent bundles of aspect specializations, technique trees, and Intent Reading teaching tiers. Tradition is the *learning structure*; aspects (§6) are the *operating structure*.

### 5.1 Histories framing (canonical)

Per audit principle #4 (Histories not Skills) and params/core.md §Attributes: a character's Histories are lived experiences that grant point-based bonuses. **Combat Histories** are a subset of all Histories — those representing combat training.

A character's History points are capped per History at the character's **Recall** value (params/core.md). A character with Rec 3 can have at most 3 points in any single History.

**Tradition Depth** is **derived** from History points in that Tradition's defining History entry: a character with 3 points in "Long-thrust dueling tradition" History is at Tradition Depth 3 (Journeyman). The "Tradition Depth modifier" referenced in Pool formulas equals the character's History points in that History.

### 5.2 Combat Histories — Valoria-faction-aligned (full set)

**Ten named combat Histories** aligned to Valoria's faction-cultural landscape. Characters may also create per-character custom combat Histories via canonical History creation rules; the catalog below represents recognizable Tradition bundles for common combat training.

| # | Tradition (History name) | Aspect bundle | Valoria faction binding | Intent Reading teaches up to | Weapon-class fit |
|---|---|---|---|---|---|
| 1 | Long-thrust dueling tradition | Forward-point stance + Linear footwork + Standard grip + Direct/Explosive approach + Kinetic reading + Hand-led reactions + Decisive commitment + Clean/Pursuing disengage | Hafenmark formal duelists; Crown court fencing | Tier 2 (Steady) | Long thrust-primary |
| 2 | Long-blade contact tradition | Centered/Raised stances + Linear + Standard grip with half-grip-available + Direct press + Tactile reading + Yielding/Pressing reactions + Sustained commitment + Defensive disengage | Crown infantry; mixed faction soldiery | Tier 1 (Surface) | Long cut-and-thrust |
| 3 | Long-thrust geometric tradition | Forward-point + Curvilinear footwork + Standard grip + Angled approach + Geometric reading + Hand-led + Cautious commitment + Defensive disengage | Crown court advanced fencing academy (theoretical/mathematical training); Löwenritter officer training | Tier 1 (Surface) | Long thrust-primary |
| 4 | Counter-time tradition | Centered/Side stances + Linear + Standard + Drawing approach + Kinetic reading + Reactive anticipation + Hand-led counter reactions + Defensive disengage | Crown court fencing masters; Hafenmark senior duelists; rare in other factions | **Tier 4 (Pre-empt)** | Long thrust-primary; Long cut-and-thrust |
| 5 | Single-strike tradition | Stance-flux mid-Bout (per §5.5.1 Apprentice technique) + Linear + Standard + Direct/Drawing + Intent reading focus + Body-led reactions + Decisive commitment + Clean disengage | Niflhel sword-saints (peripheral monastic lineage); rare Restoration Movement contemplative wing | **Tier 5 (Master)** | Long cut-and-thrust; Single short (formal seppuku-equivalent context) |
| 6 | Curved-blade cavalry tradition | Variable stance + Bursting footwork + Thumb-anchor grip + Direct press approach + Rhythmic reading + Pressing reactions + Burst commitment + Pursuing disengage | Crown light cavalry; Varfell highland raiders; Hafenmark merchant-escort cavalry | Tier 1 (Surface) | Curved cut-primary |
| 7 | Continuous-flow tradition | Continuous (no discrete stance) + Triangular footwork + Paired grip + Angled approach + Rhythmic reading + Voiding reactions + Sustained commitment + Sudden disengage | Niflhel highland practice (paired-blade form); Restoration Movement Thread-aware practitioners (continuous flow as Thread-state combat) | Tier 2 (Steady) | Paired short; secondary Continuous-blade variant |
| 8 | Mounted multi-weapon tradition | Mode-dependent stance + Bursting footwork + Variable grip + Direct approach + Geometric/Kinetic reading + Pressing reactions + Burst commitment + Pursuing disengage | Löwenritter knightly cavalry (signature tradition); Crown heavy cavalry | Tier 2 (Steady) | Long pole (lance); Curved cut-primary (saber dismounted); Long cut-and-thrust (sword dismounted) |
| 9 | Conditioning-and-grappling tradition | Centered + Linear + (body grip) + Direct + Body-contact reading + Yielding/Pressing + Sustained + Clean | Niflhel highland practice; Varfell light infantry; Restoration Movement militia training | Tier 1 (Surface) | Single short (close-range backup); unarmed |
| 10 | Formation-and-discipline tradition | Variable + Linear with formation positioning + Variable + Coordinated approach + Kinetic + Disciplined defaults + Patterned anticipation + Defensive | Crown infantry (line formation); Church Templars (formal protocol); Löwenritter ground formation | Tier 1 (Surface) | Long pole (spear/pike); Long cut-and-thrust (formation backup) |

**Valoria-faction binding rationale:**
- **Crown** has the broadest combat-tradition footprint — court fencing (1, 3, 4), infantry (2, 10), cavalry (6, 8). Reflects Crown's politically central + militarily diverse role.
- **Hafenmark** specializes in formal duelist traditions (1, 4) reflecting its merchant-civic culture and judicial-combat tradition.
- **Niflhel** holds the most distinctive traditions — Single-strike (5), Continuous-flow (7), Conditioning-and-grappling (9) — reflecting its peripheral cultural position and contemplative martial practices.
- **Varfell** holds practical infantry traditions — Curved-blade cavalry (6 highland raiders), Conditioning-and-grappling (9) — reflecting highland practical combat needs.
- **Löwenritter** signature tradition is Mounted multi-weapon (8); also Long-thrust geometric (3) for officers and Formation-and-discipline (10) for ground.
- **Church** has Formation-and-discipline (10) for Templar protocol; canonical Templar combat protocol (§13) layers over this tradition.
- **Restoration Movement** has emergent Continuous-flow (7) for Thread-aware practitioners and Conditioning-and-grappling (9) for militia.
- **Guilds**, **Revolution** factions have no signature traditions in this catalog — Guild mercenaries hire across; Revolution rarely engages formal combat.

### 5.3 Cross-training

A character's primary combat History grants full Aspect Proficiency access to its bundle. Cross-trained Histories' aspects come at **Proficiency cap = History points in that History − 1** (preserves canonical Recall-cap structure).

**Time and progression cost:**
- Each combat History requires training time (in-game months at mentor-relationship Standing ≥ 1)
- History points accrue per canonical progression rules (XP investment + lived experience)
- Recall cap applies per-History

**Example hybrid (preserved from proposal §6):** A fencer trained primarily in Long-thrust dueling History (3 points, Tradition Depth 3) who additionally studies Counter-time tradition (2 points, Tradition Depth 2):
- Stance: Forward-point (both teach; Aspect Prof from Long-thrust at 3 cap)
- Footwork: Linear (both teach)
- Reading: Kinetic primary AspProf 3 (Long-thrust + Counter-time lineage)
- Reaction: Hand-led counter (both teach)
- Anticipation: Reactive (Counter-time exclusive; AspProf 2 cap)
- Plays as a Long-thrust duellist with counter-time counter-attack capability — mechanically a hybrid.

### 5.4 Histories integration with character creation

At character creation, a character's lived Histories generate starting combat-Tradition exposure:
- "Hafenmark Court Page" History → +1 starting point in "Long-thrust dueling tradition" History
- "Crown Cavalry Service" History → +2 starting points in "Long-blade contact tradition" + +1 in "Long-thrust dueling tradition"
- "Niflhel Highland Childhood" → +1 in "Conditioning-and-grappling tradition"
- "Crown Court Fencing Studies" → +2 in "Long-thrust dueling" + +1 in "Counter-time"
- "Löwenritter Page" → +1 in "Mounted multi-weapon" + +1 in "Long-thrust geometric"
- "Varfell Highland Service" → +2 in "Curved-blade cavalry" + +1 in "Conditioning-and-grappling"
- "Restoration Movement Contemplative" → +1 in "Continuous-flow" + +1 in "Conditioning-and-grappling"
- "Templar Initiation" → +2 in "Formation-and-discipline" + +1 in "Long-blade contact"

Full Histories-to-Tradition mapping table sourced from `designs/personal/character_generation_questionnaire_v30.md` (pending update on this proposal's ratification).

### 5.5 Tradition technique trees

Each Tradition has a **technique tree** — phase-action unlocks gated by Tradition Depth (= History points in that Tradition's History). Techniques unlock cumulatively: a character with Tradition Depth 3 has access to all techniques at Depth 1, 2, 3.

**Tree structure (general):**

| Depth | Tier name | Unlock count | Typical content |
|---|---|---|---|
| 1 | Apprentice | 2 techniques | Foundational sub-actions in the tradition's strong phases |
| 2 | Journeyman | 2 techniques | Improved variants of Apprentice techniques + 1 new Aspect specialization access |
| 3 | Adept | 2 techniques | Signature techniques (combos chaining sub-actions) + Aspect Proficiency cap to 4 |
| 4 | Master | 1 technique | Tradition-defining technique (unique to this tradition) + Aspect Proficiency cap to 5 |

**Technique mastery (preserved from proposal §10):** each learned technique has three personal mastery levels — Learned (base reliability), Practiced (improved reliability + follow-up options), Mastered (maximum reliability + advanced chain options).

#### 5.5.1 Sample technique trees (4 of 10)

The four traditions below have detailed trees as design exemplars. Trees for the remaining 6 traditions (Long-blade contact, Long-thrust geometric, Curved-blade cavalry, Continuous-flow, Mounted multi-weapon, Formation-and-discipline) follow the same structure; specific techniques deferred to faction-specific design passes per I-12b.

**Tradition 1 — Long-thrust dueling tradition** (Hafenmark formal duelists; Crown court fencing)

| Depth | Technique | Phase | Mechanical effect |
|---|---|---|---|
| 1 (Apprentice) | Direct thrust lunge | Phase 3 Approach + Phase 5 Commit | Direct press Approach + depth-3 thrust as single chained action; Stamina cost reduced by 1 (combined economy) |
| 1 (Apprentice) | Forward-point parry | Phase 6 Bout (Closing state) | Hand-led Reaction at +1D Pool when defending against opponent's Phase 5 thrust; works in Forward-point Stance only |
| 2 (Journeyman) | Explosive lunge | Phase 3 + Phase 5 | Explosive close + depth-3 thrust as chained action; ignores opponent's Phase 4 Reading (combined with Explosive close mechanic) |
| 2 (Journeyman) | Counter-thrust | Phase 6 Bout (In-bind state) | When opponent commits Thrust against you in bind, free counter-Thrust at same depth at +1 Ob to opponent |
| 3 (Adept) | Glide-and-thrust | Phase 6 Bout combo | Sustained Press (sub-action 1) → Wind (sub-action 2) → Thrust (sub-action 3) as a single chained commitment; chain step cost reduced by 0.5 Conc each |
| 3 (Adept) | Lunge-and-recovery | Phase 5 + Phase 7 | Depth-4 Deep thrust + Clean disengage as a single chained action; opponent's pursuit at +1 Ob (recovery posture) |
| 4 (Master) | **Master's straight thrust** | Phase 5 Commit | Depth-3 thrust at +2D Pool against opponent's Centered, Raised, or Side stance (Forward-point counters Centered hardest); requires Forward-point Stance + Standard grip + Decisive Commitment aspects all at AspProf ≥ 4 |

**Tradition 4 — Counter-time tradition** (Crown court fencing masters; Hafenmark senior duelists)

| Depth | Technique | Phase | Mechanical effect |
|---|---|---|---|
| 1 (Apprentice) | Counter-thrust drawing | Phase 3 + Phase 6 | Drawing approach (Phase 3) + when opponent pursues with Thrust at Phase 6 entry, +1D Pool on counter-Yield sub-action |
| 1 (Apprentice) | Tempo-read setup | Phase 4 Reading peak | Kinetic channel read with no Conc penalty (normally costs 1 Conc) |
| 2 (Journeyman) | Counter-thrust deflection | Phase 6 Bout | When opponent commits depth-3+ Thrust, Hand-led Reaction at +2D Pool; on Success, opponent's commit reduced by 2D (counter-time disrupts opponent's flow) |
| 2 (Journeyman) | Reactive Anticipation refinement | Phase 4 | Reactive Anticipation: Reading channels fire at +1D *during* opponent's Phase 5 Commit, not just at Phase 4 peak |
| 3 (Adept) | Indes (in-tempo strike) | Phase 6 Bout | Mid-Bout, when sensor channels reveal opponent's commit class transition, free counter-strike sub-action at +1 Ob to opponent |
| 3 (Adept) | False tempo | Phase 3 Approach | Drawing approach at +1D versus-roll Pool; on Overwhelming, opponent's Phase 5 Commit options reduced by 1 (forced into reactive depth, can't initiate deep) |
| 4 (Master) | **Pre-emptive counter** | Phase 4 + Phase 5 | When Phase 4 Intent Reading scores net ≥3 against opponent's commit-class read, perceiver gains free Phase 5 Commit at probe depth *before* opponent's Phase 5 fires (mirrors §10 Intent Tier 4 Pre-empt; works without Tier 4 Intent if Counter-time Tradition Depth 4) |

**Tradition 5 — Single-strike tradition** (Niflhel sword-saints)

| Depth | Technique | Phase | Mechanical effect |
|---|---|---|---|
| 1 (Apprentice) | Intent-focused commit | Phase 5 | Depth-3 commit at +1D Pool when character has used 0 Phase 5 commits this scene (preserves a single decisive moment) |
| 1 (Apprentice) | Stance-flux | Phase 1 | Character may switch Stance once per Bout entry without Concentration cost (other traditions: Conc cost or restricted timing) |
| 2 (Journeyman) | Distance reading | Phase 4 Reading peak | Geometric channel reads at +2D Pool when both fighters are at Long Reach (positional clarity at distance) |
| 2 (Journeyman) | Body-led counter | Phase 6 Bout | Body-led Reaction at +1D Pool when defending against depth ≥3 Commits (whole-body parry favored against deep) |
| 3 (Adept) | Single-cut commit | Phase 5 | Depth-5 Full commit at reduced Stamina cost (10 → 7) when this is character's first depth-5 commit of the scene; subsequent depth-5 commits in same scene at normal cost |
| 3 (Adept) | Intent Cascade preparation | Phase 4 | Sustained Read (Intent track Tier 2 prerequisite) carries forward additional 1 sub-action in Bout chain |
| 4 (Master) | **Single decisive strike** | Phase 5 | Once per scene: depth-5 Full commit at +3D Pool, +2 weapon modifier vs armor (one decisive blow). Other depth-5 commits this scene at normal magnitude. Requires Intent Reading Tier 4+. The Tradition's defining technique. |

**Tradition 9 — Conditioning-and-grappling tradition** (Niflhel highland; Varfell light infantry)

| Depth | Technique | Phase | Mechanical effect |
|---|---|---|---|
| 1 (Apprentice) | Body-contact closing | Phase 3 | Direct press Approach: on closing, free Tie Up sub-action attempt at Phase 6 entry (canonical Tie Up rules) |
| 1 (Apprentice) | Wrestler's yield | Phase 6 Bout | Yielding Reaction at +1D Pool when in body-grip sub-action (close-range grappling) |
| 2 (Journeyman) | Displacing throw | Phase 6 Bout | Displace sub-action: on Success, opponent forced to Phase 8 with stance broken (cannot use Centered next pass); on Overwhelming, opponent's Stamina −3 (thrown impact) |
| 2 (Journeyman) | Sustained pressure | Phase 6 + Phase 7 | Sustained Commitment + Phase 7 Pursuing disengage if opponent breaks; pursuit at +1D Pool |
| 3 (Adept) | Ground-and-control | Phase 6 Bout | Tie Up sub-action: on Overwhelming, opponent's Combat Pool reduced by 4D (not 2D as canonical) for 2 rounds; both fighters at −2D as normal |
| 3 (Adept) | Body-read | Phase 4 | Tactile channel works at Long Reach (normally only in Bout In-bind state); reveals opponent's stance commitments through implied body language |
| 4 (Master) | **Pinning grip** | Phase 6 Bout | When opponent is Heavily Wounded, free Tie Up at +3D Pool + Tie Up's effect doesn't penalize self; on Overwhelming, opponent goes to Stage 1 (Down) without further damage — non-lethal incapacitation |

#### 5.5.2 Technique acquisition

- **At character creation:** Apprentice (Depth 1) techniques unlock automatically with starting Tradition Depth ≥ 1
- **Through play:** Journeyman (Depth 2), Adept (Depth 3), Master (Depth 4) techniques unlock as Tradition Depth advances via History point investment + training time
- **Mentor relationships (canonical):** Master-tier techniques require a Master-tier mentor at faction Standing ≥ 3; mentor-relationship maintenance per canonical NPC behavior rules
- **Technique mastery (Learned → Practiced → Mastered):** use-based per canonical progression rules; specific use-counts and triggers in I-12b implementation pass

#### 5.5.3 Open items (I-12b)

- Full technique trees for the 6 remaining Traditions (Long-blade contact, Long-thrust geometric, Curved-blade cavalry, Continuous-flow, Mounted multi-weapon, Formation-and-discipline)
- Mentor-relationship Standing requirements per technique tier
- Cross-tradition technique borrowing (can a Counter-time fencer learn Long-thrust dueling's Counter-thrust technique without learning the full tradition?)
- Technique mastery use-counts for Learned → Practiced → Mastered transitions

---

<!-- §§6–10 in Pass 2 turn 2b -->

---

## 6. ASPECT SPECIALIZATIONS (CHARACTER MECHANICS)

A character is built by configuring **10 aspect slots**. Each aspect has 3–6 specialization options. Aspect specializations are sub-skills *within* the character's combat Histories (§5). A character's available specialization options are gated by which combat Histories they have trained; the player configures within available set.

Each specialization has its own **Aspect Proficiency** value (0–5), advancing through use and capped by the character's points in the source History.

This section enumerates the 10 aspects, their specializations, and mechanical effects — the character's **trained pool**. The **equip** step that selects an active **loadout** from this pool (and the named sets it can form) is §6.11. All magnitudes draft; sim-tunable per I-17.

### 6.1 Stance

**Sustained bodily configuration.** Sets Phase 1 baseline state for the pass. Sustained — persists across phases until Phase 8 Return.

| Specialization | Available positions | Sensor channel bonus | Signal Level | Concentration recovery |
|---|---|---|---|---|
| Centered guard | Universal (cut, thrust, parry) | Tactile (bind-ready) | Medium | Standard (+Focus per Phase 8) |
| Raised guard | Descending cuts | Geometric (high overview) | High (telegraphed) | Standard |
| Low guard | Rising attacks; bind-baiting | Kinetic (reads opponent commitment cleanly) | Low (concealed) | +1 (low-stress posture) |
| Side guard | Angled cuts; voiding | Kinetic (reads opponent's motion clearly) | Medium | Standard |
| Forward-point guard | Thrusts; counter-time | Kinetic + Intent (with §10 track) | Low (concealed; weapon as line) | −1 (tense posture) |

**Stance Counter Matrix** (§7.1) provides a σ-space modifier per stance-vs-stance matchup, state-gated to the Closing state (§12.3).

### 6.2 Footwork

**Movement pattern through phases**. Affects Phase 3 Approach Pool composition and Bout sub-action movement options.

| Specialization | Phase 3 Approach Pool effect | Bout movement options |
|---|---|---|
| Linear | +1D Direct press / Explosive close | Step-back, step-in |
| Curvilinear | +1D Angled approach | Side-step, curve-around (changes facing) |
| Triangular | +0.5D Angled; +0.5D Drawing | Multi-vector step (3-point pivots) |
| Drawing | +1D Drawing approach | Draw-and-counter (Bout sub-action enables) |
| Bursting | +1D Explosive close (Stamina cost unchanged) | Burst-in (one-time Bout movement Phase 6 entry) |

### 6.3 Grip

**Weapon hold; gates available techniques**. Affects which Bout sub-actions are surfaced and which weapon-class commits are available.

| Specialization | Available Bout sub-actions | Notes |
|---|---|---|
| Standard | Cut, Thrust, Press, Yield, Disengage | Default; available to all weapons |
| Thumb-anchor | + Wind, + Bind-stability | Cut weapons; improves bind retention |
| Short grip | + Half-sword strikes | Long weapons only; gives close-range option |
| Half-grip-available | Standard set + Grip-change sub-action enables transitioning mid-Bout | Long Heavy Blade requirement |
| Paired grip | + Off-hand actions; + Coordinated sub-actions | Paired weapons only; two simultaneous declarations |

### 6.4 Approach

**Closing-distance pattern**. The 5 options are the Phase 3 menu (§4.4). Specialization in an Approach raises Aspect Proficiency in that option, adding to its Approach Pool roll.

| Specialization | Mechanical effect at Phase 3 |
|---|---|
| Direct press | +AspProf to Direct press Approach Pool; no Stamina cost |
| Angled | +AspProf to Angled approach Pool; arrives with facing advantage; +0.5 Ob to opponent Phase 4 Reading next pass |
| Feinted | +AspProf to Feinted approach versus-roll Pool; on success forces opponent's Phase 5 at +1 Ob |
| Drawing | +AspProf to Drawing approach Pool; opponent chase at +1 Ob next pass |
| Explosive | +AspProf to Explosive close Pool; bypasses opponent Phase 4 Reading |

### 6.5 Reading

**Primary sensor channel preference.** The 4 mundane channels + Thread (TS-gated) are the Phase 4 Reading peak menu (§4.5). Specialization raises Aspect Proficiency in one or more channels.

| Specialization | Reading channel preferred | Notes |
|---|---|---|
| Tactile | Bout (bind state); Phase 6-active | Primarily reads in-bind opponent |
| Kinetic | Phase 4 measure → Phase 5 commit | Reads the incoming attack: commitment timing + motion order/type |
| Geometric | Phase 1-2 (stable positions) | Reads positional vulnerabilities |
| Rhythmic | Multi-pass (pass 2+) | Reads cadence; long-fight channel |
| Thread | TS 30+ required (canonical) | Reads thread state; canon per combat_v30 §10.2 |

**Intent reading** is *not* an Aspect spec under Reading. See §10 — separate progression track per Jordan canon override.

### 6.6 Anticipation

**Pre-commit prediction pattern.** Affects Phase 4 Reading peak attention split and Phase 5 Commit decision-window.

| Specialization | Mechanical effect |
|---|---|
| Predictive | Attention split bonus: secondary channel at 0.5 Pool instead of 0.3 |
| Reactive | Reading bonus *during* opponent's Commit: Kinetic channel fires at +1D when opponent depths ≥3 |
| Proactive | Phase 5 Commit fires before Reading peak if Initiative high; trades Reading info for tempo |
| Adaptive | Attention split adjusts mid-Bout: can re-allocate sensor focus on player intervention triggers |
| Patterned | Phase 6 Bout: opponent's repeated sub-actions raise Reading channel bonuses cumulatively (+0.25 Ob per repeat, capped at +1.5) |

### 6.7 Reaction

**In-Bout reflex default.** The 5 specs are the Reaction-aspect Ob modifier table (§7.2) — how the character's defensive sub-actions resist opponent commits at various depths.

| Specialization | Bout default sub-action style | Reaction-aspect Ob modifier (per §7.2) |
|---|---|---|
| Hand-led | Quick parry; weapon-against-weapon | Strong vs probe/preparatory; weak vs deep/full |
| Body-led | Whole-body shift; full-body parry | Strong vs deep/full; neutral vs probe |
| Yielding | Receive pressure; redirect | Strongest vs deep/full overcommit; weak vs probe |
| Pressing | Counter-pressure; force opponent off-line | Strong vs probe; neutral vs deep |
| Voiding | Evade with footwork | Strongest vs probe (clean evasion); weak vs full (insufficient time) |

### 6.8 Commitment

**Depth pattern across commits.** Affects Phase 5 Commit depth selection cost or default; some specs interact with Bout chain length cap.

| Specialization | Mechanical effect |
|---|---|
| Cautious | Depth 1–2 commits at reduced Concentration cost (−1 Conc); depth 4+ unavailable unless wounded threshold crossed |
| Decisive | Depth 3 (committed) at +0.5 Pool; no penalties to higher depths |
| Escalating | Depth raises by 1 per round beyond round 1 (forced); cannot lower depth back |
| Burst | Depth 4 commits at −1 Stamina cost; locked out of Phase 6 Bout chain past 2 sub-actions (must Phase 7 disengage) |
| Sustained | Bout chain length cap +2 (longer engagements); Phase 8 recovery −1 (sustained engagement is tiring) |

### 6.9 Disengage

**Separation preference.** The 5 specs are the Phase 7 menu (§4.8). Specialization raises Aspect Proficiency in that option.

| Specialization | Mechanical effect at Phase 7 |
|---|---|
| Clean | +AspProf to Disengage Pool when opponent pursues; no extra cost |
| Pursuing | Pursuing disengage at +1D against opponent Reaction Pool |
| Defensive | +AspProf to Defensive disengage; opponent's pursuit at +2 Ob (per §4.8 + AspProf) |
| Drawing | Drawing disengage at +1D versus-roll; opponent +1 Ob next pass (per §4.8 + AspProf bonus) |
| Sudden | Sudden disengage at +AspProf; Concentration cost reduced by 1 (Sudden is energetic but masterable) |

### 6.10 Conditional Logic Profile

**Auto-resolution decision tree.** The character's behavior settings governing Bout AI-driven default and any phases the player has set to auto-resolve.

The CLP is the **meta-aspect** — it doesn't define a combat capability; it defines how the character's other 9 aspects fire under autonomous control. Implementation surface: **priority-ordered rule list** with structured condition+action grammar.

#### 6.10.1 Implementation choice — priority-ordered rule list

Among three considered options (priority list, decision-tree builder, natural-language declarative), this proposal commits to **priority-ordered rule list with structured DSL**. Rationale:

- **Programmable**: rules evaluate top-to-bottom; first matching rule fires; deterministic
- **Inspectable**: player can read the entire profile in one glance; reorder via drag-and-drop
- **Tunable**: rules can be added, removed, or reordered without rewriting the whole profile
- **Mentor-portable**: characters can copy/share rule lists between save files (per-character behavior templates)
- **Avoids decision-tree complexity** which produces deeply-nested edge cases harder to test/debug
- **Avoids natural-language ambiguity** which produces parser failures on edge-case wording

#### 6.10.2 Rule structure

Each rule has three components: priority, condition, action.

```
[priority N]
WHEN <condition>
THEN <action>
[optional: ALSO <secondary action>]
```

Rules are evaluated in priority order (lowest N = highest priority). First matching rule fires its action; subsequent rules in the same phase skipped unless the rule includes `CONTINUE` (then evaluation continues to lower-priority rules).

#### 6.10.3 Condition grammar

Conditions are predicates over game state. The condition DSL supports the following primitives:

**Resource thresholds:**
- `concentration < 50%` / `concentration <= 5` / `concentration >= max`
- `stamina < 30%` / `stamina = 0` / `stamina >= half`
- `wounds = 0` / `wounds >= 1` / `wounds = max` (Heavily Wounded)
- `coherence <= 3`

**Phase / engagement state:**
- `phase = N` (N = 1..8)
- `in_bout` / `out_of_bout`
- `bout_state = "closing"` / `bout_state = "in-bind"` / `bout_state = "breaking"`
- `bout_steps >= N` (sub-actions completed this Bout)
- `passes_elapsed >= N` (passes since combat start)

**Opponent state:**
- `opponent.stance = "Forward-point"` (and all named stance specializations)
- `opponent.depth >= N` (last commit depth observed)
- `opponent.commit_class = "thrust"` / `"cut"` / `"thread-op"` / `"unknown"`
- `opponent.facing = "flank"` / `"rear"` / `"quarter"` / `"square"`
- `opponent.wounds >= N`
- `opponent.signal = "low"` / `"medium"` / `"high"`
- `opponent.reads_as = "Predictive"` / `"Reactive"` / etc. (Anticipation aspect inferred)

**Reading state:**
- `last_read.success` (Phase 4 most recent Reading peak succeeded)
- `last_read.overwhelming` (Reading peak at net ≥3)
- `intent_tier >= N` (character's own Intent Reading tier; static character attribute)

**Honor/scene context:**
- `scene.context = "judicial"` / `"ritual"` / `"templar"` / `"prisoner"` / `"tutorial"`
- `code.foreclosed_includes("depth_5")` (per §13 Authored code; checks scene metadata)

**Logical combinators:**
- `AND`, `OR`, `NOT`
- Parentheses for grouping

#### 6.10.4 Action grammar

Actions are declarative — they specify *which option to take in which phase* or *which override to fire*.

**Phase-specific actions:**
- `phase_1 := "Centered guard"` (Stance choice — must be trained specialization)
- `phase_2 := "thrust-line"` (Position choice — Position names are defined per Stance in §4.3, not enumerated as discrete specs)
- `phase_3 := "Direct press"` (Approach choice from the 5 options)
- `phase_4 := { primary: "Kinetic", split: 70/30, secondary: "Intent" }` (attention allocation)
- `phase_5 := { action: "thrust", depth: 3 }` (Commit class + depth)
- `phase_5 := { technique: "Counter-thrust" }` (named technique reference — uses character's trained techniques from §5.5; technique declarations include their own canonical class+depth from §5.5)
- `phase_5 := { thread_op: "Mend", target: "self_wound" }` (Thread-op commit)
- `phase_5 := { tier4_preempt: true, target_class: "thrust" }` (Tier 4 Intent Reading Pre-empt activation; requires Intent Reading Tier 4+ per §10.2)
- `phase_6_default := { sub_action: "Yield", on_state: "in-bind" }` (default sub-action per engagement state)
- `phase_6_default := { technique: "Indes (in-tempo strike)" }` (named technique reference for Bout sub-action)
- `phase_7 := "Clean withdrawal"` (Disengage choice from the 5 options)
- `phase_8 := { stance: "Centered guard" }` (Phase 8 stance return)

**Position naming note.** Position is described abstractly in §4.3 (stance-narrowed options; multi-attack-affording vs single-attack-affording); the engine surfaces specific Position options at the UI layer per current Stance + Weapon Class. CLP rules may reference Position by intent (`thrust-line`, `cut-line`, `parry-ready`, etc.) rather than discrete names, with engine resolving to the available option matching that intent.

**Override actions:**
- `prefer_disengage` (raises Phase 7 weight; engine prefers Phase 7 even from non-default trigger)
- `refuse_bout_entry` (engine refuses to enter Phase 6 Bout; if forced, takes Phase 7 even after Phase 5 commit lands)
- `force_player_decision` (pauses engine; surfaces full player UI for the matching phase)
- `escalate_depth(+N)` / `cap_depth(N)` (modifies Phase 5 Commit depth selection)
- `cap_chain_length(N)` (modifies Phase 6 Bout chain cap)

**Compound actions:**
- Multiple `phase_X := Y` declarations may chain in a single rule (one rule sets behavior for multiple phases)

#### 6.10.5 Default profile per Tradition

Each Tradition provides a default CLP that a character inherits when first acquiring the History. Players modify from there.

**Default profile — Long-thrust dueling tradition:**

```
[priority 1]
WHEN wounds >= max - 1 AND concentration < 30%
THEN phase_7 := "Clean withdrawal"
ALSO force_player_decision  // critical state, hand to player

[priority 2]
WHEN opponent.commit_class = "thrust" AND last_read.success
THEN phase_5 := { technique: "Counter-thrust" }  // Long-thrust dueling Journeyman tech §5.5.1

[priority 3]
WHEN opponent.signal = "low"
THEN phase_3 := "Feinted approach"
ALSO phase_4 := { primary: "Intent", split: 70/30, secondary: "Kinetic" }

[priority 4]
WHEN bout_state = "in-bind" AND bout_steps >= 2
THEN phase_6_default := { sub_action: "Disengage", on_state: "in-bind" }

[priority 5]  // default opening
WHEN passes_elapsed = 0
THEN phase_1 := "Forward-point guard"
ALSO phase_2 := "thrust-line"
ALSO phase_3 := "Direct press"
ALSO phase_5 := { action: "thrust", depth: 3 }
```

**Default profile — Counter-time tradition:**

```
[priority 1]
WHEN wounds >= max - 1
THEN phase_7 := "Defensive disengage"
ALSO force_player_decision

[priority 2]
WHEN opponent.depth >= 4 AND last_read.success
THEN phase_5 := { technique: "Counter-thrust deflection" }  // Counter-time Journeyman tech §5.5.1
// Counter-time's signature — opponent's deep commit is the trigger

[priority 3]
WHEN passes_elapsed = 0
THEN phase_1 := "Centered guard"
ALSO phase_3 := "Drawing approach"  // draws opponent into commitment

[priority 4]
WHEN bout_state = "closing"
THEN phase_4 := { primary: "Kinetic", split: 50/50, secondary: "Intent" }
// reads opponent's commit timing

[priority 5]
WHEN intent_tier >= 4 AND last_read.overwhelming
THEN phase_5 := { tier4_preempt: true, target_class: "thrust" }  // Tier 4 Pre-empt ability §10.2
```

**Default profile — Conditioning-and-grappling tradition:**

```
[priority 1]
WHEN wounds >= max - 1
THEN phase_7 := "Clean withdrawal"
ALSO force_player_decision

[priority 2]
WHEN bout_state = "closing"
THEN phase_6_default := { sub_action: "Tie Up", on_state: "closing" }

[priority 3]
WHEN opponent.wounds >= max - 1 AND scene.context != "lethal"
THEN phase_6_default := { sub_action: "Tie Up at Pinning grip", on_state: "in-bind" }
// uses Master technique if available

[priority 4]
WHEN passes_elapsed = 0
THEN phase_1 := "Centered guard"
ALSO phase_3 := "Direct press"
ALSO phase_5 := { action: "close", depth: 2 }
```

#### 6.10.6 Player customization

The CLP UI surfaces the rule list as:
- **List view**: rules in priority order; drag-to-reorder; one-line summary of each
- **Rule editor**: per-rule deep edit; condition builder with predicates from §6.10.3 catalog; action builder from §6.10.4
- **Test mode**: simulate combat scenarios; show which rule fires for each phase
- **Template browser**: import default profiles from any Tradition the character has Tradition Depth in; cross-faction profiles importable at Standing ≥ 3 with the faction
- **Conditional Logic Profile sharing**: export/import between save files (per-character behavior templates)

#### 6.10.7 Validation rules

- Rules referencing aspect specializations not trained by the character are flagged on save (e.g., "Counter-thrust" requires Counter-time Tradition Depth 2; CLP referencing it without that depth produces a non-firing rule)
- Rules with circular references (rule A modifies state that triggers rule A) are flagged
- Rules that conflict in their actions (e.g., two rules both setting phase_5 with same priority) fire the rule appearing first in the list
- Maximum CLP size: 32 rules (UI / cognitive limit; sim-tunable)
- Conditions must reference only documented predicates; custom predicates require code-side extension

#### 6.10.8 Open items (I-14b)

- Concrete UI design (mock-up, interaction patterns)
- Rule conflict resolution edge cases (priority ties, action conflicts)
- AI-side: how does engine optimize a Conditional Logic Profile for an NPC during runtime (caching, evaluation order)
- Cross-character profile portability (does a profile written for a Long-thrust duelist make sense if copied to a Counter-time fencer character?)

In tactical-mode play (auto-resolved Phase 4–7), the Conditional Logic Profile drives engine choices. In manual-mode play (all phases player-controlled), the Profile remains as fallback for non-controlled NPCs.

### 6.11 Trained pool vs equipped loadout

The aspects above (§6.1–6.10) describe a character's **trained pool** — everything they have learned across their Histories. v32 adds an **equip** step (Pillar 2, 6): before a fight the player equips a *subset* of the trained pool as the active combat **loadout**. This is the front-end-strategy surface — the analogue of choosing weapon + kit before an engagement — and it is where build-level decisions are made, keeping the in-bout experience clean.

**6.11.1 The distinction.**
- **Trained pool** — all specializations the character has, each with its Aspect Proficiency (0–5), grown through use, capped by History points. Broad; persistent.
- **Equipped loadout** — the active configuration of aspect slots for *this* fight: which specialization fills each of the 10 slots, plus the equipped weapon (§8) and its handling profile. Re-equipped freely **between** fights; **fixed for the duration of a bout** (no mid-bout swapping — stance/position/approach choices happen *within* the equipped configuration). A character can carry several saved loadouts and pick one at engagement start.
- Per-aspect Proficiency contributes to the relevant state-transition Pools only for the *equipped* specialization in each slot.

**6.11.2 Named sets and set bonuses.** Coherent loadouts — the Synergistic-dense clusters §7.3 referenced — are recognized as **named sets** granting a σ-space **set bonus** (state-gated, §12.3) surfaced to the player as a named advantage rather than a sum of pair contributions:

| Set | Core equipped aspects | Set bonus (σ-space, state-gated) | Weapon affinity (§8) | Inherent tension |
|---|---|---|---|---|
| **Thrust Duelist** | Forward-point Stance · Linear Footwork · Standard grip · Direct/Explosive Approach · Kinetic Reading · Hand-led Reaction · Decisive Commitment · Clean Disengage | +Moderate on Thrust commits at **Closing** | Long thrust-primary | — |
| **Bind Fighter** | Centered/Raised Stance · Linear Footwork · Standard grip (Half-grip-available) · Direct-press Approach · Tactile Reading · Patterned Anticipation · Yielding Reaction · Sustained Commitment | +Moderate on Wind/Press/Yield at **In-bind** | Long cut-and-thrust | — |
| **Counter-time** | Centered/Side Stance · Linear Footwork · Drawing Approach · Kinetic Reading · Reactive Anticipation · Hand-led counter Reaction · Cautious Commitment | +Strong on reactive sub-actions **when a Reading channel succeeded** (else +0) | Long thrust-primary | — |
| **Burst** | Bursting Footwork · Explosive Approach · Burst Commitment · Sudden Disengage | +Strong on the **opening Closing transition**; no In-bind bonus (intentionally short-engagement) | Single short / Paired short | — |
| **Continuous-flow** | Side guard (stance-flux) · Triangular Footwork · Paired grip · Angled Approach · Rhythmic Reading · Voiding Reaction · Sustained Commitment · Sudden Disengage | +Moderate on consecutive sub-actions / Voiding flow | **Paired short (required)** | Commitment × Disengage (Sustained + Sudden) — characteristic whiplash cost |

**Partial credit (N4 — cliff smoothing).** A **full set** (all core aspects equipped) grants its stated bonus; a **near-set** (exactly one core aspect missing) grants the bonus **one level lower** (Strong→Moderate→Minor→none); fewer than that grants nothing. This softens the build-axis cliff the NERS test flagged (N4, Lesson 6) — a near-complete build is rewarded proportionally instead of falling off a wall — while staying legible: the player reads "near Bind Fighter: +Minor in-bind" vs the full "Bind Fighter: +Moderate." It does **not** reintroduce per-pair computation: credit is keyed to the named set, not to aspect-pair synergies. The choice is self-consistency with the armature's own A2 (saturating, no cliff) applied to the build axis. Set-bonus magnitudes draft; sim-tunable Phase 14. *(A fully-graded bonus — scaling with fraction-of-set — would smooth further per A2 but trades legibility; the 2-step form is the legibility/smoothness balance, and is Jordan-revertible to all-or-nothing if pure legibility is preferred.)*

**6.11.3 Incompatibility warnings.** The two antagonisms §7.3 lists are surfaced at **equip time**, not recomputed per bout. If a loadout equips both members of an antagonistic pair, the equip screen flags it and the −Moderate (δσ −0.5) penalty applies whenever both co-fire on a sub-action:
- **Anticipation × Reaction** — e.g., Predictive Anticipation + Reactive Reaction (contradictory mental model).
- **Commitment × Disengage** — e.g., Sustained Commitment + Sudden Disengage (the Continuous-flow set's built-in cost) or Burst Commitment + Defensive Disengage.

These are *playable* — a player may accept a tension for the rest of a set's strengths (Continuous-flow does exactly this) — but they are never silent. There is **no general 36-pair computation**: only named-set bonuses (6.11.2) and these flagged antagonisms (6.11.3) affect coherence.

---

## 7. MATCHUP SYSTEMS (σ-SPACE MODIFIERS)

Three tables produce **modifiers** applied at Phase 5 Commit and Phase 6 Bout sub-action resolutions. Per Pillar 7, all modifiers operate in σ-space within canonical Ob grammar (§12.3).

### 7.1 Stance Counter Matrix (authored — does not derive)

Per-stance × per-stance σ-space modifier, **state-gated to the Closing state** (§12.3) and persisting from Phase 1 stance until stance changes. Anti-symmetric (cell [A][B] = −cell [B][A]); diagonal = 0.

**Why authored.** Unlike Reaction (§7.2, derives cleanly) and coherence (§7.3, mostly derives), the Stance Counter **resists reduction to a low-dimensional model**: Hodge decomposition shows it is ≈85% cyclic (rock-paper-scissors), only ≈15% transitive, and an interpretable low-D wheel reproduces only 19/25 cells. Two hard counters (±2) both involve Forward-point, and no smooth low-D model places two hard counters on one stance. It is kept as an authored 5×5 table by design (designs/audit/2026-05-28-combat-reframe/matchup_derivation_analysis.md). State-gating is what reduces its in-bout load, not derivation.

| Aggressor ↓ vs Defender → | Centered | Raised | Low | Side | Forward-point |
|---|---|---|---|---|---|
| Centered | 0 | +1 | 0 | −1 | +2 |
| Raised | −1 | 0 | +1 | 0 | +1 |
| Low | 0 | −1 | 0 | +1 | 0 |
| Side | +1 | 0 | −1 | 0 | −2 |
| Forward-point | −2 | −1 | 0 | +2 | 0 |

**Reading:** values are *legacy Ob magnitudes* mapped to σ-space levels for §12.3 (±1 → Moderate 0.5δσ; ±2 → Strong 0.75δσ; sign: negative = Aggressor advantaged). Forward-point vs Centered (−2 → Strong, Aggressor favored: straight thrust against open guard); Side vs Forward-point (−2 → Strong, Side answers Forward-point). Magnitudes draft; Phase 11 sim tunes to Fast-vs-Titan 50–60%.

### 7.2 Reaction modifier — 2-parameter formula (derived)

v31 used a 5×4 table (Defender's Reaction × Aggressor's commit depth). The derivation found this **reduces cleanly to two interpretable parameters per reaction** — a baseline and a depth-slope — reproducing 18/20 cells within ±0.5 (rank-2 embedding: 20/20). So v32 replaces the table with a formula:

```
Reaction δσ = baseline_r + slope_r · (depth − 3)        depth ∈ {1..5}, centred at Committed (3)
(σ-space, fed to §12.3; positive δσ = Defender advantaged / raises Aggressor Ob)
```

The slope sign encodes a **physical family**:
- **Punishes hesitation** (slope < 0 — strongest vs light/probing commits, fades vs deep): Voiding, Pressing, Hand-led. These beat tentative attacks and are overrun by full commitment.
- **Punishes overcommitment** (slope > 0 — weak vs light, strongest vs deep/full): Body-led, Yielding. These turn an overcommitted opponent's force back (Yielding vs Full is the archetype).

| Reaction | baseline_r (δσ) | slope_r (δσ/depth) | family | reproduces (v31 intent) |
|---|---|---|---|---|
| Voiding | +0.40 | −0.35 | punishes hesitation | strong vs probe, weak vs full |
| Pressing | +0.30 | −0.25 | punishes hesitation | strong early, fades deep |
| Hand-led | 0.00 | −0.25 | punishes hesitation | deflects light, can't stop deep |
| Body-led | +0.10 | +0.15 | punishes overcommitment | needs depth to engage |
| Yielding | +0.10 | +0.35 | punishes overcommitment | reversal vs full |

Two interpretable parameters per reaction replace twenty hand-set cells; the families are legible to the player (and gate which reactions a stance prepares, §11.2). Exact parameters draft; sim-tunable I-17.

### 7.3 Aspect coherence — named sets (derived) + exceptions

v31 carried a hand-authored 36-pair aspect-coherence matrix (9 operational aspects, ±0.5 Pool per Synergistic/Antagonistic pair). The derivation found coherence is **mostly low-rank**: a rank-2 embedding reproduces ~86% of the pairwise structure, and the Synergistic-dense regions *are* the recognizable historical styles. So v32 replaces the matrix with two pieces:

**(a) Named loadout sets carry the synergies (§6).** The coherent clusters the matrix surfaced — Thrust Duelist, Bind Fighter, Counter-time, Burst, Continuous-flow — become **equipped loadout sets** with explicit set bonuses (§6.x). Equipping a coherent set grants its bonus (a σ-space set-bonus modifier, §12.3); the player reads "Bind Fighter set: +Moderate in-bind" instead of summing 0.5-Pool pair contributions. This is the front-end-strategy framing (Pillar 2, 6): coherence is a build/loadout property, surfaced as named bonuses, not an in-bout per-pair computation.

**(b) Hand-listed antagonism exceptions.** Two pairings do **not** fold into the low-rank/set structure — they are genuine cross-cluster tensions the rank-2 embedding leaves as residual, and they stay explicit:

| Antagonistic pair | Why it resists the set structure | Effect |
|---|---|---|
| Anticipation × Reaction | Pre-commit prediction vs in-bout reflex pull cognitive resources opposite ways (Predictive Anticipation + Reactive Reaction is a contradictory mental model) | −Moderate (δσ −0.5) when both co-fire on a sub-action |
| Commitment × Disengage | Commit depth and willingness to break inversely related at extremes (Burst Commit + Defensive Disengage; Sustained Commit + Sudden Disengage = whiplash) | −Moderate (δσ −0.5) when both co-fire |

A loadout that combines a named set with one of these antagonisms (e.g., the Burst set inherently carries Commitment × Disengage) accepts the tension as the archetype's characteristic cost — flagged at equip time (§6), not recomputed per bout. No general 36-pair matrix is retained; the named sets plus these two exceptions are the playable baseline. Set-bonus and exception magnitudes draft; sim validation Phase 14.

---

## 8. WEAPON CLASSES (PHASE-KEYED STRENGTHS)

**Seven weapon classes.** Each maps to the canonical 3-axis weapon TN matrix (combat_v30 §5: Reach × Weight × Type) and adds phase-keyed Pool/TN modifiers.

### 8.1 Canonical mapping + base TN

| Class | Canonical Reach × Weight × Type | Base Hit TN | Min STR | Examples |
|---|---|---|---|---|
| Long thrust-primary | Long × Light × Blade | 6 | 2 | Rapier, smallsword, estoc, light lance |
| Long cut-and-thrust | Long × Heavy × Blade | 7 | 3 | Longsword, hand-and-a-half, federschwert |
| Curved cut-primary | Long × Light × Blade | 6 | 2 | Saber, cavalry saber, kilij |
| Long pole (spear) | Long × Light × Blade | 6 | 2 | Spear, pike, partisan |
| Long pole (staff) | Long × Light × Blunt | 7 | 2 | Quarterstaff, bo |
| Paired short | Short × Light × Blade (×2) | 5 each | 1 | Dagger pair, paired short swords |
| Single short | Short × Light × Blade | 5 | 1 | Dagger, short sword, arming sword (in close-grip) |
| Long Heavy Blunt | Long × Heavy × Blunt | 8 | 4 | War hammer, pollaxe, poleaxe (STR ×3 multiplier per canon §5) |

### 8.2 Weapon handling (ease-of-use)

Weapon choice changes not only reach, damage, and engagement profile but the **skill curve** — how a fighter's per-weapon Proficiency converts into effective contribution. Each class has a handling profile that maps Proficiency `P` (0–7, the character's trained proficiency with that weapon class) to an effective handling value `H` fed into the relevant sub-action/Commit Pools:

| Profile | H(P) | Character |
|---|---|---|
| **Forgiving** | `min(P + 1, 3)` | early competence, low ceiling — accessible to generalists |
| **Standard** | `min(P, 4)` | linear, moderate ceiling |
| **Demanding** | `min(max(P − 1, 0), 5)` | punishes low skill, high ceiling — rewards specialization |

Handling value by Proficiency (verified):

| P | Forgiving | Standard | Demanding |
|---|---|---|---|
| 1 | 2 | 1 | 0 |
| 2 | 3 | 2 | 1 |
| 3 | 3 | 3 | 2 |
| 4 | 3 | 4 | 3 |
| 5 | 3 | 4 | 4 |
| 6 | 3 | 4 | 5 |
| 7 | 3 | 4 | 5 |

**Crossover at P ≈ 4** (verified): below 4, a Forgiving weapon out-delivers a Demanding one for the same Proficiency; at 4 they tie (H=3); above 4 the Demanding weapon pulls ahead (ceiling 5 vs 3). This is the front-end-strategy lever on the *build* axis (Pillar 2, 6): a low-investment or generalist character is better served by a Forgiving weapon; a specialist who pushes Proficiency high is rewarded by a Demanding one. Note the structural echo of MaxWounds/Power (floor/ceiling stepping on a 1–7 stat) — the same design grammar applied to weapon mastery.

**Provisional class assignments** (sim-tunable, Phase 11):

| Class | Handling | Rationale |
|---|---|---|
| Long thrust-primary | **Demanding** | rapier/smallsword precision punishes the unskilled, rewards mastery |
| Long cut-and-thrust | Standard | versatile longsword, moderate curve |
| Curved cut-primary | Standard | saber, moderate curve |
| Long pole (spear) | **Forgiving** | reach + simple thrust = early competence, lower ceiling |
| Long pole (staff) | **Forgiving** | accessible percussive control |
| Paired short | **Demanding** | two-blade coordination punishes low skill |
| Single short | **Forgiving** | simple, close, accessible; low ceiling |
| Long Heavy Blunt | **Demanding** | knightly armored-combat weapon (cf. Le Jeu de la Hache); high STR floor, high mastery ceiling |

Handling H feeds the weapon's contribution to Commit/sub-action Pools (replacing a flat weapon-proficiency term for weapon-dependent actions). Exact Pool-coupling and assignments draft; sim-tunable I-17.


### 8.3 Damage modifier vs armor (canonical combat_v30 §5)

Each weapon class inherits canonical weapon-modifier-vs-armor-tier. No change to canon.

| Class | vs None | vs Light | vs Medium | vs Heavy |
|---|---|---|---|---|
| Long thrust-primary (Light Blade) | +3 | +2 | +1 | +0 |
| Long cut-and-thrust (Heavy Blade) | +6 | +4 | +2 | +0 |
| Curved cut-primary (Light Blade) | +3 | +2 | +1 | +0 |
| Long pole spear (Light Blade) | +3 | +2 | +1 | +0 |
| Long pole staff (Light Blunt) | +3 | +3 | +3 | +3 |
| Paired short (Light Blade ×2) | +3 each | +2 each | +1 each | +0 each |
| Single short (Light Blade) | +3 | +2 | +1 | +0 |
| Long Heavy Blunt (Heavy Blunt) | +5 | +5 | +5 | +5 |

**Heavy plate — closed (I-13b).** Light/medium blades hit Heavy plate at +0 weapon modifier (cannot wound through plate on the modifier alone). v32 closes this two ways: (1) the **Long Heavy Blunt** class above (+5 vs *all* tiers — concussive force transmits through plate; STR ×3, TN 8) — the *bring-the-right-tool* answer; (2) the **Targeted-line** sub-action (§12.4) — the *skill-instead-of-tool* answer: a precise thrust to an armor gap (visor, armpit, groin, joint) that recomputes damage against a lower armor tier at a precision penalty. A light-weapon fighter is no longer helpless against plate — they pay in precision (Targeted-line) where the Heavy-Blunt fighter pays in speed (TN 8, slow).

### 8.4 Phase-keyed Pool/TN modifiers

| Class | Strong phases (+0.5D Pool at action class) | Weak phases (−0.5D Pool) | Foreclosed sub-actions | Weapon Speed |
|---|---|---|---|---|
| Long thrust-primary | Phase 2 Position (precise telegraphing); Phase 3 Approach (lunge bonus); Phase 5 Commit (thrust class) | Phase 6 Bout (in-bind handling: degraded grip control on a thrust weapon) | Sustained-bind sub-actions (Wind, sustained Press); Grip-change without Half-grip-available | +1.5 |
| Long cut-and-thrust | Phase 6 Bout (Cut, Wind, Press sub-actions); Phase 5 Commit (depth ≥3 with Heavy Blade STR multiplier) | Phase 3 Approach (heavier weapon, slower close) | Sudden disengage at depth 5 (committed Heavy Blade is hard to abort) | +0.5 |
| Curved cut-primary | Phase 3 Approach (continuous-cut entry); Phase 5 Commit (cut class) | Phase 6 Bout (limited binds; curved blade slides out of contact) | Half-sword grip; Sustained-bind sub-actions | +2 |
| Long pole (spear) | Phase 2 Position (reach advantage); Phase 3 Approach control (zone distance) | Phase 6 Bout (close-range disadvantaged); Phase 6 In-bind precision | In-bind precision sub-actions (Wind requires shorter weapon); Throw-strike at close range | 0 |
| Long pole (staff) | Phase 2 Position; Phase 6 Bout Press/Displace (Blunt force in bind) | Phase 5 Commit (no cutting; lower wound transition rate) | Cut/Thrust sub-actions; weapon is Blunt only | 0 |
| Paired short | Phase 6 Bout (flow — both blades active); Reaction sub-actions (off-hand parry) | Phase 5 Commit (no decisive single strike with one blade) | Depth-5 Commits (Paired short cannot achieve full-commit decisive strike); Grip-change (paired grip locked) | +2.5 |
| Single short | Phase 6 Bout (close-range); Reaction speed | Phase 3 distance control (short reach loses zone) | Reach-dependent options (cannot engage at Long Reach without closing) | +3 |
| Long Heavy Blunt | Phase 5 Commit (depth ≥3, STR ×3 concussive); Phase 6 Press/Displace (plate-cracking force in bind) | Phase 3 Approach (slow, heavy); Reaction speed (slowest) | Fine in-bind precision (Wind); fast Void; Sudden disengage at depth ≥4 | −0.5 |

### 8.5 Sub-actions available per weapon class

Cross-reference §12.1 (engagement state × sub-action options). Weapon class **restricts** which sub-actions are surfaced from the option set:

| Class | Bout sub-actions available |
|---|---|
| Long thrust-primary | Cut (light only, low net damage); **Thrust (preferred)**; Yield; Void; Disengage; **NO** Wind, Press (extended), Grip-change without Half-grip |
| Long cut-and-thrust | **Cut; Thrust; Wind; Yield; Press; Displace; Grip-change** (Half-grip-available unlocks); Break-bind; Throw-strike; Disengage |
| Curved cut-primary | **Cut (preferred)**; Thrust (limited); Yield; Press (limited); Void; Disengage; NO Wind, Grip-change |
| Long pole (spear) | **Thrust (preferred at reach)**; Cut (limited); Displace; Throw-strike (with shaft); Disengage; **NO** in-bind precision (Wind, Yield) |
| Long pole (staff) | Cut (Blunt force); **Press (preferred)**; Displace; Throw-strike; Disengage; NO Thrust, Wind, Grip-change |
| Paired short | Cut; Thrust; **Coordinated sub-actions (both blades fire — counts as one declaration)**; Void (speed); Yield; Disengage; NO depth-5 commits; NO Wind without specific Paired-Wind technique |
| Single short | Cut; Thrust; **Void (preferred)**; Yield; Disengage; NO Sustained-bind, NO Grip-change |
| Long Heavy Blunt | **Press (preferred, concussive); Displace; Cut (blunt); Thrust (spike/beak); Targeted-line (spike to gap, §12.4)**; Grip-change (half-haft); Break-bind; NO fine Wind; NO fast Void |

### 8.6 Cross-armor combat considerations

- **Heavy plate vs Heavy plate**: combat keys to seeking gaps (grip-change, half-sword, grappling sub-actions); Long cut-and-thrust + Half-grip-available aspect is the canonical answer
- **Light vs Heavy plate**: the light attacker now has two answers (I-13b, specified): the **Targeted-line** sub-action (§12.4 — gap-thrust, precision penalty, recompute vs a lower armor tier), or switching to the **Long Heavy Blunt** class (§8.1, +5 vs all tiers). Without either, reduced consequence per the canonical weapon-modifier table — many sub-actions land, no wound transition
- **Heavy plate's Stamina tax**: per canonical derived_stats §4.2 + this proposal §9.1, Heavy plate +2 Stamina per phase action. Sustained engagement against Light attacker depletes Heavy-plate Stamina before wounds accrue. Stamina-economy fighter (Sustained Commitment) in Light armor may outlast Heavy plate

### 8.7 Weapon-class fit with combat Histories

| Class | Best-fit Traditions |
|---|---|
| Long thrust-primary | Long-thrust dueling; Long-thrust geometric; Counter-time (Forward-point stance + Linear footwork standard set) |
| Long cut-and-thrust | Long-blade contact; Single-strike (specifically when paired with depth-keyed striking) |
| Curved cut-primary | Curved-blade cavalry; Continuous-flow (continuous cuts + Triangular footwork) |
| Long pole | Formation-and-discipline (formation pole arms); Mounted multi-weapon (lance variant) |
| Paired short | Continuous-flow (paired grip + Triangular footwork); Conditioning-and-grappling (off-hand for grappling support) |
| Single short | Conditioning-and-grappling (close-range backup); any tradition for off-hand backup |
| Long Heavy Blunt | Conditioning-and-grappling (armored close combat); Formation-and-discipline (poleaxe in the line) |

Wielding a weapon outside its best-fit Tradition is mechanically suboptimal — the character's aspect specializations don't reinforce the weapon's strong phases. Possible but penalized.

### 8.8 Sim validation

Phase 11 sim (I-17 post-pivot) validates that weapon class differentiation produces distinct viable builds — Fast (Single short, Paired short) vs Strong (Long cut-and-thrust) vs Reach (Long pole) vs Plate-breaker (Long Heavy Blunt) at 50–60% balance across symmetric optimization.

Phase 11b sim (open, I-13b): validates per-armor weapon balance — does Long cut-and-thrust dominate against Heavy plate? Does Long pole (staff Blunt) provide a viable anti-armor option? Targeted-line sub-action (gap-seeking) needs specification before this sim runs.

---

## 9. ARMOR AND WOUND DISPLAY

### 9.1 Armor levels (canonical)

Four levels per canonical combat_v30 §6. **No new mechanics added**; sensor channel degradation noted from the proposal §7 is added as a small extension.

| Armor | STR Min | Stamina Mod | Sensor channel degradation (new) |
|---|---|---|---|
| None | — | +0 | None |
| Light | 2 | +0 per action | −0.5D to Tactile channel (glove limits) |
| Medium | 3 | +1 per action | −0.5D to Tactile, −0.5D to Geometric (helmet limits visual) |
| Heavy plate | 4 | +2 per action | −1D to Tactile, −1D to Geometric, −0.5D to Intent (helmet vision-limit); unlocks half-sword grip via Half-grip-available aspect |

Damage Reduction (DR) per canonical weapon-modifier-vs-armor-tier table (combat_v30 §5 Damage Resolution + §6 Armour). No change.

**Cross-armor implications** (preserved from proposal §7):
- Heavy plate vs Heavy plate: combat keys to seeking gaps (grip-change, half-sword, grappling sub-actions)
- Light vs Heavy: light attacker must seek joint/gap lines (Targeted-line sub-action, Pass 2c) or fail to wound

### 9.2 Wound display layer (3 perceptual states over canonical 4-wound math)

Canonical Wound math (derived_stats §4.1) tracks Wound count 0 through MW+1 (Felled). For End 1, max wounds before Felled = 2; for End 4, max = 4. The math produces 2–5 numerical wound states across the Endurance range.

**Display layer compresses to 3 perceptual states** for UI clarity and Phase 5/Phase 1 filter rules. Canonical Wound count is the underlying state; display computes from it:

| Perceptual state | Trigger | Canonical Wound count |
|---|---|---|
| Unwounded | 0 wounds | 0 |
| Wounded | 1 wound (any End) | 1 |
| Wounded (extended for End 4–7) | 2 wounds for End 4–7 (MW=3) | 2 |
| Heavily wounded | 2 wounds for End 1–3 (MW=1 or 2); 3 wounds for End 4–7 (MW=3) | 2 or 3 |
| (Felled — canonical ending) | MW+1 wounds | per canon |

**End-range caveat.** For End 1 characters (MW=1, Felled at 2 wounds), only 2 perceptual states exist pre-Felled: Unwounded and Wounded. No Heavily Wounded category — the character is either Wounded or Felled. The 3-state UI compression naturally degrades to 2-state for these characters.

**Mechanical effects per perceptual state:**
- **Unwounded**: no penalty (canonical: −1D per Wound; here zero)
- **Wounded**: −1D Combat (per canonical −1D per Wound × 1); Phase 5 Commit depth cap reduced by 1
- **Heavily wounded**: −2D Combat (canonical sum × 2); Phase 5 Commit depth cap reduced by 2; Stance options narrow by ~50% (advanced stances unavailable)

This **does not modify the canonical wound math**; the canonical −1D-per-wound penalty (PP-716, derived_stats §4.1) governs Pool reductions. The 3-state display is purely UI compression.

---

## 10. INTENT READING TRACK

Reading Intent is the foundational perceptual discipline of pre-motor opponent reading. Per Jordan canonical override (2026-05-XX), Intent maintains its own progression track and unlocks specific abilities at training tiers — separate from the Reading aspect's other channels (Tactile, Kinetic, Geometric, Rhythmic, Thread).

### 10.1 Why separate

Intent Reading is qualitatively distinct from the other Reading sub-channels. Where Tactile reads pressure and Geometric reads positions, Intent reads the *pre-motor state* — what opponent is about to do, before their body commits. This requires perceptual training that doesn't transfer from general martial proficiency. A master swordsman who never studied fühlen-equivalent Intent reading may have all four mundane channels at Master tier (5) Aspect Proficiency and Intent at Surface (1) on this track.

### 10.2 Track structure

**0–5 scale.** Parallels Tradition Depth structure. Each tier unlocks Intent Reading Pool magnitude and specific abilities. Progression is **not** use-based; advancement requires explicit training time + History point investment + per-tier prerequisites.

| Tier | Name | Intent Reading Pool | Specific ability unlocked (cumulative) |
|---|---|---|---|
| 0 | Untrained | Channel unavailable as primary. Available only as secondary at Phase 4 attention split, rolling `Cog` (single, no track contribution). | — |
| 1 | Surface | `Cog × 2 + 1` | **Channel available as primary.** Reading peak reveals opponent's likely Phase 5 commit *class* (cut / thrust / Thread-op), no depth/specifics. |
| 2 | Steady | `Cog × 2 + 2` | **Sustained Read.** Intent channel keeps reading across Phase 6 Bout (normally only Tactile reads in-bind). Reveals opponent's chain-step commit class one sub-action ahead. Reading peak now reveals commit class + commit depth. |
| 3 | Counter-deception | `Cog × 2 + 3` | **False Read Counter.** When opponent uses Feinted approach or low-signal Position (Signal Level penalty applies to other Reading channels), Intent channel ignores the Signal Level penalty and produces full read. *Sustained Read carried forward.* |
| 4 | Pre-empt | `Cog × 2 + 4` | **Pre-empt.** On successful Phase 4 Intent read (Reading Pool net successes ≥ 3 against opponent's Signal), perceiver gains a free Phase 5 Commit at probe depth (depth 1) **before opponent's Phase 5 fires**. Implements counter-time at the perceptual layer — opponent's commit is interrupted by perceiver's pre-emptive action. Costs 2 Concentration. *Sustained Read + False Read Counter carried.* |
| 5 | Master (peak fühlen) | `Cog × 2 + 5` | **Conviction Read** (1× per duel, in any phase): perceiver reads one active Conviction of opponent (player_agency §2). Reveals one Code-generating Conviction or Duty (§12), exposing one foreclosed-action set. **Intent Cascade**: Pre-empt extends to preparatory depth (depth 2) free commit; carries Pre-empt, False Read Counter, Sustained Read. |

### 10.3 Progression gates

| Advancing to | Prerequisites |
|---|---|
| Tier 1 (Surface) | Find a Tier 1+ teacher; invest 1 History point |
| Tier 2 (Steady) | Tier 1 sustained for 1 in-game season; invest 1 History point |
| Tier 3 (Counter-deception) | Tier 2 sustained for 1 in-game season; tutor at Tier 3+; 2 History points |
| Tier 4 (Pre-empt) | Tier 3 sustained for 2 in-game seasons; tutor at Tier 4+; 3 History points; one prior dueling experience at Wounded or higher |
| Tier 5 (Master) | Tier 4 sustained for 3 in-game seasons; Master tutor; 5 History points; one prior dueling experience at Heavily Wounded |

**History point cost:** Intent Reading track consumes History points but doesn't constitute its own History — points come from any combat History the character holds. A character cross-training Counter-time tradition may invest History points there toward Intent Reading advancement.

### 10.4 Tradition teaching tiers

Per §5.2, traditions teach Intent Reading at the following tier caps. A character can advance further only with a non-Tradition tutor at the higher tier.

| Tradition | Teaches Intent up to |
|---|---|
| Long-blade contact | Tier 1 (Surface) |
| Long-thrust dueling | Tier 2 (Steady) |
| Long-thrust geometric | Tier 1 (Surface) |
| **Counter-time** | **Tier 4 (Pre-empt)** — central discipline |
| **Single-strike** | **Tier 5 (Master)** — foundational discipline |
| Curved-blade cavalry | Tier 1 (Surface) |
| Continuous-flow | Tier 2 (Steady) |
| Mounted multi-weapon | Tier 2 (Steady) |
| Conditioning-and-grappling | Tier 1 (Surface) |
| Formation-and-discipline | Tier 1 (Surface) |

### 10.5 Integration with attention split

Intent Reading at Tier 1+ can be primary or secondary channel per Phase 4 attention split (§4.5):
- As primary at full attention: full Pool
- As secondary at 30/70 split: Pool × 0.3 rounded down
- As reserve (50/50 Phase 4 / Phase 6): full Pool × 0.5 fires Phase 4; Pool × 0.5 held for Bout sensor-read trigger

**Abilities unlocked at tier still apply regardless of attention level.** A Tier 4 perceiver with Intent as secondary may still trigger Pre-empt if Pool × 0.3 net successes ≥ 3 — high tier, harder to clear with reduced Pool but possible.

### 10.6 Conviction Read (Tier 5) and player agency integration

Tier 5 Conviction Read produces a substantial cross-system effect. When fired (1× per duel):

1. Perceiver chooses one active Conviction of opponent to read
2. Engine reveals whether that Conviction has a Code-generating effect on combat (per §12 Authored honor-code scene contexts) or modifies depth/action availability
3. Perceiver gains *information* — knows opponent's foreclosed action set for the duel
4. **Strain effect on opponent**: opponent's read Conviction takes 1 Conviction Scar per player_agency §2.3 (witnessing one's own conviction read by an opponent is a kind of confrontation)

Conviction Read is *not* a Thread operation — it requires no TS. Master Intent reading is a learned perceptual capacity. (P-15 layer-2 self-apperception via mundane training.)

### 10.7 Open items

- Concrete History-point cost scaling vs Tradition Depth investment (I-12 closure)
- Mentor-relationship requirements at Tiers 3–5 (cross-ref character_generation_questionnaire)
- Pool magnitudes (`Cog × 2 + tier`) pre-sim — Phase 11 (I-17) validates Intent build against non-Intent-trained opponents

---

<!-- §§11–15 in Pass 2 turn 2c -->

---

## 11. COMBAT STATE VARIABLES

Five continuous state variables run throughout an engagement. They update across phases and modify decision outcomes. Cross-references to phases where each is set/consumed.

### 11.1 Reading

Quality of the character's current sensor-channel information about opponent. Defined and detailed in §4.5 (Phase 4 Reading peak) and §6.5 (Reading aspect).

**Builds across Phases 1–3** (ambient observation; Geometric channel in Phases 1–2; Kinetic at Phase 4 measure).
**Peaks at Phase 4** before Commit.
**Updates from Phase 6 Bout** (Tactile in bind-active states; Intent at Tier 2+ Sustained Read).
**Partial reset in Phase 7–8** (sensor-channel state preserved selectively; Rhythmic channel reads persist across passes).

Reading produces a **Reading-modifier** — a σ-space δσ contribution (§12.3) on opponent's Commits and Bout sub-actions, per §4.5 net-success table. Sight-mediated channels are FoV-scaled (§11.2); Tactile is exempt.

### 11.2 Perception — facing sets field of view

**The direction a fighter faces determines their field of view (FoV); FoV determines what they can read, anticipate, and react to.** This replaces v31's authored Facing Ob table: facing's effect is now *emergent* from perception, per Pillar 5.

**FoV zones** (relative angular position of the opponent within the fighter's facing):

| Zone | Angular band (from facing centre) | FoV factor | Reaction availability |
|---|---|---|---|
| Central | ±~30° | 1.0 | all reactive aspects available |
| Near-peripheral | ~30–70° | 0.6 | Hand-led + Body-led only |
| Far-peripheral | ~70–110° | 0.3 | Hand-led only (reflexive) |
| Blind (rear) | >~110° | 0.0 | none |

**Effect on Reading (§11.1).** Each Reading channel Pool fired against an opponent is scaled by that opponent's FoV factor in the reader's facing:
```
Effective Reading Pool (channel) = base Reading Pool × FoV_factor(opponent position)
```
Tactile reading (the bind) is the exception — it is contact-mediated, not sight-mediated, so it is **not** FoV-scaled (you feel the bind regardless of where you are looking). All sight-mediated channels (Geometric, Kinetic, Rhythmic) are scaled.

**Effect on reaction.** Reactive aspects (Body-led, Yielding, Voiding) require the incoming line to be within the defender's FoV at the listed factor or better. An attack arriving from the defender's blind rear permits **no reactive aspect**; from far-peripheral, only the reflexive Hand-led at a penalty. You cannot void what you cannot see.

**Why facing advantage is emergent (and roughly matches v31's authored values).** An aggressor attacking into the defender's periphery or rear gains advantage through two compounding channels, not an authored Ob line: (1) the defender's Reading Pool against the aggressor is FoV-scaled down (less anticipation → worse Reading-modifier on the defender's resolution), and (2) the defender loses access to reactive aspects (fewer options, forced into weaker responses). Verified: these compound **super-linearly**, reproducing ≈ −1 effective Ob at flank and ≈ −2 at rear — the v31 authored values emerge from the perception model rather than being asserted (designs/audit/2026-05-28-combat-reframe/reframe_blueprint.md §4).

**Changes during:**
- Phase 3 Approach: Angled/flanking approaches (§4.4) move the aggressor toward the defender's periphery; Drawing approach holds relative facing.
- Phase 6 Bout: Voiding changes facing; Curvilinear/Triangular Footwork enables mid-bout facing changes; Bursting enables facing reset (re-centring the opponent in FoV).

**The spatial contest.** Positioning is the fight over perception: keep the opponent in your central cone (full Reading + all reactions) while working into their periphery/blind (degrading theirs). Footwork aspects are the levers; this is the "reading the opponent is its own skill" + "positioning is the sub-game" observations made mechanical.

Facing/FoV state is tracked per round of engagement; resets toward square on Phase 8 Return unless Phase 3 held a facing advantage.

### 11.3 Signal Level

How clearly the character's intent is readable by opponent. Affects opponent's Phase 4 Reading peak Pool TNs.

**Affected by:**
- Stance choice (per §6.1 — Centered/Raised medium-high signal; Low/Forward-point low signal)
- Position choice (Phase 2 — multi-attack-affording positions low signal; single-attack high signal)
- Weapon class (per §8 — thrust-primary low signal due to less lateral motion; cut-heavy high signal)
- Aspect specialization (Feinted Approach, Drawing Approach — explicitly low-signal at Phase 3)

**Mechanical effect:** opponent's Phase 4 Reading Pool TNs increase by Signal Level magnitude.

| Signal Level | Opponent's Reading TN modifier |
|---|---|
| Low (concealed) | +1 TN (Reading harder to clear) |
| Medium (default) | +0 |
| High (telegraphed) | −1 TN (Reading easier; even partial-attention reveals commit) |

Low signal costs: typically reduced commit options at that phase (Forward-point stance restricts attack lines to thrust + Forward-point-permitted cuts).

### 11.4 Combat Concentration

Finite mental resource. Per §3.5 (Concentration combat extension): formula `Focus × 3` shared with social contest. Combat drain rates per phase.

**Drain triggers** (cumulative across pass):

| Source | Cost |
|---|---|
| Phase 4 attention split (each channel beyond primary) | +1 Conc |
| Phase 4 Reserve attention (50/50 split with Bout) | +1 Conc |
| Phase 5 Commit depth 3 (Committed) | +1 Conc |
| Phase 5 Commit depth 4 (Deep) | +2 Conc |
| Phase 5 Commit depth 5 (Full) | +4 Conc |
| Phase 5 Thread-op commit (any depth) | +2 Conc additional (Thread Fatigue handles primary cost) |
| Phase 6 Bout sub-action (per step) | +0.5 Conc |
| Phase 6 Wound transition (incoming wound) | +3 Conc (shock) |
| Phase 6 Coherence drift (per Coherence point lost) | +1 Conc |
| Phase 7 Sudden disengage | +1 Conc |
| Phase 5 Pre-empt activation (Intent Tier 4) | +2 Conc |

**Recovery:** Phase 8 only: `+Focus` per round. No recovery during Bout.

**Threshold effects:**

| Concentration level | Effect |
|---|---|
| <30% of max | Reading sub-channel rolls at −1D; opponent gains +0.5 Ob advantage during Bout |
| <20% of max | Commit depth ceiling drops by 1 |
| <10% of max | Cannot enter Phase 6 Bout — Phase 7 Disengage forced |
| 0 (Spent — canonical social-contest threshold) | −2D all combat rolls; resets to max per canonical social-contest Regroup rule; functionally similar to Stamina Out-of-Breath in combat |

**Social-combat shared pool:** a character entering combat after a social contest carries reduced Concentration. A character whose Concentration was Spent in a social exchange (canonical: resets to max) enters subsequent combat at full pool, but the next social contest in the same scene carries combat-drained Concentration.

### 11.5 Stamina

Canonical formula `Endurance × 5` (derived_stats §4.2). Per-phase costs reweighted for the SETUP/BOUT/RESET phase structure (replaces canonical action-cost table; see §4 phase descriptions).

**Drain summary** (cumulative across pass; canonical action-cost language preserved as reference):

| Phase action | Stamina cost | Canonical equivalent |
|---|---|---|
| Phase 3 Direct press / Drawing / Feinted | 0 | Movement included in commit |
| Phase 3 Angled approach | 1 | (movement subset) |
| Phase 3 Explosive close | 3 | Heavy/special movement |
| Phase 5 Commit depth 1 (Probe) | 2 | Below standard attack |
| Phase 5 Commit depth 2 (Preparatory) | 3 | Below standard attack |
| Phase 5 Commit depth 3 (Committed) | 5 | Standard attack (canonical 5) |
| Phase 5 Commit depth 4 (Deep) | 7 | Between standard and heavy |
| Phase 5 Commit depth 5 (Full) | 10 | Above heavy attack |
| Phase 6 Bout sub-action (per step) | 1 (Cut/Thrust/Yield/Void) — 2 (Press/Wind/Displace) — 3 (Grip-change) | Distributed across canonical action-cost range |
| Phase 7 Clean withdrawal | 1 | Movement |
| Phase 7 Defensive disengage | 2 | Defensive |
| Phase 7 Sudden disengage | 3 | Dodge-equivalent |
| Armor passive drain per round | +0 (None) / +0 (Light) / +1 (Medium) / +2 (Heavy plate) | Per canonical derived_stats §4.2 armor mod |

**Recovery:** Phase 8: `+(Endurance + relevant combat History) × 2`, capped at max (canonical Take a Breath formula preserved). No recovery during Bout.

**Threshold effects** (canonical):
- 0 (Out of Breath): −2D all combat rolls until recovery action taken

**Threshold effects** (new; sim-tunable):
- <30% of max: reaction sub-actions in Bout compress (chain max −1 step)
- <20% of max: Commit depth ceiling drops by 1
- <10% of max: Phase 5 Commit available only at probe/preparatory depths

### 11.6 Resource asymmetry — combat as dual-resource contest

Per Pillar 4, Concentration and Stamina drain asymmetrically. A character may be **physically fresh but mentally exhausted** (sustained Reading + deep commits → Concentration low; Stamina untouched) or **physically spent but mentally sharp** (Bursting Footwork + Explosive Close + Burst Commitment → Stamina low; Concentration low only if Bout chains were sustained).

This produces distinct combat shapes:
- **Burst fighters** (Bursting Footwork + Burst Commitment + Decisive Reaction): deplete Stamina fast, must end engagement quickly or disengage
- **Sustained fighters** (Sustained Commitment + Linear Footwork + Tactile Reading): Stamina-economical but Concentration-vulnerable in long engagements
- **Counter-time fighters** (Counter-time tradition + Pre-empt Tier 4 Intent): high Concentration cost per engagement (Pre-empt activations + attention splits) but conserve Stamina

Sim validation (I-17) confirms dual-resource economy produces meaningful build differentiation.

---

## 12. BOUT SUB-ACTION MECHANICS (DEEP SPEC)

This section is the substantive detail for Phase 6 (§4.7). Per Jordan directive: Bout is the primary engagement action, not a Strike-resolution elaboration.

### 12.1 Sub-action option enumeration per engagement state

| Engagement state | Sub-action options |
|---|---|
| **Out-of-contact** (entering Bout from a commit miss; both fighters in measure but no weapon contact) | Probe-cut, Probe-thrust, Step-around, Disengage-to-Phase-7 |
| **Closing** (weapons in striking distance, contact imminent) | Cut, Thrust, Press-the-bind, Yield-to-bind, Void-and-counter, Targeted-line (vs heavy armor, needs Reading success), Disengage |
| **In-bind** (weapons in sustained contact; Tactile channel active) | Wind, Yield, Press, Displace, Break-bind, Grip-change (weapon-class dependent), Targeted-line (gap-thrust), Throw-strike |
| **Breaking** (one fighter committed to disengage; other has choice to follow or release) | Pursue, Release, Throw-strike (pursue with attack of opportunity) — leads to Phase 7 |

Each engagement state surfaces 3–6 sub-action options. Aspect Reaction specialization gates which options are surfaced as **player-default** in AI-driven mode; other options surface only on player intervention.

### 12.2 Per-sub-action Pool composition

All sub-action Pools follow canonical grammar:

```
Sub-action Pool = (relevant-attribute × 2) + Aspect Proficiency + History modifier
```

Aspect Proficiency here is that of the **equipped** specialization in the relevant slot (§6.11) — not the character's full trained pool. The weapon's handling value (§8.2) also feeds weapon-dependent sub-actions.

| Sub-action | Relevant attribute | Aspect Proficiency source |
|---|---|---|
| Cut (light) | Agility | Commitment + Reaction |
| Cut (heavy) | Strength | Commitment + Stance |
| Thrust | Agility (light) / Strength (heavy thrust) | Commitment + Stance |
| Press / Wind | Strength | Reaction + Stance |
| Yield | Will (canonical absent — substitute Cog or Foc per Jordan call; this proposal uses Foc) | Reaction + Anticipation |
| Void | Agility | Reaction + Footwork |
| Displace | Strength + Agility composite (sim-tunable) | Reaction + Footwork |
| Grip-change | Strength | Grip specialization (must have Half-grip-available or equivalent) |
| Break-bind | Strength | Reaction |
| Probe (cut/thrust) | Agility | Approach + Commitment |
| Step-around | Agility | Footwork |
| Throw-strike | Strength | Disengage + Commitment |
| Disengage | Agility | Disengage |
| Targeted-line | Agility | Reaction + Anticipation (precision; requires the gap seen or felt) |

**Wound penalty applies** (canonical PP-716 / derived_stats §4.1): −1D per Wound on all sub-action Pools.

### 12.3 Per-sub-action Ob composition — σ-space, soft cap, state-gating

v31 added modifiers directly to Ob (additive fractional Ob). The diagnostic found this produced **non-uniform impact** (a fixed Ob shift swings a small Pool far more than a large one — F1) and **compound foreclosure** (stacked modifiers could drive effective success to ~0% before any roll — F2). v32 replaces it with a three-part system (full derivation: designs/audit/2026-05-28-combat-reframe/modifier_system_spec.md).

**(a) Modifiers live in σ-space.** Every modifier is expressed in standard-deviation units (δσ), not raw Ob. It converts to an Ob shift scaled to the Pool:
```
σ_N = 0.8 · √Pool          (continuous-engine per-die SD × √Pool, per params/core)
Ob shift = δσ · σ_N
```
Because the shift scales with σ_N, a given δσ produces the **same probability impact at every Pool size** (≈25.8 percentage points at 50% baseline for δσ = 1.0, verified across 5D–18D). This is the F1 fix: uniform *impact*, not uniform *form*.

**(b) Player-facing levels (the math is hidden).** Players never see σ. Modifiers are surfaced as advantage levels; the engine maps level → δσ:

| Level | δσ | Source examples |
|---|---|---|
| Minor | 0.25 | small Reading edge; secondary set bonus |
| Moderate | 0.50 | Stance Counter (soft); favorable Reaction matchup; weapon phase-strength |
| Strong | 0.75 | Stance Counter (hard); strong Reading-modifier; full set bonus |
| Major | 1.00 | dominant perception (rear) emergent; stacked advantages post-cap |

Migration from v31: a v31 ±1 Ob modifier ≈ **Moderate**; a v31 ±2 Ob modifier ≈ **Strong** (the soft cap, below, prevents the old ±2 stack from foreclosing).

**(c) Soft cap (saturating).** The net σ-sum is passed through a saturating cap before conversion, so no stack can foreclose an outcome:
```
net_σ  = Σ(live, state-gated δσ)              (signed)
eff_σ  = M_max · tanh(net_σ / M_max)          M_max = 1.5σ
Effective Ob = base Ob − eff_σ · σ_N          σ_N = 0.8·√Pool
```
`tanh` saturates smoothly toward ±M_max with no dead-zone (a hard clamp would create a threshold cliff — Lesson 6; `tanh` does not). Verified worst case: a full adverse stack leaves the disadvantaged sub-action at ~9% rather than 0% — foreclosure removed (F2 fix), and the cap's *impact* is uniform across Pool (≈43pp at all Pool sizes, vs the dice-space ±4 stack's 37–50pp spread).

**(d) State-gating.** Only modifiers physically relevant to the current engagement state are live (the rest are zero for that state). This both shrinks the per-state decision (Elegance) and bounds the raw σ-sum feeding the cap (reinforces F2):

| Engagement state | Live modifiers (δσ contributors) |
|---|---|
| Out-of-contact | perception/FoV, Reading-modifier, weapon phase-strength, set bonus |
| Closing | Stance Counter, Reaction matchup, perception/FoV, Reading-modifier, weapon phase-strength, set bonus |
| In-bind | Reaction matchup, Tactile Reading-modifier, Grip/weapon phase-strength, set bonus (Stance Counter and sight-perception drop — the bind is contact-mediated) |
| Breaking | perception/FoV, Reaction matchup, Reading-modifier |

**Worked conversion.** Closing state, attacker Pool 6D (σ_N = 0.8·√6 ≈ 1.96), base Ob 2. Live: Stance Counter Moderate (+0.50), favorable Reaction Moderate (+0.50), Reading-modifier Minor (+0.25), perception Minor (+0.25). net_σ = +1.50; eff_σ = 1.5·tanh(1.50/1.5) = 1.5·0.762 = 1.14. Ob shift = 1.14·1.96 ≈ 2.24 → Effective Ob ≈ 2 − 2.24 = −0.24 (floored at 0 → near-auto on this sub-action, as intended for a fully-set-up attacker; the *bout* still has multiple transitions + the damage roll, so variance lives downstream — see §12.6). The same level stack at 16D (σ_N ≈ 3.2) yields the same *probability* outcome, not a larger Ob jump — the F1 property.

`[ASSUMPTION: M_max = 1.5σ and base-Ob values are draft — sim-tunable in Phase 11; the modifier_system_spec flags the strong-pool+full-setup near-certainty on a single sub-action as the intended front-end payoff, with bout-level variance carrying the uncertainty]`

### 12.4 Sub-action degree-of-success effects

| Sub-action | Failure (net ≤ 0) | Partial (0 < net < Ob) | Success (net ≥ Ob) | Overwhelming (net ≥ 2·Ob ∧ net ≥ 3) |
|---|---|---|---|---|
| Cut / Thrust | Misses; expose to counter | Glances; minor consequence (no wound) | Lands; wound transition check per damage formula | Critical (canonical: weapon modifier doubled) |
| Press | Pushed back | Held; opponent +0.5 Ob next step | Opponent off-line; aggressor +1D next step | Opponent's stance broken (forced to Phase 1 next pass) |
| Wind | Slip; opponent gains Tactile read | Held bind position | Bind position improved; +1D for aggressor next sub-action | Bind controlled; opponent forced to break-bind or accept disadvantaged sub-actions |
| Yield | Overrun | Partial redirect | Force redirected; opponent's commit reduced by 1D | Reversal — aggressor becomes initiator of next sub-action |
| Void | Caught by attack | Partial evasion (half-consequence) | Clean evasion | Counter-position established (free Phase 5 probe-depth commit next pass) |
| Displace | No movement | Half-zone shift | Full zone displacement | Opponent off-balance (their Stance Pool reduced 1 pass) |
| Grip-change | Weapon dropped | Partial change (half-effective grip) | Grip changed; new sub-action options surface | Grip changed + free Phase 5 probe depth commit |
| Break-bind | Bind held | Partial separation (still in bind) | Bind broken; engagement state → Out-of-contact | Clean break + free disengage to Phase 7 |
| Probe | Telegraphed; opponent +0.5 Ob | Light contact; no wound | Probe lands; minor wound check (depth 1 damage formula) | Probe + counter info revealed |
| Targeted-line | Misses gap; thrust slides off plate (no wound), exposed | Hits plate; armor NOT bypassed (glances) | Gap hit — damage recomputed vs armor tier −1 (Heavy→Light); wound check | Deep gap thrust — recompute vs None + critical |

Magnitudes draft; sim-tunable I-17.

**Targeted-line (anti-armor, I-13b).** A precise thrust to an armor gap (visor, armpit, groin, joint), available at **Closing** (requires a Reading success this round — you must perceive the opening) or **In-bind** (you can feel it), to thrust-capable weapons (Long thrust, Long cut-and-thrust, spear, Single short, the Long Heavy Blunt spike). Mechanic: a **precision penalty** (Strong adverse, δσ −0.75 on the attacker — the gap is small) in exchange for **recomputing the hit's damage against an armor tier one lower** (Heavy plate → treated as Light; overwhelming → None). This is the *skill-instead-of-tool* anti-armor path (§8.3): a light-weapon fighter wounds plate by paying in precision rather than switching to Long Heavy Blunt. It does not bypass armor for free — most attempts glance (partial), and a missed gap leaves the attacker exposed.

### 12.5 Edge case rulings (consolidated from §4.7)

- **Mutual disengage** (both fighters declare Break-bind / Disengage simultaneously): both succeed; both fighters separate; Phase 7 fires simultaneously
- **Mutual deep commit (depth ≥ 4)**: resolves by highest Pool net successes; one wounds, other's commit fails
- **Mutual depth-5 (full) clash**: both Pools roll; both apply wound consequences at net-successes magnitude. If tied, both heavily wounded.
- **Mutual depth-5 with one Thread-op**: Thread-op resolves first per P-01 temporal-auto-effect ordering (metaphysical co-movement precedes martial outcome)
- **Chain-termination ambiguity** (multiple termination conditions fire same step): priority order 1, 5, 2, 6, 3, 4 (wound transition first; chain cap second; mutual separation third; clash fourth; resource depletion fifth/sixth)
- **Wound transition mid-chain**: chain ends immediately; control passes to Phase 7 (Disengage); incoming wound applies before Phase 7 declarations
- **Concentration/Stamina critical threshold mid-chain**: depleted fighter forced into Phase 7 next sub-action step; cannot continue Bout

### 12.6 Bout chain length and termination

**Length cap from Phase 5 depth choice:**

| Commit depth | Bout chain length cap |
|---|---|
| 1 Probe | 1 sub-action |
| 2 Preparatory | 2 sub-actions |
| 3 Committed | 4 sub-actions |
| 4 Deep | 6 sub-actions |
| 5 Full | unlimited (terminates only on wound, separation, or resource depletion) |

When chain cap reached, Phase 6 ends; engagement moves to Phase 7 Disengage automatically.

### 12.7 Worked example — Bout chain

Ilse (Long-thrust dueling, Tier 2 Intent Reading, Forward-point Stance, Decisive Commitment, depth 3 thrust commit) vs Hugo (Long-blade contact, Centered Stance, Hand-led Reaction, Yielding Reaction available).

Phase 5 commit: Ilse declared depth 3 Thrust. Engagement enters Bout in Closing state.

**Sub-action step 1** (Closing):
- Ilse declares **Thrust**: Sub-action Pool = (Agi 5 × 2) + Decisive Commitment AspProf 4 + Long-thrust History 3 = 17D. Effective Ob = base 2 + Stance Counter (Forward-point vs Centered: −2) + Reaction-aspect (Hand-led vs Committed: 0) + Reading mod (assume Sustained Read fired at Phase 4 for +1 Ob) + Facing (Square: 0) = 1 Ob. E[net] at TN 6 = 17 × 0.5 = 8.5; net hits >> 1 Ob; Success likely.
- Hugo declares **Yield-to-bind** (Hand-led aspect surfaces this as player-default at +1 Ob disadvantage to attacker; Hand-led isn't strong vs depth 3 Committed but options narrow): Sub-action Pool = (Foc 3 × 2) + Hand-led Reaction AspProf 4 + Long-blade History 3 = 13D vs Ilse's Thrust resolution. 
- Resolution: Ilse's Thrust lands at Success; Hugo's Yield reduces consequence by 1D. Engagement transitions to In-bind state.

**Sub-action step 2** (In-bind):
- Ilse declares **Press**: trying to drive Hugo off-line. Sub-action Pool = (Str 3 × 2) + Decisive Commitment AspProf 4 + Long-thrust History 3 = 13D. Ob 2 + Stance Counter persists (−2) = 0 Ob. E[net] ~ 13 × 0.5 = 6.5 net hits; Overwhelming likely.
- Hugo declares **Wind**: rotate weapon in bind. Pool = 13D Str-based. Wind requires bind-stable grip (Thumb-anchor or Standard); Hugo has Standard; OK.
- Resolution: Ilse's Press overwhelms Hugo's Wind; opponent off-line + Stance broken (forced to Phase 1 next pass). Chain step Stamina cost: 2 (Press) for Ilse, 2 (Wind) for Hugo. Concentration cost: 0.5 each.

**Termination check:** chain step 2 of 4 cap (Committed depth 3). No wound transition yet (Press doesn't wound, just displaces). Chain continues if both want.

**Sub-action step 3** (In-bind, with Hugo at disadvantage):
- Ilse declares **Thrust** (depth-keyed; counts within depth-3 cap): Pool 17D, Ob 1 + Stance Counter persists + Hugo's stance broken (additional −0.5 Ob to Aggressor) = 0.5 Ob. Net hits overwhelming.
- Hugo declares **Break-bind**: Pool 13D Str-based, Ob 2. Net hits ~6.5; Break-bind succeeds at Success degree.
- Resolution: Ilse's Thrust lands; Hugo's Break-bind succeeds (engagement transitions to Out-of-contact). Damage check fires per Phase 5 damage formula (canonical: net hits + Str modifier + weapon modifier vs armor; Ilse Light Blade vs Hugo's Light armor: 5 net hits + Str 3 ×1 + Light Blade vs Light = +2 = 10 damage. Hugo's Health 44 → 34. Hugo's WI = 11. floor(10/11) = 0 wounds (Hugo just below wound threshold). No wound transition.

**Termination check:** Hugo's Break-bind succeeded; engagement state Out-of-contact + Hugo wants Phase 7. Chain ends at step 3 of 4 cap. Phase 7 fires.

**Pass totals:** Ilse Stamina drained 5 (Commit depth 3) + 2 (Press) + 1 (Thrust step 3) = 8. Concentration drained 1 (depth 3) + 0.5 × 2 (Bout steps) + 1 (Sustained Read sustain) = 3. Ilse goes into Phase 8 with Stamina 7 and Concentration 6 (of 9). Recovery: +Focus × Phase 8 contribution = +3 Concentration → 9; Stamina +(End + History) × 2 = (3+3) × 2 = +12 → 15 (capped at max). Both restored.

Hugo: Stamina 25 - 1 (Yield) - 2 (Wind) - 0 (Break-bind succeed) - 1 (Phase 7 cost) = 21 of 25. Health 34 of 44. Worse off mechanically; goes into next pass with stance broken filter (cannot use Centered, forced into limited Stance set).

This is one Bout chain at depth 3. Demonstrates σ-space modifier composition (§12.3), Reading-modifier inheritance, Stance Counter persistence (Closing), sub-action Pool variety, termination on engagement-state change.

---

## 13. AUTHORED HONOR-CODE SCENE CONTEXTS

The proposal's 8 honor codes (Capture-over-kill, No humiliation, Single-decisive, etc.) do **not** map to canonical Convictions or Duties at the character level. Per the Pass 1 critique: Convictions are player-authored worldview statements with strain mechanic (player_agency §2); Duties are 8 institutional types assigned by faction leader (player_agency §3). Neither functions as "combat action-space filter."

**Resolution:** Honor codes survive as **Authored scene-context filters** per VGMS §3 "GM Decides" Register (Authored resolution type). Specific encounter authoring may specify foreclosed actions for the scene.

### 13.1 Scene-context catalog

| Scene context | Authored action-space modifier |
|---|---|
| Judicial combat (Crown court trial-by-arms) | Phase 5 Commit depth capped at 4 (cannot kill defendant outright); Phase 7 Sudden disengage forbidden once Bout has entered In-bind |
| Ritual duel (Hafenmark formal challenge) | Pre-engagement ritual mandatory: Phase 5 Commit unavailable round 1 (ritual completes during Phase 1–4); both fighters' Disengage options reduced to Clean withdrawal only |
| Templar combat protocol (Church military rules) | Specific weapon required: foreclosed weapons not surfaced in encounter weapon selection; depth 5 Commit unavailable against unconsecrated targets |
| Niflhel combat-honor (capture-over-kill against named opponents) | Commit depth capped at 4 against Heavily Wounded opponents (lethal blow forbidden); Phase 7 Sudden disengage against wounded opponents forbidden |
| Combat against bound prisoner | Phase 5 depth 5 unavailable; Phase 6 Bout chain length cap −2 (engagement should be brief) |
| Tutorial / training engagement | Phase 5 depth 4–5 unavailable; Phase 7 Clean disengage always succeeds without opposed roll; Wound transitions produce flavor wounds only (no Health cost) |

These are **scene metadata**, not character state. Scene authoring (encounter author + faction-cultural rules + Duty context) determines which constraints apply per encounter.

### 13.2 Interaction with Conviction and Duty

When a character's active Conviction or Duty creates a *behavioral preference* that aligns with a scene's Authored constraint, mechanical effects compose:

- **Aligned**: a Conviction "I will not kill except in defense of the helpless" + Judicial combat scene context: the depth-4 cap is *natural*; player gains +1 Momentum if Bout ends without lethal blow (Belief-supporting per canonical Momentum)
- **Conflicting**: a Duty "Bring the Cardinal to justice [alive]" + scene context where opponent is the Cardinal at heavily-wounded threshold: depth-5 commit is foreclosed by scene; if player attempts to override (per VGMS §3 Player choice), Duty Completion is failed per player_agency §3.4 (Standing −1)

This restores the proposal's "Code violation has mechanical and narrative consequence" intent without inventing a parallel codes-as-character-state system. The mechanical effect lives at the scene context layer; the narrative consequence lives in canonical player_agency mechanics (Momentum, Conviction strain, Duty completion, Standing).

### 13.3 What's cut

The proposal's per-character "active code set" (zero, one, or two codes) is **not preserved** as character-level state. Combat behavior preferences are expressed through:
- Conviction wording (player_agency §2)
- Duty type assigned (player_agency §3.3)
- Aspect specializations (§6 — e.g., Cautious Commitment expresses "I do not commit to lethal force casually")
- Faction Standing context (player_agency §3.4 Standing thresholds restrict what behaviors are tolerated within faction context)

The proposal's "code violation buff" (mechanical advantage on violation) does not survive as a separate mechanic.

---

## 14. THREAD INTEGRATION

Thread integration with combat is **canonical** per combat_v30 §10. This section enumerates how the proposal's engine interacts with that canon.

### 14.1 Thread-op as Phase 5 Commit alternative

Per §4.6, TS-sensitive practitioners (TS ≥ 30 per params/threadwork) may commit a Thread operation in place of a martial commit. Available Thread-ops per canon: Leap, Weave, Pull, Mend, FR.

**Pool composition:** canonical Thread Pool = `(Spirit × 2) + History + TPS` (params/threadwork PP-616).

**TN modifiers:** per canonical params/threadwork TN table (TN 7 standard ops; TN 8 Binding ops, POP; TN 9 POP Binding).

**Ob:** canonical three-axis Ob (Depth + Breadth + Distance) per params/threadwork PP-622, PP-623.

**Costs:**
- Canonical Thread Fatigue cost per op (Leap 3, Pull 5, Mend 4, Lock 7, Dissolve 10) per derived_stats §6.1
- **+2 Concentration** additional (this proposal's combat extension)

### 14.2 P-01 Inseparability fires

Per canon P-01: every Thread operation produces three-dimensional co-movement (temporal CD + History Resonance; epistemic Certainty modifiers; actual d6 consequence table). This applies in combat per combat_v30 §10.1.

**Resolution priority**: in Phase 6 Bout, if Thread-op sub-action resolves alongside martial sub-actions in the same step, **Thread-op resolves first** per P-01 temporal-auto-effect ordering (metaphysical co-movement precedes martial outcome within same tick).

### 14.3 Coherence drift in combat

Per canon P-10, P-12, P-15: Coherence drains under specific triggers. In combat:

| Trigger | Coherence cost |
|---|---|
| Thread-op commit in combat | −1 (per combat_v30 §10.1; canonical mass-battle rule extends) |
| Sustained Thread-mediated Bout (3+ Thread sub-actions in chain) | −1 additional |
| Reading Thread channel sustained (Phase 4 + Phase 6 Reserve attention through 3+ passes) | −1 per 3 passes |

**Coherence-0 in combat** triggers PP-261 NPC transition: character becomes 100%-functional NPC, player agency ends. TS-gated branching from P-15 still applies for narrative outcomes (low-TS dissolution; high-TS forced layer-3 maintenance via Thread Fatigue) but mechanically the character exits player control.

### 14.4 Intent Reading Tier 5 vs Thread channel — distinction

Both Tier 5 Intent Reading (Conviction Read) and Thread channel Reading (combat_v30 §10.2 visibility table) read aspects of opponent's deeper state. They are *distinct* mechanisms:

| Mechanism | Reads what | TS required | Source |
|---|---|---|---|
| **Tier 5 Intent (Conviction Read)** | One active Conviction; reveals one Code-generating constraint set | None (mundane perceptual mastery) | This proposal §10.6 |
| **Thread channel Reading** | Opponent's thread state, knot connections, Coherence integrity, Conviction strain magnitude | TS 30+ (basic); TS 50+ (full structural depth) | combat_v30 §10.2 |

A Tier 5 Intent reader sees the Conviction *as a behavioral commitment* (what opponent is committed to do). A Thread reader sees the Conviction *as metaphysical strain on opponent's configuration* (how the Conviction is constraining their being-state).

Both can fire in the same Phase 4 attention split (Intent primary, Thread secondary, or vice versa). Combined: full understanding of opponent's Conviction landscape.

### 14.5 Cross-system fire from combat (canon preserved)

Per combat_v30 §10.3 (unchanged):

| Combat event | Consequence | System |
|---|---|---|
| Killing named NPC | Knot rupture + Conviction Scar on witnesses | §15.3 Death Cascade; npc_behavior_v30 §3.4 |
| Practitioner Dissolution in combat | RS cost + Scar on all witnesses with engaged Conviction | threadwork_v30 §5.2 |
| Practitioner Dissolution witnessed by companion | Companion Thread violation departure if Faith/Order/Equity Conviction | companion_specification_v30 §6.1 |
| Thread operation witnessed by adjudicator in formal proceeding | Certainty-indexed adjudicator response | social_contest_v30 §9.4b |

---

## 15. WORLD BRIDGE INTEGRATION + EDITORIAL LEDGER

### 15.1 Combat World Bridge (canon preserved unchanged)

Combat World Bridge per combat_v30 §13 is **fully preserved**. This proposal does not modify §13. Summary of canonical mechanics that fire from combat_v32 engine outcomes:

| §13 Component | combat_v32 trigger |
|---|---|
| §13.1 Domain Echo (faction officer outcomes) | Triggered at pass-end (Phase 8) on identified-named-NPC opponent with faction office. Outcome = wound state at end (Heavily wounded = defeated; killed via Death Cascade). |
| §13.2 Combat Reputation Cascade (0–6+ tiers) | Public combat (3+ witnesses) accumulates Combat Reputation. |
| §13.1b Resources / loot | Equipment changes on combat outcome interact identically (Phase 7 Disengage → Resources gain table). |
| §13.2b Settlement-Level Consequences | Combat in a settlement produces Order, Disposition, Garrison Size feedback per canon. |
| §13.3 Death Cascade (5 steps) | All 5 steps fire on Killed wound state at pass-end: (1) Knot rupture, (2) Scene Slate priority, (3) Faction Stability/Succession, (4) Exposure, (5) Player Conviction test. |

### 15.2 Mass combat interface (combat_v30 §9, §11 preserved)

Mass combat (combat_v30 §9 TTRPG scale, §11 faction unit rosters) is **preserved**. Personal-scale combat_v32 transitions to mass combat via canonical scale_transitions_v30 mechanics. Mass combat uses canonical Martial/Discipline stats, not combat_v32's engagement state graph.

**Transition rules:**
- Personal combat in a mass-battle context: combat_v32 fires per round; mass-battle resolution continues on engine tick clock
- Wound state in personal combat affects mass-battle Command checks per canonical PP-716 (−1D per Wound on Command Pool)
- Mass-battle Thread operations affect personal-combat Coherence per combat_v30 §10.1 ("Mass battle: Coherence −1 per Thread operation")

### 15.3 Fieldwork transitions (combat_v30 §11.5 preserved)

§11.5 Fieldwork Transitions are **preserved unchanged**. Exposure mechanics, post-combat investigation, kill-evidence accumulation all operate per canon. Combat_v31's three-state wound display (§9.2) feeds canonical wound-state input to §11.5 transition rules.

### 15.4 Social-contest interaction (Concentration shared pool)

The Concentration combat extension (§3.5, §11.4) creates a shared resource between combat and social contest. A character who exhausted Concentration in a Council debate enters subsequent combat at reduced Concentration. A character spent in Bout enters subsequent social contest similarly impaired.

**Open item** (Pass 2c sim validation): does shared-pool create unintended cross-system pressure? Sim-tunable; possible alternative is separate per-system Concentration pools at cost of mechanical complexity.

### 15.5 Editorial ledger entries needed on ratification

The following editorial ledger entries enter on ratification of this proposal:

| ED ID (to be assigned) | Entry | Affects |
|---|---|---|
| PP-XXX-A | Supersede combat_v30 §§1–4 (Combat Pool framing, Round Structure, Initiative, Actions) | combat_v30 |
| PP-XXX-B | Establish combat_v32 engagement state graph as canonical combat engine | combat_v30, derived_stats |
| PP-XXX-C | Concentration combat extension: derived_stats §5.2 social-contest formula extended to combat use; per-phase drain rates established | derived_stats §5.2; combat_v32 §11.4 |
| PP-XXX-D | First-round Initiative spec: `Att + Weapon Speed` with Cog/Agi tiebreak | combat_v30 §3 (PP-232 augment) |
| PP-XXX-E | Reach terminology unified to PP-290 (Short Reach / Long Reach / Ranged); supersedes PP-268 | combat_v30 §5 |
| PP-XXX-F | Stunt mechanic Authored mode: scene-metadata-driven, replaces GM-set N dice | combat_v30 §4 (Stunt entry) |
| PP-XXX-G | Strike action retired as canonical primary; Bout (Phase 6) replaces as primary engagement substance; canonical Strike/Feint/Disarm/Tie Up/Retrieve become Bout sub-actions per engagement state | combat_v30 §4 |
| PP-XXX-H | Three-state wound display layer (Unwounded / Wounded / Heavily wounded) over canonical 4-wound math; does not modify canonical Health/WI/MW formulas | derived_stats §4.1; combat_v32 §9.2 |
| PP-XXX-I | Intent Reading track established as separate progression from Reading aspect specializations; Tier 0–5 with ability unlocks | combat_v32 §10 |
| PP-XXX-J | Aspect specializations established as History sub-skills (audit principle #4 aligned); aspect Proficiency advances within History; Tradition Depth derived from History points | combat_v32 §5, §6; player_agency (Histories) |

### 15.6 Cross-system propagation list

Documents requiring update on ratification:

| Document | Change required |
|---|---|
| `designs/scene/combat_v30.md` | Strike §§1–4 with [SUPERSEDED-BY: combat_v32] markers; §§5 weapon system retained as canonical mapping; §§9, 10, 11.5, 13 preserved unchanged |
| `params/combat.md` (pending refresh) | Rewrite Pool composition formulas per combat_v32 phase structure; per-phase Stamina/Concentration costs; sub-action Pool table |
| `references/canonical_sources.yaml` | Update combat system canonical path: `designs/scene/combat_v30.md` → `designs/scene/combat_v32.md` (proposal file becomes canonical on ratification) |
| `designs/scene/derived_stats_v30.md` | §5.2 Concentration: add combat extension note |
| `designs/scene/threadwork_v30.md` | §2.3 visibility table cross-reference; no content change |
| `designs/provincial/mass_battle_v30.md` | §A.10 (Command checks) reference combat_v32 wound state; no formula change |
| `designs/scene/fieldwork_v30.md` | §11.5 transitions preserved; cross-reference combat_v32 |
| `designs/architecture/social_contest_v30.md` | Concentration shared-pool note (open: may require separate-pool variant) |
| `npc_behavior_v30.md` | §3.4 cross-system fire from combat preserved; NPC Conditional Logic Profile spec aligns to combat_v32 §6.10 |

### 15.7 Sim validation work needed

| Sim | Purpose | Acceptance |
|---|---|---|
| Phase 11 combat_v32 v1 sim (I-17 pivoted) | Validate Fast vs Strong build differentiation under the engagement state graph + σ-space modifiers | Fast (Agi-stacked, Single short) vs Strong (Str-stacked, Long cut-and-thrust) at 50–60% across symmetric optimal builds |
| Phase 12 dual-resource economy sim | Validate Concentration + Stamina create meaningful build differentiation | Burst, Sustained, Counter-time builds each viable; no dominant strategy across resource axes |
| Phase 13 Intent track sim | Validate Tier 4 Pre-empt economy doesn't break game balance | Pre-empt activates 0.2–0.4× per round at Tier 4; combat lethality not >2× canonical baseline |
| Phase 14 aspect-coherence sim | Validate named-set bonuses + 2 antagonism exceptions don't produce a one-build-dominates outcome | Three distinct "coherent" archetype builds within 5% win-rate margin |

### 15.8 Open items (consolidated)

- **I-11** (sim): named-set bonus magnitudes + Reaction 2-param coefficients + per-spec mechanical magnitudes (currently draft; the 36-pair matrix was retired in v32 per matchup_derivation_analysis)
- **I-12** (Pass 2c expansion): Valoria-faction-binding for additional 5 traditions (Long-thrust geometric, Curved-blade cavalry, Continuous-flow, Mounted multi-weapon, Formation-and-discipline); Tradition technique trees
- **I-13** Weapon TN matrix refresh — seven weapon classes' canonical 3-axis mapping + phase-strength values. **I-13b done** (this session): Long Heavy Blunt 7th class + Targeted-line anti-armor sub-action added.
- **I-14** (deferred to UI design pass): Conditional Logic Profile UI/syntax — priority list vs decision-tree builder vs natural-language rules
- **I-15** (sim work): Concentration combat formula scaling — current proposal uses canonical `Focus × 3`; may need separate combat formula if shared pool produces cross-system imbalance
- **I-17** (Phase 11 sim refit per §15.7 above)
- **Bout sub-action options expansion**: aspect-coherence-driven sub-action availability surface — when do which sub-actions become available based on trained aspects?
- **Combat-Thread interaction balance**: combat-time Thread-op timing, Coherence drift rates, Conviction Read frequency caps

---

## 16. PROVENANCE AND CHANGELOG

### 16.1 Design element provenance

| Element | Source |
|---|---|
| Engagement state graph (SETUP→BOUT→RESET; bout = probability-weighted subgraph) | v31 eight-phase loop, reframed per designs/audit/2026-05-28-combat-reframe/reframe_blueprint.md (Jordan top-down vision) |
| Aspect specialization framework (10 aspects × 5 specs) | dueling_combat_proposal.md §5 |
| Tradition learning bundles (recast as Histories) | dueling_combat_proposal.md §6; reframed per audit principle #4 |
| Reading sub-channels (source 5 mundane; consolidated to 4 in v32 per F7 — Kinetic merge) + Thread + Intent | dueling_combat_proposal.md §3; Intent extracted to separate track per Jordan canon override 2026-05-XX; F7 consolidation this session |
| Seven weapon classes with phase strengths (Long Heavy Blunt added per I-13b) | dueling_combat_proposal.md §7 + canon §5; mapped to canonical 3-axis weapon TN matrix |
| Four armor levels with sensor degradation | dueling_combat_proposal.md §7; canonical Stamina mod preserved |
| Three-state wound display | dueling_combat_proposal.md §4; reframed as UI compression over canonical 4-wound math |
| Stance Counter / Reaction-aspect / Aspect coherence matrices | dueling_combat_proposal.md §5 (aspect coherence framing) + extracted matchup logic |
| Intent Reading track with tier abilities | Jordan canon override; structurally novel per Pre-empt counter-time mechanic |
| Conviction Read (Tier 5) | This proposal extension; connects combat Intent reading to player_agency §2 Convictions |
| Combat Concentration as parallel resource | dueling_combat_proposal.md §3; canonically extended from derived_stats §5.2 social-only |
| Dual-resource economy (Stamina + Concentration) | dueling_combat_proposal.md §3 |
| First-round Initiative (Att + Weapon Speed) | combat_v30 §3 PP-232 gap closure |
| Reach terminology unification | params/core.md PP-290 wins over combat_v30 PP-268 |
| Stunt Authored mode | VGMS §3 GM Decides Register adaptation |
| Authored honor-code scene contexts | dueling_combat_proposal.md §8; reframed as VGMS §3 Authored content (not character-level state) |
| **Front-end strategy / probability-weighted state graph framing** | v32 reframe_blueprint.md §1–2 |
| **σ-space modifier system (soft cap + state-gating)** | v32 modifier_system_spec.md (resolves diagnostic F1/F2) |
| **Perception = facing→field of view; Facing Ob emergent** | v32 reframe_blueprint.md §4 (verified flank≈−1 / rear≈−2 emergent) |
| **Reaction 2-parameter formula (baseline + depth-slope)** | v32 matchup_derivation_analysis.md (table reduces; 18/20 within ±0.5) |
| **Aspect coherence → named sets + 2 antagonism exceptions** | v32 matchup_derivation_analysis.md (rank-2 ~86%; 36-pair matrix retired) |
| **Stance Counter kept authored + state-gated** | v32 matchup_derivation_analysis.md (Hodge ~85% cyclic; resists low-D) |
| **Weapon handling (Forgiving/Standard/Demanding)** | v32 reframe_blueprint.md §5 (crossover P≈4 verified) |
| **Equip-loadout layer (trained pool vs equipped loadout, named set bonuses)** | v32 reframe_blueprint.md §6 |

### 16.2 Conversation-level corrections incorporated

- **Canonical attribute set** (Agi, End, Str, Cog, Rec, Foc, Att, Bon, Cha, Spi) replaces proposal's Burning-Wheel-style names
- **Combat Pool canonical** `(Agi × 2) + History + 3` preserved as substrate; per-phase Pools compose via canonical formula
- **Health canonical** `(End+6) × (MW+1)` preserved; 3-state wound display is UI compression only
- **Stamina canonical** `End × 5` preserved; per-phase costs reweighted from canonical action-cost table
- **TS gates canonical** 30/50/70/90 (not invented 10/30/50)
- **VGMS §4 narrative-mode strike** preserved; this proposal is single-mode
- **player_agency §§2–3 Convictions/Duties** correctly understood (not repurposed as honor codes)
- **combat_v30 §10, §13** preserved as canonical Thread integration + World Bridge

### 16.3 What's not in this proposal (Pass 2c+ work)

- Specific per-spec mechanical magnitudes throughout (draft sim-tunable)
- Exact σ-space level→δσ calibration, M_max value, base-Ob values (Phase 11 sim)
- Conditional Logic Profile UI/syntax
- Five additional Tradition catalog entries with Valoria-faction binding (I-12b)
- Reaction 2-param exact coefficients; named-set bonus magnitudes (Phase 14 sim)
- Full sim validation results (the test pass re-runs the resolution diagnostic on this proposal; broader balance sims are Phase 11–14)

### 16.4 v32 changelog (state-graph reframe of v31)

v32 is a reframe of combat_v31_proposal (checkpointed at designs/proposals/combat_v31_proposal.md), per Jordan's top-down vision and the resolution diagnostic that found v31 NON-COMPLIANT (failing E + correctness-R at the "expressive-R-maximal corner"). Changes from v31:

- **§0/§1** — reframed around the probability-weighted state graph + front-end strategy; pillars 6→8 (added Front-end-strategy, Perception).
- **§4** — eight-phase loop regrouped as SETUP→BOUT→RESET; bout made an explicit probability-weighted subgraph; timescale recalibrated (bout 6–10s, cycle ~10–15s).
- **§7** — Reaction table → 2-param formula; aspect coherence 36-pair matrix → named sets + 2 exceptions; Stance Counter kept authored but state-gated. (Per matchup_derivation_analysis: Reaction derives, coherence mostly derives, Stance Counter does not.)
- **§8** — added §8.2 weapon handling (ease-of-use curve).
- **§11.2** — Facing authored-Ob table → perception/field-of-view; Facing advantage now emergent.
- **§4.5/§6.5/§11.1 (F7, post-verdict)** — Reading channels consolidated: Temporal + Biomechanical → **Kinetic** (Lesson-1 minimal merge, 5 mundane → 4); addresses the F7 over-split the test flagged as not-done.
- **§12.3** — additive fractional Ob → σ-space + soft cap + state-gating (resolves diagnostic F1 non-uniform impact and F2 compound foreclosure).
- **§6.11** — added equip-loadout layer (trained pool vs equipped loadout; named set bonuses; incompatibility warnings).
- **§6.11.2 (N4, post-verdict)** — set bonus smoothed from all-or-nothing to 2-step graded (full / near-set one level lower / none); resolves the build-axis cliff the test flagged, per armature A2.
- **§8, §12 (I-13b)** — anti-armor gap closed: Long Heavy Blunt 7th weapon class (+5 vs all tiers, STR ×3, TN 8) + Targeted-line gap-thrust sub-action (precision penalty, recompute vs lower armor tier). Light weapons no longer helpless vs plate.

Diagnostic targets and how v32 addresses them: F1 (non-uniform modifier impact) → σ-space (§12.3); F2 (compound foreclosure) → soft cap + state-gating (§12.3, §4.7); F6 (E failure / over-complexity) → front-loading + derivations + matrix retirement (§1 P2, §7); F7 (Reading over-split) → addressed: Temporal+Biomechanical merged into Kinetic (§4.5/§6.5, post-verdict this session; 5 mundane channels → 4); Facing → emergent (§11.2). F4 (loop-winner definition) remains a noted open item (see test pass).

---

*End of v32 reframe. Pass 3 (verification) and the diagnostic re-test follow.*
