# NERS Verdict — Personal Combat

**Date:** 2026-05-28
**Skill:** valoria-resolution-diagnostic (Stages 3–4)
**Companion:** `resolution_diagnostic_combat.md` (Stage 1 Phase 0–6 + Stage 2 lesson mapping)
**Standing caveat:** Open handoff `2026-05-17-scene-combat-redesign-exploration` — verdict applies to **current chassis** under resolution-fitness lens. Does NOT prescribe among the 5 open directions.

## System summary

```
SYSTEM:     Personal combat
COMPONENTS: dice (Combat Pool 5–17D, floored) + continuous resources (Health, Stamina)
            + clock (Stamina-bounded round timer; wound counter; action-triangle loop)
SCOPE:      combat_v30 + params/combat + derived_stats §4.1 (AUTHORITATIVE) §4.2
PRIOR ART:  pp717_ners_all_directions.md (D1–D5 ratified state); combat_integration_session_a_ners.md
            (chassis validation); all_directions_ners_v27.md (PP-717 baseline)
HANDOFF:    open scene-combat-redesign with 5 directions in analysis;
            content-coverage scope, distinct from resolution-fitness lens
```

## Verdict

```
VERDICT: NERS-COMPLIANT — current chassis under resolution-fitness lens
        (2 P1 canon-defect findings require propagation, 2 P2 canon-defect/gap require
        Jordan ruling, 1 P2 residual Lesson-2 micro-flag at low-End builds, 1 OPEN
        TRADE-OFF deferring to handoff)

N: PASS    — No redundant apparatus. Lessons explicitly implemented:
             Pool DR (L2 mitigation above Agi 4 per PP-717 D2 ratification),
             Pool floor 5 (L3 floor preventing wound-stacking death spiral),
             MW cap 3 (L2 fix preventing End super-linear at high end),
             Crit threshold ≥ 4 (PP-717 D3, "earned" crits),
             Wound penalty universal −1D (PP-716, cross-system Smooth),
             Stage 1/2 dying STRUCK (ED-130 simplification).
             Stamina as deliberate round timer (v27 Throughline 5).
             Action triangle as deliberate tactical loop (v27 T5).

R: PASS    — Chassis holds at extremes:
             • Pool floor 5 prevents low-Agi death spiral
             • Wound clearance at session end prevents inter-session compounding
             • ED-130 (no Stage 1/2 dying) reduces irreversibility
             • Trigger 5 three-condition gate protects skirmish-scale loss
               from cascading to faction Stab (cross-scale CL5 properly gated)
             • Feint pool-reduction non-stacking (PP-293) prevents chained-feint
               loop runaway
             Caveat: under-tested cases — Heavy-armour build × low-End OOB
             chain (per combat_integration audit Horizontal flag). Test
             before declaring full R.

S: PARTIAL — Three active canon issues block clean cross-system reasoning:
             • C2 — PP-717 D2 Pool DR formula ratified per audit but NOT
               propagated to combat_v30 §1 or params/combat §Pool Formula.
               Current canon docs show pre-PP-717 `Agi×2 + Hist + 3`; audit
               shows ratified `min(Agi,4)×2 + max(0,Agi-4)×1 + Hist + 3`.
               Sim against stale docs produces wrong builds. **P1.**
             • C6 — STR multiplier text "Heavy Blunt = ×3" contradicts
               example "Mace=6" (which implies ×1.5 at STR 4). Flagged in
               combat_integration_session_a_ners.md as editorial-open;
               unresolved. **P2.**
             • C3 — OOB −2D vs Pool Floor 5 interaction undefined. Two
               possible canon reads (floor holds vs. OOB bypasses); canon
               does not explicitly say. **P2 (canon gap).**
             Strong Smooth-positive: PP-716 wound penalty universality
             (−1D to ALL Pools incl. Thread, Mass-battle Command) is
             cross-system consistent.

E: PASS    — Player can intuit:
             • Agi = pool + initiative (PP-717 D2 explicitly splits these
               into "tactical" and "statistical" channels per pp717_ners D2)
             • End = HP + Stamina (one stat, coherent "body durability"
               narrative)
             • STR = damage (one stat, coherent "body power" narrative)
             • Action triangle (Strike/Feint/Defend) learnable in one
               sentence
             • Initiative as declare-last information advantage
             PP-717 ratifications (D1 MW cap, D3 crit ≥ 4) are single-
             parameter changes — no new subsystems, no new tracking.
             v27 Meta-Throughline A "Compression over expansion" holds.
             
             E caveat: Stamina round-count cliffs (v27 Meta-B) are
             "real but invisible" — UI must surface the round count for
             the cliffs to be playable rather than mystifying. UI domain,
             not mechanics; flag, not failure.
```

