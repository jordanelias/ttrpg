# Module Manifest — Combat Architecture Residual-Risk Stress Test
## Sim name: combat_arch_residual_stress_01
## Date: 2026-05-09
## Base reference: tests/stress/combat_videogame_arch_2026-05-01/ (commit 06dae57)
## Mode: G (Incremental Build Protocol) + Mode A/B/D applied per module
## Status: in-progress

---

## Scope

Pressure-test the ten residual risks (R1–R10) flagged in `06_synthesis.md §4` of the 2026-05-01 combat videogame architecture stress test. Each R-module produces decision-shaped output Jordan can act on directly during ratification of the EXPLORATORY composite stack (T2+T4 / S7-hybrid / I1→I4→I2 / A+C / E1+E6+E7 / F2+F3).

The composite stack is **not yet canon**. R-module findings are inputs to ratification — they do not presuppose ratification. If Jordan rejects the stack entirely, R-module data still constrains alternative architectures because the questions (wound permanence, skill input, mass-mode reframe, hero participation, wager stake range, Fibonacci cap, friendly fire, tempo-shift mechanism, two-arch sufficiency, IP-gauge threshold) are stack-independent.

**This is NOT a new full-stack sim.** Existing canonical resolution math is preserved. Only new code: per-module isolation/interaction harnesses targeting the specific R-question.

---

## Self-audit findings carried forward (from 07_audit_synthesis.md)

The 2026-05-01 self-audit identified four methodological flaws in the original stress test. R-modules apply these corrections explicitly:

1. **NERS at full grain.** Each candidate option per R-module gets all 24 cells (6 directions × 4 NERS). No compression.
2. **N-failures are categorical.** Any candidate with N=✗ on any direction is rejected outright. Vote-counting does not apply.
3. **Diagonal vs lateral boundary made explicit.** Diagonal = cross-system (e.g., combat ↔ thread). Lateral = same-scale parallel (e.g., combat ↔ social-contest at scene scale). Findings cited under both lenses are flagged for double-counting.
4. **No threshold drift.** Per-direction scoring criteria fixed at module start; same criteria applied to every candidate.

Mode D (edge case discovery) applied to each R-module across all 9 categories: boundary, cascade, regression, deadlock, crunch cascade, ambiguity, incoherence, optimal play, degenerate.

---

## Pre-flight gates (Module 0)

| Item | Status |
|---|---|
| Bootstrap complete | ✓ |
| `task_gate('simulation')` | ✓ |
| Parallel-session check via `read_active_sessions()` | known broken — returned `[]`; unverifiable |
| Synthesis files read at full grain | ✓ — 06/05/04/07 read in entirety |
| `canonical_sources.yaml` registry drift documented | ✓ — see "Registry drift" below |
| PP-684 collision resolved | ✓ — see "PP-684 collision" below |
| Verification ledger built | (Module 0 deliverable) |
| `sim_gate('custom', systems=[...])` | (Module 0 deliverable) |

---

## PP-684 collision resolution

Two PP-684 entries appeared in the survey:

| Date | Commit | Original meaning |
|---|---|---|
| 2026-04-18 | 6427e2b | Disposition ceiling = Bonds. Resolves ED-683 — Knot formation. |
| 2026-05-01 | 0f29cf8 | 13-Conviction taxonomy + Self-Other axis. |

Resolution: per fce5953 (2026-05-02) — "PP register collision repair — mass-battle set renumbered to PP-711..715 — ED-782" — the 2026-04-18 PP-684 (Disposition ceiling = Bonds) was renumbered to the PP-711..715 batch. The 2026-05-01 PP-684 (13-Conviction taxonomy) is canonical.

**Implication:** any code or text in this stress harness referring to "PP-684" must mean the 13-Conviction taxonomy. The Disposition-ceiling-=-Bonds rule survives under one of PP-711..715 — exact mapping verified at ledger time per module that touches Knot Lifecycle (relevant for R1 wound permanence × Knot interaction).

---

## Registry drift in canonical_sources.yaml

The `combat` system block in `references/canonical_sources.yaml` declares:

```yaml
combat:
  design_doc: params/combat.md
  canonical_sha__params__combat_md: "50c50d0032210e4613bfc2388582961aa46c9f07"
```

But the actual section-structured combat design lives at `designs/scene/combat_v30.md` (which exists, with `_index.md` and `_infill.md`). The 2026-05-01 synthesis files reference `designs/scene/combat_v30.md` for §2, §5, §7, §8, §11.5, §13.2, §13.3 — which is correct. The registry's `design_doc` field for combat is pointing at the params file rather than the design file.

This is the same shape as the prior session's Solmund/Galbados drift finding. Both reference paths are real; the registry's `design_doc` field is incomplete.

