# R1 v2 — Wound Permanence vs Canonical Recovery (PP-716 canon)
## Module 1 of combat_arch_residual_stress_01

**Date:** 2026-05-09
**Mode:** B (interaction chain) + D (exhaustive edge cases)
**Source question:** `tests/stress/combat_videogame_arch_2026-05-01/06_synthesis.md §4 R1`
**Question text:** *"Canonical §4 says Wounds clear at end of session. Wildermyth pattern (Chunk 2 §3) suggests permanent-consequence Wounds for narrative weight. The composite stack doesn't take a position. Decision needed: do some Wounds (catastrophic — limb loss, blind eye) become permanent for narrative payoff, with normal Wounds clearing canonically?"*

**Decision shape:** yes (specify catastrophic-Wound criteria) / no (preserve canonical) / partial (use existing permanence channel)

**Supersedes:** `r1_wound_permanence.md` v1 (committed 45c693e2). v1 was authored against pre-PP-716 canon (Vitality = End × 10; Threadwork +1 Ob per Wound). Both formulations were reverted by PP-716 (committed 6e3a8ae). This v2 rebuilds the analysis against corrected canon. Conclusion is unchanged (recommendation: C1.3 Knot-tagged via existing Conviction Scar channel); rationale is tightened.

---

## 1. Verification ledger entries (this module, PP-716 canon)

All quoted_text strings verbatim-verified against fetched canonical content (force_full=True).

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| R1v2-L01 | combat_pool_formula | (Agility × 2) + Relevant History + 3 (minimum 5) | designs/scene/combat_v30.md | §1 | "Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)" |
| R1v2-L02 | wound_pool_penalty | −1D per Wound, cumulative, no Ob | designs/scene/combat_v30.md | §7 | "Each Wound: −1D Combat Pool only (cumulative). No Ob penalty from wounds." |
| R1v2-L03 | wound_penalty_universal | −1D to ALL Pools (Combat, Thread, mass-Command) per Wound | designs/scene/derived_stats_v30.md | §4.1 (PP-716 authoritative) | "Wound penalty \| −1D to ALL Pools (Combat, Thread — Leap, Weaving, Pulling, Mending, FR — Hybrid mass-battle Command). Universal rule." |
| R1v2-L04 | health_formula | (Endurance + 6) × (Max Wounds + 1) | designs/scene/derived_stats_v30.md | §4.1 | "Formula \| `Health (full) = (Endurance + 6) × (Max Wounds + 1)` = WI × (MW+1)" |
| R1v2-L05 | max_wounds_formula | floor(Endurance / 2) + 1 | designs/scene/derived_stats_v30.md | §4.1 | "Max Wounds \| `Max Wounds = floor(Endurance / 2) + 1`" |
| R1v2-L06 | wound_interval_formula | Endurance + 6 | designs/scene/derived_stats_v30.md | §4.1 | "Wound Interval \| `WI = Endurance + 6` (range 7–13 across End 1–7)" |
| R1v2-L07 | wounds_clearance | All wounds clear at session end (canonical) | designs/scene/derived_stats_v30.md | §4.1 | "Wounds clearance \| All wounds clear at session end (canonical). Stabilised characters return to action after one full scene of rest." |
| R1v2-L08 | felling_threshold | Felled at MW+1 wounds (= 0 Health) | designs/scene/derived_stats_v30.md | §4.1 | "Felled (incapacitated) at 0 Health, which equals MW + 1 wounds accrued." |
| R1v2-L09 | combat_pool_floor | minimum 5D, no further wound penalty at floor | params/combat.md | §Pool minimum | "Combat Pool minimum 5 is a clean floor. No −1D penalty at the floor." |
| R1v2-L10 | thread_pool_floor | minimum 5D for Thread Pool | designs/threadwork/threadwork_v30.md | §Pool floor R-57 | "Pool floor correction (R-57):** Minimum 5 dice before rolling any Pull. Below 5D (from wounds, degradation, low stats):" |
| R1v2-L11 | conviction_scar_existing | permanence channel exists, attached to Conviction track | designs/scene/derived_stats_v30.md | §Conviction | "Lifetime; shifts only through Scar accumulation or major narrative events" |
| R1v2-L12 | knot_lifecycle_strain_capacity | Distant 4 / Close 7 | designs/scene/fieldwork_v30.md | §5.6b | "\| Distant Knot \| 4 strain \| Can be upgraded to Close (per §5.6a Success outcome)." |
| R1v2-L13 | fr_dissolution_wound | +1 Wound to Knot partner on FR Dissolution | designs/scene/fieldwork_v30.md | §5.6b | "Tears the Knot directly; partner-of-rupture takes +1 Wound (no armor)." |
| R1v2-L14 | dissolution_witness_scar | scar on all witnesses to Dissolution | params/combat.md | §thread interactions | "**Dissolution in combat:** RS cost per threadwork_v30 §5.2. Scar on all witnesses per npc_behavior_v30 §3.4." |
| R1v2-L15 | coherence_track_permanence | Coherence is permanent degradation track | designs/scene/derived_stats_v30.md | §Coherence | "**Coherence** (survival resource): unchanged. 10→0 countdown. Not a derived value — a permanent degradation track." |