## Remediation — severity-ranked, worst-first

```
P1 C2  (PP-717 D2 Pool DR not propagated)        → editorial ledger candidate
       Direction: ED-NEW Pool DR propagation. Update combat_v30.md §1 and
       params/combat.md §Pool Formula to:
         Combat Pool = min(Agi,4)×2 + max(0,Agi-4)×1 + Hist + 3 (minimum 5)
       Per PP-717 D2 ratification per pp717_ners_all_directions.md. Cite.
       Until propagated, sim runs against stale params produce wrong builds
       (Agi 6 = pool 18 against current canon, pool 15 against audit).

P2 C6  (STR multiplier text vs example)          → editorial ledger candidate
       Direction: ED-NEW STR multiplier reconciliation. Existing canon:
         params/combat.md §Damage Formula states:
           "STR multiplier (multiplicative): Light×1, Heavy×2, Blade×1,
            Blunt×1.5. Heavy Blunt = ×3."
         Examples at STR 4: "Dagger=4, Arming sword=8, Mace=6, Warhammer=12."
       Mace is Short Heavy Blunt — by formula ×3 → 12, but example says 6.
       Jordan ruling: which is canonical? Update the other to match.

P2 C3  (OOB −2D vs Pool Floor 5)                 → editorial ledger candidate
       Direction: ED-NEW OOB-Floor interaction. Two options:
         (a) OOB respects floor: 5−2 → 5 (no impact at floor). Extends the
             Pool-floor L3 safeguard to OOB, consistent with wound penalty
             treatment (derived_stats §4.1 caps wound penalty at floor).
         (b) OOB ignores floor: 5−2 → 3 (OOB always bites).
       Recommendation: (a) for consistency with wound penalty treatment,
       but Jordan-decision-owned. Resolution unblocks sim accuracy.

P2 C5  (Health super-linear at low End)          → L2 (base-parameter)
       Direction (a, mechanical): smooth low-End Health curve. E.g.,
       reduce End 1 Health from 14 to 10, End 2 from 24 to 18 (per-End
       jumps narrow from +71% to ~+50%).
       Direction (b, documentation): document as intentional low-End
       brittleness. Players choosing End 1–2 know they're sharp-disadvantage
       builds.
       (b) is lower-cost; low-End exposure mitigates impact.

Note C1  (Pool floor + wound non-uniform impact, L2/L3 trade-off)
       NO REMEDIATION. The trade-off (Lesson 2 violated at floor in
       exchange for Lesson 3 floor-safeguard working) is the correct
       priority per skill master-lesson framing. "Small pools are
       primarily architectural — route through Lessons 3/4 (don't roll
       it, or clock it) or aggregate the pool." The floor IS the
       architectural pool-aggregation. Document the trade-off in design
       doc as deliberate.

PASS C4  Crit threshold ≥ 4 — discrete trigger, exempt L6 per three-category
PASS C7  Cross-scale CL5 (combat → faction Trigger 5) — gate is safeguard
PASS C9  Action triangle (CL3) — bounded by round count + Stamina
PASS C10 Stamina round-count cliffs (CL1) — UI domain, leverage by intent
PASS C11 Wound penalty universality (PP-716) — Smooth-positive
PASS C12 Take-a-Breath recovery (End+Hist)×2 — tapered tradeoff

OPEN TRADE-OFF C8 — Five convergent observations from open handoff
       (initiative-as-state, engagement-profile, bind/distance, asymmetric
       commitment, reading opponent). These are CONTENT-COVERAGE concerns
       (Mode B lens), distinct from RESOLUTION-FITNESS (this skill's
       lens). My verdict applies to the current chassis as a resolution
       engine. If a redesign direction is selected that materially
       restructures the resolution components, this diagnostic MUST be
       re-run on the new chassis. The current verdict (NERS-COMPLIANT)
       does NOT endorse leaving the chassis unchanged — it says the
       chassis is sound under the resolution lens, leaving the
       content-coverage question to Jordan and the handoff.

       NO PRESCRIPTION among the 5 directions per standing instruction.
```

## Stage 4 — Re-test of proposed remediations

### Re-test of C2 (propagate PP-717 D2 formula)

