# F — Personal-Scale Lifecycle Bundle (Knot Lifecycle Focus)
## fieldwork_lifecycle_stress_01

**Date:** 2026-05-10
**Mode:** A coverage + B (interaction chains) on Knot Lifecycle (F2); deferred coverage on Wager B5 (analyzed in R5), Heresy B8, Mending B10/B11.
**Source authority:** ED-773 (Knot Lifecycle canonized); fieldwork_v30 §5.6, §5.6a, §5.6b.

---

## 1. Bundle scope

The F module per `combat_arch_residual_stress_01` handoff covers four lifecycle audits:

| Sub-module | Mechanic | Status this session |
|---|---|---|
| **F1** | Wager B5 lifecycle | **DEFERRED** — covered substantively in `combat_arch_residual_stress_01 R5` (commit `d46ad908`). Recommendation: C5.1 preserve canonical post-ED-778. No further analysis surfaced. |
| **F2** | Knot Lifecycle B7 | **VERIFIED THIS MODULE** — focal analysis below. |
| **F3** | Heresy Investigation B8 | **DEFERRED** — canonical jurisdiction spec at `npc_behavior_v30 §2.13a` (ED-670) exists; lifecycle-state-machine audit not in this session's scope. Open follow-up. |
| **F4** | Mending B10/B11 | **DEFERRED** — canonical Mending Stability tracks at `threadwork_v30 §5.1–5.5` exist with thresholds and degradation sources. Mending interaction with PP-716 wound-penalty (R1v2 Chain 2) re-validated; no extinction cascade. Lifecycle-state-machine audit not in this session's scope. Open follow-up. |

F2 is the highest cross-cutting target — Knot Lifecycle threads through R1 (FR Dissolution → Knot rupture → Conviction Scar permanence channel), R4 (named-officer Disposition bond at +3 → companionship eligibility), and R5 (Wager Obligation prerequisite includes Knot existence in some configurations). F2 verification is done here; F1/F3/F4 follow-ups are flagged.

---

## 2. Verification ledger entries

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| F-L01 | knot_formation_prerequisites | 5 prerequisites: Disposition +5, TS ≥30, count limit, no existing, Bonds ≥5 | designs/scene/fieldwork_v30.md | §5.6a | "**Prerequisites (all required):**" |
| F-L02 | knot_count_max_formula | floor(Bonds/2)+1 | designs/scene/fieldwork_v30.md | §5.6a | "PC's current Knot count < floor(Bonds/2)+1 (per params_core §Bonds max Knot count)" |
| F-L03 | bonds_disposition_ceiling | Disposition ceiling = Bonds (PP-684 revised from PP-632) | designs/scene/fieldwork_v30.md | §5.1 (R5 cross-ref) | "ceiling = Bonds** (PP-684, revised from PP-632 floor formula)" |
| F-L04 | knot_resolution_spirit_pool | Spirit×2 vs TN 7 Ob 2; Overwhelming → Close, Success → Distant | designs/scene/fieldwork_v30.md | §5.6a | "**Resolution:** Spirit pool (Spirit × 2) vs TN 7, Ob 2." |
| F-L05 | knot_strain_capacity | Distant 4, Close 7 | designs/scene/fieldwork_v30.md | §5.6b | "\| Distant Knot \| 4 strain \| Can be upgraded to Close (per §5.6a Success outcome). Upgrade resets strain to 0. \|" |
| F-L06 | knot_strain_sources | 6 strain accumulation mechanisms canonical | designs/scene/fieldwork_v30.md | §5.6b | "**Strain accumulation:** A Knot accrues *strain* through several mechanisms:" |
| F-L07 | knot_break_consequences | Disposition → +2 floor, 4 Composure both partners, benefits cease, slot frees, Close-broken → Conviction Scar +1 both | designs/scene/fieldwork_v30.md | §5.6b | "**Knot break consequences:**" |
| F-L08 | knot_rupture_triggers | 5 immediate-rupture triggers (public counsel, death, FR Dissolution, opposing Conviction, player choice) | designs/scene/fieldwork_v30.md | §5.6b | "**Rupture (immediate break, bypassing strain accumulation):**" |
| F-L09 | knot_strain_decay | −1 per season at Accounting if no strain added AND Disposition ≥+3 | designs/scene/fieldwork_v30.md | §5.6b | "**Strain decay:** Knot strain decays at −1 per season at Accounting if no strain was added that season AND Disposition is +3 or higher." |
| F-L10 | fr_dissolution_knot_partner | Tears Knot; partner-of-rupture takes +1 Wound (no armor) | designs/scene/fieldwork_v30.md | §5.6b | "Tears the Knot directly; partner-of-rupture takes +1 Wound (no armor)." |
| F-L11 | conviction_scar_close_knot_break | Close Knots breaking at high strain → Conviction Scar +1 both | designs/scene/fieldwork_v30.md | §5.6b | "For Close Knots that broke at high strain: Conviction Scar +1 to both partners" |
| F-L12 | ed773_lifecycle_authority | ED-773 canonized Knot Lifecycle | designs/scene/fieldwork_v30.md | §5.6b editorial | "[EDITORIAL: ED-773 — Knot Lifecycle specified in fieldwork §5.6b. Closes the gap surfaced by audit during stress-test 26: Knot strain accumulation was canonized (multiple use-sites add strain) but Kno" |

