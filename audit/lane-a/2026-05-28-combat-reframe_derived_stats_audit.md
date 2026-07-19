# Derived-Statistics Audit — All Scores, All Scales

**Scope:** every derived score in Valoria (personal + faction/mass), how each is derived from attributes, and whether attribute weight is roughly equivalent across them (Jordan's equivalence principle, 2026-05-28). Extends `attribute_weight_standard.md`, which covered only the dice-pool roll systems.

**Command derivation (the specific ask):** **Command = ⌈(Charisma + Cognition) ÷ 2⌉** for player-character generals; NPC generals get Command assigned directly (1–7) as a narrative stat (Command-P2-02). Confirmed at `mass_battle_v30.md` L246.

---

## 1. Complete derived-score inventory

### Personal scale (`derived_stats_v30.md`)

| Score | Formula | Source attr | Type | Multiplier shape |
|---|---|---|---|---|
| Combat Pool | (Agility × 2) + History + 3 | Agility | roll pool | ×2 + floor |
| Thread Pool | (Spirit × 2) + History + TPS | Spirit | roll pool | ×2 |
| Social Argue Pool | (Primary × 2) + History | Primary | roll pool | ×2 *(no +3)* |
| **Health** | **(End + 6) × (MaxWounds + 1)** | Endurance | resource | **multiplicative + stepped** |
| Max Wounds | min(floor(End/2)+1, 3) | Endurance | capacity tier | floor(/2)+1, cap 3 |
| Wound Interval | End + 6 | Endurance | threshold | +const |
| Stamina | Endurance × 5 | Endurance | resource | ×5 linear |
| Composure | Charisma × 3 | Charisma | resource | ×3 linear |
| Concentration | Focus × 3 | Focus | resource | ×3 linear |
| Thread Fatigue thr. | Spirit × 5 | Spirit | threshold | ×5 linear |
| Disposition ceiling | Bonds | Bonds | cap | ×1 linear |
| Initiative *(proposed)* | Attunement + Weapon Speed | Attunement | order | +const |

### Faction / mass scale (`mass_battle_v30.md`)

| Score | Formula | Source | Type | Shape |
|---|---|---|---|---|
| **Command** | **⌈(Charisma + Cognition) ÷ 2⌉** (player) / direct 1–7 (NPC) | Cha + Cog | leadership | **two-attr average** |
| Power (unit) | floor(Military / 2) + 1 | Military (faction) | quality tier | floor(/2)+1 |
| Effective Combat Pool | min(Size, Command) + Command | Size + Command | roll pool | min+add |
| Morale | general's Command + unit quality | Command (→Cha+Cog) | rout threshold | +const on Command |
| Army Morale | floor(avg unit Morale) + Command mod + Discipline mod | Command, Discipline | aggregate | average + mods |
| Discipline | min(general's …, …) starting; org. integrity | general stat | integrity | min() |
| Size | floor(TroopCount / block_size) | TroopCount *(resource)* | scale | floor(/blocksize) |
| Total Health (army) | Size_at_muster × (min(Discipline,Command) + DR) | Size, Disc, Cmd | resource | product |

---

## 2. Three leverage classes — equivalence assessment

Attribute "weight" means different things for different score types. Three classes, three metrics:

### Class A — Roll pools (metric: σ-leverage per attribute point)

From `attribute_weight_standard.md`, verified: **Combat = Thread = 0.30σ/pt** at typical (exact match); **Social Argue = +17%** (lacks combat's +3 floor → 8D vs 11D baseline). Mass-battle pool leverage on Command analyzed in Class C.

### Class B — Linear resources (metric: proportional gain 1/k per point)

**Verified clean equivalence.** Any ×N resource gains `1/k` proportionally per +1 attribute point at value k — **independent of N**. So Composure (×3), Stamina (×5), Concentration (×3), Thread Fatigue (×5), and Disposition (×1) **all share the identical proportional-leverage curve** (50%/pt at k=2, 33% at k=3, 25% at k=4, …). The linear resources already honor the equivalence principle by construction. ✓

### Class C — The outliers

**Health (Endurance) — the one resource that breaks Class B.** Health = (End+6)×(MaxWounds+1) is multiplicative, not linear ×N, and MaxWounds steps (floor(End/2)+1, capped 3). Verified leverage:

| End→ | ΔHealth | +% | note |
|---|---|---|---|
| 1→2 | +10 | **71%** | MW step (1→2) |
| 2→3 | +3 | 12% | flat |
| 3→4 | +13 | **48%** | MW step (2→3) |
| 4→5 | +4 | 10% | MW capped |
| 5→6 | +4 | 9% | flat |
| 6→7 | +4 | 8% | flat |

Two problems vs the equivalence principle: (1) **non-uniform** — Endurance's survivability leverage spikes at MW steps (End 1→2, 3→4) and flattens after the cap, where the linear resources are smooth; (2) **Endurance is double-loaded** — it drives both Health (multiplicative durability) AND Stamina (×5), so it carries more total weight than single-resource attributes. *Note:* the multiplicative form is deliberate — ED-694 proposed linear `End × 10`, PP-716 reverted to multiplicative. So the steepness is an accepted design choice; the **non-uniformity (MW stepping) is the live concern**, structurally identical to combat's F1 but on the survival axis.

**Command (Cha + Cog) — two-attribute average.** `⌈(Cha+Cog)/2⌉` means +1 Command costs +2 attribute points (one each), or pushes the average. In mass battle's Command-limited regime (Effective Pool = 2·Command), +1 Command = +2 pool, so **~+1 pool per attribute point — half of personal combat's +2/pt**. *But* Cha and Cog also feed personal systems (Cha→Composure/Argue, Cog→Reading), so a general's mental-attribute investment pays in both arenas; mass-battle leverage is **secondary value layered on personal value**, which roughly balances the halving. Structurally reasonable; flag for sim confirmation, not an obvious defect.

---

## 3. Structural parallels (consistency wins, not defects)

- **Power = floor(Military/2)+1 mirrors Max Wounds = floor(Endurance/2)+1.** Faction unit-quality tiers and personal wound-capacity tiers use the *same* "halved-stat stepping" shape (Power uncapped; MW capped at 3). This is a genuine cross-scale consistency — the same design grammar for "capacity tier from a 1–7 stat" at both scales. ✓
- **Morale inherits Command's Cha+Cog dependence** (Morale = Command + quality) — consistent propagation, not a separate derivation.
- **Size is resource-derived** (floor(TroopCount/block_size)), not attribute-derived — correctly so; it's a logistics/economy output, not an attribute-leverage score. Outside the equivalence question by design.

---

## 4. Findings (ranked)

| # | Finding | Severity | Class |
|---|---|---|---|
| **D1** | **Health non-uniformity** — Endurance's survivability leverage spikes at MW steps (71%, 48%) then flattens (8–12%), unlike the smooth linear resources. Survival-axis analogue of combat's F1. | **significant** | C |
| **D2** | **Endurance double-load** — only attribute driving two resources (Health multiplicative + Stamina ×5); carries more weight than single-resource attributes. Partly intentional (PP-716). | moderate | C |
| **D3** | **Social Argue +17%** — lacks combat's +3 floor → modestly higher pool leverage. | minor | A |
| **D4** | **Command half-leverage per point** — two-attr average halves per-point mass-pool leverage; mitigated by Cha/Cog double-duty (secondary value). Likely balanced; confirm in sim. | minor | C |
| — | Linear resources (Composure/Stamina/Concentration/ThreadFatigue/Disposition) mutually equivalent (1/k). | ✓ pass | B |
| — | Power/MW structural parallel; Morale propagation; Size as resource — all consistent. | ✓ pass | — |

---

## 5. The cross-axis limit (what derivation analysis cannot settle)

The equivalence checks above are **same-axis, cross-system** (pool-vs-pool, resource-vs-resource). They cannot settle **cross-axis** equivalence — e.g., does a point of Agility (combat *offense*, via Pool) matter as much as a point of Endurance (combat *survival*, via Health)? That trade depends on how offense and survival actually exchange in a fight, which only **combat simulation** answers (Phase-11+ sims). Derivation analysis bounds the question (we know the leverage *shapes*); it does not close it. `[GAP: cross-axis offense-vs-survival weighting — sim-only]`

---

## 6. Recommendations + decisions

1. **D1 (Health non-uniformity)** — `[DECISION for Jordan]`. Options: (a) accept (the MW-step survivability jumps are dramatic "toughness breakpoints," arguably good game-feel); (b) smooth it — make Health a clean ×N like the other resources (but PP-716 already rejected linear End×10); (c) keep multiplicative but remove the MW-step discontinuity (e.g., Health = (End+6)×(End/2+1) continuous). This is a `derived_stats_v30` change, not a combat-proposal change. The σ-space/uniform-impact discipline applied to *modifiers* (Piece 2) suggests the same instinct applies to *resources* — but it's your call whether survivability breakpoints are a feature.
2. **D2 (Endurance double-load)** — `[DECISION for Jordan]`. Accept (durability-as-king is a deliberate genre choice, PP-716), or move Stamina partly off Endurance (e.g., Stamina = (End+Focus)×k) to spread the load. Low urgency.
3. **D3 (Social +3)** — as before: add +3 to Argue Pool for exact parity, or accept +17%.
4. **D4 (Command)** — likely fine; verify in faction/mass sim that general-attribute investment isn't under- or over-rewarded relative to personal investment.
5. **Adopt the dual standard:** roll pools checked by **σ-leverage (~0.30σ/pt)**, resources checked by **proportional leverage (1/k)**. Any new derived score states which class it's in and is checked against the matching standard.

`[CONFIDENCE: high on all formulas + leverage math (verified in-script, sourced); medium on the D1/D2 severity calls (they hinge on game-feel intent only Jordan + sim can judge)]`
`[READ: designs/scene/derived_stats_v30.md — full derived-score formulas (L62,63,85,495–501); designs/provincial/mass_battle_v30.md — Command L246, Power L817, Size L84/134, Morale L184/392, Discipline L163]`
`[SELF-AUTHORED — bias risk: this audit extends my own attribute-weight standard; I surfaced Health's non-uniformity (D1) as a significant finding even though it's a canonical PP-716 choice I could have waved through, and flagged the cross-axis limit (§5) rather than overclaiming the analysis settles build balance]`