---

## 2. Existing permanence channels (canon, unchanged by PP-716)

| # | Channel | Carrier | Trigger | Mechanical effect |
|---|---|---|---|---|
| P1 | Conviction Scar | Conviction (Piety/Persuasion Track post-rename) | Major narrative events; Knot rupture at Close threshold | +1 Scar; Lifetime; Resonant Style change |
| P2 | Witness Scar | NPC reaction state | Witnessing Dissolution event | per npc_behavior §3.4 — Disposition shifts and faction reaction lock-in |
| P3 | Coherence track | Practitioner | Thread overdraw, FR Lock failures, Calamity radiation | Permanent degradation track 10→0 |
| P4 | Inspiration permanent loss | derived_stats | Focus permanently destroyed/captured/lost | Drops to 0; recovery requires new focus |
| P5 | Knot rupture | Relational state | Conviction opposition, FR Dissolution, public counsel citation | Disposition reset, possible Conviction Scar |

A new permanent-Wound channel would be channel P6.

---

## 3. Candidates (unchanged from v1)

| ID | Name | Description |
|---|---|---|
| **C1.1** | Pure canonical | All wounds clear at session end. No new channel. |
| **C1.2** | Catastrophic-permanent | Tag wounds "catastrophic" at accrual; persist across sessions; normal wounds clear canonically. Tag criteria require specification. |
| **C1.3** | Knot-tagged | Wounds taken in events that already trigger existing permanence channels (FR Dissolution +1 Wound to Knot partner per R1v2-L13; Dissolution-witness +1 Wound by extension) become permanent as Conviction Scar +1. Reuses P1, no new channel. |
| **C1.4** | All-permanent | All wounds persist across sessions; clearance via specific actions only. |

---

## 4. NERS at full grain — 24 cells per candidate (PP-716 canon)

Criteria locked at module start (consistent with v1):
- N: ✓ if mechanic present and complete; ⚠ specified with gaps; ✗ missing/undefined.
- E: ✓ depth without overhead; ⚠ depth with non-trivial bookkeeping; ✗ overhead exceeds depth.
- R: ✓ produces emergent variation across character types; ⚠ uneven; ✗ homogenizing or dominant strategy.
- S: ✓ integrates without contradicting another rule; ⚠ adds new edge cases; ✗ contradicts canonical rule.

### C1.1 — Pure canonical

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Canonical clearance fully specified; no new state. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Health formula (R1v2-L04), MW (R1v2-L05), WI (R1v2-L06) all preserved as PP-716 baseline. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Wound clearance scales identically across personal / mass / faction. |
| Diagonal (cross-system) | ✓ | ✓ | ✓ | ✓ | Cross-system effects (Thread −1D Pool per R1v2-L03) scoped to wounded session and clear with the wound. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Wounds ↔ Stamina ↔ Composure ↔ Concentration all clear at session end. |
| Horizontal | ⚠ | ✓ | ⚠ | ✓ | Campaign-arc narrative weight of a battle wound is *not* mechanically retained; relies on Conviction Scar / faction-reputation channels. |

