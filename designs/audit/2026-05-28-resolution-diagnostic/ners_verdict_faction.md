# NERS Verdict — Faction Action Layer

**Date:** 2026-05-28
**Skill:** valoria-resolution-diagnostic (Stages 3–4)
**Companion:** `resolution_diagnostic_faction.md` (Stage 1 Phase 0–6 + Stage 2 lesson mapping)
**NERS source:** PI `<definitions>` block (canon/definitions.yaml 404 — see diagnostic §0)

## System summary

```
SYSTEM:     Faction action layer
COMPONENTS: dice (bare 1–7 stat pools) + deterministic (CI/Stability/Wealth accounting, Triggers, Collapse) + clock (CI 0–100; shallow Parliamentary best-of-3)
SCOPE:      faction_layer_v30 + factions_personal_v30 + military_layer_v30 + ci_political_v30
PRIOR ART:  designs/audit/2026-05-16-faction-ners-all-directions.md (content-coverage, complementary lens; A-1..A-8 gaps remain open)
```

## Verdict

```
VERDICT: NON-COMPLIANT
        — bare-stat dice pools resolve pivotal, irreversible outcomes at small-pool
          floors where the designed safeguards (anti-death-spiral floor, shallow
          Parliamentary clock) are mathematically inactive; the L1 collapse loop
          and the L7 Wealth-Zero Military cascade are both damped on the wrong
          dimension and bounded only to non-functional terminal states.

N: PASS    — Removing the dice apparatus or the Trigger surface would worsen play;
             nothing here is redundant. Note: a Lesson-3 fix that adds aggregating
             apparatus must itself be necessary; over-engineering Domain Action
             resolution to "fix" small pools would fail N.

R: FAIL    — F1, F3, F6, F7 all bite at extremes. The system does not hold:
             • Bare 2D pool vs Ob 4 at TN 7 → P ≈ 0 on pivotal Domain Actions
               (F1) — Lesson 3.
             • Anti-death-spiral floor caps Ob at 4 but pool is still 2D — safeguard
               present, safeguard cannot save (F3) — Lesson 3 + 4.
             • L1 collapse loop terminal-unbounded; recovery rate +1/clean-season
               vs. trigger rate ≥1/season net negative under contest (F6) — Lesson 5.
             • L7 Wealth-Zero Mil-erosion undamped on Mil dimension — Wealth
               recovery doesn't restore Mil; Mil 1 floor is non-functional (F7) —
               Lesson 5.

S: FAIL    — Canon-internal contradictions block clean reasoning:
             • Conflicting Ob formulas: params says floor(stat/2)+1, design doc
               says target stat directly (F2) — diverges at stat ≥ 3.
             • factions_personal_v30 §8.1 still 6-stat (Mandate, no Intel);
               params/factions/stats_1_7_scale.md is 7-stat per PP-686 v2 +
               ED-787 (F8) — active drift between authoritative sources.
             • Absolute stat damage (−1 Mil) has non-uniform impact: −30%
               relative at Mil 6→5, −64% at Mil 4→3, 0% at Mil 2→1 (already
               P=0) — Lesson 2 violation (F4).
             • Best-of-3 Parliamentary clock is too shallow to defang small
               pools — sibling system mass_battle achieves deeper averaging
               via Margin System; faction Vote does not (F9) — Lesson 4
               execution-shallow.

E: FAIL    — The player cannot intuit the system's failure modes from the
             surface. A faction at Stab 2 reads as "fragile but recoverable"
             (Stability is a 1–7 stat, 2 is not the bottom; anti-death-spiral
             floor exists as a stated safeguard); the player is not given the
             information that Stab 2 produces P ≈ 0 Accounting Check passes
             and is mechanically a doomed state. The safeguard *appears
             strong* and *misleads intuition*. Independent of F1/F3, the F10
             concern (Stab triple-role) is borderline-elegant but resolves to
             a single causal narrative — not a true conflation. A Lesson-1
             remediation that split Stab would itself fail E (added apparatus
             not necessary). So E fails on the legibility-of-failure axis,
             not on excess apparatus.
```

## Remediation — severity-ranked, worst-first

