# NERS Verdict — Mass Battle

**Date:** 2026-05-28
**Skill:** valoria-resolution-diagnostic (Stages 3–4)
**Companion:** `resolution_diagnostic_mass_battle.md` (Stage 1 Phase 0–6 + Stage 2 lesson mapping)
**Prior comprehensive audit:** `designs/audit/mass_battle_stress_test_2026-04-29.md` + interdependency + patch_proposals — this verdict cites that audit as canonical for consistency findings, surfaces only the resolution-fitness-lens novel addition (MB5).

## System summary

```
SYSTEM:     Mass Battle
COMPONENTS: dice (Pool = min(Size,Cmd)+Cmd; no floor) + deterministic (TC/H/Damage
            PP-233, simultaneous resolution) + clocks (Morale 1-7 multi-trigger,
            Discipline 1-7 with 0-cliff, Substrate Saturation Counter from threadwork,
            IP/Strain accounting) + state machine (7-phase or 5-phase consolidated)
SCOPE:      mass_battle_v30 + params/mass_combat + mass_battle_integration_v30
PRIOR ART:  2026-04-29 comprehensive audit trio (stress test + interdependency +
            patch proposals); 27 PROVISIONALs + 8 Jordan decisions + 8 auto-approvable
            patches generated, status as of 2026-05-28 unverified at PI changelog level
```

## Verdict

```
VERDICT: NERS-COMPLIANT under resolution-fitness lens, WITH SIGNIFICANT BACKLOG
        — the core resolution architecture is sound (state machine carries weight,
        loops well-bounded, simultaneous damage v21 BIAS-1 validated, cross-scale
        Trigger 5 gate proper, Substrate Saturation cap from threadwork), but 1
        novel resolution-fitness finding (MB5 — no Pool Floor at mass scale) plus
        a substantial pre-existing backlog (8 Jordan decisions + 27 PROVISIONALs +
        3 INTER-CRIT propagation gaps) limit S to PARTIAL.

N: PASS    — No redundant apparatus. The architecture is dense but each piece earns
             its place: Pool formula (PP-233), simultaneous resolution (v21 BIAS-1),
             phase machine, Discipline-degradation trigger, Morale multi-cause +
             cascade-with-brake, Trigger 5 cross-scale gate, Substrate Saturation
             (from threadwork), Battle Plan templates with override, Cavalry pursuit
             with recall. Note: PP-PROP-MB-01 (H frozen at battle start) is REQUIRED
             for N — without it, H formula loops and runs the sim into undefined
             behavior. Auto-approvable status unverified.

R: PASS    — Robust under most extremes:
             • Damage simultaneity preserved (v21 BIAS-1 fix; Mirror Cmd 4v4 n=40
               validated p=0.62 not significant — symmetric outcomes)
             • Rout cascade braked (ROUT_CONTAGION_MORALE_HIT=1; cannot re-cascade
               same turn)
             • Cavalry pursuit damped (recall TN 7 Ob 2)
             • Trigger 5 three-condition gate prevents skirmish-scale loss from
               cascading to faction Stab
             • Domain Echo timing queued to Accounting (no mid-battle stat change;
               Hybrid-clean)
             Caveat: at floor pool (2D, MB5 case), unit is in death-spiral mode
             — architecturally accepted (unit deletion = floor) but the math
             ensures near-zero damage out at that state.

S: PARTIAL — Multiple canon-coherence gaps surface from the 2026-04-29 audit
             that are presumed-still-open as of 2026-05-28:
             • MB1 — 8 DECISION-MB-01..08 open (Stalemate Break, Muster initial
               Size, Morale reset, Discipline recovery, Rout brake, Shadow Intel,
               Siege formula, Cascade cap). **P1.**
             • MB2 — RS=MS terminology drift (peninsular_strain uses RS, others
               use MS — same stat, different name; pre-flagged INTER-CRIT-01). **P1.**
             • MB3 — ED-743 propagation gap (battle-occurrence as direct IP/Strain
               trigger not removed from victory_v30 §0.4 and peninsular_strain
               Step 4e; pre-flagged INTER-CRIT-02). **P1.** Sim that uses those
               docs currently double-counts IP.
             • MB4 — Siege math impossible (Ob 5 from 4D = 0%, doc claims 2%;
               pre-flagged MATH-FAIL-01; DECISION-MB-07 Option A reco pending).
               **P1.**
             • MB9 — H frozen at battle start (PP-PROP-MB-01 auto-approvable;
               status unverified). **P1.**
             • MB14 — 27 PROVISIONAL items open per stress-test §PROVISIONALS.
               **P2 backlog.**
             • INTER-09 through INTER-17 — ~10 cross-system consistency findings.
               **P2-P3 backlog.**

E: PASS-with-flag — Core architecture is intuitive once learned:
             • Pool = min(Size, Cmd) + Cmd — Command caps capacity, Size feeds
               attrition; player can intuit "good general doubles your effective
               pool" and "lose troops, lose pool when Size > Cmd"
             • 7-phase structure (or 5-phase consolidated) is sequential and clean
             • Simultaneous damage at Phase 6 Step 1 — no advantage to declaring
               first
             • Phase 5 Engagement is the moment of decision
             
             E caveat: MB5 (no Pool Floor) is **not visible to the player.** The
             same architecture in personal combat has a Pool Floor 5 that players
             can intuit ("you have a minimum"); mass battle's substitute (unit
             gets deleted) is dramatic but not predictable. If a player has a
             Cmd-1 general's army hit floor pool 2D, the game-state read is
             "we're losing" but the *mechanism* of doom (no Pool Floor =
             accelerating death spiral) is non-obvious. UI work or rule
             reinforcement could help.
```

