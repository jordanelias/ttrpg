# R7 — Friendly Fire & Ranged Attacks in Melee
## Module 7 of combat_arch_residual_stress_01

**Date:** 2026-05-09
**Mode:** A (single-mechanic isolation) + D (exhaustive edge cases)
**Source question:** *"Does friendly fire exist when ranged attacks fire into melee zones? Decision: no FF (current canon implicit) / FF on miss / FF as separate roll / FF on stress conditions only."*

**Decision shape:** no FF / FF on miss / FF separate / FF on stress

---

## 1. Verification ledger entries

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| R7-L01 | ranged_distinct_category | Ranged weapons distinct from melee 3-axis matrix | designs/scene/combat_v30.md | §5 (ED-129 resolved) | "### Ranged Weapons (distinct category — ED-129 resolved)" |
| R7-L02 | ranged_weapon_tn_table | LP TN 7, HP TN 6, Sling TN 8 | designs/scene/combat_v30.md | §5 Ranged | "\| LP — Light Piercing (bow) \| 7 \| Min STR 2 \|" |
| R7-L03 | melee_range_zone_renamed | Close zone = Melee range; Far zone = Ranged distance | designs/scene/combat_v30.md | §5 Reach Rules (PP-268) | "**Zone terminology (PP-268):** Close zone renamed **Melee range**; Far zone renamed **Ranged distance** throughout." |
| R7-L04 | ranged_attacker_in_melee_def_tn | Ranged in Close zone defends at Def TN 8 | designs/scene/combat_v30.md | §5 Reach Rules | "Ranged defence at Close zone: a character carrying a ranged weapon may defend at Def TN 8 if forced into Close zone by a melee attacker." |
| R7-L05 | net_hits_min_zero | Net hits = Offence − Defence (minimum 0) | designs/scene/combat_v30.md | §5 Damage Resolution | "Net hits = Offence successes − Defence successes (minimum 0)." |
| R7-L06 | rescue_eligibility_outnumbered | Rescue eligible at outnumbered situations | designs/scene/combat_v30.md | §8 (R6-L06 cross-ref) | "**Eligibility (PP-290):** Rescue may only be declared if the rescued actor is outnumbered at Phase 1 declaration — facing 2+ attackers with no supporting ally" |

**Note:** No canonical entry exists for friendly fire. The canon is silent — friendly fire does not occur at present, but the silence is not an explicit "no" rule. R7 fills this spec gap.

---

## 2. Candidates

| ID | Name | Description |
|---|---|---|
| **C7.1** | No friendly fire (preserve current implicit canon) | Ranged attacks resolve target-only. Adjacent allies in melee zone are not at risk. Player-declared targets are safe from miss-spillover. |
| **C7.2** | FF on miss | Any ranged attack into a melee zone that misses (Defence successes ≥ Offence) rolls a secondary check vs all allies adjacent to the target. |
| **C7.3** | FF as separate roll | After miss, separate hit-on-ally roll (e.g., 1d10, 1+ on a 1 = ally hit; otherwise stray). Independent of the original attack roll. |
| **C7.4** | FF on stress only | FF triggers only when shooter is wounded (≥1 Wound), low Composure (≤3), or in degraded conditions (low light, weather, smoke). Otherwise no FF. |

---

## 3. NERS at full grain

### C7.1 — No FF (preserve current)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Current canon implicit. Targeting is player-declared and resolved against single target. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Net hits min 0 (R7-L05) — miss = no effect. Clean. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Mass-scale (Volley keyword) doesn't track adjacent-ally hits; consistent. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | No cross-system effects. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Stamina, Composure, Wounds unaffected. |
| Horizontal | ⚠ | ✓ | ⚠ | ✓ | ⚠ Horizontal: realism-genre expectation that arrows-into-melee carry risk. ⚠ R: removes a tactical choice (whether to risk ally hit for ranged support). |

**Verdict C7.1:** 22/24 ✓, 2 ⚠ on Horizontal (realism gap, tactical-choice gap). Mechanically sound and minimal.

