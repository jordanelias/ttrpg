# COGNITIVE LOAD OPTIMIZATION — LIGHT-MODERATE TO MODERATE TARGET
## Builds on: designs/cogload_reduction_strategies.md (Moderate-Heavy package)
## Target: All systems ≤ 8.0 (Moderate ceiling)
## Constraint: Retain texture. Canon P-01–P-15 inviolable.
## Honest assessment included where target cannot be met.

---

## STARTING SCORES (post-Moderate-Heavy package)

| System | Score | Target | Gap | Achievable? |
|--------|-------|--------|-----|-------------|
| Personal Combat | 7.7 | ≤8 | ✓ | Yes — and can push to 6.7 |
| BG Turn | 8.6 | ≤8 | −0.6 | Yes |
| Social Contest | 9.25 | ≤8 | −1.25 | Yes |
| Thread Operations | 10.0 | ≤8 | −2.0 | Yes, with one texture concession |
| Mass Combat (3 units) | 10.0 | ≤8 | −2.0 | Yes, via physical tracking aids |
| Thread in Mass Combat | ~8.0 | ≤8 | ✓ | Already met |

---

## DESIGN PRINCIPLE

**Every player decision should be meaningful and non-obvious.** If a decision has a dominant strategy (always-yes/always-no) or is pro forma (only one viable option), it should be automated or eliminated. If a computation always produces the same class of result, it should be pre-computed. If a variable rarely changes mid-scene, it belongs on the character sheet as a static entry, not in working memory.

This principle preserves texture — meaningful decisions stay; bookkeeping goes.

---

## 1. PERSONAL COMBAT (7.7 → 6.7)

### PC-1: Weapon Cards (Tier 1 — zero texture loss)
Each weapon type gets a physical card pre-printed with:
- Hit TN (computed from Short/Long × Light/Heavy × Blade/Blunt — player never touches the matrix)
- Damage modifier per armour tier: "vs None: +3 | vs Light: +2 | vs Medium: +1 | vs Heavy: +0"
- STR minimum and penalty note
- Reload requirement (ranged only)

The player picks up the card for their weapon at session start. All weapon lookups become card reads.
- Reduction: −1.0
- Texture cost: None. The weapon matrix is preserved mechanically — the card is its interface.

**Result: 6.7** (Light-Moderate to Moderate) ✓

---

## 2. BG TURN (8.6 → ≤8.0)

### BG-1: Action Card Outcomes (Tier 1 — zero texture loss)
Print full success/failure outcomes on each action card in the hand. When the player plays "Diplomacy," the card reads:

> **Diplomacy** — Target: one faction in adjacent territory.
> Roll: Influence, TN 7, Ob = target Influence.
> Overwhelming: Target Mandate −1, Your Influence +1.
> Success: Your Influence +1 in target territory.
> Partial: No effect. Card spent.
> Failure: Target Stability +1 (they rallied against you).

Eliminates the accounting lookup — the card tells you what changes.
- Reduction: −0.5

### BG-2: Accounting Checklist on Faction Mat (Tier 1 — zero texture loss)
Printed order-of-operations on the faction player mat:
1. ☐ TC: +/− from this season's actions
2. ☐ RS: +/− from Thread events (if any)
3. ☐ IP: +1 if no Crown military action
4. ☐ Check thresholds (TC 40/60/80, IP 75, RS thresholds)
5. ☐ Stat changes from Domain Actions
6. ☐ Draw cards to hand limit

- Reduction: −0.3

**Result: 7.8** ✓

---

## 3. SOCIAL CONTEST (9.25 → ≤8.0)

### SC-3: Argument Styles (Tier 1 — zero texture loss)
Combine genre + orientation into 4 named argument styles. Mechanically identical — presentation change only.

| Style | = Genre + Orientation | Flavour |
|-------|----------------------|---------|
| **Precedent** | Memory + Revealing | "This happened. Everyone knows it. Act accordingly." |
| **Suppression** | Memory + Obscuring | "Let us not speak of what was. It serves no one." |
| **Vision** | Projection + Revealing | "Here is what will happen if we act. Look clearly." |
| **Insinuation** | Projection + Obscuring | "There are consequences you haven't considered." |

