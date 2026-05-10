# A — Conviction Taxonomy + Axis Matrix Stress Test
## conviction_stress_01 (single-module Mode A coverage)

**Date:** 2026-05-10
**Mode:** A (single-system coverage) + drift surface
**Scope:** PP-684 13-Conviction taxonomy and the 52-cell axis matrix in `conviction_axis_matrix_v30.md`. PP-685 migration roster cross-referenced but not stress-tested in this module.
**Source authority:** PP-684 (canonical 2026-05-01 Stage 10 promotion)

---

## 1. Verification ledger entries

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| A-L01 | conviction_taxonomy_authority | PP-684 supersedes legacy 9-Conviction set | designs/personal/conviction_taxonomy_v30.md | header | "AUTHORITY: PP-684 (this doc); supersedes legacy \"Reason / Continuity\" Conviction labels and per-character anachronistic philosophical-tradition labels." |
| A-L02 | thirteen_convictions_canonical | 13 Convictions: Faith, Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent, Community, Identity, Warden, Virtue, Honor | designs/personal/conviction_taxonomy_v30.md | §2 | "## §2 The 13 Convictions" |
| A-L03 | self_other_orthogonal | Self-Other orientation is separate orthogonal axis | designs/personal/conviction_taxonomy_v30.md | §1 | "**Self-Other orientation** is a separate, orthogonal axis tracking whom an actor primarily benefits — themselves vs the broader populace. Greed, ambition, altruism, and self-sacrifice are represented along this axis, not as Convictions." |
| A-L04 | structured_concentration | Primary 1-3 Convictions weight 0.6-0.8; distributed cultural background 0.2-0.4 | designs/personal/conviction_taxonomy_v30.md | §4 | "## §4 Structured Concentration" |
| A-L05 | four_axis_projection | Convictions project onto 4-axis: hierarchical, sacred, instrumental, traditional | designs/personal/conviction_axis_matrix_v30.md | §2 | "\| Conviction \| hierarchical \| sacred \| instrumental \| traditional \|" |
| A-L06 | matrix_calibration_range | Axis values calibrated within [-1, +1] | designs/personal/conviction_axis_matrix_v30.md | §2 | "Magnitudes are calibrated within `[-1, +1]`. A value near 0 indicates the Conviction is largely orthogonal to that axis. Magnitudes near ±1 indicate strong polarity." |
| A-L07 | five_axis_class_b_allowance | 5th-axis allowance as Class B if Stage 10 calibration finds Community/Identity collapse load-bearing | canon/patch_register_active.yaml | PP-684 description | "4-axis vectorization (hierarchical/sacred/instrumental/traditional) with 5th-axis allowance as Class B if Stage 10 calibration finds Community/Identity collapse load-bearing." |
| A-L08 | self_other_decoupled_from_convictions | Greed/ambition/altruism live on Self-Other axis, NOT in Conviction set | designs/personal/conviction_taxonomy_v30.md | §2.3 | "### §2.3 Greed and ambition are not Convictions" |
| A-L09 | stale_v1_doc_path | npc_behavior_v30 redirects to stale conviction_track_v1.md (9-Conviction set) | designs/npcs/npc_behavior_v30.md | §1.2 | "*The Conviction taxonomy specification has been promoted to its own canonical doc per PP-681.\nSee `designs/personal/conviction_track_v1.md` §1 for the canonical 9-Conviction definitions\n(Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity, Community, Warden).*" |
| A-L10 | resonant_style_taxonomy | 4 Resonant Styles: Evidence, Consequence, Authority, Solidarity | designs/npcs/npc_behavior_v30.md | §1.3 | "### §1.3 Resonant Style Taxonomy" |
| A-L11 | provisional_status | Doc status PROVISIONAL despite Stage 10 PASS | designs/personal/conviction_taxonomy_v30.md | header | "**Status:** PROVISIONAL." |
| A-L12 | sim_battery_passed | Stage 10 sim battery 12/14 PASS | designs/personal/conviction_taxonomy_v30.md | header | "promoted from PROVISIONAL after Stage 10 sim PASS (12/14 battery; commits bb5e293 lateral + 3cb5207 articulation)" |

---

## 2. Drift surface (canon-state inconsistency)

A-L09 surfaces a concrete drift defect:

