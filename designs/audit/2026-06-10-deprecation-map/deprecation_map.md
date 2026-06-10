# Valoria — Deprecation Map
**2026-06-10 · status: ACTIVE record · the legible companion to the hook-enforced `canon/supersession_register.yaml`**

**Purpose.** One place that answers "is this artifact still live, and if not, what replaced it?" — so a cold session pulls up the **current** master and resolver, never a superseded one. This file is the readable map; the **enforcement** lives in `canon/supersession_register.yaml`, which `valoria_hooks.supersession_check()` reads to warn (non-blocking) whenever a commit touches a superseded path.

`[SELF-AUTHORED — bias risk: the superseding artifacts were authored by my sessions. Mitigation: every "Current canonical" cell cites a committed SHA or ratified ED read live this session; partial supersessions are marked PARTIAL, not over-stated.]`

---

## 1 · Workplans — pull up **v3 only**

| Deprecated artifact | Status | Current canonical | Why | Authority |
|---|---|---|---|---|
| `designs/audit/2026-06-06-architecture-map/valoria_master_workplan.md` | SUPERSEDED (frozen record) | **`designs/audit/2026-06-10-master-workplan-v3/valoria_master_workplan_v3.md`** | Approved content (Waves 0–1, K8) carried into v3 with live status; file kept as the 06-06 approved record, banner in place; W-item IDs stay citable | commit `e471b694`; banner committed same |
| `designs/audit/2026-06-09-ecosystem-reconciliation/valoria_workplan_R2_2026-06-09.md` | SUPERSEDED (frozen record) | **v3** (same path) | Phases A–E carried; v3 §0 de-stales R2's carried docket and records A-1 executed | commit `e471b694`; banner in place |
| `valoria_delta_workplan_2026-06-09.md` (never committed) | SUPERSEDED | **v3** | Superseded first by R2, then v3; its "M4 BUILT (L1980–2483)" claim is **false** (M4 unbuilt → v3 LB-8) | R2 header + `e471b694` |

**Net rule:** the only master workplan is **v3**. The two older committed workplans carry in-file `> SUPERSEDED → v3` banners; `lane_assignments.yaml`'s source + entry queues already repoint to v3 IDs (`e471b694`).

## 2 · combat-v32 — **filed as deprecated** (resolver is the ratified engine)

"combat-v32" is the **proposal lineage**, not the canonical engine. The ratified personal-combat resolver is **`designs/scene/combat_engine_v1/`** (CANONICAL — ED-900/901/902/903/904; `canonical_sources` `resolution_engine`).

| Deprecated artifact | Status | Current canonical | Why | Authority |
|---|---|---|---|---|
| `designs/proposals/combat_v32_proposal.md` | **DEPRECATED** | **`designs/scene/combat_engine_v1/`** | Pre-ratification state-graph reframe PROPOSAL; self-marked "not canonical until ratification"; never ratified as a doc — the `combat_engine_v1` implementation is the ratified outcome | ED-900 |
| `designs/proposals/combat_v31_proposal.md` | **DEPRECATED** | `combat_engine_v1` | Earlier proposal in the same superseded engine-replacement line | ED-900 |
| `designs/audit/2026-05-28-combat-reframe/ners_verdict_combat_v32.md` | **DEPRECATED** (record retained) | `combat_engine_v1` | NERS verdict on a proposal the project did not ratify; kept as the honest v32 test record. **Banner added this session.** Clears this file's "registered to no concept" index-drift orphan | ED-900 |
| `designs/scene/combat_v30.md` | **PARTIAL only** — do **not** full-deprecate | `combat_engine_v1` (resolution); `config.py` (params) | RESOLUTION layer superseded 2026-06-04; **lore/flavor/non-resolution content retained and canonical** (banner already in file since 2026-06-04) | ED-900 |

**Caveat (load-bearing):** `combat_v30.md` is *partially* superseded. The register records it so the supersession is discoverable, but its non-resolution content stays canonical — a full deprecation here would delete live lore.

## 3 · Godot conversion framing — superseded-in-part by the strategy

| Deprecated artifact | Status | Current canonical | Why | Authority |
|---|---|---|---|---|
| `designs/godot/implementation_sequence.md` (G1–G7) | PARTIAL | conversion strategy Part VI (`…/2026-06-10-godot-conversion-strategy/godot_conversion_strategy_v1.md`) | G1–G7 phasing replaced by the gated Gate-0 → spine → wave sequencing | commit `b42aa03` (strategy's own supersedes-in-part clause) |
| `designs/godot/data_serialization_spec.md` | FRAMING only | conversion strategy Part V | Schemas now derive from `module_contracts.yaml` + Descriptor Registry, not the retired `sim_framework/state.py`; the `.tres` mechanics stay a reference | commit `b42aa03` |

The strategy itself is **current** (Lane C's governing spec). Its three same-day errata (adjudicator A1–A12, contracts v3, Gate-0 type set → ED-1009) are recorded in master-v3 §0 / LC-0c — an erratum note, not a deprecation.

## 4 · Already in `deprecated/` (recorded for completeness — no action)

| Artifact | Moved | Replacement |
|---|---|---|
| `deprecated/params/combat.md` (was `params/combat.md`) | 2026-06-04 (Jordan) | `combat_engine_v1/config.py` resolution values |
| `deprecated/canon/editorial_ledger*.yaml` (12 files) | 2026-05-28 | live `canon/editorial_ledger.jsonl` (JSONL store) |

These were physically relocated already; `deprecated/` is exempt from `forbidden_token_gate` and the abbreviation gate (frozen content).

---

## 5 · Enforcement model & residuals (how "only pull up v3" actually holds)

Two surfaces, deliberately layered:

1. **Read path — in-file banners.** A session that opens a superseded file sees `> SUPERSEDED → <current>` at the top. Done for both workplans and the v32 verdict. The two 150k combat proposals are covered by the register + this map; their in-file banners + `git mv` to `deprecated/proposals/` are the **Lane-B completion** (master-v3 **LB-13** audit-promotion) — deferred deliberately: prepending to inherited 150k files mid-parallel-session risks a `forbidden_token_gate` halt on unscanned legacy content and a wasteful full recommit, when relocation is the right fix.
2. **Commit path — `canon/supersession_register.yaml`.** `supersession_check()` warns on any commit whose paths overlap a register entry's `files_to_recheck`, naming the current canonical. This is the robust, hook-read "filed as deprecated" authority; this session added **9** entries (8 file-level + the combat_v30 PARTIAL note), total **17**.

**Residual that would make the commit-path warn fire *always* (not built here):** `supersession_check()` only runs if `canon/supersession_register.yaml` was fetched in-session; bootstrap does not currently fetch it. Wiring it into the bootstrap fetch set is a one-line Lane-B infra change — **propose, do not self-commit** (PI: architecture/hook text is Jordan-applied), and it sits behind the K-budget per master-v3 §2. Until then the register fires whenever the file is in the session's fetch set (e.g. any session that reads it, including consolidation work).

**Not deprecated (explicitly):** `weapon_axes_v2.md` (the *other* index-drift orphan) is live weapon-physics-S2 input, not combat-v32 — left untouched. The conversion strategy v1 and `combat_engine_v1` are current canon.
