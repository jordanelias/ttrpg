# Session handoff — 2026-08-24, branch `claude/hub-and-bus-contract` (PR #329)

> **⚠ DO NOT MERGE PR #329 AT ITS CURRENT HEAD (`e4070d4`).** The last commit is a deliberate WIP:
> `engine/tests` is fully green (2055 passed) but `tests/valoria` has ~24 residual failures from a
> half-finished engine port. The exact list is in §5. Everything BEFORE that commit (`d080a36` and
> earlier) was green and is mergeable on its own.

**Read next, in this order:** `proposals/2026-08-24-error-regions-v1.md` (11 error regions as
executable plan items — this is the primary deliverable of the session), then §5 below (the port's
open tail), then §6 (culling/centralization state).

---

## 1. What was ruled this session (Jordan, all 2026-08-24)

These are now in `CLAUDE.md` and bind future sessions:

1. **§0.05 — CODE IS THE MECHANISM, PROSE IS REFERENCE.** *"Whatever mechanisms we have that rely on
   prose are worthless. We rely on code ONLY for the game work; our design documents in .MD are
   reference and information only."* With a table of what is/isn't a mechanism and the test: *if this
   document were deleted, would the game behave differently?*
2. **§0 — `needs_jordan` is not a parking space.** Five-test escalation ladder (superseded /
   irrelevant / answered by a design document / answered by precedent / answered by architecture).
   Escalate only what survives all five.
3. **No `.md` sweeping unless prose is explicitly named.** Enforced as a `PreToolUse` hook
   (`tools/hook_md_sweep_guard.py`), not a paragraph.
4. **Work-item triage** — if it doesn't concern code it isn't a work item; **but** unbuilt mechanic
   proposals are kept ("code that doesn't exist yet is still code to me").
5. **Port `tests/sim/mass_battle` over `systems/mass_battle/sim`** (§5).

**⚠ §0.05 HAS A LIMIT I GOT WRONG AND A LATER SESSION MUST NOT REPEAT.** "The code is the formula"
resolves **doc-vs-code**. It does **not** resolve doc-vs-doc when the code implements *neither*
value, and it **cannot** resolve **code-vs-code**. I filed 20 ledger rows as "answered by §0.05";
3 of 3 spot-checked were misfiled. `ED-SC-0004` is two live Argue-pool formulas in two live modules —
a genuine Jordan fork, not a prose defect.

---

## 2. Repository state — measured, not estimated

| | lines | note |
|---|---|---|
| `engine/` + `systems/` (non-test) | **41,501** | includes the ported engine (was 30,159 before the port) |
| `tests/valoria/` | 29,602 | ≈ the size of all game code |
| `tools/` | 16,593 across **56** modules | was ~106 modules before the culling waves |
| `engine/tests/` | 4,060 | **the only suite that executes the game** |

**The shape to keep in view:** the *graded* surface (`tests/valoria`) is seven times the size of the
surface that *plays the game* (`engine/tests`). An audit measured **~36% of `tests/valoria` (~51
files, ≈10,800 lines) has apparatus — a tool, registry, ledger, doc or another test — as its
subject**, after crediting the bridge/exporter/milestone guards to the game side.

**A guard chain has re-formed at depth 4**, the shape §0.3 documents:
`game ← tests ← tools/ci_vacuous_assertion_check.py ← tests/valoria/test_vacuous_assertion_check.py`.
Report-only, one rung shallower than the deleted `test_wf_harness_check.py`.

**This session's own output ratio was 11:1 apparatus-to-game** (+904 `tools/`, +436 `tests/valoria`,
+120 game code), in a session whose subject was centralizing the game. That is §0.3's **T2** term,
and §6 records that no plan addresses it.

---

## 3. What actually shipped and is green (commits `5cd99ee` … `d080a36`)

- **Convictions centralized.** Three incompatible rosters (9 / 8 / 13) collapsed to one owner:
  `references/descriptor_registry.yaml:conviction_roster` → `tools/export_descriptors.py` →
  `engine/engine_params/descriptors.json` → `engine.substrate.descriptors.CONVICTIONS` → read by
  `conviction.py` and `npe.py`. **A ratified mechanic that was a silent no-op now runs**: ED-912
  §6.1's Close-Knot-break Scar hit an unknown-name branch and returned `magnitude=0` on every call
  while the caller reported `conviction_scar = 1`.
- **`tools/export_module_contracts.py` + `engine/engine_params/module_contracts.json`** — the
  contract interface is cooked, and its `path_to_module` block is the single owner of the
  directory→contract-module binding that nothing owned before.
- **`tools/contract_runtime_conformance.py`** — runs a seeded campaign and asks the engine what it
  emits. **Not wired into CI anywhere** (deliberate; see §5).
- **`tools/hook_md_sweep_guard.py`** + 12 tests pinning that it is *wired*, not merely present.

---

## 4. The measurement that should drive the next session

From `contract_runtime_conformance.py` (n=2, seed 0):

