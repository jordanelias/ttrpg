# Repository Reorganization (v1) — content-class taxonomy + phased migration

## Status: PROPOSED — HELD FOR JORDAN (ED-IN-0071, 2026-07-15 · Lane: IN, cross-cutting all lanes · Jordan-vetoable throughout). This is a hard architecture call filed so it stops evaporating — **not** a routine-merge item. Merging this PR ratifies only that the proposal is *tracked* (per ED-1094 the reconciliation-map pattern, cf. ED-IN-0069); it authorizes **no** file move. **Several taxonomy forks were RULED by direct Jordan input 2026-07-15 (see §2 / §5)** — those are settled; the remaining forks and all execution stay HELD-BACK.

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

Thirteen top-level primaries. **✓ RULED** = decided by direct Jordan input 2026-07-15. **⊘** = still a fork, see §5.

| Target primary | Contents | Status |
|---|---|---|
| `canon/` | World/design truth ONLY: philosophy (P-01..P-14), amendments, canonical timeline, constraints. Registers move OUT (#10). | core |
| `registers/` | All process ledgers: `editorial_ledger*` (11), `patch_register*`, `supersession_register`, `id_reservations`, collision/naming/deprecated-terms registries, `apparatus_registry`, `audit_registry`. | core — ⊘ handoffs placement (§5) |
| `systems/` | Design docs **by scale**, one folder per system, laid out per §2a. `ui/` lives here. Scale-local sim scripts co-locate here (see §2a). | core — ⊘ scale roster/names (§5) |
| `arcs/` | Generated narrative content (arc_expansion, arcs_16–35, scenario chains, throughline resolutions) + the `references/arc_register*` registers. | **✓ RULED — own primary** |
| `proposals/` | Unratified design proposals (today `designs/proposals/`), promoted out of `designs/`. | **✓ RULED — own primary** |
| `research/` | External inbound source material (governance, pre-firearms formations, rhetoric) + `references/historical/` folded in. | **✓ RULED — own primary** |
| `engine/` | The **executable model** (Python side): `sim/mc_v18.py` (the Monte-Carlo campaign core), `params/` (numeric layer), and the typed `engine_params/` exports. | **✓ RULED — MC + params here** |
| `godot/` | The Godot port, consolidated: the conversion-strategy doc, `skeleton/`, and the impl docs from `designs/{godot,videogame}` (#5, three homes → one). | **✓ RULED — own primary** |
| `audits/` | **In-flight audits only**, under a lifecycle rule (#9): findings promote to the system/register, the closed audit archives to `deprecated/`. | core — ⊘ lifecycle rule (§5) |
| `workplans/` | Master workplan + progress board (steering). Promoted to primary (#6). | core |
| `infrastructure/` | `skills/`, `tools/`, CI, hooks, the structural-observatory / "vector shape" self-description. Generators here; published view in `dashboard/`. | core |
| `dashboard/` | The published status site (today `docs/dashboard/`). | core |
| `deprecated/` | Everything dead — `archives/` merged in, split `content/` vs `code/` (#1). | core |

### §2a — Intra-`systems/` layout (RULED)

Every system is a folder whose **design prose (`.md`) sits at its root**, with a **`sim/` subfolder holding all that system's executable scripts** — co-locating the 1:1 Python oracle beside the design it implements:

```
systems/
  scenes/                        # personal-scale resolution
    social_contest/
      social_contest_v30.md      # + _index, _infill, params tables, etc. (prose at root)
      sim/                       # this system's scripts (from sim/personal/contest/, …)
    combat/
      combat_*.md
      sim/                       # from sim/personal/ combat modules
  provincial/
    mass_battle/  { *.md ; sim/ }
  territory/
    settlement/   { *.md ; sim/ }        # from sim/territory/
  world/          { *.md ; sim/ }        # from sim/world/, sim/thread/
  _cross/                        # scale-spanning substrate (mirrors the ID system's IN lane)
    { key_substrate, propagation_spec, holonic_doctrine, scale_transitions,
      player_agency, clocks/tracks, narrative_engine ; sim/ ← sim/substrate/, sim/cross_scale/ (⊘ §5) }
  ui/                            # UI/UX (RULED: under systems)
```

**`sim/` disposition (RULED):** `mc_v18.py` (the Monte-Carlo driver) → `engine/`; every scale-specific subpackage (`sim/personal`, `sim/provincial`, `sim/territory`, `sim/thread`, `sim/world`) → `systems/<scale>/<system>/sim/`; the cross-scale substrate (`sim/substrate`, `sim/cross_scale`) → `systems/_cross/sim/` **or** `engine/` (⊘ §5).

---

## §3 — Migration risk (why this is not `git mv`)

CLAUDE.md is emphatic that paths and names are load-bearing (~16k citations, `canonical_sha__*` pins, co-file pairs). A top-level move breaks, non-exhaustively:
- `references/canonical_sources.yaml` SHA pins + `references/module_contracts.yaml` `doc:` paths
- `tools/workplan_status.py` `RELEVANT_PREFIXES`; `tools/audit_staleness.py` `artifact_paths`; `tools/dashboard_data.py`; `.github/workflows/dashboard.yml` + `audit-refresh.yml` path filters; `.githooks/` + `tools/valoria_local.py`
- `references/audit_registry.jsonl` + `references/apparatus_registry.yaml` path fields
- thousands of in-doc `designs/scene/… §x` citations and every co-file `*_index.md`/`*_infill.md` pair
- moving `sim/` splits an import graph — `mc_v18` imports the per-scale subpackages, so the `engine/` ↔ `systems/*/sim/` split needs the Python import paths rewritten together, not folder-by-folder

So the migration needs **tooling, not moves**: a path-rewrite pass (with an alias/redirect map), a citation-rewrite pass, an import-rewrite pass for the sim split, a CI-path update, and a co-file-pair integrity re-check — sequenced so CI stays green at every step. This is a real `IN`-lane cross-cutting project. Its size is exactly why it never self-started.

---

## §4 — Phased migration plan (cheapest / highest-value first)

Each phase is independently mergeable and leaves CI green. **None executes until §5's remaining forks are ruled and sequencing is approved.**

1. **P0 — Registers out of `canon/`** (#10). Highest value, lowest blast radius (ledgers cited by ID, not path). → `registers/`; update `tools/` ledger readers (`obs_core.py`, `currency_consistency_check.py`, `validate_ed_citations.py`, `ci_audit_registry_check.py`) + workflow/hook path refs. Ship a path-map + CI green-check.
2. **P1 — Promote the easy primaries** (#6, #8, and the RULED calls): `designs/workplans`→`workplans/`, `designs/proposals`→`proposals/`, `designs/arcs`+`references/arc_register*`→`arcs/`, `docs/dashboard`→`dashboard/`, `references/historical`→`research/`, `skills`+`tools`→`infrastructure/`. Mostly moves + path refs.
3. **P2 — Collapse duplicate homes** (#5, #7): merge `designs/{videogame,godot}` + the strategy doc (`designs/audit/2026-06-10-godot-conversion-strategy/`) into the `godot/` primary; sigma-leverage armature docs → `systems/_cross/`; empty shells → `deprecated/`.
4. **P3 — `engine/` assembly** (RULED): `sim/mc_v18.py` + `params/` + `references/engine_params/` → `engine/`. Rewrite `mc_v18`'s imports in lockstep with P4's per-scale sim moves.
5. **P4 — `systems/` by scale + intra-system sim** (the big one, §2a). Rehome `designs/{scene,personal,provincial,territory,world,architecture,threadwork,npcs,articulation,factions,ui}` → `systems/`, and distribute `sim/`'s per-scale subpackages into each system's `sim/` subfolder. Requires the full citation- + import-rewrite tools. Do last.
6. **P5 — `tests/` disentangle + `audits/` lifecycle + `archives/`→`deprecated/`** (#1, #4, #9). Keep executable `tests/valoria/`; relocate the ~95% narrative prose to `deprecated/content/` or `audits/`. Introduce the audit promotion rule + a CI gate (a `*workplan*`/reconciliation artifact under `audits/` fails — the §3-rule violation found this session).

---

## §5 — Forks — resolved vs still HELD-BACK

**RULED 2026-07-15 (direct Jordan input) — settled, folded into §2/§2a above:**
- `arcs/` → its own primary.
- `proposals/` → its own primary.
- `research/` → its own primary.
- `ui/` → under `systems/`.
- `params/` → `engine/`.
- `sim/` split: `mc_v18` (Monte-Carlo) → `engine/`; each scale's sim → `systems/<scale>/<system>/sim/`.
- Intra-`systems/` layout: design `.md` at each system's root + a `sim/` subfolder for its scripts.
- `godot/` → its own primary (the port is **not** under `engine/`; the three current Godot homes consolidate here).

**Still HELD-BACK (needs Jordan):**
1. **`engine/` remaining scope** — the typed **`engine_params/`** exports live under `engine/` (recommended: yes); does the **cross-scale sim** (`sim/substrate`, `sim/cross_scale`) go to `engine/` or `systems/_cross/sim/`?
2. **`registers/` vs `continuity/`** — do handoffs (prose) live with the ledgers (data), or separately?
3. **`mechanics_index.yaml`** — register (→`registers/`) or canon-derived index (stays near `canon/`)?
4. **`systems/` scale roster + names** — confirm the axis and exact names (e.g. `scenes/` vs `scene/`), and where threadwork (spans scales → `world/`? `_cross/`?) and factions (`provincial/`? `_cross/`?) sit.
5. **`audits/` lifecycle rule** — the exact promotion marker + the staleness/misfile CI gate.
6. **Sequencing** — approve the P0→P5 order (P0 first recommended as a scoped proof-of-tooling), or re-prioritize.