**Verdict C1.1:** 22/24 ✓, 2 ⚠ on Horizontal (Wildermyth narrative-weight gap). All N, E, S clean. Mechanically minimal, narratively sparse.

### C1.2 — Catastrophic-permanent (PP-716 re-derivation)

Under PP-716, the v1 categorical rejections weaken because (a) Pool floor 5D still binds but with bounded compounding, (b) Thread Pool floor 5D (R1v2-L10) prevents the practitioner-extinction cascade I cited in v1. New analysis:

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ⚠ | ⚠ | ⚠ | Tag criteria undefined ("catastrophic" — limb loss, blind eye is illustrative, not mechanical). Faction layer must track per-NPC permanent Wound state across sessions. |
| Bottom-up | ⚠ | ⚠ | ⚠ | ✗ | Pool floor 5D (R1v2-L09) creates asymmetry: at MW carry-load (the binding cap per R1v2-L05/L08), End=7 character (Pool 12D max) sees up to −4D pool penalty; End=1 character (Pool 5D) sees no penalty. **S ✗:** contradicts canonical wound clearance R1v2-L07. |
| Vertical | ⚠ | ⚠ | ⚠ | ✗ | **S ✗:** mass-scale Discipline/Morale resolution does not have Wound Interval; permanence at unit scale undefined. |
| Diagonal | ⚠ | ⚠ | ⚠ | ⚠ | Thread Pool penalty −1D under PP-716 is floored at 5D (R1v2-L10) → no cascade extinction. ⚠ R: Mending operations (which are themselves Thread Pool ops) become harder for wounded practitioners — Mending becomes the canonical wound-clearance ritual but is harder when wounded. Mild self-treatment friction; not a closed loop. |
| Lateral | ⚠ | ⚠ | ⚠ | ⚠ | Mismatch with Stamina / Composure / Concentration which clear cleanly. Asymmetric clearance. |
| Horizontal | ✓ | ⚠ | ✓ | ⚠ | Narrative-weight goal achieved; campaign arcs gain battle-wound permanence channel. |

