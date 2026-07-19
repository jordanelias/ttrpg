# Module-Contract Adjudication — FULL GRAPH VERDICT

**Skill:** valoria-module-adjudicator · **Scope:** full graph (all 27 modules in `references/module_contracts.yaml`)
**Date:** 2026-07-13 · **Run:** multi-agent audit lane
**Machine pass:** `contract_adjudicator.py` — **22 violation(s), 61 warning(s)**, exit 1
**Derived views regenerated:** `module_flowchart.mermaid`, `state_graph.mermaid`, `module_map_flat.md` (27 modules)

---

## GRAPH VERDICT: **OPEN** — by a bounded, fully-characterized margin (no missing-mechanism hole)

- **Emit-closure (A2):** ~47/48 distinct emitted type-strings registered ≈ **97.9%**. One failure: `scene_outcome.battle_concluded` (mass_battle) — and that one is a **contract transcription defect**, not a canon gap (see P1-A below). No genuine unregistered emission exists in canon.
- **Consume-closure (A3): 100%** — every consumed type is registered and produced by ≥1 module or `engine`. Zero A3 violations.
- **Cycle closure (A7): 100%** — every module-graph cycle carries a `loops[]` damper/cap annotation. Zero A7 violations.
- **Gate / derivation / sequence integrity (A10/A11/A12): 100%** — zero violations. Only `A11-info` (faction_state Mandate & Treasury are computed cross-module by settlement_layer — canon-legal per §14.1 LPS-2e).
- **Cross-scale seam coverage (A6): the OPEN margin.** 20 of 22 violations are A6 cross-scale edges with no `transitions` annotation on either endpoint. **Per canon (`scale_transitions §12.2`, ED-1038 / Jordan J-1) these are explicitly EXEMPT from the "missing top-down channel" reading** — the Key substrate is the sole, all-directions delivery path and no bespoke channel is to be authored. What remains real is a *lower-severity authoring-discipline gap* (§12.3 sub-scale `targets[]` not yet populated; §12.4 enumerates these exact seams as Lane-B implementation targets) **plus an un-propagated contract-hygiene gap** (ED-1038 authored §12 but the down-seam modules were never given a `transitions:` entry citing it). **The assessor's A6 check is a co-defect: it does not implement the §12.2/§12.4 carve-out.**

**Bottom line:** the graph does not lint clean, so the honest machine verdict is OPEN. But the substantive closure is high: consume-closure, cycles, gates, derivations, and the accounting spine are all clean; emit-closure fails only on one mislabeled string; and the entire A6 cluster reduces to one canon-acknowledged, canon-exempted down-seam family + one propagation miss. There is **no unreachable direction and no missing mechanism** — `scale_transitions §12` guarantees all six directions over the single substrate.

---

## SEVERITY-RANKED FINDINGS

### P1-A (contract defect — canon disagrees with the contract; doc wins)
**`mass_battle` emits a fabricated type `scene_outcome.battle_concluded`, mislabeled "substrate §8.5 verbatim."**
Canon does **not** contain this type_id. `key_substrate §8.5` (line 523) writes **`scene.battle_concluded`**; `§3` (line 173) uses **`scene_outcome`** only as the *family name* whose members are `scene.contest_resolved, scene.battle_concluded, scene.investigation_resolved`. The contract conflated the family label with a type_id prefix and asserted a false "verbatim" provenance. The correct emit — `scene.battle_concluded` — is already present as the second emit on the same module.
→ **A2 violation + A4 orphan are both artifacts of this one spurious edge.** Remove the `scene_outcome.battle_concluded` emit. This is a **contract fix**, not a registry §10 extension. **Candidate lane: MB.**

### P1-B (registry-hygiene gap — real canon doc absent from the source registry)
**`piety_track` home doc `designs/personal/conviction_track_v1.md` is not declared in `references/canonical_sources.yaml`** (A8 violation). The file exists on disk (10 KB, real canon; the personal Conviction-scar system) and the contract cites it correctly; only the *territorial* `designs/scene/conviction_track_v30.md` is registered. This is the same 3-way name-collision hazard flagged in the module's own gap_note. Fix: add the personal doc to `canonical_sources.yaml` (distinct entry from the territorial one). **Candidate lane: IN** (canonical-sources registry hygiene; cross-cutting).

