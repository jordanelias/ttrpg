# Armour System — Bottom-Up Redesign (Brand New, Responding to the Combat Substrate)

**Status:** Class-C **proposal**, Jordan-vetoable. Per Jordan design grant 2026-05-30 ("design armour bottom-up brand new, validate against historical precedent"). Built **bottom-up** from the canonical armour skeleton + the σ-leverage engine + the weapon-axes-v2 `head` axis, and **top-down** from real arms-and-armour history. **No canon retconned** — every canonical value is *reproduced*; new structure is added only where nothing was decided.

`[READ: references/atoms_pending/.../14__3-4-armour.md — full; derived_stats_v30 §4.2/§14 armour lines; m3 ARMOR_STR_MIN + WEAPON_ARMOR_MOD; weapon_axes_v2 POINT_ARMOR_MOD — this session.]` `[CONFIDENCE: high — calibrated to reproduce the ratified table + skeleton exactly; each axis maps to a documented historical function.]`

---

## §0 — What the canon already fixes (the skeleton I build on, never overwrite)

From the canonical armour atom (`3.4 Armour`) + `derived_stats_v30`:
- **Four tiers:** None / Light / Medium / Heavy.
- **STR-min:** 0 / 2 / 3 / 4 (wearing above your STR penalises).
- **Per-action Stamina drain:** **+0 / +0 / +1 / +2** (armour's cost is fatigue, not base-Stamina loss).
- **Flat Health bonus:** +4 leather / +6 chain / +8 plate (a second, already-canonical armour contribution).
- **Wield constraint:** Stamina cannot drop to ≤ 1 (armour you can't sustain locks you out).
- **Weapon-vs-armour table** (`combat_v30 §5`, W1-ratified + W5 point row): the per-attack damage modifier across the four tiers.
- The atom's **S⚠** flag (Stamina-formula dependency) is **resolved** by ratified S1 (Stamina = 3·End + 2·Spirit).

**The redesign reproduces all of the above exactly.** It adds only the *structure underneath* — why the tiers behave as they do, and two axes the skeleton lacks.

## §1 — The core insight: the weapon-vs-armour table is a projection of a matrix

The canonical table assigns each weapon **damage-class** a row that degrades across tiers:

| (ratified) | none | light | medium | heavy |
|---|---|---|---|---|
| cut (light blade) | 3 | 2 | 1 | 0 |
| cut (heavy blade) | 6 | 4 | 2 | 0 |
| point (light blade) | 3 | 3 | 2 | 1 |
| blunt (light) | 3 | 3 | 2 | 2 |
| blunt (heavy) | 5 | 5 | 4 | 3 |

Read the **columns as armour materials** and the structure is a **(attack-head × material) mitigation matrix** — the historically-central interaction:

- **cut** is stopped progressively: cloth absorbs a little, **mail stops slashes** (rings resist the edge), **plate deflects entirely** (→ +0). Mitigation 0/1/2/3.
- **point** is barely stopped by soft armour (a thrust goes through cloth), **mail can be burst** by a stiff point, **plate stops it on the solid surface but the gaps remain** (→ retains +1). Mitigation 0/0/1/2.
- **blunt** is barely stopped by *anything* — cloth padding absorbs a little, **mail transmits percussion, plate transmits/concusses** (→ stays high). Mitigation ~0/0/1/2.

So the table is not arbitrary per-weapon tuning — it is **one matrix**: `effective_mod = base_vs_none − mitigation[head][material]`. This is the bottom-up explanation, and it is **Smooth** (one calculation unifying weapons and armour) and **Elegant** (the matrix replaces five hand-tuned rows). The redesign *calibrates the matrix to reproduce the ratified rows exactly* — no value changes.

## §2 — The two armour axes (new structure the skeleton lacks)

The four canonical tiers are **presets** in a two-axis space; making the axes explicit adds fidelity without discarding the tiers.

| Axis | Values | Drives |
|---|---|---|
| **material** | none / cloth / mail / plate | the **mitigation matrix** (which attacks it defeats) |
| **coverage** | partial / full | the **gap exposure** (how much of the body the armour actually protects) |

**material** lets a *full mail hauberk* and a *plate breastplate* — both ~"medium" by protection — behave **differently vs a thrust** (mail bursts, plate deflects on the covered zone). The flat tier cannot express that; material can.

**coverage** lets a *breastplate-only* (plate, partial) leave the limbs exposed (any weapon hits bare flesh there) while a *full harness* (plate, full) forces **gap-targeting** (the point's whole niche). Coverage modulates mitigation: `applied_mitigation = matrix × coverage_factor` (full = full matrix; partial ≈ half — the covered zone protected, the rest bare).

**The four canonical tiers as presets** (reproduce the ratified columns exactly):
- **None** = material none.
- **Light** = cloth, full (a gambeson) — the levy's armour / the universal underlayer.
- **Medium** = mail, full (a hauberk over gambeson).
- **Heavy** = plate, full (a full harness over mail over gambeson).

Off-preset combos the new axes unlock: **breastplate** (plate, partial — between medium and heavy, vital-zone only); **mail shirt** (mail, partial — light-medium); **three-quarter harness** (plate, full minus the lower legs). These are now *expressible* — which become game items is a content call.

## §3 — Cost & integration with the engine (the trade-off that makes armour Necessary)

Armour is **damage mitigation purchased with tempo and fatigue** — never a strict upgrade. Each cost reproduces or extends a canonical hook:

- **Fatigue — per-action Stamina drain (CANONICAL, reproduced):** +0/+0/+1/+2 by tier (→ derived by weight from material+coverage). Against ratified Stamina = 3·End + 2·Spirit, heavier armour reaches **Out-of-Breath (0 → −2D)** faster. *This is the real cost*: in a long fight you gas out. (Worked: End 4 → Stamina ~20; +2 drain heavy → effective ~7 actions/round-budget before Out-of-Breath, per derived_stats.)
- **Tempo — σ-leverage penalty (NEW, gap-fill):** armour imposes a modest **initiative/tempo δσ penalty** scaled by weight (plate is mobile but *slower* than unarmoured — the historically-accurate "tiring and a step slow," **not** the Hollywood "can't move"). This is the duel cost: in a finesse race, tempo is everything.
- **Health — flat bonus (CANONICAL, reproduced):** +4/+6/+8 (leather/chain/plate) feeds the wound model's effective Health.
- **STR-min (CANONICAL, reproduced):** 0/2/3/4; wearing above your STR penalises (parallels under-STR weapon wielding).
- **Economic/status (NEW, strategic-layer hook):** a plate harness is a fortune — armour as a **wealth/status gate**, fitting Valoria's political economy. (A strategic-layer cost, not a combat mechanic; flagged for the economy layer.)

**Armour is mitigation, NOT defence (one variable, one role).** Armour makes hits *not matter* (deflect / fail to penetrate); it does **not** make you harder to *hit*. "Harder to hit" is the **skill/parry/shield** channel (the weapon system's off-hand buckler, the σ-leverage defence). Keeping mitigation and evasion as separate channels is NERS-clean.

## §4 — The duel ↔ battlefield split, now emergent (not stipulated)

The validated two-context model falls **out of the armour trade-off** rather than being asserted:
- **Duel (unarmoured by convention):** no mitigation → a **finesse race** where tempo/reach/skill decide. Armour's tempo+fatigue cost is exactly why a duellist *chooses* light/none. Damage magnitude is irrelevant (any clean hit ends it).
- **Battlefield (armoured):** mitigation dominates → **attrition** → damage magnitude governs → **blunt wins** (plate transmits percussion) and **fatigue bites** (heavy armour gasses out in a long melee) and **the point finds gaps** (coverage). Defence is suppressed when engaged (R10).

So whether you armour up *is* the choice of which resolution regime you fight in. This unifies the armour system with the ratified duel/battlefield contexts.

## §5 — NERS + the over-engineering guard

- **Necessary:** the tempo+fatigue ↔ mitigation trade-off makes armour a genuine decision; the material matrix makes weapon-`head` choices matter; coverage makes the point's niche real. Remove any one and a real distinction collapses.
- **Robust:** holds at the extremes (unarmoured finesse duel; full-plate attrition battlefield with fatigue + blunt counter); material/coverage are smooth tiers, fatigue is continuous Stamina — no fragile cliffs.
- **Smooth:** one matrix unifies weapon×armour; costs route through the *existing* Stamina/σ/Health/STR channels; the duel/battlefield split emerges from the same trade-off.
- **Elegant:** the matrix + two axes replace a pile of per-class rows; the four tiers survive as derived presets; the player intuits "heavier = safer but slower & tiring; match your weapon's head to their armour's material; aim for the gaps."

**Over-engineering guard (explicit):** the classic armour over-engineering trap is **per-body-part hit locations** (separate armour on head/torso/arms/legs + a hit-location roll). I deliberately **do not** do that — `coverage` (partial/full) is the elegant abstraction that captures the gap mechanic without a location subsystem. Likewise material is the **dominant layer** with implied underlayers (plate implies mail+gambeson = the harness), not a combinatorial stack of every layer. Two axes, one matrix, the canonical costs. No more.

## §6 — What remains yours (contract)

1. **Ratify the two new mechanics:** the **σ-tempo penalty** for armour (the only genuinely new combat lever) and the **material/coverage axes** (the matrix-reproduction and tier-presets touch no canonical value, but the *structure* is a design addition). The Stamina-drain, Health, STR-min, and weapon-vs-armour values are all reproduced canon — no ratification needed.
2. **Which off-preset armours to instantiate** — breastplate, mail shirt, three-quarter harness are now expressible; which become game items is a content call.
3. **In-world naming** — Valorian armour names, regional styles, and which cultures field what are your creative layer; the above are the historical/mechanical archetypes only.

`[ASSUMPTION: material maps to the canonical tier as none/cloth=light/mail=medium/plate=heavy for the four presets, calibrated to reproduce the ratified weapon-vs-armour columns. Flag if you intend a different tier↔material correspondence.]`
`[GAP: the economic/status cost of armour is a strategic-layer hook, not specified here — it belongs with the faction/economy layer, flagged for that system.]`
