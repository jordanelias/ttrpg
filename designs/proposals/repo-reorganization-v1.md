# Repository Reorganization (v1) — content-class taxonomy + phased migration

## Status: PROPOSED — HELD FOR JORDAN (ED-IN-0071, 2026-07-15 · Lane: IN, cross-cutting all lanes · Jordan-vetoable throughout). A hard architecture call, filed so it stops evaporating — **not** a routine-merge item. Merging tracks the proposal only (ED-1094 reconciliation-map pattern, cf. ED-IN-0069); it authorizes **no** file move. **The primary axis is now decided on evidence (§2a): subsystem, not scale.** Several sub-forks RULED by direct Jordan input 2026-07-15; the rest stay HELD-BACK (§5).

**Provenance.** Jordan raised, in conversation, reorganizing the repo around its code architecture/schema. A corpus search found it recorded **nowhere** — no ED, proposal, or decision-queue row (only workplan v6 §5 "queue 21–23", tier T2-H3, narrow ledger-path cleanup). It fell through the same continuity gap that (same session) left the workplan board a week stale and mis-filed a workplan-reconciliation under `designs/audit/`. This doc is the register hook.

---

## §1 — Adversarial critique of the current structure

Current top-level: `archives · canon · deprecated · designs · docs · engine · handoffs · params · references · research · sim · skills · tests · tools · versions`.

| # | Current placement | What it actually is | The incoherence |
|---|---|---|---|
| 1 | `archives/` vs `deprecated/` | archives = dead **content**; deprecated = dead **code/machinery** | Leaks: `deprecated/canon/` holds dead ledger content; `archives/audit/` is indistinguishable from `designs/audit/`. Two graveyards, one unenforced rule. |
| 2 | `references/` vs `research/` | references = internal **index layer**; research = external **inbound source material** | `references/` is an overloaded junk drawer (`arcs/`, `historical/`, `engine_params/`, a workplan, `npc_registry.sql`, `effort-guide.md`); `references/historical/` overlaps `research/`. |
| 3 | `params/` | A parallel **numeric-truth layer** | Prose tables, not typed data → can't be ingested, and duplicate numbers already in the design docs (§5 drift risk). Content masquerading as data. |
| 4 | `tests/` at root + `tests/sim` + `tests/sim_framework` vs root `sim/` | `sim/` = real oracle; `tests/sim/` = narrative records; `tests/sim_framework/` = retired harness; only `tests/valoria/` executes | Worst offender: `tests/` is ~5% executable, ~95% historical prose. Naming collision (sim ×3) + category collision. |
| 5 | `designs/godot/` vs `designs/videogame/` | Same subsystem, two folders + a 3rd home (`designs/audit/2026-06-10-godot-conversion-strategy/`) | Pure accretion — three homes for one port. |
| 6 | `designs/workplans/` | The live steering surface | Process/steering nested inside `designs/` as if a design artifact. |
| 7 | `engine/` (2 files) | Sigma-leverage *armature* prose | Vestigial; overlaps `designs/architecture/`; the real "engine" (executable model) is `sim/`. |
| 8 | `designs/arcs/` | Generated **narrative content** | Neither system-mechanics nor world-canon; split from its `references/arc_register*` registers. |
| 9 | audit subfolders **everywhere** (24 in `designs/audit`, +`archives/audit`, `tests/audit`, `skills/*-audit`) | "Audit" is both a place and an activity dumping artifacts wherever the session ran | Findings never promoted-then-archived → the landfill. |
| 10 | editorial/patch **registers** under `canon/` | Object-level world-truth mixed with meta-level process ledgers | The editorial ledger is *about* canon — it isn't canon. Constitution + legislative record in one folder. |

**Through-line:** no distinction between an artifact's *content class* and the *activity that produced it*, and no lifecycle (produce → promote → archive). Folders accrete by "where the session worked," not "what kind of thing this is."

---

## §2 — Target taxonomy (13 primaries)

**✓ RULED** = decided by direct Jordan input 2026-07-15. **⊘** = fork, see §5.

| Primary | Contents | Status |
|---|---|---|
| `canon/` | World/design truth ONLY (philosophy, amendments, timeline, constraints). Registers move out. | core |
| `registers/` | All process ledgers (`editorial_ledger*`, patch/supersession registers, `id_reservations`, collision/naming/apparatus/audit registries). | core — ⊘ handoffs placement |
| `systems/` | Design docs by **subsystem**, laid out per §2a; `ui/` lives here. | **✓ RULED axis (§2a)** |
| `arcs/` | Narrative content + `references/arc_register*`. | ✓ RULED — own primary |
| `proposals/` | Unratified proposals (from `designs/proposals/`). | ✓ RULED — own primary |
| `research/` | External source material + `references/historical/`. | ✓ RULED — own primary |
| `engine/` | Executable model (Python): `sim/mc_v18.py`, `params/`, typed `engine_params/`. | ✓ RULED — MC + params here |
| `godot/` | The Godot port, consolidated (strategy doc + `skeleton/` + `designs/{godot,videogame}`); the `res://` project (§6). | ✓ RULED — own primary |
| `audits/` | In-flight audits only, under a lifecycle rule (§7). | core — ⊘ lifecycle rule |
| `workplans/` | Master workplan + progress board. | core |
| `infrastructure/` | `skills/`, `tools/`, CI, hooks, structural-observatory; also `scene_timer`/`audit` telemetry (§7). | core |
| `dashboard/` | Published status site (`docs/dashboard/`). | core |
| `deprecated/` | Everything dead — `archives/` merged, split `content/` vs `code/`. | core |

