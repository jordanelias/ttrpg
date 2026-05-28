<!-- PROPOSAL — PP-TBD; supersedes designs/scene/combat_v30.md §§1–4 on ratification -->
<!-- Source: dueling_combat_proposal.md (2026-05-24 upload) reframed per Jordan directives -->
<!-- Architecture: Option 2 (engine replacement) within d10/TN/Ob substrate -->
<!-- Status: PROPOSAL — not canonical until editorial ratification -->

# VALORIA — Combat System Rewrite (Proposal)

## Date: 2026-05-25
## Version: combat_v31_proposal v1.0
## Status: PROPOSAL — pending editorial ratification; will supersede designs/scene/combat_v30.md §§1–4 on ratification
## Scope: Personal-scale combat engine. Mass combat, Thread-in-combat (combat_v30 §10), Combat World Bridge (combat_v30 §13), Fieldwork transitions (combat_v30 §11.5) preserved by reference.
## Mode applicability: VIDEOGAME (Godot). Per VGMS §4, TTRPG-only mode struck — single mode in this proposal.
## Authority: canon/00_philosophical_foundations_rules.md → canon/02_canon_constraints.md → designs/architecture/videogame_mode_spec.md → this document → params/combat.md (pending refresh)
## Cross-references: params/core.md (attributes, dice engine, derived stats); designs/scene/derived_stats_v30.md (Health, Stamina, Concentration authoritative); designs/architecture/player_agency_v30.md (Convictions, Duties); designs/scene/combat_v30.md §§10, 13 (Thread, World Bridge); designs/scene/threadwork_v30.md (Thread operations); params/threadwork.md (TS, TPS, Thread Pool).

---

## 0. DISPOSITION

This proposal **replaces** the canonical combat engine (combat_v30 §§1–4: Combat Pool framing, Round Structure, Initiative, Actions) with an eight-phase Bout-centric engagement loop. The d10/TN/Ob resolution substrate (params/core.md continuous engine, PP-717 fractional Ob/TN) is **preserved and load-bearing** — all phase rolls, sub-action resolutions, and matchup modifiers operate within canonical Pool/TN/Ob/degree grammar.

