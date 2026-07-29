# Connective-Tissue & Compliance Orchestration Plan v1

## Status: PROPOSED (merge ratifies per ED-1094, EXCEPT the §5 held-back forks — those are Jordan's alone) — ED-IN-0091, 2026-07-29

**Adversarially reviewed and reconciled 2026-07-29.** A `fable`-tier read-only critic scored this
plan, the register, and the two inbound sections against the working tree and the other two plans;
**17 findings, all reconciled the same day, folded in at source.** Two of them overturned claims this
plan made (the zero-collision claim, which is true of code files and false of shared registry files;
and OI-53's staleness). The two artifacts that carry the reconciliation:
**`02_disposition_map.md`** — the authoritative OI→owner table, seeded here at plan time, which
Wave 5 now diffs against instead of re-deriving; and **`03_adversarial_review_2026-07-29.md`** — the
findings register with the adjudication for each.

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
  mapping (OI-26 — **a scheduled post-E3 batch (PC §15 I4), not a conditional rider**: it runs the
  §12 wrapper audit and produces the mapping table, which this program's Wave 3 consumes; promoted
  2026-07-29 per critic F11, because §12's own "if budget" framing cannot gate a cross-session
  deliverable).
  **Declared seam:** `combat_engine_v1/wrapper.py`'s public resolve API. Wave 1's dispatch
  bridge (OI-01) lives entirely on the IN side of that seam (`engine/cross_scale/`), consuming
  the wrapper as-is; if the bridge needs a wrapper change, the item is filed to the PC session,
  never edited here. (Coordination note: the PC plan flags wrapper.py as its own §12 blind
  spot — the bridge pins the wrapper at the seam with a characterization test that is
  **SHAPE/CONTRACT-LEVEL ONLY**.)

**Seam terms for the wrapper — the goldens problem, stated (critic F2).** PC's E1b/E2a/E2b/E3a/E3b
change roster-wide damage *on purpose*. The moment the bridge routes combat through the wrapper,
those changes reach IN-owned campaign goldens (`engine/tests/test_f7_smoke_oracle.py` pins
`scenes_resolved`). Three terms make that safe rather than accidental:

1. **The characterization test asserts shape, never outcome** — result schema, determinism under a
   fixed seed, and the presence of the fields the bridge consumes. It never pins a damage value, a
   win rate, or any balance quantity. A PC batch that rebalances the roster must not turn this test
   red; if it does, the test was written wrong.
2. **The bridge ships FLAG-OFF.** A named flag (`DISPATCH_COMBAT_BRIDGE`, default off) gates the new
   path, and Wave 1 proves **byte-identical goldens with the flag off**. The flip to ON happens only
   **after PC batches E0–E3 have merged**, as a deliberate, single-owner (IN session) golden
   re-record citing both plans in the PR body — never as a side effect of a wave.
3. **The reach oracle asserts combat under the flag**, and xfails those rows while it is off — so the
   burn-down list stays honest about what is wired versus what is merely reachable.

**Golden families — one owner each (critic F3).** The MB plan's G11 ("one golden-moving PR globally")
was written inside one lane and reads, globally, as a serialization of all three sessions. It is
therefore **scoped, not overruled**, into three families with one owner apiece:

| Family | Contents | Owner |
|---|---|---|
| MB goldens | `tests/sim/mass_battle` digests, `bat.py` batteries | **MB session** |
| PC reference tables | `combat_armour_reference.json` and its siblings | **PC session** |
| Campaign goldens | `engine/tests/` — F7 smoke oracle, pipeline-reach | **IN session** (this plan) |

**G11 restated: one golden-moving PR in flight PER FAMILY.** A change that would cross families
requires a coordination note in root `HANDOFF.md` **before** the PR opens. Inside the MB family, the
MB plan's own G11 text remains authoritative.

**ORDERING (critic F10).** MB §12 and PC §15 land in **PR #252** — this program's PR. **PR #252
merges BEFORE the MB/PC sessions branch from `main`; the three-session concurrency begins after that
merge.** A session that branches earlier reads a plan with no inbound section and will silently drop
the routed items.

**Shared non-code files — the conventions that keep three sessions off each other (critic F4/F5/F6/F13).**
The zero-file-overlap claim below is true of *code*; these registry and generated files are the real
collision surface, so each gets a single writer:

| File | Convention |
|---|---|
| `registers/review_baseline.yaml` | **IN only**, among the three. CODEOWNERS-gated to Jordan; a raise is an explicit ED with a loud call-out, never a silent edit (Wave 1 / Wave 4 protocols below). |
| `references/id_reservations.yaml` | **Nobody touches it mid-run.** Wave 0 pre-allocates all three sessions' ED blocks in one commit before the sessions start. |
| `references/module_contracts.yaml` | MB owns rows `:465-486` (mass_battle) and its E1 deletion; **IN owns the rest**. The hunks are distant and git-mergeable; each session's PR touches only its own rows. |
| Generated observability artifacts (`graph.json`, incompleteness, the PROPOSALS family) | **IN is the sole regenerator**, at Wave 5. MB's E1 edits *sources* only and defers regeneration here. |
| `CURRENT.md` | MB's E4 edits only MB's own subsystem rows/status lines; IN's Wave-5 stamp reconcile runs **last** among the merges it can see and touches only the stamp + IN-owned rows. |
| Lane handoffs | IN writes **only** `HANDOFF_IN.md` and root `HANDOFF.md`; never a carved-out lane's handoff while its session is live. |

**The routing is physical, not referential:** every item this program identified that the two
dedicated plans did not already carry has been appended to them — **MB plan §12** (stubwire
conversion of `altonian_reinforcements` with a suggested slot, the two MB import cycles, the
`test_persubunit_stress.py` `sys.path` residue **as corrected by the 2026-07-29 critic pass — a
redundant duplicate insert, not a retired root**, F8; F6/F7 token reconciliation; the coordination
bullets and seam declaration) and **PC plan §15** (pool-formula + 8.0-anchor single-owner riders on
E0/M15, the wiring audit's dead list as an M12 rider, `sel_*`/`point_concentration` shape hygiene,
the `_emit()`→Key mapping **promoted to a scheduled post-E3 batch with a named home file**, F11/F16;
seam declaration) — both in this PR. A dedicated session reading only its own plan misses
nothing. **For every register row that routes to neither dedicated plan, `02_disposition_map.md` is
the equivalent guarantee** — one named owner per row and per split half, with no "covered somewhere"
cell (critic F1).

This is §3's session-lane-scoping made structural: zero **code**-file overlap ⇒ zero merge
collisions on the subsystem trees. **The claim does not extend to shared registry and generated
files** — that overreach is the critic's F4/F5/F6/F13, and the single-writer table above is the fix.
If a future directive carves out another lane (SC is the obvious candidate), the same recipe applies:
route the register rows, append the items to the lane's plan, declare the seam, characterize it with
a shape-level test, assign the shared files a single writer, never cross it.

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
- **Duplication logging discipline (Jordan directive, 2026-07-29 — binding on all three
  sessions).** The *known* multi-definition defects are scheduled with sole owners (Wave 4 here;
  PC E0/M15+I1; MB B1/B2; one owner per item in `02_disposition_map.md`). For a duplication
  DISCOVERED mid-work — a rule, value, formula, or name defined in more than one place that the
  current task is not load-bearing on — the rule is **log, don't chase** (§0.1 #5): file an
  `ED-<LANE>-NNNN` in the discovering session's lane citing (a) every definition site found,
  (b) the proposed single owner, (c) why it was out of scope — and keep moving. Never fix it
  inline out-of-scope (scope creep dragged ~100 pre-existing uncited constants into a blocking
  gate once, §0.1); never leave it unlogged (an unlogged duplicate is invisible until it
  diverges silently). The editorial ledger IS the duplication log — no new register. Wave 5's
  capstone collects the EDs so filed into the next round's work-list.
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
- **Zero unconditional `NotImplementedError` in live trees, EXCEPT files under an accepted
  cross-session handoff**, each cited in the reach oracle's xfail manifest — **currently exactly
  one: `systems/mass_battle/sim/altonian_reinforcements.py` → MB plan §12 I1** (critic F9: an IN
  exit criterion may not be hostage to another session's schedule). Every other OI-17 stub is
  converted to a self-flagging stub-wire (§2.1); the stub count is a *visible, decreasing* telemetry
  line, not a hidden crash class.

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
  never stored (single-owner rule applied to the flag itself). **Seed the baseline at the FULL
  expected converted set, INCLUDING the MB-owned `altonian_reinforcements`** (critic F4): MB's later
  §12-I1 conversion then moves the count in the improving direction only and trips nothing on a
  Jordan-gated file that IN is the sole writer of.
- Falsifier: `tests/valoria/test_stubwire.py` — converts a fixture stub, asserts the audit
  attribute + telemetry + ratchet all see it; mutation check: delete the import, all three fail.

### 2.2 Dispatch closure — no silent deferral
`scene_dispatch._resolve_slot` gets a total mapping: every `scene_type` → canonical resolver or
`stubwire`. Concretely: `combat` → `combat_engine_v1/wrapper.py` behind a **`[SEED]`
party-derivation bridge** reusing the exact pattern `_emergency_council_parties` established
(ED-SC-0006/0007 — derive combatants from the same faction aggregates, no invented actors),
retiring the deprecated `systems.combat.sim.combat` call (OI-01). **PC-seam terms** (the three
numbered terms in the lane-partition block, critic F2): the bridge is IN-side only
(`engine/cross_scale/`), consumes the wrapper's public API as-is, and ships a **shape/contract-level**
characterization test — result schema, determinism under a fixed seed, presence of the fields the
bridge consumes, **never an outcome or balance value**. It ships **behind `DISPATCH_COMBAT_BRIDGE`,
default OFF, with byte-identical goldens proven in the OFF state**; the flag flips ON only after PC's
E0–E3 have merged, as one deliberate IN-owned campaign-golden re-record citing both plans. Any
wrapper-side need is filed to the PC session (lane partition above). `investigation`/`fieldwork` → stub-wired
resolvers (OI-02) until FI designs land; the `"resolver not live"` string is deleted — the
fallback becomes `stubwire`, which is visible.

### 2.3 `engine/tests/test_pipeline_reach.py` — the acceptance oracle (OI-56)
Seeded campaign; asserts per §1 with explicit coverage counting (`assert checked >= N` per
§0.1 #2 — a direction that never came up is a FAIL, not a skip). Ships red-marked (xfail rows
per unwired direction, each citing its OI row); waves flip rows to strict as they land. The
xfail manifest IS the live P1 burn-down list. Two manifest rules follow from the seam terms:
**combat rows assert under `DISPATCH_COMBAT_BRIDGE` and xfail while it is off** (F2), and **a file
under an accepted cross-session handoff gets a manifest row naming the owning plan item** — today
exactly one, `altonian_reinforcements.py` → MB §12 I1 (F9). **Re-entry (F17):** if MB fork 1 is ruled
"promote", the oracle's MB battle-resolution rows flip to stub-flag the moment the ruling lands and
stay there until the spawned FA-lane wiring item re-pins them (§5 row 1).

---

## §3 · Waves

Sizing respects the default guideline (≤15 agents per workflow run); each wave = one Workflow
invocation + one PR. Model tiers per CLAUDE.md §10: **Sonnet implements, Opus adjudicates,
critics are `valoria-critic` via `hCritic`** (read-only by construction). Every write lane runs
`isolation: worktree`. Orchestrator (this session class) plans and gates; it does not author
artifacts (Jordan's 2026-07-28 Fable-placement ruling). Workflow scripts are authored at
execution time from `tools/wf_harness.js` via `python tools/ci_wf_harness_check.py --fix`
(edit the owner, never a copy) and path-checked with `ci_claude_workflow_paths.py`.

### Wave 0 — Preflight (no code): ruling docket + instrument integrity + ID pre-allocation — ~5 agents
| # | Stage | Agents | Tier |
|---|---|---|---|
| 1 | Assemble the §5 Jordan docket as one decision surface (options + defaults where they exist, per workplan §5 row format) | 1 | opus |
| 2 | Fix orphan-detector integrity BEFORE any triage acts on its output (OI-55: `__init__` misresolution, CLI-entry labeling) + known-answer tests for `vector_audit` core | 2 | sonnet |
| 3 | **Pre-allocate the three sessions' ED blocks** in ONE commit to `references/id_reservations.yaml` before the concurrent sessions start (critic F5) | 1 | sonnet (effort low) |
| 4 | Critic pass on all three | 1 | valoria-critic (opus) |

**The ID pre-allocation, concretely.** `id_reservations.yaml` is one YAML mapping with hand-maintained
comment provenance — three live sessions bumping `next_free` mid-run is precisely the same-lane
collision class §3 documents, on the one file with no merge-friendly structure. So: allocate the IN
block from the IN lane, plus a small **MB** and a small **PC** block from their lanes, recorded in the
file's comment per its own ALLOCATION PROTOCOL, in a single commit; **after that commit no session
touches the file for the duration of the run.** One-line mirrors of this term live in MB §12 and
PC §15.

Exit: docket filed in the PR body + **`HANDOFF_IN.md` / root `HANDOFF.md` only** — cross-lane items
are filed as §5-docket / `02_disposition_map.md` lines and flagged in the PR body for the lane
session to ingest, **never written into a live lane's handoff** (critic F12; the MB plan's §10 makes
its orchestrator the sole writer of `HANDOFF_MB.md`, and the same courtesy is owed PC). Detector
fixes land with expected-delta tests (§0.1: the orphan list may shrink — record the delta, don't
celebrate it silently); the three ED blocks are allocated and the file is frozen for the run.
**Falsifier:** known-answer fixture where a fake orphan/cycle must be found and a labeled
CLI entry must NOT be.

### Wave 1 — The P1 spine: stubwire + dispatch closure + reach oracle — ~8 agents (IN lane)
| # | Stage | Agents | Tier |
|---|---|---|---|
| 1 | Build §2.1 stubwire + telemetry + ratchet signal (seed `stubs.count` per the F4 term below) | 1 | sonnet |
| 2 | Build §2.3 reach oracle (OI-56; xfail manifest from the register) | 1 | sonnet |
| 3 | §2.2 dispatch closure: combat bridge behind `DISPATCH_COMBAT_BRIDGE` (OI-01) · investigation/fieldwork stub-wire (OI-02) — 2 parallel worktree lanes | 2 | sonnet |
| 4 | Convert the OI-17 Pass-2l stub class → stubwire (pipeline over ~19 files; mechanical, uniform — EXCLUDES the MB-owned `altonian_reinforcements.py`, handed to the MB session with the stubwire recipe), **plus the self-flag/stub-wire halves of OI-18, OI-19 and OI-10 per the scope note below** (`02_disposition_map.md` rows OI-18a / OI-19 / OI-10a) | 2 | sonnet (effort low) |
| 5 | Contract-conformance adjudication of the combat bridge (Key IN → resolver → OUT closure, module-adjudicator method) | 1 | **opus** |
| 6 | Adversarial critic relay over the whole wave's diff | 1 | valoria-critic (opus) |

**Stub-conversion scope, stated exhaustively** (critic F1a — these halves were dropped between
register and plan): the conversion stage covers the OI-17 class **plus OI-18's B half** (the contest
GAMES router's `consensus`/`negotiation`/`inquiry` rows and the `DyadicMode`/`NegotiationMode`/
`CeremonialMode.play` scaffolds — **self-flag only**; the actual game builds stay gated on the SC P0
docket, ED-SC-0003..0005, §5 row 14) **plus OI-19's partial branches** (`tribunal.py:149`,
`treaty.py:107`, `contest/dictionaries.py:710`; `resolver.py:51` is a benign abstract base and is
left alone, recorded as such). OI-10's stub-wire half rides the same pipeline; its *naming* half is
§5 row 12.