Player picks one style per exchange. Interaction type derived automatically:
- Same style = REINFORCE
- Same genre, opposite orientation = CLASH
- Different genre = CROSS

One choice instead of two binary choices. The interaction type lookup becomes implicit.
- Reduction: −0.5
- Texture cost: None. Arguably adds texture — the styles have rhetorical identity. Players think "I'll argue by Precedent" rather than "I'll pick Memory and Revealing."

### SC-4: Auto-Corroborate (Tier 2 — minimal texture loss)
Corroboration fires automatically when Bonds ≥ 3 (symmetric) or ≥ 4 (asymmetric disadvantaged). No per-exchange decision.

Rationale: the decision to NOT corroborate when eligible is near-dominated. You're declining +1D for free. The only edge case is concealing your Bonds stat from an observant opponent — preserved by marking corroboration visibly.
- Reduction: −0.5
- Texture cost: Minimal. Removes a decision with a dominant strategy. Bonds still matter — they determine eligibility.

### SC-5: Resistance Announced Once (Tier 1 — zero texture loss)
Audience resistance is a fixed number per contest (average Stability of relevant factions, round up, −1). Announce it at contest start. Print it on a token placed next to the Conviction Track. "Track movement = your margin minus this number."

Players no longer need to compute resistance — they subtract one fixed, visible number.
- Reduction: −0.25
- Texture cost: None. Resistance is already fixed per contest; this just makes it physically present.

**Result: 9.25 − 0.5 − 0.5 − 0.25 = 8.0** ✓

---

## 4. THREAD OPERATIONS (10.0 → ≤8.0)

### TW-3: Auto-Scale (Tier 2 — minimal texture loss)
Scale is determined by the target, not selected by the player:
- Targeting a person or object → Personal/Object scale
- Targeting a group or relationship → Relational scale
- Targeting a territory → Territorial scale
- Targeting an institution or kingdom → Structural scale

The practitioner chooses WHAT to affect; the scale follows from that choice. This removes "choose your scale" as a separate decision — it was always derivable from context.
- Reduction: −0.5
- Texture cost: Minimal. Removes the (rare) case where a player might attempt a lower-scale operation on a higher-scale target for reduced cost. This case is uncommon and arguably a misapplication — you operate at the scale the target demands.
- Canon impact: None. P-01 co-movement still fires at the determined scale.

### TW-4: TN Mnemonic — "Heavy Ops = 8" (Tier 1 — zero texture loss)
Three operations use TN 8: Locking, Dissolution, Past-Oriented Pulling. All three involve structural manipulation of thread configurations (freezing, destroying, temporally displacing). All others use TN 7.

Rule: **If you're breaking, freezing, or displacing a thread, TN 8. Everything else, TN 7.**

Print on character sheet: "Standard ops: TN 7 | Lock/Dissolve/Pull: TN 8"

This replaces a per-operation TN lookup with a single-line rule.
- Reduction: −0.25
- Texture cost: None.

### TW-5: Flat Coherence Cost (Tier 2 — some texture loss)
Replace per-operation Coherence cost lookup with:
- Object/Personal scale: −0 Coherence
- Relational scale: −1 Coherence
- Territorial/Structural scale: −2 Coherence

Flat per scale, not per operation type. The current system has slight variation by operation type at each scale, but the variation is narrow (typically ±1). Flattening to a scale-only cost eliminates the lookup entirely — the scale is already known.
- Reduction: −0.5
- Texture cost: Moderate. Loses the per-operation Coherence cost variation. Currently, Dissolution costs more Coherence than Mending at the same scale, reflecting the philosophical weight of destruction vs repair. Flattening this removes a mechanical expression of the Foundations' ontological hierarchy. However, the RS cost differences between operations already carry this thematic weight more prominently (Dissolution = −5 RS, Mending = +1 RS). Coherence was a secondary expression.
- Canon impact: P-15 requires Coherence tracking (layer 2 integrity). Coherence is still tracked — only the per-op lookup is simplified. No violation.