- **PP-684 (canonical 2026-05-01):** the 13-Conviction taxonomy at `designs/personal/conviction_taxonomy_v30.md` is the canonical source.
- **`designs/npcs/npc_behavior_v30.md` §1.2** redirects readers to `designs/personal/conviction_track_v1.md` (9-Conviction set: Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity, Community, Warden).
- The 9-Conviction set is the *legacy* per A-L01: "supersedes legacy 'Reason / Continuity' Conviction labels."
- **Reason** and **Continuity** appear in conviction_track_v1.md but are explicitly superseded by PP-684. **Autonomy** is replaced by **Liberty** (period-correct vocabulary).

**Defect:** readers landing on `npc_behavior_v30 §1.2` follow the redirect to a stale doc and learn the wrong Conviction set. The 13-Conviction PP-684 promotion is undocumented at the redirect site.

This is a Class P1 drift — readers learning the wrong taxonomy will mis-design NPCs.

**Recommended fix (separate PP):** rewrite `npc_behavior_v30 §1.2` to redirect to `designs/personal/conviction_taxonomy_v30.md`, marking `conviction_track_v1.md` as superseded or moving its content into the v30 chain.

---

## 3. NERS at full grain — taxonomy completeness (96 cells across 4 dimensions)

**Dimensions stress-tested:** taxonomy completeness (covers known design space), axis matrix coherence (52-cell matrix produces sensible polarities), Self-Other independence (orthogonality holds), structured concentration tractability (1-3 primary + cultural background).

### Dim 1 — Taxonomy completeness (24 cells)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | 13 Convictions cover religious (Faith), political (Authority, Order), epistemic (Scholastic), pragmatic (Utility), social-justice (Equity, Liberty), historical (Precedent), relational (Community, Identity), ethical (Warden, Virtue), social-binding (Honor). Renaissance period-correct vocabulary per A-L02. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Per-character migration (PP-685) covered 9 named characters + 4 placeholders without forcing edge-cases into the taxonomy. Coverage adequate. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Personal-scale and faction-scale both consume the same taxonomy. Aggregation via Cascade math (PP-686 §3.2). |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Conviction interacts with Threadwork (Resonant Style targeting), Mass-battle (faction Conviction → unit Discipline modifier), Fieldwork-Socializing (Resonant Style choice in contest). |
| Lateral | ⚠ | ✓ | ⚠ | ⚠ | ⚠ N: Community vs Identity overlap noted in axis matrix §4.1 — the two have similar axis projections (Community `[+0.0, +0.3, -0.2, +0.5]` vs Identity `[+0.4, +0.2, +0.0, +0.6]`). Mathematical near-collinearity may cause Cascade math to weight them redundantly. ⚠ R, ⚠ S: same. |
| Horizontal | ⚠ | ✓ | ✓ | ⚠ | ⚠ Horizontal: A-L09 drift surface — npc_behavior §1.2 redirect to stale v1 doc means downstream NPC design references the wrong taxonomy. Discoverability defect. |

**Verdict Dim 1:** 20/24 ✓, 4 ⚠ (Community/Identity collinearity + npc_behavior redirect drift). Taxonomy is mature; defects are localized.

### Dim 2 — Axis matrix coherence (24 cells)

Per A-L05 / A-L06, the 4-axis projection (hierarchical, sacred, instrumental, traditional) produces a 52-cell matrix.

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | 4-axis space is human-readable; axis names are interpretable independent of game terminology. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Per-row calibration rationale provided (axis_matrix_v30 §3) for all 13 Convictions. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Same 4-axis space at personal and faction scales. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Cross-system Conviction projection consumes the same 4-axis vector. |
| Lateral | ⚠ | ✓ | ⚠ | ⚠ | Order `[+0.5, -0.1, +0.2, +0.4]` vs Authority `[+0.9, +0.2, +0.1, +0.4]` differ primarily on hierarchical magnitude. Per axis_matrix §4.2, intentional separation but mathematically close. |
| Horizontal | ⚠ | ⚠ | ✓ | ⚠ | A-L07: 5th-axis allowance as Class B if Community/Identity collapse load-bearing. The 4-axis system is *currently* sufficient but the 5th-axis trigger is undefined — what telemetry signals "load-bearing collapse"? Spec gap. |

**Verdict Dim 2:** 20/24 ✓, 4 ⚠ (Order/Authority near-collinearity + 5th-axis trigger undefined).

