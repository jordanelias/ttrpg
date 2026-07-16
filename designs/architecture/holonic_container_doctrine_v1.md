# Holonic Container / Wrapper Doctrine — v1

## Status: CANONICAL — ratified 2026-07-02 (Jordan, PR #55 merge-approval; ED-1083, ED-1094)

Filed PROPOSED 2026-07-01; ratified under the merge-approval-ratifies-by-default convention
adopted the same day (ED-1094) — merging a PR ratifies its PROPOSED contents unless the PR
body explicitly holds an item back. This doctrine did not hold anything back at filing.
Ratification covers the cross-map and the two named guardrails (§2); it does NOT itself
author the propagation spec (§4 — deferred to workplan v5 J-38, a separate authorship task
gated on its own review) and does not ratify the attribute roster or any other item this
doctrine explicitly deferred.

**What this is.** The architectural doctrine extracted from the 2026-07-01 workflow spec
(ingested verbatim at `designs/audit/2026-07-01-month-overview-architecture-consolidation/inputs/claude_code_emergent_game_workflow_spec.md`)
and **bound to what Valoria already has**. It names correspondences and closes enforcement
gaps; it invents no parallel system, renames nothing, and ratifies nothing that is Jordan's.

**The doctrine in one paragraph.** Valoria is a bottom-up emergent game over a nested
container/wrapper architecture: holonic — each container is at once a whole and a part — with
**one uniform canonical shape at every scale**, events propagating **up** (aggregated at each
boundary crossing) and **down** (distributed/refined), such that code is *compliant* (conforms
to the shape) and *convertible* (liftable/lowerable between scales — and between the Python
oracle, typed data, and the GDScript port — without loss). Two properties define fidelity and
are not in tension: **structure is uniform and top-imposed** (one shape at every scale);
**behaviour is bottom-up and emergent** (local rules produce play; the engine resolves
everything — no GM). The contract constrains shape, never behaviour.

---

## 1. The cross-map: spec concept → existing Valoria artifact

This is the load-bearing section. Every doctrine concept already has a (partial) home; the
doctrine's job is to make the correspondence canonical so future work strengthens one spine
instead of growing dialects.

| Doctrine concept | Existing Valoria artifact | State / gap |
|---|---|---|
| **Canonical container contract** (one shape, every scale) | `references/module_contracts.yaml` — 27 modules, uniform **Key IN → resolver → OUT** shape (schema-2); design-side enforcement via `valoria-module-adjudicator` (checks A1–A12) | Shape exists and is uniform. Gaps: 10/27 `doc: null`, 11/27 `[ASSUMPTION]` resolvers (ED-1051, open — awaiting Jordan); conformance scan now CI-wired report-only (2026-07-01) |
| **Holonic scale ladder** | `sim/` subpackages: `personal → thread → provincial → territory → peninsular → world`, with `cross_scale/` as the boundary layer and `autoload/` as shared services | Ladder is real and already holonic. `cross_scale/articulation.py` (the lift/lower seam) is stubbed |
| **Wrapper** (composes containers across a boundary) | The Key substrate (`designs/architecture/key_substrate_v30.md` + `key_type_registry_v30.md`); `KeyBus` in the Godot skeleton; `sim/cross_scale/scene_dispatch` | Upward aggregation is the established direction. **Downward delivery has no governing rule** — conversion-strategy open register #1 (ED-1006), Jordan-gated |
| **Propagation spec** (boundary transform per direction; ordering & determinism; termination/convergence guarantee) | Scattered: Key substrate (up), register #1 (down), `engine_clock` module contract `doc: null` (the temporal spine that would carry ordering) | **The highest-value unauthored canon in the repo.** Non-termination (up-event → down-event → up-event) is the scariest runtime risk. Scheduled as a workplan docket item — top-tier judgment, NOT authored here (see §4) |
| **Emergence contract** (name the local systems that produce each intended emergent behaviour; prohibit scripted shortcuts) | P-01..P-14 (`canon/`), the no-GM principle, the emergent-arc machinery (`valoria-arc-generator`), the anti-fabrication gate | Exists as philosophy + tooling; not yet per-behaviour spec. The two named failure modes below are its enforcement edge |
| **Determinism** (seeded RNG, fixed timestep, stable iteration order — emergence is debugged by replaying seeds) | `mc_v18.run_campaign(seed…)`; ED-1053 seeded regression (`sim/tests/`); Gate-0 RNG service for Godot (Jordan-gated) | Established in the Python reference; the Godot side waits on Gate-0 |
| **Convertibility = round-trip morphisms** (lift∘lower ≡ id across every adjacent pair) | **Key-log parity** — the port's master validation gate; `params/scale_transitions.md`; `references/d10_success_probabilities.json` fixture | First *mechanical* round-trip check landed 2026-07-01: `tools/export_engine_params.py --check` (oracle → typed JSON → diff). Scale-pair round-trips await `articulation.py` |
| **Deterministic conformance scan** (cheap, non-negotiable) | `skills/valoria-module-adjudicator/scripts/contract_adjudicator.py` (contract side); `tools/ci_module_shape_check.py` (code side, 2026-07-01) | Both CI-wired report-only as of 2026-07-01; graduation to blocking follows the names-drift lane pattern |
| **Tiered model roster** (spend capability where fidelity is decided) | `CLAUDE.md` §10 (haiku / sonnet / opus; fable added 2026-07-01) | Roster stays *selective* per the spec's own §7 warning: promote a role into `.claude/agents/` only after it recurs. None created at ingest |