**Preserved unchanged from canon:**
- 10-attribute character (Agi, End, Str, Cog, Rec, Foc, Att, Bon, Cha, Spi), 31-point creation, range 1–7
- Histories as progression backbone (audit principle #4: Histories not Skills; Recall caps History points)
- d10/TN/Ob resolution (continuous engine, fractional Ob/TN per PP-717)
- Health, Wound Interval, Max Wounds (per derived_stats §4.1, PP-716)
- Stamina = Endurance × 5 (per derived_stats §4.2, ED-694; action costs reweighted for new phase structure)
- Coherence 10→0 with PP-261 NPC transition at 0; Coherence drift per P-10/P-12/P-15
- TS gates 30/50/70/90; Thread Pool = (Spirit × 2) + History + TPS per params/threadwork PP-616
- Convictions (3 player-authored statements, strain mechanic) per player_agency §2
- Duties (8 institutional types, Standing 0–7) per player_agency §3
- Combat World Bridge (combat_v30 §13): Domain Echo, Reputation Cascade, Settlement Consequences, Death Cascade
- Thread in Combat (combat_v30 §10): wound penalty propagation, TS-gated perception, cross-system fire

**Extended / added:**
- Eight-phase Bout-centric engagement loop (replaces canonical action priority resolution)
- Combat Concentration as parallel mental resource (new; uses canonical Focus attribute)
- Reading sub-channels (5 mundane + Thread + Intent track) — combat sensory information layer
- Stance / Position / Facing / Signal Level as new combat state variables
- Intent Reading track (Tier 0–5 with specific abilities; per Jordan override 2026-05-XX)
- Stance Counter Matrix + Reaction-aspect Ob modifiers + Aspect coherence matrix (fractional Ob modifiers on Bout sub-action resolution)
- Six weapon-class phase-strengths (Pool/TN modifiers at named phases)

**Recalculated:**
- Combat resource economy: Stamina drain rates rebuilt for phase structure; Concentration combat formula proposed
- Wound display layer: 3 perceptual states over canonical 4-wound math (compressed for UI)

**Cut / superseded:**
- Canonical action priority resolution (Strike=1, Feint=2, Disarm=3, etc. per combat_v30 §4) — replaced by phase-keyed sub-action option sets
- Canonical Round Structure (combat_v30 §2 six resolution-process phases) — replaced by §4 eight-phase engagement loop
- Strike as primary action — Strike collapses into Bout sub-action chain (§4.6)
- Canonical Concentration as social-only — extended to combat (parallel social usage unchanged)

**Editorial ledger entries needed on ratification** (named here, drafted Pass 2c):
- Supersession of combat_v30 §§1–4
- New canonical combat engine ratification
- Concentration combat extension (new derived stat use)
- Cross-system propagation: mass_battle_v30 Bout integration, fieldwork_v30 transition update, social_contest interaction (Concentration shared pool)

---

## 1. DESIGN PILLARS

Six commitments. Where a design choice conflicts with a pillar, the pillar wins.

**Pillar 1 — The eight-phase loop is the engagement engine.** Combat runs as a sequence of eight phases per pass through the loop. Decision-points are phase-keyed; resolution happens across phases. This replaces canonical "declare-and-resolve action priority" with sequenced engagement-points. Single-action mechanics (Disarm, Tie Up, etc.) survive as Bout sub-actions within Phase 6, not as round-level alternatives to Strike.

**Pillar 2 — Bout is the primary action; Strike collapses into Bout.** A canonical Round = one pass through phases 1–8. The Bout (Phase 6) is the engagement's substantive resolution — sub-action chain producing wounds, displacement, bind states, and termination conditions. There is no separate "Strike" action; what was canonical Strike is now a depth-keyed Commit in Phase 5 that initiates Bout.

**Pillar 3 — Two resource economies: physical and mental.** Stamina (Endurance × 5, canonical) is the physical reservoir; drains per phase action. Combat Concentration (Focus × 3, new combat extension of social formula; sim-tunable) is the mental reservoir; drains under reading load, deep commits, sub-action chains, wound shock. Both finite. Recovery only in Phase 8 (stance return). Long fights become resource-management contests across two axes.

**Pillar 4 — Aspect specialization is character mechanics; History is character progression.** A character is built by configuring 10 aspect slots, each with 3–6 specializations. Aspect specializations are sub-skills *within* combat Histories (audit principle #4). Combat Histories (Tradition bundles) determine which aspect options are accessible; player configures within available set. Per-aspect Proficiency contributes to phase Pools.

**Pillar 5 — d10/TN/Ob with fractional modifiers is the resolution substrate.** Every phase roll, sub-action contest, and matchup modifier operates within canonical params/core dice grammar. Fractional Ob/TN (PP-717) absorbs per-aspect, per-stance, per-reaction, per-weapon, per-Reading matchup granularity without new resolution mechanics.

**Pillar 6 — Constraints are mechanical, not flavor.** Honor codes (when present) filter the action space at specific phases. Equipment forecloses options at specific phases. Wound state forecloses options at specific phases. Convictions modify available commit depths in specific contexts (cross-ref player_agency §3.5 Duty vs Conviction tension). Every constraint operates by removing or modifying decisions, not by adding narrative color.

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
- **Att**: Reading sub-channel Pools (Tactile, Temporal, Biomechanical, Rhythmic, Thread); Initiative
- **Spi**: Thread-op commits in combat; Coherence interaction
- **Bon, Cha**: not combat-active by default; Bon factors into Death Cascade via Knot mechanics (combat_v30 §13.3 + threadwork Knot rules); Cha affects Composure (social fallback if combat de-escalates)

### 2.2 Dice engine (params/core.md §Die Rule, §Continuous Engine)

- d10 face rule: 1 = −1 success, 2–6 = 0, 7–9 = +1, 10 = +2; no chain
- TN values: 6 / 7 / 8 (controlled / standard / desperate)
- **Continuous engine canonical for Godot**: `net ~ Normal(μ·N, σ·√N)` with per-die statistics per TN
- **Fractional TN and Ob canonical** (PP-717 Fiore half-step TN ratified; this proposal extends fractional Ob throughout phase modifiers)
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

## 4. THE EIGHT-PHASE ENGAGEMENT LOOP

This section replaces combat_v30 §§2–4 in their entirety.

### 4.1 Loop structure

A combat encounter consists of one or more **passes** through the eight-phase loop. Each pass represents 15–30 seconds of in-fiction time. Termination conditions per §4.4. The Bout (Phase 6) is the primary engagement substance; phases 1–5 set up the Bout; phases 7–8 resolve and reset.

| Phase | Name | Primary mechanic | Initiative effect | Duration target |
|---|---|---|---|---|
| 1 | Stance | Player choice; sets derived state (Signal, Sensor gating, Stance Counter, Concentration recovery rate) | Simultaneous | Player ~5s |
| 2 | Position | Player choice (stance-narrowed options); sets Phase 5 Commit Pool modifiers, Signal Level adjustment | Simultaneous | Player ~3s |
| 3 | Approach | Player choice (5 options); opposed Approach Pool vs opponent's Reaction Pool determines zone arrival | Higher init first | Player ~3s |
| 4 | Reading peak | Deterministic + Player choice (attention split); sensor-channel Pools fire vs opponent Signal | Simultaneous (rolls fire concurrently) | Engine ~2s |
| 5 | Commit | Player choice (action class + depth); initiates Bout if commit lands. Sequenced by Initiative within phase. | Higher init first; clash if mutual full | Player ~5s |
| 6 | Bout | Sub-action chain; simultaneous-declared per chain step; AI-driven default with player intervention at decision-state changes | Simultaneous-declared per chain step | Engine + player ~10s |
| 7 | Disengage | Player choice (5 options); opposed Disengage Pool when pursued | Higher init first | Player ~3s |
| 8 | Return | Default + Player choice (when wound-state filter narrows >1); recovery applies | Simultaneous | Player ~2s |

Pacing target: **30–60 seconds player time per pass**, representing **15–30 seconds of in-fiction action**. A 3-pass duel resolves in 1.5–3 minutes of play.

### 4.2 Phase 1 — Stance

Player chooses a stable bodily configuration from trained Stance specializations (per §5 aspect catalog). Stance is sustained — it persists across the pass and affects subsequent phases.

**Mechanical effects:**
- Sets baseline **Signal Level** (low/medium/high — ambiguous stances reduce signal)
- Gates **Reading sub-channel bonuses** (each Stance favors specific channels)
- Sets **Stance Counter Ob modifier** vs opponent's chosen Stance (per §7 Stance Counter Matrix; fractional Ob)
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
- **Angled approach**: close from off-line, arrives with facing advantage. Cost: 1 Stamina; takes 2 zone transitions
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
| Temporal | Free of bind, at measure | Opponent's commitment-window timing | `(Att × 2) + AspProf(Reading-Temporal) + History` |
| Geometric | Stable Positions (Phase 1–2) | Positional vulnerabilities | `(Cog × 2) + AspProf(Reading-Geometric) + History` |
| Biomechanical | During opponent's Commit (Phase 5) | Initiation order of opponent's motion | `(Att × 2) + AspProf(Reading-Biomechanical) + History` |
| Rhythmic | Multi-pass (after pass 2) | Opponent's cadence | `(Att × 2) + AspProf(Reading-Rhythmic) + History` |
| **Thread** | TS ≥ 30 (params/threadwork) | Opponent's thread state, Coherence integrity, Conviction strain | `(Spirit × 2) + History + TPS` per Thread Pool canon |
| **Intent** | At measure before Commit (Phase 4–5); higher tiers in Bout | Opponent's pre-motor state; tier-keyed abilities | `(Cog × 2) + Intent Reading track value` (see §6) |

**Resolution:** rolls vs opponent's Signal Level as fractional TN. Net successes produce **Reading modifiers** applied as fractional Ob modifiers on Phase 5 Commit and Phase 6 Bout sub-actions.

| Net successes | Reading-modifier effect |
|---|---|
| 0 (failure) | No information; Commit/Bout resolves at base Ob |
| 1 (partial) | Class read (commit category visible) — Phase 5 Commit Pool +0.5 Ob modifier for *information advantage* |
| 2 (success) | Class + Depth read — Phase 5 Commit Pool +1.0 Ob modifier |
| 3+ (overwhelming) | Full read — Phase 5 Commit Pool +1.5 Ob; in Bout, sub-action options expanded by 1 (precognition surface) |

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

**Commit initiates Bout** (Phase 6). The commit's action class + depth + Reading modifiers + Stance Counter + Reaction-aspect modifier + facing modifier + weapon-class phase-strength + Signal Level effect produce the **opening sub-action** of the Bout chain.

### 4.7 Phase 6 — Bout (primary engagement substance)

The compressed exchange. 6–10 seconds in fiction; engine resolves a sub-action chain with player intervention at decision-state changes.

**Sub-action chain model:** simultaneous-declared per chain step. Both fighters declare from current engagement state's option set. Both resolve. State updates. Next step proceeds until termination.

**Engagement states (Bout has internal sub-state):**

| Sub-state | Sub-action options |
|---|---|
| **Out-of-contact** (entering Bout from a commit miss) | Probe-cut / Probe-thrust / Step-around / Disengage-to-Phase-7 |
| **Closing** (weapons in striking distance, contact imminent) | Cut / Thrust / Press-the-bind / Yield-to-bind / Void-and-counter |
| **In-bind** (weapons in sustained contact; Tactile channel active) | Wind / Yield / Press / Displace / Break-bind / Grip-change (weapon-class dependent) |
| **Breaking** (one fighter committed to disengage) | Pursue / Release / Throw-strike (attack of opportunity) — leads to Phase 7 |

**Sub-action Pool composition** (per sub-action):

```
Sub-action Pool = (relevant-attribute × 2) + AspProf(Reaction or other aspect) + History modifier
```

Relevant-attribute per sub-action class:
- Cut/Thrust: Agi (light) or Str (heavy); per weapon class phase-strength
- Press/Wind: Str
- Yield/Void: Agi
- Displace/Grip-change: Str + Agi composite (sim-tunable)
- Disengage: Agi
- Probe: Agi

**Ob composition per sub-action** (fractional):
```
Effective Ob = base Ob (typically 1–3)
  + Stance Counter Ob modifier (§7)
  + Reaction-aspect Ob modifier (§7)
  + Reading-modifier (from Phase 4 net successes)
  + Aspect coherence modifier (§7)
  + Weapon-class phase-strength modifier (§8)
  + Facing modifier
  + Signal Level effect
```

**Player intervention triggers** (engine pauses for player decision):
- (a) Opponent's commit depth crosses player's response threshold
- (b) Bind state transitions (out-of-contact ↔ in-bind)
- (c) Sensor channel reveals previously-occluded information
- (d) Resource crosses critical threshold (Concentration <30%, Stamina <30%)
- (e) Thread-mediated sub-action becomes available (TS-gated)

Outside triggers, Bout auto-resolves via Conditional Logic Profile (§5) drawing on aspect specializations.

**Termination conditions:**
1. **Wound transition**: a sub-action lands at "significant consequence" — net successes ≥ Ob + (current wound count + 1) — pushing wound state. Chain ends; control passes to Phase 7.
2. **Both separate**: both fighters declare Disengage sub-action. Chain ends; Phase 7 fires simultaneously.
3. **Concentration depletion**: either fighter's Concentration drops below 30% threshold. Chain ends; depleted fighter forced into Phase 7 (per Spent threshold).
4. **Stamina depletion**: either fighter's Stamina drops below 30%. Chain ends; depleted fighter forced into Phase 7.
5. **Chain cap reached**: depth-keyed cap (§4.6 table) reached. Chain ends; Phase 7 fires.
6. **Mutual deep-commit clash**: both fighters depth ≥ 4 sub-action collision. Resolves by highest Pool net successes; one wounds, one's commit fails. Chain ends.

**Edge case rulings:**
- **Mutual depth-5 (full) clash**: both Pools roll opposed; both apply wound consequences at net-successes magnitude. If tied, both heavily wounded.
- **Mutual depth-5 with one Thread-op**: Thread-op resolves first per P-01 temporal-auto-effect ordering (the metaphysical co-movement happens before the martial outcome).
- **Chain-termination ambiguity** (multiple conditions fire same step): priority 1, 5, 2, 6, 3, 4 (wound first; chain cap second; mutual separation third; clash fourth; resource depletion fifth/sixth).
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
| 1 | Long-thrust dueling tradition | Forward-point stance + Linear footwork + Standard grip + Direct/Explosive approach + Temporal reading + Hand-led reactions + Decisive commitment + Clean/Pursuing disengage | Hafenmark formal duelists; Crown court fencing | Tier 2 (Steady) | Long thrust-primary |
| 2 | Long-blade contact tradition | Centered/Raised stances + Linear + Standard grip with half-grip-available + Direct press + Tactile reading + Yielding/Pressing reactions + Sustained commitment + Defensive disengage | Crown infantry; mixed faction soldiery | Tier 1 (Surface) | Long cut-and-thrust |
| 3 | Long-thrust geometric tradition | Forward-point + Curvilinear footwork + Standard grip + Angled approach + Geometric reading + Hand-led + Cautious commitment + Defensive disengage | Crown court advanced fencing academy (theoretical/mathematical training); Löwenritter officer training | Tier 1 (Surface) | Long thrust-primary |
| 4 | Counter-time tradition | Centered/Side stances + Linear + Standard + Drawing approach + Temporal/Biomechanical reading + Reactive anticipation + Hand-led counter reactions + Defensive disengage | Crown court fencing masters; Hafenmark senior duelists; rare in other factions | **Tier 4 (Pre-empt)** | Long thrust-primary; Long cut-and-thrust |
| 5 | Single-strike tradition | Stance-flux mid-Bout (per §5.5.1 Apprentice technique) + Linear + Standard + Direct/Drawing + Intent reading focus + Body-led reactions + Decisive commitment + Clean disengage | Niflhel sword-saints (peripheral monastic lineage); rare Restoration Movement contemplative wing | **Tier 5 (Master)** | Long cut-and-thrust; Single short (formal seppuku-equivalent context) |
| 6 | Curved-blade cavalry tradition | Variable stance + Bursting footwork + Thumb-anchor grip + Direct press approach + Rhythmic reading + Pressing reactions + Burst commitment + Pursuing disengage | Crown light cavalry; Varfell highland raiders; Hafenmark merchant-escort cavalry | Tier 1 (Surface) | Curved cut-primary |
| 7 | Continuous-flow tradition | Continuous (no discrete stance) + Triangular footwork + Paired grip + Angled approach + Rhythmic reading + Voiding reactions + Sustained commitment + Sudden disengage | Niflhel highland practice (paired-blade form); Restoration Movement Thread-aware practitioners (continuous flow as Thread-state combat) | Tier 2 (Steady) | Paired short; secondary Continuous-blade variant |
| 8 | Mounted multi-weapon tradition | Mode-dependent stance + Bursting footwork + Variable grip + Direct approach + Geometric/Temporal reading + Pressing reactions + Burst commitment + Pursuing disengage | Löwenritter knightly cavalry (signature tradition); Crown heavy cavalry | Tier 2 (Steady) | Long pole (lance); Curved cut-primary (saber dismounted); Long cut-and-thrust (sword dismounted) |
| 9 | Conditioning-and-grappling tradition | Centered + Linear + (body grip) + Direct + Body-contact reading + Yielding/Pressing + Sustained + Clean | Niflhel highland practice; Varfell light infantry; Restoration Movement militia training | Tier 1 (Surface) | Single short (close-range backup); unarmed |
| 10 | Formation-and-discipline tradition | Variable + Linear with formation positioning + Variable + Coordinated approach + Temporal + Disciplined defaults + Patterned anticipation + Defensive | Crown infantry (line formation); Church Templars (formal protocol); Löwenritter ground formation | Tier 1 (Surface) | Long pole (spear/pike); Long cut-and-thrust (formation backup) |

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
- Reading: Temporal primary (Long-thrust) AspProf 3; Biomechanical secondary (Counter-time) AspProf 2 cap
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
| 1 (Apprentice) | Tempo-read setup | Phase 4 Reading peak | Temporal channel + Biomechanical channel attention split with no Conc penalty (normally costs 1 Conc) |
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

This section enumerates the 10 aspects, their specializations, and mechanical effects. All magnitudes draft; sim-tunable per I-17.

### 6.1 Stance

**Sustained bodily configuration.** Sets Phase 1 baseline state for the pass. Sustained — persists across phases until Phase 8 Return.

| Specialization | Available positions | Sensor channel bonus | Signal Level | Concentration recovery |
|---|---|---|---|---|
| Centered guard | Universal (cut, thrust, parry) | Tactile (bind-ready) | Medium | Standard (+Focus per Phase 8) |
| Raised guard | Descending cuts | Geometric (high overview) | High (telegraphed) | Standard |
| Low guard | Rising attacks; bind-baiting | Temporal (reads opponent commitment cleanly) | Low (concealed) | +1 (low-stress posture) |
| Side guard | Angled cuts; voiding | Biomechanical (reads opponent's motion clearly) | Medium | Standard |
| Forward-point guard | Thrusts; counter-time | Temporal + Intent (with §10 track) | Low (concealed; weapon as line) | −1 (tense posture) |

**Stance Counter Matrix** (§7.1) provides fractional Ob modifiers per stance-vs-stance matchup at Phase 5 Commit.

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

**Primary sensor channel preference.** The 5 mundane channels + Thread (TS-gated) are the Phase 4 Reading peak menu (§4.5). Specialization raises Aspect Proficiency in one or more channels.

| Specialization | Reading channel preferred | Notes |
|---|---|---|
| Tactile | Bout (bind state); Phase 6-active | Primarily reads in-bind opponent |
| Temporal | Phase 4 peak vs Free-of-bind opponent | Reads commitment timing |
| Geometric | Phase 1-2 (stable positions) | Reads positional vulnerabilities |
| Biomechanical | Phase 5 (during opponent commit) | Reads motion order |
| Rhythmic | Multi-pass (pass 2+) | Reads cadence; long-fight channel |
| Thread | TS 30+ required (canonical) | Reads thread state; canon per combat_v30 §10.2 |

**Intent reading** is *not* an Aspect spec under Reading. See §10 — separate progression track per Jordan canon override.

### 6.6 Anticipation

**Pre-commit prediction pattern.** Affects Phase 4 Reading peak attention split and Phase 5 Commit decision-window.

| Specialization | Mechanical effect |
|---|---|
| Predictive | Attention split bonus: secondary channel at 0.5 Pool instead of 0.3 |
| Reactive | Reading bonus *during* opponent's Commit: Biomechanical channel fires at +1D when opponent depths ≥3 |
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
| Escalating | Depth raises by 1 per pass beyond pass 1 (forced); cannot lower depth back |
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
- `phase_4 := { primary: "Temporal", split: 70/30, secondary: "Intent" }` (attention allocation)
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
ALSO phase_4 := { primary: "Intent", split: 70/30, secondary: "Temporal" }

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
THEN phase_4 := { primary: "Biomechanical", split: 50/50, secondary: "Intent" }
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

---

## 7. MATCHUP MATRICES (FRACTIONAL OB)

Three tables produce **fractional Ob modifiers** applied at Phase 5 Commit and Phase 6 Bout sub-action resolutions. Per Pillar 5, all modifiers operate within canonical Ob grammar.

### 7.1 Stance Counter Matrix

Per-stance × per-stance Ob modifier applied to **Aggressor's Phase 5 Commit** (and continuing into Bout sub-actions until stance changes). Anti-symmetric (cell [A][B] = −cell [B][A]); diagonal = 0 (same-stance no counter).

| Aggressor ↓ vs Defender → | Centered | Raised | Low | Side | Forward-point |
|---|---|---|---|---|---|
| Centered | 0 | +1 | 0 | −1 | +2 |
| Raised | −1 | 0 | +1 | 0 | +1 |
| Low | 0 | −1 | 0 | +1 | 0 |
| Side | +1 | 0 | −1 | 0 | −2 |
| Forward-point | −2 | −1 | 0 | +2 | 0 |

**Reading:** Values are Ob modifiers on the Aggressor's Pool. Negative = Aggressor advantaged (lower threshold to land); positive = Aggressor disadvantaged.

- Forward-point vs Centered: −2 Ob (Aggressor strongly favored — straight thrust against open guard)
- Centered vs Forward-point: +2 Ob (Aggressor at thrust disadvantage)
- Side vs Forward-point: −2 Ob (Side stance is the answer to Forward-point)

Magnitudes draft. Phase 11 sim (I-17) tunes to Fast-vs-Titan 50–60% target.

### 7.2 Reaction-aspect Ob modifier

Per Defender's Reaction × Aggressor's Commit-depth class, Ob modifier on Aggressor's Phase 5 Commit and resulting Bout sub-actions.

| Defender's Reaction | vs Probe / Preparatory (depth 1–2) | vs Committed (depth 3) | vs Deep (depth 4) | vs Full (depth 5) |
|---|---|---|---|---|
| Hand-led | +1 | 0 | −1 | −1 |
| Body-led | 0 | 0 | +1 | +1 |
| Yielding | −1 | +1 | +2 | +2 |
| Pressing | +1 | +1 | 0 | −1 |
| Voiding | +2 | +1 | 0 | −1 |

**Reading:** Values are Ob modifiers on Aggressor's Pool. Negative = Aggressor advantaged. Positive = Aggressor disadvantaged.

- Yielding vs Full: +2 (Yielding turns overcommitted opponents' force back on them)
- Voiding vs Probe: +2 (Voiding evades light attacks cleanly)
- Hand-led vs Full: −1 (Hand-led can't deflect deep commits — body must move)

Magnitudes draft; sim-tunable I-17.

### 7.3 Aspect coherence — pairwise modifier

Some aspect-pair combinations reinforce each other; others are awkward. **Pairwise across the 9 operational aspects** (CLP excluded as meta-aspect): 9 × 8 / 2 = **36 unique pairs**. Each pair: Synergistic / Neutral / Antagonistic.

**Mechanical effect**:
- **Synergistic pair**: when both aspects' Pools contribute to the same phase action, **+0.5 Pool** to that action
- **Neutral pair**: no effect
- **Antagonistic pair**: when both aspects' Pools contribute to the same phase action, **−0.5 Pool**

**Verdict scope.** Each pair's verdict applies at the aspect-pair level (i.e., default when specializations are chosen). Specific specialization-pair combinations may modulate (e.g., a default-Neutral pair may become Synergistic for one specific specialization combo). Specialization-level matrix deferred to future expansion; aspect-level matrix is the playable baseline.

#### 7.3.1 Full 36-pair matrix

Aspects sorted by phase order: Stance, Footwork, Grip, Approach, Reading, Anticipation, Reaction, Commitment, Disengage.

| Pair | Verdict | Reasoning |
|---|---|---|
| Stance × Footwork | Synergistic | Bodily configuration and movement pattern reinforce each other (Forward-point + Linear thrusts; Centered + Curvilinear bind work) |
| Stance × Grip | Synergistic | Weapon hold and stance posture co-determine reach and lines (Standard grip + Centered guard; Half-grip + Forward-point) |
| Stance × Approach | Neutral | Approach choice is independent of held stance (multiple stances support each approach) |
| Stance × Reading | Synergistic | Stance gates which Reading channels work best (Forward-point opens Temporal channel; Low guard opens Geometric) |
| Stance × Anticipation | Neutral | Stance is sustained; Anticipation pattern is moment-to-moment |
| Stance × Reaction | Synergistic | Stance prepares specific reactions (Centered = Hand-led ready; Side = Voiding ready; Forward-point = Pressing ready) |
| Stance × Commitment | Neutral | Stance affords all depths; depth chosen at Phase 5 |
| Stance × Disengage | Neutral | Disengage occurs after engagement; stance reset is independent |
| Footwork × Grip | Neutral | Movement and weapon hold are mechanically independent |
| Footwork × Approach | Synergistic | Movement pattern and closing preference tightly coupled (Linear + Direct press; Curvilinear + Angled; Bursting + Explosive) |
| Footwork × Reading | Neutral | Reading channels operate on opponent state, not own footwork |
| Footwork × Anticipation | Neutral | Independent — movement and prediction cognitively separate |
| Footwork × Reaction | Synergistic | Defensive movement enables specific reactions (Curvilinear + Voiding; Linear + Pressing) |
| Footwork × Commitment | Neutral | Independent at moment of Commit |
| Footwork × Disengage | Synergistic | Movement pattern shapes disengage execution (Drawing footwork + Drawing disengage; Bursting + Sudden) |
| Grip × Approach | Neutral | Grip determines weapon function; approach is closing-distance choice |
| Grip × Reading | Synergistic | Grip stability enables Tactile reading in bind (Standard grip with Half-grip-available + Tactile channel) |
| Grip × Anticipation | Neutral | Independent — grip is mechanical, anticipation cognitive |
| Grip × Reaction | Synergistic | Grip determines available reactive sub-actions (Standard + Yielding; Paired + Voiding) |
| Grip × Commitment | Neutral | All grips support all depths |
| Grip × Disengage | Neutral | Disengage independent of grip during separation |
| Approach × Reading | Synergistic | Approach phase fires Reading peak; aligned (Feinted Approach + Intent Reading reveals opponent's false-read response) |
| Approach × Anticipation | Synergistic | Approach choice expresses anticipation (Direct + Reactive; Feinted + Predictive; Drawing + Adaptive) |
| Approach × Reaction | Neutral | Approach is offensive; Reaction defensive — different domains |
| Approach × Commitment | Synergistic | Approach choice shapes Commit depth ceiling (Explosive + Burst; Drawing + Sustained) |
| Approach × Disengage | Neutral | Independent phases |
| Reading × Anticipation | **Synergistic** | Strongest cognitive synergy — Reading channels feed Anticipation patterns; Anticipation refines Reading attention split |
| Reading × Reaction | Synergistic | Reading reveals opponent commit class/depth, enabling specific defensive reactions |
| Reading × Commitment | Neutral | Reading informs Commit choice but doesn't structurally reinforce specific depths |
| Reading × Disengage | Neutral | Reading aids any disengage; no specific synergy |
| Anticipation × Reaction | **Antagonistic** | Pre-commit prediction and in-bout reflex pull cognitive resources different directions; Predictive Anticipation + Reactive Reaction is contradictory mental model |
| Anticipation × Commitment | Synergistic | Anticipation pattern shapes Commit depth preference (Predictive + Decisive; Adaptive + Escalating) |
| Anticipation × Disengage | Neutral | Disengage occurs after Anticipation has resolved into Commit/Bout |
| Reaction × Commitment | Synergistic | Defense style and attack depth interact in Bout (Yielding + Sustained Commitment + bind-fighter; Pressing + Decisive + tempo fighter) |
| Reaction × Disengage | Neutral | Reaction is in-Bout; Disengage transitions out |
| Commitment × Disengage | **Antagonistic** | Commit depth and willingness to break engagement inversely related at extremes (Burst Commit + Defensive Disengage = mismatched intensity; Sustained Commit + Sudden Disengage = whiplash) |

#### 7.3.2 Coherent build clusters

The matrix surfaces recognizable historical styles as **Synergistic-dense clusters**:

| Cluster | Aspects | Synergistic pairs in cluster |
|---|---|---|
| **Bind fighter** | Centered or Raised Stance + Linear Footwork + Standard grip with Half-grip-available + Direct press Approach + Tactile Reading + Patterned Anticipation + Yielding Reaction + Sustained Commitment + Defensive Disengage | Grip × Reaction, Grip × Reading, Reading × Reaction, Reaction × Commitment, Stance × Reading; (Commitment × Disengage Antagonistic — must accept this tension) |
| **Thrust duelist** | Forward-point Stance + Linear Footwork + Standard grip + Direct/Explosive Approach + Temporal Reading + Hand-led Reactions + Decisive Commitment + Clean Disengage | Stance × Footwork, Stance × Grip, Stance × Reading, Stance × Reaction, Footwork × Approach, Reading × Anticipation (when applicable) |
| **Counter-time fighter** | Centered/Side Stance + Linear Footwork + Drawing Approach + Temporal+Biomechanical Reading + Reactive Anticipation + Hand-led counter Reaction + Cautious Commitment (with Decisive override on Reading-success via CLP) + Defensive Disengage | Approach × Anticipation, Reading × Anticipation, Reading × Reaction; (must manage Anticipation × Reaction Antagonism via training) |
| **Burst fighter** | Bursting Footwork + Explosive Approach + Burst Commitment + Sudden Disengage | Footwork × Approach, Approach × Commitment, Footwork × Disengage; (Commitment × Disengage Antagonistic — accept this tension; the Burst archetype is intentionally short-engagement) |
| **Continuous-flow fighter** | Side guard with stance-flux + Triangular Footwork + Paired grip + Angled Approach + Rhythmic Reading + Voiding Reaction + Sustained Commitment + Sudden Disengage | Footwork × Approach, Grip × Reaction; (Sustained Commitment + Sudden Disengage is Antagonistic — characteristic tension) — requires paired weapons (Paired short class) |

**Awkward builds.** A character with multiple Antagonistic pairs (e.g., Predictive Anticipation + Reactive Reaction + Burst Commitment + Defensive Disengage) accumulates −1.5D to −2D Pool modifiers across Bout sub-actions where these contributing aspects co-fire. Playable but mechanically inferior; produces unique characters who play unconventionally.

#### 7.3.3 Pool modifier composition

Per pass, the engine computes total Aspect coherence modifier as sum across all firing aspect-pair contributions:

```
Aspect coherence modifier (this sub-action) = Σ (±0.5 per Synergistic/Antagonistic pair that contributes Pool to this sub-action)
```

Cap: ±2D modifier per sub-action (prevents extreme aspect-coherence stacking).

Magnitudes draft. Sim validation per §15.7 Phase 14 (aspect-coherence sim).

---

## 8. WEAPON CLASSES (PHASE-KEYED STRENGTHS)

**Six weapon classes.** Each maps to the canonical 3-axis weapon TN matrix (combat_v30 §5: Reach × Weight × Type) and adds phase-keyed Pool/TN modifiers.

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

### 8.2 Damage modifier vs armor (canonical combat_v30 §5)

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

**Heavy plate implication:** Long thrust, Curved cut, Spear, Paired short, Single short all hit Heavy plate at +0 weapon modifier (must rely on net hits + STR damage; insufficient against high WI). Long cut-and-thrust also hits +0 at Heavy. **Only Heavy Blunt weapons (war hammer, pollaxe; canonical Long Heavy Blunt TN 8) bypass Heavy plate** — but this proposal's 6-class scheme doesn't include Long Heavy Blunt as a default class. Heavy-Blunt fighters use canonical Long Heavy Blunt (TN 8) and map to a 7th implicit class outside the proposal-canonical 6 (sim-tunable; possibly added per I-13b).

### 8.3 Phase-keyed Pool/TN modifiers

| Class | Strong phases (+0.5D Pool at action class) | Weak phases (−0.5D Pool) | Foreclosed sub-actions | Weapon Speed |
|---|---|---|---|---|
| Long thrust-primary | Phase 2 Position (precise telegraphing); Phase 3 Approach (lunge bonus); Phase 5 Commit (thrust class) | Phase 6 Bout (in-bind handling: degraded grip control on a thrust weapon) | Sustained-bind sub-actions (Wind, sustained Press); Grip-change without Half-grip-available | +1.5 |
| Long cut-and-thrust | Phase 6 Bout (Cut, Wind, Press sub-actions); Phase 5 Commit (depth ≥3 with Heavy Blade STR multiplier) | Phase 3 Approach (heavier weapon, slower close) | Sudden disengage at depth 5 (committed Heavy Blade is hard to abort) | +0.5 |
| Curved cut-primary | Phase 3 Approach (continuous-cut entry); Phase 5 Commit (cut class) | Phase 6 Bout (limited binds; curved blade slides out of contact) | Half-sword grip; Sustained-bind sub-actions | +2 |
| Long pole (spear) | Phase 2 Position (reach advantage); Phase 3 Approach control (zone distance) | Phase 6 Bout (close-range disadvantaged); Phase 6 In-bind precision | In-bind precision sub-actions (Wind requires shorter weapon); Throw-strike at close range | 0 |
| Long pole (staff) | Phase 2 Position; Phase 6 Bout Press/Displace (Blunt force in bind) | Phase 5 Commit (no cutting; lower wound transition rate) | Cut/Thrust sub-actions; weapon is Blunt only | 0 |
| Paired short | Phase 6 Bout (flow — both blades active); Reaction sub-actions (off-hand parry) | Phase 5 Commit (no decisive single strike with one blade) | Depth-5 Commits (Paired short cannot achieve full-commit decisive strike); Grip-change (paired grip locked) | +2.5 |
| Single short | Phase 6 Bout (close-range); Reaction speed | Phase 3 distance control (short reach loses zone) | Reach-dependent options (cannot engage at Long Reach without closing) | +3 |

### 8.4 Sub-actions available per weapon class

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

### 8.5 Cross-armor combat considerations

- **Heavy plate vs Heavy plate**: combat keys to seeking gaps (grip-change, half-sword, grappling sub-actions); Long cut-and-thrust + Half-grip-available aspect is the canonical answer
- **Light vs Heavy plate**: light attacker (typically Single short / Paired short / Long thrust) must seek joint/gap lines through advanced techniques (Targeted-line sub-action, I-13b); otherwise reduced consequence per canonical weapon-modifier-vs-armor table — typical outcome: many sub-actions land but no wound transition
- **Heavy plate's Stamina tax**: per canonical derived_stats §4.2 + this proposal §9.1, Heavy plate +2 Stamina per phase action. Sustained engagement against Light attacker depletes Heavy-plate Stamina before wounds accrue. Stamina-economy fighter (Sustained Commitment) in Light armor may outlast Heavy plate

### 8.6 Weapon-class fit with combat Histories

| Class | Best-fit Traditions |
|---|---|
| Long thrust-primary | Long-thrust dueling; Long-thrust geometric; Counter-time (Forward-point stance + Linear footwork standard set) |
| Long cut-and-thrust | Long-blade contact; Single-strike (specifically when paired with depth-keyed striking) |
| Curved cut-primary | Curved-blade cavalry; Continuous-flow (continuous cuts + Triangular footwork) |
| Long pole | Formation-and-discipline (formation pole arms); Mounted multi-weapon (lance variant) |
| Paired short | Continuous-flow (paired grip + Triangular footwork); Conditioning-and-grappling (off-hand for grappling support) |
| Single short | Conditioning-and-grappling (close-range backup); any tradition for off-hand backup |

Wielding a weapon outside its best-fit Tradition is mechanically suboptimal — the character's aspect specializations don't reinforce the weapon's strong phases. Possible but penalized.

### 8.7 Sim validation

Phase 11 sim (I-17 post-pivot) validates that weapon class differentiation produces distinct viable builds — Fast (Single short, Paired short) vs Strong (Long cut-and-thrust) vs Reach (Long pole) at 50–60% balance across symmetric optimization.

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

Reading Intent is the foundational perceptual discipline of pre-motor opponent reading. Per Jordan canonical override (2026-05-XX), Intent maintains its own progression track and unlocks specific abilities at training tiers — separate from the Reading aspect's other channels (Tactile, Temporal, Geometric, Biomechanical, Rhythmic, Thread).

### 10.1 Why separate

Intent Reading is qualitatively distinct from the other Reading sub-channels. Where Tactile reads pressure and Geometric reads positions, Intent reads the *pre-motor state* — what opponent is about to do, before their body commits. This requires perceptual training that doesn't transfer from general martial proficiency. A master swordsman who never studied fühlen-equivalent Intent reading may have all five mundane channels at Master tier (5) Aspect Proficiency and Intent at Surface (1) on this track.

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

**Builds across Phases 1–3** (ambient observation; Geometric channel in Phases 1–2; Temporal at Phase 4 measure).
**Peaks at Phase 4** before Commit.
**Updates from Phase 6 Bout** (Tactile in bind-active states; Intent at Tier 2+ Sustained Read).
**Partial reset in Phase 7–8** (sensor-channel state preserved selectively; Rhythmic channel reads persist across passes).

Reading produces **Reading modifiers** — fractional Ob modifiers applied to opponent's Commits and Bout sub-actions, per §4.5 net-success table.

### 11.2 Facing

Angular orientation between practitioners. **Not binary** — facing has fractional values representing alignment.

**Changes during:**
- Phase 3 Approach: Angled approach (§4.4) produces facing advantage; Drawing approach holds facing
- Phase 6 Bout: Voiding sub-action (§12) changes facing; Curvilinear or Triangular Footwork enables mid-Bout facing changes; Bursting enables facing reset

**Mechanical effects:**

| Facing state | Effect on Aggressor's Phase 5 Commit + Bout sub-actions |
|---|---|
| Square (full-face) | 0 Ob modifier |
| Quarter (off-line) | −0.5 Ob (Aggressor advantaged) |
| Flank | −1 Ob (Aggressor advantaged; Defender cannot use Body-led, Yielding, or Voiding reactions) |
| Rear | −2 Ob (Aggressor advantaged; Defender cannot use any reactive aspect except Hand-led at penalty) |

Facing state is tracked per pass; resets to Square on Phase 8 Return unless Phase 3 specifically held facing advantage.

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

**Recovery:** Phase 8 only: `+Focus` per pass. No recovery during Bout.

**Threshold effects:**

| Concentration level | Effect |
|---|---|
| <30% of max | Reading sub-channel rolls at −1D; opponent gains +0.5 Ob advantage during Bout |
| <20% of max | Commit depth ceiling drops by 1 |
| <10% of max | Cannot enter Phase 6 Bout — Phase 7 Disengage forced |
| 0 (Spent — canonical social-contest threshold) | −2D all combat rolls; resets to max per canonical social-contest Regroup rule; functionally similar to Stamina Out-of-Breath in combat |

**Social-combat shared pool:** a character entering combat after a social contest carries reduced Concentration. A character whose Concentration was Spent in a social exchange (canonical: resets to max) enters subsequent combat at full pool, but the next social contest in the same scene carries combat-drained Concentration.

### 11.5 Stamina

Canonical formula `Endurance × 5` (derived_stats §4.2). Per-phase costs reweighted for the eight-phase structure (replaces canonical action-cost table; see §4 phase descriptions).

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
| Armor passive drain per pass | +0 (None) / +0 (Light) / +1 (Medium) / +2 (Heavy plate) | Per canonical derived_stats §4.2 armor mod |

**Recovery:** Phase 8: `+(Endurance + relevant combat History) × 2`, capped at max (canonical Take a Breath formula preserved). No recovery during Bout.

**Threshold effects** (canonical):
- 0 (Out of Breath): −2D all combat rolls until recovery action taken

**Threshold effects** (new; sim-tunable):
- <30% of max: reaction sub-actions in Bout compress (chain max −1 step)
- <20% of max: Commit depth ceiling drops by 1
- <10% of max: Phase 5 Commit available only at probe/preparatory depths

### 11.6 Resource asymmetry — combat as dual-resource contest

Per Pillar 3, Concentration and Stamina drain asymmetrically. A character may be **physically fresh but mentally exhausted** (sustained Reading + deep commits → Concentration low; Stamina untouched) or **physically spent but mentally sharp** (Bursting Footwork + Explosive Close + Burst Commitment → Stamina low; Concentration low only if Bout chains were sustained).

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
| **Closing** (weapons in striking distance, contact imminent) | Cut, Thrust, Press-the-bind, Yield-to-bind, Void-and-counter, Disengage |
| **In-bind** (weapons in sustained contact; Tactile channel active) | Wind, Yield, Press, Displace, Break-bind, Grip-change (weapon-class dependent), Throw-strike |
| **Breaking** (one fighter committed to disengage; other has choice to follow or release) | Pursue, Release, Throw-strike (pursue with attack of opportunity) — leads to Phase 7 |

Each engagement state surfaces 3–6 sub-action options. Aspect Reaction specialization gates which options are surfaced as **player-default** in AI-driven mode; other options surface only on player intervention.

### 12.2 Per-sub-action Pool composition

All sub-action Pools follow canonical grammar:

```
Sub-action Pool = (relevant-attribute × 2) + Aspect Proficiency + History modifier
```

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

**Wound penalty applies** (canonical PP-716 / derived_stats §4.1): −1D per Wound on all sub-action Pools.

### 12.3 Per-sub-action Ob composition

```
Effective Ob = base Ob (typically 1–3 per sub-action class)
  + Stance Counter Ob modifier (§7.1, persists from Phase 1 stance)
  + Reaction-aspect Ob modifier (§7.2, per Defender's Reaction × Aggressor's Commit-depth class)
  + Reading-modifier (from Phase 4 net successes, per §4.5)
  + Aspect coherence modifier (§7.3, fractional)
  + Weapon-class phase-strength modifier (§8, ±0.5D Pool — note: applies to Pool, not Ob, per §8)
  + Facing modifier (§11.2)
  + Signal Level effect (§11.3, applies to defending-against-read rolls)
```

Fractional Ob accumulates without quantization; canonical continuous-engine resolution handles fractional values.

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

Magnitudes draft; sim-tunable I-17.

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

This is one Bout chain at depth 3. Demonstrates fractional Ob composition, Reading-modifier inheritance, Stance Counter persistence, sub-action Pool variety, termination on engagement-state change.

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

Combat World Bridge per combat_v30 §13 is **fully preserved**. This proposal does not modify §13. Summary of canonical mechanics that fire from combat_v31 engine outcomes:

| §13 Component | combat_v31 trigger |
|---|---|
| §13.1 Domain Echo (faction officer outcomes) | Triggered at pass-end (Phase 8) on identified-named-NPC opponent with faction office. Outcome = wound state at end (Heavily wounded = defeated; killed via Death Cascade). |
| §13.2 Combat Reputation Cascade (0–6+ tiers) | Public combat (3+ witnesses) accumulates Combat Reputation. |
| §13.1b Resources / loot | Equipment changes on combat outcome interact identically (Phase 7 Disengage → Resources gain table). |
| §13.2b Settlement-Level Consequences | Combat in a settlement produces Order, Disposition, Garrison Size feedback per canon. |
| §13.3 Death Cascade (5 steps) | All 5 steps fire on Killed wound state at pass-end: (1) Knot rupture, (2) Scene Slate priority, (3) Faction Stability/Succession, (4) Exposure, (5) Player Conviction test. |

### 15.2 Mass combat interface (combat_v30 §9, §11 preserved)

Mass combat (combat_v30 §9 TTRPG scale, §11 faction unit rosters) is **preserved**. Personal-scale combat_v31 transitions to mass combat via canonical scale_transitions_v30 mechanics. Mass combat uses canonical Martial/Discipline stats, not combat_v31's eight-phase loop.

**Transition rules:**
- Personal combat in a mass-battle context: combat_v31 fires per pass; mass-battle resolution continues on engine tick clock
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
| PP-XXX-B | Establish combat_v31 eight-phase engagement loop as canonical combat engine | combat_v30, derived_stats |
| PP-XXX-C | Concentration combat extension: derived_stats §5.2 social-contest formula extended to combat use; per-phase drain rates established | derived_stats §5.2; combat_v31 §11.4 |
| PP-XXX-D | First-round Initiative spec: `Att + Weapon Speed` with Cog/Agi tiebreak | combat_v30 §3 (PP-232 augment) |
| PP-XXX-E | Reach terminology unified to PP-290 (Short Reach / Long Reach / Ranged); supersedes PP-268 | combat_v30 §5 |
| PP-XXX-F | Stunt mechanic Authored mode: scene-metadata-driven, replaces GM-set N dice | combat_v30 §4 (Stunt entry) |
| PP-XXX-G | Strike action retired as canonical primary; Bout (Phase 6) replaces as primary engagement substance; canonical Strike/Feint/Disarm/Tie Up/Retrieve become Bout sub-actions per engagement state | combat_v30 §4 |
| PP-XXX-H | Three-state wound display layer (Unwounded / Wounded / Heavily wounded) over canonical 4-wound math; does not modify canonical Health/WI/MW formulas | derived_stats §4.1; combat_v31 §9.2 |
| PP-XXX-I | Intent Reading track established as separate progression from Reading aspect specializations; Tier 0–5 with ability unlocks | combat_v31 §10 |
| PP-XXX-J | Aspect specializations established as History sub-skills (audit principle #4 aligned); aspect Proficiency advances within History; Tradition Depth derived from History points | combat_v31 §5, §6; player_agency (Histories) |

### 15.6 Cross-system propagation list

Documents requiring update on ratification:

| Document | Change required |
|---|---|
| `designs/scene/combat_v30.md` | Strike §§1–4 with [SUPERSEDED-BY: combat_v31] markers; §§5 weapon system retained as canonical mapping; §§9, 10, 11.5, 13 preserved unchanged |
| `params/combat.md` (pending refresh) | Rewrite Pool composition formulas per combat_v31 phase structure; per-phase Stamina/Concentration costs; sub-action Pool table |
| `references/canonical_sources.yaml` | Update combat system canonical path: `designs/scene/combat_v30.md` → `designs/scene/combat_v31.md` (proposal file becomes canonical on ratification) |
| `designs/scene/derived_stats_v30.md` | §5.2 Concentration: add combat extension note |
| `designs/scene/threadwork_v30.md` | §2.3 visibility table cross-reference; no content change |
| `designs/provincial/mass_battle_v30.md` | §A.10 (Command checks) reference combat_v31 wound state; no formula change |
| `designs/scene/fieldwork_v30.md` | §11.5 transitions preserved; cross-reference combat_v31 |
| `designs/architecture/social_contest_v30.md` | Concentration shared-pool note (open: may require separate-pool variant) |
| `npc_behavior_v30.md` | §3.4 cross-system fire from combat preserved; NPC Conditional Logic Profile spec aligns to combat_v31 §6.10 |

### 15.7 Sim validation work needed

| Sim | Purpose | Acceptance |
|---|---|---|
| Phase 11 combat_v31 v1 sim (I-17 pivoted) | Validate Fast vs Strong build differentiation under eight-phase loop + fractional Ob | Fast (Agi-stacked, Single short) vs Strong (Str-stacked, Long cut-and-thrust) at 50–60% across symmetric optimal builds |
| Phase 12 dual-resource economy sim | Validate Concentration + Stamina create meaningful build differentiation | Burst, Sustained, Counter-time builds each viable; no dominant strategy across resource axes |
| Phase 13 Intent track sim | Validate Tier 4 Pre-empt economy doesn't break game balance | Pre-empt activates 0.2–0.4× per pass at Tier 4; combat lethality not >2× canonical baseline |
| Phase 14 aspect-coherence sim | Validate 45-pair coherence matrix doesn't produce one-build-dominates outcome | Three distinct "coherent" archetype builds within 5% win-rate margin |

### 15.8 Open items (consolidated)

- **I-11** (Pass 2c expansion): Full 45-pair aspect coherence matrix; specific Pool/Ob magnitudes per spec mechanical effect (currently draft)
- **I-12** (Pass 2c expansion): Valoria-faction-binding for additional 5 traditions (Long-thrust geometric, Curved-blade cavalry, Continuous-flow, Mounted multi-weapon, Formation-and-discipline); Tradition technique trees
- **I-13** (Pass 2c expansion): Weapon TN matrix refresh — six weapon classes' canonical 3-axis mapping + phase-strength values
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
| Eight-phase engagement loop | dueling_combat_proposal.md §2 (2026-05-24 upload) |
| Aspect specialization framework (10 aspects × 5 specs) | dueling_combat_proposal.md §5 |
| Tradition learning bundles (recast as Histories) | dueling_combat_proposal.md §6; reframed per audit principle #4 |
| Reading sub-channels (5 mundane + Thread + Intent) | dueling_combat_proposal.md §3; Intent extracted to separate track per Jordan canon override 2026-05-XX |
| Six weapon classes with phase strengths | dueling_combat_proposal.md §7; mapped to canonical 3-axis weapon TN matrix |
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

- Full 45-pair aspect coherence matrix (sample only in §7.3)
- Specific per-spec mechanical magnitudes throughout (draft sim-tunable)
- Conditional Logic Profile UI/syntax
- Five additional Tradition catalog entries with Valoria-faction binding
- Weapon TN matrix refresh with specific phase-strength values
- Full sim validation results

---

*End of consolidated rewrite. Pass 3 (verification) follows in the next turn.*
