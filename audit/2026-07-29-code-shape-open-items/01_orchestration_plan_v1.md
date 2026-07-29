# Connective-Tissue & Compliance Orchestration Plan v1

## Status: PROPOSED (merge ratifies per ED-1094, EXCEPT the §5 held-back forks — those are Jordan's alone) — ED-IN-0091, 2026-07-29

**Objective.** Execute the open-items register (`00_open_items_register.md`, "OI-nn" below) via
orchestrated Sonnet/Opus agent waves, in two strict priorities:

1. **P1 — Connective tissue.** Resolve every orphan — with self-flagging stubs where real
   behavior is design-gated — so the gameplay pipeline runs end-to-end across all scene
   directions and all scales. Exit = the pipeline-reach oracle (§2.3) is green.
2. **P2 — Compliance.** Bring all code into the hierarchical / modular / centralized shape the
   repo requires (CLAUDE.md §8 "every rule lives once", ED-1083 guardrails: declared I/O only,
   no entity special-casing, no interface dialects).

**Concurrency & lane partition (Jordan directive, 2026-07-29).** Multiple Claude Code sessions
run simultaneously; two lanes are carved out whole to dedicated sessions, each executing its own
merged plan:

- **MB** → `audit/2026-07-26-mass-battle-fable-audit/03_execution_plan.md` (ED-MB-0045 plan v2,
  as corrected by PR #250). This plan **touches no MB-owned surface**: not
  `tests/sim/mass_battle/`, not `systems/mass_battle/`, not the `mass_battle` contract rows or
  MB registries/docs. Routed there (register rows "→ MB plan"): the fabricated emit (E1), the
  empty contract (E6), CellTable/epsilon/pool dedups (A2/B1/B2), dead machinery (B3), MB
  doc/token hygiene (E4/E5/E8), the MB import cycles, and the two-tree + damage-law forks (§7
  there). **Declared seam:** `faction_action.py:349` (the FA-lane call site into the wired MB
  tree) — byte-untouched here; a wave needing it changed files the item to the MB session.
- **PC** → `audit/2026-07-26-combat-balance-customization-state/combat_execution_plan.md`
  (PR #249: batches E0–E3 fully specified and ⚖-free, E4+ blocked, §13 orchestration layer).
  This plan **touches no file under `systems/combat/`**. Routed there (rows "→ PC plan"): dead
  surface + unreachable elements (E0/M12, E2/M9), vocabulary/knob ownership incl. the ~60-knob
  config-leak (E0/M15 — its 279-literal census subsumes OI-46), the pool-formula and
  8.0-anchor dedups (OI-44/45, riders on E0's ownership pass), and the `_emit()`→`scene.combat_*`
  mapping (OI-26 — a natural rider on the §12 wrapper audit the PC plan itself calls for).
  **Declared seam:** `combat_engine_v1/wrapper.py`'s public resolve API. Wave 1's dispatch
  bridge (OI-01) lives entirely on the IN side of that seam (`engine/cross_scale/`), consuming
  the wrapper as-is; if the bridge needs a wrapper change, the item is filed to the PC session,
  never edited here. (Coordination note: the PC plan flags wrapper.py as its own §12 blind
  spot — the bridge treats the wrapper's CURRENT observable behavior as the contract and pins
  it with a characterization test at the seam.)

**The routing is physical, not referential:** every item this program identified that the two
dedicated plans did not already carry has been appended to them — **MB plan §12** (stubwire
conversion of `altonian_reinforcements`, the two MB import cycles, the F4 sys.path residue,
F6/F7 token reconciliation, seam declaration) and **PC plan §15** (pool-formula + 8.0-anchor
single-owner riders on E0/M15, the wiring audit's dead list as an M12 rider, `sel_*`/
`point_concentration` shape hygiene, the `_emit()`→Key mapping as a §12-wrapper-audit rider,
seam declaration) — both in this PR. A dedicated session reading only its own plan misses
nothing.

This is §3's session-lane-scoping made structural: zero file overlap ⇒ zero merge collisions
between the concurrent sessions. If a future directive carves out another lane (SC is the
obvious candidate), the same recipe applies: route the register rows, append the items to the
lane's plan, declare the seam, characterize it with a test, never cross it.

**Doctrine bindings (non-negotiable, every wave):**
- **Bottom-up from primitives (§0).** P1 builds ONE new primitive (the stub-wire owner, §2.1)
  and composes everything else from what exists (`engine/substrate/keys.py`, `obs_core`,
  `structure_audit`, `review_core`). No wave re-implements a rule.
- **Measurement discipline (§0.1).** Every wave names its falsifier artifact in its exit
  criteria — a test that would have shown the wave's claim wrong, shipped in the same PR.
  Conditional assertions assert that they asserted (`assert checked >= N`). Behaviour changes
  (incl. golden re-records, e.g. OI-05's `npcs_generated == 0`) are named loudly in the PR body.
- **Adversarial relay (§10).** Every producing stage is followed by a structurally independent
  critic — `valoria-critic` (read-only tools) via `hCritic`, receiving OUTPUT, never reasoning.
- **G12 (adopted from the MB plan v2, PR #250).** A subagent's measurement is a **lead** until
  the orchestrator re-derives it; provenance is marked per claim, and agent output never becomes
  settled fact by restatement. (Applied already: this program's own register carries
  `[verified]`/`[corrected]` tags from the orchestrator's 07-29 spot-check pass.)
- **No fabrication (§5/§7).** No wave introduces a numeric constant without a `PP-NNN`/`ED-NNNN`
  provenance line; stubs return typed no-ops, never invented values.
- **Lane scoping (§3/§4).** Each wave lands as its own PR, scoped to one lane where possible
  (IN for the cross-cutting spine; PC/MB/SC/SE/FA/WR/FI for subsystem lanes), allocating
  `ED-<LANE>-NNNN` at execution time from `id_reservations.yaml` (never max+1; expect same-lane
  collisions — reconcile on merge as documented precedent).

---

## §1 · What "the pipeline runs across all directions and scales" means (acceptance)

A seeded `mc_v18` campaign (deterministic, N seasons) in which:

- **All scene directions dispatch**: every `scene_type` the slate can queue (`combat`, `contest`,
  `investigation`/`fieldwork`, thread operation, domain action) either resolves through its
  canonical resolver or records a **stub-flag** — never a silent `"not live"` deferral (OI-01/02).
- **All 7 Key-delivery directions** (directional_coverage_v1's roster) either fire ≥once or
  record a stub-flag: lateral, bottom-up echo (incl. the Accord leg, OI-03), top-down targets[],
  diagonal causes[] (OI-28), vertical-up handoff (OI-06), temporal (decay stays a **declared**
  deferral, OF-3 — flagged, not faked).
- **All scale rungs are representable** in `scale_signature` (OI-35, after the §5 confirm) and
  every world chain is populated: `world.npcs`, `world.knots`, `world.settlements` non-empty
  (OI-05/07).
- **Every dangling emit has a consumer or a ruled disposition** (OI-21/22).
- **Zero unconditional `NotImplementedError` in live trees** — every OI-17 stub converted to a
  self-flagging stub-wire (§2.1); the stub count is a *visible, decreasing* telemetry line, not
  a hidden crash class.

The instrument asserting all of this is **`engine/tests/test_pipeline_reach.py`** (§2.3) — built
first, red, and driven green wave by wave. That ordering is deliberate: the oracle is the
falsifier for every subsequent wave's "wired" claim.

## §2 · The three P1 primitives (Wave 1 builds exactly these)

### 2.1 `engine/substrate/stubwire.py` — the single owner of "explicitly-flagged not-built"
- `stub_resolve(module: str, io_contract: str, *, reason: str) -> StubResult` — a frozen
  dataclass `{stub: True, module, io_contract, reason}`; callers treat it as a typed no-op.
- A module-level `invocations` counter the season loop folds into campaign telemetry
  (`SeasonReport.stub_hits`, alongside the existing F7 `npcs_generated` pattern).
- **Self-flagging in every audit/sweep, by construction:** (a) every converted stub imports
  `stubwire` — one greppable owner; (b) `structure_audit` gains a `stub_wired` node attribute
  derived from that import (audit sees stubs without a second registry to rot); (c)
  `review_core` gains a report-only `stubs.count` signal with the count in
  `registers/review_baseline.yaml` as a **ratchet** — a session that silently adds a stub
  regresses the baseline and the Stop-hook says so. No standalone stub-registry file: derived,
  never stored (single-owner rule applied to the flag itself).
- Falsifier: `tests/valoria/test_stubwire.py` — converts a fixture stub, asserts the audit
  attribute + telemetry + ratchet all see it; mutation check: delete the import, all three fail.

### 2.2 Dispatch closure — no silent deferral
`scene_dispatch._resolve_slot` gets a total mapping: every `scene_type` → canonical resolver or
`stubwire`. Concretely: `combat` → `combat_engine_v1/wrapper.py` behind a **`[SEED]`
party-derivation bridge** reusing the exact pattern `_emergency_council_parties` established
(ED-SC-0006/0007 — derive combatants from the same faction aggregates, no invented actors),
retiring the deprecated `systems.combat.sim.combat` call (OI-01). **PC-seam terms:** the bridge
is IN-side only (`engine/cross_scale/`), consumes the wrapper's public API as-is, and ships a
characterization test pinning the wrapper behavior it depends on; any wrapper-side need is
filed to the PC session (lane partition above). `investigation`/`fieldwork` → stub-wired
resolvers (OI-02) until FI designs land; the `"resolver not live"` string is deleted — the
fallback becomes `stubwire`, which is visible.

### 2.3 `engine/tests/test_pipeline_reach.py` — the acceptance oracle
Seeded campaign; asserts per §1 with explicit coverage counting (`assert checked >= N` per
§0.1 #2 — a direction that never came up is a FAIL, not a skip). Ships red-marked (xfail rows
per unwired direction, each citing its OI row); waves flip rows to strict as they land. The
xfail manifest IS the live P1 burn-down list.

---

## §3 · Waves

Sizing respects the default guideline (≤15 agents per workflow run); each wave = one Workflow
invocation + one PR. Model tiers per CLAUDE.md §10: **Sonnet implements, Opus adjudicates,
critics are `valoria-critic` via `hCritic`** (read-only by construction). Every write lane runs
`isolation: worktree`. Orchestrator (this session class) plans and gates; it does not author
artifacts (Jordan's 2026-07-28 Fable-placement ruling). Workflow scripts are authored at
execution time from `tools/wf_harness.js` via `python tools/ci_wf_harness_check.py --fix`
(edit the owner, never a copy) and path-checked with `ci_claude_workflow_paths.py`.

### Wave 0 — Preflight (no code): ruling docket + instrument integrity — ~4 agents
| Stage | Agents | Tier |
|---|---|---|
| Assemble the §5 Jordan docket as one decision surface (options + defaults where they exist, per workplan §5 row format) | 1 | opus |
| Fix orphan-detector integrity BEFORE any triage acts on its output (OI-55: `__init__` misresolution, CLI-entry labeling) + known-answer tests for `vector_audit` core | 2 | sonnet |
| Critic pass on both | 1 | valoria-critic (opus) |
Exit: docket filed in the PR body + lane handoffs; detector fixes land with expected-delta tests
(§0.1: the orphan list may shrink — record the delta, don't celebrate it silently).
**Falsifier:** known-answer fixture where a fake orphan/cycle must be found and a labeled
CLI entry must NOT be.

### Wave 1 — The P1 spine: stubwire + dispatch closure + reach oracle — ~8 agents (IN lane)
| Stage | Agents | Tier |
|---|---|---|
| Build §2.1 stubwire + telemetry + ratchet signal | 1 | sonnet |
| Build §2.3 reach oracle (xfail manifest from the register) | 1 | sonnet |
| §2.2 dispatch closure: combat bridge · investigation stub-wire (2 parallel worktree lanes) | 2 | sonnet |
| Convert the OI-17 Pass-2l stub class → stubwire (pipeline over ~19 files; mechanical, uniform — EXCLUDES the MB-owned `altonian_reinforcements.py`, handed to the MB session with the stubwire recipe) | 2 | sonnet (effort low) |
| Contract-conformance adjudication of the combat bridge (Key IN → resolver → OUT closure, module-adjudicator method) | 1 | **opus** |
| Adversarial critic relay over the whole wave's diff | 1 | valoria-critic (opus) |
Exit: `pytest tests/valoria` + `engine/tests` green; reach oracle red rows reduced per manifest;
zero unconditional raises in live trees. **Falsifiers:** test_stubwire mutation check;
reach-oracle rows for combat/investigation flipped to strict; byte-parity probe that the combat
bridge changes NO existing golden (new path only) — if a golden moves, the wave stops and says so.

### Wave 2 — Orphan closure: echo, transfer, NPC/knot/settlement chains — ~10 agents (lanes: IN/FA/SE/WR)
Parallel worktree lanes, one per seam, each = implement (sonnet) with the opus adjudicator +
critic relay shared:
1. `compute_accord_echo` caller in the echo path (OI-03) — spec: LPS-2e aggregate, cite it.
2. `parliamentary_transfer.propose_transfer` wiring via the parliamentary bridge (OI-04) —
   closes the territory one-way ratchet.
3. `generate_npc` at world-gen + season tick (OI-05) — **golden re-record, named loudly**
   (`test_f7_smoke_oracle.py:127` self-documents this flip; re-record deliberately, cite OI-05).
4. `world.knots`/`world.settlements` population via existing `registry.py` (OI-07).
5. `handoff_rules` wired as the vertical-up dispatcher inside dispatch (OI-06); its "§3 rule
   missing" fallback becomes a stubwire flag; §3.3's EMPTY section stays a flagged stub pending
   ED-IN-0049 (J).
6. Articulation minimal subscriber (OI-08): subscribe to the bus, consume the §3.1 trigger
   table's registered types, render nothing yet — stub-flag per invocation. Kills the
   zero-subscriber state without inventing the render layer (that stays ED-IN-0073's docket).
7. `npc_ai`, `companion`, `rs_track`/`ip_track`, threadwork/world orphan sims → stubwire or a
   one-line wire where the design doc already specifies the call site (OI-09/12).
Exit: reach-oracle direction rows for bottom-up echo, vertical-up, NPC/knot/settlement chains
strict; `structure_audit` orphan count measurably down with the delta recorded in the PR.
**Falsifiers:** per-lane — e.g. a seeded campaign where a faction loses then regains a territory
(OI-04); an NPE season over a now-populated store asserting ≥1 npc action (OI-05, with
`assert checked >= 1`).

### Wave 3 — Keys & contract truth — ~9 agents (IN lane + per-lane one-liners)
1. Wire `scene.combat_resolved`/`_felled` declared consumers minimally (npc_behavior/
   faction_state `apply=` handlers + articulation trigger rows, OI-22/OI-27's ED-IN-0004 slice).
2. ~~`_emit()` vocabulary mapping~~ **→ PC session** (OI-26 edits PC-owned files; the IN-side
   half — registering/consuming the 4 canonical `scene.combat_*` types — lands with item 1).
3. Contract truth sweep (sonnet pipeline): OI-24's npc_behavior residue, `doc:` repoint
   (C-KEY-2), faction_politics `state:` block (OI-20's contract half), MS ownership declaration
   (OI-32). (`mass_battle` contract honesty note = MB plan E6, not here.)
4. Register the OI-30 Category-B scalars in `descriptor_registry` (mechanical; C2 stays J).
5. `causes[]`/`targets[]` population at the emitters the armature already specifies (OI-28) —
   authoring-guidance from `political_dynamics_keys_migration_v30.md`, cited per site.
6. Opus adjudicator: emit-closure re-run (module-adjudicator) + critic relay.
Exit: dangling-emit count 4 → ≤1 (`env.crisis` held for §5); adjudicator emit-closure ≥ its
2026-07-13 97.9% with the residual named. **Falsifier:** adjudicator run BEFORE vs AFTER in the
PR, plus a campaign asserting ≥1 consumed `scene.combat_resolved` (`assert checked >= 1`).

### Wave 4 — Centralization (P2, live trees) — ~10 agents (PC/SC/IN lanes)
1. ~~PC dedups~~ **→ PC session** (OI-44/45/46 ride the PC plan's E0 ownership pass — M15's
   literal census is the same defect class; this wave touches nothing under `systems/combat/`).
2. Import-cycle break (OI-52): `game_state ↔ npe` only (contest cycle stays, documented
   intentional-during-rebuild; both MB cycles → MB session).
3. Dead-root sweep (OI-53): `--sim-root` default, 11 `mechanics_index` paths, the 4 remaining
   tools — **plus the §0.1 #5 guard**: a test failing on any live-tool reference to a retired
   root (the class recurred once already; the guard is the fix, not the sweep). Stays in THIS
   plan by the MB audit's own filing: it declared these out-of-MB-lane (IN). The one MB-owned
   site (`test_persubunit_stress.py:17` sys.path) is left to the MB session.
4. Contract↔code join (OI-54): `sim_module:` field populated 27/27 (or explicit `none` with
   reason), `structure_audit` correspondence check upgraded from name-match to join-verified,
   report-only `review_core` signal.
5. ruled-but-unexecuted sweep (OI-51) + currency-layer orphans (OI-57) — mechanical (sonnet,
   effort low).
6. Opus verifier (goldens/parity) + critic relay.
Exit: `review_core --check` no regression; every dedup carries its equality/parity test.
**Falsifiers:** per-dedup mutation check (perturb the single owner, every former call site
moves); the dead-root guard test red on a planted regression.

### Wave 5 — Capstone: verify, re-measure, re-baseline — ~6 agents
1. Re-run the full observatory (structure_audit, vector-audit refresh — clears the stale
   families, OI-58) and diff every §Counts metric vs this register: orphans, dangling emits,
   stub count, cycles, correspondence.
2. Reach oracle strict-row census vs §1; remaining xfails must each cite a §5 fork or a D row.
3. Completeness critic (opus): "what's missing — an OI row not covered by any wave, a claim
   with no falsifier artifact, a golden re-recorded without a loud callout?"
4. 2× independent refuter critics over the capstone claims (majority kill per §10).
5. File per-lane EDs for everything executed; update lane handoffs; CURRENT.md stamp reconcile.
Exit: this folder gains `02_execution_ledger.md` mapping OI-nn → PR/ED/falsifier/outcome —
**every row accounted: done, stub-flagged, held (§5), or deferred (D) — no silent drops.**

## §4 · Orchestration mechanics (binding on every wave)

- **Tiering:** Sonnet for bounded implementation/extraction (effort `low` on mechanical
  pipelines, `high` on seam wiring); Opus for the adjudication/verify/synthesis nodes that gate
  a result and for any competing-considerations judgment; critics run as `valoria-critic`
  (Opus tier on gating verdicts, Sonnet on bounded checks). No default-Opus fan-outs.
- **Caching (§10's three facts):** fire one agent per shared-prefix family, await first token,
  then fan out; don't assume cheap-tier ⇒ cheap fan-out (Haiku's 4,096-token cache floor —
  moot here since the roster is Sonnet/Opus, noted for any future haiku extraction stage);
  escalate tiers only at phase boundaries.
- **Write isolation:** every implementing agent gets `isolation: worktree`; lanes return
  fixed-format summaries (files touched · tests added · falsifier · golden status), never raw
  context. Synthesis binds in the orchestrator.
- **Run discipline:** the wf-harness prelude (stop signals, null-result alarm paired with
  rediscovery ranking, disagreement records) applies as-is; report-only per Jordan's ruling.
- **Stop conditions:** a wave that would move a golden it did not declare, touch a D row, or
  need a §5 ruling STOPS that lane and files the item — it does not improvise (§0.1 #4: no
  uncontrolled result gets banked because it looked favourable).

## §5 · Held for Jordan (loud, per ED-1094 — nothing here ratifies on merge)

| # | Fork | OI | Default on offer | Blocks |
|---|---|---|---|---|
| 1 | Two mass-battle trees: declare / adapter / promote — **held AND adjudicated in MB plan §7 fork 1; cross-session visibility row only** | OI-11/14/47 | none (MB plan poses all three) | all MB centralization + honest MB battle resolution in-campaign |
| 2 | ED-MB-0010 fabricated-emit deletion — **executed by the MB session as E1** (merge-ratification with ledger flip, "cheapest independent win") | OI-21 | delete | dangling-emit zero; MB workbench cards |
| 3 | ED-1051: flip `engine_clock` `doc:null` → `propagation_spec_v1.md` | OI-43 | the long-standing default | T0/M1 juncture 6; GO Gate-0 |
| 4 | `env.crisis` consumer (or ruled terminal) | OI-22 | none named anywhere | last dangling emit |
| 5 | `scale_signature` extension to province/duchy/country per B12 | OI-35 | extend enum + registry defaults | scales above territory |
| 6 | ED-SC-0004 canonical Argue-pool formula (legacy stub vs σ-kernel) | OI-48 | none (P0 docket) | contest single-owner; ED-SC-0011 bridge lands either way as B |
| 7 | Turmoil writer + `parliamentary_vote` L-restoration | OI-31/32 | none — both flip campaign outcomes (~72% winners) | honest victory/mandate loops |
| 8 | Dual-emit attribution (scene.dialogue / scene_entered / belief_revised) | OI-29 | assign single canonical emitter each | contract truth completeness |
| 9 | Retire-candidates: `settlement_economy`, `campaign_architecture`; NPC lane ownership | OI-43/59 | fold/retire per GAP-K2/K3; lane = Jordan's | contract hygiene |
| 10 | ED-IN-0029 attribute-roster docket (Character dataclass gate) | OI-50 | docket UNRULED — do not bind | any typed actor schema (explicitly NOT in P1/P2 scope) |
| 11 | §1.0-class design forks carried unchanged (ED-IN-0049 §3.3 body, ED-SC-0005 cap, Field/Gauge primitive, ED-SC-0015; damage-law canon = MB plan fork 6) | various | per their own dockets | named stages only |

**What P1 does about these meanwhile:** stub-flag, never fake. The investigation branch runs as
a flagged stub until FI design lands; MB battles keep resolving on the wired tree exactly as
today — the staleness and its fix are wholly the MB session's (fork #1 there); this plan adds
no flag inside MB files and does not touch the `faction_action.py:349` seam.

## §6 · Sequencing, cost, and M1

Wave 1 → 2 are strictly ordered (spine before seams); Waves 3 and 4 can interleave after 2;
Wave 5 last. Expected shape: 5 PRs, ~45 agent-tasks total, Sonnet-heavy (~70%) with Opus on
~10 gating nodes — consistent with §10's ladder (the expensive tier sits where being wrong is
silent). M1 alignment: Waves 1–3 directly serve junctures 2–7 (dispatch, echo, season close
visibility); nothing here pre-empts the T0 wall (ED-1051 stays Jordan's).

**Register maintenance:** `02_execution_ledger.md` (created by Wave 5, appended by every wave)
is the single status surface for OI rows — this plan and the register itself stay immutable
snapshots (statuses live in one place, per workplan v6 §0's anti-drift rule).