## Remediation — severity-ranked, worst-first

```
P1 MB1  (8 open DECISION-MB-01..08)              → ratify per 2026-04-29 recommendations
        Direction: ratify each decision per the audit's recommended option (Stalemate
        Option A, Muster Option C, Morale-reset A, Discipline-recovery B, Rout-brake A,
        Shadow-Intel A, Siege Option A, Cascade-cap as-is). Verify resolution status
        first — if any were resolved between 2026-04-29 and now, narrow this finding.

P1 MB2  (RS=MS terminology drift)                → editorial ledger candidate
        Direction: global RS → MS replace in peninsular_strain_v30. Update any
        references in sim/peninsular/ that grep for "RS". Pre-flagged INTER-CRIT-01.

P1 MB3  (ED-743 propagation)                     → editorial ledger candidate
        Direction: strike "Battle: IP+2, Strain+1" from victory_v30 §0.4 and
        peninsular_strain Step 4e. ED-743 (mass_battle §E.2) is canonical authority;
        these two are stale. Pre-flagged INTER-CRIT-02.

P1 MB4  (Siege math impossible)                  → editorial ledger candidate
        Direction: apply DECISION-MB-07 Option A — Pool = Military + 3 (siege
        engineers/equipment bonus). Validates calibration at ~2% Fort3 Mil4 (the
        doc's claimed value). Update mass_battle §1.9 + params/mass_combat
        accordingly.

P1 MB5  (NOVEL: No Pool Floor at mass scale)     → L3 architectural gap
        Three options (do NOT prescribe — Jordan-decision):
          (a) Add explicit Pool Floor = 2 or 3 at mass scale. Matches combat (5) and
              thread (5) architectural pattern. Cost: small mechanical change.
          (b) Document unit-deletion-as-floor as deliberate. Surface in UI: clear
              "this unit is in critical state" indicator when Pool ≤ 3D. Cheap E fix.
          (c) Tie Pool Floor to General Command: min Pool = Command, floored at 2.
              Wedge between (a) and (b). Reinforces "good general saves bad units."
        Recommend **(b) primary + (c) secondary if (b) insufficient**. (a) is the
        most invasive and may not be necessary if the design intent is "armies
        with poor generals fall apart faster" — which is historically defensible.

P1 MB9  (H frozen at battle start)               → apply PP-PROP-MB-01 verbatim
        Direction: per 2026-04-29 patch proposal, auto-approvable. Status as of
        2026-05-28 unverified — confirm before treating as still-needed.

P2 MB14 (27 PROVISIONAL items)                   → per-item Jordan decisions
        Direction: batch-resolve the PROVISIONALs over multiple sessions. Most are
        small clarifications. The count is the issue, not individual blockers.

P2 MB7  (Morale decrease > increase asymmetry)   → L5 (composes with MB5)
        Direction: apply DECISION-MB-03 Option A (Morale resets between battles).
        Removes accumulating multi-battle Morale debt. The intra-battle asymmetry
        is intent-justified ("battle degrades morale by design"); reset between
        battles prevents long-campaign rout cascades.

P2 MB6  (Discipline 0 binary cliff)              → composes with MB5
        Direction: no separate remediation if MB5 addressed. Otherwise document
        the compounding-floor risk (Cmd-1 + Disc 0 + Size-1 = death-spiral
        unrecoverable).

P2-P3 INTER-09 through INTER-17                  → batch with audit phase
        Per 2026-04-29 interdependency audit recommendations.

PASS MB8  Rout contagion — braked
PASS MB10 Damage simultaneity (v21 BIAS-1) — validated
PASS MB11 Battle Plan templates with Command override
PASS MB12 Cross-scale → Trigger 5 (gated)
PASS MB13 Substrate Saturation Counter from threadwork
PASS MB15 GD-1 binding
PASS MB16 Cavalry pursuit with recall
PASS MB17 Phase machine simultaneity
PASS MB18 Output scaling (capacity-only, not survival)
```

