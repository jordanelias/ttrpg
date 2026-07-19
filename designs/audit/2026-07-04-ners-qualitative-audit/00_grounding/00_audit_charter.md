# Qualitative NERS Audit — Charter (read this first)

## Status: RATIFIED (Jordan, 2026-07-05 — accepted as filed; post-merge instruction on PR #77)
## Date: 2026-07-04 · Lane: IN (cross-cutting) · Session branch: `claude/ners-audit-fable5-9cpfdz`

## THE NORTH STAR

**Valoria is to be a Godot emergent grand-strategy · tactical-management · political-simulation ·
narrative RPG in which every subsystem points toward an emergent-narrative player experience with
rich, meaningful choices through myriad options and decisions.**

Every judgment in this audit answers one master question, asked of every subsystem, every
interdependency, every juncture:

> Does this widen the space of meaningful player decisions and feed the collision engine that
> produces emergent narrative — or does it collapse choice (degenerate play), exist for its own
> sake (unnecessary), fragment the experience (incohesive), or generate state no narrative
> surface ever renders (inert)?

## Criteria (the corpus's own instruments — do not invent new ones)

This is a **qualitative** audit. Do NOT bind to the rolling-engine mechanical framework
(`valoria-resolution-diagnostic` P-i..P-v) or any strict engine documentation.

- **Intent-of-game** (`references/throughlines_meta_infill.md` §1): "a positive feedback loop
  between player decisions and mechanics that produces an engaging game world with emergent
  narratives."
- **Ω-Intent, 4 clauses** (`references/throughlines_meta.md`, PP-672/PP-674): cross-scale
  consequence · personal transformation · autonomous world · **non-dominance** (no solvable
  strategy).
- **Q-robust / Q-smooth / Q-elegant** (same doc, tier 5 — Claude-owned; Q-fail = iterate, not
  reject). Includes the **dramatic-legibility test**, the canonical playability bar: from the
  screen, answer in one sentence each — *whose position is at risk; what does each named actor
  want; what happens if no one acts next season.*
- **N-Necessity** (tier 0 — Jordan-owned: **flag, never auto-reject**): models a real,
  load-bearing dynamic of Renaissance-era political leadership; complexity only when grounded in
  subject matter.
- **The throughlines tree** (`references/throughlines_complete.md`: Μ causal modes / М structural
  meta-patterns / Τ 41 concrete throughlines). Cross-system **collisions are canonically "the
  game's emergent narrative engine."**
- Philosophy gates: `canon/02_canon_constraints.md` P-01..P-15 + GD-1..GD-3 (esp. **P-14**:
  inseparability must be expressed in every play mode — the threadwork bar).
- Qualitative-NERS ancestor (equivalent content for R/S/E): NRSE all-directions framework,
  `references/simulation_workplan_v1.md` §2.1. Note: `canon/definitions.yaml` does NOT exist
  (stale skill citation).

## Method disciplines

1. **Working tree only.** Read local files; never GitHub API; never memory. Cite `file §section`
   for every claim, else tag `[UNGROUNDED]`.
2. **All directions.** Judge along six axes and tag findings with a `direction`:
   **top-down** (philosophy → mechanic) · **bottom-up** (primitives/sim/params → design claims) ·
   **lateral** (sibling subsystems, same scale) · **diagonal** (cross-scale/cross-system) ·
   **forwards** (workplan/roadmap → Godot end-state sequencing) · **backwards** (supersession
   lineage, stale citations, resumed-from-superseded risk).
3. **Shape & sequence artifacts are first-class inputs**: `canon/mechanics_index.yaml`,
   `canon/supersession_register.yaml`, `canon/03_canonical_timeline.md`,
   `canon/patch_register_active.yaml`, `references/canonical_sources.yaml`,
   `references/module_contracts.yaml`, propagation maps + throughlines registries under
   `references/`, `references/roadmap_state.yaml`, `designs/workplans/valoria_master_workplan_v5.md`,
   `tools/observability/DECISIONS.md` + `decisions.json`, `tests/coverage_matrix.md`,
   `references/id_reservations.yaml`, `handoffs/HANDOFF_<LANE>.md`.
4. **Threadwork at every juncture.** For your territory, verdict each juncture: threadwork
   **present** (cite) / **absent-but-plausible** (state the natural interaction) /
   **absent-deliberate** (cite intent evidence). P-14 is the bar.
5. **Adversarial, no false balance.** Verdict first; severity-ranked; every candidate finding gets
   an intent gate (DELIBERATE / NOT-INTENDED / UNDETERMINED — don't guess). Self/prior-session
   work gets no deference.
6. **Qualitative severity**: P1 = blocks or actively undermines the North Star; P2 = materially
   narrows choice/legibility/cohesion; P3 = friction/debt.

## Calibration — KNOWN items (re-reporting these as novel discoveries is an audit failure)

Tag findings `KNOWN-TRACKED` (has an ED / HANDOFF / decision-queue entry), `KNOWN-UNTRACKED`
(documented somewhere but no tracking artifact), or `NEW`.

- Spear/polearm dominance in personal combat (84–96%) — KNOWN; R2 closing-distance redesign
  MERGED (PR #72), R3 weapon-model consolidation in flight (PR #76).
- `combat_engine_v1` has no threadwork interface — KNOWN, **ED-911 (open, P1)**.
- Threadwork open items: ED-1010 (per-op Coherence cap homeless), ED-1011 (Coherence-0 → NPC
  transition split), ED-913 (Thread-Read stale attribute), ED-414 (Debate co-movement timing),
  ED-931 (dangling clock-registry path).
- `module_contracts.yaml`: 10 modules doc:null (incl. `domain_actions`, `engine_clock`), 11
  [ASSUMPTION]-grade resolvers — KNOWN (ED-1051 backlog, contract-conformance CI report-only).
- Orphan/thin modules — KNOWN via module_contracts gap_notes: `ci_political`,
  `territorial_piety`, `clock_registry`, `victory` (unowned MS clock), phantom
  `settlement_economy`, stub `campaign_architecture`.
- `values_master.yaml` QUARANTINED (ED-1084); Combat Pool collapsed to `max(5, History+6)`
  across live sites (ED-1084) — verify current state before claiming divergence.
- Sim balance has a known degenerate seeded win-share (one faction ~87%) with no regression
  oracle beyond the smoke test — KNOWN (CLAUDE.md §7).
- Godot port: skeleton non-compilable, 1/27 modules, Gate-0 unexecuted — KNOWN (CLAUDE.md §6).
- The frozen 23-item Jordan decision queue:
  `designs/audit/2026-07-01-month-overview-architecture-consolidation/` — check it before
  calling something undecided.
- Recent infra (live context, not discovery): ED-1081..1087 consolidation, holonic doctrine
  ED-1083, propagation spec ED-1093, merge-ratifies convention ED-1094, typed engine-params
  export + round-trip CI, freshness gate blocking, social-contest rebuild Stages 0–3 done
  (Stage 4 next).

## Companion grounding files (read the ones your lane needs)

- `01_criteria_ners_lineage.md` — full criteria lineage + prior audit report format.
- `02_interdependency_map.md` — cross-subsystem edge list, module-contract state, scale spine.
- `03_threadwork_surface.md` — threadwork mechanics, declared + silent junctures, spec drift.
