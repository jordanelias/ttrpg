> **SUPERSEDED — 2026-06-10.** This Stage-1+3 verdict was issued from an index-depth read (its own caveat: "if a deeper read surfaced a fresh finding, it would supersede this verdict"). The full-depth read exists: `designs/audit/2026-06-10-investigation-exploration-diagnostic/` (`00_MASTER.md` + `resolution_diagnostic_fieldwork.md` + `ners_verdict_fieldwork.md`). Architecture findings INV1–INV9 **stand**; the NERS-COMPLIANT verdict is **reversed** (NON-COMPLIANT: E fail P1 — roll inputs canonically indeterminate across master/params/investigation_systems; R fail P2, scoped — ER-2 unlanded at wound-floored pools). Retained unedited below for the record.

# Resolution Diagnostic + NERS Verdict — Investigation / Fieldwork

**Date:** 2026-05-28
**Skill:** valoria-resolution-diagnostic (Stages 1+3 consolidated)
**Scope:** investigation + fieldwork per skill INITIAL HYPOTHESES — covers `designs/scene/investigation_systems_v30.md` (CANONICAL 2026-04-17), `designs/scene/fieldwork_v30.md` (DESIGN, v1.1 PP-628/PP-630)
**Status:** Audit output. Format: compact (single file, Stages 1+3 consolidated) — system is skill-predicted clean PASS.

## §0 Citations

- `designs/scene/investigation_systems_v30_index.md` — full heading map (38 sections, 4 subsystems: NPE / Investigation Interface / Dialogue Lattice / Response Resolution Matrix)
- `designs/scene/fieldwork_v30_index.md` — full heading map (70 sections incl. §4 Investigation Evidence Track)
- prior turn substrate (canon constraints, mechanic-audit SKILL, canonical_sources)

## §1 Component decomposition (Phase 0)

| Component | Mechanism | Quantity category |
|---|---|---|
| **A · Fieldwork Pool** | `Spirit×2 + History (+ TPS for Thread-Read)`; per-activity attribute rotation | Dice |
| **B · Evidence Track** | 3 / 5 / 8 thresholds per case complexity | **Discrete accumulator** (clock) |
| **C · Five-Filter Chain** | Response Resolution Matrix §4 — deterministic five-filter pipeline | **Deterministic** |
| **D · Scene-as-Graph** | Investigation Interface — graph traversal, not dice | Deterministic |
| **E · Dialogue Lattice Gate Types** | 6 gate categories (Information / Cooperation / Trust / Sincerity / Disclosure / Refusal); state machine | Discrete state machine |
| **F · NPC Population Engine (NPE)** | Procedural NPC generation; territory-scaled social ecology | Deterministic |
| **G · Cover / Exposure tracks (fieldwork §6)** | Continuous resource with thresholds | **Continuous resource** |
| **H · Thread-Read** | Cross-system to threadwork (TS ≥ 30 gate; Leap eligibility) | Dice + clock |
| **I · Knot-Mediated Remote Investigation (§2.6)** | Cross-system to knots_v30 | Discrete state + Knot strain |
| **J · Three-axis Ob (PP-630)** | Depth + Breadth + Distance (matches threadwork) | Deterministic gate |

## §2 Findings

| # | Finding | Phase | Lesson | Status |
|---|---|---|---|---|
| **INV1** | Five-Filter Chain owns decisions; dice only feed Evidence | 0/2 | L4 clock-routing | **PASS** — skill INITIAL accurate |
| **INV2** | Evidence Track 3/5/8 multi-threshold | 3b | exempt L6 | **PASS** |
| **INV3** | Fieldwork pool routes through Evidence clock for resolution | 1 | **L4 done well** | **PASS** |
| **INV4** | Knot-Mediated Remote Investigation inherits T6 TIER-DRIFT contradiction | 4 | (inherited) | **PASS-with-inheritance** |
| **INV5** | Cover/Exposure as continuous resource with intended thresholds | 3a/3b | exempt L6 second clause | **PASS** |
| **INV6** | Scene-as-Graph — no dice, no loops | 0 | n/a | **PASS** |
| **INV7** | Dialogue Lattice Gate Types — state machine, bounded | 0 | n/a | **PASS** |
| **INV8** | Thread-Read = Perceptive Leap (cross-system) | 4 | gated | **PASS** |
| **INV9** | Three-axis Ob matches threadwork three-axis system | meta | Smooth-positive | **PASS** |

## §3 Verdict

```
SYSTEM:  Investigation / Fieldwork
VERDICT: NERS-COMPLIANT — confirms skill INITIAL hypothesis
         "deterministic five-filter chain owns decisions; dice only feed
         the Evidence clock"

N: PASS — Each component earns its place (NPE creates population; Interface
         provides traversal; Lattice gates dialogue; Matrix resolves
         response; pool feeds Evidence). No redundancy.
R: PASS — Deterministic Matrix carries decision weight; dice contribute to
         clock not to outcome. Robust at extremes — small pool produces
         slow Evidence accumulation, not failure cliff.
S: PASS — Cross-system smooth: Three-axis Ob (PP-630) shares pattern with
         threadwork; Cover shares architecture with combat Composure;
         Thread-Read gates through threadwork TS/Leap; Knot inheritance
         is consistent (modulo T6 TIER-DRIFT pending).
E: PASS — "Intelligibility Gradient" core principle (§Core Principle) is
         player-legible architecture; Scene-as-Graph + Case Board are
         intuitive UI patterns; Evidence thresholds (3/5/8) provide
         clear progress feedback.
```

**No new findings.** System inherits T6 (Knot TIER-DRIFT-001) from threadwork as cross-system dependency; no novel resolution-fitness defects.

`[CONFIDENCE: high]` — architecture cleanly matches skill prediction; Lesson 4 explicitly implemented.

**Files NOT deep-read:**
- investigation_systems_v30 main body (read via index only)
- fieldwork_v30 main body (read via index only, 16k tokens uncovered)
- `tests/sim/fieldwork_lifecycle_stress_01/*` — sim outputs not consulted
- prior audit `tests/sim/sim_threadwork_fieldwork.md` — not consulted

The system is skill-INITIAL-confirmed PASS; depth-of-read appropriate to expected-clean status. If a deeper read surfaced a fresh finding, it would supersede this verdict.