### C7.2 — FF on miss

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ⚠ | ✓ | ⚠ | Adds resolution step on every ranged miss in melee zone. ⚠ E: per-miss adjudication overhead. |
| Bottom-up | ✓ | ⚠ | ✓ | ⚠ | Net hits min 0 (R7-L05) frequent on TN 7 ranged shots. Many misses → many secondary rolls. |
| Vertical | ⚠ | ⚠ | ⚠ | ⚠ | Mass-scale Volley: would FF on Volley miss propagate? Spec gap. |
| Diagonal | ✓ | ⚠ | ✓ | ✓ | No cross-system surface added. |
| Lateral | ✓ | ⚠ | ✓ | ⚠ | Rescue mechanic (R7-L06): outnumbered ally protected by Rescue — does FF affect Rescuer? Spec gap. |
| Horizontal | ✓ | ⚠ | ✓ | ✓ | Realism preserved; tactical-choice surface added (avoid melee-supporting fire under risk). |

**Verdict C7.2:** N=⚠ on 1, E=⚠ on 5, R=⚠ on 1, S=⚠ on 4. **PASS with bookkeeping cost; per-miss adjudication on every ranged shot in melee.**

### C7.3 — FF as separate roll

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ⚠ | ✓ | ⚠ | Introduces non-canonical d10 mechanic. Combat resolution uses pool dice (TN 7); separate d10 roll is a new dice channel. ⚠ S: contradicts canonical pool-only resolution. |
| Bottom-up | ⚠ | ⚠ | ✓ | ⚠ | Probability spec needed (1-in-10? 2-in-10? Adjustment for crowd density?). |
| Vertical | ⚠ | ⚠ | ⚠ | ⚠ | Mass-scale equivalent unspecified. |
| Diagonal | ✓ | ⚠ | ✓ | ⚠ | Cross-system: separate roll precedent could metastasize (other "stray" mechanics demand similar treatment). |
| Lateral | ✓ | ⚠ | ⚠ | ⚠ | Adds channel that other mechanics don't have. |
| Horizontal | ✓ | ⚠ | ✓ | ⚠ | Realism preserved with cleaner adjudication than C7.2; cost is mechanic proliferation. |

**Verdict C7.3:** N=⚠ on 3, E=⚠ on 6, R=⚠ on 2, S=⚠ on 6. **MARGINAL — non-canonical dice channel.**

### C7.4 — FF on stress only

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ⚠ | ✓ | ⚠ | Stress conditions need explicit enumeration (Wounds, Composure threshold, environmental). Spec work. |
| Bottom-up | ✓ | ⚠ | ✓ | ✓ | Conditional check leverages existing Wound / Composure tracking; integrates cleanly. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Stress-state propagation across scales already canonical. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Stress mechanics couple to Threadwork, Stamina, Composure — already established channels. |
| Lateral | ✓ | ⚠ | ✓ | ✓ | Adds a "stress is dangerous" theme consistent with canonical wounds → Pool penalty (PP-716). |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Realism + tactical-choice + stress-narrative — covers all desired Horizontal value. |

**Verdict C7.4:** 19/24 ✓, 5 ⚠ (mostly on N spec needs and E enumeration). **PASS with spec — leverages existing stress channels; thematically consistent.**

### Cross-candidate summary

| Candidate | N | E | R | S | Verdict |
|---|---|---|---|---|---|
| C7.1 No FF | 6/6 (1⚠) | 6/6 | 5/6 (1⚠) | 6/6 | **PASS — minimal, conservative** |
| C7.2 FF on miss | 5/6 (1⚠) | 1/6 (5⚠) | 5/6 (1⚠) | 2/6 (4⚠) | **PASS but per-miss bookkeeping cost** |
| C7.3 FF separate roll | 3/6 (3⚠) | 0/6 (6⚠) | 4/6 (2⚠) | 0/6 (6⚠) | **MARGINAL — non-canonical dice channel** |
| C7.4 FF on stress | 5/6 (1⚠) | 4/6 (2⚠) | 6/6 | 5/6 (1⚠) | **PASS — narratively rich, mechanically integrable** |

---

## 4. Mode D — Edge cases (compressed)