### §2a — `systems/` is subsystem-organized (RULED, evidence-backed)

The axis was a real fork — **scale** (matches the `sim/` package layout) vs **subsystem** (matches the ID lanes / CURRENT.md / handoffs). Decided **subsystem**, on two grounds:

1. **Isomorphism.** One subsystem = one folder = one ID lane = one CURRENT.md row = one `HANDOFF_<LANE>.md` = one Godot module tree (§6). Today those four indices agree with each other but not with the folder tree; this aligns all five.
2. **The co-location cost is measured and small.** Co-locating each subsystem's `sim/` scripts beside its design `.md` requires splitting the scale-packaged `sim/`. From the vector-audit import graph (`g_code.json`, §6): of 178 `sim.*→sim.*` edges, **104 stay intra-subsystem, 60 point at shared homes (`engine`/`_architecture`), and only 14 become cross-folder** — and those 14 are real couplings that already exist (e.g. the parliamentary-vote kernel shared by `factions`↔`social_contest`; `knots`↔`conviction`; faction actions reaching `settlements`). 14 explicit import rewrites, not a shatter.

Layout — design `.md` at each subsystem's root, a `sim/` subfolder for its scripts:

```
systems/
  combat/            { *.md ; sim/ ← sim/personal/combat.py }
  social_contest/    { *.md ; sim/ ← sim/personal/contest/ + parliamentary_vote/stay }
  factions/          { *.md ; sim/ ← sim/provincial/ (faction+domain actions) }
  fieldwork/         { *.md ; sim/ ← sim/personal/{fieldwork,investigation,knots} }
  mass_battle/       { *.md ; sim/ }
  settlements/       { *.md ; sim/ ← sim/territory/ }
  character_generation/ { *.md ; sim/ ← sim/personal/{conviction,beliefs,companion} }
  threadwork/        { *.md ; sim/ ← sim/thread/ }
  world/             { *.md ; sim/ ← sim/world/ + sim/peninsular/ tracks }
  npcs/              { *.md ; sim/ }            # own folder (RULED)
  articulation/      { *.md ; sim/ }            # own folder (RULED)
  ui/                { *.md ; sim/ (starts empty — not Key-emitting, §7) }   # under systems (RULED)
  _architecture/     # substrate the gameplay rides on (RULED)
                     # Key substrate, propagation_spec, holonic_doctrine, scale_transitions,
                     # player_agency, clock_registry, narrative_engine ; sim/ ← sim/substrate + sim/cross_scale
```

Names normalized to **singular** to match the ID lanes. Scale becomes a frontmatter tag, not a folder level.

---

## §3 — Migration risk (why this is not `git mv`)

Paths/names are load-bearing (~16k citations, `canonical_sha__*` pins, co-file pairs). A move breaks: `canonical_sources.yaml` pins + `module_contracts.yaml` `doc:` paths; `workplan_status.py` `RELEVANT_PREFIXES`, `audit_staleness.py` `artifact_paths`, `dashboard.yml`/`audit-refresh.yml` filters, `.githooks/`; `audit_registry.jsonl`/`apparatus_registry.yaml` path fields; thousands of in-doc citations + co-file pairs; and the sim import graph (the 14 cross-folder edges from §2a, rewritten in lockstep). So: **tooling, not moves** — a path-rewrite pass + alias map, a citation-rewrite pass, an import-rewrite pass, a CI-path update, a co-file re-check — CI green at every step. The §6 vector-audit artifacts are the inputs to that tooling.

---

## §4 — Phased plan (cheapest / highest-value first)

Each phase independently mergeable, CI green throughout. **None executes until §5's remaining forks are ruled + sequencing approved.**

