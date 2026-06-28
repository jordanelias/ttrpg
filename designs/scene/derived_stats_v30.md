# VALORIA — Derived Stat System Specification
## Status: CANONICAL
## Date: 2026-04-18
## Status: PROPOSAL — supersedes prior derived_stats_v30.md
## Scope: Unified derived value system across personal, unit, settlement, and faction scales
## Principle: Stats are what your faction/character CAN do. Derived values are what they HAVE right now.

---

## §1 — Core Architecture

Every 1–7 stat remains the dice pool for its resolution system. No change to the dice engine. Each stat additionally produces a **derived value** — a granular resource the player tracks and the engine consumes.

**Derivation formula:** `derived_value = attribute × multiplier`

One attribute per derived value. No multi-attribute combinations. History and equipment modify drain/recovery rates, never the base pool size. The multiplier is an integer constant, calibrated to the interaction frequency of the system.

Stats change rarely (structural capability). Derived values change frequently (current state). The two-layer split exists because stats serve the resolution engine (small integers for dice pools) while derived values serve the state engine (large integers for resource tracking). These are different jobs requiring different scales.

**Documented exceptions (TD-1/TD-2, audit 2026-05-15).** The claim "no change to the dice engine" applies to the d10/TN/Ob/degree primitives; small parameter shifts have occurred under PP-717 (crit threshold raised from ≥3 to ≥4) and combat-layer half-step TN conventions (PP-717 Fiore: base 7.0, 2H −0.5). The derived-value formula `attribute × multiplier` has one documented exception: Health uses `round(WI × (MW+1) + 0.25 × Strength × End)` with `WI = round(End + 4 + 0.4 × Spirit)` and MW cap 3 (PP-716/PP-717 D1; D-A noise terms ED-1021), preserving the wound-interval × wound-count structure that a simple multiplier cannot capture. §4.1 is the authoritative spec.

**Engine duality (Decision E, 2026-05-15).** The engine is now specified two ways: discrete (d10 dice, legacy/TTRPG mode) and continuous (Normal-distribution sampling, videogame/Godot mode). Both produce statistically equivalent outputs. The continuous specification enables fractional Ob, fractional TN, and continuous degree resolution. See `params/core.md` §Continuous Engine for full spec. Derived stat formulas remain unchanged under either engine.

**Output scaling** (TroopCount only): `output = floor(integer_result × derived_value / max_derived_value)`, capped at ratio 1.0. Applied only to active capacity outputs (TroopCount → damage dealt). Not applied to survival resources (Vitality, Composure) — a depleted survival pool makes you easier to kill, not weaker at killing.

---

## §2 — The Problem

The 1–7 stat system was designed for a board game where stats ARE dice pools. For a videogame, it creates three problems:

1. **Granularity.** ±1 on a 1–7 scale is a 14–100% change in capability. You can't express "a modest drain."
2. **Feedback.** The player sees "Wealth 4 → 3" and must mentally calculate implications. No visceral feedback.
3. **Conflation.** "How capable is my faction" (capacity) and "what resources do I have" (state) are one number.

Resolution: stats remain 1–7 (correct pool range for d10 probability curves). Derived values provide granularity, feedback, and state tracking. Small numbers for decisions, big numbers for consequences.

---

## §3 — Multiplier Tiers

| Tier | Multiplier | Systems | Rationale |
|------|-----------|---------|-----------|
| High | ×10 (effective via MW+1) | Health | Combat has most interactions per scene (5–8+ rounds). Fine granularity for gradual degradation, wound thresholds, equipment differentiation. Note: Health uses non-multiplier `(End+6)×(MW+1)` — documented exception, §4.1 authoritative. |
| Medium | ×5 | Stamina, Thread Fatigue | Action economy resources deplete per-round/per-operation. Variable action costs (3–10 per action) without inflating numbers. |
| Low | ×3 | Composure, Concentration | Social contests are 1–5 exchanges. Lower multiplier gives equipment modifiers proportionally more impact. |
| Faction | ×10–100 | Treasury, Legitimacy, Reputation, Discipline | Seasonal interaction frequency (1–5 events/season). Each calibrated independently. |

**Calibration intent (V-2, audit 2026-05-15).** Multipliers are set per-system to match interaction frequency: more interactions per unit time → smaller multiplier (each tick matters more; smaller numbers track better at high event density). Faction multipliers (×10–100) reflect seasonal interaction frequency at a different timescale than personal-scale (×3–10). The system does not enforce a single derived formula — multipliers were calibrated independently against playtest data. Future systems should pick a multiplier matching their interaction frequency rather than mechanically deriving from a master formula.

---

## §4 — Personal Scale: Combat Resources

### 4.1 Health (survival resource) — AUTHORITATIVE (PP-716)

This section is the source-of-truth for the Health formula and wound mechanic across all systems. Other documents (combat_v30, threadwork_v30, params/combat, params/threadwork, params/mass_combat) reference this section rather than restating.

**D-A update (ED-1021, Jordan-ratified 2026-06-18).** To reduce uniformity, Spirit now adds a low-weight term to the Wound Interval and Strength a very-low-weight term (proportional to Endurance) to Health. The flat Wound-Interval base was lowered 6→4, the 2 points reallocated into these terms, so **average Health is conserved** (Endurance-4 average = 40, unchanged). Felling switched from a fixed wound count (≥ MW+1 wounds) to **Health depletion** (cumulative damage ≥ Health) so the Strength→Health buffer actually affects outcomes — under the wound-count rule it was inert. Equal average characters now fall in ~4–6 landed hits.