### Boundary
**EC-D7.B-01 [P3] (C7.2):** What counts as "in melee zone"? Per R7-L03, Melee range = Close zone. Spec needed: ranged shot from Ranged distance INTO Melee range = FF candidate; from Melee range itself = different rules?

### Cascade
**EC-D7.C-01 [P3] (C7.4):** Stress + Wounds compounding: a wounded shooter in low light is multiply-stressed. Spec needs to handle additive vs multiplicative stress conditions.

### Regression
**EC-D7.R-01 [P2] (C7.2):** Players optimize: never use ranged in melee zone. Removes tactical choice rather than adding it.

**EC-D7.R-02 [P3] (C7.4):** Players optimize: keep shooter at full HP / Composure to avoid FF. Encourages defensive positioning.

### Crunch cascade
**EC-D7.CR-01 [P2] (C7.2):** Per-miss check on every ranged shot in melee zone. Common scenario; bookkeeping ramps fast.

### Ambiguity
**EC-D7.A-01 [P1] (C7.4):** "Stress" criteria undefined. Wound count threshold? Composure threshold? Environmental enumeration?

### Incoherence
**EC-D7.I-01 [P2] (C7.3):** d10 channel inconsistent with canonical pool-dice resolution.

### Optimal play
**EC-D7.O-01 [P3] (any):** Players optimize: Rescue mechanic (R7-L06) interaction with FF. Does Rescue protect against FF or only direct attacks?

---

## 5. Decision-shape findings

**Recommendation: C7.4 (FF on stress only) — primary; C7.1 (no FF) — fallback if Jordan determines stress-spec work isn't justified.**

**Rationale:**

1. **C7.1 (no FF)** passes 22/24 NERS but has acknowledged Horizontal gap on realism / tactical-choice surface. Functionally minimal; preserves current canon-silence as canon-default.

2. **C7.4 (FF on stress)** passes 19/24 NERS. Leverages existing canonical channels (Wounds, Composure, environmental modifiers) — no new dice mechanic. Thematically consistent with PP-716 wound-penalty universality (stressed bodies miss; stressed shooters endanger allies). Stress criteria need enumeration (P1 ambiguity per EC-D7.A-01) but the channels themselves are canonical.

3. **C7.2 (FF on miss)** is functionally workable but adds per-miss adjudication overhead on every ranged shot in melee. High-frequency mechanic; bookkeeping cost compounds.

4. **C7.3 (FF separate roll)** introduces a non-canonical d10 dice channel. Functionally tractable but stylistically inconsistent. Reject unless Jordan wants explicit "stray-arrow" precedent.

**Implementation under C7.4 (spec needed):**

- Define stress threshold: ≥1 Wound, OR Composure ≤ 3, OR environmental degradation (low light / weather / smoke as enumerated by GM).
- On stress condition + ranged miss into melee: FF roll vs adjacent allies (one secondary attack roll, TN +1 or +2 for stress severity).
- Adjacent ally Defence allocation as normal.
- Damage on ally hit: half attacker's STR (mitigated impact representing glancing strike).

**Decision-shape statement for Jordan ratification:**

> Friendly fire from ranged attacks into melee occurs only under stress conditions (≥1 Wound, Composure ≤ 3, or GM-declared environmental degradation). On stress + ranged miss into melee zone, a secondary FF check fires against adjacent allies. No FF in baseline conditions. Stress-FF leverages existing canonical wound/Composure/environmental channels rather than introducing a new dice mechanic. The narrative weight of "your shooter shouldn't be shooting now" emerges organically from canonical stress tracking. Open: enumerate the GM-declared environmental degradation list explicitly.

**Jordan-decision items:**

- Pursue C7.4 (stress-FF spec work needed) or default to C7.1 (preserve canon-silence)?
- If C7.4: ratify stress thresholds and environmental enumeration in subsequent PP.

---

## 6. Module status

| Item | Status |
|---|---|
| Canonical sources fetched | ✓ |
| Verification ledger (6 entries; spec-gap noted) | ✓ |
| NERS full-grain analysis | ✓ |
| Mode D edge cases | ✓ |
| Decision-shape finding (C7.4 primary; C7.1 fallback) | ✓ |

**Module 7 status: verified.**