## Stage 4 — Re-test of proposed remediations

### Re-test of MB5 (a) — Explicit Pool Floor 2 or 3 at mass scale

- Phase 1: floor pool now bounded. Cmd-1 unit at Size 1 = floor pool 2 or 3 (vs current 2). Marginal change at the worst case; meaningful at Cmd-1 + Size > 1 (where currently Pool = min(Size,1)+1 = 2 stays floor, but the floor was already the *protection*).
- Phase 3a: at very low Cmd, floor provides escape from death spiral.
- Lesson 1: no new variable.
- Lesson 5: dampens MBL2 (Discipline death-spiral) at very low Pool.

**Re-test verdict:** PASS. Minor mechanical addition.

### Re-test of MB5 (b) — Document unit-deletion-as-floor + UI surface

- No mechanical change.
- Phase 5 intent: makes implicit design intent explicit. Improves auditability.
- E: UI surface specifically addresses the E-flag in the verdict.

**Re-test verdict:** PASS — no mechanical surface to test. Cheap fix.

### Re-test of MB5 (c) — Pool Floor = General Command

- Phase 1: at General Cmd 5, floor pool = 5 (matches combat). At Cmd 1, floor = 2 (current). Provides general-scaling protection.
- Phase 3a: reinforces "good general saves bad units" — could be elegant design intent.
- Lesson 1: tied to existing Cmd variable; no new variable.
- New finding risk: at very high Cmd (6-7), floor pool could exceed natural pool for tiny units (Size 1, Cmd 6 = floor 6 vs natural min(1,6)+6 = 7). The natural-pool already exceeds the proposed floor; no harm.

**Re-test verdict:** PASS, with slightly more design appeal than (a). Still architecturally additive.

### Re-test of MB4 fix (Siege Pool = Military + 3)

- Phase 1: Fort3 Mil4 → Pool 7, Ob 6, TN 7 → ~2% (claimed value matches).
- Phase 3a: scaling with Military uniform; +3 constant is the "siege engineering" representation.
- Lesson 1: no new variable.
- Lesson 3: floor sieges become more achievable for high-Mil factions; balance preserved.

**Re-test verdict:** PASS.

### Re-test of MB7 (Morale reset between battles per DECISION-MB-03 A)

- Phase 1: Morale at start of each battle = (Command + quality modifier) regardless of prior battle outcomes.
- Phase 4: removes multi-battle Morale debt cascading toward deterministic rout.
- Lesson 5: damper improvement on MBL1.

**Re-test verdict:** PASS.

### Stage 4 summary

```
RE-TEST: All proposed remediations PASS standalone.
         MB5 has 3 valid resolutions, recommend (b) primary + (c) secondary.
         No new findings of severity > P2 introduced.
         The remediations primarily ratify or apply existing 2026-04-29 audit work;
         MB5 is the only novel remediation requiring fresh design decision.
```