```
P1 F1  (Bare-stat pool on pivotal DA)            → L3 (master)
       Direction: route Domain Action consequence through deterministic accounting
       OR aggregate the NPC pool the way player-leader bonus does for players
       (e.g., NPC roll = stat + 2 floor; or stat + ally-faction-influence bonus).
       Defang the P=0 floor.
       
P1 F3  (Anti-death-spiral floor non-functional)  → L3 + L4
       Direction: replace the Ob 4 cap with either (a) deterministic suspension
       of the Accounting Check at Stab ≤ 2 with cumulative pressure routed to
       a recovery-clock, OR (b) pool-augmentation at low Stab (Stab ≤ 2 →
       roll Stab + 2 bonus dice for the Check) so the safeguard can actually
       function. Current safeguard is theatre.
       
P1 F6  (L1 collapse loop unbounded)              → L5
       Direction: bound the loop short of extinction. Options ranked least to
       most invasive: (i) Stab=1 as a hard floor that cannot tick to 0 except
       via Trigger 5 or narrative-flagged events; (ii) raise §1.3 Recovery
       rate at low Stab (+2 per clean season at Stab ≤ 3); (iii) formalize
       collapse → RM-emergence as an explicit recovery path (already in GD-3,
       but currently described as "new emergent faction" rather than as a
       structural damper on the collapse loop — re-frame).
       
P1 F7  (L7 Wealth-Zero Mil cascade undamped)     → L5
       Direction: couple recovery to the degrading dimension. Wealth recovery
       restores Mil at +1 per 2 seasons (Wealth ≥ 1), capped at the original
       Mil value. This makes the loop have a damper on the dimension that
       actually degrades.
       
P1 F5  (Decrease > Increase stat asymmetry)      → L5
       Direction: broaden the recovery surface. Currently only Church
       Absolution (+1 Stab) and Löwenritter endorsement (+1 Stab) provide
       external recovery. Add per-faction recovery actions (e.g., "Domestic
       Stabilization": Govern OW in capital → +1 Stab once/season; or
       Diplomacy with allied faction → +1 Stab on Success), so non-Church
       factions can recover without external aid.
       
P1 F2  (Canon defect — conflicting Ob formulas)  → editorial ledger candidate
       Direction: ED-NEW Domain Ob formula reconciliation. Decide between
       floor(stat/2)+1 (params) and stat directly (design doc §8.1).
       Cite ratification. Update both docs to match. Until resolved, F1 dice
       math has two interpretations and the diagnostic floor probabilities
       are inexact at stat ≥ 3.
       
P1 F8  (Canon defect — PP-686 v2 / ED-787 drift) → editorial ledger candidate
       Direction: ED-NEW factions_personal_v30 §8.1 refresh to 7-stat
       L + PS + Intel per PP-686 v2 + ED-787. Add SUPERSEDED marker per
       supersession discipline. Reframe Mandate-keyed rules (Parliamentary
       Vote uses Mandate) to either L or PS per PP-686 v2 §3.4-3.5 intent.
       
P2 F4  (Absolute stat damage non-uniform)        → L2
       Direction (a, mechanical): convert stat-damage events to proportional
       damage when the stat is being rolled (e.g., −20% of pool, floor 1).
       Direction (b, documentation): leave absolute, document as deliberate
       brittleness modelling, add Phase 5 intent statement. (b) is the lower-
       cost fix if the brittleness is in fact intended.
       
P2 F9  (Best-of-3 Parliamentary clock shallow)   → L4 (deepen)
       Direction: best-of-5, OR replace with an accumulator (Vote Track 0–6,
       +1 per won exchange, threshold = 4 to pass). Deeper clock provides
       averaging that defangs small pools enough to give 2D pools a non-
       zero floor.

Note F10  Stab triple-role surfaced; NOT a Lesson 1 violation
       Rationale: cohesion → resistance under check → collapse if check fails
       is one causal narrative, not three independent jobs. Per Lesson 1's
       "apply minimally — over-splitting harms Elegance" — leave intact.
       Departure from skill worked-example noted.

PASS F11  CI political amplification (Lesson 5)  — damped + bounded by intent
PASS F12  GD-3 RM emergence (Lesson 5)           — deliberate + adequate safeguard
```

## Stage 4 — Re-test of proposed remediations

Per skill discipline, run Phases 1–6 on the *proposed fixes*, not the original system. New findings emerging from the remediation must be surfaced.

### Re-test of F1 Remedy (aggregate NPC pool / route through deterministic)

**Direction (i): NPC pool = stat + floor of 2 (so min 2D becomes effectively 4D + leader+).**

