# Stub Infill Plan — sim/ Implementation Roadmap
**Draft · 2026-05-19 · proposed for Jordan ratification**

## Summary

The `sim/` tree has **45 stub modules** raising `NotImplementedError`, against **17 implemented modules** (plus 1 partial, `sim/personal/tribunal.py`). The implemented subset is concentrated in `sim/provincial/` (mass battle + Crown/Church faction-unique actions) and `sim/autoload/` (game state + dice engine + victory check). Everything else is armature.

This means current `mc_v18.run_batch()` runs only exercise: Crown Initiative dispatch, Church Excommunication/Council/Absolution, generic Conquest, generic Muster, generic Govern, mass battle execution + accounting. It does **not** exercise: any scene-scale combat or social contest, any threadwork operation, any insurgency, any infrastructure-mediated mechanic, any settlement-scale state, any Varfell or Hafenmark faction-unique action, any cross-scale articulation, any NPE / miraculous event, any peninsular CI/IP/MS/RS clock advance, or any of the 5 deferred Pass 2 Church/Hafenmark/Varfell territorial actions.

**Game-balance claims are not currently valid output from the sim.** Pass 2d (Varfell) and Pass 2e (Hafenmark) faction-side authoring + the contamination audit block ~10 of the 45 stubs at the canon layer. The remaining 35 are implementable against existing canon if the dependency order is respected.

## Inventory by domain layer

| Layer | Stubs | Notes |
|---|---|---|
| `sim/` (root) | 1 | `__init__.py` |
| `sim/autoload/` | 1 | `npc_ai.py` only; dice / state / season / scene / registry / victory implemented |
| `sim/cross_scale/` | 4 | articulation, domain_echo, handoff_rules, zoom_in_out |
| `sim/peninsular/` | 5 | ci_track, ip_track, ms_track, rs_track, season; `accounting` is implemented |
| `sim/personal/` | 10 | beliefs, combat, companion, contest, conviction, fieldwork, investigation, knots, parliamentary_stay, parliamentary_vote; `tribunal` is partial-impl |
| `sim/provincial/` | 10 | altonian_reinforcements, charter_liberties, hafenmark_equipment, home_sanctuary, infrastructure_reclamation, mass_seizure, parliamentary_transfer, treaty, varfell_mandate_action, varfell_territorial_acquisition |
| `sim/territory/` | 3 | infrastructure, settlement, temperaments; `adjacency` is implemented |
| `sim/thread/` | 7 | co_movement, coherence, collective, operations, opposing, rendering, threadcut |
| `sim/world/` | 4 | insurgency_pipeline, miraculous_event, npe, restoration_movement |
| **Total** | **45** | |

## Canon-availability blockers

Four stubs cite canon files that don't exist in `designs/`:

| Stub | Missing canon | Action |
|---|---|---|
| `sim/provincial/altonian_reinforcements.py` | `designs/provincial/altonian_reinforcements_v30.md` | Author canon first (Pass 2e Hafenmark scope) |
| `sim/provincial/home_sanctuary.py` | `designs/provincial/home_sanctuary_t9_v30.md` | Author canon first (Pass 2f Church scope) |
| `sim/provincial/infrastructure_reclamation.py` | `designs/provincial/infrastructure_reclamation_v30.md` | Author canon first (Pass 2f Church scope) |
| `sim/world/restoration_movement.py` | `designs/provincial/restoration_movement_v30.md` | Author canon first (Pass 2d Varfell scope) |

Plus `sim/provincial/hafenmark_equipment.py` declares canon "(pending — hafenmark_equipment_v30.md not yet authored)" inline. So **5 stubs total** are blocked at canon.

These cannot be infilled until the canon-authoring passes complete. Per `sim/provincial/__init__.py` the contamination audit is the upstream gate.

## Dependency graph

Most-depended-upon implemented modules (these are stable foundations):

| Dependents | Module |
|---|---|
| 16 | `sim/autoload/game_state` |
| 11 | `sim/autoload/dice_engine` |
| 3 | `sim/territory/infrastructure` (stub) — bottleneck |
| 3 | `sim/thread/coherence` (stub) — bottleneck |
| 4 | `sim/personal/conviction` (stub) — bottleneck |
| 4 | `sim/thread/operations` (stub) — bottleneck |