- Phase 1: pool formula change is what the audit already ratified; sim outcomes match the audit's NERS verdict on D2 (PASS).
- Phase 4: no new loops introduced; existing loops re-stated with corrected formula.
- Lesson 1: no new variable. PASS.
- Lesson 2: directly implements L2 mitigation. PASS.

**Re-test verdict:** PASS. Propagation only — no mechanical change.

### Re-test of C5(a) (smooth low-End Health)

- Phase 1: End 1 floor at Health 10. Build floor unchanged (Combat Pool min 5; this affects Health only).
- Phase 3a: smoother Health-per-End curve at low end. New jump magnitudes (End 1→2 from +71% to ~+50%) — still a jump due to MW threshold, but reduced.
- Phase 3b: new threshold cliff? **No** — the curve is smoothed within the existing MW structure. PASS.
- Lesson 1: no new variable. PASS.
- Phase 5 intent: matches design philosophy of PP-717 (smooth scaling). PASS.

**Re-test verdict:** PASS for direction (a). Direction (b) is documentation-only; no re-test needed.

### Re-test of C5(b) (document low-End brittleness as intentional)

- No mechanical change. Documentation update only.
- Phase 5 intent: makes implicit intent explicit, satisfying Phase 5 evidence-of-intent requirement for future audits.

**Re-test verdict:** PASS — no mechanical surface to test.

### Re-test of C1 (NO remediation — confirm trade-off stable)

A hypothetical "fix" of the L2 wound non-uniformity at floor (e.g., proportional wound penalty: −20% pool per wound):

- Phase 3a: now uniform impact at all pools (proportional).
- **Phase 1**: but Pool floor 5 was the L3 safeguard. Removing the floor (which is required for proportional penalty to bite) re-introduces small-pool death-spiral. Floor-pool character now drops to 4D (1 wound) → 3D (2 wounds) → cliff.
- Lesson 3 now violated. Lesson 5 (wound death-spiral loop) becomes unbounded.

**Re-test verdict:** "Fix" of C1 FAILS — creates worse findings than the trade-off it removes. Confirms the current chassis's choice is correct. **No remediation needed.**

### Re-test of C8 (handoff direction selection — out of scope)

`[OPEN TRADE-OFF — DEFERS to handoff resolution.]` If a redesign direction is selected:
- Resolution-fitness diagnostic must re-run on the new chassis.
- The current chassis's NERS verdict will not transfer — new components, new loops, new floors.
- No remediation prescription is made in this diagnostic.

### Stage 4 summary

```
RE-TEST: 4 remediations PASS, 1 confirms trade-off stable (C1 no-fix),
         1 OPEN TRADE-OFF (C8 defers to handoff).
         No new findings of severity > P2 introduced by any remediation.
         C1 hypothetical "fix" actively FAILS — confirms current trade-off.
```

## Editorial ledger candidates (commits blocked, staged inline)

Per Stage 3 output rules: P1 findings append to canon/editorial_ledger.yaml. Commits blocked (B6). Staged inline.

