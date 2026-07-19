# Gap Register (v1) — Gameplay-Subsystem Observatory

## Status: FILED — 2026-07-14 · Lane: IN · ED-IN-0064

> ⚠️ **Phase-2 correction layer (`adversarial_review_v1.md` + `directional_coverage_v1.md` win any conflict).** The
> adversarial gate reclassified **GAP-F1 (`MS`-owner) GENUINE → CTC** (MS is already ticked: PP-255 →
> `sim/peninsular/ms_track.py` → `accounting.py:61`; only a *contract* owner is missing) and **GAP-A1's engine_clock
> sub-case GENUINE → CTC** (home doc `propagation_spec_v1.md` is CANONICAL with a drafted contract; pointer-flip pends
> ED-1051). The directional double-check added **GAP-DIR-1..5** (category D) — the genuine uncalled/unreached/deferred
> directions the `!A6` annotation-debt story missed. The revised GENUINE surface is `domain_actions` home (leaning
> CTC) + `env.crisis` consumer (leaning CTC) + **GAP-DIR-1 (diagonal, zero instances)** + **GAP-DIR-5 (temporal
> decay, deferred)** — not the four items the pre-gate summary implied.

Every gap / break / dead-end / friction on the gameplay-subsystem graph, keyed to a graph edge or node,
evidence-traced, and **classified before any fix is proposed** per the repo's two-tier doctrine (ED-1050):

- **[COMPLETE-THE-CHAIN]** — an unbuilt link in an otherwise-built chain; the fix is **derived from the logic of
  its surroundings**. No game/historical mechanic is imported. Precedent is *confirmatory only*.
- **[GENUINE-GAP]** — the surrounding logic does not determine the answer; only here would an imported-and-adapted
  precedent supply the solution.