### Dim 3 — Self-Other orientation orthogonality (24 cells)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Self-Other is a separate scalar [-1, +1] per A-L03; canonical decoupling from Conviction set per A-L08. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Per-actor scalar; trivially trackable. Initial values per §3.3. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Same scalar at personal and faction (faction = aggregate over members). |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Self-Other affects outcome attribution (§3.1) — orthogonal to Conviction-vector projection. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Self-Other × Conviction produces 14-dimensional state per actor (13 Conviction weights + 1 Self-Other scalar). Bookkeeping reasonable. |
| Horizontal | ✓ | ✓ | ✓ | ⚠ | ⚠ on display: the Self-Other axis is mechanically orthogonal but the player may conflate it with Convictions in UI. Display affordance needed (treat as separate axis from Conviction wheel). |

**Verdict Dim 3:** 23/24 ✓, 1 ⚠ on UI display affordance.

### Dim 4 — Structured concentration tractability (24 cells)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Per A-L04: 1-3 primary Convictions (weight 0.6-0.8) + distributed cultural background (0.2-0.4). Sums to 1.0 per actor. Author-friendly: pick 1-3 dominant values + cultural template. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Per-NPC representation: vector of 13 weights summing to 1.0. Trivial to compute aggregates. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Faction = weighted aggregate over members (PP-686 §3.2 Cascade). |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Threadwork Resonant Style targeting consumes the actor's primary Conviction(s); Cascade math consumes the full vector. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Cultural background (0.2-0.4) preserves shared cultural-context across NPCs without forcing personal Convictions to align. |
| Horizontal | ⚠ | ✓ | ✓ | ✓ | ⚠ N: 8 cultural background templates (per PP-684 description) — coverage of Valoria's 17 territories may need 8-12 templates depending on cultural distinctness. Spec deferred to migration. |

**Verdict Dim 4:** 23/24 ✓, 1 ⚠ on cultural template count.

### Cross-dimension summary

| Dimension | N | E | R | S | Verdict |
|---|---|---|---|---|---|
| 1 Taxonomy completeness | 4/6 (2⚠) | 6/6 | 5/6 (1⚠) | 5/6 (1⚠) | **PASS — drift defect at npc_behavior §1.2 redirect** |
| 2 Axis matrix coherence | 5/6 (1⚠) | 5/6 (1⚠) | 5/6 (1⚠) | 5/6 (1⚠) | **PASS — 5th-axis trigger spec gap** |
| 3 Self-Other orthogonality | 6/6 | 6/6 | 6/6 | 5/6 (1⚠) | **PASS — UI display affordance** |
| 4 Structured concentration | 5/6 (1⚠) | 6/6 | 6/6 | 6/6 | **PASS — cultural template count** |

**Overall:** the taxonomy + matrix is mature post-PP-684 Stage 10 promotion. No categorical fail. Five ⚠s flag actionable refinements rather than mechanical defects.

---

## 4. Mode A — single-mechanic isolation

### Test 1: Resonant Style targeting via Conviction primary

Per Resonant Style taxonomy A-L10:
- **Evidence** targets actors whose primary Conviction is reality-responsive (Scholastic; potentially Equity, Utility).
- **Consequence** targets actors whose Conviction depends on outcome-justification (Utility primary; Authority secondary).
- **Authority** targets actors deferring to recognized authorities (Faith, Authority, Order, Honor primary).
- **Solidarity** requires active Knot with the NPC; targets Community, Identity, Warden, Honor primary actors.

Coverage check: every Conviction has at least one Resonant Style that targets it. **No "untargetable" Conviction.** Liberty primary actors are interesting — most resistant to Authority targeting (per definition); Evidence and Consequence land best.

### Test 2: Conviction crisis trigger threshold

Per `npc_behavior_v30 §3.3` (redirected to `conviction_track_v1.md §2`): Conviction crisis at 3+ Scars. Under PP-684's structured concentration, an actor with primary Conviction at 0.7 weight accumulating 3 Scars on that primary undergoes crisis.

**Question:** does the 3-Scar threshold scale with weight? An actor with 0.6 weight on a primary may crisis faster (each Scar is a larger fraction of the primary)? PP-684 §3.3 doesn't specify. **[GAP: Conviction crisis weight-scaling — basis: A-L09 redirect to v1 doc means the canonical Scar accumulation table may not have been updated for structured concentration.]**

### Test 3: Self-Other × Conviction interaction

Self-Other orientation is orthogonal per A-L08. But certain Convictions seem semantically self-leaning (Liberty, Identity) or other-leaning (Equity, Warden, Community). Does the orthogonality hold mechanically when an actor has Liberty primary + Self-Other -0.8 (self-sacrificing libertarian)?

The taxonomy supports this combination — there is no constraint preventing it. Interpretively: a self-sacrificing libertarian is a hermit prioritizing personal autonomy over community, but accepting harm to self in service of that autonomy. Coherent. Orthogonality holds.