---

## 3. Knot Lifecycle state machine (canonical reconstruction)

Drawing from F-L01 through F-L12, the Knot lifecycle is a five-state machine:

```
                      ┌──── Cooldown 4s ────┐
                      ▼                      │
                  [No Knot] ◄────────────────┤
                      │                      │
                      │ Disposition +5; TS≥30; Bonds≥5; count<MaxKnots; Spirit pool roll
                      │                      │
              ┌───────┴───────────────┐      │
              │                       │      │
       Failure (0 net)          Partial (1)  │ Cooldown 2s
       Disposition −1            ─────────►  │
       Cooldown 4s                           │
                                             │
              ┌─────────────┬─────────────┐  │
              ▼             │             │  │
          [Distant]         │             │  │
       cap 4 strain         │             │  │
              │             ▼             │  │
              │       Success (2 net)     │  │
              │       upgrade via 3       │  │
              │       Disposition +5      │  │
              │       social scenes       │  │
              │             ↓             │  │
              ▼             ▼             ▼  │
          [Close] ◄──── upgrade ─── Overwhelming (3+ net) directly
       cap 7 strain                          │
              │                              │
              ├── strain ≥ cap → break ──────┤
              │                              │
              ├── strain decay −1/season ────┤
              │   if Disposition ≥ +3                                        
              │                              │
              ├── rupture trigger (5 types)  │
              │                              ▼
              │                          [Broken] → consequences applied
              │                          (Disposition −2 or +2, 4 Composure
              │                           both, ScarChannel if Close-broken,
              │                           slot frees)
              ▼
        [Memory state] (partner death; Knot-as-buffer last-stand)
```

The lifecycle is mature post-ED-773.

---

## 4. NERS at full grain — Knot Lifecycle (24 cells)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | F-L01 prerequisites + F-L04 resolution + F-L06 strain sources + F-L08 rupture + F-L09 decay = complete state-machine. ED-773 canonized post-audit gap (F-L12). |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Strain capacities (F-L05) provide bounded mechanic. Spirit-pool resolution (F-L04) integrates with canonical pool math. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Knot operates at personal scale; aggregate effects (relational contagion P-12) propagate to faction Disposition tracking. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | FR Dissolution → Knot rupture (F-L10) is the canonical cross-system pathway threading R1's Conviction Scar permanence channel via F-L11. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Knot-as-Composure-buffer + Knot-mediated remote Thread-Read + Knot-mediated counsel extraction all accumulate strain (F-L06). Lateral coherence preserved. |
| Horizontal | ⚠ | ✓ | ⚠ | ✓ | ⚠ N: max Knot count formula (F-L02 floor(Bonds/2)+1) caps the lifecycle's reach. At Bonds=5, max Knots = 3; at Bonds=10, max = 6. Campaign-arc impact uneven by player Bonds investment. ⚠ R: low-Bonds builds locked out of the deepest social mechanic. |

**Verdict:** 22/24 ✓, 2 ⚠ on Horizontal (Bonds-investment-dependent reach). Mature mechanic, well-audited.

---

## 5. Mode B — Knot Lifecycle interaction chains

### Chain 1: FR Dissolution → Knot rupture → Conviction Scar (load-bearing in R1)

Per F-L10: FR Dissolution targeting Knot partner *tears the Knot*, partner-of-rupture takes +1 Wound (no armor). Per F-L11: Close Knot breaking at high strain produces Conviction Scar +1 both partners.