### P2-A (contract-propagation + script co-defect — the A6 cluster, 20 violations)
**ED-1038 authored `scale_transitions §12` (all-directions substrate + §12.4's enumerated down-seams) but the down-seam modules were never given a `transitions:` entry citing it, and the assessor never learned the §12.2 exemption.** The 20 A6 violations decompose into exactly the §12.4 known-seam family plus one scale-enum-granularity artifact:

| A6 seam (consumer ← emitter) | Types | In §12.4 known-seam list? |
|---|---|---|
| npc_behavior ← domain_actions | da.antinomian/covert/public_governance, scene.draft_da | **Yes** |
| npc_behavior ← peninsular_strain | env.peninsular_strain_shock | **Yes** |
| npc_behavior ← faction_politics | scene.investigation_resolved, state.coup_attempted/standing_change/succession | **Yes** |
| piety_track ← domain_actions | da.antinomian/covert | **Yes** |
| settlement_layer ← peninsular_strain | env.disaster, env.peninsular_strain_shock | **Yes** |
| settlement_layer ← scenario_authoring | env.disaster | **Yes** |
| settlement_economy ← domain_actions | da.economic_intervention | **Yes** |
| settlement_economy ← peninsular_strain | env.population_change | **Yes** |
| piety_track ← scene_slate | scene.dialogue/insult/threat/witness | **No** — scene→personal, an adjacent-band artifact of the `[scene]` vs `[personal]` scale-enum split (scene.* keys default to `[personal]` scale_signature; this reads lateral in practice) |

**Intent gate (resolution-diagnostic):** every seam in the table is a *deliberate, registry-canonical coupling* with an explicit design-doc statement (§12.4 enumerates them; the consumers are declared in `key_type_registry`). Per the intent gate the **couplings PASS** — they are not accidental. What is unfulfilled is the §12.3 authoring obligation (emitter populates sub-scale `targets[]`) and the contract's own transition annotation. **Dual remediation:** (a) **script** — teach A6 to accept a `scale_transitions §12` transition citation and/or suppress edges enumerated in §12.4 (the assessor is the defect for the missing-mechanism reading); (b) **contract/canon** — add `transitions: [{via: "scale_transitions §12 all-directions substrate"}]` to the down-seam modules and drive §12.3 `targets[]` population (Lane-B implementation, already tracked in §12.4). **Candidate lane: IN** (cross-cutting architecture / substrate).

### P3-A (necessity / A4 — emitted type with no concrete wired consumer)
**`env.crisis` is emitted by `peninsular_strain` and `scenario_authoring` but consumed by ZERO module contracts.** The registry declares `consuming_systems: [all]`, yet no module's `consumes[]` names it (only the articulation/fieldwork wildcards see it, which A4 correctly does not count). J3 necessity: either a genuine **missing consumer edge** (faction_state and/or settlement_layer plausibly should consume peninsula-scale crisis) or an over-emission. Not a fabrication risk; low-severity. **Candidate lane: WR** (world/peninsula) or IN.

### P3-B (loop-annotation asymmetry — no A7 violation, judgment note)
The `npc_behavior ↔ social_contest` 2-cycle is annotated **BOUNDED from the social_contest side** (Procedure-D 1/Accounting cadence + |Δaffect|≥0.5 threshold + Chain-Contest cap 3) but the **npc_behavior side records "dampers unconfirmed [OPEN — Jordan]."** One-sided damper confirmation; A7 passes on existence, but the two annotations should be reconciled. Low severity. **Candidate lane: SC.**

---

## PER-MODULE VERDICTS (27 modules)

**NON-CONFORMANT (10):** modules carrying an A-violation. Nine of these are the single P2-A down-seam cluster (root cause = one un-propagated §12 annotation, canon-exempt as mechanism); one is the P1-A contract typo.

| Module | Resolver | Verdict | A-findings |
|---|---|---|---|
| mass_battle | dice_pool | **NON-CONFORMANT** | A2 spurious `scene_outcome.battle_concluded` (P1-A) + A4 orphan (same edge) |
| npc_behavior | deterministic_accounting | **NON-CONFORMANT** | A6 ×9 (P2-A down-seam, consumer side; couplings intent-PASS) |
| piety_track | deterministic_accounting | **NON-CONFORMANT** | A8 doc not in canonical_sources (P1-B) + A6 ×6 (P2-A) |
| settlement_layer | deterministic_accounting | **NON-CONFORMANT** | A6 ×3 (P2-A, consumer side) |
| settlement_economy | deterministic_accounting | **NON-CONFORMANT** | A6 ×2 (P2-A); also standing RECOMMEND-RETIRE phantom (W-GAP, ED-SE-0005) |
| domain_actions | d_sigma | **NON-CONFORMANT** | A6 (P2-A, emitter side — da.*/scene.draft_da → npc_behavior/piety_track/settlement_economy); doc:null REFINE (ED-FA-0006) |
| peninsular_strain | deterministic_accounting | **NON-CONFORMANT** | A6 (P2-A, emitter side); A4 env.crisis (P3-A) |
| faction_politics | deterministic_accounting | **NON-CONFORMANT** | A6 (P2-A, emitter side → npc_behavior) |
| scenario_authoring | manifest | **NON-CONFORMANT** | A6 (P2-A, emitter side → settlement_layer); A4 env.crisis (P3-A) |
| scene_slate | manifest | **NON-CONFORMANT** | A6 (P2-A, scene→personal artifact → piety_track); W-DOC (home doc [GAP]) |

**CONFORMANT (16 extracted + 1 stub):** examined and sound at the A-check level (warnings/W-GAP/W-DOC/A4-orphan-with-universal-reader are non-blocking).

| Module | Resolver | Verdict | Notes |
|---|---|---|---|
| faction_state | deterministic_accounting | **CONFORMANT** | self-loop DAMPED (drift 0.6/season); Mandate/Treasury derived_value writable:false (F1-clean); A11-info cross-module derivation (legal) |
| npc_memory | state_reader | **CONFORMANT** | pure consumer; W-DOC (schema in doc-12 §2.3) |
| territorial_piety | deterministic_accounting | **CONFORMANT** | zero Key integration (registry §10 candidate, W-GAP) but no contract edge violates |
| threadwork | dice_pool | **CONFORMANT** | transitions §3.1/§3.5/§3.6 semantically fit (J2 pass); Coherence track (ED-830 ratified) |
| fieldwork_knots | dice_pool | **CONFORMANT** | wildcard consume (engine); transitions §3.9 fit |
| game_director | manifest | **CONFORMANT** | scene-lifecycle emitter; W-DOC |
| scene_timer | state_reader | **CONFORMANT** | telemetry sidecar; pure consumer |
| audit | state_reader | **CONFORMANT** | telemetry consumer |
| social_contest | dice_pool | **CONFORMANT** | transitions §3.4 Domain Echo fit (J2 pass); loop BOUNDED; persuasion_track bucket [ASSUMPTION] (see J1) |
| ci_political | deterministic_accounting | **CONFORMANT** | CI read-only (writable:false, correct — owned by territorial_piety); pool/track buckets fit |
| victory | state_reader | **CONFORMANT** | reader-only; gates use `reads:` for unowned MS/Mandate (A10-clean); doc DESIGN-not-CANONICAL (W-GAP) |
| engine_clock | clock_advance | **CONFORMANT** | A4 season_change orphan (ambient); doc:null (propagation_spec_v1 candidate, ED-1051 open) |
| miraculous_event | state_reader | **CONFORMANT** | single emit; home doc RESOLVED (ED-IN-0023) |
| articulation_layer | deterministic_accounting | **CONFORMANT** | universal wildcard reader (substrate §8.7); emits nothing |
| clock_registry | manifest | **CONFORMANT** | pure manifest; owns no state |
| personal_combat | d_sigma | **CONFORMANT** | Health derived_value writable:false (F1-clean); self-loop bounded; transitions §3.4/§12.3 fit; A4 combat_felled/resolved orphans are registry-declared-but-unwired (tracked gap_note) |
| campaign_architecture | — | **CONFORMANT (stub, vacuous)** | status:stub, zero edges — guardrail respected; standing retirement recommendation (W-GAP) |

---

## ALL-DIRECTIONS COVERAGE

*(`canon/definitions.yaml` referenced by the skill does not exist on disk; directions taken from the canonical enumeration in `scale_transitions §12.1`, the authoritative all-directions table.)*

| Direction (§12.1) | Substrate carrier | Graph evidence | Coverage |
|---|---|---|---|
| lateral / horizontal (same-scale) | shared scale_signature + scene presence | scene_slate→social_contest→npc_behavior (personal/scene); faction_state↔faction_politics (provincial) | **Covered** — dense |
| vertical up (§3.1-§3.8 handoffs) | eight handoffs | threadwork §3.1/3.5/3.6; mass_battle §3.6-3.8; social_contest §3.4; faction_state §3.2; fieldwork §3.9; personal_combat §3.4 | **Covered** where declared (J2 fit) |
| bottom-up (Domain Echo, §5/§7) | scene→faction on Sufficient Scope | social_contest→faction_state Mandate; settlement L/PS → faction Mandate (A11 cross-module) | **Covered** |
| top-down (§12.3 sub-scale targets) | strategic Key naming sub-scale actor in targets[] + scale_signature | domain_actions/faction_politics/peninsular_strain/scenario_authoring → sub-scale | **Mechanism present; targets[] UNPOPULATED** — the P2-A gap (§12.4 seams) |
| diagonal (causes[]-chain cross-scale) | Thread Echo §5.6; causes[] chains | threadwork Thread Domain Echo; causal chains | **Partial** — down-diagonal seams share the P2-A gap |
| down-diagonal (top-down across family) | as top-down, cross-family | §12.4 enumerated | **Mechanism present; UNPOPULATED** (P2-A) |

Four of six directions are substantively covered; the two top-down variants have the mechanism (canon-guaranteed, §12.2) but unpopulated authoring targets (§12.3) — the single P2-A cluster, not a missing channel.

---

## CYCLE TABLE (A7 = 0 violations)

| Cycle | Damper / cap | Verdict |
|---|---|---|
| faction_state self-loop (cascade / mission_shift) | drift_coef 0.6/season + 4-consecutive-season mission counter; crisis-bypass (scars≥3) intentional bounded un-damping | **DAMPED** (LD-5) |
| npc_behavior ↔ social_contest (2-cycle) | social_contest side BOUNDED (Procedure-D cadence + Δaffect threshold + Chain cap 3); npc_behavior side "unconfirmed [OPEN—Jordan]" | **BOUNDED, one-sided annotation** (P3-B) |
| settlement_layer ↔ faction_state (Mandate↔L/PS) | saturating Mandate = 7T/(T+6) + mean-reverting drift ±1; Stage-4 sim bounded 30 seasons | **DAMPED** |
| personal_combat self-loop (strike→hit→wound) | terminates at felling / Health depletion | **BOUNDED** |

---

## J-PASS (judgment — what the script cannot check)

- **J1 bucket fitness — PASS with two [ASSUMPTION]-grade notes.** Write-legality buckets are broadly correct: all derived aggregates (faction Mandate/Treasury, settlement Local Economy/Garrison/Public Order/province Accord, personal Health) are `derived_value writable:false` — F1-clean, deltas routed to substrate tracks. Two classifications are name/bucket tensions, both justified in-contract: (1) `social_contest.persuasion_track` named "track" but bucketed **clock** (bidirectional with terminal win/loss thresholds — scene-resolution progress, clock-like; A4-rationalized); (2) `npc_behavior.projects`/`arc state` reclassified track→**clock** (monotonic advance to completion/stall/terminal-FSM; A4-rationalized). No pool stored across actions; no derived_value writable. **Caveat:** these rest on `derived_stats_v30 §14`, a doc carrying a **status-line collision** (`## Status: CANONICAL` line 2 vs `## Status: PROPOSAL` line 4) — the taxonomy is relied upon but its ratification state is itself unresolved (pre-flagged by the skill).
- **J2 transition semantics — PASS where declared.** Every module that declares `transitions[]` cites a §3/§5/§12 handoff whose payload actually carries the edge (social_contest §3.4→Domain Echo Mandate; threadwork §3.1/3.5/3.6 thread-scale bridges; faction_state §3.2 personal→faction; fieldwork §3.9; personal_combat §3.4/§12.3). No decorative citations found. The J2 *gap* is the inverse: the P2-A down-seam modules declare **no** transition at all where §12 should be cited.
- **J3 necessity — one over-emission + one under-wiring.** Over-emission: the spurious `scene_outcome.battle_concluded` (P1-A) is a removal candidate. Under-wiring: `env.crisis` (P3-A) is emitted with no concrete consumer. All other emits are load-bearing (consumed by ≥1 concrete module or a tracked-pending registry consumer).

---

## NERS MAPPING

- **S (scale transitions + clean inter-module interaction):** near-complete — all six directions guaranteed by the substrate (§12), handoffs semantically fit; the residual is unpopulated top-down `targets[]` (P2-A), a discipline gap not a scale-coherence break.
- **R (complete, error-free wiring):** consume-closure 100%, cycles annotated, gates/derivations/sequence clean; emit-wiring fails only on one mislabeled string (P1-A) and one un-wired consumer (P3-A).
- **N / E (no redundant edges/types):** one redundant emit (scene_outcome.battle_concluded, P1-A) flagged for removal; otherwise no over-coupling.
- A passing lint is **necessary, not sufficient** for NERS; behavioral compliance remains with `valoria-resolution-diagnostic`.

---

## LEDGER CANDIDATES (recorded here only — NOT filed; centralized filing step handles allocation)

Per run instructions, P1/P2 canonical-gap findings are recorded as candidates with a proposed lane; no ledger/id_reservations/audit_registry write is performed by this agent for the ledger itself.

| # | Class | Summary | File | Proposed lane |
|---|---|---|---|---|
| P1-A | contract-defect | Remove spurious `scene_outcome.battle_concluded` emit (mislabeled "§8.5 verbatim"; canon writes `scene.battle_concluded`, `scene_outcome` is the family name) | `references/module_contracts.yaml` (mass_battle) | MB |
| P1-B | registry-hygiene | Add `designs/personal/conviction_track_v1.md` (real piety_track home) to `canonical_sources.yaml` (A8) | `references/canonical_sources.yaml` | IN |
| P2-A | propagation + script | Propagate ED-1038 §12 into down-seam modules' `transitions[]` and drive §12.3 `targets[]` population (§12.4 seams); teach A6 the §12.2/§12.4 exemption | `references/module_contracts.yaml` + `scripts/contract_adjudicator.py` (A6) + §12.4 emitters | IN |
| P3-A | necessity | Wire a concrete consumer for `env.crisis` (or confirm ambient-only) | `references/module_contracts.yaml` | WR |
| P3-B | loop-annotation | Reconcile npc_behavior↔social_contest damper (one-sided confirmation) | `references/module_contracts.yaml` | SC |

---

## GUARDRAILS OBSERVED

- **Stubs stayed empty** — campaign_architecture reported vacuous-conformant, zero invented edges.
- **Canon over chat** — every edge verdict traces to a `[READ:]` this session (key_substrate §8, key_type_registry, scale_transitions §3/§5/§12, derived_stats §1/§11/§14).
- **Doc wins over script** — A2 traced to canon (§8.5 writes `scene.battle_concluded`), contract flagged as defect; A6 cluster traced to §12.2 exemption, script flagged as co-defect. No `--force`.
- **No writes outside this audit folder.** No git commit/push. No edits to `editorial_ledger*`, `id_reservations.yaml`, or `audit_registry.jsonl`. The skill's mandatory `audit_registry.jsonl` completion-append is **deferred to this run's dedicated sequential registry step** per the orchestrator instruction (concurrent-write-collision avoidance) — this parallel agent deliberately does not append it.