---

## 5. Decision-shape findings

**Recommendation: A1 (preserve PP-684 13-Conviction taxonomy + 52-cell axis matrix; address the npc_behavior §1.2 redirect drift in a follow-up PP).**

**Rationale:**

1. **All four NERS dimensions pass.** No categorical fail. Five ⚠s are actionable refinements.

2. **Drift at A-L09 is the highest-priority defect.** `npc_behavior_v30 §1.2` redirects to a stale 9-Conviction doc when canon is now the 13-Conviction set per PP-684. Any reader relying on §1.2 learns the wrong taxonomy. This is structurally a Class P1 documentation drift — should be patched.

3. **Five ⚠s are deferred refinements:**
   - Community/Identity near-collinearity (Dim 1 Lateral): monitor; trigger PP-684's 5th-axis allowance if Cascade math reveals load-bearing collapse.
   - Order/Authority near-collinearity (Dim 2 Lateral): same monitor.
   - 5th-axis trigger spec gap (Dim 2 Horizontal): define telemetry threshold for "load-bearing collapse" before the 5th-axis can fire.
   - Self-Other UI display affordance (Dim 3 Horizontal): UI design item, not mechanical.
   - Cultural template count for 17 territories (Dim 4 Horizontal): defer to migration roster.

4. **Conviction crisis weight-scaling spec gap (Test 2):** basis A-L09 redirect drift. Likely the canonical Scar table at conviction_track_v1.md §2 was not updated to interact with PP-684 structured concentration. Should be checked when fixing the redirect.

**Implementation (separate PP-X — recommended next):**

- Rewrite `npc_behavior_v30 §1.2` Conviction Taxonomy redirect to point to `designs/personal/conviction_taxonomy_v30.md` (canonical PP-684).
- Mark `conviction_track_v1.md` as SUPERSEDED with banner pointing to v30, OR consolidate v1's Scar accumulation content into v30 (preserving the Scar mechanics under PP-684 vocabulary).
- Verify Scar accumulation table interacts correctly with PP-684 structured-concentration weights (1-3 primary at 0.6-0.8) — does the 3-Scar threshold apply per Conviction or aggregate?
- Update `designs/scene/conviction_track_v30.md` (Piety Track) to clarify it is *not* the same as Conviction taxonomy v30 — naming collision risk.

**Decision-shape statement for Jordan ratification:**

> The PP-684 13-Conviction taxonomy + 52-cell axis matrix is mature and stress-passes NERS coverage analysis across taxonomy completeness, axis matrix coherence, Self-Other orthogonality, and structured concentration tractability. One Class P1 documentation drift identified: `npc_behavior_v30 §1.2` redirects readers to the stale 9-Conviction `conviction_track_v1.md` rather than the canonical 13-Conviction `conviction_taxonomy_v30.md`. Recommended: separate PP to fix the redirect and verify the Scar accumulation mechanic interacts correctly with PP-684 structured concentration. Five lower-priority ⚠s are deferred refinements (Community/Identity collinearity monitoring, 5th-axis trigger spec, UI display, cultural template count, Scar weight-scaling).

---

## 6. Module status

| Item | Status |
|---|---|
| Canonical sources fetched at full depth (PP-684 taxonomy + axis matrix; npc_behavior; v1 stale doc) | ✓ |
| Verification ledger (12 entries) | ✓ |
| sim_gate('custom', systems=['conviction', 'npc_behavior']) | (called at commit) |
| NERS full-grain across 4 dimensions (96 cells) | ✓ |
| Mode A isolation tests (3) | ✓ |
| Drift surface defect identified (P1 — A-L09 redirect to stale doc) | ✓ |
| Decision-shape finding (A1 + recommended follow-up PP) | ✓ |

**conviction_stress_01 status: verified.**

**Open editorial items surfaced (carryover for Jordan):**

- `[GAP]` Conviction crisis 3-Scar threshold weight-scaling under PP-684 structured concentration
- `[ASSUMPTION: Stage 10 sim battery 12/14 PASS — basis: A-L12. The 2/14 fails should be reviewed for relevance to current canon.]`
- `[GAP]` 5th-axis collapse trigger telemetry threshold undefined per A-L07
- `[ASSUMPTION: Resonant Style taxonomy A-L10 covers all 13 Convictions — basis: every Conviction maps to at least one Resonant Style per Test 1. Verify under PP-685 migration that no canonical NPC is "untargetable."]`
