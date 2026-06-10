# Valoria — Workplan R2
**2026-06-09 (evening) · supersedes `valoria_delta_workplan_2026-06-09.md` (same-day session artifact, not separately committed; consolidated here)**
status: proposed · as_of: ttrpg@26b5ecee (latest observed HEAD this session) · binds_to: `designs/audit/2026-06-06-architecture-map/valoria_master_workplan.md` (Jordan-approved)
provenance: produced in-session from the 06-09 reconciled report + four subsequent evaluation/adversarial/reconciliation rounds; [SELF-AUTHORED — bias risk] acknowledged; Jordan-vetoable throughout.

---

## §0 — Operating constraints (the feasibility frame)

- **One operator.** Jordan, solo, with Claude doing coding, maintenance, and collaborative content infill, over GitHub. The currency of every estimate below is **sessions**, not days.
- **WIP limit: one infrastructure item in flight at a time** (proposed default; Jordan-adjustable). Infrastructure sessions alternate with design/content sessions — infrastructure serves iteration and must never displace it for more than one session at a stretch.
- **Per-system rituals over upfront builds.** Game-side quality mechanisms (exports, parity scenarios, property checks) ride along with each system as it is implemented — never as a standalone infrastructure phase. This is the structural answer to "too much infrastructure blocks iterative work."
- **Budget rule (carried from this session's reconciliation):** no new structural proposals advance while K-1/K-2/K-3 remain unbuilt. Escalation-path items build only on their named trigger.
- **Allocation:** hooks detect · the model interprets · Jordan decides.

## §1 — Model & capability note (adjusted)

Workflow targets **the latest Opus** (Opus 4.8). `references/ecosystem_versions.yaml` already pins `opus-4.8` with `tokenizer_factor 1.35`, and W0.1's `context_gate` recalibration was performed against that tokenizer — **the pin is current for the declared operating model**; the prior turn's "stale pin" precondition is withdrawn as stated. Residual (one line, rides with T3): note in `ecosystem_versions.yaml` that sessions may occasionally run on adjacent newer models (this session ran on one), and that `context_gate` therefore stays calibrated conservatively (undercount direction is the dangerous one). Every item below is sized to single-session execution on Opus-class capability (1M context, Code Interpreter, GraphQL commits, hooks, skills) under the existing `<tool_call_granularity>` staging discipline. No item depends on capabilities beyond that.

---

## PHASE A — Coordination + the every-session keystone (~2 sessions)

| ID | Item | Notes |
|---|---|---|
| A-1 | Reconcile the **2 stale** handoffs (06-04 active-work-index, 06-05 weapon-physics) into the master — strike the false 94-ID backlog + IDR; archive via `archive_handoff`. The **third** active handoff (`win-computation-victory-2026-06-09`) is current and stays active | Overdue; was T1. Count verified live this session (3 active; it was 2 at this morning's bootstrap — the moving count is itself the as-of lesson). While touching the handoff template: add an `as_of: <SHA>` header line to `write_handoff` output so handoff staleness becomes mechanically visible. Template change, not a mechanism. |
| A-2 | Confirm one green CI run in each repo | Was T2. One API check per repo. |
| A-3 | Roadmap micro-reconcile + the §1 ecosystem-versions note | Was T3. |
| A-4 | **K-1: build `report_open_items()` (W1.1)** — co-scheduled with its dependents **W1.2** (Status-Block decision-aging) and **W1.8** (roadmap auto-feed), both `blocked_by W1.1` in the master, in the same build | The one build that pays every session: bootstrap reports open decisions with age, handoffs behind HEAD, drift warnings, register state — one computed answer to "where are we." Three register items, one build session — dependency-respecting co-scheduling, not a register amendment. |

## PHASE B — Freshness + derived graph (~1–2 sessions)

| ID | Item | Notes |
|---|---|---|
| B-1 | **K-2: freshness SHA-split** → `canonical_freshness.yaml`, exactly as approved (W1.9) | Unchanged from master. Relieves the `canonical_sources.yaml` cap. |
| B-2 | **Derived-graph extraction** (sibling to K-2, time-boxed to one session): index pipeline harvests dependency edges from existing signals — commit `Citations:` blocks, co-file rules, code imports — and K-1's report gains a staleness section ("X moved; Y cites X; Y unmoved since") | No authored metadata; the graph is extracted, not declared. **Stop rule:** if extraction precision is poor on real queries, ship staleness-only and stop — poor precision is the trigger for the front-matter escalation path, not a reason to build it now. |
| B-3 | Land the M4 citation soft-warn (`pre_commit_gate`, non-halting) — **= W1.12** (register-carried, P2) | Was S-6 / audit 3.2. Verified **unbuilt** in live hooks this session (whole-file scan; the morning report's contrary claim is corrected). Tiny; becomes load-bearing as B-2's data source — citing inputs is what makes your impact set visible. |
| B-4 | JSON Schema for the hand-authored stores (ledger JSONL + the 1–2 authored YAML registries), validated in CI | Rides along with B-1's store work; generated stores are excluded (regeneration is their validation). |

## PHASE C — Lifecycle, minimal form (~1 session)

| ID | Item | Notes |
|---|---|---|
| C-1 | **K-3, precise:** build **W1.6 exactly as approved** (supersession-citation check — cite a superseded_id → warn); **W1.7 trimmed** to one status vocabulary across artifact classes + `superseded_by` required when status=superseded | **W1.7 trim APPROVED — Jordan, 2026-06-09.** The full "lifecycle state machine wired to commit primitives" is amended to the two pieces a solo operator exercises (one status vocabulary + required `superseded_by`); full transition-legality enforcement moves to an escalation path (trigger: a transition error actually occurs). W1.6 builds exactly as approved, untouched. |
| C-2 | ED-867 supersession markers | Was L-3; rides on C-1's vocabulary. |
| C-3 | Fresh-context review as **soft policy, not gate**: canonical promotion of `canon/` files and hook code *recommends* a separate-session pass (`reviewed_by` field, soft-warn if absent) | Demoted from gate per feasibility — a mandatory two-session cycle on every promotion is friction a solo operator will route around. Honestly named: fresh-context review (kills context anchoring), not independent review. |

## PHASE D — Legibility + text paydown + creative gate (~1 session, mostly mechanical)

| ID | Item | Notes |
|---|---|---|
| D-1 | Execute the `designs/audit/` promotion (git mv live design work out; repoint co-files) | Was L-1; Jordan's 2026-06-05 flag. |
| D-2 | Clear the 2 index-drift orphans; PI text fixes (bootstrap/manifests naming — `.jsonl` vs deleted `_summary.yaml`); finish the **W0.6** B6-strike corpus sweep | Was L-2 + D-1 + D-2 of the morning plan, one pass. The morning plan's "M4 → built" PI edit is **cut** — verification shows the PI's M4 text is already correct. |
| D-3 | **Creative-tier path gate, soft-warn — mechanism APPROVED, Jordan, 2026-06-09.** Hook warns on session edits under creative/narrative path prefixes *absent explicit Jordan direction in-session* | Directory-prefix rule, not a front-matter field. Soft-warn, not block — collaborative content infill under Jordan's direction is the workflow; what it catches is Claude *initiating* creative changes as a side effect of mechanical work. **Prefix set: see the D-3 block below** — the unambiguous-creative prefixes are confirmed; four mixed-boundary cases await Jordan rulings before the gate ships. |

### D-3 — creative-tier prefix set (grounded in `ttrpg@main` tree walk, 2026-06-09)

**Confirmed creative-tier** (soft-warn applies; narrative / character / world / metaphysics — Claude does not initiate edits here absent Jordan direction):
- `designs/world/` — worldbuilding, geography, character histories, Solmund corpus, southernmost, calamity (22 files)
- `designs/npcs/` — character canon + NPC analyses (18 files)
- `designs/arcs/` — narrative scenario chains, arc analysis (39 files)
- `canon/00_philosophical_foundations.md`, `canon/00_philosophical_foundations_rules.md`, `canon/01_foundations_amendment_self_rendering.md`, `canon/02_foundations_amendment_leap_mechanism.md`, `canon/03_canonical_timeline.md` — metaphysics + timeline

**Explicitly NOT creative-tier** (regex false-positives ruled out by content/role): `params/history/*` (mechanical param patch-histories), `sim/world/*` (simulation code), `designs/audit/*` (audit artifacts *about* creative content, not the content), `canon/02_canon_constraints.md` + ledger + registers + `mechanics_index.yaml` (mechanical).

**Four mixed-boundary cases — [OPEN — Jordan rulings] (gate does not ship until ruled):**
1. `designs/articulation/articulation_layer_v30.md` — the articulation *layer* is a mechanical system spec, but its subject is omniscient-voice narrative generation. Gate it as creative, mechanical, or split?
2. `designs/threadwork/threadwork_philosophical_reference_v30.md` (+ `_infill`) — a creative philosophical-reference file inside an otherwise-mechanical `threadwork/` dir. Per-file creative, dir stays mechanical?
3. `designs/personal/character_generation_questionnaire_v30.md` — single character-content file in a mechanical dir. Per-file creative?
4. `skills/prose-writer/` — voice/tone/literary tooling (a skill, not canon content). Include in the creative gate, or leave to skill governance?

## PHASE E — Implementation foundation as per-system ritual (begins alongside, not after, A–D)

**Foundation choices** (cost nothing extra if made at the start of game-side work, ~1 setup session total):
- Engineering floor in `valoria-game`: enforced static typing + gdlint/gdformat + gdUnit4 + CI extension for headless test runs.
- Kernel written **scene-tree-free and headless-runnable** from day one; regimes behind a strategy registry; one injected seeded RNG.
- Scale/phase flow as an explicit statechart; cross-system effects through a typed event bus (events are past-tense facts; commands are direct calls down the dependency direction).
- First, verify the standing `[GAP]`: how does the game currently source canon values? If hand-transcription → adopt the export ritual below.

**The ritual each implemented system carries** (rides with feature work; no standalone phase):
1. A generated, generator-stamped export of its canonical parameters (one file per system; the general pipeline *emerges* from accumulated instances, it is not built first).
2. One golden-master parity scenario: seeded inputs → Python-sim fixture → headless GDScript run asserts agreement.
3. Property checks encoding the applicable lessons (monotonicity, bounded loop gain, impact-uniformity tolerance, no-cliff on continuous resources).
4. Keys discipline: namespaced StringNames; retired keys alias-with-warning.

First target system: Jordan's choice (combat-v32 remains Jordan-gated for ratification; the ritual applies to whichever system goes first).

---

## DEFERRED (opportunistic; no scheduled slot)
S-1 session-log D5 completion (W1.10) · S-2 CI documentation (W1.11) · S-5 R2 emit-type hook (W1.3) · W1.14 kernel+3-regimes doc-adoption pass (dispatcher reification stays per K8 commission terms) · R-1 registry consumer-trace → R-2 retire the 3 legacy index generators → R-3 consolidate orphaned registries (when R-2 runs, add the scoped tombstone check to CI: fail on *code imports* of tombstoned paths — prose mentions excluded) · reachability report (fold into index pipeline when next convenient).

## TRIGGERED (build nothing until the trigger fires)
Front-matter metadata ← B-2 extraction precision fails real queries · ID-addressing / stable-filenames-at-next-major ← filename churn actually bites · sim↔telemetry calibration contract ← playtest telemetry exists · TimeAuthority as separate module ← a second consumer of time · input-language schema ← extracted from the bus when parity work begins · full lifecycle transition enforcement ← a transition error occurs.

## DROPPED (recorded so they stay dropped)
`owner_tier` front-matter field (path rule supersedes) · blanket review gate · impact-set scheduler as built mechanism (B-2 detects; the model interprets) · upfront command grammar · canon-in-database · full ECS · object pooling · session locking · monorepo unification (Jordan call if ever; not architecture-forced).

## PRINCIPLES (Level-1 text in the architecture spec; explicitly *not* claimed as enforcement — the V2.4 lesson)
1. **Checkability-or-expiry:** durable artifact classes need a mechanical validator; ephemeral classes auto-expire. Neither validator-less durables nor immortal ephemera.
2. **Acyclic knowledge flow:** canon → designs → params → sims → exports → game; downstream regenerates; upstream moves only through explicit decision events (`decision_refs`).
3. **Kernel closed, data open:** new mechanics enter through registries/data + at most one strategy class; kernel diffs cite a decision.
4. **Resume-from-repo:** any operation >1 block externalizes state so a fresh session resumes from repo + checkpoint alone.

## CARRIED — Jordan docket (unchanged, untouched, ungated by this plan)
F1 Mandate-echo calibration · C2 scene.thread_operation form · Composure name (Charisma vs Presence) · OWN-4 insurgency dissolution · OWN-5 defection cascade · combat-v32 ratify · ED-868 collapse-loop bound · D6 unified scope set (decision → then mechanical D-pass) · Resonant Styles define-or-vestigial · filename-versioning convention (lockfile trade-off, surfaced this session) · Python-sim long-term role (spec oracle vs retire post-implementation — shapes Phase E ritual depth).

## SEQUENCE
Infra slots: **A → B → C → D**, one item in flight, alternating with design/content sessions throughout. **Phase E starts whenever implementation work resumes — it does not wait on B–D** (only A-1/A-4 meaningfully improve every session and are worth doing first). Total infrastructure: **~5–7 sessions**, amortized; everything else rides with the work it serves.