**Action this session:** fetch BOTH `designs/scene/combat_v30.md` and `params/combat.md` for combat. Cite from the appropriate file in the ledger. Do NOT update canonical_sources.yaml in this session — that is a separate editorial task (open item for Jordan: realign registry `design_doc` fields).

Same applies to `derived_stats` (registry → `params/factions/stats_1_7_scale.md`; section-structured doc → `designs/scene/derived_stats_v30.md`).

---

## Module table

Module 0 = manifest + ledger + gates. Modules R1–R10 = the residual risks. Each marked `pending` / `in-progress` / `verified`.

| # | Name | Mode | Depends On | Canonical sources (full-depth fetch required) | Decision shape | Status |
|---|------|------|------------|-----------------------------------------------|----------------|--------|
| 0 | Manifest + ledger + gates | — | — | (this file) | gate cleared | in-progress |
| 1 | R1 Wound permanence | B + D | M0 | `designs/scene/derived_stats_v30.md §4.1 Health (PP-716)`, `designs/scene/combat_v30.md §7`, `params/combat.md §wounds`, `designs/scene/fieldwork_v30.md §5.6b Knot Lifecycle`, `params/fieldwork.md §knot` | yes (catastrophic-Wound criteria) / no (preserve canonical) / partial (Knot-tagged subset) | **verified v2 — recommend C1.3** (v1 superseded; v2 built on PP-716) |
| 2 | R2 Skill input layer in C | A + D | M0 | `designs/scene/combat_v30.md §1 Combat Pool`, `designs/scene/combat_v30.md §B (proposed) Duel`, `params/combat.md`, synthesis `05_q4_q5_q6.md §Q4 E5/E7` | pure dice / cap +1 / cap +2 / no cap | **verified — recommend C2.1 (pure dice); C2.2 fallback** |
| 3 | R3 Mass three-mode reframe | A coverage + D | M0 | `designs/provincial/mass_battle_v30.md §A (TTRPG)`, `§B (Board)`, `§D (World Bridge)`, `params/mass_combat.md` | full reframe / partial / preserve | **verified — recommend C3.3 (preserve + phase-mapping table); synthesis premise partially obsolete (TTRPG/Hybrid merger already done 2026-04-17)** |
| 4 | R4 Hero participation default | A + B | M0, M3 | `designs/provincial/mass_battle_v30.md §B.5 Hybrid Handoff`, `§D.2 Named officers`, `designs/architecture/scale_transitions_v30.md`, `params/scale_transitions.md` | default-on / default-off / context-sensitive | pending |
| 5 | R5 Wager stake range | A + B | M0 | `designs/scene/social_contest_system_v2.md §6.1.1 Wager`, `params/contest.md`, `designs/scene/conviction_track_v30.md` (post-rename = piety/persuasion), `params/factions/stats_1_7_scale.md §Reputation` | stake-type table + range table + cross-system effect table | pending |
| 6 | R6 Fibonacci cap at high N | A | M0 | `designs/scene/combat_v30.md §8 Fibonacci`, `params/combat.md` | cap=8 / cap=N>8 / no-cap asymptote | pending |
| 7 | R7 Friendly fire & ranged in melee | A + D | M0 | `designs/scene/combat_v30.md §5 Reach/Zone/Cover`, `designs/scene/combat_v30.md §6 Ranged`, `params/combat.md` | no FF / FF on miss / FF separate roll / FF on stress/wound | pending |
| 8 | R8 Fieldwork ↔ combat tempo shift | B | M0 | `designs/scene/combat_v30.md §11.5 Combat↔Fieldwork`, `designs/scene/fieldwork_v30.md §Exposure`, `designs/scene/fieldwork_exposure.md`, synthesis `05_q4_q5_q6.md §Q6 F2+F3` | full freeze / partial / continuous | pending |
| 9 | R9 Two-architecture sufficiency | A coverage | M0 | `designs/scene/combat_v30.md §5 Reach/Zone`, synthesis `05_q4_q5_q6.md §Q5`, `04_q3_scene_mass.md §I-candidates` | A+C sufficient / restore B for [shapes] | pending |
| 10 | R10 IP-gauge actor-count threshold | A | M0 | `designs/scene/combat_v30.md §2 Phase round structure`, synthesis `02_q1_timeshape.md §T2/T4`, `designs/provincial/mass_battle_v30.md §A.7` | full / collapsed at N / hidden at N | pending |

---

## Per-module session protocol

Each R-module follows the Mode G per-module protocol with these per-module specifics:

1. **Bootstrap** + verify Module 0 ledger entries exist.
2. **`task_gate('simulation')`** — already cleared this session, but re-asserted at module start.
3. **Read manifest from GitHub** to confirm dependencies.
4. **Fetch canonical sources** at FULL depth (`force_full=True`); verify with `read_depth_report`.
5. **Verification ledger entries** for every constant the module uses. Format:
   ```json
   {"sim_variable": "wound_interval", "value": 3, "canonical_source": "designs/scene/combat_v30.md", "section": "§4 Wound Interval", "quoted_text": "..."}
   ```
   `quoted_text` must appear verbatim in the fetched canonical content.