Exit: `pytest tests/valoria` + `engine/tests` green; reach oracle red rows reduced per manifest;
**zero unconditional raises in live trees except the one accepted cross-session handoff**
(`altonian_reinforcements.py` → MB §12 I1), which carries a named xfail-manifest row (critic F9).
`stubs.count` seeded in `registers/review_baseline.yaml` at the full expected converted set including
that file (critic F4). **Falsifiers:** test_stubwire mutation check;
reach-oracle rows for combat/investigation flipped to strict **under `DISPATCH_COMBAT_BRIDGE`**;
byte-parity probe that with the flag OFF the combat bridge changes NO existing golden — if a golden
moves in the OFF state, the wave stops and says so (the ON-state re-record is a separate,
deliberately-scheduled IN action after PC's E0–E3 merge, §2.2).

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
7. **The full OI-12 list** (critic F15 — the earlier shorthand silently dropped four members) →
   stubwire or a one-line wire where the design doc already specifies the call site (OI-09/12):
   `engine.autoload.npc_ai`, `systems.characters.sim.companion`,
   `systems.overview.sim.{rs_track, ip_track}`,
   `systems.threadwork.sim.{co_movement, collective, opposing, rendering}`,
   `systems.world.sim.{miraculous_event, restoration_movement}`,
   `systems.settlements.sim.{settlement, temperaments}`,
   `systems.social_contest.sim.parliamentary_stay`, `engine.autoload.registry`. Verify-before-wiring
   per the detector's own caveat (Wave 0 fixed its `__init__` misresolution first, OI-55).
Exit: reach-oracle direction rows for bottom-up echo, vertical-up, NPC/knot/settlement chains
strict; `structure_audit` orphan count measurably down with the delta recorded in the PR.
**Falsifiers:** per-lane — e.g. a seeded campaign where a faction loses then regains a territory
(OI-04); an NPE season over a now-populated store asserting ≥1 npc action (OI-05, with
`assert checked >= 1`).

### Wave 3 — Keys & contract truth — ~10 agents (IN lane + per-lane one-liners)
1. Wire `scene.combat_resolved`/`_felled` declared consumers minimally (npc_behavior/
   faction_state `apply=` handlers + articulation trigger rows, OI-22/OI-27's ED-IN-0004 slice).
2. ~~`_emit()` vocabulary mapping~~ **→ PC session** (OI-26 edits PC-owned files; the IN-side
   half — registering/consuming the 4 canonical `scene.combat_*` types — lands with item 1).
   The PC side is now a **scheduled** post-E3 batch (PC §15 I4) whose deliverable is a mapping table
   at `audit/2026-07-26-combat-balance-customization-state/wrapper_emit_key_map.md`; **this wave
   CONSUMES that table** and remains the sole editor of
   `systems/_architecture/key_type_registry_v30.md` (critic F11/F16). If the table has not landed,
   item 1 still ships — the registry-side wiring does not block on it — and the consumption is
   recorded as outstanding rather than guessed at.
3. Contract truth sweep (sonnet pipeline): OI-24's npc_behavior residue, `doc:` repoint
   (C-KEY-2), faction_politics `state:` block (OI-20's contract half — its **sim** half is a
   deferred FA-lane build, §3.5), MS ownership declaration (OI-32's mechanical half; Turmoil is
   §5 row 7), and **OI-40's IN half — the 4-vocabulary scale reconciliation** across contracts and
   token registers (critic F1a). The EXPLORATORY cross-scale locality metric stays a **D** row: it
   is deferred by its own audit, not by omission. (`mass_battle` contract honesty note = MB plan E6;
   the MB half of OI-40 = MB plan E4/E5/E8 + §12 I4 — neither is here. **Contract-file convention:**
   MB owns rows `:465-486`, IN owns the rest, and each PR touches only its own rows, critic F6.)
4. Register the OI-30 Category-B scalars in `descriptor_registry` (mechanical; C2 stays J, §5 row 11).
5. `causes[]`/`targets[]` population at the emitters the armature already specifies (OI-28) —
   authoring-guidance from `political_dynamics_keys_migration_v30.md`, cited per site — **and, at
   the same six emit sites, clear ED-WR-0003's hard-coded `private_observers`** (OI-31's B half,
   critic F1a; the ED is WR-lane, so it files to `HANDOFF_WR.md` even though the emitters are
   IN-owned).
6. Opus adjudicator: emit-closure re-run (module-adjudicator) + critic relay.
7. **Key the silent emitters (OI-25, ED-IN-0014):** `settlement_layer`'s revolt/auto-capture gates
   (`g_ord0`/`g_def0`), `ci_political`, `victory`'s era/occupation transitions, and
   `territorial_piety` (in-0/out-0 INERT) currently have zero Key integration in either their
   CANONICAL docs or their contracts. Declare the emits in the contracts and register the types;
   consumers follow the same rule as item 1 — a declared consumer or a ruled disposition, never a
   dangling emit added by this wave. (New item, critic F1a: OI-25 was owned by no wave.)

Exit: dangling-emit count **4 → ≤1** (`env.crisis` held for §5), **or ≤2 while ED-MB-0010's row
(MB plan E1) has not yet merged — that row is excluded from this wave's denominator** (critic F6:
its deletion is the MB session's ED-1094 ratification, not ours to wait on or to do). Adjudicator
emit-closure ≥ its 2026-07-13 97.9% with the residual named. **Falsifier:** adjudicator run BEFORE
vs AFTER in the PR, plus a campaign asserting ≥1 consumed `scene.combat_resolved`
(`assert checked >= 1`).

### Wave 4 — Centralization (P2, live trees) — ~10 agents (PC/SC/IN lanes)
1. ~~PC dedups~~ **→ PC session** (OI-44/45/46 ride the PC plan's E0 ownership pass — M15's
   literal census is the same defect class; this wave touches nothing under `systems/combat/`).
2. Import-cycle break (OI-52): `game_state ↔ npe` only (contest cycle stays, documented
   intentional-during-rebuild; both MB cycles → MB session).
3. **Dead-root sweep (OI-53) — RE-SCOPED against the working tree** (critic F7: the register's OI-53
   was partly stale, and a wave executing it as written would have re-implemented a landed fix).
   **Already done, do not redo:** `ci_quantity_vocabulary_check` routes through
   `ci_common.sim_reference_roots()` (ED-IN-0087) *and* already has a recurrence guard
   (`tests/valoria/test_retired_tree_apparatus.py`); `build_apparatus_registry` is fixed; the
   `mechanics_index` `sim_module:` paths verify live. **Genuinely remaining:**
   `tools/audit_staleness.py:69`, `tools/observability/build_decisions.py:57`,
   `tools/workplan_status.py:71`, and — the critic's own addition (F14) —
   `tools/ci_audit_registry_check.py:23`, which still scans the retired `designs/audit/`.
   **Method, binding:** re-verify each site at execution (a fifth may have landed meanwhile, a
   listed one may have been fixed), route every fix through the **EXISTING** single owner
   `ci_common.sim_reference_roots()`, and **EXTEND the existing guard test** — adding
   `designs/audit/` to its scan set. **Never ship a second owner or a second guard** (§8: every rule
   lives once; F7 exists because the register implied building what already exists). The one
   MB-owned site (`test_persubunit_stress.py:17`) is the MB session's — and is **not** a retired
   root at all, see F8 / MB §12 I3.
4. Contract↔code join (OI-54): `sim_module:` field populated 27/27 (or explicit `none` with
   reason), `structure_audit` correspondence check upgraded from name-match to join-verified,
   report-only `review_core` signal.
5. **Mechanical sweep bucket** (sonnet, effort low): ruled-but-unexecuted class (OI-51) +
   currency-layer orphans (OI-57) + **orphaned tools and the registry-generator inconsistency
   (OI-15)** — `build_audit_registry_backfill.py`, `geography/jsx_to_canonical.py`,
   `measure_stamp_false_positives.py`, `observability/npc_audit_report_gen.py`, and
   `sim_harness/harness.py`'s `invoked_by: []` vs `orphaned: false` — **+ the `tools/registry.py`
   facade and the missing converged pointer artifacts (OI-16)**: either give the facade a consumer
   or retire it to `deprecated/tools/`, and either author `references/head_pointers.yaml` /
   `docs/REPO_MAP.md` or record them as not-to-be-built; **+ OI-32's dead constant/field slice**
   (`VICTORY_THRESHOLD`, `game_state.py:101`). OI-15/16 were owned by no wave before the critic's
   F1a; retirement decisions here follow the ED-1082 precedent (grep every workflow/hook/skill for
   the filename before moving).
6. Opus verifier (goldens/parity) + critic relay.
Exit: `review_core --check` no regression; every dedup carries its equality/parity test.
**`vocab.a17` delta protocol, pre-declared** (critic F4): `registers/review_baseline.yaml` is
CODEOWNERS-gated to Jordan and IN is its sole writer among the three sessions. If the un-blinded
scan surfaces new vocabulary debt, **the wave STOPS**, records the measured delta, and files the
baseline raise as an explicit ED for Jordan with a loud call-out per ED-1094 — **it never edits the
baseline silently**, and it never lowers a *different* row to compensate.
**Falsifiers:** per-dedup mutation check (perturb the single owner, every former call site
moves); the dead-root guard test red on a planted regression **in each of its scan roots, including
the newly-added `designs/audit/`**.

### Wave 5 — Capstone: verify, re-measure, re-baseline — ~6 agents
1. Re-run the full observatory (structure_audit, vector-audit refresh — clears the stale
   families, OI-58) and diff every §Counts metric vs this register: orphans, dangling emits,
   stub count, cycles, correspondence. **IN is the sole regenerator** of the generated artifacts
   (`graph.json`, incompleteness, the PROPOSALS family) — MB's E1 defers its regeneration here
   (critic F6), so this pass must pick up E1's source edit if it has merged, and say so if it
   has not.
2. Reach oracle strict-row census vs §1 — **this is where OI-36's directional roll-up is settled**
   (2 of 7 Key-delivery directions live at register time; the census is the after-measurement).
   Remaining xfails must each cite a §5 fork, a D row, or an accepted cross-session handoff row (F9).
3. Completeness critic (opus): "what's missing — an OI row whose owner in `02_disposition_map.md`
   did nothing, a claim with no falsifier artifact, a golden re-recorded without a loud callout?"
4. 2× independent refuter critics over the capstone claims (majority kill per §10).
5. File per-lane EDs for everything executed **from the block Wave 0 pre-allocated** (F5);
   update **`HANDOFF_IN.md` and root `HANDOFF.md` only** — never a carved-out lane's handoff while
   its session is live (F12); **CURRENT.md stamp reconcile runs LAST** among the three sessions'
   merges it can see, and touches only the stamp + IN-owned rows (F13).
Exit: this folder gains `04_execution_ledger.md` mapping OI-nn → PR/ED/falsifier/outcome, and
**every row MATCHES `02_disposition_map.md`** — which is the authoritative ownership table, **seeded
at plan time, not invented at capstone time** (critic F1c). The capstone's job is a *diff* against
that table (done · stub-flagged · held at §5 · deferred to a lane per §3.5 · D), not a fresh
attempt to prove nothing was dropped. A row whose owner did nothing is a recorded miss, not a
silently-reworded success.

## §3.5 · Deferred-to-lane table (critic F1a — build-scale work this program does NOT do)

These register rows are real, open, and **not** owned by any wave above. Each is build-scale work
belonging to a lane's own workstream rather than to this connective-tissue program — deferring them
is a routing decision, not an oversight, and it is recorded here so a sweep does not re-file them and
a capstone does not claim them. Every line names its lane, its one-line rationale, and where it is
tracked. `02_disposition_map.md` carries the same assignments as its `DEFERRED → <lane>` rows.

| OI | Item | Lane | Rationale | Tracked in |
|---|---|---|---|---|
| OI-20 (sim half) | `faction_politics` has zero sim representation despite a 1115-line CANONICAL doc | **FA** | Building the module is a faction-subsystem workstream; this program only makes its *contract* honest (Wave 3 item 3) | `HANDOFF_FA.md` · workplan v6 faction stage |
| OI-34 | Convergence Markers (8): no detector, Key type, contract, or sim | **WR** (narrative stage) | A narrative-detector build with its own design surface, not connective tissue; ED-IN-0003 remains its ledger home | ED-IN-0003 · `arcs/registers/arc_register_events.md` |
| OI-37 | L/PS pipeline fully SPEC-ONLY; `lps_inert_check` 100/100 red | **SE** | **The SE lane's own highest-priority item** (`HANDOFF_SE`: "single highest-priority open item in this entire thread"). **This program does not pre-empt a lane workstream** | `HANDOFF_SE.md` · ED-FA-0004 |
| OI-38 | No event_deck runtime (28-card Goldenfurt deck prose-only) | **SE** | M2-critical-path settlement build with its own card-store/predicate design; the harness prototype is not a port target | `HANDOFF_SE.md` · workplan v6 M2 |
| OI-39 | NPC ambition-tick absent from the Accounting cascade | **WR** (NPE) | Dossier schema is fully specified; the advancing code is a world-subsystem build, and its lane is confirmed by §5 row 9 | workplan v6 NPE stage · §5 row 9 |
| OI-41 (build half) | Design-blocked cross-scale mechanics (caste cascade, CI-consent axis, insurgency pipeline, fracture resolution, §5.2/§5.3 armature, territorial-tier propagation) | **FA / SE / WR** per item | Each is gated on its own docket and is subsystem design work; the *ruling* half is §5 row 11 | the named dockets · §5 row 11 |
| OI-43 (B half) | Doc homes for the other 8 `doc:null` modules (audit, domain_actions, game_director, npc_memory, scenario_authoring, scene_slate, scene_timer, settlement_economy) | **FA / SE / WR / IN** per module | Authoring a home doc is canon authorship in the owning lane; only `engine_clock`'s pointer flip (§5 row 3) is on this program's critical path | `references/module_contracts.yaml` · ED-FA-0002 (domain_actions) · §5 row 9 (retire-candidates) |
| OI-48 (B half) | ED-SC-0011 — the personal-party contest bridge | **SC** | Contest-subsystem build; it lands as B either way, but it is the SC lane's to schedule alongside ED-SC-0004 (§5 row 6) | `HANDOFF_SC.md` · ED-SC-0011 |
| OI-59 (B half) | Grounding the two `[ASSUMPTION]`-grade integration hubs (`faction_state` in-13, `npc_behavior` in-12) | **WR** (pending the fork-9 lane ruling) | Grounding a resolver is subsystem design, and the NPC family has no owning lane until §5 row 9 is ruled | §5 row 9 · `HANDOFF_WR.md` |

**The rule this table encodes:** a row leaves this program only with a named lane and a named
tracking surface. "Someone else's problem" is not a disposition; "SE lane, `HANDOFF_SE.md`" is.

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
- **Golden families (critic F3, binding):** goldens are partitioned into three families with one
  owner each — **MB** (`tests/sim/mass_battle` digests, `bat.py` batteries), **PC**
  (`combat_armour_reference.json` and siblings), **IN** (`engine/tests/` campaign goldens: F7,
  pipeline-reach). **G11 applies per family: one golden-moving PR in flight PER FAMILY.** A change
  that would cross families requires a coordination note in root `HANDOFF.md` **before** the PR
  opens. This *scopes* the MB plan's G11 for cross-session purposes; inside the MB family the MB
  plan's own G11 text is authoritative.
- **Stop conditions:** a wave that would move a golden it did not declare, move a golden **outside
  the IN family**, touch a D row, edit `registers/review_baseline.yaml` other than the two
  pre-declared protocols (Wave 1 seeding, Wave 4's `vocab.a17` delta), touch
  `references/id_reservations.yaml` after Wave 0's pre-allocation commit, or need a §5 ruling
  STOPS that lane and files the item — it does not improvise (§0.1 #4: no uncontrolled result gets
  banked because it looked favourable).

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
| 11 | §1.0-class design forks carried unchanged (ED-IN-0049 §3.3 body = OI-06's J half; ED-SC-0005 cap; the Field/Gauge primitive = OI-49; ED-SC-0015; OI-27's registry-contradiction slice — `meta.cascade_cluster_event`, `state.opinion_revised`, zoom-trigger `type_id`s; OI-30's C2 npc-quantity call; OI-41's design-blocked cross-scale set; OI-42's `decay()`/OF-3 fork; damage-law canon = MB plan fork 6) | OI-06/27/30/41/42/49 + various | per their own dockets | named stages only |
| 12 | Placeholder-name rulings for the 8 placeholder-named FA/MB sim modules (`varfell_mandate_action`, `varfell_territorial_acquisition`, `altonian_reinforcements`, `infrastructure_reclamation`, `home_sanctuary`, `hafenmark_equipment`, `charter_liberties`, `tactic_cards` + `mass_seizure`) | OI-10 | none — the `registers/placeholder_names.yaml` rows are unresolved | naming closure; the stub-wire half is B and lands in Wave 1 regardless |
| 13 | `settlement_layer` L/PS `bucket:` tag — derived_value (F1-guarded) vs writable track; Mandate-feedback F1 coverage | OI-33 | none | contract truth for the L/PS pipeline (whose build is SE-lane, §3.5) |
| 14 | Contest GAMES **build** (`consensus`/`negotiation`/`inquiry` + the Dyadic/Negotiation/Ceremonial `play` scaffolds) — gated on the SC stage-4 P0 docket (ED-SC-0003..0005) | OI-18 | defer to the SC docket | SC-lane build; the **self-flag** half is B and lands in Wave 1 |

**J-completeness (critic F1b).** Rows 12–14 and row 11's expanded citation list exist because the
docket previously cited no OI id at all for seven J-classed register rows (OI-10, OI-18, OI-27,
OI-30, OI-33, OI-41, OI-42) and carried two more (OI-06, OI-49) only as ED/primitive names inside
row 11's prose, where no sweep would find them. The invariant now holds and is checkable:
**every register row carrying a J component appears above, or is explicitly routed to an MB/PC
fork.** Twenty rows carry a J component (6 wholly J-classed, 12 mixed B/J or M/J, 2 D/J); two of
them route to MB forks (OI-11 → row 1 / MB §7 fork 1; OI-21 → row 2 / MB E1) and the remaining
eighteen map onto rows 3–14. `02_disposition_map.md` is where that mapping is written down per row,
and Wave 5 diffs against it rather than re-deriving it.

**Re-entry protocol for row 1 (critic F17).** A fork-1 **"promote"** ruling does not land cleanly:
it invalidates the reach oracle's MB battle-resolution rows (they are pinned against the
currently-wired tree) and it orphans `faction_action.py:349`, which is an **FA**-lane file owned by
neither the MB nor the IN session. So the ruling **spawns an FA-lane wiring item** — the seam is
FA-owned and moves on FA's schedule — and **the IN reach-oracle's MB rows flip to stub-flag the
moment the ruling lands and stay there until that FA item re-pins them.** Neither session
"just moves the call site" as part of executing the ruling. The same term is recorded in MB §12's
seam declaration.

**What P1 does about these meanwhile:** stub-flag, never fake. The investigation branch runs as
a flagged stub until FI design lands; MB battles keep resolving on the wired tree exactly as
today — the staleness and its fix are wholly the MB session's (fork #1 there); this plan adds
no flag inside MB files and does not touch the `faction_action.py:349` seam.

## §6 · Sequencing, cost, and M1

**PR #252 (this PR, carrying MB §12 + PC §15 + the reconciliation artifacts) merges first, before
the MB and PC sessions branch from `main`** — the three-session concurrency begins after that merge
(critic F10). Then: Wave 0 first (it pre-allocates all three sessions' ED blocks, F5); Wave 1 → 2
strictly ordered (spine before seams); Waves 3 and 4 can interleave after 2; Wave 5 last, and its
`CURRENT.md` stamp reconcile runs last among the merges it can see (F13). One cross-session
dependency is scheduled rather than assumed: **the `DISPATCH_COMBAT_BRIDGE` flip to ON waits on PC's
E0–E3 merging** (F2), and is an IN action on IN-family goldens.

Expected shape: **6 PRs** (one per wave, W0–W5), ~48 agent-tasks total, Sonnet-heavy (~70%) with
Opus on ~10 gating nodes — consistent with §10's ladder (the expensive tier sits where being wrong is
silent). M1 alignment: Waves 1–3 directly serve junctures 2–7 (dispatch, echo, season close
visibility); nothing here pre-empts the T0 wall (ED-1051 stays Jordan's).

**Register maintenance:** `04_execution_ledger.md` (created by Wave 5, appended by every wave) is
the single **status** surface for OI rows — this plan, the register, `02_disposition_map.md` (the
**ownership** surface) and `03_adversarial_review_2026-07-29.md` (the review record) stay immutable
snapshots (statuses live in one place, per workplan v6 §0's anti-drift rule). The two surfaces are
deliberately separate: ownership is decided once, at plan time; status changes every wave. The
ledger was numbered `02_` before the 2026-07-29 reconciliation created the disposition map at that
number; it is `04_` from here.

**Folder contents (post-reconciliation):** `00_open_items_register.md` (rows) ·
`01_orchestration_plan_v1.md` (waves — this file) · `02_disposition_map.md` (ownership, authoritative)
· `03_adversarial_review_2026-07-29.md` (the 17-finding review + adjudications) ·
`04_execution_ledger.md` (status, created by Wave 5).