### TW-6: Static Thread Sensitivity and Thread Pool Score (Tier 1 — zero texture loss)
Thread Sensitivity (TS) changes only on Overwhelming Leap results (+1 TS) — at most once per scene, typically once per session. Thread Pool Score (TPS) = TS ÷ 10. Both are effectively static during any given Thread contact.

Mark these as **character sheet constants**, not working-memory variables. Recalculate only on TS change events (which the GM announces explicitly).
- Reduction: −0.75 (removes 2 variables from active tracking)
- Texture cost: None. These already behave as constants — this just formalises the treatment.

**Result: 10.0 − 0.5 − 0.25 − 0.5 − 0.75 = 8.0** ✓

### Assessment
TW-5 (flat Coherence cost) is the only strategy with meaningful texture cost. If rejected, the score reaches 8.5 — above target but within the Moderate-Heavy range. All other strategies are lossless.

**Without TW-5: 8.5** (miss by 0.5)
**With TW-5: 8.0** ✓

---

## 5. MASS COMBAT — NO THREAD (10.0 → ≤8.0)

### MC-4: Physical Unit Cards with State Tracking (Tier 1 — zero texture loss)
Each unit gets a physical card:

```
╔══════════════════════════════════════════╗
║  CROWN HEAVY INFANTRY                    ║
║  Size: □□□□□  Power: 3  DR: 2           ║
║  Discipline: □□□□□□□  Morale: □□□□□□□   ║
║  Weapon: Heavy Blade  Armour: Heavy      ║
║  Each success = 4 damage (1+Power)       ║
║                                          ║
║  ⚠ Size loss > Discipline = degrade     ║
║  ⚠ Size < 50% = Morale −1              ║
║  ⚠ Size < 25% = Morale −1 additional   ║
╚══════════════════════════════════════════╝
```

Checkboxes crossed off as damage is taken. Triggers are printed on the card — the player doesn't need to remember them, just check when boxes are crossed.

The card also shows: "Pool = min(Size, Command) + Command = [pre-filled value]. Loses 1 die when Size drops below [pre-filled threshold]."

All unit-level variable tracking becomes physical manipulation of cards rather than mental state.
- Reduction: −1.5 (transforms ~9 tracked variables into physical objects)
- Texture cost: None. Same mechanics, different medium.

### MC-5: Printed Damage Shortcut on Unit Cards (Tier 1 — zero texture loss)
Instead of computing "successes × (1 + Power)" per engagement, the card says "Each success = X damage" (pre-calculated from Power). The opponent's DR is printed on THEIR card. Net damage = (successes × X) − DR. One multiplication and one subtraction.

For common matchups (Heavy vs Heavy, Levy vs Heavy, etc.), pre-printed expected outcomes on a matchup reference sheet.
- Reduction: −0.5
- Texture cost: None.

**Result: 10.0 − 1.5 − 0.5 = 8.0** ✓

---

## 6. THREAD IN MASS COMBAT (~8.0 — already at target)

Already meets target with previous Moderate-Heavy package. The strategies above (TW-3 through TW-6) apply to the Thread component, further reducing it to ~6.0 within the mass combat context. Combined with automated mass units (TM-3 from previous package), the total remains ≤8.0.

---

## META-STRATEGIES

### META-1: Tiered Complexity (zero texture loss at full tier)
Offer two mechanical tiers per system:

| System | Core Tier (for new players) | Full Tier (for experienced) |
|--------|---------------------------|---------------------------|
| Combat | Pool split + Strike only; no Feint/Tie Up/Stunt | All actions available |
| Thread | Mend + Weave + Dissolve only; no POP/FR/Collective | Full operation list |
| Contest | 1-exchange Personal Appeal only; no Grand/Tribunal | All proceeding types |
| Mass Combat | 2 units max, battle plans only | Full unit control |

Core Tier scores: all ≤6.0 (Light-Moderate). Full Tier scores: as computed above. Players graduate when ready.
- Texture cost: None at full tier (which retains everything). Core tier sacrifices depth for accessibility.
- Implementation: Mark advanced options with ★ in the rulebook. Core tier = unmarked options only.