- Phase 1 floor under fix: 4D (Guilds Mil 2 + floor 2). P(≥2 hits | 4D, p=0.4) = 0.475. Defanged.
- Phase 3c role conflation risk: does this make the "floor" a second role for an arbitrary constant? **No new role** — the floor is a balancing parameter, not a stat. Fine.
- Phase 4 loop impact: with higher pool, faction action successes increase → more CI/Wealth/Influence shifts per season → potentially destabilizes balance. **Tuning required.** `[OPEN TRADE-OFF: floor magnitude needs sim calibration — too high removes meaningful stat differentiation; too low fails to defang.]`
- Lesson 1: no new variable created. PASS.
- Lesson 5: faster faction-action throughput could amplify L3 (CI) → check that the CI seasonal cap ±5 + Baralta still hold. Probably yes; sim-validate. `[FLAG: sim-validate CI L3 loop under faster action throughput.]`

**Direction (ii): Route consequence through deterministic.**

- This effectively means making more Domain Action consequences clock-based rather than binary-roll. Significant restructure.
- Phase 3c: risk of forcing one clock variable to absorb the consequences of multiple action types → role-conflation candidate (Lesson 1). `[FLAG: if a single "Faction Pressure" clock absorbs Assert/Suppress/Censure consequences, that's a Lesson 1 risk.]`
- Higher integration cost. Direction (i) is preferable.

**Re-test verdict:** Direction (i) PASS with sim-calibration flag; Direction (ii) risks Lesson 1.

### Re-test of F3 Remedy (anti-death-spiral floor active)

**Direction (a): Suspend Accounting Check at Stab ≤ 2 + route pressure to recovery-clock.**

- Phase 1: low-Stab factions no longer roll the Check → no P=0 floor. Defanged.
- Phase 2: outcome at Stab ≤ 2 becomes clock advancement (recovery from low Stab) rather than binary collapse. Clock depth matters — make it 3+ segments (e.g., 3 seasons of no hostile action → Stab +1).
- Phase 3b: introduces a new clock — risk of accidental threshold cliff. **Mitigation: design as smooth recovery, not stepped reward.**
- Phase 4: this directly damps L1 → strengthens compliance.
- Lesson 1: new variable (recovery-clock) is necessary — fixes a real failure. PASS.

**Direction (b): Stab ≤ 2 → roll Stab + 2 bonus dice for the Check.**

- Phase 1: 2D + 2 = 4D pool. Same as F1 floor fix.
- Phase 3c: bonus dice tied to "low Stab" is a new mechanic. Does it role-conflict with Trigger 5 gate (which requires Mil pool ≥ 4)? **No** — Trigger 5 is offensive, this is defensive Accounting. Disjoint.
- Lesson 5: damps L1 — strengthens compliance.

**Re-test verdict:** Both directions PASS. Direction (a) is more conceptually clean (explicit recovery clock); direction (b) is lower-cost (pool augmentation). Jordan-decision-owned.

### Re-test of F6 Remedy (bound L1 short of extinction)

**Direction (i): Stab=1 as hard floor.**

- Phase 4: L1 loop now bounded at Stab=1 unless Trigger 5 or narrative event fires. Loop bounded ✓.
- Phase 5 intent gate: does this break the intent of allowing faction collapse for GD-3 RM-emergence? **No** — Trigger 5 (lost capital, named officer killed) and narrative events still route to collapse, just not Accounting drift. Existence of collapse preserved.
- Lesson 1: no new variable. PASS.
- Lesson 5: directly satisfies. PASS.

**Re-test verdict:** PASS.

### Re-test of F7 Remedy (Wealth restores Mil)

**Direction: Wealth ≥ 1 sustained → Mil +1 per 2 seasons capped at original.**

- Phase 4: L7 now has damper on Mil dimension. Loop damped ✓.
- Phase 3a: rate at which Mil recovers is uniform-impact (1 stat per 2 seasons regardless of current Mil) — slightly faster recovery in relative terms at low Mil than at high Mil, which is Lesson-2-favorable (small-pool factions recover proportionally faster). PASS.
- Lesson 1: no new variable. PASS.

**Re-test verdict:** PASS.

### Re-test of F9 Remedy (deepen Parliamentary clock)

**Direction: Vote Track 0–6 accumulator, +1 per won exchange, threshold 4.**

- Phase 2: depth = 6 → significant averaging. P(2D vs Ob 4 single exchange) ≈ 0, but accumulator across many exchanges allows long-game accumulation. **But:** if a single exchange is still binary at P=0, no exchange-wins accumulate. Accumulator only helps if per-exchange probability is non-zero.
- Composes with F1 fix: if F1 fixes the pool floor (4D not 2D), then per-exchange P > 0 and accumulator works.
- **F9 alone is insufficient — must be paired with F1.** This is a real Stage 4 finding.

**Re-test verdict:** PASS *if and only if* F1 is also applied. Flag dependency.

### Stage 4 summary