6. **`sim_gate('custom', systems=[<systems touched this module>])`**.
7. **Apply NERS at full grain** to each candidate option (24 cells per).
8. **Mode A/B execution** with state tracking format from SKILL.md.
9. **Mode D exhaustive** across 9 edge-case categories.
10. **Decision-shaped finding statement** at module end.
11. **`safe_commit()`** — module file + manifest with status update + ledger snapshot.

---

## System keys for `sim_gate`

Per `references/canonical_sources.yaml`, valid system keys touched across modules:

- `combat` (R1, R2, R6, R7, R9, R10 — uses `params/combat.md`; supplement with `designs/scene/combat_v30.md`)
- `mass_combat` (R3, R4, R10 — `designs/provincial/mass_battle_v30.md`; SHA pending PP_705)
- `scale_transitions` (R4, R8)
- `derived_stats` (R1 — Vitality reference)
- `social_debate` (R5 — wager via social_contest)
- `factions` (R5 — Reputation track)
- `clocks` (R5 — Piety/Persuasion track post-rename)

Sim_gate call per module declares the subset actually touched by that module's code.

---

## Probability conventions (from SKILL.md, locked)

- TN5: 0.6 / die · TN6: 0.5 · TN7: 0.4 · TN8: 0.3
- 1s subtract → P(net success per die at TN7) ≈ 0.3
- Expected net per die at TN7 ≈ 0.33
- For critical edges, exact binomial.

Pool quick-ref locked at: 4D→1.3 net, 6D→2.0, 8D→2.6, 10D→3.3, 12D→4.0, 15D→5.0 (TN7 expected).

---

## Anti-patterns flagged for this harness

Drawn from Mode G failure mode list:

- ✗ Build all 10 R-modules in one session at compressed depth → use module-per-iteration cadence; checkpoint between
- ✗ Cite section titles without full-depth read of section body → `force_full=True` required
- ✗ Invent values because they "match canonical feel" → ledger entry or skip
- ✗ Run batch over an unverified module → batch only after module status: verified
- ✗ Treat the synthesis as canonical → it is EXPLORATORY; ledger entries cite canonical sources, not the synthesis

---

## Open items to flag at session close

- canonical_sources.yaml `design_doc` field drift for `combat`, `derived_stats` — needs editorial realign (Jordan to schedule)
- PP-684 → PP-711..715 mapping for Disposition-ceiling rule — verify exact PP number when R1 module touches Knot Lifecycle
- Architecture-spec enforcement_spectrum table update from prior session still pending paste into project knowledge
- `read_active_sessions` defect — concurrent-session detection still unreliable
- VALORIA_PAT exposure from prior session — rotation still pending Jordan

---

## Changelog

- 2026-05-09 — Initial manifest. Modules 0–10 enumerated. Self-audit findings carried forward. PP-684 collision resolved. Registry drift documented.

## PP-716 supersession (2026-05-09)

The wound mechanic was substantially corrected in PP-716 after Module 1 R1 was committed. The corrections:

1. **Health formula reverted** to `(Endurance + 6) × (Max Wounds + 1)`, where `Max Wounds = floor(Endurance / 2) + 1`. ED-694's `Vitality = End × 10` formula is reverted because it did not match the WI × wound-count structure for End values 1, 2, 3, 5, 7.
2. **Wound penalty unified** as −1D Pool universally (Combat, Thread, mass-battle Command, BG-CF tactic). The previously canonical "+1 Ob per Wound" for Thread operations, mass Command, and CF Zoom-In is now reverted.
3. **Authoritative source** is now `designs/scene/derived_stats_v30.md §4.1` (rewritten as canonical Health spec).

Module 1 R1 (`r1_wound_permanence.md`, committed 45c693e2) was authored against the now-superseded canon. It carries a SUPERSEDED banner. Its decision-shape recommendation (C1.3) was based on:
- Pool floor 5D asymmetry under permanent-wound accumulation (still applies — Combat Pool floor unchanged).
- Threadwork +1 Ob per Wound unfloored producing practitioner extinction cascade (no longer applies — wounds now give −1D Pool with floor protection, not +Ob).

The R1 redo against PP-716 canon may produce a different recommendation. Plan: redo R1 in a subsequent session, save as `r1_wound_permanence_v2.md`, mark v1 superseded.

Modules 2–10 remain pending and will use PP-716 canon from the start.

## R4 verified — C4.2

## R5 verified — C5.1

## R6 verified — C6.1

## R7 verified — C7.4 primary; C7.1 fallback

## R8 verified — C8.2