```yaml
# Candidates for canon/editorial_ledger.yaml — NOT YET COMMITTED (B6)
# Date: 2026-05-28

- id: ED-NEW (assign on commit)
  type: canon_drift
  severity: P1
  title: "PP-717 D2 Pool DR formula not propagated to combat_v30 / params/combat"
  description: >
    tests/audit/pp717_ners_all_directions.md ratifies D2 (Pool DR above Agi 4):
    "Combat Pool = min(Agi,4)×2 + max(0,Agi-4)×1 + Hist + 3" — diminishing returns
    at Agi 5–7 giving +1D instead of +2D per point.
    But designs/scene/combat_v30.md §1 Combat Pool still states:
    "Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)"
    And params/combat.md §Pool Formula matches the pre-PP-717 version.
    Active drift between audit-ratified state and canonical design+params.
    Sim against stale params produces wrong builds: Agi 6 = pool 18 (current
    canon) vs pool 15 (audit-ratified).
  affected_systems: [personal_combat, combat_integration_sim]
  resolution_required:
    - update combat_v30.md §1 to PP-717 D2 formula
    - update params/combat.md §Pool Formula to match
    - cite PP-717 D2 ratification per pp717_ners_all_directions.md
  surfaced_by: resolution_diagnostic_combat 2026-05-28 finding C2
  status: open

- id: ED-NEW (assign on commit)
  type: canon_defect
  severity: P2
  title: "STR multiplier text vs example contradiction (Heavy Blunt ×3 vs Mace=6)"
  description: >
    params/combat.md §Damage Formula:
    "STR multiplier (multiplicative): Light×1, Heavy×2, Blade×1, Blunt×1.5.
     Heavy Blunt = ×3."
    Worked example at STR 4: "Dagger=4, Arming sword=8, Mace=6, Warhammer=12."
    Mace is Short Heavy Blunt — by formula ×3 → STR 4 × 3 = 12, but example
    says 6 (implying ×1.5). Both are not internally consistent.
    Previously flagged in tests/audit/combat_integration_session_a_ners.md as
    editorial-open; unresolved.
  affected_systems: [personal_combat]
  resolution_required:
    - Jordan ruling on Mace damage scaling
    - update params and worked example to match
  surfaced_by: resolution_diagnostic_combat 2026-05-28 finding C6
              (prior surfacing: combat_integration_session_a_ners.md)
  status: open

- id: ED-NEW (assign on commit)
  type: canon_gap
  severity: P2
  title: "OOB −2D vs Combat Pool Floor 5 interaction undefined"
  description: >
    params/combat.md §Pool modifiers states: "Stamina Out of Breath: −2D to
    all rolls until recovery action taken."
    designs/scene/derived_stats_v30.md §4.1 states wound penalty is "Cumulative;
    capped by per-Pool floor (Combat Pool floor 5)."
    Canon does NOT explicitly state whether OOB respects the Pool floor.
    Two consistent interpretations:
      (a) OOB respects floor: 5 − 2 → 5 (no impact at floor — consistent with
          wound penalty treatment)
      (b) OOB ignores floor: 5 − 2 → 3 (OOB always bites)
    Sim implementations must currently choose; choice affects floor-pool
    character outcomes.
  affected_systems: [personal_combat, combat_integration_sim]
  resolution_required:
    - Jordan ruling on OOB-Floor interaction
    - update params/combat.md §Pool modifiers with explicit statement
  surfaced_by: resolution_diagnostic_combat 2026-05-28 finding C3
  status: open

- id: ED-NEW (assign on commit)
  type: balance_residual
  severity: P2
  title: "Health super-linear at low End due to MW threshold jumps"
  description: >
    Per derived_stats_v30.md §4.1 reference table:
    End 1 → 14 HP (MW 1), End 2 → 24 HP (MW 2): +71% jump at MW threshold.
    End 3 → 27 HP (MW 2), End 4 → 40 HP (MW 3): +48% jump at MW threshold.
    End 4–7 smoothed by PP-717 D1 (MW cap 3): +4 HP/End consistent.
    PP-717 D1 was calibrated for high-End dominance (End 6+); low-End jumps
    remain.
    Lesson-2 residual at low-End builds (exposure low — End 1–2 builds are
    rare).
  affected_systems: [personal_combat]
  resolution_required:
    - choose: (a) smooth low-End Health curve or (b) document as intentional
      low-End brittleness
  surfaced_by: resolution_diagnostic_combat 2026-05-28 finding C5
  status: open
```

## Confidence and limitations

`[CONFIDENCE: high]` — C2 (drift verified by reading both audit and current docs), C4/C7/C9/C11/C12 (audit-validated)
`[CONFIDENCE: medium]` — C1 (math reasoning), C5 (probability calculations from Binomial)
`[CONFIDENCE: medium]` — C3 (canon gap discovered this session; possible canon resolves it somewhere not read)
`[CONFIDENCE: low]` — C8 (out of resolution-fitness scope by skill construction)

**Files NOT deep-read:**
- `combat_v30.md` §6+ (advanced mechanics)
- `all_directions_ners_v27.md` Meta-Throughlines + 6-direction balance (partial)
- `derived_stats_v30.md` §5+ (Composure/Social/Faction — covered later in Turn G social contest)
- `designs/audit/2026-05-17-scene-combat-contest/**` — **intentionally not read** to avoid risk of direction-among-5 prescription per standing instruction

**Departures from skill INITIAL HYPOTHESES:**
- Skill: "Personal combat — likely mostly compliant; watch the flat −1D wound at the 5D floor (Lesson 2 candidate)." → confirmed as a **trade-off (C1)**, not a violation. The floor is the L3 safeguard; the L2 non-uniformity at floor is the trade-off price; the trade-off is correct per master-lesson priority.
- New canon-defect findings (C2, C3) not predicted by skill — discovered via audit-vs-canon cross-checking.

**Handoff caveat upheld:** zero prescriptions among the 5 open directions. C8 explicitly defers. If a direction is selected, this diagnostic must re-run on the new chassis.