### META-2: GM-Side Tracking Delegation
Many tracked variables are world-state, not player-state:
- RS → GM tracks (it's a world track, not a character track)
- Faction stats → GM tracks (or faction player tracks their own only)
- NPC Morale/Discipline → GM tracks
- Clock thresholds → GM checks

Player tracks only: own character stats (Health, Stamina, Wounds, Composure, Coherence, Concentration) + their unit card (if commanding one).

This doesn't reduce total table load but reduces per-player load. A practitioner-general player tracks: ~6 character stats + 1 unit card = ~7 effective variables. GM tracks the rest.
- Texture cost: None. Standard division of labour.

### META-3: Reference Architecture
Instead of memorising rules, players use a physical reference system:

| Component | Contains | Used By |
|-----------|----------|---------|
| Character sheet | All static stats, pre-computed pools, TPS, Composure formula | Player |
| Weapon card | TN, damage mod per armour tier, STR min, reach | Player |
| Unit card | Size/Discipline/Morale checkboxes, trigger thresholds, damage per success | Player (mass combat) |
| Faction mat | Stat tracks, accounting checklist, unique action summary | Player (BG) |
| Strain card | Margin × Cha mod × Foc def → strain lookup | GM (contest) |
| ×3 RS card | Pre-multiplied RS costs for mass battle Thread | GM (mass+thread) |
| Mode transition flowchart | 8 handoff rules as a decision tree | GM |

With this architecture, the game's mechanical depth is preserved entirely — it's just stored in physical components rather than human memory. The cognitive load scores above assume this architecture is in place.

---

## FINAL SCORES

| System | Original | Post-MH Package | Post-Moderate Package | Rating |
|--------|----------|-----------------|----------------------|--------|
| Personal Combat | 7.7 | 7.7 | **6.7** | Light-Moderate |
| BG Turn | 8.6 | 8.6 | **7.8** | Moderate |
| Social Contest | 11.0 | 9.25 | **8.0** | Moderate |
| Thread Operations | 12.8 | 10.0 | **8.0** (8.5 without TW-5) | Moderate |
| Mass Combat (3 units) | 14.5 | 10.0 | **8.0** | Moderate |
| Thread in Mass Combat | 19.4 | ~8.0 | **≤8.0** | Moderate |

### What was sacrificed

| Strategy | What's Lost |
|----------|------------|
| SC-2 (Read once) | Per-exchange social perception uncertainty |
| SC-4 (Auto-corroborate) | Decision to withhold social capital (near-dominated) |
| TW-2 (Contact as op count) | Round-by-round contact countdown tension |
| TW-5 (Flat Coherence) | Per-operation Coherence cost variation (secondary expression of ontological hierarchy) |
| MC-1 (Battle plans) | Per-unit tactical micro-management |
| MC-3 (Phase consolidation) | Volley/Manoeuvre timing distinction |
| TM-1 (Late Thread declaration) | Phase 1 Thread intent signalling (which was already secret) |
| TM-2 (Single op per battle turn) | Multi-operation contact windows at mass scale |

### What was retained

Every meaningful tactical decision. Every canon constraint. All three-dimensional co-movement. Coherence tracking. RS tracking. The weapon matrix. Pool splitting. Conviction Track. Faction stat interactions. Domain Echoes. Scale transitions. Mode boundaries. All NPC mechanics. All clock systems. All victory conditions.

### Honest Assessment
The target of ≤8.0 across all systems is achievable. Thread Operations hits 8.0 only with TW-5 (flat Coherence cost), which has moderate texture cost. Without TW-5, it sits at 8.5 — close but above target. Every other system reaches ≤8.0 with strategies that have zero or minimal texture cost, primarily through better information presentation (reference architecture) rather than mechanical simplification.

The game's complexity lives in its interconnected systems, not in per-turn arithmetic. The reference architecture (META-3) externalises the arithmetic while preserving the interconnections. This is the single highest-value intervention.