**One genuine cycle** in stub-to-stub deps: `sim/personal/beliefs.py ↔ sim/personal/conviction.py`. Both modules must be drafted and landed in a single session, with mutual imports declared at the bottom of one of them.

## Tiered infill order

Tiers correspond to dependency depth. Tier 0 stubs have all dependencies satisfied by currently-implemented modules and can be built immediately. Each higher tier requires the prior tier to land first.

### Tier 0 — 11 stubs, ready immediately

| Stub | Canon | Why first |
|---|---|---|
| `sim/__init__.py` | (declarations only) | Trivial; module-list update |
| `sim/territory/settlement.py` | `designs/territory/settlement_layer_v30.md` | Unblocks `infrastructure`, `temperaments` |
| `sim/thread/coherence.py` | `designs/threadwork/threadwork_v30.md` Part 3 | Unblocks `operations`, `threadcut` |
| `sim/cross_scale/handoff_rules.py` | `designs/architecture/scale_transitions_v30.md` §3 | Unblocks `combat`, `operations` |
| `sim/peninsular/ms_track.py` | `params/core.md` §MS Baseline Decay PP-255 | Standalone clock |
| `sim/peninsular/season.py` | `designs/architecture/campaign_architecture_v30.md` | Standalone driver |
| `sim/provincial/treaty.py` | balance audit memo §faction_balance | Standalone provincial action |
| `sim/provincial/charter_liberties.py` | `faction_canon_v30.md` §6 | Standalone Hafenmark action |
| `sim/provincial/varfell_mandate_action.py` | balance audit §part10 | Standalone Varfell action |
| `sim/world/insurgency_pipeline.py` | `canon/02_canon_constraints.md` §B GD-3 + insurgency design | Standalone world event source |
| `sim/world/npe.py` | `designs/scene/investigation_systems_v30.md` (NPE) | Standalone — unblocks investigation |
| `sim/cross_scale/zoom_in_out.py` | `scale_transitions_v30.md` §4 | Standalone, ties scale views |
| `sim/cross_scale/domain_echo.py` | `scale_transitions_v30.md` §5 | Step 10.1 from Phase 7 follow-on |
| `sim/autoload/npc_ai.py` | `complete_systems_reference.md` Part 1 | Standalone — separate AI |

**14 stubs in Tier 0** (counted some boundary cases). Realistic scoping: one stub per session = 14 sessions; or batch by domain layer (`provincial` = 3 sessions for treaty + charter_liberties + varfell_mandate; `cross_scale` = 1 session for handoff_rules + zoom_in_out + domain_echo) = ~7 sessions.

### Tier 1 — 13 stubs, depend on Tier 0

- `sim/territory/infrastructure.py` (needs settlement) — **critical path**, blocks Church work
- `sim/territory/temperaments.py` (needs settlement)
- `sim/personal/conviction.py` + `sim/personal/beliefs.py` (cyclic pair — single session)
- `sim/thread/operations.py` (needs coherence + handoff_rules)
- `sim/world/restoration_movement.py` (needs insurgency_pipeline) [BLOCKED on canon authoring]
- `sim/personal/combat.py` (needs handoff_rules)

### Tier 2 — 10 stubs

- `sim/peninsular/ci_track.py` (needs infrastructure)
- `sim/personal/contest.py` (needs conviction + beliefs)
- `sim/personal/knots.py` (needs coherence + conviction)
- `sim/thread/co_movement.py`, `collective.py`, `threadcut.py` (need operations)
- `sim/thread/opposing.py` (needs operations + knots)
- `sim/provincial/infrastructure_reclamation.py` (needs infrastructure) [BLOCKED on canon]
- `sim/provincial/mass_seizure.py` (needs ci_track + infrastructure)
- `sim/provincial/varfell_territorial_acquisition.py` (needs temperaments + restoration_movement)

### Tier 3 — 6 stubs