## 2. The two named failure modes (binding guardrails for all infill work)

The spec's central observation: the model *causes* these, it does not merely miss them.

1. **Scripting drift.** The cheapest path to a working behaviour is a top-down special case
   that hard-codes an outcome meant to *emerge* from local rules. Guardrail, binding on every
   infill task (human or agent): implement the **local rule only**; touch only declared
   inputs/outputs; **never special-case an entity or an outcome to make it work.** In Valoria
   terms: nothing may write global state to force a P-01..P-14-shaped result; the
   anti-fabrication gate's spirit extends from constants to *control flow*.
2. **Shape divergence.** Asked to build containers at different scales in separate lanes, a
   model treats each as a fresh problem and emits subtly different dialects — invisible until
   a wrapper composes across a boundary. Guardrail: **the frozen shape is top-imposed**
   (module_contracts schema-2, Key IN → resolver → OUT); no scale grows its own interface
   members; no port "corrects" its oracle in place (ED-1050's rule). Conformance is
   deterministic, so it is checked by tooling, not judgment: `contract_adjudicator` (contract
   side) + `ci_module_shape_check` (code side).

**The lever these guardrails buy:** because every container is the same shape, conformance is
a schema check, not a judgment call — which is what lets volume move down-tier (Haiku/Sonnet
infill lanes) safely while top-tier judgment concentrates where fidelity is decided (the
contract, the propagation spec, the emergence audit).

## 3. Container hygiene rules (code side)

Derived from the doctrine, enforced by `tools/ci_module_shape_check.py` (report-only lane):

- **No cross-container reach-ins.** Engine/sim code must not manipulate `sys.path` or import
  from `tests/` trees. (The last live instance — `combat_engine_v1/core.py` importing σ
  primitives from `tests/sim/v32-combat-balance/` — was retired 2026-07-01 in favour of
  `sim/autoload/sigma_leverage.py`, the sanctioned shared service.)
- **Tunables live in the container's declared config.** For `combat_engine_v1`, Class-C
  coefficients live in `config.py` (the oracle) and cross boundaries only by **export**
  (`references/engine_params/`), never by re-declaration.
- **Shared services live in `autoload/`** (the ladder's service layer), not in any one
  scale's package — σ-leverage is the model case.

## 4. What this doctrine does NOT do (deferred, gated)

- **Does not author the propagation spec.** Aggregate-up/distribute-down transforms, ordering
  and determinism guarantees, and the termination/convergence condition are the hardest
  reasoning artifact in the corpus and interlock with two Jordan gates (register #1 downward
  Key delivery; `engine_clock` authorship, ED-1051). Filed as a workplan v5 §3 docket item;
  when taken up, it is top-tier-judgment work (fable/opus per CLAUDE.md §10) and lands as its
  own PROPOSED design doc beside this one.
- **Does not ratify anything.** The attribute roster stays IN FLUX; Gate-0 stays unexecuted;
  the 8-item register stays open; this doc itself is PROPOSED.
- **Does not build the agent roster.** Per the spec's §7 economy warning, `.claude/agents/`
  definitions are promoted from recurring need, not architected up front. The recurring
  candidates to watch: a standing conformance-scanner and, once seeded headless sims + ablation
  are runnable, an emergence-auditor (decision_queue.md item).

## 5. Relationship to other canonical surfaces

- `CURRENT.md` — indexes this doc under Architecture once ratified; until then it is
  discoverable via the 2026-07-01 audit session and `HANDOFF.md`.
- `designs/architecture/key_substrate_v30.md` — remains the canonical substrate spec; this
  doctrine *frames* it (wrapper/propagation vocabulary) and defers to it on every mechanic.
- `references/module_contracts.yaml` — remains the canonical contract store; this doctrine
  names its shape as *the* container contract and directs all new modules to instantiate it
  unchanged.
- `godot/godot_conversion_strategy_v1.md` —
  remains the conversion plan; convertibility here (§1 morphisms row) is the doctrine-level
  statement of that plan's Key-log-parity discipline.