**R1 v2 cross-reference:** The recommended C1.3 (Knot-tagged permanence via existing Conviction Scar channel) operates entirely through this chain. F-L10 + F-L11 confirm the canonical pathway. R1's analysis is grounded.

The +1 Wound from FR Dissolution targeting Knot partner is canonically session-cleared per R1v2-L07. The Conviction Scar carries the permanent narrative weight. R1's recommendation aligned with this canonical structure.

### Chain 2: Public counsel citation → immediate rupture (Disposition −4)

Per F-L08 row 1: ED-664 §3.5.4 — public citation of private counsel ruptures the Knot with Disposition reset to −4. Tabletop play: this is a high-stakes social mechanic that punishes betrayal.

### Chain 3: Player explicit dissolution

Per F-L08 row 5: Player may dissolve at Accounting at any time. Cost: 2 Composure. Disposition unchanged. Player agency preserved — exit lifecycle is graceful.

### Chain 4: Knot strain decay vs accumulation balance

Per F-L09: −1 strain/season if no strain added AND Disposition ≥+3. Per F-L06: 6 sources of strain accumulation.

**Question:** what's the equilibrium? If a player uses Knot-as-Composure-buffer once per session (+1 strain) and otherwise maintains Disposition ≥+3 with no other strain events, decay −1 cancels accumulation 1:1. Knot is sustainable.

If player uses 2+ Knot-mediated mechanics per season, strain accumulates faster than decay. Capacity 4 (Distant) breaks in 4 seasons of intensive use; capacity 7 (Close) in 7 seasons.

This produces a mechanically interesting tradeoff: heavy Knot use is finite, encouraging cycling among multiple Knot relationships rather than over-relying on one.

### Chain 5: Bonds investment → max Knot count

Per F-L02: max Knots = floor(Bonds/2) + 1. Per F-L03: Disposition ceiling = Bonds. Per F-L01 prereq 5: Bonds ≥5 needed for Knot formation.

**Implication:** Bonds is a triple-gating attribute for Knot lifecycle. Low-Bonds builds (Bonds 1–4) are categorically locked out of the entire Knot mechanic. Bonds 5+ unlocks formation; Bonds 6+ allows 4 max Knots; Bonds 10+ allows 6 max Knots.

This is the ⚠ Horizontal in Section 4 NERS table — a build-investment dependency. It's intentional design (Bonds as the relational-investment stat) but worth noting that low-Bonds builds experience a significantly different campaign character.

---

## 6. Mode D — Knot Lifecycle edge cases (compressed)

### Boundary
**EC-F2.B-01 [P3]:** Strain at exactly capacity (4 or 7) — does the Knot break at next Accounting or at the strain event? Per F-L05 and F-L06, "exceeded" → break at next Accounting. Boundary canonically clean.

**EC-F2.B-02 [P3]:** Distant Knot at strain 3, upgraded to Close via 3 social scenes (F-L04 Success outcome) — does upgrade reset strain to 0 or carry over? Per F-L05 row 1: "Upgrade resets strain to 0." Canonically clean.

### Cascade
**EC-F2.C-01 [P2]:** FR Dissolution near Knot partner (F-L06 source 4) adds +1 strain. If multiple Dissolutions occur in close succession, strain compounds. At Knot capacity, the next Dissolution triggers break PLUS +1 Wound (no armor) per F-L10. Compound effect canonically defined.

### Regression
**EC-F2.R-01 [P3]:** Knot break floor at Disposition +2 or current −2 whichever is lower (F-L07). If pre-break Disposition was −1, post-break is −3 (the floor). Cascading negative trajectory.

### Crunch cascade
**EC-F2.CR-01 [P3]:** Per-season strain accounting + Disposition tracking + max Knot count check + cooldown tracking per failed attempt + Conviction-shift compatibility check (F-L08 row 4). Game-Master bookkeeping at scale; manageable but non-trivial.

### Ambiguity
**EC-F2.A-01 [P2]:** "Sustained Disposition reduction (drops below +3 sustained for 2 seasons)" (F-L06 source 6) — is "sustained" continuous or cumulative? E.g., 1 season at +2, 1 at +3, 1 at +2 — does this count as "2 seasons sustained below +3"? Spec ambiguity.

### Incoherence
**EC-F2.I-01 [P3]:** Threadcut being Knots (§5.6b "Threadcut being Knots") use Coherence as parallel resource. At Coherence 0 (the canonical "memory state"), the Knot enters memory state per F-L08 row 2 (death analog). Coherent but unusual interaction; correctly defined.