- `sim/cross_scale/articulation.py` (needs knots + beliefs)
- `sim/peninsular/ip_track.py` (needs altonian_reinforcements) [conditional on canon]
- `sim/peninsular/rs_track.py` (needs rendering)
- `sim/thread/rendering.py` (needs rs_track — possible circular, audit on infill)
- `sim/personal/parliamentary_vote.py` (needs contest)
- `sim/personal/fieldwork.py` (needs investigation + conviction)
- `sim/personal/investigation.py` (needs fieldwork + npe — may have cycle, audit)

### Tier 4 — 4 stubs

- `sim/personal/parliamentary_stay.py` (needs parliamentary_vote)
- `sim/provincial/parliamentary_transfer.py` (needs parliamentary_vote)
- `sim/personal/companion.py` (needs contest + fieldwork)
- `sim/world/miraculous_event.py` (needs rendering)

### Tier 5 — canon-gated (cannot start until canon lands)

- `sim/provincial/altonian_reinforcements.py` (Pass 2e)
- `sim/provincial/home_sanctuary.py` (Pass 2f)
- `sim/provincial/infrastructure_reclamation.py` (Pass 2f) — already in Tier 2 by deps but canon-blocked
- `sim/provincial/hafenmark_equipment.py` (canon not yet authored)
- `sim/world/restoration_movement.py` (Pass 2d) — already in Tier 1 by deps but canon-blocked

## Per-stub session protocol

For each stub, the session protocol per `skills/valoria-simulator/SKILL.md` Mode G:

1. `quick_bootstrap()`; `task_gate('simulation')`.
2. `read_files_graphql([canon_path], force_full=True)` — full read of every canonical source declared in the stub's docstring.
3. Verify deps: every `Dependencies:` listed module must be implemented (not stub). If a dep is still a stub, halt — wrong tier.
4. Build the verification ledger entry for every new constant introduced. Append to `tests/sim/v18-integration/sim_verification_ledger.json`. Each entry: `sim_variable`, `value`, `canonical_source`, `section`, `quoted_text` (verified present in fetched canon).
5. `h.sim_gate(...)`.
6. Replace stub body. Preserve `Dependencies:` / `Entry points:` docstring. Add `[canonical: path §section]` inline comments at every mechanical constant. Remove `[PROVISIONAL — Pass 2l armature stub]` status marker; replace with `[implemented: 2026-MM-DD]`.
7. Test in isolation: smoke runs against known inputs; output logged.
8. `h.safe_commit()` with the stub file + manifest + ledger updates. Single stub per commit unless the cycle pair forces 2.
9. Update `tests/sim/v18-integration/module_manifest.md` status row from `pending` / `stub` to `verified`.

## Scope-of-session rules

Per Mode G's "no multi-module code in a single session": one stub per session, with the single exception of the `beliefs`/`conviction` cyclic pair. Avoid the temptation to batch — each module's canonical read is non-trivial (multiple sections of v30 design docs).

## Verification approach

The sim's correctness is currently asserted only at the commit-message level. After each infill batch:

- **`mc_v18.run_batch(50, base_seed=0)` baseline** — record `battles_mean`, `win_share`, `season_mean`, `winner_mean`. Capture before and after each tier completes. Drift > 30% in any metric without an explanatory canon change is a regression flag.
- **Per-module unit smoke** — every entry-point function called with at minimum 3 input configurations. Output logged to the commit body.
- **Battery (when available)** — `tests/sim/battery_v22.py` if/when it exists per Step 4.2b. Run after Phase 7 Steps 4.3-4.9 complete; in-band count per §3.2 recalibration table.

**Game balance claims become valid only after Tier 0 + Tier 1 + Tier 2 land** (the core territorial/threadwork/conviction loop), and only against scenarios that don't depend on canon-gated modules. Even then, balance claims need to be scoped: "Crown vs Church Excommunication interaction at full PP-233 lethality, holding Hafenmark and Varfell as fixed neutral AI" is a defensible claim; "Crown wins 40%" without scoping is not, because Hafenmark and Varfell are not playing the game.

## Open items