1. **P0 — Registers out of `canon/`** → `registers/` (cited by ID, low blast radius). Update ledger readers + workflow/hook refs. Proof-of-tooling.
2. **P1 — Promote easy primaries**: `workplans/`, `proposals/`, `arcs/`, `dashboard/`, `research/` (+`references/historical`), `infrastructure/` (`skills`+`tools`).
3. **P2 — Collapse Godot's three homes** → the `godot/` primary; sigma-leverage armature → `systems/_architecture/`; shells → `deprecated/`.
4. **P3 — `engine/` assembly**: `sim/mc_v18.py` + `params/` + `engine_params/`; rewrite `mc_v18` imports in lockstep with P4.
5. **P4 — `systems/` by subsystem + intra-system sim** (§2a): rehome `designs/*` → `systems/*`; distribute `sim/` subpackages into each `sim/`; apply the 14 cross-folder import rewrites. Full citation + import tooling. Do last.
6. **P5 — `tests/` disentangle + `audits/` lifecycle + `archives/`→`deprecated/`** (#1, #4, #9). Keep `tests/valoria/`; relocate narrative prose; add the audit promotion rule + misfile CI gate.

---

## §5 — Forks: resolved vs held-back

**RULED 2026-07-15 (direct Jordan input):** subsystem axis (§2a, evidence-backed); `arcs`/`proposals`/`research`/`godot` each own primary; `ui` under `systems`, mapped at Godot conversion (§6); `params`+`mc_v18` → `engine`; per-scale sim → `systems/<subsystem>/sim/`; npcs/articulation/ui own folders, singular names; `_architecture/` for the substrate tier.

**Still HELD-BACK (needs Jordan):**
1. `engine/` remainder — typed `engine_params/` under `engine/` (rec: yes); cross-scale sim (`sim/substrate`, `sim/cross_scale`) → `engine/` or `systems/_architecture/sim/`?
2. `registers/` vs `continuity/` — handoffs (prose) with the ledgers (data), or separate?
3. `mechanics_index.yaml` — register or canon-derived index?
4. `piety_track` home (module-census orphan, §7) — player conviction, fits no gameplay folder cleanly.
5. `audits/` lifecycle rule — promotion marker + misfile CI gate.
6. Sequencing — approve P0→P5, or reorder.

---

## §6 — Migration data sources + Godot conversion map

**Repo-shape inputs (reuse, don't re-derive).** The 2026-07-14 `valoria-vector-audit` / gameplay-subsystem-observatory runs left the machine-readable shape under `designs/audit/2026-07-14-{governance-vector-audit,gameplay-subsystem-observatory}/`:

| Artifact | Drives |
|---|---|
| `data/g_code.json` (import graph) | The sim-split / import-rewrite (the §2a 14-edge measurement came from this) |
| `data/g_cite.json` + `degrees.json` | Boundary placement (fewest-cut) + hub/substrate identification |
| `vector_audit/data/corpus_manifest.json` | The migration work-list (every file → target home) |
| `data/tokens.json` | Sequencing (biggest movers) |
| `graphs/module_flowchart.mermaid`, `structure/data/g_pointer.json` | Post-move stat-vocabulary resolution check |

**Godot conversion is a *map*, not a mirror.** Godot separates headless engine logic from presentation from singletons from typed data; the repo organizes by subsystem (logic+presentation together). The `ui`-under-`systems` fork (RULED) is resolved at conversion, not in the repo:

| Repo | → Godot `res://` |
|---|---|
| `systems/<sub>/*.md` | design source — not shipped |
| `systems/<sub>/sim/` (Python oracle) | `res://engine/modules/<sub>/` — GDScript `EngineModule` per module (1:1 oracle→port, ED-1050) |
| `systems/_architecture/` | `res://autoloads/` — `KeyBus`, `GameState`, `Resolver`, `EngineClock` singletons (the spine CLAUDE.md §6 says is defined nowhere yet) |
| `systems/ui/` | `res://scenes/` + `res://ui/` — presentation tree |
| `engine/engine_params/` | `res://resources/*.tres` — the `combat_engine_v1.json` pattern → Godot Resources |
| `engine/` (mc_v18, params) | not shipped — Python-side oracle/balance; its typed exports are the only bridge |
| `godot/` (primary) | **is** the `res://` project root (engine/modules, autoloads, scenes, ui, resources) + the strategy doc + skeleton |

**Payoff:** `godot/engine/modules/<subsystem>/` becomes a **folder-for-folder mirror of `systems/<subsystem>/sim/`**, and the oracle-parity check (Python ↔ GDScript) is a per-folder diff. This is a second, independent argument for the subsystem axis.

---

## §7 — Module-census blind spots to fix (from `module_contracts.yaml`, 27 modules)

- `ui` and `character_generation` map to **zero** engine modules (not Key-emitting) — their `sim/` starts empty. Legitimate; named so it isn't mistaken for an error.
- `piety_track` is **homeless** (player conviction) → §5 fork 4.
- `scene_timer` and `audit` are **telemetry, not gameplay** → `infrastructure/`, not `systems/_architecture/`.
- `campaign_architecture` is a stub already dissolved into 4 folders → **no folder**.
- `settlement_economy` flagged **RECOMMEND RETIRE** (phantom module — no doc/state/logic).
- Data bug to fix in passing: `mass_battle.scales = [scene]` (should be provincial).
- Coupling note (not a taxonomy failure): `faction_state` (13 producers) and `npc_behavior` (11) are terminal accounting **sinks** — every axis leaves them importing widely. Don't optimize the tree to "minimize cross-folder edges" (unwinnable); optimize for navigation + lane isomorphism (done).