| Aspect | Specification |
|---|---|
| Stat name | Health |
| Underlying attribute | Endurance |
| Max Wounds | `Max Wounds = min(floor(Endurance / 2) + 1, 3)` — capped at 3 (PP-717) |
| Wound Interval | `WI = round(Endurance + 4 + 0.4 × Spirit)` — Spirit adds a low-weight, uniformity-reducing term (D-A, ED-1021). At average Spirit 3, `WI = round(End + 5.2)`. |
| Formula | `Health (full) = round(WI × (Max Wounds + 1) + 0.25 × Strength × Endurance)` — the Strength term (very low weight, proportional to Endurance) adds a survivability buffer that reduces uniformity (D-A, ED-1021). At average Strength 4. |
| Behavior | Total damage capacity. Non-resetting grand total. Each wound subtracts WI from Health. **Felled (incapacitated) at Health depletion (cumulative damage ≥ Health)** (D-A, ED-1021); the Strength buffer makes this slightly beyond MW+1 wounds, so Strength buys survivability. Coincides with the legacy 'MW+1 wounds = 0 Health' rule when the Strength buffer is zero. The wound counter (driving the −1D/wound penalty) still caps at MW+1. |
| Damage > WI in one hit | Multiple wounds applied simultaneously (each WI of damage = +1 wound counter). |
| Wounds clearance | All wounds clear at session end (canonical). Stabilised characters return to action after one full scene of rest. |
| Equipment | ~~Adds flat Health (+4 leather, +6 chain, +8 plate)~~ - **STRUCK 2026-06-05 (Jordan ratified): armour grants damage reduction only (DR/Resist; engine core.py RESIST), NOT flat Health - the engine WoundTracker takes no equipment_health**. Consumables restore on rest (+4 rations, +8 healer's kit). Poisons drain per round. |
| Wound penalty | −1D to ALL Pools (Combat, Thread — Leap, Weaving, Pulling, Mending, FR — Hybrid mass-battle Command). Universal rule. **No Ob penalty from wounds, ever.** Cumulative; capped by per-Pool floor (Combat Pool floor 5, Thread Pool floor 5 per threadwork §pool-floor). |

Per-Endurance reference table:

| End (avg Spirit 3, Strength 4) | WI | MW | Health (full) | wounds before felled |
|-----|----|----|---------------|---------------------|
| 1 | 6 | 1 | 13 | 1 (felled in the 2nd wound) |
| 2 | 7 | 2 | 23 | 2 (felled in the 3rd wound) |
| 3 | 8 | 2 | 27 | 2 (felled in the 3rd wound) |
| 4 | 9 | 3 | 40 | 3 (felled in the 4th wound) |
| 5 | 10 | 3 | 45 | 3 (felled in the 4th wound) |
| 6 | 11 | 3 | 50 | 3 (felled in the 4th wound) |
| 7 | 12 | 3 | 55 | 3 (felled in the 4th wound) |

Endurance-4 worked example (per Jordan canonical clarification 2026-05-09): Health 40 → 30 (1 wound) → 20 (2 wounds) → 10 (3 wounds, still alive at last threshold) → 0 (4 wounds, felled).

**Naming history.** "Vitality = Endurance × 10" was introduced by ED-694 as a simplification proposal. PP-716 reverts the simplification: the linear formula failed to match the WI × (MW+1) total-damage-capacity structure for End values 1, 2, 3, 5, 7 (only End 4 and 6 happened to align numerically). Stat name reverted from Vitality to Health for consistency with `params/combat.md` L16 and Jordan's design intent.

**Max Wounds cap (PP-717).** Simulation testing (v22–v24, 26 tests, 6 iteration rounds) found that the uncapped MW formula produces super-linear Health scaling — End 6 at 60 HP is 50% more than End 4 at 40 HP, making Endurance the dominant stat investment at all armour tiers (69–82% win rate for End-6 builds). Capping MW at 3 reduces End 6 to 48 HP (20% over End 4), preserves the WI × (MW+1) wound structure, and leaves End 1–5 unchanged. Sim-validated: top build drops from 69% to ~62% unarmoured (under 65% threshold). Historical precedent: plate armour wearers (high-End builds) were not invulnerable — exhaustion and mobility penalties limited their advantage.

**Wound penalty universality.** Prior canon (combat_v30 §thread, threadwork_v30 §2.3, §3, §5; params/combat.md §thread; params/mass_combat §CF wound) variously specified "+1 Ob per Wound" for Thread operations, mass-battle Command checks, and CF Zoom-In tactics. PP-716 unifies all wound penalties as −1D to the relevant Pool. The Ob channel is reserved for non-wound mechanics (Thread Sensitivity Ob bands, Mending Stability Ob, Cover Ob, Stunt Ob).

### 4.2 Stamina (action economy resource)

| Property | Value |
|----------|-------|
| Formula | (3 × Endurance) + (2 × Spirit)  [RATIFIED 2026-05-29 S1: replaces Endurance × 5. Stamina now draws on both Endurance (raw conditioning) and Spirit (will to keep going), per S2's expanded Spirit role. Armour remains a per-action drain modifier (below), not a base-Stamina reduction — resolving the armour-atom S⚠ flag.] |
| Range | 5–47 (Spirit/End 1–7) |
| Direction | Drains down from max |
| Depleted at | 0 (Out of Breath: −2D all combat rolls) |
| Recovery | Take a Breath: restores (Endurance + relevant combat History) × 2, capped at max |
| Equipment | Heavy armor: +2 drain per action. Medium: +1. Light/none: +0. |

**Variable action costs:**

| Action | Stamina Cost |
|--------|-------------|
| Standard attack | 5 |
| Heavy/special attack | 8 |
| Defensive stance | 3 |
| Dodge/disengage | 4 |
| Special maneuver (Feint, Disarm, etc.) | 6–10 |
| Movement (per zone) | 2 |

End 4: Stamina 20. Standard attacks at 5/round: 4 rounds before Out of Breath. Heavy armor (+2): effective 7/round, ~3 rounds. Take a Breath with History 3: restores (4+3)×2 = 14.

**Eliminates:** Current formula `End + History + 1 − armour_mod`. History moves to recovery. Armour moves from base reduction to drain modifier (Battle Brothers precedent: armor adds to per-action fatigue cost, doesn't reduce max fatigue).

**Precedent:** Battle Brothers fatigue system. Variable action costs create pre-combat decisions (loadout) and in-combat decisions (burst vs sustain). Viable in videogame because UI handles math.

**UI note:** Equipment screen should display "Estimated combat rounds: N" based on loadout weight and Endurance. No hard Endurance gate for armor — the Stamina math IS the gate.

---

## §5 — Personal Scale: Social Contest Resources

### 5.1 Composure (survival resource)

| Property | Value |
|----------|-------|
| Formula | Charisma × 3 |
| Range | 3–21 |
| Direction | Strain accumulates toward threshold; Rattled when strain ≥ Composure |
| Depleted at | Rattled: −1D per Rattled level to all contest rolls (cumulative) |
| Recovery | Full restore at scene change (unchanged) |
| Equipment | Court attire +2, Crown regalia +4, formal robes +3. Emotional state: +3 in own court, −3 confronting personal enemy. |

Strain per exchange: rescaled ×3.
Charisma modifier (attacker): `max(0, floor((Cha−3)/2)) × 3`. Range 0–6.
Focus defense (defender): `floor(Foc/2) × 3`. Range 0–9.

**Eliminates:** Current formula `Cha + 6`. Removes the +6 constant. Low-Cha characters become appropriately fragile in social contests.

[EDITORIAL: ED-939 — Rattled penalty channel corrected +1 Ob → −1D (PP-716 / Decision-B channel reservation: Ob channel reserved for circumstance, dice channel for condition); aligns §5.1 with §10.5. Outbound social-contest propagation pass, docket J-31.]

### 5.2 Concentration (action economy resource)

| Property | Value |
|----------|-------|
| Formula | (3 × Focus) + (2 × Spirit) |
| Range | 5–35 |
| Direction | Drains down from max |
| Depleted at | 0 (Spent: −2D next exchange, opponent +1D; then resets to max) |
| Depletion rate | −3 per exchange; −3 additional on exchange loss |
| Recovery | Regroup forfeit action: restores to max ((3 × Focus) + (2 × Spirit)) |

**Eliminates:** Current formula `Focus + Recall`. Recall removed — has no conceptual connection to sustained mental focus. Recall already provides +2D citation bonus in the Argue step (correct role for knowledge/memory). Concentration is sustained focus under pressure, governed by Focus (primary driver) plus Spirit (the will to sustain) — the `(3 × Focus) + (2 × Spirit)` form per ED-902 (2026-06-04, Jordan), superseding the Focus × 3 interim.

[EDITORIAL: ED-939 — §5.2 Concentration formula propagated Focus × 3 → (3 × Focus) + (2 × Spirit) to match §14.1 / §12 (ED-902); closes the intra-file contradiction. Outbound social-contest propagation pass, docket J-31.]

---

### 5.3 Inspiration (motivation resource — propagated 2026-04-25)

Inspiration is a per-character motivation resource representing the depth of a character's emotional or ideological investment in specific people, places, ideals, or objects (called "foci"). Inspirations grant +1D bonuses to actions taken in genuine pursuit of the focus and reduce Ob by 1 when spent strategically (per fieldwork_v30 §2.2).

| Property | Value |
|----------|-------|
| Formula | Total Inspiration value ≤ Spirit attribute (Resolve cap, params/core L128) |
| Range | 0 to Spirit per individual Inspiration; cumulative cap = Spirit across all foci |
| Direction | Spent (reduces value) and recovered (raises value) per scene engagement |
| Reset | Inspirations do NOT reset between scenes or seasons. They are persistent character resources, modified through play. |
| Recovery | Per-scene engagement with focus (see §5.3.2 below); maximum recovery 2 points per Inspiration per season |
| Loss | Focus permanently destroyed/captured/lost: Inspiration drops to 0 immediately (see §5.3.3) |

**§5.3.1 Inspiration Acquisition (mid-campaign)**

A character without an Inspiration may acquire one through play:

1. Player declares intent and names the focus (a specific named person, place, ideal, or object — not a category).
2. Two scenes where the character actively engages with the focus (GM/engine confirms engagement is genuine, not incidental).
3. After each scene: Spirit check TN 7, Ob 1.
   - **Both succeed:** Inspiration established at 1 point.
   - **One succeeds, one fails:** Inspiration established at 1 point with a **Complication Tag** — a narrative condition under which the Inspiration applies (e.g., "only while in Valorsplatz" or "contingent on Lenneth's survival"). The Complication Tag is set by the GM/engine and persists until the Inspiration is upgraded or lost.
   - **Both fail:** Focus not yet crystallized. Player may retry next season with new scenes.

**CP shortcut (G-053):** 4 CP + one scene of genuine engagement + one Spirit check (TN 7, Ob 1). Success: Inspiration at 1 point, no Complication Tag. Failure: 4 CP spent; retry available next season.

**Belief-to-Inspiration conversion:** Completing a Belief converts it to a new Inspiration at 1 point at no CP cost (the conversion is the reward — see §5.3.4 below for Belief mechanics overview). An NPC whose relationship with the character reaches significant depth (Disposition ≥ +4 sustained for 2+ seasons) may become an Inspiration focus through this conversion path.

**§5.3.2 Inspiration Recovery (from reduced value)**

When an Inspiration drops below its established value through use (Inspiration spend per fieldwork §2.2: 1 Inspiration → Ob −1) or narrative loss (focus threatened, partner injured, place damaged):

- **Full scene engaged with the focus:** +1 point. No roll required.
- **Focus physically present and uncontested:** automatic +1, no check. (Seeing a loved one safe after battle restores the Inspiration without requiring a scene structure.)
- **Maximum recovery per season:** 2 points per Inspiration per season. Full restoration in one season is not possible — multi-season investment is required to rebuild a deeply spent Inspiration.

**§5.3.3 Focus Destroyed or Permanently Lost**

When an Inspiration's focus is permanently destroyed, captured, or fundamentally changed such that engagement is no longer possible:

1. Inspiration drops to 0 immediately (skipping intermediate recovery).
2. Player may convert to a new Inspiration through a **Grief Scene**: one scene of genuine reckoning with the loss + Spirit check TN 7 Ob 2.
   - **Success:** new Inspiration at old value −1 (minimum 1). New focus must thematically connect to the loss.
   - **Failure:** Inspiration lost entirely. Player may attempt fresh Inspiration acquisition (§5.3.1) next season.

**§5.3.4 Inspiration vs Belief vs Conviction (cross-system distinction)**

These three character-mechanics are distinct and operate at different scales:

| Mechanic | Scale | Function | Persistence |
|---|---|---|---|
| **Conviction** (per player_agency §2) | Worldview / framework | Drives all major decisions; determines Resonant Style; tracked on Piety Track | Lifetime; shifts only through Scar accumulation or major narrative events |
| **Belief** (per character_histories Stage 4 + valoria_ttrpg_complete §10.2 — TODO: full propagation pending) | Active personal stance | Specific stance taken in the moment; may be revised; produces CP awards on revision | Active until completed or revised |
| **Inspiration** (this section) | Emotional/ideological investment | Specific focus that grants +1D / Ob −1 when actively engaged | Persistent until focus lost; modifiable via play |

A Belief like "I will protect Lenneth from the Cardinal's reach" can be **converted** to an Inspiration "Lenneth" upon completion (Belief mechanic produces narrative resolution; Inspiration converts it into ongoing mechanical resource). The Conviction underlying both might be Continuity or Care — a deeper framework that motivated the original Belief.

[EDITORIAL: ED-779 — Inspiration mechanic propagated to canonical derived_stats §5.3. Closes propagation defect: canonical Inspiration spec existed only in deprecated/valoria_ttrpg_complete.md §10.4 (acquisition, recovery, focus loss); active canonical docs (params/core L128 'Resolve = Spirit max Inspiration', fieldwork §2.2 'Inspiration spend → Ob −1') referenced but did not define the underlying mechanism. Now consolidated in §5.3 with Acquisition (mid-campaign two-scene + Spirit check or 4 CP shortcut), Recovery (full-scene engagement +1, focus-present-uncontested +1, season cap 2), Focus loss (immediate drop to 0, optional Grief Scene conversion), Inspiration vs Belief vs Conviction distinction table. Belief mechanic itself flagged for future propagation (§5.3.4 TODO note). Source: 2026-04-25 stress-test 52.]

---

## §6 — Personal Scale: Thread Resources

### 6.1 Thread Fatigue (action economy resource)

| Property | Value |
|----------|-------|
| Formula | Spirit × 5 (threshold) |
| Range | Threshold 5–35 |
| Direction | **Counts up from 0** toward threshold |
| Threshold reached | Thread exhaustion: contact breaks involuntarily, cannot re-establish until rested |
| Recovery | Full rest: resets to 0. Meditation: reduces by Spirit score. |
| Equipment | Thread-conductive artifact: −1 fatigue/round. Einhir proximity: +3/round. Stimulant herbs: threshold +5 temporarily. |

**Per-operation fatigue costs:**

| Operation | Fatigue/Round |
|-----------|--------------|
| Leap (entry cost, one-time) | 3 |
| Passive sensing | 2 |
| Mending | 4 |
| Pulling | 5 |
| Locking | 7 |
| Dissolution | 10 |

**Focus role change:** Focus no longer sets contact duration. Contact Rounds eliminated. Focus sets maximum operations per contact session, preserving current `Focus − 1` cap:

| Focus | Max Operations per Session |
|-------|---------------------------|
| 1 | 0 (experience only) |
| 2 | 1 |
| 3 | 2 |
| 4 | 3 |
| 5+ | 4+ |

Spirit 6 / Focus 2: high threshold (30), sustained contact, but only 1 operation — endurance without skill. Spirit 2 / Focus 6: low threshold (10), exhausts quickly, but 5 operations if endurance allowed — skill without staying power.

**Coherence** (survival resource): unchanged. 10→0 countdown. Not a derived value — a permanent degradation track.

---

## §7 — Unit Scale: TroopCount

| Property | Value |
|----------|-------|
| Formula | Size × block_size (set at muster) |
| Direction | Drains down |
| Depleted at | TroopCount < block_size (Size = 0, unit destroyed) |

**block_size by battle scale** (canonicalizes A.3 narrative table):

| Scale | block_size |
|-------|-----------|
| Skirmish | 10 |
| Company | 100 |
| Battle | 500 |
| Campaign | 1,000 |
| War | 5,000 |

**Size** (1–7) becomes a computed integer: `Size = floor(TroopCount / block_size)`. All combat formulas reference Size unchanged: `Pool = min(Size, Command) + Command`.

**Output scaling:** `effective_damage = floor(successes × (1 + Power) × TroopCount / max_TroopCount)`, where `max_TroopCount = Size_at_muster × block_size`. Ratio is always ≤ 1.0 (capped — reinforcement above muster grants pool dice via Size increase, not output bonus). Damage degrades smoothly as troops are lost. No discontinuities at Size boundaries. A unit at 4,600 / 5,000 deals 92% damage; at 3,000 / 5,000 deals 60% damage. The pool die loss at Size thresholds provides the cliff drama; output scaling provides the continuous degradation between cliffs.

**Health layer (engine-only):** `Total Health = Size_at_muster × H`, where `H = min(Discipline, Command) + DR`. Unchanged. TroopCount = `floor(current_Health × block_size / H)`.

Player sees: **"Heavy Infantry — 4,428 / 5,000 (Size 4)"**

---

## §8 — Faction Scale

| Stat | Derived Value | Derivation | What It Represents |
|------|--------------|------------|-------------------|
| Mandate | **Legitimacy** | Mandate × 20, starting = stat × 20 | Popular/institutional trust capital. 0–140 at Mandate 0–7 — a per-system derived buffer (§3, calibrated to interaction frequency), sized like the sibling faction meters (Reputation Influence×15→0–105, Discipline Stability×10→0–70, Treasury Wealth×100); there is no 0–100 master scale. Mandate's *resolution* impact is the d+σ resolver (+10%/pt, ED-865/874), separate from this buffer. |
| Wealth | **Treasury** | Wealth × 100, starting = stat × 100 | Accumulated economic resources |
| Military | **Levies Available** | Military × 2 (ceiling) | Force projection capacity — not spendable, constrains active unit count |
| Influence | **Reputation** | Influence × 15, starting = stat × 15 | Political capital across factions |
| Stability | **Discipline** | Stability × 10, starting = stat × 10 | Internal faction unity |

### 8.1 Income and Drain

Each derived value has **seasonal income** (automatic at Accounting) and **drains** (from actions, events, ongoing costs).

**Treasury (from Wealth):**
- Seasonal income: Σ(Prosperity of controlled settlements) × 10 gold/season
- Trade Success: +Wealth × 25 gold (one-time)
- Trade Overwhelming: +Wealth × 50 gold
- Haushalt Competence bonus: +Competence × 25 gold/season (Competence 0–3). Cap: Haushalt Competence income cannot exceed Wealth × 50 per season. (ED-663 resolution)
- Campaign Supply (units in hostile territory): −100 gold/season (flat total, regardless of unit count — per mass_battle_v30 §A.14b. Prior per-unit formulation struck 2026-04-29.)
- Siege (attacker): −100 gold/season per active siege
- Muster (Levy): −50 gold
- Muster (Professional): −150 gold
- Muster (Heavy Infantry/Cavalry): −300 gold
- Muster (Artillery): −500 gold
- Unit upkeep (professional units, per season): −25 gold per unit
- Construction (Fortify, infrastructure): −200 gold per action

**When Treasury reaches 0:** Faction cannot Muster, Fortify, or perform gold-cost actions. Professional units begin Discipline degradation (−1/season). At NEXT Accounting where Treasury is still 0: **Wealth −1** (structural economic damage). Only routine path from derived value depletion to stat damage.

**When Wealth stat drops:** Treasury maximum drops (new max = Wealth × 100). Current Treasury retained. Recovery requires Trade actions.

**Legitimacy (from Mandate):**
- Seasonal income: +5 per territory at Accord ≥ 2
- Successful Govern action: +Mandate × 5
- Consensus Delay override (RM): −20
- Emergency authority invocation: −30
- Unpopular Domain Action (drops Accord): −15
- Battle in own territory: −10
- Campaign-scale defeat: Mandate −1 (direct stat damage; large-scale military collapse is a structural event per mass_battle_v30 §A.14)
- Turmoil Mandate check failure: Legitimacy −25 AND Mandate −1

**When Legitimacy reaches 0:** Mandate check at Accounting (Ob 2). Failure: Mandate −1. Accord −1 in all territories.

**Reputation (from Influence):**
- Seasonal income: +5 per diplomatic relationship at Disposition ≥ +2
- Successful Intel/Spy: +Influence × 5
- Successful Diplomacy: +Influence × 10
- Failed diplomatic initiative: −15
- Exposed Niflhel/Altonian operation: −50
- Church Attention triggered: −10
- Casus Belli declared against faction: −20

**When Reputation reaches 0:** Diplomatic and Intel actions +1 Ob. At next Accounting still at 0: Influence −1.

**Discipline (from Stability):**
- Seasonal income: +10 per peaceful season
- Successful Govern: +5
- Battle loss (defending force routed): −15
- Campaign-scale defeat (Campaign/War scale loss): −30 (structural; represents collapse of strategic initiative)
- Accord drops to 0 in any territory: −20
- Faction leader death/succession: −30
- Coup (Löwenritter): −50
- Internal faction schism: −40

**When Discipline reaches 0:** Stability check at Accounting (Ob 1). Failure: Stability −1. Discipline drain at Stability ≤ 2 triggers faction collapse checks.

**Levies Available (from Military):** Ceiling, not spendable. Military × 2 = max active units. If Military drops, ceiling drops — disband excess units.

### 8.2 Stat Damage Only From Structural Failure

**No game event directly modifies a 1–7 stat except through derived value depletion or explicit major events.**

Events that SHOULD still directly modify stats (major structural shifts): faction collapse triggers, coup, CI=100 Mass Seizure, Altonian Occupation, Parliamentary Outlawry, Generational Shift, Turmoil ≥7, Trade/Govern Overwhelming, decisive battle loss (margin ≥2), unit destruction.

The dividing line: "bad quarter" (derived drain) vs "fundamentally weakened" (stat damage).

---

## §9 — Settlement Scale (PENDING)

Architecture supports settlement-level derived values:

| Settlement Stat | Derived Value | Derivation |
|----------------|---------------|-----------:|
| Prosperity | **Local Economy** | Prosperity × 50 |
| Defense | **Garrison Strength** | Defense × 20 + Fort Level × 30 |
| Order | **Public Order** | Order × 20 |

Multipliers and interaction design pending settlement_v30 development. Not canonicalized.

---

## §10 — Cross-Scale Bridges

### 10.1 Disposition and the Bonds Attribute (ED-912 — decoupled)

Disposition is a flat **−5..+5** (ED-912 — supersedes the PP-684 "ceiling = Bonds"). Bonds is structural capability (relational *capacity* — it gates Knot eligibility at Bonds ≥ 5 and sets max Knot count); Disposition is current relational state. The two are **decoupled**: Bonds no longer caps Disposition. (Disposition is therefore NOT a Bonds-derived value — it is its own −5..+5 track per NPC.)

Companion formation (Disposition ≥ +3) requires Bonds ≥ 5. Knot candidacy (Disposition +5) requires Bonds ≥ 5 (achievable at creation).

Cross-reference: fieldwork_v30 §5.1, params_core §Bonds (PP-632/PP-684), companion_specification §2.1.

### 10.2 Army Morale (Mass Combat Derived Composite)
<!-- Cross-reference: mass_battle_v30 Part C §Army Morale references this section for modifier values. -->

**Army Morale = floor(average unit Morale) + Command modifier + Discipline modifier**

| Component | Source | Range |
|-----------|--------|-------|
| Average unit Morale | mean of active units' Morale, floored | 1–7 |
| Command modifier | +1 if Command ≥ 4; −1 if Command ≤ 2 | −1 to +1 |
| Discipline modifier | +1 if faction Discipline ≥ 75% of max; −1 if ≤ 25% | −1 to +1 |

Thresholds: 6+ Resolute, 4–5 Steady, 2–3 Shaken (−1D Morale checks, Command check Ob 2 each Cascade), 1 Wavering (−2D, Withdrawal unless rally Ob 3), 0 Routed (army-level rout, battle lost).

### 10.3 Renown ↔ Derived Value Bridge

When player holds governance position (Standing ≥ 3), faction derived value drains from governance failures apply Renown penalties:

| Event | Derived Value Drain | Renown Consequence |
|-------|--------------------|-------------------|
| Accord drops in governed territory | Discipline −20 | Governor: Renown −1 |
| Treasury reaches 0 while faction officer | Wealth −1 at Accounting | Counselor+: Renown −1 |
| Battle loss in governed territory | Discipline −15 | Governor: Renown −1 |
| Faction Stability reaches 0 | Faction collapses | Member: Renown −2 |

Renown governance penalties cap at −2 per season. Does not decay below 0.

### 10.4 Settlement Combat Defense Feedback

| Combat Outcome | Garrison Strength Effect |
|----------------|------------------------|
| Player wins defense (repels attacker) | Garrison Strength +10 |
| Player wins with Overwhelming | Garrison Strength +20 + Public Order +5 |
| Player loses defense | Garrison Strength −10 |
| Settlement falls during player defense | Garrison Strength → 0, Defense stat check Ob 2 at next Accounting |

Personal combat outcome → settlement derived value → faction derived value income: the most complete personal→faction feedback loop.


### §10.5 Propagation timescales (D-1, audit 2026-05-15)

Outcomes propagate at different speeds depending on which engine layer absorbs them:

| Timescale | Propagating outcome | Owner layer |
|---|---|---|
| Per-action | Wound penalty to next-round Pool (combat); Rattled to next exchange (contest, post-PP-716 −1D); Thread Fatigue accumulation during contact session | Pool |
| Per-scene | Composure/Concentration depletion; Saturation Counter resets between battle turns | Derived values |
| Per-session | Momentum reset; Inspiration scene engagement; wound clearance at session end | Tracks, Momentum |
| Per-season | Disposition shifts → Reputation income; faction stat changes from territory transfers; PT integration | Faction-scale derived |
| Per-year | MS baseline decay (−1/year); CI/IP long-term drift | Peninsula clocks |

**Player expectation note.** Combat outcomes register in real time (next round). Social contest outcomes register at scene granularity (Disposition shifts that influence next-season Reputation income). Thread operation outcomes register at peninsula-clock granularity (MS shifts visible across multiple sessions). The asymmetry is intentional — different fictional registers operate at different timescales. UI/tooltip surfaces should make the active timescale legible to the player.

---

## §11 — Stat Modification Conversion Registry (PP-680)

Audit of all 51 stat ±1/±2 references. Classified as CONVERT (routine → derived drain) or KEEP (structural → direct stat modification).

### Converted to Derived Value (routine fluctuations):

| Original | Converted To | Files Affected |
|----------|-------------|----------------|
| Campaign Supply: Wealth −1/season | Treasury −100/season | mass_battle_v30 |
| Battle Partial: Stability −1 | Discipline −15 | mass_battle_v30, military_layer_v30 |
| Battle loss (routed): Stability check Ob 1 | Discipline −15 | mass_battle_v30 |
| Campaign defeat: Stability check Ob 2 | Discipline −30 | mass_battle_v30 |
| Siege supply: Wealth −1/season | Treasury −100/season | military_layer_v30 |
| Siege failure: Stability −1 | Discipline −15 | military_layer_v30 |
| Siege parley rejected: Stability −1 | Discipline −15 | military_layer_v30 |
| Assert failure: Stability −1 | Discipline −15 | tc_political, victory_v30 |
| Suppress failure: Stability −1 | Discipline −15 | tc_political, victory_v30 |
| Govern failure at Prosperity 0: Stability −1 | Discipline −15 | tc_political |
| Trade Success: Wealth +1 | Treasury +Wealth×25 | tc_political |
| Strain 3–4: Mandate check → Mandate −1 | Legitimacy −25 | tc_political, peninsular_strain |
| Seizure failure: Stability −1 | Discipline −20 | peninsular_strain |
| Proclamation failure: Stability −1 | Discipline −20 | peninsular_strain |
| Cultural Reformation failure: Stability −1 | Discipline −20 | peninsular_strain |
| IP 90 inter-faction Battle: Stability −1 | Discipline −20 | victory_v30 |
| Settlement expansion: Wealth −3 | Treasury −300 | settlement_layer |
| Mine surplus: Wealth +1 | Treasury +50/season | settlement_layer |

### Kept as Direct Stat Modification (structural events):

| Event | Stat Change | Rationale |
|-------|-----------|-----------|
| Battle loss (margin ≥2): Military −1 | KEEP | Decisive loss IS structural military damage |
| Unit destroyed: Military −1 | KEEP | Permanent force loss |
| Campaign defeat: Mandate −1 | KEEP | Major political event |
| Crown Treaty: target Mandate −1 | KEEP | Diplomatic victory — structural |
| Social contest Domain Echo (decisive Memory win): faction Mandate +1 in cited domain | KEEP | Fires only on decisive institutional wins — structural, matching the Crown Treaty precedent (social_contest_v30 §6) |
| Appease (Institutional Mandate): Mandate −1 | KEEP | Deliberate institutional sacrifice |
| Parliamentary Censure/Outlawry: Mandate −1/−2 | KEEP | Formal political action |
| Crown-break: Stability −2, Mandate −1 | KEEP | Treaty betrayal — structural crisis |
| RM Uprising: Church Mandate −2/−1 | KEEP | Loss of territory — structural |
| Dynastic Proclamation success: target Mandate −1 | KEEP | Major political act |
| Trade Overwhelming: Wealth +1 | KEEP | Exceptional success = structural improvement |
| Govern OW in capital: Mandate +1 | KEEP | Exceptional governance = structural |
| Faction collapse triggers | KEEP | Terminal events |
| Coup, Occupation, Generational Shift | KEEP | Campaign-altering events |
| Turmoil ≥7: Mandate check | KEEP | Existential crisis level |

---

## §12 — What Changes from Current Systems

| Current System | Change | Rationale |
|---------------|--------|-----------|
| Vitality = End × 10 (proposed by ED-694) | → reverted to Health = (End+6) × (Max Wounds + 1), MW = floor(End/2)+1 | PP-716 — End × 10 misaligned numerically with Wound Interval × wound-count structure; MW restored; equipment space preserved as flat additive bonus |
| Max Wounds = floor(End/2)+1 | → Eliminated | Wounds computed on the fly: floor(damage / Wound_Interval) |
| Stamina = End + History + 1 − armour | → Stamina = End × 5 [SUPERSEDED by RATIFIED S1: now (3×End)+(2×Spirit)]; History → recovery; armour → drain modifier | Single-attribute base, variable action costs, BB precedent |
| Composure = Cha + 6 | → Composure = Cha × 3 | Removes +6 constant, opens social equipment space |
| Concentration = Focus + Recall | → Concentration = `(3×Focus) + (2×Spirit)` | Focus-driven attention + Spirit; supersedes the Focus×3 interim (2026-06-04, Jordan, ED-902) |
| Contact Rounds = Focus | → Thread Fatigue threshold = Spirit × 5; Focus → max ops per session | Separates duration (Spirit) from skill (Focus), variable costs |
| Size (1–7 stored stat) | → TroopCount = Size × block_size; Size computed | Sub-Size visibility, output scaling, reinforcement decisions |
| A.3 scale table (narrative only) | → block_size canonicalized | Required for TroopCount derivation |

## §13 — What Does NOT Change

- Dice engine: d10, TN 6/7/8, integer pools, integer Ob, degree table
- Combat Pool: (Agi × 2) + History + 3, split offense/defense
- Wound Interval: End + 6
- Wound penalty: −1D per wound (cumulative)
- DR / armor damage reduction tables
- All faction stat → dice pool relationships
- All mass combat formulas (Pool, H, damage per success)
- Coherence (10→0 countdown), Certainty (0–5), Momentum (0–4)
- Social contest: Argue pools, genre/orientation, Persuasion Track, interaction types
- Thread operations: Leap procedure, operation types, co-movement, Ob values
- Disposition Track, Renown Track, Standing
- CI, PT, Accord, MS, IP — already distinct tracked values

---

## §14 — Complete Engine Value Map (Decision-C 4-bucket taxonomy)

Four buckets of state in the engine, distinguished by what they represent and how they move. **Decision-C 2026-05-15:** taxonomy standardized across canon docs; `params/core §Derived Scores` references this section as authoritative.

### §14.1 Derived Values — `Stat × multiplier`, actor/faction state, drains and refills

| Scale | Stat | Derived Value | Multiplier | Direction |
|-------|------|--------------|-----------|-----------|
| Personal | Endurance | **Health** | non-multiplier: `(End+6) × (MW+1)`, MW cap 3 | Drains down |
| Personal | Endurance + Spirit | **Stamina** | `(3×End)+(2×Spirit)` (RATIFIED S1; was ×5) | Drains down |
| Personal | Charisma | **Composure** | ×3 | Drains down |
| | Personal | Focus + Spirit | **Concentration** | `(3×Focus)+(2×Spirit)` — **STRUCK** old `Focus×3` 2026-06-04 (Jordan; ED-902) | Drains down |
| Personal | Spirit | **Thread Fatigue** | ×5 (threshold) | Counts up |
| Personal | Spirit | **Resolve / Inspiration cap** | ×1 (passthrough) | Ceiling |
| Unit | Size | **TroopCount** | ×block_size | Drains down |
| Faction | Legitimacy* | **Legitimacy (derived)** | ×20 | Drains down |
| Faction | Wealth | **Treasury** | ×100 | Drains down |
| Faction | Military | **Levies Available** | ×2 (ceiling) | Ceiling |
| Faction | Influence | **Reputation** | ×15 | Drains down |
| Faction | Stability | **Discipline** | ×10 | Drains down |
| Faction | Intel | **Intelligence Holdings** | (PENDING — derive on use) | (PENDING) |
| Settlement | Prosperity | **Local Economy** | ×50 | PENDING |
| Settlement | Defense | **Garrison Strength** | ×20 + Fort | PENDING |
| Settlement | Order | **Public Order** | ×20 | PENDING |

\* LPS-1 → LPS-2e (Jordan ruling 2026-05-30): Legitimacy and Popular Support are PER-SETTLEMENT values (0–7; settlement_layer §1.8), NOT a faction-level split of Mandate. Faction Mandate is their size-weighted aggregate; the faction Legitimacy meter = Mandate × 20 is the displayed aggregate.

### §14.2 Tracks — bounded counters representing relationship/character/perceptual state

| Track | Range | Direction | Owner | Notes |
|-------|-------|-----------|-------|-------|
| Disposition | −5 to +5 | Oscillating | Relational (per NPC) | Flat; Bonds does NOT cap (ED-912) |
| Piety Track | 0–10 | Oscillating | Per character | Personal religious standing |
| Certainty | 0–5 | Drifts down with Thread exposure | Per character | Cosmological worldview |
| Coherence | 0–10 | Monotonic drain | Per character | Personal rendering legibility — moved from "Derived Scores" per F7 |
| Thread Sensitivity (TS) | 0–N | Grows | Per character | Cumulative perceptual depth |
| Renown | varies | Grows | Per character | Reputation in narrow domain |
| Standing | varies | Oscillating | Per character | Social class indicator |

### §14.3 Clocks — world/scene/campaign progress, mostly monotonic

| Clock | Range | Direction | Scope | Notes |
|-------|-------|-----------|-------|-------|
| Mending Stability (MS) | 0–100 | Decays −1/year baseline | Peninsula | Cosmological state |
| Crown Index (CI) | 0–100 | Bidirectional | Peninsula | Crown legitimacy index |
| Imperial Pressure (IP) | 0–100 | Grows | Peninsula | Altonian intervention pressure |
| Piety Territory (PT) | 0–3+ per territory | Bidirectional | Territory | Church seizure progress |
| Evidence Track | 3/5/8 thresholds | Grows | Per investigation | Investigation progress |
| Saturation Counter | 0–N | Resets per battle turn | Per battle turn | Thread Ob escalator |
| Coup Counter (Löwenritter) | 0–N | Grows | Faction-specific | Coup viability |

### §14.4 Pools — dice quantities computed at action time

| Pool | Formula | Default Range | System |
|------|---------|---------------|--------|
| | Combat Pool | `max(5, History + 6)` — Agility-**independent**, weapon-SKILL (History)-driven; **STRUCK** old `(Agility×2)+History+3` 2026-06-04 (Jordan — combat_engine_v1 canonical, ED-901) | 6–12D | Combat |
| Argue Pool | `(Primary × 2) + History + 3 + style` | 5–18D | Social Contest |
| Thread Pool | `(Spirit × 2) + History + TPS`, min 5 | 5–17D+ | Thread Operations |
| Fieldwork Pool | `(Primary × 2) + History + 3` | 5–17D | Fieldwork |
| Knot Pool | `(Bonds × 2) + 3` | 5–17D | Knot Formation |
| Mass Combat Pool | `min(Size, Command) + Command` | 2–14D | Mass Combat (unit) |
| Faction Domain Pool | bare faction stat | 1–7D | Faction action |

### §14.5 Scale-pool relationship — player-facing note (V-1, audit 2026-05-15)

The same 1–7 attribute number produces dramatically different dice pool sizes across scales. Personal-scale formulas multiply (`×2 + H + 3`) to produce 5–17D pools; faction-scale uses the bare stat (1–7D). A faction Wealth 7 is mechanically not equivalent to a character Cog 7 in terms of dice quantity, even though both occupy the top of the 1–7 range.

**This is intentional.** Faction stats represent collective capacity at a different scale of action — a faction's Wealth roll is the institution committing resources, not a person executing a precise act. The scale-shift is structural, matching scale-of-fiction to scale-of-mechanics. Players reading two character/faction sheets should not expect proportional dice pools from numerically identical stats. Char-sheet UI should surface the active scale so the player can interpret their stats correctly.

[EDITORIAL: ED-694 — Derived stat system v2 (legacy header retained for trace). Architectural redesign for videogame layer. PP-686 v2, PP-716, PP-717 (D1, D3) supersede portions. Decision-C 2026-05-15 standardized this section to 4-bucket taxonomy and added Tracks/Clocks/Pools subsections. Closes F4 (Vitality naming), F5 (Intel + Mandate naming), F7 (Coherence taxonomy), D-3 (Inspiration in map), and V-1 (player-facing scale-pool note).]