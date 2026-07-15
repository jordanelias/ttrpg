# Repository Reorganization (v1) — content-class taxonomy + phased migration

## Status: PROPOSED — HELD FOR JORDAN (ED-IN-0071, 2026-07-15 · Lane: IN, cross-cutting all lanes · Jordan-vetoable throughout). This is a hard architecture call filed so it stops evaporating — **not** a routine-merge item. Merging this PR ratifies only that the proposal is *tracked* (per ED-1094 the reconciliation-map pattern, cf. ED-IN-0069); it ratifies **no** taxonomy decision and authorizes **no** file move. Every fork in §2 and §5 is HELD-BACK for your explicit pick.

**Provenance / why this exists.** Jordan raised, in conversation, a suggestion to *reorganize the repository around its code architecture / schema*. A corpus search (ledgers, decision queues, workplan v6 §5 register, `designs/proposals/`, handoffs) found **no record of it anywhere** — no ED, no proposal, no decision-queue row. The only pre-existing structural-debt item is one line in workplan v6 §5 (*"queue 21–23 — stale branches · duplicate compilation homes · pre-restructure ledger paths"*, tier **T2-H3**, the lowest), which is narrow cleanup, not this. The suggestion fell through the same continuity gap that (same session) left the workplan board a week stale and bundled a workplan-reconciliation into `designs/audit/`: a call that needs human judgment, with no register hook, silently disappears. This doc is the hook.

---

## §1 — Adversarial critique of the current structure

Current top-level: `archives · canon · deprecated · designs · docs · engine · handoffs · params · references · research · sim · skills · tests · tools · versions`.

Ten incoherences, each grounded in the working tree:

| # | Current placement | What it actually is | The incoherence |
|---|---|---|---|
| 1 | `archives/` vs `deprecated/` | Intended: archives = dead **content** (superseded docs, `archives/workplans/`, `archives/audit/`); deprecated = dead **code/machinery** (`deprecated/{tools,skills,session_machinery,engine}`) | Boundary leaks: `deprecated/canon/` holds dead *ledger content*; `archives/audit/` holds *audit content* indistinguishable from `designs/audit/`. Two graveyards, one unenforced rule. |
| 2 | `references/` vs `research/` | references = internal **index layer** (canonical_sources, names_index, module_contracts, descriptor/apparatus/audit registries); research = external **inbound source material** (8-civ governance, pre-firearms formations, rhetoric) feeding `=> design hook` lines | The distinction is real, but `references/` is an overloaded junk drawer: it also holds `arcs/`, `historical/`, `engine_params/`, `mass_battle_redesign_workplan_v1.md`, `npc_registry.sql`, `effort-guide.md`, `D10_INTEGRATION_GUIDE.md`. `references/historical/` overlaps `research/` conceptually. |
| 3 | `params/` | A parallel **numeric-truth layer** — mechanical values lifted out of design prose into their own tables | Justified in theory, broken in practice (CLAUDE.md §5): the values are *prose tables, not typed data*, so they can't be ingested, **and** they duplicate numbers that also live in the design docs → the drift risk §5 warns of. Content masquerading as a data layer. |
| 4 | `tests/` at root **and** `tests/sim` **and** `tests/sim_framework` vs root `sim/` | Three unrelated things named "sim": root `sim/` = the real ~11.4k-LOC Python oracle; `tests/sim/` = **narrative markdown** sim *records*; `tests/sim_framework/` = a **retired** arc-test harness. Only `tests/valoria/` is executable pytest. | Worst offender. `tests/` is ~5% executable and ~95% historical prose (`emergent_arc_skeleton_*`, `coverage_matrix_archive_*`, `audit/`, `handoffs/`, `stress/`). Naming collision (sim ×3) **and** category collision (specs vs records). |
| 5 | `designs/godot/` vs `designs/videogame/` | Same subsystem, two folders. godot/ = 4 stale (2026-04-18) impl docs + the 1-of-27 non-compilable skeleton; videogame/ = a *single* file `godot_architecture_specification.md` | Pure accretion. The *governing* spec is a **third** home (`designs/audit/2026-06-10-godot-conversion-strategy/`). Three homes for one port. |
| 6 | `designs/workplans/` | The live steering surface (master workplan v6 + progress board) | A workplan is *process/steering*, not a *design artifact* — the map nested inside the territory. Workplan artifacts leak anyway (`designs/audit/` April sprawl, `references/…workplan…`, `designs/ui/…workplan…`). |
| 7 | `engine/` (top-level, 2 files) | Two markdown docs about the sigma-leverage *armature* (the harness code was retired to `deprecated/engine/`) | Vestigial. It's *architecture prose* that overlaps `designs/architecture/`. A 2-file top-level primary whose "engine" (the executable model) actually lives in `sim/`. |
| 8 | `designs/arcs/` | Generated **narrative content** (arc_expansion, arcs_16–35, scenario chains, throughline resolutions) | Arcs are neither system-mechanics nor world-canon — a third content class. And split: content in `designs/arcs/`, registers in `references/arcs/` + `references/arc_register*`. |
| 9 | audit subfolders **everywhere** (`designs/audit` ×24, `archives/audit` ×6, `tests/audit`, `tests/sim/**/audits`, `skills/*-audit`, `references/audit_registry`) | "Audit" treated as both a *place* and an *activity that dumps artifacts wherever the session ran* | Audit outputs are **never promoted-then-archived**, so every session's findings accrete in-place forever. `designs/audit/` has become the repo's session-output landfill. |
| 10 | editorial/patch **registers** under `canon/` | `canon/` mixes object-level **world/design truth** (philosophical_foundations, canonical_timeline, constraints, amendments) with meta-level **process ledgers** (10× editorial_ledger, patch_register, supersession_register, mechanics_index) | The editorial ledger is *about changes to* canon — it isn't canon. Canon is currently both constitution and legislative record. Object-level and meta-level conflated. |