```
RE-TEST: 4 remediations PASS standalone, 1 PASS conditional (F9 requires F1).
         2 OPEN TRADE-OFFs flagged:
           - F1 floor magnitude needs sim calibration
           - F1 + L3 CI loop interaction needs sim validation under
             faster faction action throughput
         No new findings of severity > P2 introduced by remediation.
```

## Editorial ledger candidates (commits blocked, staged inline)

Per Stage 3 output rules: "P1/P2/P3 findings that are canonical gaps append to canon/editorial_ledger.yaml (subject to commit gate; if blocked, stage inline and flag [DRIFT])." Commits are blocked by B6 branch protection. Staged.

```yaml
# Candidates for canon/editorial_ledger.yaml — NOT YET COMMITTED (B6)
# Date: 2026-05-28

- id: ED-NEW (assign on commit)
  type: canon_defect
  severity: P1
  title: "Conflicting Domain Action Ob formulas — params vs design doc"
  description: >
    params/factions/stats_1_7_scale.md §Domain Action Rules states:
    "Ob = floor(relevant stat / 2) + 1."
    designs/provincial/factions_personal_v30.md §8.1 Domain Actions states:
    "Domain Ob: Target faction's relevant stat directly (1–7 scale;
    no division). A faction at stat 4 sets Ob 4."
    These diverge at stat ≥ 3 (params Ob=2; design Ob=3 at stat 4 vs. params Ob=3,
    design Ob=4 at stat 5, etc.).
  affected_systems: [faction_action_layer]
  resolution_required:
    - Jordan ratification of canonical formula
    - update both docs to match
    - cite resolution
  surfaced_by: resolution_diagnostic_faction 2026-05-28 finding F2
  status: open

- id: ED-NEW (assign on commit)
  type: canon_drift
  severity: P1
  title: "factions_personal_v30 §8.1 stat-schema behind PP-686 v2 / ED-787"
  description: >
    factions_personal_v30 §8.1 Faction Stats / §8.1 Starting Values shows the
    pre-PP-686-v2 6-stat schema (Mandate/Influence/Wealth/Military/Intel-blank/Stability;
    Intel column shows "—" for all factions). params/factions/stats_1_7_scale.md is the
    post-PP-686-v2 / post-ED-787 7-stat schema (Legitimacy/Popular_Support/Influence/
    Wealth/Military/Intel/Stability with Intel populated 3–4 per faction).
    Active drift between authoritative sources. Parliamentary Vote in §8.11 routes
    through Mandate which no longer exists as a primary stat per PP-686 v2 (split
    into L + PS).
  affected_systems: [faction_action_layer, parliamentary_layer]
  resolution_required:
    - update factions_personal_v30 §8.1 table to 7-stat
    - add SUPERSEDED 2026-05-01 PP-686 v2 marker
    - reframe Parliamentary Vote rules to specify L or PS (not Mandate)
  surfaced_by: resolution_diagnostic_faction 2026-05-28 finding F8
  status: open
```

## Confidence and limitations

`[CONFIDENCE: high]` — for F1, F3, F4, F6 (skill worked-example math validated against canonical §§).
`[CONFIDENCE: medium]` — for F7 (L7 Wealth-0 Mil cascade is a new loop not in skill or prior audits; derived from military_layer §1.7 + §6.2 in this session).
`[CONFIDENCE: low]` — for the precise floor probabilities at stat ≥ 3 until F2 resolves which Ob formula applies.

**Files not deep-read this pass** (for transparency, per the prior audit's calibration discipline):
- `designs/provincial/faction_behavior_v30.md` (PP-686 v2 Mission/Cascade/PE — relevant for what Ob *would* be under PP-686 v2 if §8.1 is reframed; not read because PP-686 v2's full architecture is beyond resolution scope)
- `designs/provincial/victory_v30.md` (Crown Treaty, Mass Seizure detail — touched only via citation)
- `designs/provincial/peninsular_strain_v30.md` (Turmoil details for L5; covered at substrate level only)
- `designs/world/insurgency_pipeline_v30.md` (GD-3 detail — Pass 2i pending per Pass-2 closure tag)
- `designs/audit/2026-05-16-faction-ners-all-directions.md` §3+ (truncated at ~9k of 29k chars; T-7..T-10 + meta-throughlines + A-1..A-8 not deep-read)

**Departures from skill worked example explicitly noted:**
- F10 (Stab role) — downgraded from Lesson 1 candidate to "not a true conflation."
- F7 — new loop added (Wealth-0 Mil cascade not in skill catalog).
- F2/F8 — canon defects surfaced beyond resolution scope.