## Editorial ledger candidates (commits blocked, staged inline)

Most P1 findings are already in editorial-ledger backlog from 2026-04-29 (auto-approvable patches + Jordan decisions). The novel addition is MB5:

```yaml
# Candidate for canon/editorial_ledger.yaml — NOT YET COMMITTED (B6)
# Date: 2026-05-28

- id: ED-NEW (assign on commit)
  type: architectural_gap
  severity: P1
  title: "Mass battle has no Pool Floor; unit deletion serves as implicit floor"
  description: >
    Per PP-233: mass-battle Pool = min(Size, Command) + Command. At Cmd 1 + Size 1
    (or any low-Cmd low-Size combination), Pool floors at 2D — well below the
    architectural Pool Floor 5 present in personal combat (combat_v30 §1) and
    threadwork (params/threadwork §Thread Pool floor).
    The mass-battle implicit floor is unit deletion (Size → 0): a unit at low
    enough state to hit floor pool is typically destroyed within rounds anyway.
    But this is not stated as intentional in the design doc; the architectural
    asymmetry with combat and thread is silent.
    P(≥3 hits | 2D, p=0.4) = 0% under Binomial. Identical floor-math shape to
    faction layer F1 finding. Different downstream consequence: faction layer
    has terminal Stab=0; mass battle has unit-deletion as floor.
    Resolution-fitness lens: the architectural choice is legitimate (different
    scales can have different floor mechanisms) but Elegance suffers because
    the player cannot intuit the death-spiral mechanism — they see "we're
    losing" without seeing "no Pool Floor here = floor pool means unit dies
    fast, not that unit recovers like a personal-combat character."
  affected_systems: [mass_battle, sim/provincial/massbattle.py]
  resolution_required:
    - Jordan decision: explicit Pool Floor (option a), documentation +
      UI surfacing (option b), or Pool Floor = Command (option c)
    - if (a) or (c): update params/mass_combat §Core Formula
    - if (b): document in mass_battle §A.4 + add UI indicator spec
  surfaced_by: resolution_diagnostic_mass_battle 2026-05-28 finding MB5
  status: open
```

The other P1s (MB1, MB2, MB3, MB4, MB9) are **already in 2026-04-29 audit pipeline.** This verdict cites their continuation. Resolution status verification (commit history scan) recommended before treating any as still-open.

## Confidence and limitations

`[CONFIDENCE: high]` — MB5 (math verified against PP-233 formula); MB10, MB12, MB15, MB17 (audit-validated)
`[CONFIDENCE: medium]` — MB1, MB3, MB9 (resolution status verification deferred — would require commit-log scan)
`[CONFIDENCE: medium]` — MB7 lesson-mapping (composes with MB5; somewhat dependent on MB5 resolution)

**Files NOT deep-read this pass (transparency, per audit-discipline):**
- `designs/provincial/mass_battle_v30.md` main body (read via index only)
- `tests/sim/sim_mb_06_v22.py` (referenced via integration spec only)
- `params/mass_combat.md` after first 11k (truncated, full file 33k)

**Departures from skill INITIAL HYPOTHESES:**
- Skill: "Mass battle — likely compliant, well-bounded spiral; small pools exist but the state machine carries the weight; loops appear damped."
- **Confirmed.** State machine carries the weight; loops are well-damped.
- **Skill did not predict MB5.** Novel resolution-fitness finding — architectural asymmetry between mass-battle (no Pool Floor) and combat/thread (Pool Floor 5). Legitimate by intent but legibility-weak.
- **Skill did not anticipate the 2026-04-29 audit scope.** The system has had recent comprehensive consistency-stress-testing; this turn's role is cross-checking + novel-finding surfacing, not duplication.

**Relationship to handoff and adjacency:**
- No active handoff for mass battle (unlike combat).
- MB5 lesson-mapping respects skill discipline: surfaces 3 options, recommends a primary + secondary, but does NOT prescribe among the 3 (Jordan-decision).
- Adjacent verdicts: MBL3 = faction L1 (covered in faction verdict); MBL6 = faction L7 (covered in faction verdict); cross-scale Substrate Saturation = threadwork TL4 (covered in threadwork verdict).