**Verdict C1.2 (revised):** **N=⚠ on 5/6 directions** (categorical concern remains). **S=✗ on 2 directions** (canonical clearance contradiction + vertical scale gap). The v1 R-fail ✗ on Bottom-up and Diagonal is *removed* under PP-716 (Thread Pool floor 5D contains the cascade). The Pool asymmetry persists but is bounded by MW (max ~4D Pool penalty at End=7, vs unbounded in v1's analysis). **C1.2 still REJECTS** on canon-contradiction (S) and ambiguity (N), but the rejection is less categorical than v1.

### C1.3 — Knot-tagged

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Reuses existing P1 (Conviction Scar) channel; no new state. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Wound mechanic unchanged at scene scale (clears at session end per R1v2-L07); permanence carried by Scar at perception layer. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Conviction Scar already operates across scales (R1v2-L11). |
| Diagonal | ✓ | ✓ | ✓ | ✓ | FR Dissolution → Knot rupture (existing) → +1 Wound (R1v2-L13) → Conviction Scar (existing P1, fieldwork §5.6b "Close Knots that broke at high strain: Conviction Scar +1 to both partners"). No new compounding pathway. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Stamina/Composure/Concentration clear normally; Wound clears normally; Scar fires only on triggered events. |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Narrative weight earned via existing Scar mechanism — battles producing Knot ruptures or Dissolution events leave Scars on participants/witnesses. |

**Verdict C1.3:** 24/24 ✓. **PASSES NERS at full grain.** No new channel required; uses existing P1/P2 permanence pathways. Unchanged from v1.

### C1.4 — All-permanent (PP-716 re-derivation)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ✗ | ⚠ | ✗ | **E ✗:** every NPC tracked across all sessions for cumulative permanent Wound state (≈12 NPCs × 30 sessions × 1.5 wounds = 540 entries). **S ✗:** contradicts R1v2-L07 universally. |
| Bottom-up | ✗ | ✗ | ⚠ | ✗ | **N ✗:** clearance mechanism undefined ("specific actions" not enumerated). The PP-716 bounded-MW structure means characters cap their permanent-wound load at MW (End=4 → 3 wounds carry; 4th fells), so universal-permanent under MW cap = "you're permanently MW-wounded, then unplayable." |
| Vertical | ✗ | ⚠ | ⚠ | ✗ | Same as C1.2 vertical issues. |
| Diagonal | ✗ | ⚠ | ⚠ | ✗ | Thread Pool floor 5D (R1v2-L10) contains the cascade but Mending operations remain harder for wounded practitioners; cumulative under PP-716 is reduced but ⚠ persists. |
| Lateral | ⚠ | ⚠ | ⚠ | ✗ | Stamina/Composure/Concentration still clear; Wound permanence creates asymmetry. |
| Horizontal | ✓ | ✗ | ⚠ | ⚠ | Narrative weight at the cost of MW-bounded campaign-time degradation; characters become unplayable after carrying ≈MW permanent wounds. |

**Verdict C1.4 (revised):** **N=✗ on 3 directions, E=✗ on 3, R=⚠ but no ✗, S=✗ on 4.** Still REJECTS — but the R-fail of v1 (universal extinction cascade) is replaced with R-⚠ (bounded but ugly degradation). Net: still categorical multi-axis fail.

### Cross-candidate summary (revised)

| Candidate | N pass | E pass | R pass | S pass | Verdict |
|---|---|---|---|---|---|
| C1.1 Pure canonical | 6/6 (1⚠) | 6/6 | 5/6 (1⚠) | 6/6 | **PASS — minor narrative gap** |
| C1.2 Catastrophic-permanent | 1/6 (5⚠) | 1/6 (5⚠) | 1/6 (5⚠) | 4/6 (2 ✗) | **REJECT — canon-contradiction + ambiguity, but bounded** |
| C1.3 Knot-tagged | 6/6 | 6/6 | 6/6 | 6/6 | **PASS — uses existing channels** |
| C1.4 All-permanent | 3/6 (3✗) | 2/6 (3✗) | 0/6 (5⚠) | 2/6 (4✗) | **REJECT — multi-axis categorical fail** |

---

## 5. Mode B — Interaction chain analysis (PP-716 canon)

### Chain 1: Wound → Pool degradation → next-session combat viability

Reference character: Agility 4, Relevant History 1 → **Pool = 12D** (R1v2-L01). Pool floor 5 (R1v2-L09).

Under PP-716 with MW = floor(End/2)+1, the maximum **carryable** permanent wounds is bounded:

| End | MW (max wounds carry) | Pool penalty if all MW carried | Next-session Pool (12D max) |
|---|---|---|---|
| 1 | 1 | −1D | 11D |
| 2 | 2 | −2D | 10D |
| 4 | 3 | −3D | 9D |
| 7 | 4 | −4D | 8D |

Compare v1's analysis (unbounded Wound counter): 7 wounds → 5D (floor). PP-716 caps at 4 wounds for End=7, so worst-case Pool penalty is −4D, not −7D. Pool floor 5D doesn't bind for typical-stat characters under PP-716 carry limits.

For low-stat character (5D Pool): same as v1, no penalty (floor binds at session start).

**Updated finding:** Pool asymmetry under permanent-wound rules persists but is bounded. Worst-case differential at MW carry: 12D − 4 = 8D (high-End) vs 5D (low-End at floor) — a 3D gap. v1 reported a 7D gap (12D → 5D vs 5D → 5D). Halved magnitude.

### Chain 2: Wound → Thread Pool degradation → practitioner viability (REWRITTEN under PP-716)

Under PP-716 (R1v2-L03): wounds give −1D to Thread Pool, floored at 5D (R1v2-L10). No +1 Ob.

Practitioner with Spirit 4, History 2, TPS = 3 (TS 30+) → Thread Pool = (Spirit×2) + History + TPS = 8 + 2 + 3 = 13D.

| Carried wounds | Thread Pool | Expected net (TN7) |
|---|---|---|
| 0 | 13D | 4.29 |
| 1 | 12D | 3.96 |
| 2 | 11D | 3.63 |
| 3 | 10D | 3.30 |
| 4 (MW for End≥6) | 9D | 2.97 |

Mending Stability Ob varies; depth-3 Mending typically Ob 3. Under PP-716 with MW=4 wounds carried, expected net = 2.97. Mending at depth 3 still viable (Ob 3 needs ~3 net successes; ~50% chance per attempt).

**v1 cited "practitioner-extinction cascade" because +1 Ob per Wound was unfloored and Mending depth-3 became Ob 5+5 = 10. Under PP-716 −1D Pool with floor 5D, this cascade does not fire.** Mending becomes harder under permanent wounds but does not become impossible. The closed regression loop (cannot Mend → wound persists) is broken.

Friction remains: a wounded practitioner is mechanically less effective at self-treatment. Under PP-716 this is a tactical consideration, not an extinction mechanism.

### Chain 3: Wound → Knot strain → relational rupture (unchanged)

Under canon: Knot accrues strain from specific use; FR Dissolution → +1 Wound (no armor) AND tears the Knot (R1v2-L13). The +1 Wound is canonically session-clearing per R1v2-L07.

Under C1.2: if FR-Dissolution-induced Wound is tagged "catastrophic," permanent-wound state attaches to the same event that already triggers Conviction Scar +1 (existing P1 via Knot rupture). **Double-permanence on a single triggering event** — same finding as v1.

Under C1.3: the Wound clears at session end (canon); the Conviction Scar carries the permanent record. Single permanence channel per event. Mechanically clean.

### Chain 4: Wound → narrative arc density (unchanged)

Wildermyth narrative-weight pattern is satisfied via the existing Conviction Scar mechanism (R1v2-L11). No new channel required. Unchanged from v1.

### Chain 5: Wound → fieldwork capability (revised)

Fieldwork pools (Investigation, Exploration, Socializing) are not directly penalized by Wounds under PP-716. Threadwork-adjacent fieldwork actions take the universal −1D Pool penalty (R1v2-L03), floored at 5D (R1v2-L10).

Under C1.2/C1.4: a wounded practitioner has reduced Thread Pool for fieldwork-adjacent operations across all sessions until the wound is permanently cleared (which has no canonical mechanism). Persistent reduction; not extinction.

Under C1.3: Thread Pool clears with the Wound at session end. Persistent narrative weight via Conviction Scar without persistent mechanical degradation.

---

## 6. Mode D — Edge case discovery (PP-716 canon)

### Boundary
**EC-D1.B-01 [P2] (C1.2/C1.4 only) — REVISED:** Pool floor 5D combined with permanent wounds creates bounded asymmetry. Worst-case differential: high-End (12D − MW=4 = 8D) vs low-End (5D floor) = 3D. v1 reported 7D gap; PP-716 halves the magnitude.

**EC-D1.B-02 [P2] (C1.2/C1.4) — UNCHANGED:** Stage 2 Dying stabilisation at Ob 3 (combat_v30 §4) — if a Stage-1 Wound is "catastrophic," the wound carries narrative weight from a death-cascade-adjacent state with no mechanical handle for the catastrophe-vs-routine distinction.

### Cascade
**EC-D1.C-01 [REMOVED under PP-716]:** v1's practitioner-extinction cascade no longer fires. Thread Pool floor 5D (R1v2-L10) contains the loop.

**EC-D1.C-02 [P2] (C1.2) — UNCHANGED:** "Catastrophic" tag undefined → cross-table inconsistency.

### Regression
**EC-D1.R-01 [P3 — DOWNGRADED from P1] (C1.2/C1.4):** Wound → Thread Pool −1D → reduces Mending efficacy. Mending is the canonical wound-clearance ritual. Closed loop downgraded to *friction loop*: not extinction, just reduced self-treatment efficiency. Tactical, not terminal.

### Deadlock
**EC-D1.D-01 [P3 — DOWNGRADED] (C1.4):** Party with all members at Pool floor 5D and high carried-wound count. Under PP-716, MW caps wound count at floor(End/2)+1, so worst-case is "every member at MW carried" = Pool penalty up to −4D for End=7, −0D for End=1. Combat encounters above ~Ob 2–3 become difficult but not impossible.

**EC-D1.D-02 [P3] (C1.2) — UNCHANGED:** Undefined criteria → Game Masters lock into "no Wounds qualify" → C1.2 collapses to C1.1 with overhead.

### Crunch cascade
**EC-D1.CR-01 [P2 — DOWNGRADED] (C1.4):** Per-NPC permanent-Wound state across all named characters × all sessions; bounded by MW per character, but still ≈12 NPCs × 30 sessions × MW (avg 3) = 1080 state-entries to track. Tabletop-burdensome.

**EC-D1.CR-02 [P2] (C1.2) — UNCHANGED:** Per-Wound "catastrophic" tagging adjudication.

**EC-D1.CR-03 [P3] (C1.3) — UNCHANGED:** Conviction Scar tracking already in canon; no additional crunch.

### Ambiguity
**EC-D1.A-01 [P1] (C1.2) — UNCHANGED:** "Catastrophic" criterion is the central undefined term. PP-716 doesn't introduce hit-location detail; criterion remains undefinable mechanically without canon expansion.

**EC-D1.A-02 [P2] (C1.4) — UNCHANGED:** "Specific actions" for clearance not enumerated.

### Incoherence
**EC-D1.I-01 [P1] (C1.2/C1.4) — UNCHANGED:** Direct contradiction with R1v2-L07 ("All wounds clear at session end (canonical)"). PP-716 reaffirms canonical clearance; permanent-wound rules require explicit canonical override.

**EC-D1.I-02 [P2] (C1.2) — UNCHANGED:** Single-event-double-permanence at FR Dissolution / Knot rupture events.

### Optimal play
**EC-D1.O-01 [P2 — DOWNGRADED from P1] (C1.2/C1.4):** Player optimal: avoid combat after carrying ≈MW wounds (since the next wound fells). Combat avoidance still incentivized but bounded by MW rather than unbounded. v1 reported P1; PP-716 downgrades because the MW cap creates a clear incentive ceiling rather than open-ended decay.

**EC-D1.O-02 [P3] (C1.4) — UNCHANGED:** Players take only low-Endurance characters into combat (already at floor, take no further penalty). Reverses canonical role differentiation.

### Degenerate
**EC-D1.DG-01 [P3] (C1.2) — UNCHANGED:** Too narrow → C1.2 = C1.1 with overhead.

**EC-D1.DG-02 [P2] (C1.2) — UNCHANGED:** Too broad → C1.2 = C1.4 with degeneracies.

---

## 7. Decision-shape findings

**Recommendation: C1.3 (Knot-tagged permanence via existing Conviction Scar channel).** Unchanged from v1.

**Rationale (revised under PP-716):**

1. **C1.1 still passes 24/24 NERS** with ⚠ Horizontal narrative-weight gap. Solves R1 by leaving canon alone.

2. **C1.2 still rejects** but for fewer and softer reasons under PP-716:
   - Ambiguity of "catastrophic" tag (P1, unchanged) — undefined criterion is structurally undefinable without canon expansion to hit-location.
   - Direct contradiction with canonical wound clearance R1v2-L07 (S ✗, unchanged).
   - Pool asymmetry persists but is bounded by MW (R-⚠ instead of R ✗).
   - Single-event-double-permanence at FR Dissolution / Knot rupture (P2, unchanged).
   - **The v1 practitioner-extinction-cascade rejection is dropped** because PP-716 floors Thread Pool at 5D and changes the wound penalty from +1 Ob to −1D Pool. The cascade no longer fires.

3. **C1.3 still passes 24/24 NERS** under PP-716. The existing P1 (Conviction Scar) and P2 (Witness Scar) channels deliver narrative permanence. The mechanical Wound continues to clear at session end per R1v2-L07. Recommendation is robust to PP-716.

4. **C1.4 still rejects** for multi-axis categorical fail. The R-fail axis softens from "extinction" to "MW-bounded but ugly degradation" under PP-716, but the verdict is unchanged.

**Implementation under C1.3 (no new code, design-doc clarification):**

- Affirm canonical session-end Wound clearance (R1v2-L07).
- Document explicitly: narrative-weight permanence for combat events is carried by the Conviction Scar channel (R1v2-L11), not by physical-wound persistence.
- Verify the existing FR-Dissolution + Knot rupture cascade (R1v2-L13 → Conviction Scar via fieldwork §5.6b "broken at high strain → Conviction Scar +1 both partners") is well-documented as the *primary mechanism* by which combat events leave permanent narrative residue.
- Optionally extend: dissolution-witness Scar (R1v2-L14) propagates to PCs witnessing a Dissolution event in combat. Existing canon — no further specification needed.

**Decision-shape statement for Jordan ratification:**

> Wounds clear at session end (canonical, preserve per PP-716 R1v2-L07). Narrative-weight permanence for catastrophic combat events is carried by existing Conviction Scar / Witness Scar channels, triggered by canonical Knot rupture, FR Dissolution, and Dissolution-witness mechanics. No new permanent-wound channel introduced. The Wildermyth narrative pattern is satisfied via the existing Scar apparatus, not via a parallel physical-wound permanence track.

---

## 8. Changes from R1 v1 (audit trail)

| Change | v1 | v2 (PP-716) |
|---|---|---|
| Health formula citation | Vitality = End × 10 (R1-L04) | Health = (End+6) × (MW+1) (R1v2-L04) |
| Max Wounds | "eliminated" (cited from stale L255) | floor(End/2)+1 (R1v2-L05) |
| Wound penalty channel | Combat: −1D Pool; Thread: +1 Ob (cited stale combat_v30 L378) | Universal: −1D Pool (R1v2-L03) |
| Pool degradation worst case (12D start) | 12D → 5D over 7 wounds (unbounded counter) | 12D → 8D over 4 MW-bounded wounds at End=7 |
| Practitioner extinction cascade (Chain 2) | Active P1 cascade; central rejection of C1.2 | Removed; Thread Pool floor 5D (R1v2-L10) contains the loop |
| C1.2 rejection grounds | Categorical R-fail and S-fail (multiple ✗) | Categorical S-fail (canon contradiction) and ambiguity (N-⚠) — softer rejection |
| C1.4 rejection grounds | Multi-axis categorical fail with universal extinction | Multi-axis categorical fail with MW-bounded degradation |
| Recommendation | C1.3 | C1.3 (unchanged) |
| Stale citations | R1-L03 (Threadwork +1 Ob), R1-L04 (Vitality formula), R1-L05 (Max Wounds eliminated) | All re-grounded against PP-716 canon |

---

## 9. Module status

| Item | Status |
|---|---|
| PP-716 canon read at full depth | ✓ |
| Verification ledger entries (15) | ✓ |
| sim_gate('custom', systems=['combat', 'derived_stats']) | (called at commit) |
| NERS full-grain analysis (96 cells, PP-716) | ✓ |
| Mode B chains (5, with Chain 2 fully rewritten) | ✓ |
| Mode D edge cases (15 across 9 categories, several downgraded under PP-716) | ✓ |
| Decision-shape finding (C1.3, unchanged from v1) | ✓ |
| Changes-from-v1 audit trail | ✓ |

**Module 1 R1 v2 status: verified. Supersedes v1.**