### Optimal play
**EC-F2.O-01 [P3]:** Players optimal: form Distant Knots only with NPCs unlikely to hit FR Dissolution / public counsel events; reserve Close Knot capacity (high formation cost) for stable allies; cycle through Distant Knots for tactical buffs, accept eventual breaks. This is intentional design space.

---

## 7. Decision-shape findings

**Recommendation: F2.1 (preserve PP-684/ED-773 Knot Lifecycle as canonical; no mechanical changes recommended).**

**Rationale:**

1. **Knot Lifecycle passes 22/24 NERS** with two ⚠ on Horizontal (Bonds-investment dependency). The ⚠s are intentional design space, not defects.

2. **The lifecycle is mature post-ED-773 (F-L12).** The audit gap (Knot strain accumulation was canonized without break specification) was closed; full state machine now defined.

3. **R1 v2 recommendation depends on this canon being correct.** The F-L10 + F-L11 chain is what makes C1.3 (Knot-tagged permanence) work. F2 verification confirms R1's grounding.

4. **One spec ambiguity surfaced:** EC-F2.A-01 — "sustained Disposition reduction" definition (continuous vs cumulative across seasons). P2 priority. Recommend Game Master adjudication clause OR explicit Spec.

**Implementation:** No mechanical changes. EC-F2.A-01 is a candidate for a small clarification PP if Jordan deems necessary.

---

## 8. F1 / F3 / F4 status (deferred sub-modules)

### F1 — Wager B5 lifecycle
**Status:** Covered substantively in `combat_arch_residual_stress_01 R5` (commit `d46ad908`). Recommendation: C5.1 (preserve canonical Wager Obligation post-ED-778). No further analysis warranted. Wager lifecycle is mature.

### F3 — Heresy Investigation B8
**Status:** **DEFERRED to follow-up session.** Canonical jurisdiction spec at `npc_behavior_v30 §2.13a` (ED-670) exists. A focused F3 module should:
- Audit Heresy Investigation state machine: trigger conditions, evidence accumulation, Tribunal escalation, Excommunication threshold.
- Verify interaction with Conviction track (Faith primary), Reputation, Mandate.
- Surface any drift between npc_behavior §2.13a and Tribunal mechanic in social_contest.

### F4 — Mending B10/B11
**Status:** **DEFERRED to follow-up session.** Canonical Mending Stability tracks at `threadwork_v30 §5.1–5.5` exist. A focused F4 module should:
- Audit Mending Stability degradation sources (§5.2) and threshold consequences (§5.3).
- Verify interaction with PP-716 wound-penalty (Mending Pool subject to −1D Pool with floor 5D per R1v2-L10).
- Audit Mend order in mass-battle (§4.4 New Order: Mend) and Mending Stability Track (§4.4 New track).
- Surface any propagation gaps after PP-716 wound mechanic correction.

**R1 v2 already validated** that PP-716 −1D Pool with floor 5D contains the practitioner-extinction cascade that v1 cited under +1 Ob unfloored. Mending self-treatment loop is a friction loop, not extinction.

---

## 9. Module status

| Item | Status |
|---|---|
| F2 Knot Lifecycle canonical sources fetched at full depth | ✓ |
| F2 Verification ledger (12 entries) | ✓ |
| F2 NERS full-grain analysis (24 cells) | ✓ |
| F2 Mode B chains (5) | ✓ |
| F2 Mode D edge cases (8 across 7 categories) | ✓ |
| F2 Decision-shape finding (F2.1 preserve canonical; one spec ambiguity flagged) | ✓ |
| F1 Wager — covered in R5; no further analysis | ✓ |
| F3 Heresy Investigation — deferred to follow-up | DEFERRED |
| F4 Mending B10/B11 — deferred to follow-up | DEFERRED |

**fieldwork_lifecycle_stress_01 status: F2 verified; F3/F4 deferred.**

**Open follow-ups (carryover for Jordan):**

- F3 Heresy Investigation lifecycle audit (separate session).
- F4 Mending lifecycle audit including PP-716 wound-penalty propagation check (separate session).
- `[GAP: EC-F2.A-01 — "sustained Disposition reduction" definition (continuous vs cumulative across seasons) — basis: F-L06 source 6 ambiguity. Spec clarification or Game Master adjudication clause recommended.]`