- **Canon authoring sequence** (Pass 2d / 2e / 2f + contamination audit) is upstream of 5 stubs. Until those land, the sim has structurally incomplete coverage. Worth deciding whether to drive Pass 2d/e/f as separate handoffs or wait.
- **`sim/personal/tribunal.py`** has one `raise NotImplementedError` despite being mostly implemented. Investigate whether this is a hot path that fires during mc_v18 runs and what it gates.
- **`sim/thread/rendering.py` ↔ `sim/peninsular/rs_track.py`** — possible circular, needs audit at first infill attempt.
- **`sim/personal/investigation.py` ↔ `sim/personal/fieldwork.py`** — possible circular, needs audit.
- The infill sequence as written totals ~45 sessions plus canon authoring. At the prior session rate (~1-2 sim deliverables per session), this is 6-12 months of work. Worth deciding which subsets actually need to land vs which can stay armature for the foreseeable game-design horizon.

## Recommendation

Before any further mass-battle balance work or claims about the sim's outputs:

1. Land Tier 0 (14 sessions or ~7 batched).
2. Land Tier 1 + the cyclic pair (~6 sessions).
3. Land Tier 2 critical-path: `ci_track`, `mass_seizure`, `contest`. Skip canon-blocked stubs.
4. Take a fresh `mc_v18.run_batch(50)` reading. Compare to today's baseline.
5. *Then* decide whether to continue infilling vs work the Pass 2d/e/f canon-authoring track.

Tier 3+ and canon-gated stubs are still important but the marginal cost of leaving them as stubs while Tier 0-2 lands is smaller than the marginal cost of running balance experiments on the current 70%-stub sim.


## Amendment 2026-05-19 — Tier 0 execution status + canon-gate reclassifications

Tier 0 work executed across commits fbc08811, 6754aadb, 1d6d616c, edff2cb0
plus one batch commit covering treaty/insurgency/npe. Status after this
work:

**Implemented (8/14 Tier 0)**: settlement, coherence, handoff_rules,
zoom_in_out, domain_echo, sim/__init__, ms_track, season, insurgency_pipeline,
npe, plus treaty (partial). Total 8 fully-verified + 1 partial.

**Reclassified to canon-gated bucket (3/14 Tier 0)**:
- **T0-8 charter_liberties** — stub cited `faction_canon_v30 §6` but that
  section is "Public Temperament", not Charter Liberties. No mechanical
  spec exists for Charter Liberties anywhere in canon. Requires Pass 2e
  Hafenmark canon authoring.
- **T0-9 varfell_mandate_action** — stub docstring explicitly notes
  "Current canon mechanism (W -1 + Mil -1 -> +1 L) flagged broken by
  Jordan 2026-05-17". Both name (placeholder VARFELL-MANDATE-ACTION-001)
  and mechanism redesign pending Pass 2d Varfell contamination audit.
- **T0-14 npc_ai** — stub docstring explicitly notes "priority-stack
  contents may contain contamination per Jordan diagnosis 2026-05-17 —
  audit pending before content authoring".

**Partial (1)**: T0-7 treaty — process_treaty_expirations implemented
against §4.5; propose_treaty canon-gated on Pass 2h
(treaty_expiration_v30.md pending).

**Updated total canon-gated count**: original plan listed 5 canon-gated
stubs (altonian_reinforcements, home_sanctuary, infrastructure_reclamation,
hafenmark_equipment, restoration_movement). Add 3 more from Tier 0
reclassification: charter_liberties, varfell_mandate_action, npc_ai.
**8 stubs total now canon-gated**; reduces implementable surface to
37 of 45 stubs until Pass 2d/2e/2f/2h/2i canon authoring lands.

**Implementation pattern observed**: nearly every Tier 0 module hit the
same wall — canon assumes a richer game_state model than exists
(Settlement registry, Practitioner registry, Knot registry, NPC registry,
Insurgency registry, Treaty registry). Module-level state stores with
ASSUMPTION/DRIFT notes are the consistent workaround; schema migration
to World is a separate workstream best done when an implemented module
needs editing for unrelated reasons.

**Recommendation**: before Tier 1, do a schema-migration commit that adds
the missing registries to game_state.World (practitioners, NPCs,
insurgencies, treaties, settlements). The Tier 0 modules' module-level
stores migrate cleanly, signatures unchanged. This unblocks consumer-side
state queries (mc_v18, Godot scene controllers) without breaking the
Tier 0 surface.