```
EMITS     declared 60   observed  3   matched 0
CONSUMES  declared 82   observed 13   matched 0
397 emissions, from exactly THREE call sites, none of which any contract claims.
```

The 60-edge gap splits cleanly:

- **29 edges** belong to 7 modules with **no implementation path** — the ED-1051 authoring backlog.
- **31 edges** belong to 10 modules that **have code and emit nothing** — the real wiring gap:

```
scene_slate (8) · fieldwork_knots (4) · peninsular_strain (4) · social_contest (4)
faction_state (3) · personal_combat (3) · threadwork (2) · miraculous_event (1)
piety_track (1) · settlement_layer (1)
```

**Five of those already have a live subscriber** (`mechanical.mission_shift`, `state.scar_acquired`,
`meta.knot_formed`, `scene.combat_resolved`, `scene.combat_felled` — all subscribed at
`engine/cross_scale/articulation.py:116-130`). Wiring one closes a loop end-to-end and moves
`observed` from 3 to 4, which is falsifiable. **This is the recommended first action next session.**

Two Key types flow that **no contract declares**: `scene.accord_echo` and
`meta.cascade_cluster_event` (both in `key_types.json`, both subscribed). `--check` exits 1 today.

---

## 5. THE OPEN PORT — `tests/sim/mass_battle` → `systems/mass_battle/sim` (commit `e4070d4`)

**Done and verified:**
- 11,342 lines / 28 modules moved; imports rewritten to `systems.mass_battle.sim.*`; the
  `tests/sim` `sys.path` seam deleted from 42 test files.
- **Determinism preserved** — the canon engine drew from the global `random` at 7 sites; the engine
  it replaced threaded `rng` end-to-end after a documented 2026-05-20 fix. New
  `systems/mass_battle/sim/rngsource.py` is the single owner; `resolve_mass_battle` scopes
  `world.rng`. Verified byte-identical across two same-seed runs.
- **The strategic adapter survived** — `massbattle.py` is now *only* `resolve_mass_battle`,
  `_faction_to_unit`, the garrison stub and the degree map, carried over **field-for-field
  unchanged** so the golden delta is attributable to the resolution model alone.
- **A duplicate degree ladder was eliminated** (the `massbattle.compute_degree` twin died with the
  port; one implementation remains at `systems/mass_battle/sim/resolution.py`).
- All six campaign goldens re-recorded with notes. `engine/tests`: **2055 passed**.

**Two findings inside the re-record that are NOT re-pins — do not absorb these silently:**
1. **`da.public_governance` dropped to ZERO emissions** while the key total stayed at 187
   (battle_concluded 80→67, contest_resolved 105→120). One of only three production emitters has
   gone silent at seed 42. **Open, FA lane.**
2. **"The spine can shut a faction out entirely" no longer holds.** Pinned two-sided with the open
   question: real invariant, or artefact of the old resolution model?

**Residual red in `tests/valoria` (~24) — the port's tail:**

| family | n | what it needs |
|---|---|---|
| `test_mass_battle_systems_movement` | 8 | behavioural expectations written against the old engine |
| `test_flow_skeletons` | 5 | anchors into the rewritten `massbattle.py`; **not remappable by diff** — the file is new, they need re-authoring |
| `test_field_golden_pins` | 5 | env/pin classification over the new module set |
| `test_public_governance_transfer_key` | 3 | the emitter that went silent |
| `test_tool_input_paths_resolve`, `test_structure_audit`, `test_morale_write_sweep`, `test_import_cycle_game_state_npe` | 3 | path + cycle registers |

Also red locally: `ci_co_file_checker`, `ci_sim_fabrication_check`. `sim_params.json` grew 320 → 420
constants and surfaced a genuine collision: **`SEED_BASE` is defined twice in the canon engine** —
`bat.py` 1,000,000 vs `lanchester_signature.py` 2,000,000.

---

## 6. Culling / optimization / centralization — where the plans actually stand

Surveyed from the full plan corpus. **Do not execute from the RATIFIED culling plan text** — four of
S6's six instructions were measured wrong when run, and the corrections live only in the execution
order's RESULT blocks. Nothing reconciles the two documents.

**Done:** culling waves 1–3 (`dashboard/`, `tools/observability/`, session machinery, wf harness,
meta-gates); wave 5 (untrack generated); `deprecated/` → `FORK:baf29d5`; 6b (ledger fragments →
`registers/archive/`); 6e (`wiring_manifest` folded into `export_composition --check`); execution
order S1–S6; the S5 exporter→artifact→leaf pattern now has **seven instances**.

**Open, with owners:**
- **S7 — `audit/` extraction.** 230 files / 79,126 lines. **It needs no design**: it already exists
  executably in `tools/evacuation_plan.py` and as a named list in the culling plan. **Two
  shipping-gate tests read `audit/` paths**, so a naive fork breaks CI:
  `test_audit_plan_ids_are_allocated.py:245` (plus a `MIN_HEADER_DOCS = 40` corpus floor) and
  `test_evacuation_plan.py:293-304` (which *requires* the contest-groundup parity oracle be
  classified `relocate`). Sizing: ~6 files move to code homes, ~35–40 extract, ~185 (~72%) fork.