Evidence types: `code:` (G_code AST / grep, from `structure_audit`) · `audit:` (a prior ruling/register ID) ·
`doc:` (design-doc section) · `ledger:` (ED/PP). Status of the broken thing: **BROKEN** (should fire, doesn't) ·
**INERT** (declared, never read/written) · **DOCTRINE-ONLY** (ruled, uncoded) · **ORPHAN** (real mechanics lost
from an index) · **STUB** (self-declared placeholder) · **UNRECONCILED** (multiple live definitions) ·
**ANNOTATION-DEBT** (mechanism present, its transition rule un-annotated).

> **Instrument disclosure.** These are LEADS (the L0 validation gate FAILED 1/3, §0 of the synthesis). The L1/L2
> numbers are exact but "measure, never gate"; `valoria-module-adjudicator` (A1–A12) is the authoritative
> per-module gate and wins any disagreement. **All fixes below are HELD-BACK (ED-1094)** — this docket authors none.

---

## A · `doc:null` — registered contract, no home design doc (unimplementable spec)

`code:` `structure_audit` L2 = 9 doc:null (audit, domain_actions, engine_clock, game_director, npc_memory,
scenario_authoring, scene_slate, scene_timer, settlement_economy).

| ID | Node · state | Evidence | Class | Fix-direction (HELD-BACK) |
|---|---|---|---|---|
| **GAP-A1** | `domain_actions` **doc:null** — strategic-turn verb home | `code:` L2 doc:null; `ledger:` ED-FA-0002 open; mirrors governance GAP-H3 | **GENUINE-GAP** | Author the strategic-turn home doc — the da.*/domain-echo spine hangs off it; blocks the Cut-2 governance verbs. |
| **GAP-A2** | `settlement_economy` **doc:null** | `code:` L2 doc:null | **CTC** | Moot if retired (GAP-K2); else fold into `settlement_layer_v30`. |
| **GAP-A3** | infra `doc:null` ×7 (engine_clock, scene_slate, game_director, scene_timer, audit, npc_memory, scenario_authoring) | `code:` L2 doc:null; `doc:` `propagation_spec_v1.md` §O.2 (CANONICAL) | **CTC** *(engine_clock corrected from GENUINE)* | `engine_clock`'s home doc **exists and is CANONICAL** (`propagation_spec_v1.md` §O.2 "engine_clock module contract"); only the pointer-flip pends ED-1051 (a sliver — the tick-scheduler/`cascade_depth` — is genuinely new). The rest are plumbing — author or mark authoring-time. |

## B · `[ASSUMPTION]`-grade resolvers (13 markers; the gameplay ones)

| ID | Node | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-B2** | `faction_state` resolver `[ASSUMPTION]` on the **in-13 hub** | `code:` L2 hub in-13 + cut-vertex; `doc:` contract resolver comment | **CTC** | Highest-leverage: ground the accounting resolver (d_sigma for contested, ED-874 exists) — surrounding logic determines it. needs_jordan. |
| **GAP-B7** | `npc_behavior` resolver `[ASSUMPTION]` on the **in-12 hub** | `code:` L2 hub in-12 + cut-vertex | **CTC** | Second-highest leverage; ground the Procedure B–E accounting. |
| **GAP-B1/B3–B8** | domain_actions, faction_politics, piety_track, territorial_piety, peninsular_strain, settlement_economy, npc_memory, miraculous_event, scenario_authoring `[ASSUMPTION]` | `code:` 13 `[ASSUMPTION]` markers in `module_contracts.yaml` | **CTC** | Per-module resolver grounding; none needs an imported mechanism. |

## C · Orphan / dangling emits & missing consumers

`code:` `structure_audit` L2 = 4 dangling-emits, 0 phantom-producers.

| ID | Edge · state | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-C1** | `mass_battle` → `scene_outcome.battle_concluded` **ORPHAN + UNREGISTERED** (fabricated type) | `code:` L2 dangling + `*UNREG`; `ledger:` **ED-MB-0010** (2026-07-13) | **CTC** | **KNOWN NO-ACTION** — already filed; delete the fabricated edge (real emit `scene.battle_concluded` present). Do NOT re-file, do NOT render as LIVE. |
| **GAP-C2** | `personal_combat` → `scene.combat_felled` + `scene.combat_resolved` **ORPHAN** | `code:` L2 dangling; `doc:` module `gap_notes` CONSUMER-WIRING | **CTC** | Wire the declared consumers (npc_behavior/faction_layer/articulation per registry) — already documented; cite, don't re-file. |
| **GAP-C4** | `env.crisis` emitted (peninsular_strain + scenario_authoring), **consumed by ZERO concrete module** | `code:` L2 dangling; `doc:` registry says `[all]` but no contract wires it | **GENUINE-GAP (candidate)** | The sharpest orphan: the surrounding logic doesn't name a consumer. **NEW LEAD → WR** — candidate consumers faction_state / settlement_layer; needs_jordan. |

## D · Cross-scale seam annotation-debt (`!A6`)

`audit:` 20 `!A6` seams; `doc:` `scale_transitions_v30 §12` (ruling J-1, ED-1038) — the substrate delivers in all
six directions via one observer-resolution rule.

| ID | Edges · state | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-D1** | `domain_actions` → {npc_behavior, piety_track, settlement_economy} `!A6` | `code:` module_flowchart `!A6`; `doc:` §12.4 enumerates these as intentional | **CTC (ANNOTATION-DEBT)** | Add `transitions:` annotations; NOT missing mechanisms. |
| **GAP-D2** | `faction_politics` → npc_behavior `!A6` | same | **CTC (ANNOTATION-DEBT)** | Annotate. |
| **GAP-D3** | `peninsular_strain` → {settlement_layer, settlement_economy, npc_behavior}, `scenario_authoring` → settlement_layer `!A6` | same | **CTC (ANNOTATION-DEBT)** | Annotate as a batch. The 8 seams above == §12.4 exactly. |
| **GAP-D0** | the 9th machine `!A6` seam `scene_slate → piety_track` is **NOT** a real down-seam | `code:` `scene.dialogue/insult/threat/witness` are `scale_signature:[personal]`; piety_track is `[personal]`; the identical `scene_slate→npc_behavior` is drawn solid because npc_behavior's `scales:` includes `scene` | **CTC (scale mislabel)** | Add `scene` to piety_track's `scales:` (WS2 vocabulary), NOT a `targets[]` pass — no cross-band delivery occurs. |

### D-directional · genuine uncalled / unreached / deferred directions (the "all directions" double-check)

`doc:` `scale_transitions §12.1` six directions + `key_echo_armature §2.6` temporal 7th. Beyond the annotation-debt
seams, three directions hide an execution gap the seam-count misses. Full detail: `directional_coverage_v1.md`.

| ID | Direction · state | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-DIR-1** | **diagonal (`causes[]`) — ZERO executable instances** | `code:` `causes=` populated nowhere in `sim/**` (grep); `compute_thread_echo` zero callers; `doc:` `key_echo_armature_v1.md:41` "zero executable or exemplified instances" | **GENUINE-small** | Author the first `causes[]` exemplar end-to-end (threadwork §5.6 Thread Echo — resolver already written). After one exemplar, further diagonals are CTC. → WR/cross_scale. |
| **GAP-DIR-2** | **bottom-up Accord echo (§5.5) built-but-uncalled** | `code:` `compute_accord_echo` zero callers (grep); reproduces governance GAP-A2 | **CTC** | Wire `compute_accord_echo` into `echo_transport` beside `compute_domain_echo`. → FA. |
| **GAP-DIR-3** | **distribute-down territory transfer built-but-uncalled** | `code:` `parliamentary_transfer.propose_transfer:101` zero callers (grep); reproduces governance GAP-A1 | **CTC** | Connect `parliamentary_bridge`'s vote outcome to `propose_transfer`. → FA/SC. |
| **GAP-DIR-4** | **§3 handoff dispatcher orphaned; §3.3 empty stub** | `code:` nothing imports `handoff_rules.py` (grep `No matches`); `doc:` `scale_transitions:51` §3.3 header-only | **mixed** | De-orphan or demote `handoff_rules.py` (CTC); author §3.3 Personal→Contest body (GENUINE-small). → GO/cross_scale. |
| **GAP-DIR-5** | **temporal `decay()` un-shipped (ruled deferral)** | `doc:` `key_echo_armature_v1.md` "substrate ships WITHOUT decay… deferred to Stratum B+"; reproduces governance GAP-B4/A4 | **[deferral]** | Generalize the MS-decay cadence pattern into `decay()` when Stratum B (cross-tick convergence) starts. Flag "only-goes-up" quantities against it; do NOT fix now. |

## E · Zero-Key-integration (CANONICAL docs, no wiring — INERT)

| ID | Node · state | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-E1** | `ci_political` **in-0/out-0 INERT** (CANONICAL) | `code:` L2 in-0/out-0; `doc:` ci_political_v30 §4–§5 | **CTC** | Key the Church card-game emitters/consumers so CI/pool cross-scale-radiate; logic exists, wiring absent. |
| **GAP-E2** | `territorial_piety` **in-0/out-0 INERT** | `code:` L2 in-0/out-0 | **CTC** | Key CV/CI so territory piety participates in the graph (parallels the governance orthodoxy-axis lead). |

## F · Ownerless state / coverage gaps

| ID | State · edge | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-F1** | `victory` reads **`MS` (Mending Stability), a clock with no owning *contract* module** | `code:` `params/core.md` PP-255 (MS decay); `sim/peninsular/ms_track.py:59` writes it; `sim/peninsular/accounting.py:61` wires it into Year-End — grep-verified | **COMPLETE-THE-CHAIN** *(was GENUINE — corrected by adversarial gate)* | MS **is** ticked in the sim; the gap is only that no `module_contracts.yaml` module *declares* ownership. Fix is determined: add a `substrate_state`/peninsular owner emitting `env.ms_delta` pointing at the existing decay (a prior audit already drafted it). Not an imported mechanism. |

## G · Pointer-debt (unregistered quantities; G_pointer 52.7 %)

`code:` `pointer_audit` — 28 candidate rows. Triage: some are computed-internal ("expected backlog"), some are
non-scalar structured state (a design ruling), some are genuine missing registrations.

| ID | Quantities | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-G1** | personal_combat Wounds/Initiative/Poise/cumulative_damage | `code:` pointer_register `module_contracts.state` unresolved | **CTC** | Register the combat scalars (canonical keys exist for most). |
| **GAP-G2** | npc_behavior beliefs/opinions/concerns/projects/arc-state | `code:` pointer_register; `doc:` pointer_debt_worklist Category C | **[design ruling]** | **NON-SCALAR** — whether these are registry quantities at all is a Jordan design call, left open ON PURPOSE. needs_jordan. |
| **GAP-G4/G5/G6/G7** | faction stats 1-7; ci card-hands/cooldown/pool; settlement province-Accord + cross-module Mandate/Treasury; victory Accord/PT/PV/Turmoil | `code:` pointer_register rows | **CTC (mostly)** | Register or route to canonical keys; `W_s` correctly excluded (formula-local). victory's are the ownerless-clock reads (see GAP-F1). |

## H · Currency / hygiene

| ID | Item · state | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-H1** | `social_contest_v30.md` CANONICAL but reads **unregistered** | `code:` gen_audit unregistered-canonical (DOC_KEYS regex blind spot) | **CTC** | Verify body `**Status:**`, then fix the `canonical_sources.yaml` key name (also march_layer, settlement_adjacency, fractional_province_ownership). |
| **GAP-H2** | `piety_track` home `conviction_track_v1.md` **unregistered** in canonical_sources | `audit:` PR#131 P1-B; `ledger:` ED-IN-0048 open | **CTC (ORPHAN)** | Register the real home; coordinate ED-SC-0003. |
| **GAP-H3** | `id_reservations.yaml` **duplicate `IN:` key** — YAML last-wins resolved IN to stale 63 | `code:` two `IN:` mapping lines; recurrence of the 2026-07-07 class | **CTC (UNRECONCILED)** | **FIXED this run (OBS-IN-1)** — collapsed to one line, next_free 65. |
| **GAP-H4** | 7 Convictions throughline-**isolated** (P2 validation FAIL) | `code:` validation.json p2 cv 999; `code:` L0 Mode H | **[real finding]** | The Convictions live inline in NPC Behavior, cited nowhere — the structural cause of the gate failure. First-class doc status or throughline substantiation. |
| **GAP-H5** | CLAUDE.md §6 stale "10/27 doc:null, 11/27 [ASSUMPTION]" | `code:` live L2 = 9 / 13 | **CTC (hygiene)** | **NEW LEAD → IN**: refresh §6 to 9 doc:null / 13 [ASSUMPTION]. |
| **GAP-H6** | Threadwork = Mode-A hub AND Mode-D cascade sink (190 chains) | `code:` L0 weakness_register A + D | **[lead]** | One-way pressure — verify Ω-d feedback intent. |
| **GAP-H7/H9** | vocab-debt: Game Master 21/8 (top throughline_resolutions); Cultural Reformation 23/9 (top peninsular_strain); Coup Counter 57/13 (top arc_expansion) | `code:` L0 Mode G | **CTC** | Single-doc-concentrated grep-replace (PP-678 workflow). |
| **GAP-H8** | settlement Prosperity ×50-vs-×10 | `doc:` params prose; `ledger:` ED-SE-0045 | **[no-action here]** | Different outputs (Local Economy vs Treasury) — NOT a contract collision; formula_audit correctly 0 multi-def. The prose-table conflict is ED-SE-0045's. |
| **GAP-H10** | `combat_v30.md` registered-canonical **AND** superseded (currency drift) | `code:` gen_audit drift=1 | **CTC** | Repoint/retire the registration to `combat_engine_v1/`. |
| **GAP-H11** | 5 genuinely-dead citations (caste_integration_v1, rank_ladder_v1, einhir_revival_v30, restoration_movement_v30, a 05-15 handoff) | `code:` gen_audit stale-pointers (nonexistent bucket) | **CTC** | Human triage: dead ref / typo / open forward-ref; 10 more are trivial restructure-ledger repoints. |

## I · Code structure (G_code)

| ID | Item | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-I1** | 9-module `sim.personal.contest` import cycle (SCC) | `code:` structure_metrics cycles | **[lead]** | Intentional-during-rebuild (contest_rebuild); revisit at Stage-4 close. |
| **GAP-I2** | `sim.provincial.massbattle ↔ units` cycle | `code:` cycles | **[lead]** | Break the mutual import if not load-bearing. |
| **GAP-I3** | 87 import-orphans incl. whole fieldwork/investigation + provincial-action families | `code:` structure_register orphans | **[lead]** | Dead-code triage; verify wired-by-string (adapters) before removal. |
| **GAP-I4** | **Contract↔code black-hole** (3/27 name-map) | `audit:` capstone #7 (ED-IN-0056) | **[deferred WS]** | The single biggest confidence limiter; needs the `mechanics_index.yaml sim_module:` join. |

## J · Name collision / hidden loop / dual-emit (`[OPEN — Jordan]`)

| ID | Item | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-J1** | 3-way "**Piety Track**" collision: `piety_track` (personal, conviction_track_v1) vs `territorial_piety` (territorial, conviction_track_v30) | `doc:` both contracts' gap_notes `[OPEN — Jordan]` | **UNRECONCILED** | Do NOT merge the nodes; disambiguate the name. |
| **GAP-J2** | Mandate↔L/PS cross-module feedback loop **invisible to formula_audit** | `code:` formula_register cycles disclosure (bare vs annotated node id) | **[blind spot]** | cycles=0 is a lower bound; needs a registry-key node identity to detect. The loop's damper is real canon (settlement §1.8). |
| **GAP-J3** | dual-emit attribution: `scene.dialogue` (scene_slate+social_contest vs npc_behavior), `mechanical.scene_entered`, `state.belief_revised` | `doc:` gap_notes `[OPEN — Jordan]` | **UNRECONCILED** | Assign a single canonical emitter per type. |

## K · Retirement / contract-completeness

| ID | Item | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-K1** | `faction_politics` 1115-line CANONICAL head, **no state block** in contract | `code:` L2 (no state) | **[completeness]** | Extract its state (Standing ladder, coup/succession) into the contract. |
| **GAP-K2** | `settlement_economy` phantom (doc:null, no state, in-3/out-0) | `ledger:` ED-SE-0005 retirement | **[retire]** | Fold into `settlement_layer`; resolves A2/B5. |
| **GAP-K3** | `campaign_architecture` STUB (0 edges, consolidation doc not a runtime module) | `code:` L2 stub | **[retire]** | Retirement recommended — content distributes across victory/threadwork/settlement/peninsular_strain. |

---

## Summary

**~39 findings across 11 categories (5 directional added; 2 reclassified by the gate).** Post-gate two-tier tally:
**[COMPLETE-THE-CHAIN] ≈ 26** (now incl. GAP-F1 MS-owner + engine_clock, GAP-DIR-2/3 uncalled resolvers) ·
**[GENUINE] ≈ 2–3** (GAP-A1 domain_actions home *leaning CTC* · GAP-C4 env.crisis-consumer *leaning CTC* ·
**GAP-DIR-1 diagonal zero-instances** — the one clean genuine build) · **[deferral] 1** (GAP-DIR-5 temporal decay) ·
**[design ruling] 1** (GAP-G2 non-scalar state) · **[no-action / known] 5** (GAP-C1 ED-MB-0010, GAP-C2, GAP-H3-fixed,
GAP-H8, the annotation-debt seams) · the remainder are code-refactor/currency-hygiene **leads**.

**This is the intended shape** — and the adversarial gate *sharpened* it: the "missing" architecture is
overwhelmingly **unbuilt wiring on sound logic** — zero-Key modules to key, `[ASSUMPTION]` resolvers to ground,
annotation-debt seams, orphaned/uncalled emits to connect, pointer-debt to register. The genuine-mechanism surface
is smaller than it first looked: **`MS`-owner and `engine_clock` are CTC** (the code/canon already determines them),
leaving essentially **one clean genuine build — the first `causes[]` diagonal exemplar (GAP-DIR-1)** — plus the
`domain_actions` home (leaning consolidation) and the ruled temporal-`decay()` deferral. The two integration hubs
(`faction_state`, `npc_behavior`) carrying in-13/in-12 while both `[ASSUMPTION]`-grade remain the highest-leverage
place to spend grounding effort. The GENUINE claims survived the gate (`adversarial_review_v1.md`); the directional
double-check (`directional_coverage_v1.md`) is where the remaining genuine surface actually lives.