**Through-line (the root cause).** Almost every incoherence is one failure: **no distinction between an artifact's *content class* and the *activity that produced it*, and no lifecycle** (produce → promote findings → archive the record). Folders accrete by "where the session was working," not "what kind of thing this is." That is why audits, workplans, and sims each have 2–3 homes.

---

## §2 — Resolved target taxonomy

Jordan's proposed nine buckets, kept — with the five folders his list omitted assigned a home, and the three ambiguities that would recreate the mess pinned. **⊘ = genuine fork, needs Jordan (see §5).**

| Target primary | Contents | Notes / fixes |
|---|---|---|
| `canon/` | World/design truth ONLY: philosophy (P-01..P-14), amendments, canonical timeline, constraints | Registers move OUT (#10). `mechanics_index.yaml` is a register → `registers/` (⊘ borderline: it's canon-*derived*). |
| `registers/` | All process ledgers: `editorial_ledger*` (11 files), `patch_register*`, `supersession_register`, `id_reservations`, `collision`/`naming`/`deprecated-terms` registries, `apparatus_registry`, `audit_registry`, `mechanics_index` | Fixes #10. ⊘ **handoffs**: continuity *prose* vs ledger *data* — group here, or keep a separate `continuity/`? |
| `systems/` | Design docs **by scale**: `personal/`, `provincial/`, `territorial/`, `world/`, plus `_cross/` for scale-spanning substrate (Key substrate, propagation spec, holonic doctrine, scale_transitions, player_agency, clocks/tracks, narrative engine, threadwork) | Replaces ad-hoc `designs/{scene,provincial,territory,…}`. The `_cross/` bucket mirrors the ID system's **IN** lane — the fix for "which scale does *clocks* belong to?" (answer: none, it's cross-cutting). ⊘ **params/**, **arcs/**, **ui/** landing spots below. |
| `audits/` | **In-flight audits only**, under a lifecycle rule | Fixes #9 *only with* a promotion policy: findings propagate to the system/register; the closed audit archives to `deprecated/`. Without the rule this is `designs/audit/` renamed. |
| `workplans/` | Master workplan + progress board (steering) | Promoted to primary (#6). |
| `engine/` | The **executable model**: the Python oracle (today's `sim/`) + the Godot port + the typed `engine_params/` exports | ⊘ Defines "engine = runnable code," resolving #7. The sigma-leverage *armature docs* go to `systems/_cross/` (they're architecture prose, not engine). Consolidates the three Godot homes (#5). |
| `research/` | External inbound source material (governance, pre-firearms formations, rhetoric) + `references/historical/` folded in | Kept as a primary (#2). It is neither our canon nor our systems nor an index. |
| `infrastructure/` | `skills/`, `tools/`, CI, hooks, the structural-observatory / "vector shape" self-description | Generators live here; the *published* view lives in `dashboard/`. |
| `dashboard/` | The published status site (today `docs/dashboard/`) | Primary, as Jordan proposed. |
| `deprecated/` | Everything dead — `archives/` merged in, split `content/` vs `code/` | Fixes #1 while keeping the dead-docs vs dead-machinery signal as subfolders. |

**Homeless-folder assignments (Jordan's list omitted these five):**
- **`sim/` → `engine/`** (as the executable model). ⊘ or keep `sim/` as its own primary if "engine" should mean the Godot runtime only.
- **`params/` + `references/engine_params/` → `engine/` (as data)** or co-located `systems/<scale>/`. ⊘ — this is the §5-fragile surface; it needs an explicit, deliberate home, ideally promoted to typed data.
- **`research/` → its own primary** (recommended).
- **`arcs/` → `systems/arcs/`** (narrative content) or a `content/` primary. ⊘.
- **`ui/` → `systems/ui/`** (minor).

---

## §3 — Migration risk (why this is not `git mv`)

CLAUDE.md is emphatic that paths and names are load-bearing (~16k citations, `canonical_sha__*` pins, co-file pairs). A top-level move breaks, non-exhaustively:
- `references/canonical_sources.yaml` SHA pins + `references/module_contracts.yaml` `doc:` paths
- `tools/workplan_status.py` `RELEVANT_PREFIXES`; `tools/audit_staleness.py` `artifact_paths`; `tools/dashboard_data.py`; `.github/workflows/dashboard.yml` path filters; `.githooks/` + `tools/valoria_local.py`
- `references/audit_registry.jsonl` + `references/apparatus_registry.yaml` path fields
- thousands of in-doc `designs/scene/… §x` citations and every co-file `*_index.md`/`*_infill.md` pair
- `references/id_reservations.yaml` allocation discipline is unaffected, but ledger `citations[]` paths are

So the migration needs **tooling, not moves**: a path-rewrite pass (with an alias/redirect map), a citation-rewrite pass, a CI-path update, and a co-file-pair integrity re-check — sequenced so CI stays green at every step. This is a real `IN`-lane cross-cutting project. Its size is exactly why it never self-started.

---

## §4 — Phased migration plan (cheapest / highest-value first)

Each phase is independently mergeable and leaves CI green. **None executes until the §2/§5 forks are ruled.**

1. **P0 — Registers out of `canon/`** (#10). Highest value, lowest blast radius (ledgers are cited by ID, not often by path). Move to `registers/`; update `tools/` ledger readers (`obs_core.py`, `currency_consistency_check.py`, `validate_ed_citations.py`, `ci_audit_registry_check.py`) + the ~12 workflow/hook path refs. Ship a path-map + a CI green-check.
2. **P1 — Collapse the duplicate homes** (#5, #7). Merge `designs/videogame/` + `designs/godot/` + the strategy-doc into `engine/godot/`; move the sigma-leverage armature docs to `systems/_cross/`; retire the empty shells to `deprecated/`.
3. **P2 — `tests/` disentangle** (#4). Keep executable `tests/valoria/` (rename the *directory* concept to what it is); relocate the ~95% narrative/audit prose (`tests/sim`, `tests/sim_framework`, `emergent_arc_*`, `coverage_matrix_archive_*`) to `deprecated/content/` or `audits/` per the lifecycle rule.
4. **P3 — Promote `workplans/`, `dashboard/`, `research/`, `infrastructure/`** to primaries (#2, #6). Mostly moving `docs/dashboard`→`dashboard/`, `skills`+`tools`→`infrastructure/`, folding `references/historical`→`research/`.
5. **P4 — `systems/` by scale** (the big one). Rehome `designs/{scene,personal,provincial,territory,world,architecture,threadwork,npcs,articulation,factions,arcs,ui}` into `systems/{personal,provincial,territorial,world,_cross,…}`. Requires the full citation-rewrite tool. Do last.
6. **P5 — `audits/` lifecycle** (#9). Introduce the promotion rule + a CI gate: an `audits/` artifact older than N days with no "promoted" marker warns; a `*workplan*`/reconciliation artifact under `audits/` fails (the §3-rule violation we found). Merge `archives/`→`deprecated/` (#1).

---

## §5 — Forks HELD-BACK for Jordan

Merging this PR resolves **none** of these — it only tracks them:

1. **`engine/` definition** — executable model (Python oracle + port + data), or Godot runtime only? Determines where `sim/` and `params/` land.
2. **`params/` home + fate** — co-locate per scale, put under `engine/` as data, or (recommended) promote to a typed engine-params layer and retire the prose duplication (closes the §5 drift risk).
3. **`arcs/` class** — `systems/arcs/`, a `content/` primary, or under `canon/`?
4. **`registers/` vs `continuity/`** — do handoffs (prose) live with the ledgers (data), or separately?
5. **`mechanics_index.yaml`** — register or canon-derived index (stays near `canon/`)?
6. **Scale partition of `systems/`** — confirm the axis (`personal/provincial/territorial/world/_cross`) and where threadwork (spans scales) and factions (provincial? cross?) sit.
7. **Sequencing authority** — approve the P0→P5 order, or re-prioritize (e.g. P4 first is possible but expensive).

Recommended first action if ratified: execute **P0 only** as a scoped proof-of-tooling, then re-evaluate.