- **⚠ The most dangerous single item in the tree:** the **Churn-engine parameterization exists only
  in `audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md`** — a
  `RATIFIED` head referenced by `CURRENT.md:40`, with **no implementation anywhere** in `engine/` or
  `systems/`. Under §0.05 the game's ratified narrative layer has no mechanism at all. It must
  **move, not fork** (already ruled at culling-plan `:220-221`).
- **6d** (vocabulary fold) — blocked on re-ruling a standing "architecturally backwards" call.
- **6c** — reclassified: its "≥75% narrative" headline measured **21%**, and 12/17 `[DONE]` sections
  carry live `needs_jordan` content. It is adjudication work now, and the 2026-08-24 ruling licenses
  a session to do most of it.
- **S8 Half B** (three contradicting faction-action Ob conventions) — **suspended on a Jordan ruling**.
- **S9 / B2 / B3** — game-repo ratchet + first executing GDScript test.
- **S10** — zero-assertion counters; `faction_action_errors` / `scene_resolver_errors` appear nowhere
  in `engine/`.

**Two ledger/tree disagreements to reconcile before S7 compounds them:**
`references/restructure_ledger.md:1277` declares `audit/2026-08-06-vector-audit/` forked while
`structure_audit/data/structure_metrics.json` is still on disk and line-anchored from two live
systems heads; inversely `audit/2026-08-03-session-oddities.md` is cited by `tools/build_fork.py:20`,
is absent from disk, and has **no ledger row**.

### The finding that matters most here

**No plan addresses T2, and two say so explicitly.** `return-to-game-plan §6`: *"T2 is only
half-addressed… rewriting the reward is a Jordan decision… deliberately not attempted here."* The
Stop hook has since been **emptied**, which deleted the apparatus-facing grade **without installing a
game-facing one**. `execution-order §3a` finding 2 is the sharpest statement: **"no game regression
can currently red CI"** — `m1_acceptance.py` is one of 12 `level: 5` rows that cannot fail the build,
and its own row 4 is DOC-DERIVED, so the one game signal is structurally incapable of a green verdict.

Two concrete closures exist on paper and **neither has an owner**: wire `m1_acceptance` rows 1–2
(the execution-bound ones) into a blocking tier, and execute S10.

---

## 7. Largest unexecuted work, measured by the GAME

1. **The ruled-but-unwired obstacle model** — *"the obstacle is the opponent's score/2 plus that
   instance's modifiers"* (Jordan, 2026-08-14/15). `HANDOFF.md:238` already calls it the largest
   outstanding piece. `DECISIVE_OB = 3` is ruled dead; the migration has a measured balance delta
   (a held case moves 2.5% → 47.5% against a 40% ceiling).
2. **The MB canon-engine reconciliation** — *partly done by this session's port*, and the remaining
   half is §5's tail plus the `da.public_governance` silence.
3. **The `Faction.adjust` Key spine** — 30 of 31 call sites emit no Key. Everything centralized so
   far is the **read** side; nothing yet centralizes the **emit** side. No plan step owns it.
4. **The 321 numeric constants still defined inside `systems/`** — §0.05 names this the migration
   backlog.

---

## 8. On goldens, since it was asked

They matter, but **not as correctness claims** — at n=2 and n=8 they cannot separate a balance change
from noise, and `test_f7_smoke_oracle.py:8` still demands an n≥100 oracle that does not exist. What
they are is **change detectors**: their job is *"did this move output, and did you know it would?"*
That is worth more during active work, not less, because it is the only thing that catches an
unintended behaviour change — and the values themselves are cheap to re-record.

The real hazard is the one `CLAUDE.md` §7 already names: **the re-pin path is uncontrolled**, nothing
verifies a regeneration was intended. This session is a worked example of the distinction — six
goldens were re-recorded as routine, and the same run surfaced **two things a scalar pin could not
see**: an emitter going silent while the key *total* stayed identical at 187, and a property
assertion ("the spine can shut a faction out") that quietly stopped being true. Those two are worth
more than all six re-pins combined.

**Rule of thumb for the next session:** re-record a value pin without ceremony; **never** re-record a
*property* assertion without reading what it claimed and deciding whether the claim is still true.

---

## 9. Session error record

`proposals/2026-08-24-error-regions-v1.md` — 11 regions, each a defect that shipped or was published,
each with the lesson and the plan item. **The master pattern is R1: discriminators that do not
discriminate** — six times a classifier or filter separated something other than what its name
claimed, twice driving a bulk operation reverted in full (149 work items; 17 ledger rows). Both had a
counterexample findable in two minutes; neither was looked for, because both predicates were
*plausible*.

Four Fable-5 critics were run against this session's own published claims and overturned three
numbers. **Four of the six defects they found were the instrument's model of the registry, not the
engine** — none came from the game.
