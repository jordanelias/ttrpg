# Resolution Diagnostic + NERS Verdict — Peninsula / Victory

**Date:** 2026-05-28
**Skill:** valoria-resolution-diagnostic (Stages 1+3 consolidated)
**Scope:** peninsula / victory per skill INITIAL HYPOTHESES — covers `designs/provincial/victory_v30.md` (DESIGN, ED-311 pending), `designs/provincial/peninsular_strain_v30.md` (CANONICAL 2026-04-17)
**Status:** Audit output. Format: compact — system is skill-predicted clean PASS.

## §0 Citations

- `designs/provincial/victory_v30_index.md` — full heading map (64 sections, faction-specific victory paths + universal Peninsular Sovereignty)
- `designs/provincial/peninsular_strain_v30_index.md` — full heading map (43 sections, Accord/Turmoil/TCV architecture)
- prior turn substrate (mass battle audits surface ED-743/RS-MS issues)

## §1 Component decomposition (Phase 0)

| Component | Mechanism | Quantity category |
|---|---|---|
| **A · Peninsular Sovereignty** | Universal victory: 11/15 territories for 2 seasons | **Discrete clock** (terminal threshold) |
| **B · Provincial Value (PV)** | Per-territory deterministic value (geography-keyed) | Deterministic |
| **C · Piety Track per territory** | 0-10, multi-threshold (covered in conviction_track_v30 also) | **Discrete accumulator** |
| **D · Accord per territory** | 0-7 typical, deterministic increments/decrements | **Discrete accumulator** |
| **E · Turmoil Counter / Strain** | 0-10 cumulative, threshold effects (§4.3) | **Discrete accumulator** |
| **F · TCV (Territory Consolidation Values)** | Per-territory PV revisions (peninsular_strain §1) | Deterministic |
| **G · Faction Strategies (asymmetric)** | Crown / Church / Hafenmark / Varfell / RM / Löwenritter — each with own clock per §3 | Deterministic + faction-keyed clocks |
| **H · CI 0-100 Theocracy** | Church Seizure Ob redesign (PP-411) | **Discrete accumulator** (cross-system to ci_political and faction layer) |
| **I · World-State Transitions** | RS=0 Post-Calamity / IP=100 Phased Occupation / All Factions Dissolved → Anarchy | Discrete terminal states (campaign-ending events) |
| **J · Co-Victory: Peninsular Partition** | Alliance-stalemate negotiation; bounded by structure | Discrete state |

**Critical observation:** **no dice** at the peninsula/victory layer. All resolution is deterministic clock advancement. Per skill INITIAL: "likely compliant: deterministic clocks, no dice."

## §2 Findings

| # | Finding | Phase | Lesson | Status |
|---|---|---|---|---|
| **PV1** | Victory entirely deterministic — no dice | 0 | n/a | **PASS** — skill INITIAL exact match |
| **PV2** | Peninsular Sovereignty 11/15-for-2-seasons threshold | 3b | exempt L6 (intended terminal) | **PASS** |
| **PV3** | Accord per-territory (0-7) discrete accumulator | 3b | exempt L6 | **PASS** |
| **PV4** | Turmoil Counter with explicit threshold effects (§4.3) | 3b | exempt L6 | **PASS** |
| **PV5** | PV deterministic per geography | 0 | n/a | **PASS** |
| **PV6** | Peninsular Partition Co-Victory — alliance-stalemate negotiation | 4 | bounded | **PASS** |
| **PV7** | World-State Transitions (3 terminal events) | 3b | intended terminal | **PASS** by intent |
| **PV8** | **Inherits MB3 (ED-743 propagation)** — battle-occurrence IP/Strain trigger in victory §0.4 should be struck per mass_battle §E.2 | 0 | canon-defect | **inherited P1** |
| **PV9** | **Inherits MB2 (RS=MS terminology)** — peninsular_strain_v30 uses RS, all others use MS | 0 | canon-defect | **inherited P1** |
| **PV10** | Open editorial items pending (§11 Open Editorial Items + ED-311 Varfell Path B) | meta | design-in-flight | **P3 (note)** |

## §3 Verdict

```
SYSTEM:  Peninsula / Victory
VERDICT: NERS-COMPLIANT — confirms skill INITIAL hypothesis
         "deterministic clocks, no dice"

N: PASS — Each track (PV, Accord, Turmoil, Piety, CI) has distinct
         function; faction-specific strategies (§3) provide asymmetric
         paths without overlap. Universal Peninsular Sovereignty is
         the convergence point.
R: PASS — All clocks are bounded (PV per geography, Accord 0-7, Turmoil
         with §4.3 thresholds, Piety 0-10, CI 0-100). No undamped+unbounded
         loops at this layer (the layer doesn't produce dice variance).
S: PARTIAL — Two inherited canon defects from mass battle diagnostic:
         PV8 (ED-743 propagation gap) and PV9 (RS=MS terminology drift).
         Both are pre-flagged INTER-CRIT findings from 2026-04-29 mass-
         battle interdependency audit. Resolution at peninsula side is
         straightforward editorial work.
E: PASS — Deterministic architecture is highly intuitive: "advance your
         clock, watch others' clocks, push the universal threshold." No
         hidden dice mechanics; player can read victory state directly
         from clock values.
```

**No novel findings** at this layer. PV8 and PV9 are inherited from the mass battle diagnostic (commit batch 1) and remediated by the same editorial work staged there.

`[CONFIDENCE: high]` — deterministic system; clock states verifiable directly without simulation; skill INITIAL match is exact.

**Files NOT deep-read:**
- victory_v30 main body (read via index; 13.8k tokens uncovered)
- peninsular_strain_v30 main body (read via index; 10.7k tokens uncovered)

The system is skill-INITIAL-confirmed PASS and structurally simpler than the dice-bearing systems; index-grain read is appropriate.
